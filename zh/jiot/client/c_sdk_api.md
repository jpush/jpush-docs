#  C SDK 接口说明文档

## 设备信息结构体
保存设备端登陆JIoT平台需要的参数
```
struct DeviceInfo
{
char szProductKey[32]; //产品标示
char szDeviceName[32]; //设备名称
char szDeviceSecret[32]; //设备密钥
};
```
## SDK初始化接口
### jiotInit
创建JIOT客户端
#### 接口定义
```
JHandle jiotInit();
```
#### 参数说明
 无
####  返回值
 创建成功返回客户端的句柄，失败返回NULL

### jiotRegister
注册JIOT客户端的回调函数
#### 接口定义
```
void jiotRegister(JHandle handle,void* pContext, JClientMessageCallback *cb,JClientHandleCallback *handleCb);

```
#### 参数说明
* handle :JIOT客户端的句柄
* pContext:设备的上下文信息
* handleCb：sdk连接状态回调函数结构体
* cb: 客户端处理下行报文的回调函数结构体

####  返回值
  无
  
### jiotConn
通过SIS获取MQTT的地址和端口，并连接MQTT服务端
#### 接口定义
```
int jiotConn(JHandle handle，const DeviceInfo *pDev);
```
#### 参数说明
* handle :JIOT客户端的句柄
* pDev :设备三元组

####  返回值
* 0成功，非0失败


## SDK释放接口
### jiotDisConn
断开连接MQTT服务端。
#### 接口定义
```
void jiotDisConn(JHandle handle);
```
#### 参数说明
handle :JIOT客户端的句柄
#### 返回值
成功返回true，失败返回false

### jiotUnRegister
注销JIOT客户端的回调函数
#### 接口定义
```
void jiotUnRegister(JHandle handle);
```
#### 参数说明
 handle :JIOT客户端的句柄
#### 返回值
无

### jiotRelease
销毁JIOT客户端
#### 接口定义
```
void jiotRelease(JHandle handle);
```
#### 参数说明
handle :JIOT客户端的句柄

#### 返回值
无

## SDK状态查询接口
### jiotGetConnStatus
JIoT客户端状态查询。
#### 接口定义
```
JClientStatus jiotGetConnStatus(JHandle * handle);

```
#### 参数说明
 handle :JIOT客户端的句柄

#### 返回值
JClientStatus jClient的状态

## SDK发送上行消息接口
### jiotPropertyReportReq
JIOT客户端上报设备属性请求

#### 接口定义
```
JiotResult jiotPropertyReportReq(JHandle handle,PropertyReportReq *pReq);
```
#### 参数说明
* handle :JIOT客户端的句柄
* pReq :上报消息的结构体指针
#### 返回值
返回值结构体，内容为错误码和seqNO

### jiotEventReportReq
JIOT客户端上报设备事件请求。

#### 接口定义
```
JiotResult jiotEventReportReq(JHandle handle,EventReportReq *pReq);

```
#### 参数说明
* handle :JIOT客户端的句柄
* pReq :上报消息的结构体指针
#### 返回值
返回值结构体，内容为错误码和seqNO


### jiotVersionReportReq
JIOT客户端上报设备版本请求。
#### 接口定义
```
JiotResult jiotVersionReportReq(JHandle handle, const VersionReportReq * pReq);
```
#### 参数说明
* handle :JIOT客户端的句柄
* pReq :上报消息的结构体指针
#### 返回值
返回值结构体，内容为错误码和seqNO

### jiotPropertySetRsp
JIOT客户端回复属性设置请求的回复
#### 接口定义
```
JiotResult jiotPropertySetRsp(JHandle handle, const PropertySetRsp * Rsp);
```
#### 参数说明
* handle :JIOT客户端的句柄
* Rsp :属性设置回复结构体指针

#### 返回值
返回值结构体，内容为错误码和seqNO

### jiotMsgDeliverRsp
JIOT客户端回复消息下发请求的回复

#### 接口定义
```
JiotResult jiotMsgDeliverRsp(JHandle handle,const MsgDeliverRsp * Rsp);
```
#### 参数说明
* handle :JIOT客户端的句柄
* Rsp :属性设置回复结构体指针
#### 返回值
返回值结构体，内容为错误码和seqNO

## SDK接收下行消息回调函数接口

### jiotPropertyReportRsp

处理服务端返回JIOT客户端上报设备属性请求回复

#### 接口定义
```
typedef int jiotPropertyReportRsp(void* pContext, JHandle handle, const PropertyReportRsp * Rsp,int errcode);
```

#### 参数说明
* pContext:用户注册的上下文信息
* handle:JIOT客户端句柄
* Rsp:结构体指针
* errcode:错误码
#### 返回值
  

### jiotEventReportRsp
处理服务端返回JIOT客户端上报设备事件请求回复

#### 接口定义
```
typedef int jiotEventReportRsp(void* pContext, JHandle handle, const EventReportRsp * Rsp,int errcode);
```
#### 参数说明
* pContext:用户注册的上下文信息
* handle:JIOT客户端句柄
* Rsp:接收回复消息的结构体指针
* errcode:错误码

#### 返回值


### jiotVersionReportRsp
处理服务端返回JIOT客户端上报设备版本请求回复

#### 接口定义
```
typedef int jiotVersionReportRsp(void* pContext, JHandle handle, const VersionReportRsp * Rsp,int errcode);

```
#### 参数说明
* pContext:用户注册的上下文信息
* handle:JIOT客户端句柄
* Rsp:接收回复消息的结构体指针
* errcode:错误码
#### 返回值
  
### jiotPropertySetReq
服务端下发给JIOT客户端设备属性设置请求。

#### 接口定义
```
typedef int jiotPropertySetReq(void* pContext,JHandle handle,,PropertySetReq *Req,int errcode);
```
#### 参数说明
* pContext:用户注册的上下文信息
* handle :JIOT客户端句柄
* Req :接收属性设置消息的结构体指针
* errcode:错误码
#### 返回值
  
### jiotMsgDeliverReq
服务端下发给JIOT客户端消息下发请求。

#### 接口定义
```
typedef int jiotMsgDeliverReq(void* pContext, JHandle handle, MsgDeliverReq *Req,int errcode);
```
#### 参数说明
* pContext:用户注册的上下文信息
* handle :JIOT客户端的句柄
* Req :接收属性设置消息的结构体指
* errcode:错误码

#### 返回值
无

## SDK消息回调函数指针结构体

```
struct JClientMessageCallback
{
    jiotPropertyReportResp *_cbPropertyReportResp; 
    jiotEventReportResp *_cbEventReportResp; 
    jiotVersionReportReq *_cbVersionReportReq;
    jiotPropertySetReq *_cbPropertySetReq; 
    jiotMsgDeliverReq *_cbMsgDeliverReq;
} ;

```
## SDK状态回调函数接口

### jiotConnectedHandle
客户端mqtt连接成功。
#### 接口定义
```
typedef int jiotConnectedHandle(void* pContext);
```
#### 参数说明
* pContext:用户注册的上下文信息
####  返回值
 无 
 
### jiotConnectFailHandle
客户端mqtt连接失败
#### 接口定义
```
typedef int jiotConnectFailHandle(void* pContext,int errCode);
```
#### 参数说明
 * pContext:用户注册的上下文信息
 * errCode JIOT客户端异常错误码
####  返回值
 无

### jiotSubscribeFailHandle
客户端subscirbe失败，ACL不通过。
#### 接口定义
```
typedef int jiotSubscribeFailHandle(void* pContext,char * TopicFilter);
```
#### 参数说明
*  pContext: 用户注册的上下文信息
*  TopicFilter: JIOT订阅的topic
####  返回值
 无 
 
### jiotPublishFailHandle
客户端publish失败，ACL不通过
#### 接口定义
```
typedef int jiotPublishFailHandle(void* pContext,long long seqNo);

```
#### 参数说明
* pContext:用户注册的上下文信息
* seqNo : 消息序号
####  返回值
 无
 
### jiotMessageTimeoutHandle
客户端消息发送超时。
#### 接口定义
```
typedef int jiotMessageTimeoutHandle(void* pContext,long long seqNo);
```
#### 参数说明
* pContext:用户注册的上下文信息
* seqNo : 消息序号
####  返回值
 无
 
## SDK状态回调函数指针结构体
```
typedef struct JClientHandleCallback
{
    jiotConnectedHandle *_cbConnectedHandle; //mqtt连接成功
    jiotConnectFailHandle *_cbConnectFailHandle; //mqtt连接失败
    jiotDisconnectHandle *_cbDisconnectHandle; //mqtt连接中断
    jiotSubscribeFailHandle *_cbSubscribeFailHandle; //消息subscirbe失败，ACL不通过
    jiotPublishFailHandle *_cbPublishFailHandle; //消息publish失败，ACL不通过。由于MQTT3.1.1版本不支持，所以SDK暂时不支持,后续再开放
    jiotMessageTimeoutHandle *_cbMessageTimeoutHandle; //消息发送超时
} JClientHandleCallback;
```
## 错误码
### SDK底层返回的错误码
| 错误码 | Code | 描述 |
| --- | --- | --- |
| JIOT_SUCCESS                                                     | 0x00000000 | 成功 |
| JIOT_FAIL                                                        | 0xFFFFFFFF | 失败 |
| JIOT_ERR_AUTH_ERR                                                | 10001  | 认证失败 |
| JIOT_ERR_PRODUCTKEY_OVERLONG                                     | 10002  | product_key超过长度 |
| JIOT_ERR_DEVICENAME_OVERLONG                                     | 10003  | deviceName超过长度 |
| JIOT_ERR_DEVICESECRET_OVERLONG                                   | 10004  | deviceSecret超过长度 |
| JIOT_ERR_TEXTFIELD_OVERLONG                                      | 10005  | 字段内容超过长度 |
| JIOT_ERR_SEQNO_ERROR                                             | 10006  | 序号错误 |
| JIOT_ERR_CODE_ERROR                                              | 10007  | Code错误 |
| JIOT_ERR_TOPIC_FOTMAT_ERROR                                      | 10008  | Topic格式错误 |
| JIOT_ERR_ARGU_FORMAT_ERROR                                       | 10009  | 参数格式错误 |
| JIOT_ERR_VERSION_FORMAT_ERROR                                    | 10010  | 版本号格式错误 |
| JIOT_ERR_PROPERTY_FORMAT_ERROR                                   | 10011  | 属性异常 |
| JIOT_ERR_PROPERTY_NAME_FORMAT_ERROR                              | 10012  | 属性名异常 |
| JIOT_ERR_PROPERTY_VALUE_FORMAT_ERROR                             | 10013 | 属性内容异常 |
| JIOT_ERR_EVENT_FORMAT_ERROR                                      | 10014  | 事件异常 |
| JIOT_ERR_EVENT_NAME_FORMAT_ERROR                                 | 10015  | 事件名异常 |
| JIOT_ERR_EVENT_CONTENT_FORMAT_ERROR                              | 10016  | 事件内容异常 |
| JIOT_ERR_DATA_CONTENT_FORMAT_ERROR                               | 10017  | 数据内容异常 |
| JIOT_ERR_VERSION_APP_VAR_FORMAT_ERROR                            | 10018  | 版本信息异常 |
| JIOT_ERR_MQTT_ERR                                                | 11001  |  MQTT异常 |
| JIOT_ERR_MQTT_PING_PACKET_ERROR                                  | 11002  | MQTT心跳异常 |
| JIOT_ERR_MQTT_NETWORK_ERROR                                      | 11003  | MQTT网络异常 |
| JIOT_ERR_MQTT_CONNECT_PACKET_ERROR                               | 11004  | MQTT连接异常 |
| JIOT_ERR_MQTT_PUBLISH_PACKET_ERROR                               | 11005  | MQTT的PUBLISH消息异常 |
| JIOT_ERR_MQTT_PUSH_TO_LIST_ERROR                                 | 11006  | MQTT插入缓存队列异常 |
| JIOT_ERR_MQTT_PUBLISH_ACK_TYPE_ERROR                             | 11007  | MQTT的PUB_ACK的类型异常 |
| JIOT_ERR_MQTT_PUBLISH_ACK_PACKET_ERROR                           | 11008  | MQTT的PUB_ACK的数据异常 |
| JIOT_ERR_MQTT_SUBSCRIBE_PACKET_ERROR                             | 11009  | MQTT的SUBSCRIBE异常 |
| JIOT_ERR_MQTT_UNSUBSCRIBE_PACKET_ERROR                           | 11010  | MQTT的UNSUBSCRIBE异常 |
| JIOT_ERR_MQTT_PUBLISH_REC_PACKET_ERROR                           | 11011  | MQTT的PUBLISH_REC异常 |
| JIOT_ERR_MQTT_PUBLISH_COMP_PACKET_ERROR                          | 11012  | MQTT的PUBLISH_COMP异常 |
| JIOT_ERR_MQTT_STATE_ERROR                                        | 11013  | MQTT状态异常 |
| JIOT_ERR_MQTT_NULL_VALUE_ERROR                                   | 11014  | MQTT检验值为空 |
| JIOT_ERR_MQTT_TOPIC_FORMAT_ERROR                                 | 11015  | MQTT的Topic格式异常 |
| JIOT_ERR_MQTT_PACKET_READ_ERROR                                  | 11016  | MQTT读失败 |
| JIOT_ERR_MQTT_CONNECT_ACK_PACKET_ERROR                           | 11017  | MQTT的CONN_ACK消息读异常 |
| JIOT_ERR_MQTT_CONANCK_UNACCEPTABLE_PROTOCOL_VERSION_ERROR        | 11018  | MQTT使用的协议不匹配 |
| JIOT_ERR_MQTT_CONNACK_IDENTIFIER_REJECTED_ERROR                  | 11019  | MQTT标识符被拒绝 |
| JIOT_ERR_MQTT_CONNACK_SERVER_UNAVAILABLE_ERROR                   | 11020  | MQTT服务不可达 |
| JIOT_ERR_MQTT_CONNACK_BAD_USERDATA_ERROR                         | 11021  | MQTT用户或密码错误 |
| JIOT_ERR_MQTT_CONNACK_NOT_AUTHORIZED_ERROR                       | 11022  | MQTT客户端未授权 |
| JIOT_ERR_MQTT_CONNACK_UNKNOWN_ERROR                              | 11023  | MQTT未知错误 |
| JIOT_ERR_MQTT_SUBSCRIBE_ACK_PACKET_ERROR                         | 11024  | MQTT的SUB_ACK消息异常 |
| JIOT_ERR_MQTT_SUBSCRIBE_QOS_ERROR                                | 11025  | MQTT的SUB_QOS异常 |
| JIOT_ERR_MQTT_SUB_INFO_NOT_FOUND_ERROR                           | 11026  | MQTT未找到SUB_INFO异常 |
| JIOT_ERR_MQTT_NETWORK_CONNECT_ERROR                              | 11027  | MQTT网络连接异常 |
| JIOT_ERR_MQTT_CONNECT_ERROR                                      | 11028  | MQTT连接错误 |
| JIOT_ERR_MQTT_CREATE_THREAD_ERROR                                | 11029  | MQTT创建线程异常 |
| JIOT_ERR_MQTT_PUBLISH_QOS_ERROR                                  | 11030  | MQTT的PUB消息QOS异常 |
| JIOT_ERR_MQTT_UNSUBSCRIBE_ACK_PACKET_ERROR                       | 11031  | MQTT的UNSUB_ACK消息异常 |
| JIOT_ERR_JCLI_JSON_PARSE_ERR                                     | 12001  | JSON解析异常 |
| JIOT_HTTP_RETRIEVE_MORE_DATA                                     | 13001  | 请求响应后还有未取完的数据 |
| JIOT_ERR_HTTP_CONN                                               | 13002  | 连接失败 |
| JIOT_ERR_HTTP_PARSE                                              | 13003  | URL解析错误 |
| JIOT_ERR_HTTP_UNRESOLVED_DNS                                     | 13004  | 无法解析的Hostname |
| JIOT_ERR_HTTP_PRTCL                                              | 13005  | 协议错误 |
| JIOT_ERR_HTTP_ERROR                                              | 13006  | HTTP位置错误 |
| JIOT_ERR_HTTP_CLOSED                                             | 13007  | 远程Host关闭连接 |
| JIOT_ERR_HTTP_BREAK                                              | 13008  | 连接中断 |
| JIOT_ERR_SIS_HTTP_FAIL                                           | 14001  | SIS HTTP错误 |
| JIOT_ERR_SIS_CONTENT_ERROR                                       | 14002  | SIS 数据内容错误 |
| JIOT_ERR_SIS_JSON_PARSE_FAIL                                     | 14003  | SIS Json解析错误 |


### 服务器端返回的业务层错误码
| 错误码 | MQTT外部错误码描述信息 |
| --- | ---|
|  6000 |  internal server error |
|  6001 | params missing  |
|  6002 |  params invalid |
|  6003 |  version invalid |
|  6004 |  timestamp invalid |
|  6005 |  data configuration error |
|  6006 |  event invalid |
|  6007 | property not found |
|  6008 | property type check fail |
|  6009 | property value exceed range |
