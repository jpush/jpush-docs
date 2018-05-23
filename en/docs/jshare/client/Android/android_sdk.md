# Android JShare Integration Guide

## Use Suggestions

This article is a standard integration guide document for the JShare Android SDK. The matching SDK version is V1.0.0 and later.

* If you want a quick test, please refer to this article to run through the Demo within minutes.
* All documents, including all guides, APIs, and tutorials, are available on the Jiguang Doc website. Updated versions of this document will be posted to the site in a timely manner.
* Jiguang Community Website: If you have doubts about the documents and problems with the products, you can ask questions in the Jiguang community and you will receive respond in a timely manner.

## Description of Product Function 

JShare SDK allows your application to support multi-platform sharing. It does not take time to understand and integrate the SDK of each social sharing platform, which can effectively reduce the package size.

### Main Scenes：

* Share the sharing content to major social platforms such as QQ, WeChat, Sina Weibo, Facebook, and Twitter.
* Access to key platforms such as QQ, WeChat, Sina Weibo, Facebook and Twitter.
* Access personal information on QQ, WeChat, Sina Weibo, Facebook, Twitter and other major platforms for third party login.

### Content of jshare-android-1.x.y-release.zip

* JGShareSDK.xml
o	Reference file embedded SDK configuration of each platform in client
* AndroidManifest.xml
o	Configuration file embedded SDK reference in client.
* libs/jcore-android-1.x.y.jar
o	Core package of Jiguang Developer Services
* jshare-android-1.x.y.jar
o	JShare SDK core package
* jshare-wechat-android-1.x.y.jar
o	JShare WeChat platform packagge
* jshare-qq-android-1.x.y.jar
o	JShare QQ platform package
* jshare-sina-android-1.x.y.jar
o	JShare Sina Weibo package
* jshare-facebook-android-1.x.y.jar
o	JShareFacebook platform package
* jshare-twitter-android-1.x.y.jar
o	JShare Twitter platform package
* libs/(cpu-type)/libjcore1xy.so
o	Native development kits for various CPU types.
* example
o	It is a complete Android project that demonstrates the basic usage of the JShare SDK and can be used as a reference.

### Android SDK Version

JShare SDK supports Android 2.3 and above Android systems.

## Jcenter Automatic Integration

**Note:** Developers who use jcenter auto-integration do not need to add jar and so in the project. Jcenter will automatically complete the dependencies.

* Configure jcenter in gradle.
* Configure third-party platform information.
* Configure WeChat callbacks (if you do not need to share with WeChat, skip it).
* Configure project signatures.
* • Refer to the example project or interface documentation to use the JShare SDK.

### Configuration of gradle

* Verify that jcenter support is configured in the main gradle of the android studio's Project root. (Default configuration of new project is supported)
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
            //选择要添加的对应 cpu 类型的.so 库。
            abiFilters 'armeabi', 'armeabi-v7a', 'armeabi-v8a'
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [
            JSHARE_PKGNAME : applicationId,
            JPUSH_APPKEY : "你的 appkey", //极光控制台创建应用得到的 AppKey.
            JPUSH_CHANNEL : "developer-default", //暂时填写默认值即可.
            TENCENT_APPID: " QQ 开发者应用的 appID ",//腾讯开放平台注册应用得到的 appId
            FACEBOOK_APPID: " facebook 开发者应用的 appID ",// facebook 注册应用得到的 appId
        ]
        ......
    }
    ......
}
dependencies {
    ......
    compile 'cn.jiguang.sdk:jshare:1.5.0'  // 此处以 JShare 1.5.0 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-qqmodel:1.5.0'  // 此处以 jshare-qqmodel 1.5.0  版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-wechatmodel:1.5.0'  // 此处以 jshare-wechatmodel 1.5.0  版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-sinamodel:1.5.0'  // 此处以 jshare-sinamodel 1.5.0  版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-facebookmodel:1.5.0'  // 此处以 jshare-facebookmodel 1.5.0  版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jshare-twittermodel:1.5.0'  // 此处以 jshare-twittermodel 1.5.0  版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    compile 'cn.jiguang.sdk:jcore:1.1.7'  // 此处以 JCore 1.1.7 版本为例，具体版本请参考压缩包 libs 的 jar 包版本。
    ......
}
```

**Note:** If android Studio displays the following prompt after adding the above abiFilter configuration:

```
NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.
```
Then add the below code in the gradle.properties file of the Project root directory:
```
android.useDeprecatedNdk=true
```

## Manual Integration Steps

* Unzip jshare-android-1.x.y-release.zip 
* Copy libs/jcore-android-1.x.y.jar to the libs directory of project.
* Copy libs/jshare-android-1.x.y.jar to the libs directory of project.
* Copy libs/(cpu-type)/libjcore1xy.so to the directory where your project stored the corresponding cpu type.
* Copy the jar package of libs/jshare-xx.jar platform to the libs directory of project as needed.
* Configure AndroidManifest.xml as described below.
* Configure third-party platform information.
* Configure WeChat callbacks (if you do not need to share with WeChat, skip it).
* Configure project signatures
* Refer to example project or interface documentation to use the JShare SDK.

**Note:** Developers using android studio, if using the jniLibs folder to import so files, he only needs to copy in all cpu type folders; if so files are added to libs folder of the module, pay attention to add the following configuration in the gradle configuration of the module:

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

### Configure AndroidManifest.xml

Configure the AndroidManifest.xml of the application project according to the AndroidManifest.xml sample file in the SDK archive.

* Copy the part with the comment "Required"
* Replace the section labeled "Package name of your application" with the current application package
* Replace the section labeled "AppKey for your application" with the key for registering the application on the portal, for example: 9fed5bcb7b9b87413678c407

#### Example of AndroidManifest
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
            <!-- scheme为“tencent” 前缀再加上 QQ 开发者应用的 appID；例如 appID为123456，则 scheme＝“tencent123456” -->
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

            <!-- Optional 新浪微博私信回调 -->
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="jsharesdk" android:host="sinaweibo"/>
            </intent-filter>
        </activity>

        <!-- Optional 微信分享回调,wxapi 必须在包名路径下，否则回调不成功 -->
        <activity
            android:name=".wxapi.WXEntryActivity"
             android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:exported="true" />

        <!-- Optional facebook 配置,authorities 必须为 com.facebook.app.FacebookContentProvider+APP_ID -->
        <provider
            android:authorities="com.facebook.app.FacebookContentProvider 您申请的 facebook 的 AppId"
            android:name="cn.jiguang.share.facebook.FacebookContentProvider"
            android:exported="true"
        />

        <!-- User defined.  For test only  用户自定义的广播接收器 -->
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

## Configure Third-party Platform Information

The 1.5.0 release supports two methods for configuring third-party platform information： 

1、 Configure JGShareSDK.xml； 
2、 Set in the code. Developers should choose one of the methods. Versions prior to 1.5.0 only supports the configuration of JGShareSDK.xml.

### JGShareSDK.xml configures third-party platform information

Whether you use automatic integration or manual integration, you need to configure JGShareSDK.xml. The main steps are：

* Copy or create JGShareSDK.xml into the asset directory of the project directory.
* Replace the relevant AppKeys and AppSecrets in JGShareSDK.xml with the information obtained by your own applications created on third-party platforms.
* Configure each platform as needed. Unwanted platforms can be deleted.

#### Example of JGShareSDK.xml
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

    <Twitter
        ConsumerKey="twitter 的 ConsumerKey"
        ConsumerSecret="twitter 的 ConsumerSecret"
    />

</DevInfor>
```

### Code sets third-party platform information
For details, see [SDK Initialization API](https://docs.jiguang.cn/jshare/client/Android/android_api/#api_1)  and [Third-Party Platform Information Settings API](https://docs.jiguang.cn/jshare/client/Android/android_api/#api_2);

## Configure Callbacks of WeChat Platform 

* Create a wxapi directory in the corresponding directory of your package name, and add a WXEntryActivity class under the wxapi directory. This class inherits from WeChatHandleActivity (For example, if the package name of application is cn.jiguang.share.demo, the new class added is shown as below)

![](http://i.imgur.com/2URxXFr.png)


**Note:** If you overwrite the onCreate method, onNewIntent method, you must call the parent method, otherwise you cannot get the result of sharing, for example：

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
* Add exported attribute in the manifest file with the set to true, for example：

```
<activity
    android:name=".wxapi.WXEntryActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:exported="true" />
```

## Configure Facebook Platform
* Add the ContentProvider configuration of Facebook in the manifest file

```
<provider
    android:authorities="com.facebook.app.FacebookContentProvider 您申请的 facebook的AppId"
    android:name="cn.jiguang.share.facebook.FacebookContentProvider"
    android:exported="true"
/>
```

**Note:** The authorities of provider must be "com.facebook.app.FacebookContentProvider"+"AppId"

* If need to get the results of uploaded pictures and videos on facebook, you can be customize BroadCastReceiver, inherit FacebookBroadcastReceiver, and overwrite onSuccessfulAppCall, onFailedAppCall method：

```
<receiver android:name="cn.jiguang.share.demo.FaceBookUploadReceiver">
    <intent-filter>
        <action android:name="com.facebook.platform.AppCallResultBroadcast" />
    </intent-filter>
</receiver>
```

**Note:** The action of the receiver must be  "com.facebook.platform.AppCallResultBroadcast"。

## Configure Project Signature

### Signature Configuration of Android Studio Graphical Interface

Enter Project Structure and select your project to integrate JShare. See specific configuration as below：

![](http://i.imgur.com/ahk1DoN.png)
![](http://i.imgur.com/2oh4IKp.png)


### Manual Configuration of Android Studio
* Add signature configuration inside the android of project's build.gradle, for example：

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

* Then use the signature configuration in buildTypes of the project's build.gradle , for example：

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

### Environment Configuration of Eclipse

* In the Preferences of Eclipse, select Android -> Build, as shown below:：

![](http://i.imgur.com/mKPb3De.png)

* Specify the path of the Custom debug keystore option as the debug.keystore file in the directory of sdk demo project and apply the configuration as shown below:

![](http://i.imgur.com/TgxykaK.png)

### Note

* The application package name, application signature, AppID and AppKey registered by the third-party platform must be in one-to-one correspondence. Otherwise, sharing will fail.
* The signature of the application must correspond to the signature filled in on the third-party platform, otherwise it will not be shared.
* Sina Weibo supports sharing without installing client. Note that RedirectUrl in JGShareSDK.xml must be consistent with the information on Weibo open platform. Otherwise, an error will occur.

## Add Code
The API interfaces provided by the JShare SDK are mainly focused on the cn.jiguang.share.android.api.JShareInterface class. For usage, refer to the example or the API interface documentation.

### Basic API
* init initialization SDK

```
public static void init(Context context)
```
* init initialization SDK. Versions after 1.5.0 support setting third-party platform information in the code

```
public static void init(Context context, PlatformConfig platformConfig)
```
* setDebugMode

```
public static void setDebugMode(boolean enable)
```
Note: This interface needs to be called before the init interface to avoid the situation where some logs are not printed. In the case of multi-process, it is recommended to call in onCreate in the custom Application.
### Test Confirmation
* Confirm that the required files have been added to the project.
* Confirm that Androidmanifest.xml is properly configured.
* Confirm that the third-party platform information is correctly configured.
* Determine which platform is configured based on the following logs.
* Confirm that the application's package name and signature are the same as the information filled in the third-party background.

```
[PlatformManager] platform Wechat has configured
[PlatformManager] platform SinaWeibo has configured
[PlatformManager] platform QQ has configured
[PlatformManager] platform Facebook has configured
[PlatformManager] platform Twitter has configured
```

**Note:** If configuration of a platform fails, there will be log information, for example:

```
[PlatformManager] QQ configure fail, please check project config:
make sure jshare-qq-android-v.x.y.jar has build in your project.
```

## Obfuscation Configuration
```
-dontwarn cn.jiguang.**
-keep class cn.jiguang.** { *; }
-dontwarn cn.jpush.**
-keep class cn.jpush.** { *; }
-keep public class com.sina.** {
    *;
}
```
