<h1> MessageList 消息列表</h1>

目前只保存最近30天消息，这类 API 地址统一为（注意与 Push API 不同）：**https://report.im.jpush.cn/v1**

<h2> GetMessage 获取消息</h2>

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>使用此接口，传递给JPush的URL需要经过URL Encode处理，例如时间格式中的空格需要被转义为 %20</p>
</div>

<br/>


```
GET /messages?&start=0&count=500&begin_time={begin_time}&end_time={end_time}
```

<h3> Example Request</h3>

<h4> Request Header </h4>

```
GET /messages?start=0&count=500&begin_time=2015-11-02 10:10:10&end_time=2015-11-02 10:10:12
```

<h4> Request Body </h4>

N/A

<h4> Request Params </h4>

+ start （必填）查询的起始纪录
+ count （必填）查询的总条数  一次最多500
+ begin_time (可选) 记录开始时间 格式  yyyy-MM-dd HH:mm:ss
+ end_time (可选)   记录结束时间  格式 yyyy-MM-dd HH:mm:ss

<h3> Example Response </h3>

<h4> Response Header  </h4>

```
HTTP/1.1 200 
Content-Type: application/json; charset=utf-8 
```

<h4> Response Data </h4>

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
