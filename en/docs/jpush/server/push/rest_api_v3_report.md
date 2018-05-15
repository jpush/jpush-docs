# Report API <small>v3</small>

## Overview

JPush Report API V3 provides the query functions of statistical data in various types.


### Call Address

https://report.jpush.cn/v3

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>If the created Jiguang application is allocated to the Beijing computer room and the API caller's server is also located in Beijing, it is more suitable to call the API of the Jiguang Beijing computer room, which can improve the response speed.</p>
<p>The room where the application is located can be seen through Application Settings -> Application Info of the Jiguang Web Console. If the application locates in the Beijing computer room, the calling address of each API will be given at the same time.</p>
<p>Call address of Push API in Beijing computer room: https://bjapi.push.jiguang.cn/v3/report </p>
<p>For the detailed mapping relationship, see the "Server Location" information in "Application Information".</p>
</div>

## Service Statistics

The Received API takes msg_id as a parameter to obtain delivery statistics for this msg_id.
If there are many objects pushed by an API call (such as broadcast push), the statistics returned by this API will continue to increase because of persistent client deliveries.
Delivery statistics for each push message last up to one month. That is, after the initiation of the push request, the statistics will be reserved for one month from the time point of the last push delivery record. If there is a new delivery during the retention period, it will be held for one month from the time of the new delivery.

### Call Address

GET /received

**Request Example**

```
curl -v https://report.jpush.cn/v3/received?msg_ids=1613113584,1229760629 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"

< GET /v3/received?msg_ids=1613113584,1229760629 HTTP/1.1
< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

* list of msg_ids returned by push API. Multiple msg_ids are separated by commas. Up to 100 msg_ids are supported.

### Return Example

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

* android_received: Android delivery. Null if there is no such data
* ios_apns_sent iOS: Notifications pushed to APNs successfully. Null if there is no such data.
* ios_apns_received: iOS notification delivered to the device. Null if there is no item data. For statistics, please refer to [Advanced Features](../../client/iOS/ios_guide_new/#_9) in Integration Guide.
* ios_msg_received: Number of iOS custom message delivery. Null if there is no such data.
* wp_mpns_sent: winphone notification delivery. Null if there is no such data.

## Inquiry of Service Status

Status API is used to query the delivery status of a pushed message on a group of devices.

### Call Address

POST /status/message

**Request Example**

```
curl --insecure -X POST -v https://report.jpush.cn/v3/status/message -H "Content-Type: application/json" -u "29ea851419f747be7b5785a0:79f486970ec5c41bfe381bc3" -d '{ "msg_id": 327640176, "registration_ids":["1506bfd3a7c568d4761", "02078f0f1b8", "0207870a9b8"]}'

> POST /v3/status/message HTTP/1.1
> Host: report.jpush.cn
> Authorization: Basic MjllYTg1MTQxOWY3NDdiZTdiNTc4NWEwOjc5ZjQ4Njk3MGVjNMM0MWJmZTM4MWJjMw==
```

**Request Params**

JSON Object

* msg_id must be passed. For message id, one call only supports one message id query.
* registration_ids must be passed. JSON Array types. Multiple registration ids are separated by commas, and up to 1000 can be invoked at a time.
* Data is optional. For the specified date of the query, the format is yyyy-mm-dd and the default is the same day

## Return Example

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

**Meaning of Status**：

* 0: delivered；
* 1: not delivered；
* 2: registration_id does not belong to the application；
* 3: registration_id belongs to the application, but it is not the target of the message；
* 4: The system is abnormal.。

## Message Statistics (VIP Exclusive Interface)

Unlike the "Delivery Statistics" API, this API provides more statistics for a msgid.

If you need to open this interface, please contact: [Business Service](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### Call Address

GET /messages

**Request Example**

```
curl -v https://report.jpush.cn/v3/messages?msg_ids=269978303 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"

> GET /v3/messages?msg_ids=269978303 HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

**Request Params**

* msg_ids: Multiple msg_ids separated by commas, up to 100 msg_ids are supported.

### Return Example

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

* msg_id: Message ID queried
* android: Android statistics
    * target: Number of push target
    * online_push: Number of online push
    * received: Number of push delivery
    * click: Number of user clicks
    * msg_click: Number of custom message hits
* ios: iOS statistics
    * apns_target: Number of APNs notification push target
    * apns_sent: Number of APNS notifications pushed successfully
    * apns_received: Number of APNs notifications sent. For statistics, refer to Advanced Features in Integration Guide
    * click: User clicks
    * target: Number of custom message push target
    * received: Number of custom message delivery
* winphone: Winphone statistics
    * mpns_target: Number of MPNs notification push target
    * mpns_sent: Number of MPNS notifications successfully pushed
    * click: Number of User clicks

## User Statistics (VIP Exclusive Interface)

Provide user-related statistics for a period of time within the last 2 months: new users, online users, and active users.
Time unit supports: HOUR (hours), DAY (days), MONTH (months).

If you need to open this interface, please contact: [Business Service](https://www.jiguang.cn/accounts/business/form)

### Call Address

GET /users

**Request Example**

```
curl -v "https://report.jpush.cn/v3/users?time_unit=DAY&start=2014-06-10&duration=3" -u "dd1066407b044738b6479275:2b38ce69b1de2a7fa95706ea"

> GET /v3/users?time_unit=DAY&start=2014-06-10&duration=3 HTTP/1.1
> Authorization: Basic ZGQxMDY2NDA3YjA0NDczOGI2NDc5Mjc1OjJiMzhjZTY5YjFkZTJhN2ZhOTU3MDZlYQ==
```

**Request Params**

* time_unit: There are three values：
    * HOUR
    * DAY
    * MONTH
* start
    * If the unit is hour, the start time is hour (including days). Format example: 2014-06-11 09
    * If the unit is day, the start time is the date (day), format example: 2014-06-11
    * If the unit is month, the start time is the date (month), format example: 2014-06
* duration
    * If the unit is days, it is the number of days that it lasts. And so on.
    * Only support query of user information within 60 days. For time_unit as HOUR, only output the statistical results of the day.

### Return Example

```
< HTTP/1.1 200 OK
<
{"time_unit":"DAY","start":"2014-06-10","duration":3,"items":[{"time":"2014-06-10"},{"time":"2014-06-11","android":{"active":1}},{"time":"2014-06-12","android":{"active":1,"online":2}}]}
```

**Response Params**

JSON Object

* time_unit: The time unit of the request
* start: The start time of the request.
* duration: The duration of the request
* items: Acquired statistics items, which is a JSON Array.
    * new: new users
    * online: online users
    * active: active users

## Error Code

### Definition of Error Code

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
        <th>Code</th>
        <th>Description</th>
        <th>Detailed Explanation</th>
    </tr><tr>
        <td>10</td>
        <td>Internal System Error</td>
        <td>Internal System Error</td>
    </tr><tr>
        <td>2003</td>
        <td>Not authorized to use this interface</td>
        <td>Must correct</td>
    </tr><tr>
        <td>3001</td>
        <td>Basic authorization of HTTP failed</td>
        <td>Please refer to the API documentation for instructions</td>
    </tr><tr>
        <td>3004</td>
        <td>Parameter value of Time_unit does not match start’s</td>
        <td>Must correct</td>
    </tr><tr>
        <td>3005</td>
        <td>Only support user information within 60 days</td>
    </tr>
  </table>
</div>

### Return Example

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

Reference documents: [HTTP-Status-Code](http_status_code)
