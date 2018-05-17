# IM REST Report V2

## Message history

Currently, only the last 60 days of messages are saved. Addresses of The APIs are unified (note that unlike the Push API): https://report.im.jpush.cn/v2 ,which improves the stability and speed of the overall query compared to V1 V2, and also increases the maximum number of pages for a query

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
GET  /messages?count=1000&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 (第一次请求)
```

```
GET /messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body

+ N/A

#### Request Params

+ count (required): The total number of entries per query. Up to 1000 at a time
+ begin_time (required): Start time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition greater than or equal to the begin time
+ end_time (required): End time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition smarter or equal to end time
+ The maximum range between begin_time end_time must not exceed 7 days.
+ cursor: If there is data after the first request, it will return a cursor to get the following message (valid time of cursor is 120s. Need to re-pass the first request cursor after it is expired)
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
    "total": 3000, "cursor":"APSK234ASDKQWE", "count": 1,
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
GET /users/{username}/messages?count=1000&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /users/caiyh/messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 （ 第一次请求）
```

```
GET /users/{username}/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body

+ N/A

#### Request Params

+ Query messages are sorted in ascending order by sending time
+ count (required): The total number of entries per query. Up to 1000 at a time
+ begin_time (required): Start time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition greater than or equal to the begin time
+ end_time (required): End time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition smarter or equal to end time
+ The maximum range between begin_time end_time must not exceed 7 days.
+ cursor: If there is data after the first request, it will return a cursor to get the following message (valid time of cursor is 120s. Need to re-pass the first request cursor after it is expired)
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
  "total": 3000, "cursor":"APSK234ASDKQWE", "count": 1,
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

## Get group messages

```
GET /groups/{gid}/messages?count=1000&begin_time={begin_time}&end_time={end_time}
```
### Example Request

#### Request Header

```
GET /groups/10055201/messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 （ 第一次请求）
```

```
GET /groups/10055201/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body

+ N/A

#### Request Params

+ count (required): The total number of entries per query. Up to 1000 at a time
+ begin_time (required): Start time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition greater than or equal to the begin time
+ end_time (required): End time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition smarter or equal to end time
+ The maximum range between begin_time end_time must not exceed 7 days.
+ cursor: If there is data after the first request, it will return a cursor to get the following message (valid time of cursor is 120s. Need to re-pass the first request cursor after it is expired)
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
    "total": 1,
    "cursor": "02838264C47BA022DE545AF2D013B59A",
    "count": 1,
    "messages": [
        {
            "set_from_name": 1,
            "from_platform": "a",
            "target_name": "",
            "msg_type": "text",
            "version": 1,
            "target_id": "10055201",
            "from_appkey": "4f7aef34fb361292c566a1cd",
            "from_name": "custom name nnn",
            "from_id": "ppppp",
            "msg_body": {
                "text": "hehe",
                "extras": {}
            },
            "create_time": 1490930940,
            "from_type": "user",
            "target_appkey": "",
            "target_type": "group",
            "msgid": 287090485,
            "msg_ctime": 1490930941708,
            "msg_level": 0
        }
    ]
}
```

## Get chat room messages

```
GET /chatrooms/{chatroomid}/messages?count=100&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /chatrooms/{chatroomid}/messages?count=100&begin_time=2017-11-02 10:10:10&end_time=2017-11-02 10:10:12 （ 第一次请求）
```

```
GET /chatrooms/{chatroomid}/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body

+ N/A

#### Request Params

+ count (required): The total number of entries per query. Up to 1000 at a time
+ begin_time (required): Start time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition greater than or equal to the begin time
+ end_time (required): End time of the record. Format yyyy-MM-dd HH:mm:ss. Set the filter condition smarter or equal to end time
+ The maximum range between begin_time end_time must not exceed 7 days.
+ cursor: If there is data after the first request, it will return a cursor to get the following message (valid time of cursor is 120s. Need to re-pass the first request cursor after it is expired)
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
    "total": 1,
    "cursor": "02838264C47BA022DE545AF2D013B59A",
    "count": 1,
    "messages": [
        {
            "set_from_name": 1,
            "from_platform": "a",
            "target_name": "",
            "msg_type": "text",
            "version": 1,
            "target_id": "10055201",
            "from_appkey": "4f7aef34fb361292c566a1cd",
            "from_name": "custom name nnn",
            "from_id": "ppppp",
            "msg_body": {
                "text": "hehe",
                "extras": {}
            },
            "create_time": 1490930940,
            "from_type": "user",
            "target_appkey": "",
            "target_type": "chatroom",
            "msgid": 287090485,
            "msg_ctime": 1490930941708,
            "msg_level": 0
        }
    ]
}
```

# Statistics interface (vip exclusive interface)

## User Statistics

```
GET /statistic/users?time_unit={time_unit}&start={start}&duration={duration}
```

### Example Request

#### Request Header

```
GET /statistic/users?time_unit=DAY&start=2017-03-01&duration=3
```

#### Request Body

+ N/A

#### Request Params

+ time_unit (required): query dimension, currently only DAY
+ start (required): The starting time, time_unit is DAY when the format is yyyy-MM-dd
+ duration (required): The duration of the request, up to 60 days for DAY
+ Statistics only save records for the last 60 days

### Example Response

#### Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

#### Response Data

```
[
    {
        "active_users": 29,
        "total_users": 66938,
        "send_msg_users": 7,
        "new_users": 2,
        "date": "2017-03-01"
    },
    {
        "active_users": 29,
        "total_users": 66941,
        "send_msg_users": 10,
        "new_users": 3,
        "date": "2017-03-02"
    },
    {
        "active_users": 22,
        "total_users": 66943,
        "send_msg_users": 3,
        "new_users": 2,
        "date": "2017-03-03"
    }
]
```

+ active_user： active users
+ total_users： total users
+ send_msg_users： number of users who sent the message
+ new_user： new users

## Message Statistics

```
GET /statistic/messages?time_unit={time_unit}&start={start}&duration={duration}
```

### Example Request

#### Request Header

```
GET /statistic/messages?time_unit=DAY&start=2017-03-01&duration=2
```

#### Request Body

+ N/A

#### Request Params

+ time_unit (required): query dimension. There are currently three dimensions of HOUR, DAY, MONTH to choose from
+ start (required:) Start time. Format is yyyy-MM-dd HH when time_unit is HOUR, yyyy-MM-dd when time_unit is DAT, and yyyy-MM when time_unit is MONTH.
+ duration (required): duration of the request. HOUR only supports statistics for the day of the query, maximum for DAY is 60 days, MONTH is two months
+ Statistics only save records for the last 60 days

### Example Response

#### Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

#### Response Data

```
{
    "send_msg_stat": [
        {
            "time": "2017-03-01",
            "group_send_msg": 89,
            "single_send_msg": 170916
        },
        {
            "time": "2017-03-02",
            "group_send_msg": 306,
            "single_send_msg": 170944
        },
        {
            "time": "2017-03-03",
            "group_send_msg": 71,
            "single_send_msg": 170782
        }
    ],
    "group_msg_stat": {
        "txt_msg": 425,
        "image_msg": 39,
        "voice_msg": 1,
        "other_msg": 1
    },
    "single_msg_stat": {
        "txt_msg": 512633,
        "image_msg": 7,
        "voice_msg": 1,
        "other_msg": 1
    }
}
```

+ send_msg_stat : statistics of sending message
+ send_msg_stat->group_send_msg : 群组发送消息数number of group send messages
+ send_msg_stat->single_send_msg : 单聊发送消息数number of single chat messages
+ group_msg_stat ：群组消息类型统计group message type statistics
+ group_msg_stat->txt_msg : 群组文本消息条数number of group text messages
+ group_msg_stat->image_msg : 群组图片消息条数number of group image messages
+ group_msg_stat->voice_msg : 群组语音消息条数number of group voice messages
+ group_msg_stat->other_msg : 群组其他类型消息条数number of other types of messages in the group
+ single_msg_stat ：单聊消息类型统计single chat message type statistics
+ single_msg_stat->txt_msg : 单聊文本消息条数The number of single-talk text messages
+ single_msg_stat->image_msg : 单聊图片消息条数Number of single chat picture messages
+ single_msg_stat->voice_msg : 单聊语音消息条数number of single chat voice messages
+ single_msg_stat->other_msg : 单聊其他类型消息条数single chat other types of messages

## Group Statistics

```
GET /statistic/groups?time_unit={time_unit}&start={start}&duration={duration}
```

### Example Request

#### Request Header

```
GET /statistic/groups?time_unit=DAY&start=2017-03-01&duration=3
```

#### Request Body

+ N/A

#### Request Params

+ time_unit (required): query dimension, currently only DAY
+ start (required)：starting time, format is yyyy-MM-dd when time_unit is DAY
+ duration (required): duration of the request, up to 60 days for DAY
+ Statistics only save records for the last 60 days

### Example Response

#### Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

#### Response Data

```
[
    {
        "date": "2017-03-01",
        "active_group": 5,
        "total_group": 5,
        "new_group": 3
    },
    {
        "date": "2017-03-02",
        "active_group": 9,
        "total_group": 9,
        "new_group": 2
    },
    {
        "date": "2017-03-03",
        "active_group": 3,
        "total_group": 3,
        "new_group": 0
    }
]
```

+ active_user：active users
+ total_users： total users
+ send_msg_users ： number of users who sent the message
+ new_user： new users
