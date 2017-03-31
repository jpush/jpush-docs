# JPush SDK 华为通道集成指南


## 概述

在国内 Android 生态中，推送通道都是由终端与云端之间的长链接来维持，严重依赖于应用进程的存活状态。如今一些手机厂家会在自家 rom 中做系统级别的推送通道，再由系统分发给各个 app，以此提高在自家 rom 上的推送送达率。

JPush SDK 为了尽可能提高开发者在各类 rom 上的推送送达率，对使用 EMUI 的设备推送，自动切换到华为通道。同时，为了保证 SDK 的易用性，原本 JPush 的所有接口调用逻辑都不用修改,JPush 会对自身支持的功能做兼容.只需在manifest中配置上华为HMS SDK 必须的配置组件即可.

## 功能描述

+ JPush 初始化的时候可选择是否初始化 HMS Push 通道。

+ 在 EMUI 设备上 JPush 通道与 华为 通道共存.

+ 华为 通道初始化后支持 tag/alias这些 JPush 原有的功能,其它的 JPush 未支持的功能目前暂时还不可用.

+ 增加兼容华为HMS SDK初始化失败处理错误的接口.

***注***：极光根据 EMUI 系统版本间差异，现采取的方案是 EMUI 4.1 及以上版本，使用 HMS 服务，通知走 HMS 通道；对于 EMUI 4.1 以下版本还是走极光通道。

## 集成步骤

### 配置 AndroidManifest.xml
主要步骤为：

* [4.1. 增加华为HMS SDK的aar](#4.1)

* [4.2. 增加support v4包](#4.2)

* [4.3. 修改 minSdkVersion 的值](#4.3)

* [4.4. 配置HMS SDK Push必须的组件](#4.4)

* [4.5. 配置接收 HMS 消息的广播接收器](#4.5)

* [4.6. 替换 HMS 的 appid](#4.6)

* [4.7. 在build.gradle中配置在华为后台添加的指纹证书对应的签名](#4.7)


#### <h3 id="4.1">4.1. 增加华为HMS SDK的aar</h3>

将华为HMS sdk的aar文件(HMS-SDK-x.x.x.xxx.aar)添加到工程/libs目录下。
然后在build.gradle中增加编译该 aar 的代码:

```
    dependencies {
       compile fileTree(include: ['*.jar'], dir: 'libs')
       compile(name: 'HMS-SDK-x.x.x.xxx', ext: 'aar') //compile HMS SDK aar file
    }
    
    repositories {
        flatDir{
            dirs 'libs'  //this way we can find the .aar file in libs folder
        }
    }
```

***注1***：旧版的华为推送也有 jar 包集成的方式，但当前主推是 HMS arr 形式的业务群集成，所以极光目前采用 HMS arr 形式来集成华为通道。

***注2***：极光集成华为通道在 JPush Android SDK 3.0.5 添加，对应测试的华为HMS SDK 版本为：HMS-SDK-2.4.0.300.aar

#### <h3 id="4.2">4.2. 增加support v4包</h3>
将android-support-v4.jar添加到工程/libs目录下,如果app已经添加了support v4包可忽略这一步.

#### <h3 id="4.3">4.3. 修改 minSdkVersion 的值</h3>

***注***： HMS arr 会强制将 minSdkVersion 修改为 14。如果当前 app 使用 minSdkVersion 的值小于 14，则需要使用 tools 避免被强制覆盖。

```
        <manifest xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:tools="http://schemas.android.com/tools"
         ...
            >
		<uses-sdk
            android:minSdkVersion="9"
            android:targetSdkVersion="21"
            tools:overrideLibrary="com.huawei.hms.sdk"
         />

```


#### <h3 id="4.4">4.4. 配置HMS SDK Push必须的组件</h3>

```

 		<provider
            android:name="com.huawei.hms.update.provider.UpdateProvider"
            android:authorities="com.push.cloud.hms.update.provider"
            android:exported="false"
            android:grantUriPermissions="true"></provider>

        <receiver android:name="com.huawei.hms.support.api.push.PushEventReceiver">
            <intent-filter>
                <!-- 接收通道发来的通知栏消息,兼容老版本Push -->
                <action android:name="com.huawei.intent.action.PUSH" />
            </intent-filter>
        </receiver>
        
```

#### <h3 id="4.5">4.5. 配置接收 HMS 消息的广播接收器</h3>


```
       <receiver android:name="cn.jpush.android.service.PluginHuaweiPlatformsReceiver">
            <intent-filter>
                <!-- 必须,用于接收token -->
                <action android:name="com.huawei.android.push.intent.REGISTRATION" /> <!-- 必须,用于接收消息 -->
                <action android:name="com.huawei.android.push.intent.RECEIVE" />
                <!-- 可选,用于点击通知栏或通知栏上的按钮后触发onEvent回调 -->
                <action android:name="com.huawei.android.push.intent.CLICK" />
                <!-- 可选,查看push通道是否连接,不查看则不需要 -->
                <action android:name="com.huawei.intent.action.PUSH_STATE" />
            </intent-filter>
            <meta-data
                android:name="CS_cloud_ablitity"
                android:value="successRateAnalytics" />
        </receiver>
        
```


#### <h3 id="4.6">4.6. 替换 HMS 的 appid </h3>
在华为控制台上获取注册应用的 appid，并填充在 manifest 如下所示的位置。

```
        <meta-data
            android:name="com.huawei.hms.client.appid"
            android:value="您的应用对应华为的appID"></meta-data>


```

#### <h3 id="4.7">4.7. 在build.gradle中配置在华为后台添加的指纹证书对应的签名</h3>
***注***：HMS 服务必须要求 app 签名才能注册成功。指纹证书是在终端采用keytool -list -v -keystore keystorefileName 获取偶对应的指纹证书.

jira - EMUI 版本说明  


```
    signingConfigs {
        release {
            storeFile file("release.keystore")//签名文件的path
            storePassword "123456"
            keyAlias "android.keystore"
            keyPassword "123456"
        }
    }
    
	buildTypes {
        release {
            minifyEnabled true
            proguardFiles 'proguard-rules.pro'
            signingConfig signingConfigs.release
        }
        debug{
        	minifyEnabled false
            signingConfig signingConfigs.release
        }
    }

```


### HMS SDK的编译混淆问题

如果使用了 proguard，需要在配置文件中加入,可以防止一个误报的 warning 导致无法成功编译，

```
	-ignorewarning
	-keepattributes *Annotation*
    -keepattributes Exceptions
    -keepattributes InnerClasses
    -keepattributes Signature
    # hmscore-support: remote transport
    -keep class * extends com.huawei.hms.core.aidl.IMessageEntity { *; }
    # hmscore-support: remote transport
    -keepclasseswithmembers class * implements com.huawei.hms.support.api.transport.DatagramTransport {
      <init>(...);
    }
    # manifest: provider for updates
    -keep public class com.huawei.hms.update.provider.UpdateProvider { public *; protected *; }

```

## 新增兼容华为HMS SDK接口
1. HMS connect失败时，需要根据错误码来判断是否能通过用户行为来解决该错误,所以增加新的接口来适配此种行为.

2. 接口所在类名为:cn.jpush.android.api.JPluginPlatformInterface,以下所有接口需要在Activity中调用,并且Activity如果调用相关接口就必须全部调用.漏掉一个接口则会导致内存泄漏或功能异常.

3. 如果在Activity中没有调用相关接口,在HMS SDK初始化失败并且可以通过用户行为解决的错误则会没有入口解决(比如华为手机上的华为移动服务框架版本太低导致的初始化失败,此时HMS SDK则会弹出对话框引导用户升级用户华为移动服务框架等).

***注***：以上内容中 “用户行为” 指 app 使用者的操作行为，一般情况下就是点击 HMS 插件升级提示。

### 1. public void onStart(Activity activity)
   在Activity中的onStart方法中调用.该接口会引用当前Activity,并且如果HMS SDK没有初始化则会初始化HMS SDK.


### 2. public void onStop(Activity activity)
   在Activity中的onStop方法中调用.该接口会清空对当前Activity的引用.
   


### 3. public void onActivityResult(Activity activity,int requestCode, int resultCode, Intent data)
该接口是经过用户操作解决完错误之后,返回让HMS重新初始化.

### 代码示例：

```
    public class MainActivity extends Activity{
        
        private JPluginPlatformInterface pHuaweiPushInterface;

        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.main);
            initView();
            registerMessageReceiver();  // used for receive msg
            pHuaweiPushInterface = new JPluginPlatformInterface(this.getApplicationContext());
        }
        
        @Override
        public void onStart() {
            super.onStart();
            pHuaweiPushInterface.onStart(this);
        }
        
        @Override
        public void onStop() {
            super.onStop();
            pHuaweiPushInterface.onStop(this);
        }
        
        @Override
        protected void onActivityResult(int requestCode, int resultCode, Intent data) {
            super.onActivityResult(requestCode, resultCode, data);
            //JPush中调用HMS SDK解决错误的接口传入的requestCode为10001,开发者调用是请注意不要同样使用10001
            if(requestCode == JPluginPlatformInterface.JPLUGIN_REQUEST_CODE) {
                pHuaweiPushInterface.onActivityResult(this, requestCode, resultCode, data);
            }
        }
    }
        
```


