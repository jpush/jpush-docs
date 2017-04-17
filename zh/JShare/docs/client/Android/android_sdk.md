# Android JShare集成指南

##使用提示
本文是 JSHARE Android SDK 的标准集成指南文档。
匹配的 SDK 版本为：V1.0.0及以后版本。

* 如果你想要快速测试、请参考本文在几分钟内跑通 Demo。
* 极光文档官网上有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
* [极光社区](https://community.jiguang.cn/)网站：大家对文档有疑惑，以及产品出现问题，可以到极光社区来提问题，可以及时得到回应。

## 产品功能说明
JSHARE SDK 可以让你的应用支持多平台分享，无需花耗时间了解、集成每个社会化分享平台的 SDK，可以有效的降低包体积。

###主要场景：

* 将分享内容分享到 QQ、微信、新浪微博三个主要的社交平台。


### jshare-android-release-v1.x.y.zip 集成压缩包内容
* JGShareSDK.xml
	* 客户端嵌入SDK，各个平台配置的参考文件
* AndroidManifest.xml
	* 客户端嵌入SDK参考的配置文件
* libs/jcore-android.v1.x.y.jar
	* 极光开发者服务的核.心包。
* jshare-android_v1.x.y.jar
	* JShare SDK核心包
* jshare-wechat-android_v1.x.y.jar
	* JShare微信平台包
* jshare-qq-android_v1.x.y.jar
	* JShareQQ平台包
* jshare-sina-android_v1.x.y.jar
	* JShare新浪微博包
* libs/(cpu-type)/libjcore1xy.so
	* 各种CPU类型的native开发包。
* example
	* 是一个完整的Android项目，通过这个演示了JShare SDK的基本用法，可以用来做参考。  
	
### Android SDK 版本
JShare SDK支持Android 2.3及以上版本的Android系统。



##jcenter自动集成
**说明 ：** 使用jcenter自动集成的开发者，不需要在项目中添加jar和so，jcenter会自动完成依赖。

* 在gradle 配置jcenter。
* 配置JGShareSDK.xml文件。
* 配置微信回调（如不需要分享到微信，可跳过）
* 配置签名
* 参考example工程或者接口文档使用JShare SDK。

###gradle 配置

* 确认android studio的 Project 根目录的主 gradle 中配置了jcenter支持。（新建project默认配置就支持）

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
* 在 module 的 gradle 中添加依赖和AndroidManifest的替换变量。

```
android {
    ......
    defaultConfig {
        applicationId "com.xxx.xxx" //极光控制台创建应用时填写的应用包名.
        ......

        ndk {
            //选择要添加的对应cpu类型的.so库。
            abiFilters 'armeabi', 'armeabi-v7a', 'armeabi-v8a'
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [
            JSHARE_PKGNAME : applicationId,
            JPUSH_APPKEY : "你的appkey", //极光控制台创建应用得到的AppKey.
            JPUSH_CHANNEL : "developer-default", //暂时填写默认值即可.
            TENCENT_APPID: "QQ开发者应用的appID",//腾讯开放平台注册应用得到的appId
        ]
        ......
    }
    ......
}
dependencies {
    ......
    compile 'cn.jiguang.sdk:jshare:1.0.0'  // 此处以JShare 1.0.0 版本为例。
    compile 'cn.jiguang.sdk:jshare-qqmodel:1.0.0'  // 此处以jshare-qqmodel 1.0.0 版本为例。
    compile 'cn.jiguang.sdk:jshare-wechatmodel:1.0.0'  // 此处以jshare-wechatmodel 1.0.0 版本为例。
    compile 'cn.jiguang.sdk:jshare-sinamodel:1.0.0'  // 此处以jshare-sinamodel 1.0.0 版本为例。
    compile 'cn.jiguang.sdk:jcore:1.1.2'  // 此处以JCore 1.1.2版本为例。
    ......
}
```
**注 :** 如果在添加以上 abiFilter 配置之后android Studio出现以下提示：

```
NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.
```
则在 Project 根目录的gradle.properties文件中添加：

```
android.useDeprecatedNdk=true
```

##手动集成步骤
* 解压缩 jshare-android-release-1.x.y.zip 集成压缩包。
* 复制libs/jcore-android_v1.x.y.jar到工程libs目录下。
* 复制libs/jshare-android_v1.x.y.jar到工程libs目录下。
* 复制libs/(cpu-type)/libjcore1xy.so到你工程中存放对应cpu类型的目录下。
* 根据需要复制libs/jshare-xx.jar平台jar包到工程libs目录下。
* 按下面说明配置AndroidManifest.xml。
* 按以下说明配置JGShareSDK.xml文件。
* 配置微信回调（如不需要分享到微信，可跳过）
* 配置签名
* 参考example工程或者接口文档使用JShare SDK。

**说明 ：** 使用android studio的开发者，如果使用jniLibs文件夹导入so文件，则仅需将所有cpu类型的文件夹拷进去；
如果将so文件添加在module的libs文件夹下，注意在module的gradle配置中添加一下配置：

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
* 将标注为“您应用的Appkey”的部分，替换为在Portal上注册该应用的的Key,例如：
9fed5bcb7b9b87413678c407

####AndroidManifest 示例
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
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
		<activity android:name=".ShareTypeActivity"/>

		<!-- Required SDK核心功能-->
		<activity
			android:name="cn.jiguang.share.android.ui.JiguangShellActivity"
			android:configChanges="keyboardHidden|orientation|screenSize"
			android:exported="true"
			android:screenOrientation="portrait"
			android:theme="@android:style/Theme.Translucent.NoTitleBar"
			android:windowSoftInputMode="stateHidden|adjustResize">

			<!-- Optional QQ分享回调-->
            <!-- scheme为“tencent”前缀再加上QQ开发者应用的appID；例如appID为123456，则scheme＝“tencent123456” -->
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
		</activity>

		<!-- Optional 微信分享回调,wxapi必须在包名路径下，否则回调不成功-->
		<activity
			android:name=".wxapi.WXEntryActivity"
			android:exported="true" />

		<!-- Required. For publish channel feature -->
		<!-- JPUSH_CHANNEL 是为了方便开发者统计APK分发渠道。-->
		<!-- 例如: -->
		<!-- 发到 Google Play 的APK可以设置为 google-play; -->
		<!-- 发到其他市场的 APK 可以设置为 xxx-market。 -->
		<!-- 目前这个渠道统计功能的报表还未开放。-->
		<meta-data
			android:name="JPUSH_CHANNEL"
			android:value="developer-default" />
		<!-- Required. AppKey copied from Portal -->
		<meta-data
			android:name="JPUSH_APPKEY"
			android:value="您应用的Appkey" />

	</application>

</manifest>
```

## 配置 JGShareSDK.xml
无论是使用自动集成还是手动集成方式，都需要配置JGShareSDK.xml。
主要步骤为：

* 复制或者新建JGShareSDK.xml到工程目录的asset目录下。
* 把JGShareSDK.xml中相关的AppKey、AppSecret替换成自己在第三方平台创建的应用得到的信息。
* 根据需要配置各个平台，不需要的平台可以删除。

#### JGShareSDK.xml示例
```
<?xml version="1.0" encoding="utf-8"?>
<DevInfor>

    <!-- 如果不需要支持某平台，可缺省该平台的配置-->

    <SinaWeibo
        AppKey="新浪微博的AppKey"
        AppSecret="新浪微博ppSecret"/>

    <QQ
        AppId="QQ的AppId"
        AppKey="QQ的AppKey"/>

    <Wechat
        AppId="微信的AppId"
        AppSecret="微信的AppSectet"/>

</DevInfor>
```
## 配置微信平台回调
* 在你的包名相应目录下新建一个wxapi目录，并在该wxapi目录下新增一个WXEntryActivity类，该类继承自WeChatHandleActivity（例如应用程序的包名为cn.jiguang.share.demo，则新添加的类如下图所示）

![](http://i.imgur.com/2URxXFr.png)

**注意：** 如果复写了onCreate方法、onNewIntent方法，那么必须调用父类方法，否者无法获取分享结果，例如：

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
* 并在manifest文件里面加上exported属性，设置为true，例如：

```
<activity
    android:name=".wxapi.WXEntryActivity"
    android:exported="true" />
```



## 配置项目签名

### Android Studio图形界面签名配置
进入Project Structure，选择您集成JShare的项目，具体配置如图：

![](http://i.imgur.com/ahk1DoN.png)
![](http://i.imgur.com/2oh4IKp.png)

### Android Studio手动配置
* 在项目的build.gradle的android内部新增签名配置，例如：

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


* 然后在项目的build.gradle的buildTypes使用签名配置，例如：

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


###Eclipse环境配置

* 在Eclipse的Preferences，选择Android -> Build，如下图：

![](http://i.imgur.com/mKPb3De.png)

* 指定Custom debug keystore选项的路径为sdk demo工程目录中的debug.keystore文件，并应用该配置，如下图：
![](http://i.imgur.com/TgxykaK.png)

### 注意
* 应用的包名、应用的签名、第三方平台注册的AppID及Appkey三者要一一对应，否则会无法分享。
* 应用的签名要与在第三方平台填写的签名对应，否则会无法分享。
## 添加代码
JShare SDK 提供的 API 接口，都主要集中在 cn.jiguang.share.android.api.JShareInterface 类，使用方法请参考example或者API接口文档。

### API基础API
* init 初始化SDK

```
public static void init(Context context)
```
* setDebugMode 设置调试模式

```
public static void setDebugModel(boolean enable)
```
注：该接口需在init接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的Application中onCreate中调用。
### 测试确认
* 确认所需要的文件已经添加进工程
* 确认Androidmanifest.xml已经正确配置
* 确认JGShareSDK.xml已经正确配置
* 根据如下日志确定配置了什么平台

```
[PlatformManager] platform Wechat has configured
[PlatformManager] platform SinaWeibo has configured
[PlatformManager] platform QQ has configured
```
**说明:** 假如某个平台配置失败，会有log信息，例如：

```
[PlatformManager] QQ configure fail, please check project config:
make sure jshare-qq-android-v.x.y.jar has build in your project.
```

## 混淆配置
```
-dontwarn cn.jiguang.**
-keep class cn.jiguang.** { *; }
```

