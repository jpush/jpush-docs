# IM REST API

JPush IM API 为开发者提供 IM 相关功能。

这类 API 地址统一为（注意与 Push API 不同）：https://im.api.jpush.cn

### API 访问鉴权

参考统一文档。

###  用户注册



#### Resource

POST /v1/users/

#### Example Request

```
curl -v https://report.jpush.cn/v3/received?msg_ids=1613113584,1229760629,1174658841,1174658641 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"

< GET /v3/received?msg_ids=1613113584,1229760629,1174658841,1174658641 HTTP/1.1
< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

#### Request Params

+ msg_ids 推送API返回的 msg_id 列表，多个 msg_id 用逗号隔开，最多支持100个msg_id。

#### Example Response

```
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
```
#### Response Params

JSON Array.

+ android_received Android 送达。如果无此项数据则为 null。
+ ios_apns_sent iOS 推送成功。如果无此项数据则为 null。



### HTTP 返回

HTTP 返回码参考文档：[HTTP-Status-Code](../http_status_code)

#### Example Error Response

```
< HTTP/1.1 401 Unauthorized
< Content-Type: application/json
<
{ 
  "error": {
        "code": 3001, 
        "message": "Basic authentication failed"
     }
}
```

#### 业务错误码定义

| Code | 描述	| 详细解释 |
| ---- | ---- | ---- |
|10|系统内部错误||


### 相关文档

+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [JPush IM 指南](../../guideline/jpush_im_guide/)

