# 短信模板 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>支持创建、修改、查询和删除短信模板</li>
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
## 创建模板 API
### 功能说明

- 创建短信模板

### 调用地址

- POST https://api.sms.jpush.cn/v1/templates

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/templates -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "template": "您好，您的验证码是{{code}}，2分钟内有效！",
    "type": 1,
    "ttl": 120,
    "remark": "此模板用于用户注册"
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|template|TRUE|模板内容<br>1. 短信内容不超过350个字，短信内容包括：签名、正文、退订方式（仅营销短信），创建模版时请预留签名等文字的字数<br>2. 验证码模版仅支持设置一个变量，且变量名必须为 code<br>3. 通知、营销短信中，变量名仅支持英文及数字，若含有链接变量，变量名必须为 url ，为避免短信发送时因进入人工审核而导致发送延迟，请在 remark 参数中填写链接以报备，支持不设置参数|
|type|TRUE|模板类型，1为验证码类，2为通知类，3为营销类|
|ttl|FALSE|验证码有效期，必须大于 0 且不超过 86400 ，单位为秒（当模板类型为1时必传）|
|remark|FALSE|请简略描述正文模版的发送场景及发送对象，不超过100字|

### 返回示例

#### 请求成功

```json
{"temp_id": 37582}
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
## 修改模板 API
### 功能说明

- 修改审核不通过的模板，并再次提交审核

### 调用地址

- PUT https://api.sms.jpush.cn/v1/templates/{temp_id}

### 请求示例

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "temp_id": 37582,
    "template": "您好，您的验证码是{{code}}，5分钟内有效！",
    "type": 1,
    "ttl": 300,
    "remark": "此模板用于用户注册"
}'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|temp_id|TRUE|模板ID|
|template|TRUE|模板内容<br>1. 短信内容不超过350个字，短信内容包括：签名、正文、退订方式（仅营销短信），创建模版时请预留签名等文字的字数<br>2. 验证码模版仅支持设置一个变量，且变量名必须为 code<br>3. 通知、营销短信中，变量名仅支持英文及数字，若含有链接变量，变量名必须为 url ，为避免短信发送时因进入人工审核而导致发送延迟，请在 remark 参数中填写链接以报备，支持不设置参数|
|type|TRUE|模板类型，1为验证码类，2为通知类，3为营销类|
|ttl|FALSE|验证码有效期，必须大于 0 且不超过 86400 ，单位为秒（当模板类型为1时必传）|
|remark|FALSE|请简略描述正文模版的发送场景及发送对象，不超过100字|

### 返回示例

#### 请求成功

```json
{"temp_id": 37582}
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
## 查询模板 API
### 功能说明

- 查询短信模板

### 调用地址

- GET https://api.sms.jpush.cn/v1/templates/{temp_id}

### 请求示例

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### 返回示例

#### 请求成功

```json
{
    "temp_id": 37582,
    "template": "您好，您的验证码是{{code}}，5分钟内有效！",
    "type": 1,
    "ttl": 300,
    "remark": "此模板用于用户注册",
    "status": 1     // 状态，0为审核中，1为审核通过，2为审核不通过
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
## 删除模板 API
### 功能说明

- 删除短信模板

### 调用地址

- DELETE https://api.sms.jpush.cn/v1/templates/{temp_id}

### 请求示例

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
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
|:--- |:--- |:--- |:----|
|200|50000|success|请求成功|
|400|50001|missing auth|auth 为空|
|401|50002|auth failed|auth 鉴权失败|
|400|50003|missing body|body 为空|
|403|50007|invalid body|body 无效|
|403|50008|no sms code auth|未开通短信业务|
|403|50013|invalid temp_id|模版ID 无效|
|404|50016|api not found|API 不存在|
|415|50017|media not supported|媒体类型不支持|
|405|50018|request method not support|请求方法不支持|
|500|50019|server error|服务端异常|
|403|50025|wrong template type|错误的模板类型|
|403|50037|has black word|模板内容含有敏感词|
|403|50041|invalid ttl value|验证码有效期无效，ttl 参数值必须大于 0 并且不超过 86400 |
|403|50042|template is empty|模板内容为空|
|403|50043|template too long|模板内容过长，短信内容不超过350个字，短信内容包括：签名、正文、退订方式（仅营销短信），创建模版时请预留签名等文字的字数|
|403|50044|template parameter invalid|模板参数无效|
|403|50045|remark too long|备注内容过长，长度限制为500字符|
|403|50046|signature not set|该应用未设置签名，请先设置签名|
|403|50047|modify template not allow|只有审核不通过状态的模板才允许修改|
|403|50052|template contains special symbol|模板不能含有特殊符号，如【】|
|403|50053|special template parameter need extra remark for confirmation|模板中存在链接变量，请在 remark 参数中填写链接以报备，避免短信发送时因进入人工审核而导致发送延迟|