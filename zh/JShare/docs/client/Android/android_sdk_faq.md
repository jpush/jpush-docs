#Android SDK FAQ




##第三方平台的appkey和签名，包名是怎样对应？
由于申请新浪微博和微信的appkey和secret时，需要填写应用的签名和包名，如下：<br>
填写新浪微博的签名包名信息：
![](../image/Sina_package.png)<br>
填写微信的签名包名信息
![](../image/WeChat_package.png)<br>
所以，SinaWeibo和WeChat的appkey是跟包名，签名一一对应的，因此在程序的build.gradle文件里配置的签名文件要与JGShareSDK.xml里配置的第三方平台appkey和程序的包名是一一对应的。<br/>




##微信分享后没有回调？
例如：官方的demo的package是cn.jiguang.share.demo，在manifest.xml文件里配置的package如果为：aaa.bbb.ccc；如果微信回调的name字段
<pre>
<!-- Optional 微信分享回调-->
        < activity
            android:name=".wxapi.WXEntryActivity"
            android:exported="true" />
</pre>
所在的路径不在manifest里面配置的包名（package）目录下，则没有回调。