# 回调接口

## 设置回调地址
### 功能说明
设置并校验回调地址,JIoT 设备上报的事件将以回调的形式发给业务服务器。

### 操作路径
Step1：登入控制台
Step2：进入具体的产品页面
Step3：左侧菜单中选择［回调设置］
Step4：点击选择需要使用的回调接口

### 设置回调地址
在控制台填写回调地址，回调地址必须以 http:// 或 https:// 开头，不支持自定义端口。填写回调地址后需校验通过后才可以使用，

### 校验规则：
极光将给回调 URL 发起一个 GET 请求并附带一个 8 位随机字符串的参数 echostr，开发者需要在 Response Body 里将 echostr 的 value 返回。

## 事件回调格式
### 回调方式说明
当有回调消息时，将采用 HTTP POST 的方式向开发者填写的回调 URL 提交通知消息。需要注意的是，如果回调失败，那么极光将会立即重试一次。

### 参数说明:
| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| product_key | string | | 产品的product key| |
| report_seq| int| | 上报事件的序号 | |
| device_name | string |  | 设备的 device_name | |
| event | json | |上报事件的结构体 | |
| name | string |  | 事件的名称 | |
| content | string |  | 事件的内容 | |
| time | int |  | 事件发生的时间戳| |
| type | int  |  | 事件的类型 | 0:信息，1：告警， 2：故障 |

## 消息回调格式
当个消息送达设备的时候，结果会通过 http 回调的方式发送给客户的系统。目前只支持将成功的记录通知到客户。
### 参数说明:
| 关键字 | 类型 | 选项  | 含义 | 说明 |
| --- | --- | --- | --- | --- |
| product_key | string | | 产品的product key| |
| device_name | string |  | 设备的 device_name | |
| message_id| int| | 消息发送时返回该消息的消息 id | |
| msg_status | int |  |0:成功，其他:失败| |
| time | int |  | 事件发生的时间戳 | |