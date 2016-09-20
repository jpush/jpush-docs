# JMessage Android SDK 集成指南

### 文档说明

JMessage SDK 是基于 JPush SDK 开发的，完整支持 JPush 推送的全部功能。所以 IM SDK 的集成，是在 Push SDK 的集成操作基础上，附加少量的步骤来完成。

如果您之前未集成 JPush SDK（推送SDK），请参考其集成文档：[JPush Android SDK 集成指南](../../guideline/android_guide/)

在上述文档基础上，需要如下几个集成操作：

+ 复制 IM SDK jar 包文件：jmessage-sdk-v1.X.X.jar
+ 修改 AndroidManifest.xml 文件
+ 代码初始化

以上步骤以下详述。

#### jar 包文件

把 JMessage SDK 的 jar 包文件，放到您的应用工程里 libs/ 目录下。文件名规格如：

    jmessage-sdk-android-1.x.x.jar

其中 1.x.x 为版本号。随着版本升级，这个版本号会变更。

如果您的应用之前集成过 JPush (推送) SDK，则需要删除原来的 jar 包文件。如果这 2 个文件同时存在，Android 编译器会报错。

#### 修改 AndroidManifest.xml 文件

基于 JPush SDK 文档里描述的需要增加的部分，JMessage SDK 需要多加如下的关于广播的配置项。

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您自己的包名"
    android:versionCode="XX"
    android:versionName="XX">

<permission
        android:name="您自己的包名.permission.JPUSH_MESSAGE"
        android:protectionLevel="signature" />

<!--Required 一些系统要求的权限，如访问网络等-->
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
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />

<!-- Required SDK 核心功能-->
        <!-- option since 2.0.5 可配置PushService，DaemonService,PushReceiver,AlarmReceiver的android:process参数 将JPush相关组件设置为一个独立进程 -->
        <!-- 如：android:process=":remote" -->
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

<!-- since 1.1.4 option 可选项。用于同一设备中不同应用的JPush服务相互拉起的功能。 -->
<!-- 若不启用该功能可删除该组件，将不拉起其他应用也不能被其他应用拉起 -->
         <service
             android:name="cn.jpush.android.service.DaemonService"
             android:enabled="true"
             android:exported="true">
             <intent-filter >
                 <action android:name="cn.jpush.android.intent.DaemonService" />
                 <category android:name="您自己的包名"/>
             </intent-filter>
         </service>

<!-- Required Push SDK核心功能-->
        <receiver
            android:name="cn.jpush.android.service.PushReceiver"
            android:enabled="true">
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

<!-- Required Push SDK核心功能 -->
        <activity
            android:name="cn.jpush.android.ui.PushActivity"
            android:configChanges="orientation|keyboardHidden"
            android:theme="@android:style/Theme.Translucent.NoTitleBar">
            <intent-filter>
                <action android:name="cn.jpush.android.ui.PushActivity" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="您自己的包名" />
            </intent-filter>
        </activity>
<!-- Required Push SDK核心功能 -->
        <service
            android:name="cn.jpush.android.service.DownloadService"
            android:enabled="true"
            android:exported="false" />
<!-- Required Push SDK核心功能 -->
        <receiver android:name="cn.jpush.android.service.AlarmReceiver" />

<!-- IM Required IM SDK核心功能-->
        <receiver
            android:name="cn.jpush.im.android.helpers.IMReceiver"
            android:enabled="true"
            android:exported="false">
            <intent-filter android:priority="1000">
                <action android:name="cn.jpush.im.android.action.IM_RESPONSE" />
                <action android:name="cn.jpush.im.android.action.NOTIFICATION_CLICK_PROXY" />

                <category android:name="您自己的包名" />
            </intent-filter>
        </receiver>

<!-- Required. Enable it you can get statistics data with channel -->
        <meta-data
            android:name="JPUSH_CHANNEL"
            android:value="developer-default" />
<!-- Required. AppKey copied from Portal -->
        <meta-data
            android:name="JPUSH_APPKEY"
            android:value="您的APPKey" />
```
其中 category 部分的包名，应改为您应用的包名。

#### 代码初始化

在应用的自定义 Application 的 onCreate 方法里，加上如下的代码段，来初始化 JMessage SDK。

```
@Override
public void onCreate() {
    super.onCreate();
    Log.i("JMessageDemoApplication", "Application onCreate");
   
    JMessageClient.init(getApplicationContext());
    JPushInterface.setDebugMode(true);
}
```

**JPushInterface.init 方法不可缺少**

上述代码，即在原 JPush SDK 初始化调 JPushInterface.init 位置，替换为 JMessageClient.ini 方法，其他一样。



### 功能

#### Demo App

极光 IM SDK 提供一个完整的 Demo App，它就是一个 IM App。或者说，如果你的 App 需求只是 IM 功能，可以只做这样两个变更就是你自己的 IM App 了：

+ 换 Logo； 
+ 在 JPush Web 控制台上注册应用，获取到的 Appkey 更新到 Demo App 里。


#### IM 混淆

+ 请下载4.x版本的[proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/)， 并替换你Android Sdk "tools\proguard\lib\proguard.jar"

+ 在你的proguard.cfg加上代码：如果是使用新版本的ADT 将project.properties的中“# proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt”的“#”注释去掉，然后在proguard-android.txt中配置

```
-dontwarn cn.jpush.**
-keepattributes  EnclosingMethod,Signature
-keep class cn.jpush.** { *; }
-keepclassmembers class ** {
    public void onEvent*(**);
}

#========================gson================================
-dontwarn com.google.**
-keep class com.google.gson.** {*;}

#========================protobuf================================
#-dontwarn com.google.**
-keep class com.google.protobuf.** {*;}

```
    
<br />
