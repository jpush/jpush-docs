# Android SDK

## Android 常见问题

### 为什么应用程序无法收到 Push 消息（Android）？
+ 确认 appKey（在Portal上生成的）已经正确的写入 Androidmanifest.xml
+ 确认测试手机（或者模拟器）已成功连入网络
+ 确认有客户端 "Login succeed" 日志

详情请参考教程：[Android SDK 调试指南。]()

### Java.lang.UnsatisfiedLinkError

![](../image/error.jpg)

此错误是由于没有正确的加载libjpush.so文件，请检查libjpush.so是否在正确的位置(libs–>armeabi–>libjpush.so)


如果您的项目有libs/armeabi-v7a这个目录，请把libjpush.so也复制一份到这个目录。

如果您的应用需要支持 x86、mips 架构的CPU 需要下载对应的SDK，下载路径：[http://docs.jpush.cn/display/dev/Android](http://docs.jpush.cn/display/dev/Android) 

![](../image/dictionary_path.png)

### The permission should be defined 

![](../image/permission.jpg)

	<permission android:name="您应用的包名.permission.JPUSH_MESSAGE" android:protectionLevel="signature" />
	<uses-permission android:name="您应用的包名.permission.JPUSH_MESSAGE" />
	
### 如何在代码时混淆忽略 jpush-sdk-release.jar？

+ 请下载最新的[proguard.jar](http://sourceforge.net/projects/proguard/files/)， 并替换你Android Sdk "tools\proguard\lib\proguard.jar"

+ 在你的proguard.cfg加上代码：如果是使用新版本的ADT 将project.properties的中“# proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt”的“#”注释去掉，然后在proguard-android.txt中配置

		-dontwarn cn.jpush.**
		-keep class cn.jpush.** { *; }
		
+ 请使用 SDK1.3.X 及以后的版本

### 推送成功了，为什么有部分客户端收不到推送？

请检查收不到通知的手机：

+ 请在logcat查看日志，确定客户端的jpush是否集成成功，网络是否有问题
+ 请看日志或使用接口 isPushStopped来检查是否调用了stoppush
+ 检查手机的JPush高级设置中是否设置了“允许推送时间”
+ 手机的应用中是否勾选了“显示通知”

### MIUI 系统或小米手机收不到推送通知

由于第三方 ROM 的管理软件需要用户手动操作

+ 自启动管理：默认情况下，手机开机后，只有系统默认的服务可以启动起来。除非在自启动管理界面，设置允许第三方程序自启动。
+ 网络助手：可以手动禁止已安装的第三方程序访问2G/3G和WIFI的网络和设置以后新安装程序是否允许访问2G/3G和WIFI的网络。

### Tag、Alias、Registrationid需要每次初始化时都重新设置吗，会变化吗？

+ tag、alias可以参考别名与标签 API进行设置，每次设置是覆盖设置，而不是增量设置。Tag和alias一经设置成功，除非取消或覆盖，是不会变化的。设置好的tag、alias与客户端的对应关系保存在Jpush服务器，目前没有从JPush服务器查询这个对应关系的接口，所以需要客户将对应关系保存在APP应用服务器。

+ Registrationid是客户端SDK第一次成功连接到Jpush服务器时，Jpush服务器给分配的。可以通过获取 RegistrationID API来获取Registrationid进行推送。Registrationid对应一个应用的一个客户端。

### 没有沙箱API怎么测试？

 直接用JPush的api测试就行。

### 其他国家能否使用极光推送（局域网能否使用极光推送）？

 只要能连网到Jpush服务器都可以。判断能否联网到Jpush服务器的方法：ping通 api.jpush.cn 8800


### 用设置的标签或别名推送，出现下面提示：

![](../image/none_target.png)

这可能有两种情况：

+ SDK没有集成成功，客户端有 "Login succeed" 日志才表示SDK集成成功。
+ 设置别名或标签失败，请调用带返回值的函数Method - setAliasAndTags (with Callback)来设置标签或别名，同时参考错误码定义来修改直到设置成功返回0.

### 可以打开 www.jpush.cn，但打不开docs，提示无法找到docs.jpush.cn

+ 提示客户换个浏览器试试
+ 如果还是不行，执行下面的命令反馈结果排查一下问题
	1. ping docs.jpush.cn
	2. nslookup docs.jpush.cn
	3. telnet docs.jpush.cn
	4. 提供一下自己机器访问外网其他网站是否正常

### appkey是怎么对应的？

android的包名和appkey需对应。

### 内网使用极光推送应该怎么设置？

内网使用极光推送需要服务器开放下列端口限制，用于JPush的登录注册及保持推送长链接：   

+ 19000
+ 3000-3020

