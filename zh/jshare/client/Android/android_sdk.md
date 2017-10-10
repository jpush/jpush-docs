# Android JShare集成指南

## 使用提示
本文是 JSHARE Android SDK 的标准集成指南文档。
匹配的 SDK 版本为：V1.0.0及以后版本。

* 如果你想要快速测试、请参考本文在几分钟内跑通 Demo。
* 极光文档官网上有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
* [极光社区](https://community.jiguang.cn/)网站：大家对文档有疑惑，以及产品出现问题，可以到极光社区来提问题，可以及时得到回应。

## 产品功能说明
JSHARE SDK 可以让你的应用支持多平台分享，无需花耗时间了解、集成每个社会化分享平台的 SDK，可以有效的降低包体积。

### 主要场景：

* 将分享内容分享到 QQ、微信、新浪微博、Facebook 等主要的社交平台。
* 获得QQ、微信、新浪微博、Facebook 等主要平台授权。
* 获取QQ、微信、新浪微博、Facebook 等主要平台的个人信息，用于第三方登录。


### jshare-android-1.x.y-release.zip 集成压缩包内容
* JGShareSDK.xml
	* 客户端嵌入 SDK，各个平台配置的参考文件。
* AndroidManifest.xml
	* 客户端嵌入 SDK 参考的配置文件。
* libs/jcore-android-1.x.y.jar
	* 极光开发者服务的核心包。
* jshare-android-1.x.y.jar
	* JShare SDK 核心包。
* jshare-wechat-android-1.x.y.jar
	* JShare 微信平台包。
* jshare-qq-android-1.x.y.jar
	* JShareQQ 平台包。
* jshare-sina-android-1.x.y.jar
	* JShare 新浪微博包。
* jshare-facebook-android-1.x.y.jar
    * JShareFacebook 平台包。
* libs/(cpu-type)/libjcore1xy.so
	* 各种 CPU 类型的 native 开发包。
* example
	* 是一个完整的 Android 项目，通过这个演示了 JShare SDK 的基本用法，可以用来做参考。  
	
### Android SDK 版本
JShare SDK 支持 Android 2.3 及以上版本的 Android 系统。



## jcenter 自动集成
**说明 ：** 使用 jcenter 自动集成的开发者，不需要在项目中添加 jar 和 so，jcenter 会自动完成依赖。

* 在 gradle 配置 jcenter。
* 配置 JGShareSDK.xml。
* 配置微信回调（如不需要分享到微信，可跳过）。
* 配置项目签名。
* 参考 example 工程或者接口文档使用 JShare SDK。

### gradle 配置

* 确认 android studio 的 Project 根目录的主 gradle 中配置了 jcenter 支持。（新建 project 默认配置就支持）

```
buildscript {
    repositories {
        jcenter()
    }
    ......
}

allprojects {
    repositories {
        jcenter()
    }
}
```
* 在 module 的 gradle 中添加依赖和 AndroidManifest 的替换变量。

```
android {
    ......
    defaultConfig {
        applicationId "com.xxx.xxx" //极光控制台创建应用时填写的应用包名.
        ......

        ndk {
            //选择要添加的对应 cpu 类型的 .so 库。
            abiFilters 'armeabi', 'armeabi-v7a', 'armeabi-v8a'
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [
            JSHARE_PKGNAME : applicationId,
            JPUSH_APPKEY : "你的 appkey", //极光控制台创建应用得到的 AppKey.
            JPUSH_CHANNEL : "developer-default", //暂时填写默认值即可.
            TENCENT_APPID: "QQ 开发者应用的 appID",//腾讯开放平台注册应用得到的 appId
            FACEBOOK_APPID: "facebook 开发者应用的 appID",//facebook 注册应用得到的 appId
        ]
        ......
    }
    ......
}
dependencies {
    ......
    compile 'cn.jiguang.sdk:jshare:1.3.0'  // 此处以 JShare 1.3.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-qqmodel:1.3.0'  // 此处以 jshare-qqmodel 1.3.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-wechatmodel:1.3.0'  // 此处以 jshare-wechatmodel 1.3.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-sinamodel:1.3.0'  // 此处以 jshare-sinamodel 1.3.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-facebookmodel:1.3.0'  // 此处以 jshare-facebookmodel 1.3.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jcore:1.1.5'  // 此处以 JCore 1.1.5 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    ......
}
```
**注 :** 如果在添加以上 abiFilter 配置之后 android Studio 出现以下提示：

```
NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.
```
则在 Project 根目录的 gradle.properties 文件中添加：

```
android.useDeprecatedNdk=true
```

## 手动集成步骤
* 解压缩 jshare-android-1.x.y-release.zip 集成压缩包。
* 复制 libs/jcore-android-1.x.y.jar 到工程 libs 目录下。
* 复制 libs/jshare-android-1.x.y.jar 到工程 libs 目录下。
* 复制 libs/(cpu-type)/libjcore1xy.so 到你工程中存放对应 cpu 类型的目录下。
* 根据需要复制 libs/jshare-xx.jar 平台 jar 包到工程 libs 目录下。
* 按下面说明配置 AndroidManifest.xml。
* 配置 JGShareSDK.xml。
* 配置微信回调（如不需要分享到微信，可跳过）。
* 配置项目签名。
* 参考 example 工程或者接口文档使用 JShare SDK。

**说明 ：** 使用 android studio 的开发者，如果使用 jniLibs 文件夹导入 so 文件，则仅需将所有 cpu 类型的文件夹拷进去；
如果将 so 文件添加在 module 的 libs 文件夹下，注意在 module 的 gradle 配置中添加一下配置：

```
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
```

### 配置 AndroidManifest.xml
根据 SDK 压缩包里的 AndroidManifest.xml 样例文件，来配置应用程序项目的 AndroidManifest.xml 。

* 复制备注为 "Required" 的部分
* 将标注为“您应用的包名”的部分，替换为当前应用程序的包
* 将标注为“您应用的 Appkey” 的部分，替换为在 Portal 上注册该应用的的 Key,例如：
9fed5bcb7b9b87413678c407

#### AndroidManifest 示例
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    android:versionCode="130"
    android:versionName="1.3.0"
	package="您应用的包名">

	<!-- Required -->
	<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
	<uses-permission android:name="android.permission.INTERNET" />
	<uses-permission android:name="android.permission.WAKE_LOCK" />
	<uses-permission android:name="android.permission.READ_PHONE_STATE" />
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.VIBRATE" />
	<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
	<uses-permission android:name="android.permission.WRITE_SETTINGS" />
	<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

	<!-- Optional. Required for location feature -->
	<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
	<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
	<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
	<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
	<uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
	<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
	<uses-permission android:name="android.permission.GET_TASKS" />

	<application
		android:name=".MyApplication"
		android:allowBackup="true"
		android:icon="@mipmap/ic_launcher"
		android:label="@string/app_name"
		android:supportsRtl="true"
		android:theme="@style/AppTheme">
		<activity android:name=".MainActivity">
			<intent-filter>
				<action android:name="android.intent.action.MAIN" />
				<category android:name="android.intent.category.LAUNCHER" />
			</intent-filter>
		</activity>
		<activity android:name=".SelectPlatActivity"/>
        <activity android:name=".ShareTypeActivity"/>

		<!-- Required SDK 核心功能-->
		<activity
            android:name="cn.jiguang.share.android.ui.JiguangShellActivity"
            android:configChanges="keyboardHidden|orientation|screenSize"
            android:exported="true"
            android:launchMode="singleTask"
            android:screenOrientation="portrait"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:windowSoftInputMode="stateHidden|adjustResize">
            <!-- Optional QQ 分享回调-->
            <!-- scheme为“tencent”前缀再加上 QQ 开发者应用的 appID；例如 appID 为 123456，则 scheme＝“tencent123456” -->
            <intent-filter>
                <data android:scheme="tencent+appID" />
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.BROWSABLE" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>

            <!-- Optional 新浪微博分享回调 -->
            <intent-filter>
                <action android:name="com.sina.weibo.sdk.action.ACTION_SDK_REQ_ACTIVITY" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>

            <!-- Optional 新浪微博私信回调-->
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="jsharesdk" android:host="sinaweibo"/>
            </intent-filter>
        </activity>

		<!-- Optional 微信分享回调,wxapi 必须在包名路径下，否则回调不成功-->
		<activity
			android:name=".wxapi.WXEntryActivity"
			 android:theme="@android:style/Theme.Translucent.NoTitleBar"
			android:exported="true" />

		<!-- Optional facebook 配置,authorities 必须为 com.facebook.app.FacebookContentProvider+APP_ID;例如 APP_ID 为 123456，则authorities="com.facebook.app.FacebookContentProvider123456"-->
		<provider
			android:authorities="com.facebook.app.FacebookContentProvider+APP_ID"
			android:name="cn.jiguang.share.facebook.FacebookContentProvider"
			android:exported="true"
		/>

		<!-- User defined.  For test only  用户自定义的广播接收器-->
		<receiver android:name="cn.jiguang.share.demo.FaceBookUploadReceiver">
			<intent-filter>
				<action android:name="com.facebook.platform.AppCallResultBroadcast" />
			</intent-filter>
		</receiver>

		<!-- Required. For publish channel feature -->
		<!-- JPUSH_CHANNEL 是为了方便开发者统计 APK 分发渠道。-->
		<!-- 例如: -->
		<!-- 发到 Google Play 的 APK 可以设置为 google-play; -->
		<!-- 发到其他市场的 APK 可以设置为 xxx-market。 -->
		<!-- 目前这个渠道统计功能的报表还未开放。-->
		<meta-data
			android:name="JPUSH_CHANNEL"
			android:value="developer-default" />
		<!-- Required. AppKey copied from Portal -->
		<meta-data
			android:name="JPUSH_APPKEY"
			android:value="您应用的 Appkey" />

	</application>

</manifest>
```

## 配置 JGShareSDK.xml
无论是使用自动集成还是手动集成方式，都需要配置 JGShareSDK.xml。
主要步骤为：

* 复制或者新建 JGShareSDK.xml 到工程目录的 asset 目录下。
* 把 JGShareSDK.xml 中相关的 AppKey、AppSecret 替换成自己在第三方平台创建的应用得到的信息。
* 根据需要配置各个平台，不需要的平台可以删除。

#### JGShareSDK.xml示例
```
<?xml version="1.0" encoding="utf-8"?>
<DevInfor>

    <!-- 如果不需要支持某平台，可缺省该平台的配置-->

    <SinaWeibo
        AppKey="新浪微博的 AppKey"
        AppSecret="新浪微博 AppSecret"
        RedirectUrl="微博开放平台填写的授权回调页"/>

    <QQ
        AppId="QQ 的 AppId"
        AppKey="QQ 的 AppKey"/>

    <Wechat
        AppId="微信的 AppId"
        AppSecret="微信的 AppSectet"/>
        
    <Facebook
        AppId="facebook 的 appId"
        AppName="facebook 后台填写的名称"
    />

</DevInfor>
```
## 配置微信平台回调
* 在你的包名相应目录下新建一个 wxapi 目录，并在该 wxapi 目录下新增一个 WXEntryActivity 类，该类继承自WeChatHandleActivity（例如应用程序的包名为 cn.jiguang.share.demo，则新添加的类如下图所示）

![](http://i.imgur.com/2URxXFr.png)

**注意：** 如果复写了 onCreate 方法、onNewIntent 方法，那么必须调用父类方法，否者无法获取分享结果，例如：

```
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
}
```

```
@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
}
```
* 并在 manifest 文件里面加上 exported 属性，设置为 true，例如：

```
<activity
    android:name=".wxapi.WXEntryActivity"
	android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:exported="true" />
```

## 配置 Facebook 平台
* 在 manifest 文件里面添加 Facebook 的 ContentProvider 配置：
```
<provider
    android:authorities="com.facebook.app.FacebookContentProvider + App_Id"
    android:name="cn.jiguang.share.facebook.FacebookContentProvider"
    android:exported="true"
/>
```

**注意：** provider的authorities 必须为 "com.facebook.app.FacebookContentProvider"+"AppId"。

* 如果需要获取 facebook 上传图片、视频结果可自定义 BroadCastReceiver，继承 FacebookBroadcastReceiver，复写onSuccessfulAppCall、onFailedAppCall 方法：
```
<receiver android:name="cn.jiguang.share.demo.FaceBookUploadReceiver">
    <intent-filter>
        <action android:name="com.facebook.platform.AppCallResultBroadcast" />
    </intent-filter>
</receiver>
```

**注意：** receiver 的 action 必须为 "com.facebook.platform.AppCallResultBroadcast"。

## 配置项目签名

### Android Studio 图形界面签名配置
进入 Project Structure，选择您集成 JShare 的项目，具体配置如图：

![](http://i.imgur.com/ahk1DoN.png)
![](http://i.imgur.com/2oh4IKp.png)

### Android Studio 手动配置
* 在项目的 build.gradle 的 android 内部新增签名配置，例如：

```
signingConfigs {
        debug {
              storeFile file("jshare.jks") //签名文件路径
              storePassword "sdkteam"
              keyAlias "jshare"
              keyPassword "sdkteam" //签名密码
        }
        release {
             storeFile file("jshare.jks") //签名文件路径
             storePassword "sdkteam"
             keyAlias "jshare"
             keyPassword "sdkteam" //签名密码
        }
    }
```


* 然后在项目的 build.gradle 的 buildTypes 使用签名配置，例如：

```
buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-project.txt'
            signingConfig signingConfigs.debug
        }
        debug {
            signingConfig signingConfigs.debug
        }
    }
```


### Eclipse 环境配置

* 在 Eclipse 的 Preferences，选择 Android -> Build，如下图：

![](http://i.imgur.com/mKPb3De.png)

* 指定 Custom debug keystore 选项的路径为 sdk demo 工程目录中的 debug.keystore 文件，并应用该配置，如下图：
![](http://i.imgur.com/TgxykaK.png)

### 注意
* 应用的包名、应用的签名、第三方平台注册的 AppID 及 Appkey 三者要一一对应，否则会无法分享。
* 应用的签名要与在第三方平台填写的签名对应，否则会无法分享。
* 新浪微博支持未安装客户端分享，需要注意 JGShareSDK.xml 中的 RedirectUrl 要与微博开放平台填写的需要一致，否则会发生错误。
## 添加代码
JShare SDK 提供的 API 接口，都主要集中在 cn.jiguang.share.android.api.JShareInterface 类，使用方法请参考 example 或者 API 接口文档。

### API基础API
* init 初始化SDK

```
public static void init(Context context)
```
* setDebugMode 设置调试模式

```
public static void setDebugMode(boolean enable)
```
注：该接口需在init接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的Application中onCreate中调用。
### 测试确认
* 确认所需要的文件已经添加进工程。
* 确认 Androidmanifest.xml 已经正确配置。
* 确认 JGShareSDK.xml 已经正确配置。
* 根据如下日志确定配置了什么平台。
* 确认应用的包名、签名与第三方后台所填写的信息一致。

```
[PlatformManager] platform Wechat has configured
[PlatformManager] platform SinaWeibo has configured
[PlatformManager] platform QQ has configured
[PlatformManager] platform Facebook has configured
```
**说明:** 假如某个平台配置失败，会有 log 信息，例如：

```
[PlatformManager] QQ configure fail, please check project config:
make sure jshare-qq-android-v.x.y.jar has build in your project.
```

## 混淆配置
```
-dontwarn cn.jiguang.**
-keep class cn.jiguang.** { *; }
-dontwarn cn.jpush.**
-keep class cn.jpush.** { *; }
```

