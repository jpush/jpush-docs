# REST API
## 属性设置
### 功能说明:
设置设备的属性值。
### 调用地址:
https://api.iot.jiguang.cn/device/v1/property
### 请求示例:

```
curl --insecure -X POST -v https://api.iot.jiguang.cn/device/v1/property -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"seq_no":1, "device_name":"your device_name", "version":1, "properties":[ {"name":"p1", "value":"v1"}]}'
> POST /device/v1/property HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明：


| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| seq_no | int | 必填 | 应用端的对于该该操作的id | 该 id 应用在15 分钟内不能重复使用，否则服务端会认为是重复请求|
| device_name | string | 必填 | 待设置属性的设备名称 |  |
| version | int | 必填 | 属性设置操作的版本id |  |
| properties | array | 必填 | 待设置的属性项数组 |  |
| name | string | 必填 | 属性项名称 |  |
| value | number/string | 必填 | 属性项值 |当属性为 int/double 时，字段类型使用 number，如果设置了值的区间，会校验值是否合法。当属性是 string 时，字段类型使用 string 默认最大长度(1024 byte)。|

### 返回示例
```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "device_name": "your device_name",
    "op_code": 0,
    "op_id": 1,
    "op_status": "ok"

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
https://api.iot.jiguang.cn/msg/v1/msg
### 请求示例:

```
curl --insecure -X POST -v https://api.iot.jiguang.cn/msg/v1/msg -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"seq_no":1, "device_name":"your device_name", "msg_body":"this is the first msg"}'
> POST /msg/v1/msg HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==

```
### 参数说明

| 关键字 | 类型 | 选项 | 含义 | 说明 |
|--------|------|------|------|------|
| seq_no | int | 必选 | 应用端的对于该该操作的id |该 id 应用在 15 分钟内不能重复使用，否则服务端会认为是重复请求 |
| device_name | string | 必选 | 需要发送消息到的设备名称 | |
| msg_body | string | 必选 | 发送的消息体的内容 |最大长度 2048 byte。|
| ttl | int | 可选 | 该消息的有效期 | 范围为0~604800秒（0到7天），请求中如不携带，服务器默认为86400秒（1天）|


### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "msgid": 4
}
```

### 返回说明：
msg : 返回该消息的全局消息 id

## 查询设备基本信息
### 功能说明:
查询设备基本信息。

### 调用地址:
https://api.iot.jiguang.cn/device/v1/baseinfo

### 请求示例:
```
curl --insecure -X GET -v https://api.iot.jiguang.cn/device/v1/baseinfo?device_name="your device_name" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
 
> GET /device/v1/baseinfo HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明:
| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| device_name | string | 必填 | 需查询的设备名称 | |


### 返回示例:
```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "device_secret": "a335f2e1c59b40e3908f57e9",
    "flag": 0,
    "time_create": 1547435552,
    "time_active": 1547454560
}
```
### 返回说明：
设备基础信息的 json 对象:
* device_secret : 设备的 device_secret
* flag :  设备的 当前状态是启用还是禁用
* time_create: 设备的创建时间 unix 时间戳
* time_active: 设备的激活时间 unix 时间戳

## 查询设备属性信息
### 功能说明:
查询设备属性信息。
### 调用地址:
https://api.iot.jiguang.cn/device/v1/property
### 请求示例:
```
curl --insecure -X GET -v https://api.iot.jiguang.cn/device/v1/property?device_name="your device_name" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
 
> GET /device/v1/property HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明:

| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| device_name | string | 必填 | 需查询的设备名称 | |

### 返回示例:
```

< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "properties": [{
        "name": "string",
        "desired_value": "test",
        "desired_stime": 1547620623651,
        "reported_value": "test",
        "reported_stime": 1547620823651
    }],
    "sdk_ver": "1.01",
    "app_ver": "1.00",
    "last_desired_stime": 1547620623651,
    "last_reported_stime": 1547620823651,
    "last_desired_version": 3,
    "last_reported_version": 2
}
```

### 返回说明：

* properties: 设备属性信息的 json 数组对象
    * name : 属性名称。(必选)
    * desired_value : 设置设备属性值。
    * desired_stime ：设置设备属性值的 unix 时间戳。
    * reported_value : 设备上报属性的当前值
    * reported_stime ：设备上报属性的 unix 时间戳
* sdk_ver : 设备端使用的 sdk 的版本信息
* app_ver : 应用 app 的版本信息
* last_desired_stime ：设备最近一次设备属性的 unix 时间戳
* last_reported_stime ：设备最近一次设备属性的 unix 时间戳
* last_desired_version ：设备下一次设置可用的属性版本 id
* last_reported_version : 设备最近一次上报的属性版本

## 查询设备状态信息

### 功能说明:
查询设备状态信息。
### 调用地址:
https://api.iot.jiguang.cn/device/v1/status
### 请求示例:
```
curl --insecure -X GET -v https://api.iot.jiguang.cn/device/v1/status?device_name="your device_name" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
 
> GET /device/v1/status HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明:
| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| device_name | string | 必填 | 需查询的设备名称 | |

### 返回示例:
```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
    "status": 0,
    "client_ip": "113.31.131.101",
    "last_login_time": "1547454560",
    "last_logout_time": "1547454569"
}
```
### 返回说明：
* status : 设备当期的状态 0-未在线， 1-在线
* client_ip : 设备最近一次上线时的 ip 地址
* last_login_time : 设备最近一次登录时间
* last_logout_time : 设备最近一次登出时间


## 批量创建设备
### 功能说明:
批量创建设备接口。
### 调用地址:
```
https://api.iot.jiguang.cn/device/v1/devices
```
### 请求示例:
```
curl --insecure -X POST -v https://api.iot.jiguang.cn/device/v1/devices -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"device":[{"name":"device_1","mark":"备注1"},{"name":"device_2","mark":"备注2"}]}'
 
> POST /device/v1/devices HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
### 参数说明:

| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| device | 设备对象数组	| 必填 | 待创建的设备对象 |每个设备对象包括一个 name 和mark 每个请求最大支持添加1000个设备|
| name | string	| 必填 | 设备的名字 |只支持数字、 英文字母和-_@. 长度为4~24 字符|
| mark | string	| 可选 | 设备的备注 | 长度为0~128 字符 |

### 返回示例:
```
< HTTP/1.1 200 OK
< Content-Type: application/json
{
     "resp": [
        {
            "device_name": "device_1",
            "code": 0,
            "device_secret": "xxxxxxxx"
        },
        {
            "device_name": "device_2",
            "code": 0
            "device_secret": "xxxxxxxx"

        },
        {
            "device_name": "device_3",
            "code": 0,
            "device_secret": "xxxxxxxx"
        }
    ]
}
```

### 返回说明：

* resp json 对象：该对象为数组，数据中的每个元素对应请求中 device_name 的创建应答。如果设备创建成功，则包含device_secret，失败则包含错误原因。

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
