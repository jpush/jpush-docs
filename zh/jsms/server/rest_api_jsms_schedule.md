# JSMS Schedule API <small>v1</small>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 16px 16px;">
<ul style="margin-bottom: 0;margin-top: 8px;">
<li>API 层面支持定时功能</li>
</ul>
</div>
</br>


## 单条定时短信提交API
### 功能说明

- 提交单条模板短信定时发送任务。

### 调用地址

- POST https://api.sms.jpush.cn/v1/schedule

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/schedule -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "mobile": "13812345678",
    "temp_id": 1250,
    "temp_para": {
        "number": "741627"
    }
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|发送时间，格式为yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|
|temp_para|TRUE|模板参数,需要替换的参数名和value的键值对|

### 返回示例

#### 请求成功

```json
{"schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e"}
```

#### 请求失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

<br/>  
## 定时短信查询API
### 功能说明

- 查询模板短信定时发送任务。

### 调用地址

- GET https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### 请求示例

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### 返回示例

#### 请求成功

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "send_time": "2017-07-01 09:00:00",
    "temp_id": 1250,
    "recipients": [
        {
            "msg_id": "274887115920",
            "mobile": "13812345678",
            "temp_para": {
                "number": "741627"
            }
        }
    ]
}
```

#### 请求失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

<br/>  
## 单条定时短信修改API
### 功能说明

- 修改单条模板短信定时发送任务。

### 调用地址

- PUT https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### 请求示例

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "mobile": "13812345678",
    "temp_id": 1250,
    "temp_para": {
        "number": "741627"
    }
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|发送时间，格式为yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|
|temp_para|TRUE|模板参数,需要替换的参数名和value的键值对|

### 返回示例

#### 请求成功

```json
{"schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e"}
```

#### 请求失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```  

<br/>  
## 定时短信删除API
### 功能说明

- 删除模板短信定时发送任务。

### 调用地址

- DELETE https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### 请求示例

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### 返回示例

#### 请求成功

```json
HTTP/1.0 200
  Content-Type: application/json
  Content-Length: 0
```

#### 请求失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```
  
<br/>  
<br/>
## 返回码
|HTTP CODE| CODE| CONTENT  | DESC|
|:--- |:--- |:--- |:----
|200|50000|success|请求成功
|400|50001|missing auth|auth 为空
|401|50002|auth failed|auth 鉴权失败
|400|50003|missing body|body 为空
|400|50004|missing mobile|手机号为空
|400|50005|missing  temp_id|模版ID 为空
|403|50006|invalid mobile|手机号无效
|403|50007|invalid body|body 无效
|403|50008|no sms code auth|没有短信业务权限
|403|50009|out of freq|发送超频
|403|50013|invalid temp_id|模版ID 无效
|403|50014|no money|余额不足
|404|50016|api not found|API 不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常|
|403|50020|template auditing|模板审核中
|403|50021|template not pass|模板审核不通过
|403|50022|parameters not all replaced|模板中参数未全部替换|
|403|50023|parameters is empty|参数为空|
|403|50024|unsubscribed mobile|手机号已退订|
|403|50025|wrong template type|该API不支持此模版类型|
|403|50027|invalid send_time|send_time为空或在当前时间之前|
|403|50028|invalid schedule_id|schedule_id无效|
|403|50029|wrong schedule status|定时短信已发送或已删除，无法再修改|