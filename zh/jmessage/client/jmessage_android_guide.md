# Android SDK 集成指南

## 使用提示

本文是 JMessage Android SDK 标准的集成指南文档。用以指导 SDK 的使用方法，默认读者已经熟悉IDE（Eclipse 或者 Android Studio）的基本使用方法，以及具有一定的 Android 编程知识基础。

本篇指南匹配的 JMessage Android SDK 版本为：2.0.0 及以后版本。

+ [极光文档](https://docs.jiguang.cn/jmessage/guideline/jmessage_guide/)网站上有JMessage相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
+ 如果您看到本文档，但还未下载Android SDK，请访问[SDK下载页面](https://docs.jiguang.cn/jmessage/resources/)下载。


### JMessage SDK压缩包内容简介

+ demo/
	+ 一个用来展示JMessage SDK接口基本用法的demo应用。
+ doc/
	+ JMessage sdk中所包含所有对外接口的java doc。
+ libs/jcore-android_v1.X.Y.jar
	+ 极光开发者服务的核心包。
+ libs/jmessage-android-2.X.Y.jar
	+ JMessage SDK开发包
+ libs/(cpu-type)/libjcore1xy.so 
    + 各种CPU类型的native开发包。

### Android SDK 版本

目前SDK只支持Android 2.3或以上版本的手机系统。

## jcenter 自动集成步骤


***说明*** ： JMessage从2.1.2版本开始支持jcenter自动集成，使用jcenter自动集成的开发者，不需要在项目中添加jar和so，jcenter会自动完成依赖；在AndroidManifest.xml中不需要添加任何JPush SDK 相关的配置，jcenter会自动导入。

+ 如果开发者需要修改组件属性，可以在本地的 AndroidManifest 中定义同名的组件并配置想要的属性，然后用 xmlns:tools 来控制本地组件覆盖 jcenter 上的组件。示例：

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


+ 确认android studio的 Project 根目录的主 gradle 中配置了jcenter支持。（新建project默认配置就支持）
        
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
              
        
        
+ 在 module 的 gradle 中添加依赖和AndroidManifest的替换变量。


        
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
            
            compile 'cn.jiguang.sdk:jmessage:2.3.0'  // 此处以JMessage 2.3.0 版本为例。
            compile 'cn.jiguang.sdk:jcore:1.1.7'  // 此处以JCore 1.1.7 版本为例。
            ......
        }
        
        
***注*** : 如果在添加以上 abiFilter 配置之后android Studio出现以下提示：

        NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin.
则在 Project 根目录的gradle.properties文件中添加：

        android.useDeprecatedNdk=true


## 手动集成步骤

+ 解压缩 jmessage-sdk-android-2.X.Y.zip 集成压缩包。
+ 复制 libs/jcore-android_v1.X.Y.jar 到工程 libs/ 目录下。
+ 复制 libs/jmessage-android_2.X.Y.jar 到工程 libs/ 目录下。
+ 复制 libs/(cpu-type)/libjcore1xy.so 到你的工程中存放对应cpu类型的目录下。


***说明***：使用android studio的开发者，如果使用jniLibs文件夹导入so文件，则仅需将所有cpu类型的文件夹拷进去；如果将so文件添加在module的libs文件夹下，注意在module的gradle配置中添加一下配置：

       
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

### 配置 AndroidManifest.xml

根据 SDK 压缩包里demo中的 AndroidManifest.xml 样例文件，来配置应用程序项目的 AndroidManifest.xml 。

主要步骤为：

+ 复制备注为 "Required" 的部分
+ 将标注为“您应用的包名”的部分，替换为当前应用程序的包名
+ 将标注为“您应用的Appkey”的部分，替换为在Portal上注册该应用的的Key,例如：9fed5bcb7b9b87413678c407

**小帖士**

如果使用android studio, 可在AndroidManifest中引用applicationId的值，在build.gradle配置中 defaultConfig节点下配置，如：

```
defaultConfig {
      applicationId "cn.jmessage.example" // <--您应用的包名
      ……
 }

```

在AndroidManifest中使用 ${applicationId} 引用gradle中定义的包名


**AndroidManifest 示例**

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
            <intent-filter android:priority="1000">
                <action android:name="cn.jpush.im.android.action.IM_RESPONSE" />
                <action android:name="cn.jpush.im.android.action.NOTIFICATION_CLICK_PROXY" />

                <category android:name="您自己的包名" />
            </intent-filter>
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

### 必须权限说明

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >权限</th>
      <th >用途</th>
    </tr>
    <tr >
      <td>Your Package.permission.JPUSH_MESSAGE</td>
      <td>官方定义的权限，允许应用接收JPUSH内部代码发送的广播消息。</td>
    </tr>
    <tr >
      <td>RECEIVE_USER_PRESENT</td>
      <td>允许应用可以接收点亮屏幕或解锁广播。</td>
    </tr>
    <tr >
      <td>INTERNET</td>
      <td>允许应用可以访问网络。</td>
    </tr>
    <tr >
      <td>WAKE_LOCK</td>
      <td>允许应用在手机屏幕关闭后后台进程仍然运行</td>
    </tr>
    <tr >
      <td>READ_PHONE_STATE</td>
      <td>允许应用访问手机状态。</td>
    </tr>
    <tr >
      <td>WRITE_EXTERNAL_STORAGE</td>
      <td>允许应用写入外部存储。</td>
    </tr>
    <tr >
      <td>READ_EXTERNAL_STORAGE</td>
      <td>允许应用读取外部存储。</td>
    </tr>
    <tr >
      <td>WRITE_SETTINGS</td>
      <td>允许应用读写系统设置项。</td>
    </tr>
    <tr >
      <td>VIBRATE</td>
      <td>允许应用震动。</td>
    </tr>
    <tr >
      <td>MOUNT_UNMOUNT_FILESYSTEMS</td>
      <td>允许应用挂载/卸载 外部文件系统。</td>
    </tr>
    <tr >
      <td>ACCESS_NETWORK_STATE</td>
      <td>允许应用获取网络信息状态，如当前的网络连接是否有效。</td>
    </tr>
  </table>
</div>


### 添加代码

#### 基础API
+ setDebugMode 设置调试模式

        // You can enable debug mode in developing state. You should close debug mode when release.
        JMessageClient.setDebugMode(boolean debugEnalbed)

+ init 初始化SDK
        
        JMessageClient.init(Context context)
        

#### 调用示例代码（参考 example 项目）

+ init 只需要在应用程序启动时调用一次即可。

+ 以下代码定制一个本应用程序 Application 类。需要在 AndoridManifest.xml 里配置。请参考上面 AndroidManifest.xml 片断，或者 demo 项目。

    
        public class IMDebugApplication extends Application {
        @Override
            public void onCreate() {
                super.onCreate();
                JMessageClient.setDebugMode(true);
                JMessageClient.init(this);
            }
        }


### 测试确认

+ 确认所需的权限都已经添加。如果必须的权限未添加，日志会提示错误。
+ 确认 AppKey（在Portal上生成的）已经正确的写入 Androidmanifest.xml 。
+ 确认在程序启动时候调用了init(context) 接口
+ 确认测试手机（或者模拟器）已成功连入网络
    ＋ 客户端调用 init 后不久，如果一切正常，应有长连接登陆成功的日志信息,日志信息会如下:

```
[JMessageClient] JMessage SDK init finished!

.......

[ConnectingHelper] Login succeed!
```

如图所示，客户端启动分为 4 步：

+ 检查 metadata 的 appKey 和 channel ，如果不存在，则启动失败
+ 初始化 JMessage SDK，检查 JNI 等库文件的有效性，如果库文件无效，则启动失败
+ 检查 Androidmanifest.xml，如果有 Required 的权限不存在，则启动失败
+ 连接服务器登录，如果存在网络问题，则长连接登陆失败,或者前面三步有问题，不会启动  
JMessage SDK

## 集成时注意

因为从JMessage 2.0.0版本开始jar包的结构和之前发生了一些变化， 集成时有一些注意事项开发者需要注意
### 如果之前集成过JMessage
对于集成过JMessage 2.0.0以前版本的开发者,之前的JMessage是包含了Push的完整功能的，所以仅需要集成JMessage一个包就能同时拥有JMessage和JPush的完整功能。  

而新的JMessage 2.0.0将**不再包含JPush的功能**。JMessage和JPush今后将会作为两个相对独立的模块需要分别集成。所以对于之前已经集成过JMessage（2.0.0版本以前）的开发者，将JMessage升级到2.0.0之后，如果还需要使用JPush相关功能，请参照[JPush3.0.0的集成文档][3]将JPush集成进项目。  

</br>
**基于JMessage手动集成JPush时注意事项：**

+ 版本要求：对应的JCore需要1.1.0或以上版本，JPush需要3.0.0或以上版本。
+ jcore的替换：下载下来的JPush SDK zip包中同样包含了名为jcore-android_v1.X.Y的jar包,集成时需要注意项目中只保留一个jcore的jar就好，如果出现JPush和JMessage中所包含的jcore jar包版本不一致的情况，则保留版本号更新的那一个。so文件同理。
+ Manifest的配置：关于manifest中必要组件的配置，因为JMessage和JPush的manifest示例中包含了一部分公共的组件配置，对于已经集成JMessage 2.0.0（及以上）的开发者，仅需要将其中JPush部分的组件配置复制过来就好，包括（但不仅限以下组件，可能根据JPush之后版本变化而有不同，具体请参考[JPush3.0.0的集成文档][3]）：

	+ cn.jpush.android.service.DaemonService
	+ cn.jpush.android.ui.PushActivity
	+ cn.jpush.android.service.DownloadService
	+ cn.jpush.android.ui.PopWinActivity
	+ JPush用户的自定义广播接收器（需要的话）

+ 别忘了添加JPush SDK中的res资源
+ 加上JPush的初始化代码：JPushInterface.init(context)


### 如果之前集成过JPush
对于已经集成了JPush 3.0.0或以上版本的开发者，如果需要IM功能，直接参照上面"jcenter自动集成步骤"或“手动集成步骤”一节配置JMessage就好，其中有以下几项需要注意：

</br>
**基于JPush手动集成JMessage时注意事项：**

+ 版本要求：JCore需要1.1.0或以上版本，对应的JMessage需要2.0.0或以上版本。
+ jcore的替换：下载下来的JMessage SDK zip包中同样包含了名为jcore-android_v1.X.Y的jar包,集成时需要注意项目中只保留一个jcore的jar就好，如果出现JPush和JMessage中所包含的jcore jar包版本不一致的情况，则保留版本号更新的那一个。so文件同理
+ Manifest的配置：因为JMessage和JPush的manifest示例中包含了一部分公共的组件配置，对于已经集成JPush 3.0.0（及以上）的开发者，仅需要将其中JMessage部分的组件配置复制过来就好，包括（但不仅限以下组件，可能根据JMessage之后版本变化而有改动，具体参照上文中的“AndroidManifest 示例”)

	+  cn.jpush.im.android.helpers.IMReceiver

+ 加上JMessage的初始化代码：JMessageClient.init(context)



## JMessage混淆

+ 请下载4.x版本的[proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/)， 并替换你Android Sdk "tools\proguard\lib\proguard.jar"


+ 请在工程的混淆文件中添加以下配置：

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

    

## IM场景代码样例

极光 JMessage 提供了一个完整的IM场景下的应用JChat，它就是一个 IM App。如果你的 App 需求只是 IM 功能，做以下两个变更就可以把它变成你自己的 IM App 了：

+ 换 Logo 
+ 在 JPush Web 控制台上注册应用，获取到的 Appkey 更新到 JChat 里

[JChat Android 项目源代码](https://github.com/jpush/jchat-android/)，开源放在 Github 上，供大家下载参考。


## 技术支持

邮件联系：[support@jiguang.cn][4]


[3]: https://docs.jiguang.cn/jpush/client/Android/android_guide/
[4]: mailto:support@jiguang.cn





