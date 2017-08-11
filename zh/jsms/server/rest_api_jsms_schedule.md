# 短信定时发送 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>支持提交、修改、查询和删除模板短信定时发送任务</li>
</ul>
</div>
</br>
## HTTP 验证
> 使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)，即:对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。appKey、masterSecret 可以在控制台应用设置中查看。

</br>
## 单条定时短信提交 API
### 功能说明

- 提交单条模板短信定时发送任务

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
|send_time|TRUE|发送时间，格式为 yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|
|temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

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
## 批量定时短信提交 API
### 功能说明

- 提交批量模板短信定时发送任务

### 调用地址

- POST https://api.sms.jpush.cn/v1/schedule/batch

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/schedule/batch -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "temp_id": 1250,
    "recipients": [
        {
            "mobile": "13812345678",
            "temp_para": {
                "number": "741627"
            }
        },
        {
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|发送时间，格式为 yyyy-MM-dd HH:mm:ss|
|temp_id|TRUE|模板ID|
|recipients|TRUE|短信接收者列表|
|recipients.mobile|TRUE|手机号码|
|recipients.temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

### 返回示例

#### 请求成功

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "success_count": 1,
    "failure_count": 1,
    "failure_recipients": [
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
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
## 单条定时短信修改 API
### 功能说明

- 修改单条模版短信定时发送任务

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
|send_time|TRUE|发送时间，格式为 yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|
|temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

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
## 批量定时短信修改 API
### 功能说明

- 修改批量模板短信定时发送任务

### 调用地址

- PUT https://api.sms.jpush.cn/v1/schedule/batch/{schedule_id}

### 请求示例

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/schedule/batch/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "temp_id": 1250,
    "recipients": [
        {
            "mobile": "13812345678",
            "temp_para": {
                "number": "741627"
            }
        },
        {
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|发送时间，格式为 yyyy-MM-dd HH:mm:ss|
|temp_id|TRUE|模板ID|
|recipients|TRUE|短信接收者列表|
|recipients.mobile|TRUE|手机号码|
|recipients.temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

### 返回示例

#### 请求成功

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "success_count": 1,
    "failure_count": 1,
    "failure_recipients": [
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
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
## 定时短信查询API
### 功能说明

- 查询模板短信定时发送任务

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
## 定时短信删除 API
### 功能说明

- 删除模板短信定时发送任务

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
## 返回码
|HTTP CODE| CODE| MESSAGE  | DESC|
|:--- |:--- |:--- |:----
|200|50000|success|请求成功
|400|50001|missing auth|auth 为空
|401|50002|auth failed|auth 鉴权失败
|400|50003|missing body|body 为空
|400|50004|missing mobile|手机号码为空
|400|50005|missing  temp_id|模版ID 为空
|403|50006|invalid mobile|手机号码无效
|403|50007|invalid body|body 无效
|403|50008|no sms code auth|未开通短信业务
|403|50013|invalid temp_id|模版ID 无效
|403|50014|no money|可发短信余量不足
|404|50016|api not found|API 不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常|
|403|50020|template auditing|模板审核中|
|403|50021|template not pass|模板审核未通过|
|403|50022|parameters not all replaced|模板中参数未全部替换|
|403|50023|parameters is empty|参数为空|
|403|50024|unsubscribed mobile|手机号码已退订|
|403|50025|wrong template type|该 API 不支持此模版类型|
|403|50026|wrong msg_id|msg_id 无效|
|403|50027|invalid send_time|send_time 为空或在当前时间之前|
|403|50028|invalid schedule_id|schedule_id 无效|
|403|50029|wrong schedule status|定时短信已发送或已删除，无法再修改|
|403|50030|recipients is empty|recipients 为空|
|403|50031|too much recipients|recipients 短信接收者数量超过1000|
|403|50034|repeat send|重复发送|