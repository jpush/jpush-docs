# 服务器端基础

JPush 提供遵从 REST 规范的 HTTP API，以供开发者远程调用 JPush 提供的服务。

与此同时，为方便开发者使用 JPush API，还提供[多种常用编程语言的开发包（SDK）](../server_sdks)。


### REST API 基本约束

* API 被设计为符合 HTTP, REST 规范。例如：查询请求使用 Get 方法，提交请求使用 Post 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
* 如无特殊说明，调用参数值应转码为：UTF-8, [URL Encoded](http://en.wikipedia.org/wiki/Percent_encoding)。
* API 请求有[频率限制](#rate_limiting)。
* API 请求有[黑名单机制](#black_list)。


### REST API 资源列表
<a name="api_resources"></a>

| 名称 | 	资源 | Base URL	 |描述|
| ------------ | ------------- | ------------ |----------------|
| [REST API v3 - Push](../rest_api_v3_push)	 | POST /v3/push  | https://api.jpush.cn | 推送 |
| [REST API v3 - Report](../rest_api_v3_report) | GET /v2/received  | https://report.jpush.cn | 获取统计数据 - 消息送达 |
| [REST API v2 - Push](../rest_api_v2_push)  | POST /v2/push  | http://api.jpush.cn:8800 <br /> https://api.jpush.cn | 推送消息或通知|
| [REST API v2 - Report](../rest_api_v2_report) | GET /v2/received  | https://report.jpush.cn | 获取统计数据 - 消息送达 |

### 黑名单
<a name="black_list"></a>

如果某应用被认为是恶意推送，或者其 API 调用非法，其 AppKey 会被加入黑名单。

加入黑名单的 AppKey 的 API 调用，都会被直接拒绝，其返回码为 403（请求被拒绝）。返回内容格式为：

	{
	  "error": {
	       "code": 2002, 
	       "message": "The appKey is in black list."
	   }
	}
 
如果您的应用被加入黑名单，请发邮件到 <support@jpush.cn> 以进一步沟通协调。

### API 频率控制
<a name="rate_limiting"></a>
JPush API 对访问次数，具有频率控制。即一定的时间窗口内，API 允许调用的次数是有限制的。

#### 频率控制定义

一个时间窗口，当前定义为：1 分钟。

频率控制基于 AppKey 来定义，每个 AppKey 有一个基础的调用频率限制数量。免费版本如下表：

|API 类型|频率（次/分钟）|
|-|-|
|[Push API v2](../push_api_v2)|600|
|[Report-API](../report_api)	|2400|

收费版本根据终端用户规模的不同，具有不同级别的频率。如有需要，请访问 [价格说明](价格说明)了解更多。

####HTTP 请求与响应

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
	       "code": 2001, 
	       "message": "Rate limit exceeded"
	   }
	}
	
##### 避免遭遇频率限制的建议

+ 均匀地分布请求到各时间窗口
+ 根据 alias 大量请求时，避免无效的 alias。
+ 如果大量针对 alias 的请求内容一致，可以每次 API + 调用填写多个 alias 。具体请参考推送 API 说明。


