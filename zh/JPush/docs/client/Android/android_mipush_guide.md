# JPush SDK 小米通道集成指南


## 概述

在国内 Android 生态中，推送通道都是由终端与云端之间的长链接来维持，严重依赖于应用进程的存活状态。如今一些手机厂家会在自家 rom 中做系统级别的推送通道，再由系统分发给各个 app，以此提高在自家 rom 上的推送送达率。

JPush SDK 为了尽可能提高开发者在各类 rom 上的推送送达率，对使用 MIUI 的设备推送，自动切换到小米通道。同时，为了保证 SDK 的易用性，原本 JPush 的所有接口调用逻辑都不用修改,JPush 会对自身支持的功能做兼容.只需在manifest中配置上小米 SDK 必须的配置组件即可.

## 功能描述

+ JPush 初始化的时候可选择是否初始化 MiPush 通道。

+ 在 MIUI 设备上 JPush 通道与 MiPush 通道共存.

+ MiPush 通道初始化后支持 stopPush/resumePush 与 tag/alias这些 JPush 原有的功能,其它的 JPush 未支持的功能目前暂时还不可用.

## 集成步骤

### 配置 AndroidManifest.xml
主要步骤为：

* [4.1. 配置小米推送sdk所需要的权限](#4.1)

* [4.2. 配置小米必须的组件](#4.2)

* [4.3. 配置JPush接受的小米sdk的消息接受类](#4.3)

* [4.4. 将XIAOMI_APPKEY与XIAOMI_APPID替换为在小米后台注册对应该应用的AppKey/AppID](#4.4)

* [4.5. 增加小米推送sdk的jar](#4.5)



#### <h3 id="4.1">4.1. 配置小米推送sdk所需要的权限</h3>

```
         <permission
            android:name="您应用的包名.permission.MIPUSH_RECEIVE"
            android:protectionLevel="signature" />

         <uses-permission android:name="您应用的包名.permission.MIPUSH_RECEIVE" />

         <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
         <uses-permission android:name="android.permission.INTERNET" />
         <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
         <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
         <uses-permission android:name="android.permission.READ_PHONE_STATE" />
         <uses-permission android:name="android.permission.GET_TASKS" />
         <uses-permission android:name="android.permission.VIBRATE" />

```


#### <h3 id="4.2">4.2. 配置小米必须的组件</h3>

```

 		<service
            android:name="com.xiaomi.push.service.XMJobService"
            android:enabled="true"
            android:exported="false"
            android:permission="android.permission.BIND_JOB_SERVICE"
            android:process=":pushservice" />

        <service
            android:name="com.xiaomi.push.service.XMPushService"
            android:enabled="true"
            android:process=":pushservice" />

        <service
            android:name="com.xiaomi.mipush.sdk.PushMessageHandler"
            android:enabled="true"
            android:exported="true" />
        <service
            android:name="com.xiaomi.mipush.sdk.MessageHandleService"
            android:enabled="true" />

        <receiver
            android:name="com.xiaomi.push.service.receivers.NetworkStatusReceiver"
            android:exported="true">
            <intent-filter>
                <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />

                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </receiver>
        <receiver
            android:name="com.xiaomi.push.service.receivers.PingReceiver"
            android:exported="false"
            android:process=":pushservice">
            <intent-filter>
                <action android:name="com.xiaomi.push.PING_TIMER" />
            </intent-filter>
        </receiver>
        
```

#### <h3 id="4.3">4.3. 配置JPush接受的小米sdk的消息接受类</h3>


```
        <receiver
            android:name="cn.jpush.android.service.PluginXiaomiPlatformsReceiver"
            android:exported="true">
            <intent-filter>
                <action android:name="com.xiaomi.mipush.RECEIVE_MESSAGE" />
            </intent-filter>
            <intent-filter>
                <action android:name="com.xiaomi.mipush.MESSAGE_ARRIVED" />
            </intent-filter>
            <intent-filter>
                <action android:name="com.xiaomi.mipush.ERROR" />
            </intent-filter>
        </receiver>
        
```


#### <h3 id="4.4">4.4. 将小米应用的 appkey 和 appid 加上前缀“MI-”，填入meta-data 标签中</h3>


```

        <meta-data
            android:name="XIAOMI_APPKEY"
            android:value="MI-您的应用对应的小米的appkey" />
            
       <meta-data
            android:name="XIAOMI_APPID"
            android:value="MI-您的应用对应小米的appID" />


```

#### <h3 id="4.5">4.5. 增加小米推送sdk的jar</h3>

从小米官网将小米sdk的jar文件(MiPush_SDK_Client_x_x_x.jar)导入到工程 libs/ 目录下。


**注：极光集成小米通道在 JPush Android SDK 3.0.3 添加，对应测试的小米 SDK 版本为：3.2.2**

### MiPush SDK的编译混淆问题

如果使用了 proguard，需要在配置文件中加入,可以防止一个误报的 warning 导致无法成功编译，

+ -dontwarn com.xiaomi.push.**

