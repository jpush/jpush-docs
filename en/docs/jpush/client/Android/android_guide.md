# Android SDK Integration Guide

## Use Suggestions

This article is an integration guide document for the JPush Android SDK standard. To guide the use of the SDK, we default that the reader is already familiar with the basic usage of the IDE (Eclipse or Android Studio) and has a certain knowledge base of Android programming.

This guide matches the JPush Android SDK version: 3.0.0 and later.

+ [3 Minutes Quick Demo (Android)](android_3m/): If you want to quickly test and feel the effect of JPush, please refer to this article to run Demo in minutes.
+ On [the JPush Document website](http://docs.jiguang.cn/), there are all documents related to JPush, including all guides, APIs, and tutorials. Updated versions of this document will be posted to the site in a timely manner.
+ If you see this document but have not yet [downloaded the Android SDK](http://docs.jiguang.cn/jpush/resources/), please visit the SDK download page to download it.

## Product Function Description

JPush is an end-to-end push service that enables server-side messages to be pushed to end-user mobile phones in a timely manner, allowing developers to actively maintain connections with users, thereby increasing user activity and improving application retention. JPush client supports Android and iOS platform.

This Android SDK makes it easy for developers to increase the push function to Android apps based on JPush.

### Main Functions

+ Maintain a long connection with the server so that messages can be pushed to the client instantly
+ Receive notifications and custom messages, and pass relevant information to developer App

### Main Features

+ The maintaining the connections of the client consumes less resources and power
+ Rich interface of SDK, customizable prompt style of thenotification bar 
+ Large capacity and stability of the server

### Integration package content of the Jpush-android-3.x.x-release.zip 

+ AndroidManifest.xml
    + Client embed the configuration file of SDK reference 
+ libs/jcore-android.1.x.x.jar
    + The core package of Jiguang Developer Services.
+ Libs/jpush-android-3.x.y.jar
    + Development Kit of JPush SDK
+ Libs/(cpu-type)/libjcore1xx.so
    + Native development kits for various CPU types.
+ res
    + Integrated resource files that the SDK must add
+ example
    + This is a complete Android project. This demonstrates the basic usage of the JPush SDK and can be used as a reference.

### Android SDK version

At present, the SDK only supports Android 2.3 or later mobile phone systems. The rich media stream function requires Android3.0 or later systems.

## Auto-integration Steps of Jcenter

***Description***: Developers who use jcenter auto-integration do not need to add jar and so in the project. jcenter will automatically complete the dependency; no need to add any JPush SDK related configuration in AndroidManifest.xml, jcenter will automatically import.

+ If the developer needs to modify component properties, he could define the component with the same name in the local AndroidManifest and configure the desired properties. Then he can use xmlns:tools to control the local component to override the component on jcenter. Example:

```   
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.android.tests.flavorlib.app"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:icon="@drawable/icon"
        android:name="com.example.jpushdemo.ExampleApplication"
        android:label="@string/app_name" >

        <service android:name="cn.jpush.android.service.PushService"
            android:process=":multiprocess"
            tools:node="replace" >

            ……
        </service>

    ……
  </application>

  ……
</manifest>
```

+ Verify that jcenter support is configured in the main gradle of the android studio's Project root directory. (Default configuration of new project supports)


```
buildscript {
    repositories {
        jcenter()
    }
    ......
}

allprojets {
    repositories {
        jcenter()
    }
}
```

+ Add dependency and substitution variables of AndroidManifest in the module's gradle.

```
android {
    ......
    defaultConfig {
        applicationId "com.xxx.xxx" //JPush上注册的包名.
        ......

        ndk {
            //选择要添加的对应cpu类型的.so库。
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        manifestPlaceholders = [
            JPUSH_PKGNAME : applicationId,
            JPUSH_APPKEY : "你的appkey", //JPush上注册的包名对应的appkey.
            JPUSH_CHANNEL : "developer-default", //暂时填写默认值即可.
        ]
        ......
    }
    ......
}

dependencies {
    ......

    compile 'cn.jiguang.sdk:jpush:3.1.1'  // 此处以JPush 3.1.1 版本为例。
    compile 'cn.jiguang.sdk:jcore:1.1.9'  // 此处以JCore 1.1.9 版本为例。
    ......
}
```
***Note***: If android Studio displays the following prompt after adding the above abiFilter configuration

    NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin

Then add the followings in the gradle.properties file of the Project root directory

    android.useDeprecatedNdk=true

***Note***: If there is no res/drawable-xxxx/jpush_notification_icon, the application icon default by resource, as notification icon, using application icon as statusbar icon in the system above 5.0 may not display properly. Instead, the user can define the icon without shadow and gradient color to replace this file, under the condition of file name unchanged.


## Manually Integration Steps

+ Unzip the jpush-android--3.x.x-release.zip integrated package.
+ Copy libs/jcore-android-1.x.x.jar to the project libs/ directory.
+ Copy libs/jpush-android-3.x.x.jar to the project libs/ directory.
+ Copy libs/(cpu-type)/libjcore1xy.so to your project and store it in the corresponding directory of cpu type.
+ Copy the resource file in res/ in the drawable-hdpi, layout, values folder to the corresponding directory with the same name as res/ in your project.

***Note 1***: If there is no res/drawable-xxxx/jpush_notification_icon, the application icon default by resource, as notification icon, using application icon as statusbar icon in the system above 5.0 may not display properly. Instead, the user can define the icon without shadow and gradient color to replace this file, under the condition of file name unchanged.

***Note 2***: If developers who apply android studio use the jniLibs folder to import the so file, he only needs to copy all the cpu type of folder into it; if he needs to add the so file in the module's libs folder, he should pay attention to the module's gradle Add configuration in the configuration:

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

### Configure AndroidManifest.xml

Configure the AndroidManifest.xml of the application project according to the AndroidManifest.xml sample file in the SDK archive.

The main steps are:

+ Copy the part with the comment "Required"
+ Replace the section labeled " package name of your application " with the package name of current application 
+ 9fed5bcb7b9b87413678c407 Replace the section labeled "AppKey for your app" with the key for registering the app on Portal, for example: 9fed5bcb7b9b87413678c407

**Tips**

If android studio is used, the value of applicationId can be referenced in the AndroidManifest and configured under the defaultConfig node in the build.gradle configuration. For example:
```
defaultConfig {
      applicationId "cn.jpush.example" // <--您应用的包名
      ……
 }
```

Use ${applicationId} in AndroidManifest to refer to the package name defined in gradle

**Example of AndroidManifest** 

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您应用的包名"
    android:versionCode="311"
    android:versionName="3.1.1"
    >
    <uses-sdk android:minSdkVersion="9" android:targetSdkVersion="23" />

    <!-- Required -->
    <permission
        android:name="您应用的包名.permission.JPUSH_MESSAGE"
        android:protectionLevel="signature" />

    <!-- Required -->
    <uses-permission android:name="您应用的包名.permission.JPUSH_MESSAGE" />
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
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在6.0 系统上 层叠窗口权限 -->
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />

    <application
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:name="Your Application Name">

        <!-- Required SDK 核心功能-->
        <!-- 可配置android:process参数将PushService放在其他进程中 -->
        <service
            android:name="cn.jpush.android.service.PushService"
            android:enabled="true"
            android:exported="false" >
            <intent-filter>
                <action android:name="cn.jpush.android.intent.REGISTER" />
                <action android:name="cn.jpush.android.intent.REPORT" />
                <action android:name="cn.jpush.android.intent.PushService" />
                <action android:name="cn.jpush.android.intent.PUSH_TIME" />
            </intent-filter>
        </service>


    <!-- since 3.0.9 Required SDK 核心功能-->
        <provider
            android:authorities="您应用的包名.DataProvider"
            android:name="cn.jpush.android.service.DataProvider"
            android:exported="true"
        />

        <!-- since 1.8.0 option 可选项。用于同一设备中不同应用的JPush服务相互拉起的功能。 -->
        <!-- 若不启用该功能可删除该组件，将不拉起其他应用也不能被其他应用拉起 -->
         <service
             android:name="cn.jpush.android.service.DaemonService"
             android:enabled="true"
             android:exported="true">
             <intent-filter >
                 <action android:name="cn.jpush.android.intent.DaemonService" />
                 <category android:name="您应用的包名"/>
             </intent-filter>
         </service>

         <!-- since 3.1.0 Required SDK 核心功能-->
          <provider
               android:authorities="您应用的包名.DownloadProvider"
               android:name="cn.jpush.android.service.DownloadProvider"
               android:exported="true"
           />

        <!-- Required SDK核心功能-->
        <receiver
            android:name="cn.jpush.android.service.PushReceiver"
            android:enabled="true" >
          <intent-filter android:priority="1000">
                <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED_PROXY" />
                <category android:name="您应用的包名"/>
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.USER_PRESENT" />
                <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
            </intent-filter>
            <!-- Optional -->
            <intent-filter>
                <action android:name="android.intent.action.PACKAGE_ADDED" />
                <action android:name="android.intent.action.PACKAGE_REMOVED" />
                <data android:scheme="package" />
            </intent-filter>
        </receiver>

        <!-- Required SDK核心功能-->
        <activity
            android:name="cn.jpush.android.ui.PushActivity"
            android:configChanges="orientation|keyboardHidden"
            android:theme="@android:style/Theme.NoTitleBar"
            android:exported="false" >
            <intent-filter>
                <action android:name="cn.jpush.android.ui.PushActivity" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="您应用的包名" />
            </intent-filter>
        </activity>
        <!-- SDK核心功能-->
        <activity
            android:name="cn.jpush.android.ui.PopWinActivity"
            android:configChanges="orientation|keyboardHidden"
            android:exported="false"
            android:theme="@style/MyDialogStyle">
            <intent-filter>
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="您应用的包名" />
            </intent-filter>
        </activity>

        <!-- Required SDK核心功能-->
        <service
            android:name="cn.jpush.android.service.DownloadService"
            android:enabled="true"
            android:exported="false" >
        </service>

        <!-- Required SDK核心功能-->
        <receiver android:name="cn.jpush.android.service.AlarmReceiver" />

        <!-- Required since 3.0.7 -->
        <!-- 新的tag/alias接口结果返回需要开发者配置一个自定的广播 -->
        <!-- 该广播需要继承JPush提供的JPushMessageReceiver类, 并如下新增一个 Intent-Filter -->
        <receiver
        android:name="自定义 Receiver"
        android:enabled="true" >
        <intent-filter>
        <action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE" />
        <category android:name="您应用的包名" />
        </intent-filter>
        </receiver>

        <!-- User defined. 用户自定义的广播接收器-->
         <receiver
             android:name="您自己定义的Receiver"
             android:enabled="true">
             <intent-filter>
                 <!--Required 用户注册SDK的intent-->
                 <action android:name="cn.jpush.android.intent.REGISTRATION" />
                 <!--Required 用户接收SDK消息的intent-->
                 <action android:name="cn.jpush.android.intent.MESSAGE_RECEIVED" />
                 <!--Required 用户接收SDK通知栏信息的intent-->
                 <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED" />
                 <!--Required 用户打开自定义通知栏的intent-->
                 <action android:name="cn.jpush.android.intent.NOTIFICATION_OPENED" />
                 <!-- 接收网络变化 连接/断开 since 1.6.3 -->
                 <action android:name="cn.jpush.android.intent.CONNECTION" />
                 <category android:name="您应用的包名" />
             </intent-filter>
         </receiver>

        <!-- Required. For publish channel feature -->
        <!-- JPUSH_CHANNEL 是为了方便开发者统计APK分发渠道。-->
        <!-- 例如: -->
        <!-- 发到 Google Play 的APK可以设置为 google-play; -->
        <!-- 发到其他市场的 APK 可以设置为 xxx-market。 -->
        <meta-data android:name="JPUSH_CHANNEL" android:value="developer-default"/>
        <!-- Required. AppKey copied from Portal -->
        <meta-data android:name="JPUSH_APPKEY" android:value="您应用的Appkey"/>
    </application>
</manifest>
```

## Configuration and Code Instructions

### Permissions must be interpreted 

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Permission</th>
      <th >Usage</th>
    </tr>
    <tr >
      <td>You Package.permission.JPUSH_MESSAGE</td>
      <td>Officially-defined permissions, allowing apps to receive broadcast messages sent by JPUSH's internal code.</td>
    </tr>
    <tr >
      <td>RECEIVE_USER_PRESENT</td>
      <td>Allow apps to receive lighted screens or unlock broadcasts.</td>
    </tr>
    <tr >
      <td>INTERNET</td>
      <td>Allow apps to access the web.</td>
    </tr>
    <tr >
      <td>WAKE_LOCK</td>
      <td>Allow apps to run after the phone screen is turned off.</td>
    </tr>
    <tr >
      <td>READ_PHONE_STATE</td>
      <td>Allow apps to access phone status.</td>
    </tr>
    <tr >
      <td>WRITE_EXTERNAL_STORAGE</td>
      <td>Allow apps to write to external storage.</td>
    </tr>
    <tr >
      <td>READ_EXTERNAL_STORAGE</td>
      <td>Allow apps to read external storage.</td>
    </tr>
    <tr >
      <td>WRITE_SETTINGS</td>
      <td>Allow apps to read and write system settings.</td>
    </tr>
    <tr >
      <td>VIBRATE</td>
      <td>Allow apps to vibrate.</td>
    </tr>
    <tr >
      <td>MOUNT_UNMOUNT_FILESYSTEMS</td>
      <td>Allow apps to mount/unmount external file systems.</td>
    </tr>
    <tr >
      <td>ACCESS_NETWORK_STATE</td>
      <td>Allow apps to obtain network information status, such as whether the current network connection is valid.</td>
    </tr>
  </table>
</div>

### Confusion of the Integrated JPush Android SDK

+ Please download 4.x and later versions of [proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/) and replace your Android Sdk "tools\proguard\lib\proguard.jar"
+ Please add the following configuration to the project's confusing file：

        -dontoptimize
        -dontpreverify

        -dontwarn cn.jpush.**
        -keep class cn.jpush.** { *; }
        -keep class * extends cn.jpush.android.helpers.JPushMessageReceiver { *; }

        -dontwarn cn.jiguang.**
        -keep class cn.jiguang.** { *; }

+ Versions 2.0.5 ~ 2.1.7 have introduced gson and protobuf to increase the elimination of confusion. (Version 2.1.8 does not need to be configured)

        #==================gson && protobuf==========================
        -dontwarn com.google.**
        -keep class com.google.gson.** {*;}
        -keep class com.google.protobuf.** {*;}
        
### Add code

The API interfaces provided by the JPush SDK are mainly focused on the cn.jpush.android.api.JPushInterface class.

#### Basic API

+ init initialization SDK

        public static void init(Context context)

+ setDebugMode set debug mode

Note: This interface needs to be called before the init interface to avoid the situation where some logs are not printed. In the case of multi-process, it is recommended to call onCreate in the custom Application.

    // You can enable debug mode in developing state. You should close debug mode when release.
    public static void setDebugMode(boolean debugEnalbed)

#### Add statistics code

+ References: [Statistical Analysis API](http://docs.jiguang.cn/jpush/client/Android/android_api/#api_2)

#### Call sample code (see example project)

+ init only needs to call this API once when the application starts
+ The following code could customize an application. Need to be configured in AndoridManifest.xml. Please refer to the AndroidManifest.xml fragment above, or the example project.

```
public class ExampleApplication extends Application {
@Override
    public void onCreate() {
        super.onCreate();
        JPushInterface.setDebugMode(true);
        JPushInterface.init(this);
    }
}
```

### Test confirmation

+ Verify that the required permissions have been added. If the necessary permissions are not added, the log will indicate an error.
+ Verify that the AppKey (generated on the Portal) has been correctly written to Androidmanifest.xml
+ Make sure that the init(context) interface is called when the program starts
+ Confirm that the test handset (or emulator) has successfully connected to the network 
    + Shortly after the client invokes init, if everything is OK, there should be log information on login successful
+ Launch the application and send a custom message or notification bar prompt to the application on the portal. For details, please refer to the management [Portal](../../console/Instructions)
    + Within a few seconds, the client should be able to receive the delivered notification or defined message. If the SDK works, the log information will be as follows：

```
[JPushInterface] action:init

.......

[PushService] Login succeed!
```

As shown in the figure, startup of the client is divided into 4 steps:

+ Check the appKey and channel of metadata. If it does not exist, the startup fails
+ Initialize the JPush SDK to check the validity of library files such as JNI. If the library file is invalid, the startup fails
+ Check Androidmanifest.xml. If permissions for Required do not exist, the startup fails
+ JPush SDK Connect the server to login. If there is a network problem, the login fails, or if there are problems in the first three steps, JPush SDK will not start

## Advanced Features

Please refer to:

[API: Android](android_api)

## Technical Support

Email us at [support&#64;jpush.cn](mailto:support&#64;jpush.cn)
