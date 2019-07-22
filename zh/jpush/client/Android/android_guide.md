# Android SDK 集成指南

## 使用提示

本文是 JPush Android SDK 标准的集成指南文档。用以指导 SDK 的使用方法，默认读者已经熟悉 IDE（Eclipse 或者 Android Studio）的基本使用方法，以及具有一定的 Android 编程知识基础。

本篇指南匹配的 JPush Android SDK 版本为：3.0.0 及以后版本。

+ [3 分钟快速 Demo（Android）](android_3m/)：如果您想要快速地测试、感受下极光推送的效果，请参考本文在几分钟内跑通 Demo。
+ 极光推送[文档网站](http://docs.jiguang.cn/)上，有极光推送相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
+ 如果您看到本文档，但还未下载 Android SDK，请访问[ SDK 下载页面](http://docs.jiguang.cn/jpush/resources/)下载。

## 产品功能说明

极光推送（JPush）是一个端到端的推送服务，使得服务器端消息能够及时地推送到终端用户手机上，让开发者积极地保持与用户的连接，从而提高用户活跃度、提高应用的留存率。极光推送客户端支持 Android，iOS 两个平台。

本 Android SDK 方便开发者基于 JPush 来快捷地为 Android App 增加推送功能。

### 主要功能

+ 保持与服务器的长连接，以便消息能够即时推送到达客户端
+ 接收通知与自定义消息，并向开发者 App 传递相关信息

### 主要特点

+ 客户端维持连接占用资源少、耗电低
+ SDK 丰富的接口，可定制通知栏提示样式
+ 服务器大容量、稳定

### jpush-android-3.x.x-release.zip 集成压缩包内容

+ AndroidManifest.xml
    + 客户端嵌入 SDK 参考的配置文件
+ libs/jcore-android.x.x.x.jar
    + 极光开发者服务的核心包。
+ libs/jpush-android-3.x.y.jar
    + JPush SDK 开发包。
+ libs/(cpu-type)/libjcore1xx.so
    + 各种 CPU 类型的 native 开发包。
+ res
    + 集成 SDK 必须添加的资源文件
+ example
    + 是一个完整的 Android 项目，通过这个演示了 JPush SDK 的基本用法，可以用来做参考。


### SDK 所支持的 Android 系统版本

目前 SDK 只支持 Android 2.3 或以上版本的手机系统。

富媒体信息流功能则需 Android 3.0 或以上版本的系统。


## jcenter 自动集成步骤


***说明*** ： 使用 jcenter 自动集成的开发者，不需要在项目中添加 jar 和 so，jcenter 会自动完成依赖；在 AndroidManifest.xml 中不需要添加任何 JPush SDK 相关的配置，jcenter 会自动导入。

>***注意*** ：如果需要处理收到的消息、使用 3.0.7 版本支持的别名与标签的新接口，AndroidManifest 中的自定义广播接收器仍需开发者手动配置，参考 SDK 压缩包里的 AndroidManifest.xml 样例文件。

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


+ 确认 android studio 的 Project 根目录的主 gradle 中配置了 jcenter 支持。（新建 project 默认配置就支持）

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



+ 在 module 的 gradle 中添加依赖和 AndroidManifest 的替换变量。



        android {
            ......
            defaultConfig {
                applicationId "com.xxx.xxx" //JPush 上注册的包名.
                ......

                ndk {
                    //选择要添加的对应 cpu 类型的 .so 库。
                    abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a'
                    // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
                }

                manifestPlaceholders = [
                    JPUSH_PKGNAME : applicationId,
                    JPUSH_APPKEY : "你的 Appkey ", //JPush 上注册的包名对应的 Appkey.
                    JPUSH_CHANNEL : "developer-default", //暂时填写默认值即可.
                ]
                ......
            }
            ......
        }


        dependencies {
            ......

            compile 'cn.jiguang.sdk:jpush:3.3.4'  // 此处以JPush 3.3.4 版本为例。
            compile 'cn.jiguang.sdk:jcore:2.1.2'  // 此处以JCore 2.1.2 版本为例。
            ......
        }

      ***注*** : **如果你使用的 JCore 是 2.0.0 及以上的版本，需要额外在 Androidmanifest 中配置一个Service**，以在更多手机平台上获得更稳定的支持，示例如下。（JCore1.x版本不需要）
	
	     <!-- Since JCore2.0.0 Required SDK核心功能-->
	     <!-- 可配置android:process参数将Service放在其他进程中；android:enabled属性不能是false -->
         <!-- 这个是自定义Service，要继承极光JCommonService，可以在更多手机平台上使得推送通道保持的更稳定 -->
	     <service android:name="xx.xx.XService"
                 android:enabled="true"
                 android:exported="false"
                 android:process=":pushcore">
                 <intent-filter>
                     <action android:name="cn.jiguang.user.service.action" />
                 </intent-filter>
         </service>    
         
      ***注*** : **从JPush3.0.7开始，需要配置继承JPushMessageReceiver的广播，原来如果配了MyReceiver现在可以弃用。示例如下。

         <!-- Required since 3.0.7 -->
         <!-- 新的 tag/alias 接口结果返回需要开发者配置一个自定的广播 -->
         <!-- 3.3.0开始所有事件将通过该类回调 -->
         <!-- 该广播需要继承 JPush 提供的 JPushMessageReceiver 类, 并如下新增一个 Intent-Filter -->
         <receiver
               android:name="自定义 Receiver"
               android:enabled="true" 
               android:exported="false" >
               <intent-filter>
                    <action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE" />
                    <category android:name="您应用的包名" />
               </intent-filter>
         </receiver>


***注*** : 如果在添加以上 abiFilter 配置之后 android Studio 出现以下提示：

    NDK integration is deprecated in the current plugin. Consider trying the new experimental plugin

则在 Project 根目录的 gradle.properties 文件中添加：

        android.useDeprecatedNdk=true

***注*** : 使用 NDK r17 时，可能 Android Studio 会出现以下提示：

        A problem occurred starting process ‘command 
        ‘/Users/xxx/Library/Android/sdk/ndk-bundle/toolchains/mips64el-linux-android-4.9/prebuilt
        /darwin-x86_64/bin/mips64el-linux-android-strip”
        
        系统找不到指定的文件

这是因为 NDK r17 之后不再支持 mips 平台，在 build.gradle 里增加如下配置可解决

        android {
        
            defaultConfig {
                .....
            }
            
            packagingOptions { 
                doNotStrip '*/mips/*.so' 
                doNotStrip '*/mips64/*.so' 
            }
        }
        


***说明***：若没有 res/drawable-xxxx/jpush_notification_icon 这个资源默认使用应用图标作为通知 icon，在 5.0 以上系统将应用图标作为 statusbar icon 可能显示不正常，用户可定义没有阴影和渐变色的 icon 替换这个文件，文件名不要变。


## 手动集成步骤

+ 解压缩 jpush-android--3.x.x-release.zip 集成压缩包。
+ 复制 libs/jcore-android-x.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/jpush-android-3.x.x.jar 到工程 libs/ 目录下。
+ 复制 libs/(cpu-type)/libjcore1xy.so 到你的工程中存放对应 cpu 类型的目录下。
+ 复制 res/ 中 drawable-hdpi, layout, values 文件夹中的资源文件到你的工程中 res/ 对应同名的目录下。

***说明 1***：若没有 res/drawable-xxxx/jpush_notification_icon 这个资源默认使用应用图标作为通知 icon，在 5.0 以上系统将应用图标作为 statusbar icon 可能显示不正常，用户可定义没有阴影和渐变色的 icon 替换这个文件，文件名不要变。

***说明 2***：使用 android studio 的开发者，如果使用 jniLibs 文件夹导入 so 文件，则仅需将所有 cpu 类型的文件夹拷进去；如果将 so 文件添加在 module的libs 文件夹下，注意在 module 的 gradle 配置中添加一下配置：


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

根据 SDK 压缩包里的 AndroidManifest.xml 样例文件，来配置应用程序项目的 AndroidManifest.xml 。

主要步骤为：

+ 复制备注为 "Required" 的部分
+ 将标注为“您应用的包名”的部分，替换为当前应用程序的包名
+ 将标注为“您应用的 Appkey” 的部分，替换为在 Portal 上创建该应用后应用信息中的 Appkey，例如：9fed5bcb7b9b87413678c407

**小帖士**

如果使用 android studio，可在 AndroidManifest 中引用 applicationId 的值，在 build.gradle 配置中 defaultConfig 节点下配置，如：

```
defaultConfig {
      applicationId "cn.jpush.example" // <--您应用的包名
      ……
 }
```
在 AndroidManifest 中使用 ${applicationId} 引用 gradle 中定义的包名

**AndroidManifest 示例**

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您应用的包名"
    android:versionCode="316"
    android:versionName="3.1.6"
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
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />

    <!-- Optional. Required for location feature -->
    <uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" /> <!-- 用于开启 debug 版本的应用在 6.0 系统上的层叠窗口权限 -->
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
    <uses-permission android:name="android.permission.GET_TASKS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    

    <application
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:name="Your Application Name">

        <!-- Required SDK 核心功能-->
        <!-- 可配置 android:process 参数将 PushService 放在其他进程中 -->
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

        <!-- since 1.8.0 option 可选项。用于同一设备中不同应用的 JPush 服务相互拉起的功能。 -->
        <!-- 若不启用该功能可删除该组件，或把 enabled 设置成 false ；App 不会被其他 App 拉起，但会拉起其他的 App。 -->
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

        <!-- Required SDK 核心功能-->
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

        <!-- Required SDK 核心功能-->
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
        <!-- SDK 核心功能-->
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

        <!-- 注意此配置在 JPush 3.2.0 及以前版本是必须配置，3.2.0 以后版本已废弃此配置-->
        <service
            android:name="cn.jpush.android.service.DownloadService"
            android:enabled="true"
            android:exported="false" >
        </service>
        
        <!-- Since JCore2.0.0 Required SDK核心功能-->
	    <!-- 可配置android:process参数将Service放在其他进程中；android:enabled属性不能是false -->
        <!-- 这个是自定义Service，要继承极光JCommonService，可以在更多手机平台上使得推送通道保持的更稳定 -->
         <service android:name="xx.xx.XService"
                 android:enabled="true"
                 android:exported="false"
                 android:process=":pushcore">
                 <intent-filter>
                     <action android:name="cn.jiguang.user.service.action" />
                 </intent-filter>
         </service>

        <!-- Required SDK 核心功能-->
        <receiver android:name="cn.jpush.android.service.AlarmReceiver" />

        <!-- Required since 3.0.7 -->
        <!-- 新的 tag/alias 接口结果返回需要开发者配置一个自定的广播 -->
        <!-- 3.3.0开始所有事件将通过该类回调 -->
        <!-- 该广播需要继承 JPush 提供的 JPushMessageReceiver 类, 并如下新增一个 Intent-Filter -->
        <receiver
            android:name="自定义 Receiver"
            android:enabled="true" 
            android:exported="false" >
            <intent-filter>
                <action android:name="cn.jpush.android.intent.RECEIVE_MESSAGE" />
                <category android:name="您应用的包名" />
            </intent-filter>
        </receiver>

        <!-- User defined. 用户自定义的广播接收器-->
        <!-- 这是3.3.0之前版本的接收方式，3.3.0开始是通过继承 JPushMessageReceiver并配置来接收所有事件回调。>
        <!-- 如果仍然需要在这个Receiver里接收，需要在JPushMessageReceiver 的子类里不重写对应的回调方法，或者重写方法且调用super-->
         <receiver
             android:name="您自己定义的 Receiver"
             android:enabled="true"
             android:exported="false">
             <intent-filter>
                 <!--Required 用户注册 SDK 的 intent-->
                 <action android:name="cn.jpush.android.intent.REGISTRATION" />
                 <!--Required 用户接收 SDK 消息的 intent-->
                 <action android:name="cn.jpush.android.intent.MESSAGE_RECEIVED" />
                 <!--Required 用户接收 SDK 通知栏信息的 intent-->
                 <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED" />
                 <!--Required 用户打开自定义通知栏的 intent-->
                 <action android:name="cn.jpush.android.intent.NOTIFICATION_OPENED" />
                 <!-- 接收网络变化 连接/断开 since 1.6.3 -->
                 <action android:name="cn.jpush.android.intent.CONNECTION" />
                 <category android:name="您应用的包名" />
             </intent-filter>
         </receiver>
        
        <!-- User defined. 用户自定义 Receiver 接收被拉起回调-->
        <!-- 自定义 Receiver 组件，继承cn.jpush.android.service.WakedResultReceiver类,复写onWake(int wakeType)或 onWake(Context context, int wakeType)方法以监听被拉起 -->
         <receiver android:name="xx.xx.xx.MyWakedResultReceiver">
            <intent-filter>
                <action android:name="cn.jpush.android.intent.WakedReceiver" />
                <category android:name="${applicationId}" />
            </intent-filter>
        </receiver>
        
        <!--Required SDK核心功能 since 3.3.0-->
        <activity
            android:name="cn.jpush.android.service.JNotifyActivity"
            android:exported="true"
            android:taskAffinity="jpush.custom"
            android:theme="@android:style/Theme.Translucent.NoTitleBar">
            <intent-filter>
                <action android:name="cn.jpush.android.intent.JNotifyActivity" />
                <category android:name="您应用的包名" />
            </intent-filter>
        </activity>

        <!-- Required. For publish channel feature -->
        <!-- JPUSH_CHANNEL 是为了方便开发者统计 APK 分发渠道。-->
        <!-- 例如: -->
        <!-- 发到 Google Play 的 APK 可以设置为 google-play; -->
        <!-- 发到其他市场的 APK 可以设置为 xxx-market。 -->
        <meta-data android:name="JPUSH_CHANNEL" android:value="developer-default"/>
        <!-- Required. AppKey copied from Portal -->
        <meta-data android:name="JPUSH_APPKEY" android:value="您应用的 Appkey"/>
    </application>
</manifest>
```


## 配置和代码说明


### 必须权限说明

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >权限</th>
      <th >用途</th>
    </tr>
    <tr >
      <td>You Package.permission.JPUSH_MESSAGE</td>
      <td>官方定义的权限，允许应用接收 JPush 内部代码发送的广播消息。</td>
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
      <td>允许应用在手机屏幕关闭后后台进程仍然运行； 该权限从 JPush 3.1.5 版本开始变为可选权限，在 3.1.5 前的版本为必须权限。</td>
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
      <td>允许应用读取系统设置项。 该权限从 JPush 3.3.2 版本开始变为可选权限，在 3.3.2 前版本为必须权限。</td>
    </tr>
    <tr >
      <td>VIBRATE</td>
      <td>允许应用震动。 该权限从 JPush 3.1.5 版本开始变为可选权限，在 3.1.5 前版本为必须权限。</td>
    </tr>
    <tr >
      <td>MOUNT_UNMOUNT_FILESYSTEMS</td>
      <td>允许应用挂载/卸载外部文件系统。</td>
    </tr>
    <tr >
      <td>ACCESS_NETWORK_STATE</td>
      <td>允许应用获取网络信息状态，如当前的网络连接是否有效。</td>
    </tr>
  </table>
</div>

### 集成 JPush Android SDK 的混淆

+ 请下载 4.x 及以上版本的 [proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/)， 并替换你 Android SDK "tools\proguard\lib\proguard.jar"

+ 请在工程的混淆文件中添加以下配置：

        -dontoptimize
        -dontpreverify

        -dontwarn cn.jpush.**
        -keep class cn.jpush.** { *; }
        -keep class * extends cn.jpush.android.helpers.JPushMessageReceiver { *; }

        -dontwarn cn.jiguang.**
        -keep class cn.jiguang.** { *; }


+ 2.0.5 ~ 2.1.7 版本有引入 gson 和 protobuf，增加排除混淆的配置。（2.1.8 版本不需配置）

        #==================gson && protobuf==========================
        -dontwarn com.google.**
        -keep class com.google.gson.** {*;}
        -keep class com.google.protobuf.** {*;}



### 添加代码

JPush SDK 提供的 API 接口，都主要集中在 cn.jpush.android.api.JPushInterface 类里。

#### 基础API
+ init 初始化 SDK

        public static void init(Context context)

+ setDebugMode 设置调试模式

 注：该接口需在 init 接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的 Application 中 onCreate 中调用。

        // You can enable debug mode in developing state. You should close debug mode when release.
        public static void setDebugMode(boolean debugEnalbed)

#### 添加统计代码

+ 参考文档： [统计分析 API](http://docs.jiguang.cn/jpush/client/Android/android_api/#api_4)

#### 调用示例代码（参考 example 项目）

+ init 只需要在应用程序启动时调用一次该 API 即可。

+ 以下代码定制一个本应用程序 Application 类。需要在 AndoridManifest.xml 里配置。请参考上面 AndroidManifest.xml 片断，或者 example 项目。


        public class ExampleApplication extends Application {
        @Override
            public void onCreate() {
                super.onCreate();
                JPushInterface.setDebugMode(true);
                JPushInterface.init(this);
            }
        }



### 测试确认

+ 确认所需的权限都已经添加。如果必须的权限未添加，日志会提示错误。
+ 确认 AppKey（在 Portal 上生成的）已经正确的写入 Androidmanifest.xml 。
+ 确认在程序启动时候调用了 init（context）接口
+ 确认测试手机（或者模拟器）已成功连入网络
    ＋ 客户端调用 init 后不久，如果一切正常，应有登录成功的日志信息
+ 启动应用程序，在 Portal 上向应用程序发送自定义消息或者通知栏提示。详情请参考管理 [Portal](../../console/Instructions)。
    + 在几秒内，客户端应可收到下发的通知或者正定义消息，如果 SDK 工作正常，则日志信息会如下：

```
[JPushInterface] action:init
.......
[ConnectingHelper] Login succeed
```

如图所示，客户端启动分为 4 步：

+ 检查 metadata 的 appKey 和 channel，如果不存在，则启动失败
+ 初始化 JPush SDK，检查 JNI 等库文件的有效性，如果库文件无效，则启动失败
+ 检查 Androidmanifest.xml，如果有 Required 的权限不存在，则启动失败
+ 连接服务器登录，如果存在网络问题，则登陆失败，或者前面三步有问题，不会启动 JPush SDK

## 集成 FCM 通道
### 概述

Firebase 云消息传递（FCM）是由 Google 提供的推送服务，可以在服务器和用户设备之间建立可靠而且省电的连接，提高推送送达率。

JPush SDK 为了尽可能提高开发者在国外设备的推送送达率，对集成 FCM 的设备推送，自动切换到 FCM 通道。同时，为了保证 SDK 的易用性，原本 JPush 的所有接口调用逻辑都不用修改，JPush 会对自身支持的功能做兼容。

### 功能描述
+ FCM 集成完成后，在支持的设备上自动进行初始化。

+ FCM 可以与 JPush 和 其他三方通道 共存。

+ FCM 通道初始化后支持 tag/alias 这些 JPush 原有的功能，其它的 JPush 未支持的功能目前暂时还不可用。

### 集成方式
+ 开发者需要自行在 [Firebase](https://firebase.google.com/) 平台注册账号和应用 id；
+ 开发者需要开通极光推送的 vip 服务，提供 Firebase 平台的应用信息，我们来开通通道；

具体的开通方式和资费情况，请 [联系商务](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc) 。

***注1：***  使用 FCM 通道需要 Google Play 服务为系统服务且版本不低于 11.0.4。

***注2：***  当设备网络环境为非中国时才会通过 FCM 通道进行推送。


## 进阶功能

请参考：

[API：Android](android_api)

## 技术支持

当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。 [Android FAQ](../Android/android_faq/)
+ 你可以到极光社区搜索类似问题
+ 给我们的 support 发邮件 [support&@jpush.cn](mailto:support@jpush.cn)

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 你需要咨询的产品是 JPush，是否同时使用了极光其他的产品
+ 你所调用的是什么 API，所传参数，完整的报错信息，出现异常的时间点
+ 如果收不到消息，提供应用的 Appkey，消息的 Message ID，设备的 registration ID 信息
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录，日志信息请使用 TXT 文件上传
+ 出现异常的设备是 Android ，列出具体的机型和系统
