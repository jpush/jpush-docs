# Android JShare集成指南
## 产品功能说明
JShare SDK 可以让用户不用额外集成第三方平台的 SDK 实现平台间的分享功能，可以有效的降低包体积。
### 主要功能
* 快速集成多个平台分享。

### 主要特点
* 支持多个平台，目前支持微信、微信朋友圈、QQ、QQ空间、新浪微博。
* 一套接口接入多个平台，无需单独熟悉每个平台接入方法，接入成本低。

### jshare-android-release-1.x.y.zip 集成压缩包内容
* JGShareSDK.xml
	* 客户端嵌入SDK，各个平台配置的参考文件
* AndroidManifest.xml
	* 客户端嵌入SDK参考的配置文件
* libs/jcore-android.v1.x.y.jar
	* 极光开发者服务的核.心包。
* jshare-core.jar
	* JShare SDK核心包
* jshre-wechat.jar
	* JShare微信平台包
* jshare-qq.jar
	* JShareQQ平台包
* jshare-sina.jar
	* JShare新浪微博包
* libs/(cpu-type)/libjcore1xy.so
	* 各种CPU类型的native开发包。
* example
	* 是一个完整的Android项目，通过这个演示了JShare SDK的基本用法，可以用来做参考。
### Android SDK 版本
目前SDK只支持Android 2.3或以上版本的手机系统。

## 集成步骤
* 解压缩 jshare-android-release-1.x.y.zip 集成压缩包。
* 复制libs/jcore-android_v1.x.y.jar到工程libs目录下。
* 复制libs/jshare-android_v1.x.y.jar到工程libs目录下。
* 复制libs/(cpu-type)/libjcore1xy.so到你工程中存放对应cpu类型的目录下。
* 根据需要复制libs/jshare-xx.jar平台jar包到工程libs目录下。
* 按下面说明配置AndroidManifest.xml。
* 按以下说明配置JGShareSDK.xml文件。
* 参考example工程或者接口文档使用JShare SDK。

### 配置 AndroidManifest.xml
根据 SDK 压缩包里的 AndroidManifest.xml 样例文件，来配置应用程序项目的 AndroidManifest.xml 。

* 复制备注为 "Required" 的部分
* 将标注为“您应用的包名”的部分，替换为当前应用程序的包
* 将标注为“您应用的Appkey”的部分，替换为在Portal上注册该应用的的Key,例如：  
9fed5bcb7b9b87413678c407
#### AndroidManifest 示例
	<?xml version="1.0" encoding="utf-8"?>
	<manifest xmlns:android="http://schemas.android.com/apk/res/android"
	    package="cn.jiguang.share.demo">
	 
	    <permission
	        android:name="${applicationId}.permission.JPUSH_MESSAGE"
	        android:protectionLevel="signature"/>
	 
	 
	    <uses-permission android:name="${applicationId}.permission.JPUSH_MESSAGE"/>
	    <uses-permission android:name="android.permission.RECEIVE_USER_PRESENT"/>
	    <uses-permission android:name="android.permission.INTERNET"/>
	    <uses-permission android:name="android.permission.WAKE_LOCK"/>
	    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
	    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
	    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
	    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>
	    <uses-permission android:name="android.permission.VIBRATE"/>
	    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
	    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
	    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
	 
	    <!-- Optional for location -->
	    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
	    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
	    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
	    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS"/>
	    <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE"/>
	    <uses-permission android:name="android.permission.KILL_BACKGROUND_PROCESSES"/>
	 
	    <uses-permission android:name="android.permission.GET_TASKS" />
	    <uses-permission android:name="android.permission.INTERNET" />
	    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
	    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
	    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
	    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
	    <uses-permission android:name="android.permission.MANAGE_ACCOUNTS"/>
	    <uses-permission android:name="android.permission.GET_ACCOUNTS"/>
	    <application
	        android:allowBackup="true"
	        android:icon="@mipmap/ic_launcher"
	        android:label="@string/app_name"
	        android:supportsRtl="true"
	        android:name=".MyApplication"
	        android:theme="@style/AppTheme">
	        <activity android:name=".MainActivity">
	            <intent-filter>
	                <action android:name="android.intent.action.MAIN" />
	 
	                <category android:name="android.intent.category.LAUNCHER" />
	            </intent-filter>
	        </activity>
	        <activity android:name=".SelectPlatActivity"></activity>
	        <activity android:name=".ShareTypeActivity"></activity>
	 
	        <activity
	            android:name="cn.jiguang.share.core.ui.JiguangShellActivity"
	            android:theme="@android:style/Theme.Translucent.NoTitleBar"
	            android:configChanges="keyboardHidden|orientation|screenSize"
	            android:screenOrientation="portrait"
	            android:exported="true"
	            android:windowSoftInputMode="stateHidden|adjustResize" >
	 
	            <intent-filter>
	                <data android:scheme="tencent1105301453" />
	                <action android:name="android.intent.action.VIEW" />
	                <category android:name="android.intent.category.BROWSABLE" />
	                <category android:name="android.intent.category.DEFAULT" />
	            </intent-filter>
	 
	            <!-- 调用新浪原生SDK，需要注册的回调activity -->
	            <intent-filter>
	                <action android:name="com.sina.weibo.sdk.action.ACTION_SDK_REQ_ACTIVITY" />
	                <category android:name="android.intent.category.DEFAULT" />
	            </intent-filter>
	        </activity>
	        <!--<activity android:name="com.jshare.shareexample.wxapi.WXEntryActivity"-->
	            <!--android:exported="true"-->
	            <!--&gt;</activity>-->
	        <activity android:name=".wxapi.WXEntryActivity"
	            android:exported="true"
	            ></activity>
	        <meta-data
	            android:name="JPUSH_CHANNEL"
	            android:value="developer-default"/>
	        <meta-data
	            android:name="JPUSH_APPKEY"
	            android:value="426251cac0146ce0a08ca38f" />
	    </application>
	 
	</manifest>

### 配置 JGShareSDK.xml
主要步骤为：  

* 复制或者新建JGShareSDK.xml到工程目录的asset目录下。
* 把JGShareSDK.xml中相关的AppKey、AppSecret替换成自己的注册的。
* 根据需要配置各个平台，不需要的平台可以删除或者Enable设置为false。

#### JGShareSDK.xml示例
	<?xml version="1.0" encoding="utf-8"?>
	<DevInfor>
		<!--
		   说明：
			
		   1、表格中的第一项
			  <ShareSDK
				  AppKey="api20" />
		   是必须的，其中的AppKey是您在ShareSDK上注册的开发者帐号的AppKey
			
		   2、所有集成到您项目的平台都应该为其在表格中填写相对应的开发者信息，以新浪微博为例：
			   <SinaWeibo
					Id="1"
					SortId="1"
					AppKey="568898243"
					AppSecret="38a4f8204cc784f81f9f0daaf31e02e3"
					RedirectUrl="http://www.mob.com"
					Enable="true" />
		   其中的SortId是此平台在分享列表中的位置，由开发者自行定义，可以是任何整型数字，数值越大
		   越靠后AppKey、AppSecret和RedirectUrl是您在新浪微博上注册开发者信息和应用后得到的信息
		   Id是一个保留的识别符，整型，ShareSDK不使用此字段，供您在自己的项目中当作平台的识别符。
		   Enable字段表示此平台是否有效，布尔值，默认为true，如果Enable为false，即便平台的jar包
		   已经添加到应用中，平台实例依然不可获取。
			
		   各个平台注册应用信息的地址如下：
			 新浪微博        http://open.weibo.com
			 微信好友        http://open.weixin.qq.com
		-->
		 
		<ShareSDK
			AppKey = "1969173bdaabb"/> <!-- 修改成你在sharesdk后台注册的应用的appkey"-->
		 
		<!-- ShareByAppClient标识是否使用微博客户端分享，默认是false -->
		<!--<SinaWeibo-->
			<!--Id="1"-->
			<!--Seq="1"-->
			<!--AppKey="3746081663"-->
			<!--AppSecret="10c67a2a1ae07e6e7ad562012e94d9c3"-->
			<!--RedirectUrl="https://www.jiguang.cn"-->
			<!--ShareByAppClient="true"-->
			<!--Enable="true" />-->
		<SinaWeibo
			Id="1"
			Seq="1"
			AppKey="727232518"
			AppSecret="9b63b2c95a200e4fc671ca97a6b01ba9"
			RedirectUrl="https://www.jiguang.cn/"
			ShareByAppClient="true"
			Enable="true" />
	 
		<!-- ShareByAppClient标识是否使用微博客户端分享，默认是false -->
		<QQ
		Id="6"
		Seq="6"
		AppId="1105301453"
		AppKey="YIbPvONmBQBZUGaN"
		ShareByAppClient="true"
		Enable="true" />
	 
		<QZone
			Id="2"
			Seq="2"
			AppId="1105301453"
			AppKey="YIbPvONmBQBZUGaN"
			Enable="true" />
		 
		<!--
		   Wechat微信和WechatMoments微信朋友圈的appid是一样的；
		 
						   注意：开发者不能用我们这两个平台的appid,否则分享不了
		 
				 微信测试的时候，微信测试需要先签名打包出apk,
		  sample测试微信，要先签名打包，keystore在sample项目中，密码123456
		   
		  BypassApproval是绕过审核的标记，设置为true后AppId将被忽略，故不经过
		  审核的应用也可以执行分享，但是仅限于分享文字和图片，不能分享其他类型，
		  默认值为false。此外，微信收藏不支持此字段。
	   -->
		<!--<Wechat-->
			<!--Id="3"-->
			<!--Seq="3"-->
			<!--AppId="wx71ae0d5e5cc12994"-->
			<!--AppSecret="84a3027bb993a83ad5f16c384846b7ee"-->
			<!--BypassApproval="false"-->
			<!--Enable="true" />-->
	 
		<!--<WechatMoments-->
			<!--Id="4"-->
			<!--Seq="4"-->
			<!--AppId="wx71ae0d5e5cc12994"-->
			<!--AppSecret="84a3027bb993a83ad5f16c384846b7ee"-->
			<!--BypassApproval="false"-->
			<!--Enable="true" />-->
	 
		<Wechat
			AppId="wxa2ea563906227379"
			BypassApproval="false"
			AppSecret="338a22af3fb9440f66bff94dfcfff1de"
			Enable="true"
			Id="4"
			SortId="4" />
	 
		<WechatMoments
			AppId="wxa2ea563906227379"
			AppSecret="338a22af3fb9440f66bff94dfcfff1de"
			BypassApproval="false"
			Enable="true"
			Id="5"
			SortId="5" />
	   <WechatFavorite
			Id="5"
			Seq="5"
			AppId="wxa2ea563906227379"
			AppSecret="338a22af3fb9440f66bff94dfcfff1de"
			Enable="true" />
	 
	</DevInfor>


