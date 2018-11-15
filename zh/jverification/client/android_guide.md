#Android SDK 集成指南

##使用提示

本文是JVerification Android SDK 标准的集成指南文档。

匹配的 SDK 版本为：v1.0.0及以后版本。

+ 如果您想要快速地测试、请参考本文在几分钟内跑通Demo。
+ 极光认证文档网站上，有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。

##产品说明

极光认证整合了三大运营商的号码认证能力，为开发者提供了快速验证用户输入的手机号码和本机SIM卡号码一致性的功能，提高用户体验和安全性。

###主要场景：

* 注册
* 登陆
* 二次验证

###Android SDK 版本
目前SDK只支持Android 2.3或以上版本的手机系统.

###jverification-android-release-1.x.y.zip 集成压缩包内容

+ AndroidManifest.xml
    + 客户端嵌入SDK参考的配置文件
+ libs/jcore-android_v1.x.x.jar
    + sdk 核心包
+ libs/xxx/xx.so
    + sdk需要用的so文件
+ libs/jverification-android-sdk_v1.x.x.jar
    + SDK jverification 开发包
+ example
    + 是一个完整的 Android 项目，通过这个演示了 JVerification SDK 的基本用法，可以用来做参考。


##手动集成步骤

+ 解压缩 jverification-android--1.x.x-release.zip 集成压缩包。
+ 复制 libs/jcore-android-1.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/jverification-android-1.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/(cpu-type)/libjcore1xy.so 到你的工程中存放对应cpu类型的目录下。

##本地工程配置

+ 解压压缩包，将libs下的所有文件复制到工程的libs下面.
	+ jcore 和 jverification 两个 jar 文件。
	+ 所有 CPU 平台的 so 文件。

***说明***：使用android studio的开发者，如果使用jniLibs文件夹导入so文件，则仅需将所有cpu类型的文件夹拷进去；如果将so文件添加在module的libs文件夹下，注意在module的gradle配置中添加一下配置：

~~~

        android {
            ......
            sourceSets {
                main {
                    jniLibs.srcDirs = ['libs']
                    ......
                }
                ......
            }
            ......
        }

~~~

+ 配置 AndroidManifest:

**AndroidManifest 示例**

~~~

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您应用的包名"
    android:versionCode="100"
    android:versionName="1.0.0"
    >
    <uses-sdk android:minSdkVersion="9" android:targetSdkVersion="23" />

    <!-- Required -->
    <uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

    <!-- Optional -->
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在6.0 系统上 层叠窗口权限 -->
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />
    <uses-permission android:name="android.permission.VIBRATE" />


    <application
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:name="Your Application Name">

        <!-- Required -->
        <meta-data android:name="JPUSH_APPKEY" android:value="您应用的Appkey"/>
        <meta-data android:name="JPUSH_CHANNEL" android:value="developer-default"/>

    </application>
</manifest>

~~~

##添加代码

JVerification SDK 提供的 API 接口，都主要集中在 cn.jiguang.verify.api.JVerificationInterface 类里。

### 基础 API

+ 初始化 sdk ： 传入 application 的 context 来初始化 sdk 。

~~~
		JVerificationInterface.init(Context context);
~~~

+ 设置调试模式：参数为 true 表示打开调试模式，可看到 sdk 的日志。

~~~
		JVerificationInterface.setDebugMode(boolean isDebugMode);
~~~

### 更多 API

其他API的使用方法请参考接口文档：[Android SDK API](../android_api)

###运行Demo

压缩包附带的 example 是一个 API 演示例子。你可以将它导入到你的工程，并将你的 AppKey 填入到 example 的 AndroidManifest 中，然后直接运行起来测试。

## 技术支持

邮件联系：[support&#64;jpush.cn](mailto:support&#64;jpush.cn)
