# FAQ


## The console does not have statistics after sharing successfully?

1.Check whether the appkey of Jiguang official website is correctly configured.

2.Check if the network is normal. If there is no network, the sharing will be successful, but the data will not be reported; it will be reported the next time the data is shared.

3.Check whether QQ, WeChat and Sina Weibo are configured to share callbacks in the AnodroidManifest.xml file.


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

4.The data on the console is refreshed every hour.

## Can share without client?

If you do not have QQ and WeChat client, you cannot share; If you do not install Sina Weibo client, you can share through the web page.

## Report an error when WeChat logins and authorizes: Scope parameter is incorrect or does not have Scope permission

The account has not applied for developer qualification certification and has no relevant authority. Login to the [WeChat developer platform](https://open.weixin.qq.com/) and enter the account center to apply for developer qualification certification.

## Report an error when Sina Weibo logins and authorizes：sso package or sign error

1.Check whether the application passed the audit on the Sina Weibo open platform. If not pass the audit, it cannot use sso to login; 

2.After the application passed the audit, ensure that the package name and signature filled in the [Weibo open platform](http://open.weibo.com/) are consistent with the package name and signature of the project.
