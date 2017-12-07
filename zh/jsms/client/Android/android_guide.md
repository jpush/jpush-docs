# JSMS Android SDK 集成指南

## SDK 说明

### 支持版本
+ 目前 SDK 只支持 Android 2.3 及以上版本的手机系统。

### SDK 压缩包包含

+ AndroidManifest.xml：客户端嵌入 SDK 参考的配置文件；
+ libs/jpush-sdk-sms-v1.x.x.jar：SDK Java 开发包；
+ example：一个完整的 Android 项目，演示了 SMS SDK 的基本用法，可以用作参考。

## 集成步骤

### 创建应用
注册成为极光开发者，在极光的 Web Portal 上创建应用得到 AppKey。如果您已经是是极光其他产品的用户并且创建过应用，那么无需重复创建。

### 导入 SDK 开发包
解压压缩包，将 libs/jpush-sdk-sms-v1.x.x.jar 复制到工程的 libs 目录下面。

### 集成 JPush Android SDK 的混淆

```
-keep class cn.jpush.sms.SMSSDK {*;}
-keep class cn.jpush.sms.listener.** {*;}
```

### 配置 AndroidManifest.xml
+ 配置权限：

		<uses-permission android:name="android.permission.INTERNET"/>
		<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
		<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
		<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

+ 配置 AppKey：

		<meta-data android:name="JPUSH_APPKEY" android:value="Your AppKey"/>

### 添加代码
参考 Demo 和 SDK API 说明进行添加集成。

