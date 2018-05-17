# IM REST Report

<div style="font-size:13px;background: #F0E68C;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 10px; padding-bottom: 0;margin-bottom: 0;">
<p>
  Special note: There is a limit on the number of data obtained by the v1 version. This version will no longer provide new features and will only maintain problems caused by bugs. Please update to the v2 version as soon as possible.
</p>
</div>

## Message History

Currently, only the last 60 days of messages are saved. Addresses of these APIs are unified (note that unlike the Push API)：https://report.im.jpush.cn/v1

### HTTP Authentication

Authentication uses the HTTP Basic mechanism, that is, a field (Key/Value pair) Authorization: Basic base64_auth_string is added in the HTTP Header (header). The generation algorithm of base64_auth_string is: base64(appKey:masterSecret) That is, adding a colon to appKey, plus masterSecret Assembled strings, and then do a base64 conversion.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Tips：</p>
<p>
The URL passed to the JMessage via this interface needs to be processed by the URL Encode, for example, spaces in the time format need to be escaped as %20.
</p>
</div>

## Get Message

```
GET /messages?&start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /messages?start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

#### Request Body

+ N/A

#### Request Params

+ start (required): the starting record of the query
+ count (required): the total number of queries, up to 1000 at a time
+ begin_time (optional): record of starting time. Format yyyy-MM-dd HH:mm:ss. Set filtering condition greater than or equal to beginning time. Not take effect if not set.
+ end_time (optional): record of ending time. Format yyyy-MM-dd HH:mm:ss. Set filtering condition less than or equal to ending time. Not take effect if not set.
+ If neither ending time or beginning time is set, both conditions are not valid, and then query all messages stored on the server.
+ Queried messages are sorted in ascending order by sending time

### Example Response

#### Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

#### Response Data

```
{
    "total": 3000, "start": 0, "count": 1,
    "messages": [
        { "target_type": "single",
          "msg_type": "text",
          "target_name": "",
          "target_id": "10010648",
          "from_id": "868802000386631",
          "from_name": "868802000386631",
          "from_type": "user",
          "from_platform": "a",
          "msg_body": {
                 "text": "text",
                 "extras": { }
          },
          "create_time": 1446016259,
          "version": 1,
          "msgid": 13242735,
          "msg_level" : 0, // 0代表应用内消息 1代表跨应用消息
          "msg_ctime" : 1466866468352 // 服务器接收到消息的时间，单位毫秒
        }
    ]
}
```

## Get user messages

```
GET /users/{username}/messages?start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /users/caiyh/messages?start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

#### Request Body

+ N/A

#### Request Params

+ start (required): the starting record of the query
+ count (required): the total number of queries, up to 1000 at a time
+ begin_time (optional): record of starting time. Format yyyy-MM-dd HH:mm:ss. Set filtering condition greater than or equal to beginning time. Not take effect if not set.
+ end_time (optional): record of ending time. Format yyyy-MM-dd HH:mm:ss. Set filtering condition less than or equal to ending time. Not take effect if not set.
+ If neither ending time or beginning time is set, both conditions are not valid, and then query all messages stored on the server.
+ The URL passed to the JMessage via this interface needs to be processed by the URL Encode, for example, spaces in the time format need to be escaped as %20.
+ Queried messages are sorted in ascending order by sending time

### Example Response

#### Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

#### Response Data

```
{
  "total": 3000, "start": 0, "count": 1,
  "messages": [
        { "target_type": "single",
          "msg_type": "text",
          "target_name": "",
          "target_id": "10010648",
          "from_id": "868802000386631",
          "from_name": "868802000386631",
          "from_type": "user",
          "from_platform": "a",
          "from_appkey": "4f7aef34fb361292c566a1cd",
          "target_appkey": "4f7aef34fb361292c566a1cd",
          "msg_body": {
                 "text": "text",
                 "extras": { }
          },
          "create_time": 1446016259,
          "version": 1 ,
          "msgid": 13242735,
          "msg_level" : 0 // 0代表应用内消息 1代表跨应用消息
          "msg_ctime" : 1466866468352 // 服务器接收到消息的时间，单位毫秒
        }
 ]
}
```
