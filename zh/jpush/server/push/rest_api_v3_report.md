# Report API <small>v3</small>

## 概述
JPush Report API V3 提供各类统计数据查询功能。  

### 调用地址

https://report.jpush.cn/v3

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">

<p>如果创建的极光应用分配的北京机房，并且 API 调用方的服务器也位于北京，则比较适合调用极光北京机房的 API，可以提升一定的响应速度。</p>
<p>通过极光 Web 控制台 “应用设置” -> "应用信息" 中可以看到应用所在机房。如果应用所在地为北京机房，同时会给出各 API 的调用地址。</p>

<p>北京机房 Push API 调用地址： https://bjapi.push.jiguang.cn/v3/report </p>
<p>详细对应关系见 “应用信息” 中 “服务器所在地” 后的信息。</p>

</div>



##  送达统计（旧）

Received API 以 msg_id 作为参数，去获取该 msg_id 的送达统计数据。  
如果一次 API 调用推送有很多对象（比如广播推送），则此 API 返回的统计数据会因为持续有客户端送达而持续增加。


每条推送消息的送达统计数据最多保留一个月。即发起推送请求后从最后一个推送送达记录时间点开始保留一个月，如果保留期间有新的送达，将在这个新送达的时间点起再往后保留一个月。

### 调用地址

GET /received

### 请求示例

```
curl -v https://report.jpush.cn/v3/received?msg_ids=1613113584,1229760629 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"

< GET /v3/received?msg_ids=1613113584,1229760629 HTTP/1.1
< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

+ msg_ids 推送 API 返回的 msg_id 列表，多个 msg_id 用逗号隔开，最多支持 100 个 msg_id。

### 返回示例

```
< HTTP/1.1 200 OK 
< Content-Type: application/json
< 
[  {"msg_id":"1613113584",
    "android_received":62,
    "ios_apns_sent":11,
    "ios_apns_received":5,
    "ios_msg_received": 3, 
    "wp_mpns_sent" : 3},

   {"msg_id":"1229760629",
    "android_received":56,
    "ios_apns_sent":33,
    "ios_apns_received":17,
    "ios_msg_received": 3,  
    "wp_mpns_sent" : null}
]
```
**Response Params**

JSON Array.

+ android_received Android 送达。如果无此项数据则为 null。
+ ios\_apns_sent iOS 通知推送到 APNs 成功。如果无此项数据则为 null。
+ ios\_apns_received iOS 通知送达到设备。如果无项数据则为 null。统计该项请参考 [集成指南高级功能-通知送达统计](../../client/iOS/ios_guide_new/#_9) 。
+ ios\_msg_received  iOS 自定义消息送达数。如果无此项数据则为 null。
+ wp\_mpns_sent       winphone通知送达。如果无此项数据则为 null。


##  送达统计详情（新）

Received API 以 msg_id 作为参数，去获取该 msg_id 的送达统计数据。  
如果一次 API 调用推送有很多对象（比如广播推送），则此 API 返回的统计数据会因为持续有客户端送达而持续增加。

此接口和“送达统计”旧接口区别在于：此接口会根据消息是通过极光自有通道下发、Android厂商通道下发进行数据统计区分，如果您的应用开通了Android厂商通道支持，建议使用此接口。

每条推送消息的送达统计数据最多保留一个月。即发起推送请求后从最后一个推送送达记录时间点开始保留一个月，如果保留期间有新的送达，将在这个新送达的时间点起再往后保留一个月。

### 调用地址

GET /v3/received/detail

### 请求示例

```
curl -v https://report.jpush.cn/v3/received/detail?msg_ids=1613113584,1229760629 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"

< GET /v3/received/detail?msg_ids=1613113584,1229760629 HTTP/1.1
< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

+ msg_ids 推送 API 返回的 msg_id 列表，多个 msg_id 用逗号隔开，最多支持 100 个 msg_id。

### 返回示例

```
< HTTP/1.1 200 OK 
< Content-Type: application/json
<
[
   {"msg_id":"1613113584",
    "jpush_received":62,
    "android_pns_sent":12,
    "ios_apns_sent":11,
    "ios_apns_received":5,
    "ios_msg_received": 3,
    "wp_mpns_sent" : 3},
 
   {"msg_id":"1229760629",
    "jpush_received":56,
    "android_pns_sent":12,
    "ios_apns_sent":33,
    "ios_apns_received":17,
    "ios_msg_received": 3, 
    "wp_mpns_sent" : null}
]
```
**Response Params**

JSON Array.

+ jpush_received 极光通道用户送达数；包含普通Android用户的通知+自定义消息送达，iOS用户自定义消息送达；如果无此项数据则为 null。
+ android\_pns_sent Android厂商用户推送到厂商服务器成功数，计算方式同 Android厂商成功数；如果无此项数据则为 null。
+ ios\_apns_sent iOS 通知推送到 APNs 成功。如果无此项数据则为 null。
+ ios\_apns_received iOS 通知送达到设备。如果无项数据则为 null。统计该项请参考 [集成指南高级功能-通知送达统计](../../client/iOS/ios_guide_new/#_9) 。
+ ios\_msg_received  iOS 自定义消息送达数。如果无此项数据则为 null。
+ wp\_mpns_sent       winphone通知送达。如果无此项数据则为 null。


## 送达状态查询

Status API 用于查询已推送的一条消息在一组设备上的送达状态。

### 调用地址

POST /status/message

### 请求示例

```
curl --insecure -X POST -v https://report.jpush.cn/v3/status/message -H "Content-Type: application/json" -u "29ea851419f747be7b5785a0:79f486970ec5c41bfe381bc3" -d '{ "msg_id": 327640176, "registration_ids":["1506bfd3a7c568d4761", "02078f0f1b8", "0207870a9b8"]}'

> POST /v3/status/message HTTP/1.1
> Host: report.jpush.cn
> Authorization: Basic MjllYTg1MTQxOWY3NDdiZTdiNTc4NWEwOjc5ZjQ4Njk3MGVjNMM0MWJmZTM4MWJjMw==
```

**Request Params**

JSON Object

+ msg_id 必传。消息 id，一次调用仅支持一个消息 id 查询。
+ registration_ids 必传。JSON Array 类型，多个registration id 用逗号隔开，一次调用最多支持 1000个。
+ date 可选。查询的指定日期，格式为 yyyy-mm-dd，默认为当天。

### 返回示例

**Response Header** 

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
    "02078f0f1b8": {
        "status": 2
    },
    "1507bfd3a7c568d4761": {
        "status": 0
    },
    "0207870a9b8": {
        "status": 2
    }
}
```

**status 含义：**

+ 0: 送达；
+ 1: 未送达；
+ 2: registration_id 不属于该应用；
+ 3: registration_id 属于该应用，但不是该条 message 的推送目标；
+ 4: 系统异常。


## 消息统计（VIP 专属接口，旧）

与“送达统计” API 不同的是，该 API 提供更多的针对一个 msgid 的统计数据。


如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### 调用地址

GET /messages

### 请求示例

```
curl -v https://report.jpush.cn/v3/messages?msg_ids=269978303 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
  
> GET /v3/messages?msg_ids=269978303 HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

+ msg_ids 多个 msg_id 用逗号隔开，最多支持 100 个 msg_id。

### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
[
  {
   "android":
      {"received":1,"target":4,"online_push":1,"click":null,"msg_click":null},

   "ios":
      {"apns_sent":2,"apns_target":2,"apns_received":1,"click":null,"target":10,"received":8},
   
   "winphone":
      {"mpns_target": 100,"mpns_sent": 100,"click": 100,},
   
   "msg_id":"269978303"
  }
]
```

**Response Params**

JSON Array

+ msg_id 查询的消息 ID

+ android Android 统计数据
	+ target 推送目标数
	+ online_push 在线推送数
	+ received 推送送达数
	+ click 用户点击数
	+ msg_click 自定义消息点击数
     
+ ios iOS 统计数据
	+ apns_target APNs通知推送目标数	
	+ apns_sent APNS通知推送成功数	
	+ apns_received APNs 通知送达数 ，统计该项请参考 [集成指南高级功能-通知送达统计](../../client/iOS/ios_guide_new/#_9) 
	+ click 用户点击数
	+ target 自定义消息目标数
	+ received 自定义消息送达数

+ winphone Winphone 统计数据
     + mpns_target MPNs 通知推送目标数
     + mpns_sent    MPNS 通知成功推送数
     + click 用户点击数


## 消息统计详情（VIP 专属接口，新）

与“送达统计” API 不同的是，该 API 提供更多的针对一个 msgid 的统计数据。

与“消息统计” 旧接口相比，此接口获取到的数据更详细，而且如果您的应用开通了Android厂商通道，建议使用此接口。

如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### 调用地址

GET /messages/detail

### 请求示例

```
curl -v https://report.jpush.cn/v3/messages/detail?msg_ids=269978303 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
  
> GET /v3/messages/detail?msg_ids=269978303 HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

+ msg_ids 多个 msg_id 用逗号隔开，最多支持 100 个 msg_id。

### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
[
 {
   "msg_id": 123456789,
   "jpush": {
       "target": 110,
       "online_push": 90,
       "received": 100,
       "click": 80,
       "msg_click":60 
    },
    "android_pns":{
       "pns_target": 100,
       "pns_sent": 100,
       "xm_detail":{
            "target": 2
            "sent": 1
       },
       "hw_detail":{
            "target": 2
            "sent": 1
       },
       "mz_detail":{
            "target": 2
            "sent": 1
       },
       "oppo_detail":{
            "target": 2
            "sent": 1
       },
       "vivo_detail":{
            "target": 2
            "sent": 1
       },
       "fcm_detail":{
            "target": 2
            "sent": 1
       }
    },
    "ios": {
       "apns_target": 100,
       "apns_sent": 100,
       "apns_received": 60,
       "apns_click": 100,
       "msg_target": 80,
       "msg_received": 80
    },
   "winphone": {
      "mpns_target": 100,
      "mpns_sent": 100,
      "click": 100
   }  
 }
]
```

**Response Params**

JSON Array

+ msg_id 查询的消息 ID
+ jpush 极光通道统计数据，走极光通道下发的普通Android用户通知/自定义消息 以及 iOS用户自定义消息总体情况
	+ target 推送目标数
	+ online_push 在线推送数
	+ received 推送送达数
	+ click 用户点击数
	+ msg_click 自定义消息点击数	
+ android_pns Android厂商通道统计数据，走厂商通道下发统计数据
	+ pns_target   通过厂商通道推送目标数
	+ pns_sent     推送到厂商通道成功数
	+ xm_detail    推送到小米通道详情
	    + target  小米用户目标数
	    + sent     推送到小米平台成功数
	+ hw_detail    推送到华为通道详情
	    + target  华为用户目标数
	    + sent     推送到华为平台成功数
	+ mz_detail    推送到魅族通道详情
	    + target  魅族用户目标数
	    + sent     推送到魅族平台成功数
	+ oppo_detail    推送到OPPO通道详情
	    + target  OPPO用户目标数
	    + sent     推送到OPPO平台成功数
	+ vivo_detail    推送都VIVO通道详情
	    + target  VIVO用户目标数
	    + sent     推送到VIVO平台成功数
	+ fcm_detail    推送到FCM通道详情
	    + target  FCM用户目标数
	    + sent     推送到FCM平台成功数     
+ ios iOS 统计数据
	+ apns_target APNs 通知推送目标数	
	+ apns_sent  APNs 通知成功推送数，发送到APNs服务器成功
	+ apns_received APNs 通知送达数，APNs 服务器下发到设备成功，统计该项请参考 [集成指南高级功能-通知送达统计](../../client/iOS/ios_guide_new/#_9) 
	+ apns_click 通知点击数
	+ msg_target 自定义消息目标数
	+ msg_received    自定义消息送达数
+ winphone Winphone 统计数据
     + mpns_target MPNs 通知推送目标数
     + mpns_sent    MPNS 通知成功推送数
     + click  MPNs 通知用户点击数


## 用户统计（VIP 专属接口）

提供近 2 个月内某时间段的用户相关统计数据：新增用户、在线用户、活跃用户。  
时间单位支持：HOUR（小时）、DAY（天）、MONTH（月）。


如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business/form) 

### 调用地址

GET /users

### 请求示例

```
curl -v "https://report.jpush.cn/v3/users?time_unit=DAY&start=2014-06-10&duration=3" -u "dd1066407b044738b6479275:2b38ce69b1de2a7fa95706ea"

> GET /v3/users?time_unit=DAY&start=2014-06-10&duration=3 HTTP/1.1
> Authorization: Basic ZGQxMDY2NDA3YjA0NDczOGI2NDc5Mjc1OjJiMzhjZTY5YjFkZTJhN2ZhOTU3MDZlYQ==
```

**Request Params**

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
	+ 只支持查询 60 天以内的用户信息，对于 time_unit 为 HOUR 的，只支持输出当天的统计结果。

### 返回示例

```
< HTTP/1.1 200 OK
<
{"time_unit":"DAY","start":"2014-06-10","duration":3,"items":[{"time":"2014-06-10"},{"time":"2014-06-11","android":{"active":1}},{"time":"2014-06-12","android":{"active":1,"online":2}}]}
```

**Response Params**

JSON Object

+ time_unit 请求时的时间单位。
+ start 请求时的起始时间。
+ duration 请求时的持续时长。
+ items 获取到的统计数据项。是一个 JSON Array。
  	+ new 新增用户
  	+ online 在线用户
  	+ active 活跃用户



##错误码

### 错误码定义

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >描述</th>
      <th >详细解释</th>
    </tr>
    <tr >
      <td>10</td>
      <td>系统内部错误</td>
      <td>系统内部错误</a></td>
    </tr>
    <tr >
      <td>2003</td>
      <td>无权使用此接口</td>
      <td>必须改正</td>
    </tr>
    <tr >
      <td>3001</td>
      <td>HTTP Basic authorization 失败。</td>
      <td>请检查<a href="https://docs.jiguang.cn/jpush/server/push/server_overview/#_1">调用验证</a>，Appkey 与 MasterSecret 的正确性</td>
    </tr>
    <tr >
      <td>3004</td>
      <td>time_unit 与 start 参数值不匹配</td>
      <td>必须修正</td>
    </tr>
    <tr >
      <td>3005</td>
      <td>只支持查询 60 天以内的用户信息</td>
      <td></td>
    </tr>
  </table>
</div>

### 返回示例

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

参考文档：[HTTP-Status-Code](http_status_code)

