# API 频率控制
JPush API 对访问次数，具有频率控制。即一定的时间窗口内，API 允许调用的次数是有限制的。

### 频率控制定义

一个时间窗口，当前定义为：1 分钟。

频率控制基于 AppKey 来定义，每个 AppKey 有一个基础的调用频率限制数量。免费版本如下表：

| API 类型 | 频率（次/分钟）|
| :---| :---|
|[Push API v2](../push_api_v2)|600|
|[Report-API](../report_api)	|2400|

收费版本根据终端用户规模的不同，具有不同级别的频率。如有需要，请访问 [价格说明](价格说明)了解更多。

###HTTP 请求与响应

####响应头

所有的 HTTP API Response Header 里都加了三项频率控制信息：

+ X-Rate-Limit-Limit：当前 AppKey 一个时间窗口内可调用次数
+ X-Rate-Limit-Remaining：当前时间窗口剩余的可用次数
+ X-Rate-Limit-Reset：距离时间窗口重置剩余的秒数

####超出频率限制

当一个请求遇到频率限制时，JPush API 返回的 HTTP 返回码为 429，其含义是：太多的请求。

此时返回内容里，是如下的信息：

	{
	  "error": {
	       "code": 2001, 
	       "message": "Rate limit exceeded"
	   }
	}
	
####避免遭遇频率限制的建议

+ 均匀地分布请求到各时间窗口
+ 根据 alias 大量请求时，避免无效的 alias。
+ 如果大量针对 alias 的请求内容一致，可以每次 API + 调用填写多个 alias 。具体请参考推送 API 说明。

### 外部参考
+ HTTP 错误码关于 429 的定义：[http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)

+ Twitter API 频率控制定义：[https://dev.twitter.com/docs/rate-limiting/1.1](https://dev.twitter.com/docs/rate-limiting/1.1)
