# 服务器端 SDK

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



<!--服务SDK，基于多种服务器端编程语言，封装了REST API，简化了开发者调用远程 API 来推送消息的难度。

我们提供的开发包，编程语言类别上有限。如果不在您想要的范围内，请尝试直接基于 API 定义来进行开发，或者使用参考第三方提供的 SDK或者代码片断。

### 官方维护更新

| 开发语言 | 最近更新 | 项目地址 | 下载链接 |
| ------- | ------ | ------- | ------------- | ------------- |
| Java | v3.0.1 支持 Push API v3 | [https://github.com/jpush/jpush-api-java-client](https://github.com/jpush/jpush-api-java-client) |  |
| PHP | v3.0.0 支持 Push API v3 | [https://github.com/jpush/jpush-api-php-client](https://github.com/jpush/jpush-api-php-client) | |
| Python | v3.0.0 支持 Push API v3  | [https://github.com/jpush/jpush-api-python-client](https://github.com/jpush/jpush-api-python-client) |  | 
| Node.js | | [https://github.com/jpush/jpush-api-nodejs-client](https://github.com/jpush/jpush-api-nodejs-client) | |
| Ruby | | [https://github.com/jpush/jpush-api-ruby-client](https://github.com/jpush/jpush-api-ruby-client) | |
| C# | | [https://github.com/jpush/jpush-api-csharp-client](https://github.com/jpush/jpush-api-csharp-client) | | 


### 第三方提供（代码）

* PHP library (v2)

由网站作者 夜阑小雨 共享在其个人网站上  
链接：http://www.yelanxiaoyu.com/code/phonegap%E5%BC%80%E5%8F%91/jpush_push_php_server.html

* C API demo (v2)

由微博用户 @火星上的骑士 共享在 github 上  
链接：https://github.com/issacsonjj/JPushDemo

* .net (v2)

https://jpush.codeplex.com/
-->

