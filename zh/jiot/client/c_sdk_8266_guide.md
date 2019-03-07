# SDK esp 8266 集成指南 
## 适用版本
jiot-sdk-v1.0.2-esp8266 及以上版本，支持乐鑫 ESP8266 Wi-Fi 模块（基于 ESP8266_RTOS_SDK release/v3.1版本）

## 压缩包说明
解压后目录结构如下：

```
.
├── jiot-demo
│   ├── components
│   ├── copy_jiot-lib.sh
│   ├── main
│   │   ├── component.mk
│   │   └── user_main.c
│   ├── Makefile
│   ├── readme.txt
│   ├── sdkconfig
│   └── sdkconfig.old
└── jiot-sdk
    ├── build-info.txt
    ├── component.mk
    ├── include
    │   └── jclient
    │       ├── jiot_client.h
    │       └── jiot_code.h
    └── lib
        └── libjiot-c-sdk.a
```

## 快速 Demo 步骤
### 解压jiot-sdk压缩包

执行命令： tar zxvf jiot-sdk-xxxx-esp8266.tar.gz

### 快速 Demo
#### 编译
依次运行以下命令
```
cd jiot-demo
cp -r ../jiot-sdk/ components/
./copy_jiot-lib.sh
make all
```

注意:
* 如果make all后，提示配置工程，直接回车使用默认配置即可。
* 如果执行了make clean或删除jiot-demo/build目录，在“make all”前需要执行“copy_jiot-lib.sh”。

#### 运行 Demo

编译完成后，将生成文件下载到开发板，执行以下命令：
```
make flash
```

将开发板设置为运行模式，通过如下命令监视日志即可：
```
make monitor
```

