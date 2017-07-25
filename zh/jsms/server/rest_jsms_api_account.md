# 短信余量查询 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>支持查询开发者账号余量</li>
<li>支持查询应用余量</li>
</ul>
</div>
</br>

## 账号余量查询 API

### 功能说明

- 查询账号余量，账号余量指未分配给某个应用，属于账号共享的短信余量。

### 调用地址

- GET https://api.sms.jpush.cn/v1/accounts/dev

### HTTP 验证
> 使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(devKey:apiDevSecret)，即:对 devKey 加上冒号，加上 API DevSecret 拼装起来的字符串，再做 base64 转换。devKey、apiDevSecret 可以在控制台个人信息中查看。


### 请求示例

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/accounts/dev -H "Content-Type: application/json" -u "7e503edcb0cb725e331b0311:7289516381dcdf1113730f2b"
```

### 返回示例

##### 发送成功

```json
{"dev_balance": 20}
```

##### 发送失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

## 应用余量查询 API

### 功能说明

- 查询应用余量，应用余量指分配给某个应用单独使用的短信余量。

### 调用地址

- GET https://api.sms.jpush.cn/v1/accounts/app

### HTTP 验证
> 使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)，即:对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。appKey、masterSecret 可以在控制台应用设置中查看。


### 请求示例

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/accounts/app -H "Content-Type: application/json" -u "4c6921c9b20b2fd9bcd8ca3d:5b3e2979c8a48b84cebeaaf4"
```

### 返回示例

##### 发送成功

```json
{"app_balance": 20}
```

##### 发送失败

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

## 返回码

|HTTP CODE| CODE| CONTENT  | DESC|
|:---- |:---- |:---- |:----
|200|50000|success|请求成功
|400|50001|missing auth|auth为空
|401|50002|auth failed|auth鉴权失败
|403|50008|no sms code auth|未开通短信业务
|403|50009|out of freq|发送超频
|404|50016|api not found|API 不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常
|403|50033|app quota not assigned|该应用未分配余量