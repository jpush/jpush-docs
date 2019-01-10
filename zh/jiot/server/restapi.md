# REST API
## 属性设置
### 功能说明:
设置设备的属性值。
### 调用地址:
https://api.iot.jiguang.cn/device/v1/propertyset
### 请求示例:

```
curl --insecure -X POST -v http://api.iot.jiguang.cn/device/v1/propertyset -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"seq_no":1, "device_name":"your device_name", "version":1, "properties":[ {"name":"p1", "value":"v1"}]}'
> POST /device/v1/propertyset HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明：


| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| seq_no | int | 必填 | 应用端的对于该该操作的id |  |
| device_name | string | 必填 | 待设置属性的设备名称 |  |
| version | int | 必填 | 属性设置操作的版本id |  |
| properties | array | 必填 | 待设置的属性项数组 |  |
| name | string | 必填 | 属性项名称 |  |
| value | string | 必填 | 属性项值 |当属性是 int 类型时，会校验值区间，如果设置了取值范围。当属性是 string 类型时，默认最大长度(1024 byte)。|

### 返回示例
```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
"code": 200,
"msg": {
"device_name": "your device_name",
"op_code": 0,
"op_id": 1,
"op_status": "ok"
}
}
```

### 返回说明
  
msg json 对象：
device_name : 设备的 device_name
op_code :  属性设置操作的返回的状态码 0 表示成功
op_id :  属性设置的操作id
op_status : 用来对 op_code 的简短描述



## 下发消息
### 功能说明:
下发消息到指定的设备。
### 调用地址:
https://api.iot.jiguang.cn/msg/v1/msgpub
### 请求示例:

```
curl --insecure -X POST -v http://api.iot.jiguang.cn/msg/v1/msgpub -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"seq_no":1, "device_name":"your device_name", "msg_body":"this is the first msg"}'
> POST /msg/v1/msgpub HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==

```
### 参数说明

| 关键字 | 类型 | 选项 | 含义 | 说明 |
|--------|------|------|------|------|
| seq_no | int | 必选 | 应用端的对于该该操作的id | |
| device_name | string | 必选 | 需要发送消息到的设备名称 | |
| msg_body | string | 必选 | 发送的消息体的内容 | 二进制内容需先用base64 编码。 最大长度 2048 byte。|
| ttl | int | 可选 | 该消息的有效期 | 范围为0~604800秒（0到7天），请求中如不携带，服务器默认为86400秒（1天）|


### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "msg": {
        "msgid": 4
    }
}
```

###返回说明：
msg : 返回该消息的全局消息 id

## 返回错误说明
当返回的 code 不是 200 时，表示请求错误。

```
< HTTP/1.1 400 Bad request
< Content-Type: application/json
{
  "error" " {
      "code": 1003,
      "message": "params invalid"
   }
}
```
###参数说明：
code: 标识请求错误类型。
msg : 标识请求错误具体的原因。

## 错误码

| Code | 描述 | 详细解释 | HTTP Status |
| --- | --- | --- | --- |
| 1000  | 系统内部错误 | 服务器端内部逻辑错误，请稍后重试。或反馈问题给极光 | 500 |
| 1002 | 缺少了必须的参数 | 必须改正，检查要求必填的参数是否未写 | 400 |
| 1003 | 参数值不合法 | 必须改正。参数不合法的情况如： | 400 |
| 1004 | 验证失败	 |必须改正。检查 productkey 与 mastersecret，  | 401 |
| 2002 | API调用频率超出该应用的限制 | 注意 API 频率控制，可联系极光商务或技术支持开通更高的 API 调用频率 | 429 |
