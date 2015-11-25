# MessageList 消息列表

目前只保存最近30天消息，这类 API 地址统一为（注意与 Push API 不同）：**https://report.im.jpush.cn/v1**

## GetMessage 获取消息

**注意**

使用此接口，传递给JPush的URL需要经过URL Encode处理，例如时间格式中的空格需要被转义为 %20

```
GET /messages?&start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header 

```
GET /messages?start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

#### Request Body

N/A

#### Request Params 

+ start （必填）查询的起始纪录
+ count （必填）查询的总条数  一次最多500
+ begin_time (可选) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss
+ end_time (可选)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss

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
          "version": 1
        },  
 	] 
} 
```

<<!--

## GetUserMessage 获取用户消息

```
GET /messages/users/{username}?filter={filter}&start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /messages/users/caiyh?filter={filter}&start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

#### Request Body

N/A

#### Request Params

+ filter （可选）send ，rev 。send表示查询用户发出的消息，rev表示用户收到的消息，filter不填表示用户的所有消息
+ start （必填）查询的起始纪录
+ count （必填）查询的总条数  一次最多500
+ begin_time (可选) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss
+ end_time (可选)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss

### Example Response

#### Response Header

```
HTTP/1.1 200 
Content-Type: application/json; charset=utf-8 
```

#### Response Data

```
{ "total": 3000,  "start": 0,  "count": 1,  "messages": [ {{ "target_type": "single",  "msg_type": "text",  "target_name": "",  "target_id": "10010648",  "from_id": "868802000386631",  "from_name": "868802000386631",  "from_type": "user",  "from_platform": "a",  "msg_body": {"text": "text",  "extras": { } }, "create_time": 1446016259,  "version": 1 } ] }
```

## GetGroupMessage 群组消息列表

```
GET /messages/groups/{gid}?start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request

#### Request Header

```
GET /messages/groups/100000000?&start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```
#### Request Body

N/A

#### Request Params

+ start （必填）查询的起始纪录
+ count （必填）查询的总条数 一次最多500
+ begin_time (可选) 记录开始时间 格式 yyyy-MM-dd HH:mm:ss
+ end_time (可选)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss

### Example Response

#### Response Header

```
HTTP/1.1 200 
Content-Type: application/json; charset=utf-8 
```

#### Response Data

```
{ "total": 3000,  "start": 0,  "count": 1, 
"messages": [ { "target_type": "group",  "msg_type": "text",  "target_name": "",  "target_id": "10010648",  "from_id": "868802000386631",  "from_name": "868802000386631",  "from_type": "user",  "from_platform": "a",  "msg_body": { "text": "text",  "extras": { } }, "create_time": 1446016259,  "version": 1 } ] }
```

-->