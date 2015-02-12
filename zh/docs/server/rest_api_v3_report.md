# Report API V3
JPush Report API V3 提供各类统计数据查询功能。

这类 API 地址统一为（注意与 Push API 不同）：https://report.jpush.cn

### API 访问鉴权

使用 Basic Authorization 方式认证。了解详情请参考相关规范文档：[HTTP基本认证](http://zh.wikipedia.org/zh/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81)。

具体体现为，HTTP Header 里有一个属性 Authorization，其内容为：Basic base64_auth_string

+ base64_auth_string 生成规则是：base64(appKey:masterSecret);
+ 留意 appKey 与 masterSecret 中间使用 ":" 冒号隔开。

###  送达统计

Received API 以 msg_id 作为参数，去获取该 msg_id 的送达统计数据。

如果一次 API 调用推送有很多对象（比如广播推送），则此 API 返回的统计数据会因为持续有客户端送达而持续增加。

每条推送消息的送达统计数据最多保留一个月。即发起推送请求后从最后一个推送送达记录时间点开始保留一个月，如果保留期间有新的送达，将在这个新送达的时间点起再往后保留一个月。

#### Resource

GET /v3/received

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


### 消息统计（VIP专属接口）

与“送达统计” API 不同的是，该 API 提供更多的针对一个 msgid 的统计数据。

#### Resource
GET /v3/messages

#### Example Request

```
curl -v https://report.jpush.cn/v3/messages?msg_ids=269978303 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
  
> GET /v3/messages?msg_ids=269978303 HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

#### Request Params
+ msg_ids 逗号隔开的多个消息ID。

#### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
[
  {"android":
      {"received":1,"target":4,"online_push":1,"click":null
  },
   "ios":
      {"apns_sent":2,"apns_target":2,"click":null},
   "msg_id":269978303
  }
]

```

#### Response Params

JSON Array
+ msg_id 查询的消息ID
+ android Android统计数据
	+ target 推送目标数
	+ online_push 在线推送数
	+ received 推送送达数
	+ click 用户点击数
+ ios iOS统计数据
	+ apns_target APNs通知推送目标数
	+ apns_sent APNS通知成功推送数
	+ click 用户点击数



### 用户统计（VIP专属接口）

提供近2个月内某时间段的用户相关统计数据：新增用户、在线用户、活跃用户。

时间单位支持：HOUR（小时）、DAY（天）、MONTH（月）。

#### Resource
GET /v3/users

#### Example Request

```
curl -v "https://report.jpush.cn/v3/users?time_unit=DAY&start=2014-06-10&duration=3" -u "dd1066407b044738b6479275:2b38ce69b1de2a7fa95706ea"

> GET /v3/users?time_unit=DAY&start=2014-06-10&duration=3 HTTP/1.1
> Authorization: Basic ZGQxMDY2NDA3YjA0NDczOGI2NDc5Mjc1OjJiMzhjZTY5YjFkZTJhN2ZhOTU3MDZlYQ==
```

#### Request Params
+ time_unit 时间单位。有三个取值：
	+ HOUR 小时
	+ DAY 天
	+ MONTH 月
+ start 起始时间。
	+ 如果单位是小时，则起始时间是小时（包含天），格式例：2014-06-11 09
	+ 如果单位是天，则起始时间是日期（天），格式例：2014-06-11
	+ 如果单位是月，则起始时间是日期（月），格式例：2014-06
+ duration 持续时长。
	+ 如果单位是天，则是持续的天数。以此类推。
	+ 只支持查询60天以内的用户信息，对于time_unit为HOUR的，只支持输出当天的统计结果。

#### Example Response
```
< HTTP/1.1 200 OK
<
{"time_unit":"DAY","start":"2014-06-10","duration":3,"items":[{"time":"2014-06-10"},{"time":"2014-06-11","android":{"active":1}},{"time":"2014-06-12","android":{"active":1,"online":2}}]}
```

#### Response Params
JSON Object
+ time_unit 请求时的时间单位。
+ start 请求时的起始时间。
+ duration 请求时的持续时长。
+ items 获取到的统计数据项。是一个 JSON Array。
	+ new 新增用户
	+ online 在线用户
	+ active 活跃用户


###HTTP 返回码

参考文档：[HTTP-Status-Code](../http_status_code)

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

#### 错误码定义

| Code | 描述	| 详细解释 |
| ---- | ---- | ---- |
|10|系统内部错误||
|2003   |无权使用此接口|| 
|3001	|HTTP Basic authorization 失败。|请参考 API 文档相关说明|
|3002	|msg_ids 参数不存在	 |
|3004	|time_unit与start参数值不匹配|
|3005   |只支持查询60天以内的用户信息|


