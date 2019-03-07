#Android SDK 集成指南

##使用提示

本文是JVerification Android SDK 标准的集成指南文档。

匹配的 SDK 版本为：v1.1.0及以后版本。

+ 如果您想要快速地测试、请参考本文在几分钟内跑通Demo。
+ 极光认证文档网站上，有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。

##产品说明

极光认证整合了三大运营商的网关认证能力，为开发者提供了一键登录和号码认证功能，优化用户注册/登录、号码验证体验，提高安全性。

###主要场景：

* 注册
* 登陆
* 二次验证

###Android SDK 版本
目前SDK只支持Android 2.3或以上版本的手机系统.

##本地工程配置

###仅使用号码认证功能

+ 解压压缩包，将libs下的所有文件复制到工程的libs下面.
	+ jcore 和 jverification 两个 jar 文件。
	+ 所有 CPU 平台的 so 文件。

####jverification-android-release-1.x.y.zip 集成压缩包内容

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

####手动集成步骤

+ 解压缩 jverification-android--1.x.x-release.zip 集成压缩包。
+ 复制 libs/jcore-android-1.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/jverification-android-1.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/(cpu-type)/libjcore1xy.so 到你的工程中存放对应cpu类型的目录下。

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
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>

    <!-- Optional -->
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在6.0 系统上 层叠窗口权限 -->
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
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

+ 混淆配置

请下载 4.x 及以上版本的 [proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/)， 替换 Android SDK "tools\proguard\lib\proguard.jar"，并在工程的混淆文件中添加以下混淆代码：

~~~
		-dontwarn cn.jpush.**
		-keep class cn.jpush.** { *; }
		
		-dontwarn cn.jiguang.**
		-keep class cn.jiguang.** { *; }
		
		-dontwarn com.cmic.**
		-keep class com.cmic.** { *; }
		
		-dontwarn com.unicom.**
		-keep class com.unicom.** { *; }
~~~

###使用一键登录功能
 
如果您需要使用极光认证的一键登录功能，请在工作日9:00—18:00联系商务申请开通，QQ：303870940 TEL：400-612-5955

+ 解压压缩包，
    + 将libs下的所有文件复制到工程的libs下面.
	    + jcore 和 jverification 两个 jar 文件。
	    + 所有 CPU 平台的 so 文件。
    + 将res下的所有文件复制到工程的res下面
        + anim、drawable、drawable-xxhdpi 分别对应复制工程相应文件夹
        
####jverification-android-release-2.x.y.zip 集成压缩包内容

+ AndroidManifest.xml
    + 客户端嵌入SDK参考的配置文件
+ libs/jcore-android_v1.x.x.jar
    + sdk 核心包
+ libs/xxx/xx.so
    + sdk需要用的so文件
+ libs/jverification-android-sdk_v2.x.x.jar
    + Verification SDK 开发包
+ res/xxx
    + JVerification SDK 所需的资源文件
+ example
    + 是一个完整的 Android 项目，通过这个演示了 JVerification SDK 的基本用法，可以用来做参考。


####手动集成步骤

+ 解压缩 jverification-android-2.x.x-release.zip 集成压缩包。
+ 复制 libs/jcore-android-1.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/jverification-android-2.x.x.jar 到工程 libs/ 目录下。
+ 复制 res/xxx 到工程 res/xxx 对应的目录下。
+ 复制 libs/(cpu-type)/xxx.so 到你的工程中存放对应cpu类型的目录下。
	
	
***说明 1***：使用android studio的开发者，如果使用jniLibs文件夹导入so文件，则仅需将所有cpu类型的文件夹拷进去；如果将so文件添加在module的libs文件夹下，注意在module的gradle配置中添加一下配置：


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


####配置 AndroidManifest

**AndroidManifest 示例**

```

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您应用的包名"
    android:versionCode="100"
    android:versionName="1.0.0"
    >
    <uses-sdk android:minSdkVersion="9" android:targetSdkVersion="23" />

    <!-- Required  -->
    <uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />

    <!-- Optional -->
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在6.0 系统上 层叠窗口权限 -->
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.VIBRATE" />
    

    <application
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:name="Your Application Name">

        <!-- since 2.0.0 optional 可选项，使用一键登录功能必须添加  -->
        <activity
            android:name="com.cmic.sso.sdk.activity.OAuthActivity"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="portrait"
            android:launchMode="singleTop">
        </activity>
        <!-- since 2.0.0 optional 可选项，使用一键登录功能必须添加  -->
        <activity
            android:name="com.cmic.sso.sdk.activity.LoginAuthActivity"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="portrait"
            android:launchMode="singleTop">
        </activity>
        <!-- since 2.0.0 optional 可选项，使用一键登录功能必须添加  -->
        <activity android:name="cn.jiguang.verifysdk.CtLoginActivity"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="portrait"
            android:launchMode="singleTop">
        </activity>

        <!-- Required -->
        <meta-data android:name="JPUSH_APPKEY" android:value="您应用的Appkey"/>
        <meta-data android:name="JPUSH_CHANNEL" android:value="developer-default"/>

    </application>
</manifest>
```

####混淆配置
* 请下载 4.x 及以上版本的 proguard.jar， 并替换你 Android SDK "tools\proguard\lib\proguard.jar"
* 请在工程的混淆文件中添加以下配置：

```
-dontoptimize
-dontpreverify

-dontwarn cn.jpush.**
-keep class cn.jpush.**
{ *; }
-dontwarn cn.jiguang.**
-keep class cn.jiguang.** { *; }
-dontwarn com.cmic.**
-keep class com.cmic.** { *; }
-dontwarn com.unicom.**
-keep class com.unicom.** { *; }

-dontwarn cn.com.chinatelecom.**
-keep class cn.com.chinatelecom.** { *; }


```


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

压缩包附带的 example 是一个 API 演示例子。你可以将它导入到你的工程，并将你的 appKey 填入到 example 的 AndroidManifest 中，然后直接运行起来测试。

## 技术支持

邮件联系：[support&#64;jpush.cn](mailto:support&#64;jpush.cn)
