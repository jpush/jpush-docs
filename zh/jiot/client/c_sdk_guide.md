# SDK 集成指南 
## 适用版本
jiot-sdk-v1.0.1 及以上。已验证 ARMv7 和 x86 平台。

## 压缩包说明
解压后目录结构如下：

```
 jiot-sdk
 ├── build-info.txt
 ├── examples
 │   └── linux
 │       ├── demo.c
 │       ├── environment-setup
 │       └── makefile
 ├── include
 │   └── jclient
 │       ├── jiot_client.h
 │       └── jiot_code.h
 ├── lib
 │   └── libjiot_c_sdk.a
 └── lib-third
```

“lib-third” 是SDK依赖的第三方库，如果系统上存在该版本的库，可以不使用该目录下的库。

## 快速 Demo 步骤
### 解压jiot-sdk压缩包

执行命令： tar zxvf jiot-sdk-xxxx-xxx.tar.gz

### 快速 Demo
#### 编译
依次运行以下命令
```
cd jiot-sdk/examples/linux
source environment-setup
make
```
#### 运行 Demo

```
./demo ProductKey DeviceName DeviceSecret
```

运行参数分别为：

* ProductKey:在极光 IoT portal 上创建产品得到的对应的产品标识。
* DeviceName:在 portal 上创建设备时输入的设备名。
* DeviceSecret:在 portal 上创建设备成功后得到的产品密钥，可以通过设备详情页面查看。

运行成功会看到“jClient connect success!”等日志。

### 调试 Demo
#### 消息下发
通过调用 JIoT 的 REST API 发送消息到测试设备
消息收到会显示以下内容
```
msgDeliverReq:
message:[close]
time:[2018/12/13 18:26:55]
```

#### 属性上报
* 在对话框输入：property 然后回车
* 根据指示输入 Property Name 和 Property Value
* 消息已发送会显示：Publish Property report OK
* 消息发送失败，根据code值在sdk的错误码中找对应的错误
* 收到服务端应答会显示：propertyReportRsp

#### 事件上报
* 在对话框输入：event 然后回车
* 根据指示输入 Event Name 和 Event Value
* 消息已发送会显示：Publish Event report OK
* 消息发送失败，根据code值在sdk的错误码中找对应的错误
* 收到服务端应答会显示：eventReportRsp

#### 版本上报
* 在对话框输入：version 然后回车
* 根据指示输入 App Version
* 消息已发送会显示：Publish version report OK 
* 消息发送失败，根据code值在sdk的错误码中找对应的错误
* 收到服务端应答会显示：versionReportRsp

## 开发集成 SDK
### ssl库配置
“快速 Demo” 是通过 “environment-setup” 设定环境变量编译运行，如果集成SDK建议按如下步骤操作，如下也以demo为例。

1. 使用“ldconfig -p| grep ssl”查看ssl版本，armv7版需要依赖 1.0.2 版本，x86版本需要依赖 1.1 版本。如果版本和需求不一致，参考以下步骤添加依赖库。     
2. 从 jiot-sdk/lib-third拷贝库到指定目录，比如“/path/to/ssl/”。
3. 将“/path/to/ssl/”添加到/etc/ld.so.conf文件中。
4. 执行ldconfig（需要root权限执行）。
5. 再次查看ssl动态库版本，会出现如下版本lib（仅以1.0.2为例），即配置成功。
```
libssl.so (libc6,hard-float) => /path/to/ssl/libssl.so.1.0.2
libcrypto.so (libc6,hard-float) => /path/to/ssl/libcrypto.so.1.0.2
```
6. 修改makefile添加依赖库的路径，比如ssl库在"/path/to/ssl/"目录下，可参考如下配置：
     LIBDIR = -L/path/to/ssl
7. 保存makefile后，执行make编译命令即可生成执行文件。

### 编译程序

下面以demo.c文件为例，引入jiot-sdk下的头文件和库文件即可编译出demo。

```
gcc -o demo demo.c -Ijiot-sdk/include/jclient/ -Ljiot-sdk/lib/ -ljiot_c_sdk -lpthread -lssl -lcrypto
```