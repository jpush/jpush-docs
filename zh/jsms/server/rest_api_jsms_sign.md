# 短信签名 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>支持创建、修改、查询和删除短信签名</li>
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
## 创建签名 API
### 功能说明

- 创建短信签名

### 调用地址

- POST https://api.sms.jpush.cn/v1/sign

### 请求示例
请注意，content-type为multipart/form-data的方式。

```
curl -X POST \
  https://api.sms.jpush.cn/v1/sign \
  -u '7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1' \
  -H 'content-type: multipart/form-data' \
  -F 'sign=申请的签名'
  -F 'type=签名类型'
  -F 'remark=申请说明'

```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|sign|TRUE|签名内容|
|type|FALSE|签名类型，填写数字代号即可<br>1:公司名称全称或简称： 需提供营业执照<br>2:工信部备案的网站全称或简称： 需提供主办单位的营业执照<br>3:APP应用全称或简称： 需提供任一应用商店的下载链接及开发者的营业执照<br>4:公众号或小程序名称的全称或简称： 需提供公众号（小程序）主体营业执照<br>5:电商平台店铺全称或简称： 需提供经营者营业执照<br>6:商标名称全称或简称： 需提供商标注册证书<br>7:其他： 需提供所有者营业执照|
|image0|FALSE|请提供签名相关的资质证件图片|
|remark|FALSE|请简略描述您的业务使用场景，不超过100个字|

### 返回示例

#### 请求成功

```json
{"sign_id": 37582}
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
## 修改签名 API
### 功能说明

- 修改审核不通过的签名，并再次提交审核

### 调用地址

- POST https://api.sms.jpush.cn/v1/sign/{sign_id}

### 请求示例

```
curl -X POST \
  https://api.sms.jpush.cn/v1/sign/37582 \
  -u '7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1' \
  -H 'content-type: multipart/form-data' \
  -F 'sign=修改的签名'
  -F 'type=签名类型'
  -F 'remark=业务场景说明'
```

#### 参数

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|sign|TRUE|签名内容|
|type|FALSE|签名类型，填写数字代号即可<br>1:公司名称全称或简称： 需提供营业执照<br>2:工信部备案的网站全称或简称： 需提供主办单位的营业执照<br>3:APP应用全称或简称： 需提供任一应用商店的下载链接及开发者的营业执照<br>4:公众号或小程序名称的全称或简称： 需提供公众号（小程序）主体营业执照<br>5:电商平台店铺全称或简称： 需提供经营者营业执照<br>6:商标名称全称或简称： 需提供商标注册证书<br>7:其他： 需提供所有者营业执照|
|image0|FALSE|请提供签名相关的资质证件图片|
|remark|FALSE|请简略描述您的业务使用场景，不超过100个字|

### 返回示例

#### 请求成功

```json
{"sign_id": 37582}
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
## 查询签名 API
### 功能说明

- 查询短信签名

### 调用地址

- GET https://api.sms.jpush.cn/v1/sign/{sign_id}

### 请求示例

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/sign/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### 返回示例

#### 请求成功

```json
{
    "sign_id": 37582,
    "sign": "极光推送",
    "status": 1, //签名审核状态,1为通过，2为未通过
    "is_default": 1, //签名使用状态，1为默认签名
    "use_status": 1 //签名使用状态，1为使用中，0为未使用
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
## 删除签名 API
### 功能说明

- 删除短信签名

### 调用地址

- DELETE https://api.sms.jpush.cn/v1/sign/{sign_id}

### 请求示例

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/sign/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
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
|404|50016|api not found|API 不存在|
|415|50017|media not supported|媒体类型不支持|
|405|50018|request method not support|请求方法不支持|
|500|50019|server error|服务端异常|
|403|50101|invalid image|非法的图片|
|403|50102|invalid sign id|非法的签名 ID|
|403|50103|other signatures in the audit|已经存在其他待审核的签名，不能提交|
|403|50104|invalid signature|非法签名内容|
|403|50105|default signature cannot be deleted|默认签名不能删除|