# REST API概述
## 概述

JPush 提供遵从 REST 规范的 HTTP API，为开发者远程使用 JPush 提供的服务。

## 基本约束

* API 被设计为符合 HTTP, REST 规范。例如：查询请求使用 Get 方法，提交请求使用 Post 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
* 如无特殊说明，调用参数值应转码为：UTF-8, [URL Encoded。](http://en.wikipedia.org/wiki/Percent_encoding)
* API 请求有[频率限制。](../api_rate_limiting)
* API 请求有黑名单机制。
* [API 调试指南](../api_debug_guide)
## REST API 资源列表

| 名称 | 	资源 | Base URL	 |描述|
| ------------ | ------------- | ------------ |----------------|
| [Push API v2](../push_api_v2)  | POST /v2/push	  | http://api.jpush.cn:8800<p>https://api.jpush.cn | 推送消息或通知|
| [Push API v3](../push_api_v3)	 | POST /v3/push  | https://api.jpush.cn | 推送 |
| [Report-API](../report_api)		 | GET /v2/received  | https://report.jpush.cn | 获取统计数据 - 消息送达 |

## 黑名单

如果某应用被认为是恶意推送，或者其 API 调用非法，其 AppKey 会被加入黑名单。

加入黑名单的 AppKey 的 API 调用，都会被直接拒绝，其返回码为 403（请求被拒绝）。返回内容格式为：

	{
	  "error": {
	       "code": 2002, 
	       "message": "The appKey is in black list."
	   }
	}
 
如果您的应用被加入黑名单，请发邮件到 <support@jpush.cn> 以进一步沟通协调。
