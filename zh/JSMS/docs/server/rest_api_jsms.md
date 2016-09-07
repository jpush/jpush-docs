# SMS Code API <small>v1</small>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>发送短信验证码</li>
<li>验证短信验证码</li>
<li>使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；</li>
<li>内容完全使用 JSON 的格式；</li>
</ul>
</div>
</br>
## 发送验证码API


### 功能说明

- 向手机号下发短信验证码。

### 调用地址

- POST https://api.sms.jpush.cn/v1/codes

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"mobile":"xxxxxxxxxxx","temp_id":1}'

```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|手机号码|
|temp_id|TRUE|模板ID|

### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"msg_id":"06890980-6789-4054-bba9-90fb66ab2fce"}

```

### 调用验证

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)


即:对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

## 验证API

### 功能说明

- 验证短信验证码是否有效。

### 调用地址

- POST https://api.sms.jpush.cn/v1/codes/{msg_id}/valid
(注:msg_id为调用发送验证码API的返回值)

### 请求示例

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes/06890980-6789-4054-bba9-90fb66ab2fce/valid -d '{"code":"123456"}'

```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|code|TRUE|验证码|

### 返回示例

- 验证通过

```
    {
        "is_valid":true
    }

```
    
- 验证不通过

```
    {
        "is_valid":false,
        "error":{
            "code":***,//具体对照返回码表
            "message":"***"
        }
    }
```

## 返回码

|HTTP CODE| CODE| CONTENT  | DESC|
|:--- |:--- |:--- |:----
|200|50000|success|请求成功
|400|50001|missing auth|auth为空
|401|50002|auth failed|auth鉴权失败
|400|50003|missing body|body为空
|400|50004|missing mobile|mobile为空
|400|50005|missing  temp_id|temp_id为空
|403|50006|invalid mobile|mobile无效
|403|50007|invalid body|body无效
|403|50008|no sms code auth|没有短信验证权限
|403|50009|out of freq|发送超频
|403|50010|invalid code|验证码无效
|403|50011|expired code|验证码过期
|403|50012|verified code|验证码已验证过
|403|50013|invalid temp_id|无效temp_id
|403|50014|no money|余额不足
|400|50015|missing code|验证码为空
|404|50016|api not found|api不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常|

