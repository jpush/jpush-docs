# IM REST Report V2

## MessageList 消息历史

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


## GetMessage 获取消息




```
GET  /messages?count=1000&begin_time={begin_time}&end_time={end_time}&cursor=${cursor}

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
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件下于等于end time   
+ begin_time end_time 之间最大范围不得超过7天
+ 	cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重第一个请求获取，重新遍历)
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

##  GetUserMessage 获取用户消息

```
GET /users/{username}/messages?count=1000&begin_time={begin_time}&end_time={end_time}
```
### Example Request 

####  Request Header  

```
GET /users/caiyh/messages?count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12 （ 第一次请求）
```

```
GET /v2/users/{username}/messages?cursor=KSDKF34UISOCGAASD （第n次获取 n>1）
```

#### Request Body  

N/A

####  Request Params  
+ count （必填）查询的总条数  一次最多1000
+ begin_time (必填) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss 设置筛选条件大于end time   
+ end_time (必填)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件下于begin time   
+ begin_time end_time 之间最大范围不得超过7天
+ cursor  当第一次请求后如果后面有数据，会返回一个cursor回来用这个获取接下来的消息 (cursor 有效时间是120s，过期后需要重第一个请求获取，重新遍历)
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


