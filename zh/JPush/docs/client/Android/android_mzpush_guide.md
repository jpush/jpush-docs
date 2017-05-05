# JPush SDK魅族通道集成指南


## 概述

在国内 Android 生态中，推送通道都是由终端与云端之间的长链接来维持，严重依赖于应用进程的存活状态。如今一些手机厂家会在自家 rom 中做系统级别的推送通道，再由系统分发给各个 app，以此提高在自家 rom 上的推送送达率。

JPush SDK 为了尽可能提高开发者在各类 rom 上的推送送达率，对使用 魅族 的设备推送，自动切换到魅族通道。同时，为了保证 SDK 的易用性，原本 JPush 的所有接口调用逻辑都不用修改,JPush 会对自身支持的功能做兼容.只需在manifest中配置上魅族 SDK 必须的配置组件即可。

## 功能描述

+ JPush 初始化的时候可选择是否初始化魅族通道。 

+ 在 魅族 设备上 JPush 通道与 魅族 通道共存.

+ 魅族通道初始化后支持 tag/alias 这些 JPush 原有的功能,其它的 JPush 未支持的功能目前暂时还不可用 .

***注：*** 在flyme5.1.11.1及以上才使用 mzpush,因为之前的版本上 mzpush 的通道并非系统通道。

## 手动集成步骤

### 配置 AndroidManifest.xml
主要步骤为:

* [4.1. 增加魅族推送sdk的aar](#4.1) 

* [4.2. 修改 minSdkVersion 的值](#4.2)

* [4.3. 配置魅族推送sdk所需要的权限](#4.3)

* [4.4. 配置JPush接受魅族sdk的消息接受类](#4.4)

* [4.5. 将MEIZUAPPKEY与MEIZUAPPID替换为在魅族后台注册对应该应用 的AppKey/AppID ](#4.5)

####<h3 id="4.1"> 4.1. 增加魅族推送sdk的aar </h3>
将魅族推送 sdk 的 aar 文件(push-internal-x.x.xxxxxx-xxxx.aar)添加到工程/libs目录下。然后在build.gradle中增加编译该 aar 的代码:

```
	dependencies {
		compile fileTree(include: ['*.jar'], dir: 'libs')
		compile(name: 'push-internal-x.x.xxxxxx-xxxx', ext: 'aar') //compile meizu push SDK aar file
	}

	repositories {
		flatDir{
			dirs 'libs'  //this way we can find the .aar file in libs folder
		}
	}
	
```
#### <h3 id="4.2"> 4.2. 修改 minSdkVersion 的值</h3>

***注:*** 魅族推送 aar 会强制将 minSdkVersion 修改为 11。如果当前 app 使用的 minSdkVersion 的值小于 11,则需要使用 tools 避免被强制覆盖。

```
	<manifest 
		xmlns:android="http://schemas.android.com/apk/res/android"
		xmlns:tools="http://schemas.android.com/tools"
	... >

	<uses-sdk
		android:minSdkVersion="9"
		android:targetSdkVersion="21"
		tools:overrideLibrary="com.meizu.cloud.pushinternal" />
		
```
#### <h3 id="4.3"> 4.3. 配置魅族推送sdk所需要的权限</h3>

```
	<uses-permission android:name="com.meizu.c2dm.permission.RECEIVE" />
	<permission
		android:name="您应用的包名.permission.C2D_MESSAGE"
		android:protectionLevel="signature"></permission>
	<uses-permission android:name="您应用的包名.permission.C2D_MESSAGE" />
	
```
#### <h3 id="4.4"> 4.4. 配置JPush接受魅族sdk的消息接受类</h3>

```
	<receiver android:name="cn.jpush.android.service.PluginMeizuPlatformsReceiver">
		<intent-filter>
			<!-- 接收 push 消息 -->
			<action android:name="com.meizu.flyme.push.intent.MESSAGE" />
			<!-- 接收 register 消息 -->
			<action android:name="com.meizu.flyme.push.intent.REGISTER.FEEDBACK" />
			<!-- 接收 unregister 消息-->
			<action android:name="com.meizu.flyme.push.intent.UNREGISTER.FEEDBACK" />
			<!-- 兼容低版本 Flyme3 推送服务配置 -->
			<action android:name="com.meizu.c2dm.intent.REGISTRATION" />
			<action android:name="com.meizu.c2dm.intent.RECEIVE" />

			<category android:name="您应用的包名"></category>
		</intent-filter>
 	</receiver>
 	
```
#### <h3 id="4.5"> 4.5. 将MEIZUAPPKEY与MEIZUAPPID替换为在魅族后台注册对应该应用 的AppKey/AppID </h3>
将应用对应的魅族的 appkey 和 appid 加上前缀“MZ-”,填加在 meta-data 标签中

```
	<meta-data
		android:name="MEIZU_APPKEY"
		android:value="MZ-您的应用对应的魅族的APPKEY" />
	<meta-data
		android:name="MEIZU_APPID"
		android:value="MZ-您的应用对应的魅族的APPID" />
		
```

## 使用 JCenter 自动化集成步骤
+ 确认android studio的 Project 根目录的主 gradle 中配置了jcenter支持。(新建project默认配置就支持)

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
+ 在应用 module 的 gradle 中 dependencies 节点添加如下代码:

```
	dependencies {
		compile 'cn.jiguang.sdk.plugin:meizu:3.0.6'
	}
	
```
+ 在应用 module 的 gradle 中 defaultConfig 节点添加如下代码:

```
	manifestPlaceholders = [
   		// 设置manifest.xml中的变量
   		MEIZU_APPKEY : "MZ-0956b96085d54c6087b85c7994b02ddf", // 魅族平台注册的appkey
   		MEIZU_APPID : "MZ-110443", // 魅族平台注册的appid
   ]
   
```

## 配置魅族通知栏小图标
通过 MzPush SDK 接收的通知，可设置其通知栏 icon，方法如下：

在应用的工程目录 res/drawable-xxxx/ 几个文件夹中添加对应不同分辨率的通知栏 icon 图标，文件名为 mz\_push\_notification\_small\_icon。如果文件名错误，将无法正确显示该应用的状态栏图标。


魅族手机状态栏 icon 规范请参考 [魅族 PushSDK Demo](https://github.com/MEIZUPUSH/PushDemo/tree/master/PushdemoInternal/src/main/res) 中的图片文件。


**注：**如果没有放入符合规范的 icon 文件，会默认使用应用图标作为通知 icon。而应用图标不符合魅族的通知栏 icon 设计规范的话，则会导致通知栏图标无法正确显示。

##集成错误码

名称|Code|Commen
---|---|--- 
UNKNOWN_ERROR|-1|未知错误
SUCCESS|200|成功
SYSTEM_ERROR|1001|系统错误
SYSTEM_BUSY|1003|服务器忙
PARAMETER_ERROR|1005|参数错误，请参考API文档
INVALID_SIGN|1006|签名认证失败
INVALID_APPLICATION_ID|110000|appId不合法
INVALID_APPLICATION_KEY|110001|appKey不合法
UNSUBSCRIBE_PUSHID|110002|pushId未注册
INVALID_PUSHID|110003|pushId非法
PARAM_BLANK|110004|参数不能为空
APP_IN_BLACK_LIST|110009|应用被加入黑名单
APP_REQUEST_EXCEED_LIMIT|110010|应用请求频率过快
APP_PUSH_TIME_EXCEED_LIMIT|110051|超过该应用的次数限制
APP_REQUEST_PUSH_LIMIT|110019|超过该应用每天推送次数限制
INVALID_APPLICATION_PACKAGENAME|110031|packageName不合法
INVALID_TASK_ID|110032|非法的taskId
INVALID_APPLICATION_SECRET|110033|非法的appSecret

