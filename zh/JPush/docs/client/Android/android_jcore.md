# 定制JCore SDK集成指南
## 使用提示
本文是 JCore SDK 定制版的集成指南文档。用以指导 SDK 的使用方法，默认读者已经熟悉IDE（Eclipse 或者 Android Studio）的基本使用方法，以及具有一定的 Android 编程知识基础。
本篇指南匹配的 JCore Android SDK版本为 v1.1.3定制版
### jcore-android-1.x.y-release.zip 集成压缩包内容
+ AndroidManifest.xml
  + 客户端嵌入SDK参考的配置文件
+ libs/jcore-android-1.x.y.jar
  + 极光开发者服务的核心包。
+ libs/(cpu-type)/libjcore1xy.so
  + 各种CPU类型的native开发包。
+ 定制JCore SDK集成指南
  + 即本指南。
    ​    



## 手动集成步骤

+ 解压缩 jcore-android-1.x.y-release.zip 集成压缩包。
+ 复制 libs/jcore-android-1.x.y.jar 到工程 jniLibs/ 目录下或lib/下。
+ 复制 libs/(cpu-type)/libjcore1xy.so 到你的工程中存放对应cpu类型的目录下。  

***说明 1*** ：使用android studio的开发者，如果使用jniLibs文件夹导入so文件，则仅需将所有cpu类型的文件夹拷进去；如果将so文件添加在工程的libs文件夹下，注意在工程的gradle配置中添加一下配置：

```gradle
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
***说明 2***：此为定制版SDK，与标准版的JPush不兼容。如果你的工程里原本有标准版JPush的项目，再导入此SDK可能引发冲突，需要去除标准版SDK项目才能正常编译。



### 配置 AndroidManifest.xml

根据 SDK 压缩包里的 AndroidManifest.xml 样例文件，来配置应用程序项目的 AndroidManifest.xml 。
主要步骤为：
+ 复制备注为 "Required" 的部分
+ 将标注为“您应用的包名”的部分，替换为当前应用程序的包名
+ 将标注为“您应用的Appkey”的部分，替换为在Portal上注册该应用的的Key,例如：9fed5bcb7b9b87413678c407

**小帖士**
如果使用android studio, 可在AndroidManifest中引用applicationId的值，在build.gradle配置中 defaultConfig节点下配置，如：

```
defaultConfig {
      applicationId "cn.jpush.example" // <--您应用的包名
      ……
 }
```
在AndroidManifest中使用 ${applicationId} 引用gradle中定义的包名

**AndroidManifest 示例**

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您应用的包名">
    <permission
        android:name="您应用的包名.permission.JPUSH_MESSAGE"
        android:protectionLevel="signature" />
    <!-- Required 一些系统要求的权限，如访问网络等-->
    <uses-permission android:name="您应用的包名.permission.JPUSH_MESSAGE" />
    <uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <!-- Optional for location -->
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在6.0 系统上 层叠窗口权限 -->
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <!-- 用于同一设备中不同应用的JCore服务相互拉起的功能。 -->
        <!-- 若不启用该功能可删除该组件，将不拉起其他应用也不能被其他应用拉起 -->
        <service
            android:name="cn.jpush.android.service.DaemonService"
            android:enabled="true"
            android:exported="true">
            <intent-filter>
                <action android:name="cn.jpush.android.intent.DaemonService" />
                <category android:name="您应用的包名" />
            </intent-filter>
        </service>
        <!-- Required SDK 核心功能-->
        <!-- 可配置android:process参数将PushService放在其他进程中 -->
        <service
            android:name="cn.jpush.android.service.PushService"
            android:process=":mult">
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
            android:enabled="true">
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
        <receiver android:name="cn.jpush.android.service.AlarmReceiver" />
        <!-- Required . Enable it you can get statistics data with channel -->
        <meta-data
            android:name="JPUSH_CHANNEL"
            android:value="developer-default" />
        <meta-data
            android:name="JPUSH_APPKEY"
            android:value="您应用的Appkey" /> <!-- </>值来自开发者平台取得的AppKey -->
    </application>
</manifest>
```
​    



### 集成 JCore SDK 的混淆

+ 请下载4.x及以上版本的proguard.jar， 并替换你Android Sdk "tools\proguard\lib\proguard.jar"
+ 请在工程的混淆文件中添加以下配置：
  -dontoptimize
  -dontpreverify
  -dontwarn cn.jpush.**
  -keep class cn.jpush.** { *; }
  -dontwarn cn.jiguang.**
  -keep class cn.jiguang.** { *; }
  ​    



### 添加代码

JCore SDK 提供的 API 接口，都主要集中在 cn.jiguang.api.JCoreInterface 类里。
#### 基础API
+ init 初始化SDK

  ```Java
  public static void init(Context context)
  ```

+ setDebugMode 设置调试模式
  注：该接口需在init接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的Application中onCreate中调用。

  ```java
  public static void setDebugMode(boolean debugEnalbed)
  ```

  ​
#### 调用示例代码
init 只需要在应用程序启动时调用一次该 API 即可。
以下代码定制一个本应用程序 Application 类。需要在 AndoridManifest.xml 里配置。请参考上面 AndroidManifest.xml 片断，或者 example 项目。
```java
public class ExampleApplication extends Application {
@Override
    public void onCreate() {
        super.onCreate();
        JCoreInterface.setDebugMode(true);
        JCoreInterface.init(this);
    }
}
```
​    



## 测试确认

+ 确认所需的权限都已经添加。如果必须的权限未添加，日志会提示错误。
+ 确认 AppKey（在Portal上生成的）已经正确的写入 Androidmanifest.xml 。
+ 确认在程序启动时候调用了init(context) 接口
+ 确认测试手机（或者模拟器）已成功连入网络 
  + 客户端调用 init 后不久，如果一切正常，应有登录成功的日志信息
+ 启动应用程序，在 Portal 上向应用程序发送自定义消息或者通知栏提示。详情请参考管理Portal。
  + 在几秒内，客户端应可收到下发的通知或者正定义消息，如果 SDK 工作正常，则日志信息会如下：
```
[JCoreInterface] action:init
.......
[PushService] Login succeed!
```
如图所示，客户端启动分为 4 步：
+ 检查 metadata 的 appKey 和 channel ，如果不存在，则启动失败
+ 初始化 JCore SDK，检查 JNI 等库文件的有效性，如果库文件无效，则启动失败
+ 检查 Androidmanifest.xml，如果有 Required 的权限不存在，则启动失败
+ 连接服务器登录，如果存在网络问题，则登陆失败,或者前面三步有问题，不会启动SDK jcore-android-1.x.y-release.zip 集成压缩包内容