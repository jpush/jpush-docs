# SDK 集成指南 
## 适用版本
已验证 ARMv7 和 x86 平台。

## 压缩包说明
解压后目录结构如下：

```
jiot-sdk
├── build-info.txt
├── examples
│   └── linux
│       ├── demo.c
│       └── makefile
├── include
│   └── jclient
│       ├── jiot_client.h
│       └── jiot_code.h
└── lib
    └── libjiot_c_sdk.a
```

## 集成步骤
### 解压jiot-sdk压缩包
执行命令： tar zxvf jiot-sdk-xxxx-xxx.tar.gz

### 编译

#### 编译准备
1. armv7可以用交叉环境编译也可以直接在开发板上编译，需要gcc 和make工具。
2. 需要检查ssl和crypto库文件，armv7 版需要依赖 1.0.2 版本，x86 版本需要依赖 1.1 版本，可参考“ssl库配置”章节下载和配置。
3. 修改demo的makefile添加依赖库的路径，比如ssl库在/path/to/ssl/目录下，可参考如下配置：LIBDIR = -L/path/to/ssl
4. 保存makefile后，执行make编译命令即可生成demo执行文件。

#### make

可参考官方提供的demo.c编译。

```
cd jiot-sdk/examples/linux
make
```

编译后会生成demo可执行文件。

#### ssl库配置

1. 使用“ldconfig -p| grep ssl”查看ssl版本，如果版本和需求不一致，参考以下步骤添加依赖库。
2. 点击下载依赖的 ssl 和 crypto 库。 
    * [x_86 下载](https://sdkfiledl.jiguang.cn/sdk/libssl-1.1.tar.gz)
    * [armv7 下载](https://sdkfiledl.jiguang.cn/sdk/libssl-1.0.2.tar.gz)
     
3. 拷贝到目录中，比如/path/to/ssl/下。
4. 将“/path/to/ssl/”添加到/etc/ld.so.conf文件中。
5. 执行ldconfig（需要root权限执行）。
6. 再次查看ssl动态库版本，会出现如下版本lib（仅以1.0.2为例），即配置成功。
```
libssl.so (libc6,hard-float) => /path/to/ssl/libssl.so.1.0.2
libcrypto.so (libc6,hard-float) => /path/to/ssl/libcrypto.so.1.0.2
```


### 运行 Demo

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