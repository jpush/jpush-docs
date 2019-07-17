# Android SDK接口文档

## 初始化接口
### jiotInit
创建JIOT客户端
#### 接口定义
```
void jiotInit(Context context, boolean isUseSsl);
```

#### 参数说明
* context 应用的上下文对象
* isUseSsl 是否启用ssl加密通道的标志

#### 返回值
无
### jiotConn
连接MQTT服务器
#### 接口定义
```
int jiotConn(DeviceInfo deviceInfo, JclientMessageCallback messageCallback,JclientHandleCallback handleCallback);

```

#### 参数说明
 * deviceInfo：设备信息，三元组
 * messageCallback：客户端处理下行报文的回调函数结构体
 * handleCallback：sdk连接状态回调函数结构体
#### 返回值

## 释放接口
### jiotDisConn
断开mqtt连接
#### 接口定义
```
void jiotDisConn();
```
#### 参数说明
无
#### 返回值
无

### jiotRelease
销毁JIOT客户端
#### 接口定义
```
void jiotRelease();
```
#### 参数说明
无
#### 返回值
无

## 状态查询接口
### jiotGetConnStatus
查询JIOT客户端的连接状态
#### 接口定义
```
int jiotGetConnStatus();
```
#### 参数说明
无
#### 返回值
int  jClient的状态

## 发送上行消息接口

### jiotPropertyReportReq
JIOT客户端上报设备属性

#### 接口定义
```
JiotResult jiotPropertyReportReq(PropertyReportReq properyReport);
```

#### 参数说明
* properyReport 设备属性

#### 返回值
* 客户端实时返回结果

### jiotEventReportReq
JIOT客户端上报事件请求

#### 接口定义
```
JiotResult jiotEventReportReq(EventReportReq eventReport);
```

#### 参数说明
* eventReport 上报事件

#### 返回值
* 客户端实时返回结果

### jiotVersionReportReq
JIOT客户端上报设备版本请求
#### 接口定义
```
JiotResult jiotVersionReportReq(VersionReportReq versionReportReq);
```

#### 参数说明
versionReportReq 设备版本

#### 返回值
客户端实时返回结果

## 调试日志设置接口

### jiotSetLogLevel
设置日志级别，默认不输出日志，调试用
#### 接口定义
```
void jiotSetLogLevel(int level);
```
#### 参数说明
* level 日志等级
#### 返回值
无

## 下行消息回调接口
### jiotPropertyReportRsp
处理服务端返回JIOT客户端上报设备属性请求回复
#### 接口定义
```
void jiotPropertyReportRsp(PropertyReportRsp propertyReportRsp,int errorCode);
```
#### 参数说明
* propertyReportRsp 服务器回复的属性信息
* errorCode 错误码
#### 返回值
无

### jiotVersionReportRsp
处理服务端返回JIOT客户端上报设备版本请求回复
#### 接口定义
```
void jiotVersionReportRsp(VersionReportRsp versionReportRsp,int errorCode);
```
#### 参数说明
* versionReportRsp 服务器回复的设备版本信息
* errorCode 错误码
#### 返回值
无

### jiotPropertySetReq
服务端下发给JIOT客户端设备属性设置请求
#### 接口定义
```
void jiotPropertySetReq(PropertySetReq propertySetReq,int errorCode);
```
#### 参数说明
* propertySetReq 服务器回复的设置设备属性
* errorCode 错误码
#### 返回值
无

### jiotMsgDeliverReq
服务端下发给JIOT客户端消息下发请求
#### 接口定义
```
void jiotMsgDeliverReq(MsgDeliverReq msgDeliverReq,int errorCode);
```
#### 参数说明
* msgDeliverReq 客户端接收属性设置消息
* errorCode 错误码

#### 返回值
无

## sdk连接状态回调接口
### jiotConnectedHandle
客户端mqtt连接成功
#### 接口定义
```
void jiotConnectedHandle();
```
#### 参数说明
无
#### 返回值
无

### jiotConnectFailHandle
客户端mqtt连接失败
#### 接口定义
```
void jiotConnectFailHandle(int errorCode);
```
#### 参数说明
* errorCode JIOT客户端异常错误码
#### 返回值
无

### jiotDisconnectHandle
客户端mqtt连接中断，在此之前连接成功过
#### 接口定义
```
void jiotDisconnectHandle(int errorCode,String msg);
```
#### 参数说明
* errorCode JIOT客户端异常错误码
* msg 断开的原因

#### 返回值
无

### jiotSubscribeFailHandle
客户端subscirbe失败，ACL不通过
#### 接口定义
```
void jiotSubscribeFailHandle(String topicFilter);
```
#### 参数说明
* topicFilter JIOT订阅的topic
#### 返回值
无

### jiotPublishFailHandle
客户端publish失败，ACL不通过
#### 接口定义
```
void jiotPublishFailHandle(long seqNo);
```

#### 参数说明
* seqNo 消息序号
#### 返回值
无

### jiotMessageTimeoutHandle
客户端消息发送超时
#### 接口定义
```
void jiotMessageTimeoutHandle(long seqNo);
```
#### 参数说明
* seqNo 消息序号
#### 返回值
无











