# 常见问题


## 分享成功，但控制台没有相应的统计数据
1.检查是否正确的配置了极光官网申请的 appkey。<br>
2.检查网络是否正常，没有网络的情况下，分享成功，但是数据不会上报；等下次分享数据才会上报。<br>
3.检查 QQ, 微信，新浪微博是否在 AnodroidManifest.xml 文件里是否配置分享回调。
```
<activity
    android:name="cn.jiguang.share.android.ui.JiguangShellActivity"
    android:configChanges="keyboardHidden|orientation|screenSize"
    android:exported="true"
    android:launchMode="singleTask"
    android:screenOrientation="portrait"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
	android:windowSoftInputMode="stateHidden|adjustResize">
	<!-- Optional QQ 分享回调-->
	<!-- scheme为“tencent”前缀再加上QQ开发者应用的 appID；例如appID为123456，则scheme＝“tencent123456” -->
	<intent-filter>
		<data android:scheme="tencent1106011004" />
		<action android:name="android.intent.action.VIEW" />
		<category android:name="android.intent.category.BROWSABLE" />
		<category android:name="android.intent.category.DEFAULT" />
	</intent-filter>

	<!-- Optional 新浪微博分享回调 -->
	<intent-filter>
		<action android:name="com.sina.weibo.sdk.action.ACTION_SDK_REQ_ACTIVITY" />
		<category android:name="android.intent.category.DEFAULT" />
	</intent-filter>

	<!-- Optional 新浪微博私信回调-->
	<intent-filter>
		<action android:name="android.intent.action.VIEW" />
		<category android:name="android.intent.category.DEFAULT" />
		<category android:name="android.intent.category.BROWSABLE" />
			<data android:scheme="jsharesdk" android:host="sinaweibo"/>
	</intent-filter>
</activity>
	<!-- Optional 微信分享回调,wxapi 必须在包名路径下，否则回调不成功-->
	<activity
		android:name=".wxapi.WXEntryActivity"
		android:exported="true" />
		
```            
4.控制台的数据每隔一个小时刷新一次。<br>


## 没有安装客户端能否进行分享
如果没有安装 QQ，微信客户端，则不能进行分享； 如果没安装新浪微博客户端，可以通过网页进行分享。