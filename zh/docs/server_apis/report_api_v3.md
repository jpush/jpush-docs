# Report API v3
这是 Push API 最新的版本。在 v3 新版本启用后，原 v2 版本不再维护，会继续支持运行一段时间。

相比 API v2 版本，v3 版本的改进为：

+ 完全基于 https，不再提供 http 访问；
+ 使用 HTTP  Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl, 浏览器插件等；
+ 推送内容完全使用 JSON 的格式；
+ 支持的功能有所改进：支持多 tag 的与或操作；可单独发送通知或自定义消息，也可同时推送通知与自定义消息; windows phone 目前只有通知。

## 推送概述
### 功能说明

向某单个设备或者某设备列表推送一条通知、或者消息。

## 请求示例

推送的内容是 JSON 结构，其中包含平台信息，推送目标，通知内容，消息内容与可选参数。

调用地址

POST [https://api.jpush.cn/v3/push](https://api.jpush.cn/v3/push)

###请求示例
	curl -X POST -v https://api.jpush.cn/v3/push -H "Content-type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush!"}}'
	
	> POST /v3/push HTTP/1.1
	> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
	
### 返回示例
	
	< HTTP/1.1 200 OK
	< Content-Type: application/json
	<{"sendno":"18","msg_id":"1828256757"}

## 调用验证

HTTP Header（头）里加一个字段（Key/Value对）：

	Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。


## 推送对象

一个推送对象，以 JSON 格式表达，包含一条推送相关的所有信息，最多包含以下五个方面：

关键字	     |               | 含义
------------ | ------------- | ------------
platform	 | 必填	          | 推送平台设置
audience	 | 必填	          | 推送设备指定
notification | 可选		      | 通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存
options	     | 可选		      | 推送参数
message	     | 可选		      | 消息内容体。是被推送到客户端的内容。与 notification 一起二者  必须有其一，可以二者并存

	{
		"platform": "all",
		"audience" : {
			"tag" : ["深圳", "北京"]
		},
		"notification" : {
			"alert" : "Hi, JPush!",
		    "android" : {},
		    "ios" : {
		    	"extras" : { "newsid" : 321}
		    }
		},
		"options" : {
			"time_to_live" : 60
		}
	}
	
### platform


### audience
### notification
### message
### options
## 调用返回

### HTTP 状态码

参考文档：HTTP-Status-Code

### 业务返回码
Code	     |               | 含义
------------ | ------------- | ------------
platform	 | 必填	          | 推送平台设置


## 其他参考

