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

## 集成jiot-sdk到项目中
项目工程以乐鑫SDK中“examples/get-started/project_template”为例。
1. 将解压出来的jiot-sdk文件夹拷贝到project_template/components文件夹中。
2. 在project_template/build目录中创建文件夹jiot-sdk。
3. 将project_template/components/jiot-sdk/lib/libjiot-c-sdk.a文件拷贝到project_template/build/jiot-sdk/目录下，并重命名为libjiot-sdk.a（即jiot-demo中“copy_jiot-lib.sh”执行过程）。
4. make all即可找到jiot的头文件和库文件，完成编译。

注意，project_template/build/目录中文件为make生成文件，如果执行make clean等操作，需要重新拷贝库文件，即执行步骤3。

