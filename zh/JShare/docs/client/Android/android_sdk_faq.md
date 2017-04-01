#Android SDK FAQ




##第三方平台的appkey和签名，包名是怎样对应？
由于申请新浪微博和微信的appkey和secret时，需要填写应用的签名和包名，如下：<br>
填写新浪微博的签名包名信息：
![](../image/Sina_package.png)<br>
填写微信的签名包名信息
![](../image/WeChat_package.png)<br>
所以，SinaWeibo和WeChat的appkey是跟包名，签名一一对应的，因此在程序的build.gradle文件里配置的签名文件要与JGShareSDK.xml里配置的第三方平台appkey和程序的包名是一一对应的。<br/>




##微信分享后没有回调？
检查AndroidMmanifest.xml文件里配置的package包名和微信回调配置；
<pre>
<!-- Optional 微信分享回调-->
        < activity
            android:name=".wxapi.WXEntryActivity"
            android:exported="true" />
</pre>
微信回调的name字段所指的wxapi必须在包名（package）目录下；如果wxapi所在的路径不在包名（package）目录下，则没有回调。