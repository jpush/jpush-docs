# 短信发送 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>支持发送文本、语音验证码短信</li>
<li>支持验证验证码</li>
<li>支持发送单条、批量模板短信</li>
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
## 发送文本验证码短信 API
### 功能说明

- 发送文本验证码短信

### 调用地址

- POST https://api.sms.jpush.cn/v1/codes

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"mobile":"xxxxxxxxxxx","temp_id":*}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|

### 返回示例

#### 发送成功

```
{"msg_id": "288193860302"}
```
#### 发送失败

```
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

<br/>
## 发送语音验证码短信 API
### 功能说明

- 发送语音验证码短信

### 调用地址

- POST https://api.sms.jpush.cn/v1/voice_codes

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/voice_codes -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"mobile":"xxxxxxxxxxxxxx", "ttl":60}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|手机号码|
|code|FALSE|语音验证码的值，验证码仅支持 4-8 个数字|
|voice_lang|FALSE|语音验证码播报语言选择，0：中文播报，1：英文播报，2：中英混合播报|
|ttl|FALSE|验证码有效期，默认为60秒|

### 返回示例

#### 发送成功

```
{"msg_id": "288193860302"}
```

#### 发送失败

```
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

<br/>
## 验证码验证 API
### 功能说明

- 验证验证码是否有效

### 调用地址

- POST https://api.sms.jpush.cn/v1/codes/{msg_id}/valid (注:msg_id为调用发送验证码API的返回值)  

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes/288193860302/valid -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"code":"123456"}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|code|TRUE|验证码|

### 返回示例

#### 验证通过

```
{
    "is_valid": true
}
```
    
#### 验证不通过

```
{
    "is_valid": false,
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

<br/>
## 发送单条模板短信 API
### 功能说明

- 发送单条模板短信

### 调用地址

- POST https://api.sms.jpush.cn/v1/messages

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/messages -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" \
-d '{"mobile":"xxxxxxxxxxxxxx","temp_id":1,"temp_para":{"xxxx":"xxxx"}}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|
|temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

### 返回示例

#### 发送成功

```json
{"msg_id": 288193860302}
```

#### 发送失败

```json
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

<br/>
## 发送批量模板短信 API
### 功能说明

- 发送批量模板短信

### 调用地址

- POST https://api.sms.jpush.cn/v1/messages/batch

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/messages/batch -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
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
|temp_id|TRUE|模板ID|
|recipients|TRUE|接收者列表|
|recipients.mobile|TRUE|手机号码|
|recipients.temp_para|FALSE|模板参数,需要替换的参数名和 value 的键值对|

### 返回示例

#### 发送成功

```json
{
    "success_count": 1,
    "failure_count": 1,
    "recipients": [
        {
            "msg_id": "274887115920",
            "mobile": "13812345678"
        },
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "msg_id": "275421247364",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
}
```

#### 发送失败

```json
{
    "error": {
        "code": *****,
        "message": "******"
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
|403|50009|out of freq|发送超频
|403|50010|invalid code|验证码无效
|403|50011|expired code|验证码过期
|403|50012|verified code|验证码已验证通过
|403|50013|invalid temp_id|模版ID 无效
|403|50014|no money|可发短信余量不足
|400|50015|missing code|验证码为空
|404|50016|api not found|API 不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常|
|403|50020|template auditing|模板审核中
|403|50021|template not pass|模板审核未通过
|403|50022|parameters not all replaced|模板中参数未全部替换|
|403|50023|parameters is empty|参数为空|
|403|50024|unsubscribed mobile|手机号码已退订|
|403|50025|wrong template type|该 API 不支持此模版类型|
|403|50026|wrong msg_id|msg_id 无效|
|403|50030|recipients is empty|recipients 为空|
|403|50031|too much recipients|recipients 短信接收者数量超过1000|
|403|50034|repeat send|重复发送|
|403|50035|illegal IP|非法 IP 请求|
|403|50036|app in black|应用被列为黑名单|
|403|50037|has black word|短信内容存在敏感词汇|
|403|50038|invalid code length|语音验证码长度错误|
|403|50039|invalid code type|语音验证码内容错误，验证码仅支持数字|
|403|50040|invalid voice language type|语音验证码播报语言类型错误|
|403|50041|invalid ttl value|验证码有效期错误|