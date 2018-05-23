# Android SDK Integration Guide

## Use Suggestions

This article is an integration guide document for the JMessage Android SDK standard, which is used to guide the use of the SDK. The default reader is developers who are already familiar with the basic usage of the IDE (Eclipse or Android Studio) and have a certain knowledge base of Android programming.

JMessage Android SDK version matched with this guide matches is: 2.0.0 and later.

+ [The JIGUANG Documentation](https://docs.jiguang.cn/jmessage/guideline/jmessage_guide/) has all the JMessage-related guides, APIs, tutorials, and all other documents. Updated versions of this document will be posted to the site in a timely manner.
+ If you see this document but have not yet [downloaded the Android SDK](https://docs.jiguang.cn/jmessage/resources/), please visit the SDK download page to download it.

### Brief introduction of JMessage SDK package

+ demo/
    + A demo application to demonstrate the basic usage of the JMessage SDK interface
+ doc/
    + Java doc for all external interfaces contained in the JMessage sdk.
+ libs/jcore-android_v1.X.Y.jar
    + The core package of Jiguang Developer Services.
+ libs/jmessage-android-2.X.Y.jar
    + JMessage SDK Development Kit
+ libs/(cpu-type)/libjcore1xy.so
    + Native development kits for various CPU types.

### Android SDK version

At present, the SDK only supports Android 2.3 or later mobile phone systems.

## Automatic Integration Steps of jcenter

***Instructions***: JMessage supports jcenter automatic integration since version 2.1.2. Developers who use jcenter automatic integration do not need to add jar and so in the project, and jcenter will automatically complete the dependency; he does nor need to add any configuration related to JPush SDK in AndroidManifest.xml neither, instead, jcenter will automatically import them.

+ If the developer needs to modify component properties, he can define the component with the same name in the local AndroidManifest and configure the desired properties. Then use xmlns:tools to control the local component to override the component on jcenter. Example:

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

+ Confirm that jcenter support is configured in the main gradle of the android studio's Project root directory. (Support if new project defaults the configuration)

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

+ Add substitution variables of dependency and AndroidManifest in gradle of module

```
android {
    ......
    defaultConfig {
        applicationId "com.xxx.xxx" //JPush上注册的包名.
        ......

        ndk {
            //选择要添加的对应cpu类型的.so库。 
            abiFilters 'armeabi', 'armeabi-v7a', 'armeabi-v8a' 
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

    compile 'cn.jiguang.sdk:jmessage:2.5.0'  // 此处以JMessage 2.5.0 版本为例。
    compile 'cn.jiguang.sdk:jcore:1.1.9'  // 此处以JCore 1.1.9 版本为例。
    ......
}
```

***Note***: If android Studio displays the following prompt after adding the above abiFilter configuration:

    NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.

Then add the below in the gradle.properties file of the Project root directory

    android.useDeprecatedNdk=true

## Manually Integration Steps

+ Unzip the jmessage-sdk-android-2.X.Y.zip integrated archive.
+ Copy libs/jcore-android_v1.X.Y.jar to the project libs/ directory.
+ Copy libs/jmessage-android_2.X.Y.jar to the project libs/ directory.
+ Copy libs/(cpu-type)/libjcore1xy.so to the corresponding cpu type directory of your project

***Instruction***: For the developer using android studio, if he uses the jniLibs folder to import the so file, he only needs to copy all the cpu type folder into; if the so file is added in the module's libs folder, pay attention to add the following configuration in the gradle configuration of module:

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

Configure the AndroidManifest.xml of the application project according to the AndroidManifest.xml sample file in the demo of the SDK archive.

The main steps are:

+ Copy the part with the comment "Required"
+ Replace the section labeled "package name of your application" with the current application package name
+ Replace the section labeled “AppKey for your app” with the key for registering the app on Portal, for example: 9fed5bcb7b9b87413678c407

**Tips**

If android studio is used, the value of applicationId can be referenced in the AndroidManifest and configured under the defaultConfig node in the build.gradle configuration. For example:

```
defaultConfig {
      applicationId "cn.jmessage.example" // <--您应用的包名
      ……
 }
```

Use ${applicationId} in AndroidManifest to refer to the package name defined in gradle

**AndroidManifest example**

```
<?xml version="1.0" encoding="utf-8"?>
<manifest package="您自己的包名"
          xmlns:android="http://schemas.android.com/apk/res/android"
          android:versionCode="2"
          android:versionName="1.0.1">

    <permission
        android:name="您自己的包名.permission.JPUSH_MESSAGE"
        android:protectionLevel="signature"/>

    <!-- Required -->
    <uses-permission android:name="您自己的包名.permission.JPUSH_MESSAGE" />
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
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />

    <application
        android:name="Your Application Name"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name">

        <!-- Required SDK 核心功能-->
        <!-- 可配置android:process参数将PushService放在其他进程中 -->
        <service
            android:name="cn.jpush.android.service.PushService"
            android:enabled="true"
            android:exported="false">
            <intent-filter>
                <action android:name="cn.jpush.android.intent.REGISTER" />
                <action android:name="cn.jpush.android.intent.REPORT" />
                <action android:name="cn.jpush.android.intent.PushService" />
                <action android:name="cn.jpush.android.intent.PUSH_TIME" />
            </intent-filter>
        </service>

        <!-- Required SDK核心功能-->
        <receiver
            android:name="cn.jpush.android.service.PushReceiver"
            android:enabled="true"
            android:exported="false">
            <intent-filter android:priority="1000">
                <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED_PROXY" />
                <category android:name="您自己的包名" />
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
        <receiver
            android:name="cn.jpush.android.service.AlarmReceiver"
            android:exported="false" />

        <!-- Required since JCore 1.1.7. SDK 核心功能-->
        <provider
            android:name="cn.jpush.android.service.DataProvider"
            android:authorities="您自己的包名.DataProvider"
            android:exported="true" />

        <!-- Required JMessage SDK核心功能-->
        <receiver
            android:name="cn.jpush.im.android.helpers.IMReceiver"
            android:enabled="true"
            android:exported="false">
        </receiver>

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
            android:value="您自己的appkey" />

    </application>

</manifest>
```

### Required permissions description

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Authority</th>
      <th >Use</th>
    </tr>
    <tr >
      <td>Your Package.permission.JPUSH_MESSAGE</td>
      <td>Officially defined permissions allow the application to receive broadcast messages sent by the JPUSH internal code.</td>
    </tr>
    <tr >
      <td>RECEIVE_USER_PRESENT</td>
      <td>Allows the app to receive lighted screens or unlock broadcasts.</td>
    </tr>
    <tr >
      <td>INTERNET</td>
      <td>Allows apps to access the web.</td>
    </tr>
    <tr >
      <td>WAKE_LOCK</td>
      <td>Allows the app to run after the phone screen is turned off</td>
    </tr>
    <tr >
      <td>READ_PHONE_STATE</td>
      <td>Allows the app to access the phone's status.</td>
    </tr>
    <tr >
      <td>WRITE_EXTERNAL_STORAGE</td>
      <td>Allows the application to write to external storage.</td>
    </tr>
    <tr >
      <td>READ_EXTERNAL_STORAGE</td>
      <td>Allows the app to read external storage.</td>
    </tr>
    <tr >
      <td>WRITE_SETTINGS</td>
      <td>Allows the application to read and write system settings.</td>
    </tr>
    <tr >
      <td>VIBRATE</td>
      <td>Allows the application to vibrate.</td>
    </tr>
    <tr >
      <td>MOUNT_UNMOUNT_FILESYSTEMS</td>
      <td>Allows the app to mount/unmount external file systems.</td>
    </tr>
    <tr >
      <td>ACCESS_NETWORK_STATE</td>
      <td>Allows the app to obtain network information status, such as whether the current network connection is valid.</td>
    </tr>
  </table>
</div>


### Add code

#### Basic API

+ setDebugMode  set debug mode

```
// You can enable debug mode in developing state. You should close debug mode when release.
JMessageClient.setDebugMode(boolean debugEnalbed)
```

+ init  initialization SDK

```
JMessageClient.init(Context context)
```

#### Call sample code (see example project)

+ init only needs to be called once at application startup

+ The following code customizes an Application class, and needs to be configured in AndoridManifest.xml. Please refer to the AndroidManifest.xml fragment above, or the demo project.

```
public class IMDebugApplication extends Application {
@Override
    public void onCreate() {
        super.onCreate();
        JMessageClient.setDebugMode(true);
        JMessageClient.init(this);
    }
}
```

### Test confirmation

+ Verify that the required permissions have been added. If the necessary permissions are not added, the log will indicate an error.
+ Verify that the AppKey (generated on the Portal) has been correctly written to Androidmanifest.xml.
+ Verify that the init(context) interface is called when the program starts
+ Verify that the test phone (or emulator) has successfully connected to the network + client shortly after the init invoked. If everything is ok, there should be log information for the long connection of logging in successfully. The log information will be as follows:

```
[JMessageClient] JMessage SDK init finished!

.......

[ConnectingHelper] Login succeed!
```

As shown in the figure, the client startup is divided into 4 steps:

+ Check the appKey and channel of metadata. If it does not exist, the startup fails
+ Initialize the JMessage SDK to check the validity of library files such as JNI. If the library file is invalid, the startup fails.
+ Check Androidmanifest.xml. If permissions for Required do not exist, the startup fails.
+ Connect server to login in. If there is a network problem, the long connection login fails, or if there are problems in the first three steps, JMessage SDK won’t be initiated.

## Points to Note When Integrating

Since the structure of the jar package has changed from the JMessage 2.0.0 version, there are some considerations for integration developers need to pay attention to

### If you previously integrated JMessage

For developers who previously integrated versions before JMessage 2.0.0, the previous JMessage contained the full functionality of Push, so he only needs to integrates JMessage to obtain the full functionality of both JMessage and JPush.

The new JMessage 2.0.0 will **no longer include the functionality of JPush**. JMessage and JPush will be integrated separately as two relatively independent modules in the future. Therefore, for developers who have integrated JMessage (pre-2.0.0 version) before, if he needs to use JPush related functions after updating JMessage to 2.0.0, please refer to [the JPush3.0.0 Integration Document][3] to integrate JPush into the project.

</br>
**Points to note when manually integrating JPush based on JMessage:**

+ Version requirements: The corresponding JCore requires version 1.1.0 or later, and JPush requires version 3.0.0 or later.
+ Replacement of jcore: The downloaded JPush SDK zip package also contains a jar package named jcore-android_v1.XY. When integrating, you need to pay attention to only save one jcore jar in the project. If the version of the jcore jar package in JPush and JMessage is inconsistent, then just save the updated version. So file likewise.
+ Manifest configuration: For configuration of the necessary components in the manifest, since manifest examples  of JMessage and JPush contain some common component configurations, developers who have integrated JMessage 2.0.0 (and above), only need to copy the component configuration of JPush part, including (but not limited to the following components, may vary according to the later JPush version, please refer to the Integration Document of JPush3.0.0):

    + cn.jpush.android.service.DaemonService
    + cn.jpush.android.ui.PushActivity
    + cn.jpush.android.service.DownloadService
    + cn.jpush.android.ui.PopWinActivity
    + custom broadcast receiver of JPush user (if needed)

+ Don't forget to add the res resource in the JPush SDK
+ Plus initial code of JPush: JPushInterface.init(context)

### If you previously integrated JPush

If developers who have integrated JPush 3.0.0 or above，need the IM function, he can directly configure the JMessage by referring to the above "jcenter automatic integration procedure" or "manual integration procedure" section, among which the following items need be pay attention to:

</br>

**Points to note when manually integrating JMessage based on JPush:**

+ Version requirements: JCore requires version 1.1.0 or later, and the corresponding JMessage requires version 2.0.0 or later.
+ Replacement of jcore: The downloaded JMessage SDK zip package also contains a jar package named jcore-android_v1.XY. When integrating, you need to pay attention to only save one jcore jar in the project. If the version of the jcore jar package in JPush and JMessage is inconsistent, then just save the updated version. So file likewise.
+ Configuration of Manifest: Because manifest examples of JMessage and JPush contain some common component configurations, developers who already integrate JPush 3.0.0 (and above), just need to copy the component configuration of the JMessage section, which includes (but not limited to the following components, may change according to the JMessage after the version changes, specifically refer to the "AndroidManifest example" above)

    + cn.jpush.im.android.helpers.IMReceiver
    
+ Plus initialization code of JMessage: JMessageClient.init(context)

## JMessage Obfuscation

+ Please download the 4.x version of proguard.jar and replace your Android Sdk "tools\proguard\lib\proguard.jar"

+ Add the following configuration to the project's obfuscated file

```
-dontoptimize
-dontpreverify
-keepattributes  EnclosingMethod,Signature
-dontwarn cn.jpush.**
-keep class cn.jpush.** { *; }

-dontwarn cn.jiguang.**
-keep class cn.jiguang.** { *; }

 -keepclassmembers class ** {
     public void onEvent*(**);
 }

#========================gson================================
-dontwarn com.google.**
-keep class com.google.gson.** {*;}

#========================protobuf================================
-keep class com.google.protobuf.** {*;}
```

## Sample of IM Scene Code

JMessage provides a complete JChat application under the IM scenario. It is an IM App. If you only need IM features, you can turn it into your own IM App with the following two changes:

+ Change Logo
+ Register your app on the JPush web console and update Appkey obtained to JChat

[JChat Android Project Source Code](https://github.com/jpush/jchat-android/), open source on Github, for your reference.

## Technical Support

E-mail us at: [support@jiguang.cn][4]


[3]: https://docs.jiguang.cn/jpush/client/Android/android_guide/
[4]: mailto:support@jiguang.cn
