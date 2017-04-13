# 常见问题


## 分享成功了，但是webportal上看不到对应的统计数据
1.检查是否正确的配置了极光官网申请的appkey。<br>
2.检查网络是否正常，没有网络的情况下，分享成功，但是数据不会上报；等下次分享数据才会上报。<br>
3.检查QQ,微信，新浪微博是否在AnodroidManifest.xml文件里是否配置分享回调。

            <!-- Optional QQ分享回调-->
            <!-- scheme为“tencent”前缀再加上QQ开发者应用的appID；例如appID为123456，则scheme＝“tencent123456” -->
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
        </activity>
        <!-- Optional 微信分享回调,wxapi必须在包名路径下，否则回调不成功-->
        <activity
            android:name=".wxapi.WXEntryActivity"
            android:exported="true" />
            
4.Webportal上数据每隔一个小时刷新一次<br>


## 没有安装客户端能否进行分享
如果没有安装QQ，微信，新浪微博客户端，则不能进行分享。