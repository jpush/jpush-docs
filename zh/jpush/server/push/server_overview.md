# 服务端 REST API 概述

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; ">
<p>特别提示：建议不要在客户端直接调用 Rest API。JPush 私密信息容易因此暴露给他人，得到 Appkey 和 MasterSecret 信息的人可能进行恶意的推送。
<br>
<p>建议的使用方式是：调用 JPush Rest API 的代码放在开发者应用服务器上。开发者应用服务器对自己的客户端提供接口，开发者服务器收到来自客户端的请求后再调极光的 API 。
</div>


JPush 提供遵从 REST 规范的 HTTP API，以供开发者远程调用 JPush 提供的服务。

与此同时，为方便开发者使用 JPush API，还提供[多种常用编程语言的开发包（SDK）](../../resources/#sdk_1)。


## REST API 基本约束

* API 被设计为符合 HTTP，REST 规范。例如：查询请求使用 Get 方法，提交请求使用 Post 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
* 如无特殊说明，调用参数值应转码为：UTF-8，[URL 编码](http://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)。
* API 请求有[频率限制](#api_1)。
* API 请求有[黑名单机制](#blacklist)。

## API 资源列表
<div class="table-d" align="center" >
        <table border="1" width = "100%">
                <tr  bgcolor="#D3D3D3" >
                        <th>名称</th>
                        <th>资源</th>
                        <th>Base URL</th>
                        <th>描述</th>
                </tr>
                <tr >
                        <td>[REST API v3 - Push](rest_api_v3_push)</td>
                        <td>POST /v3/push</td>
                        <td>https://api.jpush.cn</td>
                        <td>推送消息 API</td>
                </tr>
                <tr >
                        <td>[REST API v3 - Report](rest_api_v3_report)</td>
                        <td>GET /v3/received</td>
                        <td>https://report.jpush.cn</td>
                        <td>获取统计数据</td>
                </tr>
                <tr >
                        <td>[REST API v3 - Devices](rest_api_v3_device)</td>
                        <td>/v3/devices</td>
                        <td>https://device.jpush.cn</td>
                        <td>操作 tag, alias </td>
                </tr>
        </table>
</div>


## 鉴权方式

极光 REST API 采用 [HTTP 基本认证](http://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81) 的验证方式。

基本作法为，HTTP Header（头）里加 Authorization：

    Authorization: Basic ${base64_auth_string}

Header 名称是 "Authorization"，值是 base64 转换过的 "username:password" 对（中间有个冒号）。在JPush API 的场景里，username 是 appKey，密码是 masterSecret。这二者可以在 JPush Web 控制台应用设置中查看。
即，上述 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

### 鉴权举例

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



## API 频率控制

JPush API 对访问次数，具有频率控制。即一定的时间窗口内，API 允许调用的次数是有限制的。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>请注意:
	<br>
	<p>API 频率有限制，不意味着对终端用户的推送数量与速度有控制。简单地说，一次 API 调用可以是广播，推送送达你应用的所有用户。
</div>


### 频率定义

一个时间窗口内，当前定义为：1 分钟。每个 AppKey 的 API 调用数量。

免费版本各 API 频率如下表：
<div class="table-d" align="center" >
        <table border="1" width = "100%">
                <tr  bgcolor="#D3D3D3" >
                        <th>API 类型</th>
                        <th>频率（次/分钟）</th>
                </tr>
                <tr >
                        <td>[Push API v3](rest_api_v3_push)</td>
                        <td>600</td>
                </tr>
                <tr >
                        <td>[Report-API](rest_api_v3_report)</td>
                        <td>2400</td>
                </tr>
                <tr >
                        <td>[Device-API](rest_api_v3_device)</td>
                        <td>600</td>
                </tr>
        </table>
</div>

收费版本根据终端用户规模的不同，具有不同级别的频率。如有需要，请[联系商务](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)。

### 获取频率信息

所有的 HTTP API Response Header 里都加了三项频率控制信息：

+ X-Rate-Limit-Quota：当前 AppKey 一个时间窗口内可调用次数
+ X-Rate-Limit-Remaining：当前时间窗口剩余的可用次数
+ X-Rate-Limit-Reset：距离时间窗口重置剩余的秒数

### 超出频率限制

当一个请求遇到频率限制时，JPush API 返回的 HTTP 返回码为 429，其含义是：太多的请求。
此时返回内容里，是如下的信息：

	{
	  "error": {
	       "code": 2002, 
	       "message": "Rate limit exceeded"
	   }
	}

### 频率优化建议

+ 均匀地分布请求到各时间窗口
+ 根据 alias 大量请求时，避免无效的 alias。
+ 如果大量针对 alias，registrationId 的请求内容一致，可以每次调用可以填写多个接收者。具体请参考推送 API 说明。




## BlackList 黑名单

如果某应用被认为是恶意推送，或者其 API 调用非法，其 AppKey 会被加入黑名单。
加入黑名单的 AppKey 的 API 调用，都会被直接拒绝，其返回码为 403（请求被拒绝）。返回内容格式为：

	{
	  "error": {
	       "code": 2003,
	       "message": "The appKey is in black list."
	   }
	}

如果您的应用被加入黑名单，请发邮件到 [support@jpush.cn](mailto:support@jpush.cn) 以进一步沟通协调。

## 参考

+ [HTTP 错误码 429  - WikiPedia 定义](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)
+ [Twitter API 频率控制定义](https://developer.twitter.com/en/docs/basics/rate-limiting)

