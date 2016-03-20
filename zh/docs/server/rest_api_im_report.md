# MessageList 消息列表

目前只保存最近60天消息，这类 API 地址统一为（注意与 Push API 不同）：**https://report.im.jpush.cn/v1**

### HTTP 验证

[Authorization 用户认证](../server/server_overview/#authorization)

##GetMessage 获取消息

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>使用此接口，传递给JPush的URL需要经过URL Encode处理，例如时间格式中的空格需要被转义为 %20</p>
</div>

<br/>


```
GET /messages?&start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

### Example Request 

####  Request Header  

```
GET /messages?start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

#### Request Body  

N/A

####  Request Params  

+ start （必填）查询的起始纪录
+ count （必填）查询的总条数  一次最多500
+ begin_time (可选) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss  设置筛选条件大于等于begin time 不设置不生效  
+ end_time (可选)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss  设置筛选条件下于等于end time   不设置不生效
+ end time begin time 都不设置的话 说明两个条件都不生效，则查询服务端保存的所有消息
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
          "msgid": 13242735
        }
 	] 
} 
```
