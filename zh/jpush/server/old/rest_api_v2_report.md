# Report API 

Received API 以 msg_id 作为参数，去获取该 msg_id 的送达统计数据。

如果一次 API 调用推送有很多对象（比如广播推送），则此 API 返回的统计数据会因为持续有客户端送达而持续增加。

每条推送消息的送达统计数据最多保留 10 天。即一条消息推送发起 10 天后送达统计将被清除。

###API Endpoint

https://report.jpush.cn

```
(消息)说明：仅支持 https 访问，不支持直接 http 访问。
```

###Resource

GET /v2/received

###Example Request

	curl -v https://report.jpush.cn/v2/received?msg_ids=1613113584,1229760629,1174658841,1174658641 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
	 
	< GET /v2/received?msg_ids=1613113584,1229760629,1174658841,1174658641 HTTP/1.1
	< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==


###Request Params

+ msg_ids 推送API返回的 msg_id 列表，多个 msg_id 用逗号隔开，最多支持100个msg_id。
+ HTTP Header Authorization 的值：Basic base64_auth_string
	+ base64_auth_string 生成规则是：base64(appKey:masterSecret) 
	+ 留意 appKey 与 masterSecret 中间使用 ":" 冒号隔开
	+ 请参考相关规范文档：[HTTP基本认证。](http://zh.wikipedia.org/zh/HTTP基本认证)


###Example Response


	< HTTP/1.1 200 OK 
	< Content-Type: application/json
	< 
	[  {"android_received":62,
	    "ios_apns_sent":11,
	    "msg_id":1613113584},
	   {"android_received":56,
	     "ios_apns_sent":33,
	     "msg_id":1229760629},
	   {"android_received":null,
	    "ios_apns_sent":14,
	    "msg_id":1174658841},
	   {"android_received":32,
	    "ios_apns_sent":null,
	    "msg_id":1174658641}
	]


###Response Params

JSON Array.

+ android_received Android 送达。如果无此项数据则为 null。
+ ios_apns_sent iOS 推送成功。如果无此项数据则为 null。

###Example Error Response

	< HTTP/1.1 401 Unauthorized
	< Content-Type: application/json
	< 
	{
	  "error": {
	        "code": 3001, 
	        "message": "Basic authentication failed"
	     }
	}

###HTTP 返回码

参考文档：[HTTP-Status-Code](http://zh.wikipedia.org/zh/HTTP基本认证)

###错误码定义

| Code | 描述	| 详细解释 |
| ----| ---- | ---- |
|10|系统内部错误||	 
|3001	|HTTP Basic authorization 失败。|请参考 API 文档相关说明
|3002	|msg_ids 参数不存在	 


