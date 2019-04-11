# IM REST Report V2

## 消息历史

目前只保存最近60天消息，这类 API 地址统一为（注意与 Push API 不同）：**https://report.im.jpush.cn/v2**
相比于V1 V2改进了整体查询的稳定性以及速度，提高查询一页的数量上限

### HTTP 验证

验证采用 HTTP Basic 机制，即 HTTP Header（头）里加一个字段（Key/Value对）：
Authorization: Basic base64_auth_string
其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)
即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>使用此接口，传递给JMessage的URL需要经过URL Encode处理，例如时间格式中的空格需要被转义为 %20</p>
</div>

<br/>


## 获取消息




```
GET  /messages?count=1000&begin_time={begin_time}&end_time={end_time}

```

### Example Request 

####  Request Header  

```
GET /messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 (第一次请求)
```

```
GET /messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body  

N/A

####  Request Params  

+ count （必填）每次查询的总条数  一次最多1000
+ begin_time (必填) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss  设置筛选条件大于等于begin time   
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件小于等于end time   
+ begin_time end_time 之间最大范围不得超过7天
	 	cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重新通过第一个请求获得cursor，重新遍历)
+ 查询的消息按发送时间升序排序

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

## 获取用户消息

```
GET /users/{username}/messages?count=1000&begin_time={begin_time}&end_time={end_time}
```
### Example Request 

####  Request Header  

```
GET /users/caiyh/messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 （ 第一次请求）
```

```
GET /users/{username}/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body  

N/A

####  Request Params  
+ count （必填）查询的总条数  一次最多1000
+ begin_time (必填) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss 设置筛选条件大于begin time   
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件小于end time   
+ begin_time end_time 之间最大范围不得超过7天
+ cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重新通过第一个请求获得cursor，重新遍历)
+ 查询的消息按发送时间升序排序

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


## 获取群组消息 

```
GET /groups/{gid}/messages?count=1000&begin_time={begin_time}&end_time={end_time}
```
### Example Request 

####  Request Header  

```
GET /groups/10055201/messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 （ 第一次请求）
```

```
GET /groups/10055201/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body  

N/A

####  Request Params  
+ count （必填）查询的总条数  一次最多1000
+ begin_time (必填) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss 设置筛选条件大于begin time   
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件小于end time   
+ begin_time end_time 之间最大范围不得超过7天
+ cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重新通过第一个请求获得cursor，重新遍历)
+ 查询的消息按发送时间升序排序

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

## 获取聊天室消息 

```
GET /chatrooms/{chatroomid}/messages?count=100&begin_time={begin_time}&end_time={end_time}
```
### Example Request 

####  Request Header  

```
GET /chatrooms/{chatroomid}/messages?count=100&begin_time=2017-11-02 10:10:10&end_time=2017-11-02 10:10:12 （ 第一次请求）
```

```
GET /chatrooms/{chatroomid}/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body  

N/A

####  Request Params  
+ count （必填）查询的总条数  一次最多1000
+ begin_time (必填) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss 设置筛选条件大于begin time   
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件小于end time   
+ begin_time end_time 之间最大范围不得超过7天
+ cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重新通过第一个请求获得cursor，重新遍历)
+ 查询的消息按发送时间升序排序

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


# 统计接口 （vip专属接口）

## 用户统计 

```
GET /statistic/users?time_unit={time_unit}&start={start}&duration={duration}
```
### Example Request 

####  Request Header  

```
GET /statistic/users?time_unit=DAY&start=2017-03-01&duration=3
```


#### Request Body  

N/A

####  Request Params  
+ time_unit （必填）查询维度 目前只有 DAY  
+ start (必填)  开始时间 time_unit 为DAY的时候格式为yyyy-MM-dd 
+ duration (必填)   请求时的持续时长，DAY 最大为60天
+ 统计只保存最近60天的记录

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

+ active_user ：活跃用户数
+ total_users ：总用户数
+ send_msg_users ：发送了消息的用户数
+ new_user ：新增用户数



## 消息统计 

```
GET /statistic/messages?time_unit={time_unit}&start={start}&duration={duration}
```
### Example Request 

####  Request Header  

```
GET /statistic/messages?time_unit=DAY&start=2017-03-01&duration=2
```


#### Request Body  

N/A

####  Request Params  
+ time_unit （必填）查询维度 目前有 HOUR  DAY  MONTH 三个维度可以选
+ start (必填) 开始时间 time_unit 为 HOUR时 格式为yyyy-MM-dd HH ,DAY的时候格式为yyyy-MM-dd , MONTH的时候格式为 yyyy-MM 
+ duration (必填)   请求时的持续时长 HOUR 只支持查询当天的统计， DAY 最大为60天 ，MOTH为两个月  
+ 统计只保存最近60天的记录

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

+ send_msg_stat : 发送消息统计
+ send_msg_stat->group_send_msg : 群组发送消息数
+ send_msg_stat->single_send_msg : 单聊发送消息数
+ group_msg_stat ：群组消息类型统计
+ group_msg_stat->txt_msg : 群组文本消息条数
+ group_msg_stat->image_msg : 群组图片消息条数
+ group_msg_stat->voice_msg : 群组语音消息条数
+ group_msg_stat->other_msg : 群组其他类型消息条数
+ single_msg_stat ：单聊消息类型统计
+ single_msg_stat->txt_msg : 单聊文本消息条数
+ single_msg_stat->image_msg : 单聊图片消息条数
+ single_msg_stat->voice_msg : 单聊语音消息条数
+ single_msg_stat->other_msg : 单聊其他类型消息条数


## 群组统计 

```
GET /statistic/groups?time_unit={time_unit}&start={start}&duration={duration}
```
### Example Request 

####  Request Header  

```
GET /statistic/groups?time_unit=DAY&start=2017-03-01&duration=3
```


#### Request Body  

N/A

####  Request Params  
+ time_unit （必填）查询维度 目前只有 DAY  
+ start (必填)  开始时间 time_unit 为DAY的时候格式为yyyy-MM-dd
+ duration (必填)   请求时的持续时长，DAY 最大为60天
+ 统计只保存最近60天的记录

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

+ active_group ：活跃群组数
+ total_groups ：总群组数
+ send_msg_users ：发送了消息的用户数
+ new_groups ：新增群组数

## 参考

- 老版 REST REPORT API：[REST REPORT API V1](./rest_api_im_report)