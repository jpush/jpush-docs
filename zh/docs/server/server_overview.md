# 服务器端概述

JPush 提供遵从 REST 规范的 HTTP API，以供开发者远程调用 JPush 提供的服务。

与此同时，为方便开发者使用 JPush API，还提供[多种常用编程语言的开发包（SDK）](../../resources/#sdk_1)。


### REST API 基本约束

* API 被设计为符合 HTTP, REST 规范。例如：查询请求使用 Get 方法，提交请求使用 Post 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
* 如无特殊说明，调用参数值应转码为：UTF-8, URL编码 [^1]。
* API 请求有[频率限制](#api-rating)。
* API 请求有[黑名单机制](#blacklist)。

[1]: [URL编码 - WikiPedia定义](http://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

### REST API 资源列表

| 名称 | 	资源 | Base URL	 |描述|
| ------------ | ------------- | ------------ |----------------|
| [REST API v3 - Push](../rest_api_v3_push)	 | POST /v3/push  | https://api.jpush.cn | 推送 |
| [REST API v3 - Report](../rest_api_v3_report) | GET /v3/received  | https://report.jpush.cn | 获取统计数据 - 消息送达 |
| [REST API v3 - Devices](../rest_api_v3_device) | /v3/devices | https://device.jpush.cn | tag,alias 操作 |

以下为老版本 API，仍然可用，但不鼓励使用。

| 名称 | 	资源 | Base URL	 |描述|
| ------------ | ------------- | ------------ |----------------|
| [REST API v2 - Push](../rest_api_v2_push)  | POST /v2/push  | http://api.jpush.cn:8800 <br /> https://api.jpush.cn | 推送消息或通知|
| [REST API v2 - Report](../rest_api_v2_report) | GET /v2/received  | https://report.jpush.cn | 获取统计数据 - 消息送达 |

### Authorization 用户认证

JPush/JMessage REST API 都采用 HTTP基本认证[^2] 的验证方式。

[2]: [HTTP 基本认证 - WikiPedia定义](http://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81)

基本作法为，HTTP Header（头）里加 Authorization：

    Authorization: Basic ${base64_auth_string}

Header 名称是 "Authorization"，值是 base64 转换过的 "username:password" 对（中间有个冒号）。在 JPush API 的场景里，username 是 appKey，密码是 masterSecret。这二者可以在 JPush Web 控制台上生成的应用上获取。

即，上述 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

#### 用户认证举例

你的 appKey 是 "7d431e42dfa6a6d693ac2d04", masterSecret 是 "5e987ac6d2e04d95a9d8f0d1"，则调用 Push API v3 时，使用 curl 命令的话，是这样写：

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json" 
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" 
-d  '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush!"}}'
```

HTTP 请求发出的请求是：

```
> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```


### BlackList 黑名单

如果某应用被认为是恶意推送，或者其 API 调用非法，其 AppKey 会被加入黑名单。

加入黑名单的 AppKey 的 API 调用，都会被直接拒绝，其返回码为 403（请求被拒绝）。返回内容格式为：

	{
	  "error": {
	       "code": 2003, 
	       "message": "The appKey is in black list."
	   }
	}
 
如果您的应用被加入黑名单，请发邮件到 <support@jpush.cn> 以进一步沟通协调。

### API Rating 频率控制

JPush API 对访问次数，具有频率控制。即一定的时间窗口内，API 允许调用的次数是有限制的。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>请注意:
	<br>
	<p>API 频率有限制，不意味着对终端用户的推送数量与速度有控制。简单地说，一次 API 调用可以是广播，推送送达你应用的所有用户。
</div>


#### 频率控制定义

一个时间窗口，当前定义为：1 分钟。

频率控制基于 AppKey 来定义，每个 AppKey 有一个基础的调用频率限制数量。免费版本如下表：

| API 类型                            | 频率（次/分钟） |
|-------------------------------------|-----------------|
| [Push API v3](../rest_api_v3_push)  | 600             |
| [Report-API](../rest_api_v3_report) | 2400            |
| [Device-API](../rest_api_v3_device) | 600            |

收费版本根据终端用户规模的不同，具有不同级别的频率。如有需要，请联系商务，了解更多。

#### HTTP 请求与响应

##### 响应头

所有的 HTTP API Response Header 里都加了三项频率控制信息：

+ X-Rate-Limit-Limit：当前 AppKey 一个时间窗口内可调用次数
+ X-Rate-Limit-Remaining：当前时间窗口剩余的可用次数
+ X-Rate-Limit-Reset：距离时间窗口重置剩余的秒数

##### 超出频率限制

当一个请求遇到频率限制时，JPush API 返回的 HTTP 返回码为 429，其含义是：太多的请求。

此时返回内容里，是如下的信息：

	{
	  "error": {
	       "code": 2002, 
	       "message": "Rate limit exceeded"
	   }
	}
	
##### 避免遭遇频率限制的建议

+ 均匀地分布请求到各时间窗口
+ 根据 alias 大量请求时，避免无效的 alias。
+ 如果大量针对 alias 的请求内容一致，可以每次 API + 调用填写多个 alias 。具体请参考推送 API 说明。


##### 频率控制 - 推送场景举例

A, B 两应用都有千万的用户量。

A 应用推送方式，主要是群发

一次推送（即一次 API 调用）面向大量用户。这种使用广播，或者基于 Tag 做推送。

这种情况下，由于群发几乎不可能短期内推送很多次，从而几乎不可能触发 API 频率控制。

进一步地说，API 频率控制与推送送达的终端用户数无关。一次 API 广播推送，可以送达所有用户。

B 应用推送方式，主要是单点

一次推送（即一次 API 调用）只面向一个用户。这种基于 alias 或者 registrationI 做推送。

由于用户量大，向每个用户推送都需要调用一次 API，则相对比较容易触发到频率控制。

有一个技巧可以减少 API 调用次数：推送 API 支持向 alias, registrationId 推送时，最多一次可以向 1000 个目标对象推送。也就是把推送请求批量化。

但这个作法不好的是：1 批量一起推送到很多对象，需要统一时间；2 批量一起的推送，其内容体只能一样，不能根据每个对象不同。

##### 外部参考

+ [HTTP 错误码 429  - WikiPedia定义](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)
+ [Twitter API 频率控制定义](https://dev.twitter.com/docs/rate-limiting/1.1)

