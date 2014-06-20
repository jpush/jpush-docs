# Android SDK
## 教程: Android

### Android SDK 网络问题解析

Android 客户端网络不稳定，会导致App 有时候无法及时收到 Push 消息。

很多开发者认为这是因为 JPush 推送不稳定、延迟，甚至有时候认为 JPush 后台推送系统出问题了。

本文目的是从各个方面来分析 Android 网络导致的 JPush 不能正常工作的问题。

#### JPush 正常工作的必要条件

首先，我们需要知道，JPush SDK  并不是集成到App 后就必然一直工作的。

其正常工作的必要条件是：JPush SDK 与 JPush Server 的网络保持着连接。请参考这篇文章来做进一步的理解：[极光推送技术原理：移动无线网络长连接。](http://blog.jpush.cn/jpush_wireless_push_principle/)

而 Android 设备的网络的复杂性、不稳定性，是 Android 设备开发最复杂的地方之一。

另外，每款手机的网络能力也是千差万别的。国内很多杂牌手机在网络方面甚至会有严重的问题。大品牌厂商的手机则要好很多。

只要 JPush 的网络连接是正常的，则：

+ JPush 收到消息一定是及时的。其延迟是秒级的，一般在 1 秒之内。如果超过 10 秒，则一定是客户端网络出了问题。
+ 手机休眠时，也能够及时地收到推送消息。

#### 部分系统的特殊处理导致问题

##### MIUI V5 系统

+ 自启动管理：默认情况下，手机开机后，只有系统默认的服务可以启动起来。除非在自启动管理界面，设置允许第三方程序自启动。

+ 网络助手：可以手动禁止已安装的第三方程序访问2G/3G和WIFI的网络和设置以后新安装程序是否允许访问2G/3G和WIFI的网络。


##### 4.0以上的android系统

+ 在设置－>应用，强行停止 应用程序后该程序无法再自启动，就算重新开机也一样，一定要手动开启才能运行起来。

#### 让我们从目前得到的反馈来整理调试的思路

##### 手机休眠时收不到 JPush 消息，解锁或屏幕灯亮则可以成功接收

这个现象表明，手机休眠时，JPush SDK “被迫”与服务器端的网络失去了连接。

JPush SDK 的工作原理是要确保在手机休眠时也能正常的工作，即休眠时也可以及时地收到Push消息。实际上JPush在大部分上手机上都能达到此效果。

这个“被迫”，是由 Android 设备的环境所导致的。涉及的原因有如下几个方面：

+ 手机本身的网络设置。标准版本的 Android ROM 是没有这个设置的，但某些特殊的 ROM 可能会有这方面的设置。
+ 手机上的安全、省电工具软件额外做的事情

上述的特殊机制会关闭网络。网络一旦连接上，JPush也会连接上服务器，从而Push消息就会收到。

##### 有时候收到 JPush 消息很及时，有时候则要等几分钟

JPush 会监听网络切换广播。当网络关闭时，把原来JPush连接关闭。当有新的网络时，创建JPush连接。

另外，RTC会定时发送心跳。如果之前的网络已经断了，则会重新连接。

应该说，当前的网络连接策略还是相对简单的，这样做的目的是：省电、省流量。

不 好之处就是：网络没有切换时，因为当时网络过差，JPush连接会被中断。这种情况下，就只能等 RTC 心跳去触发连接。这也是有时候JPush 无法及时接收Push消息的原因。根据网络条件的不同，出现这个情况的概率也会不同。但据我们自己的测试，90% 的时候是可以及时地收到Push消息的。

JPush 目前在网络策略方面没有像微信这种聊天工具做得积极。如果这样做到，电量和流量的消耗必然会成倍地增加。

##### 完全收不到 JPush 消息

如果集成之后就完全收不到Push消息，则很有可能是某个地方配置错误。请根据文档仔细检查：Android SDK 集成指南，iOS SDK 集成指南，或者根据参考教程：Android SDK 调试指南，iOS SDK 调试指南。


### Android SDK 调试指南

#### SDK启动过程

1. 检查AndroidManifest.xml中是否有配置AppKey，如果没有，则启动失败
2. 检查 Androidmanifest.xml文件配置的正确性，必须要保证“Android SDK 集成指南”中所有标注“ 
3. Required”的部分都正确配置，否则启动失败
4. 检查 JPush SDK库文件的有效性，如果库文件无效，则启动失败
5. 检查网络是否可用，如果网络可用则连接服务器登录，否则启动失败
6. 登陆成功后可以从log中看到如下log

![](image/jpush.jpg)

#### 测试确认

+ 确认 Androidmanifest.xml 中所需的所有 “Required” 项都已经添加。如果有 "Required" 项未添加，日志会提示错误。
+ 确认 AppKey (在Portal上生成的) 已经正确的写入 Androidmanifest.xml 中,没写会有日志提示错误。
+ 确认在程序启动时候调用了init(context) 接口
+ 确认测试手机（或者模拟器）的网络可用，如果网络正常可用，客户端调用 init 后不久，应有登录成功（Login succeed）的日志信息，如 SDK 启动过程所示
+ 启动应用程序，登陆 Portal 系统，并向应用程序发送自定义消息或者通知栏提示。在几秒内，客户端应可收到下发的通知或者正定义消息.


### 别名与标签使用教程

#### 为什么需要别名与标签

推送消息时，要指定推送的对象：全部，某一个人，或者某一群人。

	JPush 目前还提供根据 IMEI 推送。但这个建议仅用于测试目的。原因很简单：很多 Android 设备是取不到 IMEI 的。
	
全部很好办，针对某应用“群发”就好了。Portal与API都支持向指定的 appKey 群发消息。

要指定向某一个特定的人，或者某一群特定的人，则相对复杂。因为对于 JPush 来说，某一个人就是一个注册ID，这个注册ID与开发者App没有任何关系，或者说对开发者App是没有意义的。

如果要对开发者App有意义的某个特定的用户推送消息，则需要：把 JPush 注册用户与开发者App 用户绑定起来。

这个绑定有两个基本思路：

+ 把绑定关系保存到 JPush 服务器端
+ 把绑定关系保存到开发者应用服务器中

前者，就是这里要说到的：别名与标签的功能。这个机制简单易用，适用于大多数开发者。

后者，则是 JPush 提供的另外一套 RegistrationID 机制。这套机制开发者需要有应用服务器来维护绑定关系，不适用于普通开发者。Android SDK r1.6.0 版本开始支持。

#### 使用方式

别名与标签的机制，其工作方式是：

1. 客户端开发者App调用 setAliasAndTags API 来设置关系
2. JPush SDK 把该关系设置保存到 JPush Server 上
3. 在服务器端推送消息时，指定向之前设置过的别名或者标签推送

SDK 支持的 setAliasAndTags 请参考相应的文档：别名与标签 API

使用过程中有几个点做特别说明：

1. App 调用 SDK setAliasAndTags API 时，r1.5.0 版本提供了 Callback 来返回设置状态。如果返回 6002 （超时）则建议重试

	+ 老版本没有提供 Callback 无设置状态返回，从而没有机制确定一定成功。建议升级到新版本
	
2. Portal 上推送或者 API 调用向别名或者标签推送时，可能会报错：不存在推送目标用户。该报错表明，JPush Server 上还没有针对你所推送的别名或者标签的用户绑定关系，所以没有推送目标。这时请开发者检查确认，开发者App是否正确地调用了 setAliasAndTags API，以及调用时是否网络不好，JPush SDK 暂时未能保存成功。

#### 使用别名

用于给某特定用户推送消息。

所谓别名，可以近似地被认为，是用户帐号里的昵称。


#### 使用标签

用于给某一群人推送消息。

标签类似于博客里为文章打上 tag ，即为某资源分类。

##### 动态标签

JPush 提供的设置标签的 API 是在客户端的。开发者如何做到在自己的服务器端动态去设置分组呢？ 比如一个企业OA系统，经常需要去变更部门人员分组。以下是大概的思路：

+ 设计一种自定义消息格式（业务协议），App解析后可以调用 JPush SDK setAliasAndTags API 来重新设置标签（分组）
	+ 例：{"action":"resetTags", "newTags":["dep_level_1":"A公司", "dep_level_2":"技术部", "dep_level_3":"Android开发组", "address":"深圳", "lang":"zh"]}
+ 要动态设置分组时，推送这条自定义消息给指定的用户
	+ 使用别名的机制，推送到指定的用户。
+ 客户端App 调用 JPush SDK API 来设置新的标签



#### 参考

[别名与标签 API]()

###别名与标签设置异常处理

由于网络连接不稳定的原因，有一定的概率 JPush SDK 设置别名与标签会失败。
		
App 开发者合理地处理设置失败，则偶尔失败对应用的正常使用 JPush 影响是有限的。

以下以 Android SDK 作为示例。

基本思路：

+ 设置成功时，往 SharePreference 里写状态，以后不必再设置
+ 遇到 6002 超时，则稍延迟重试。

### 自定义通知栏样式教程

#### 关于自定义通知栏样式

JPush 通知推送到客户端时，默认使用手机的默认设置来显示通知栏，包括铃声、震动等效果。

如果开发者想要达到如下的效果，则需要使用“自定义通知栏样式”功能：

+ 通知栏样式使用与默认不一样的设置，比如想要控制：
	+ 铃声、震动
	+ 显示图标
	+ 替换默认的通知栏样式。
 
#### 推送消息指定通知栏样式编号

通知栏样式在服务器端向下推送时，只体现为一个编号（数字）。

	推送通知的样式编号，应该是在客户端做了自定义通知栏样式设置的。

	如果通知上的样式编号，在客户端检查不存在，则使用默认的通知栏样式。
	
开发者不自定义通知栏样式时，则此编号默认为 0。

开发者自定义的通知栏样式编号应大于 0，小于 1000。

在 Portal 上发送通知时，最下边的“可选”部分展开，开发者可指定当前要推送的通知的样式编号。如下图所示：

![](image/image2012-11-6 9_16_45.png)

#### 客户端定义通知栏样式

自定义的通知栏样式，是在客户端进行的。请参考 [通知栏样式定制API]() 来看所支持的功能。

#####自定义通知栏样式设计

+ 有个 PushNotificationBuilder 概念，开发者使用 setPushNotificationBuilder 方法为某种类型的 PushNotificationBuilder 指定编号。
+ setPushNotificationBuilder 可以在 JPushInterface.init() 之后任何地方调用，可以是开发者应用的逻辑来触发调用，或者初始化时调用。
+ 只需要设置一次，JPush SDK 会记住这个设置。在下次收到推送通知时，就根据通知里指定的编号来找到 PushNotificationBuilder 来展现、执行。

##### API - setDefaultPushNotificationBuilder 设置默认

此 API 改变默认的编号为 0 的通知栏样式。


##### API - setPushNotificationBuilder 指定编号

此 API 为开发者指定的编号，设置一个自定义的 PushNotificationBuilder（通知样式构建器）。

#####Example - 基础的 PushNotificationBuilder

定制声音、震动、闪灯等 Notification 样式。

	BasicPushNotificationBuilder builder = new BasicPushNotificationBuilder(MainActivity.this);
	builder.statusBarDrawable = R.drawable.jpush_notification_icon;
	builder.notificationFlags = Notification.FLAG_AUTO_CANCEL;  //设置为自动消失
	builder.notificationDefaults = Notification.DEFAULT_SOUND ｜ Notification.DEFAULT_VIBRATE | Notification.DEFAULT_LIGHTS;  // 设置为铃声与震动都要
	JPushInterface.setPushNotificationBuilder(1, builder);
	
#####Example - 高级自定义的 PushNotificationBuilder

基于基础的 PushNotificationBuilder，可进一步地定制 Notification 的 Layout。

`这里作为 example 的 customer_notitfication_layout 在我们的 example 项目的 /res/layout/ 下可以找到。你完全可以用自己的 layout。`

	CustomPushNotificationBuilder builder = new 
	CustomPushNotificationBuilder(MainActivity.this,
	                          R.layout.customer_notitfication_layout, 
	                          R.id.icon, 
	                          R.id.title, 
	                          R.id.text); 
	                         // 指定定制的 Notification Layout
	builder.statusBarDrawable = R.drawable.your_notification_icon;      
	// 指定最顶层状态栏小图标
	builder.layoutIconDrawable = R.drawable.your_2_notification_icon;   
	// 指定下拉状态栏时显示的通知图标
	JPushInterface.setPushNotificationBuilder(2, builder);                

####通知栏样式定义不符合要求？

以上提供的自定义通知栏样式的功能是有限的。比如：Android SDK 4.0 以后的 [Notification](http://developer.android.com/reference/android/app/Notification.html) 支持指定 Style ，而这种复杂的通知样式定义 JPush SDK 还未有支持。

或者你想要自定义的复杂的通知样式，但不愿意使用上述高级的自定义通知栏定制功能。

建议不要使用 JPush 提供的通知功能，而使用自定义消息功能。

即：推送自定义消息到客户端后，App取到自定义消息全部内容，然后App自己来写代码做通知的展示。请参考文档：通知 vs. 自定义消息。



####参考

+ [通知栏样式定制 API]()
##通知 vs. 自定义消息

极光推送包含有通知与自定义消息两种类型的推送。本文描述他们的区别，以及建议的应用场景。

只有 Android 支持自定义消息。

### 两者的区别

#### 功能角度

##### 通知

或者说 Push Notification，即指在手机的通知栏（状态栏）上会显示的一条通知信息。这是 Android / iOS 的基本功能。

一条通知，简单的填写纯文本的通知内容即可。

通知主要用于提示用户的目的。应用加上通知功能，有利于提高应用的活跃度。

##### 自定义消息

是极光推送自己的概念。

自定义消息不是通知，所以不会被SDK展示到通知栏上。其内容完全由开发者自己定义。

自定义消息主要用于应用的内部业务逻辑。一条自定义消息推送过来，有可能没有任何界面显示。

	本质上：自定义消息是原始的消息，JPush SDK 不做处理。而通知，则 JPush SDK 会做通知展示处理，其目的是为了减轻开发人员的工作量。

	所以，如果通知功能不太符合您的需求，你都可以使用自定义消息来实现（客户端展现App自己来做）。



#### 开发者使用角度

##### 通知

简单场景下的通知，用户可以不写一行代码，而完全由 SDK 来负责默认的效果展示，以及默认用户点击时打开应用的主界面。

JPush Android SDK 提供了 API 让开发者来定制通知栏的效果，请参考：自定义通知栏样式教程；也提供了 接收推送消息Receiver 让你来定制在收到通知时与用户点击通知时的不同行为。


##### 自定义消息

SDK 不会把自定义消息展示到通知栏。

所以调试时，需要到日志里才可以看到服务器端推送的自定义消息。

自定义消息一定要由开发者写[ 接收推送消息Receiver]() 来处理收到的消息。



### 使用通知  

请参考以下示例代码。


## API: Android

### 停止与恢复推送服务 API
#### 支持的版本

开始的版本：v1.3.3

#### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者App可以通过调用停止推送服务API来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。如果停止推送服务后，开发者App被重新安装，或者被清除数据，JPush SDK 会恢复正常的默认行为。（因为保存在本地的状态数据被清除掉了）。
> 
> 本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息，恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。

#### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

+ JPush Service 不在后台运行
+ 收不到推送消息
+ 不能通过 JPushInterface.init 恢复，需要调用resumePush恢复。
+ 极光推送所有的其他 API 调用都无效

##### 接口定义

	public static void stopPush(Context context);
	
##### 参数说明

+ context 应用的 ApplicationContext

#### API - resumePush

恢复推送服务。

调用了此 API 后，极光推送完全恢复正常工作。

##### 接口定义

	public static void resumePush(Context context);
	
##### 参数说明

	context 应用的 ApplicationContext

#### API - isPushStopped

用来检查 Push Service 是否已经被停止

+ SDK 1.5.2 以上版本支持。

##### 接口定义

	public static boolean isPushStopped(Context context);

#####参数说明

+ context 应用的 ApplicationContext

####代码示例
	
以下代码来自于 [JPush Android Example。]()

	public class MainActivity extends InstrumentedActivity implements OnClickListener {
	    private Button mStopPush;
	    private Button mResumePush;
	     
	    @Override
	    public void onCreate(Bundle savedInstanceState) {
	        super.onCreate(savedInstanceState);
	        setContentView(R.layout.main);
	        initView();
	    }
	     
	    // 初始化按钮
	    private void initView() {       
	        mStopPush = (Button)findViewById(R.id.stopPush);
	        mStopPush.setOnClickListener(this);
	         
	        mResumePush = (Button)findViewById(R.id.resumePush);
	        mResumePush.setOnClickListener(this);
	    }
	 
	    @Override
	    public void onClick(View v) {
	        switch (v.getId()) {
	 
	        // 点击停止按钮后，极光推送服务会被停止掉
	        case R.id.stopPush:
	            JPushInterface.stopPush(getApplicationContext());
	            break;
	 
	        // 点击恢复按钮后，极光推送服务会恢复正常工作
	        case R.id.resumePush:
	            JPushInterface.resumePush(getApplicationContext());
	            break;
	        }
	    }
	}

## Rich Push 开发指南

## Android 常见问题

### 为什么应用程序无法收到 Push 消息（Android）？
+ 确认 appKey（在Portal上生成的）已经正确的写入 Androidmanifest.xml
+ 确认测试手机（或者模拟器）已成功连入网络
+ 确认有客户端 "Login succeed" 日志

详情请参考教程：[Android SDK 调试指南。]()

### Java.lang.UnsatisfiedLinkError

![](image/error.jpg)

此错误是由于没有正确的加载libjpush.so文件，请检查libjpush.so是否在正确的位置(libs–>armeabi–>libjpush.so)


如果您的项目有libs/armeabi-v7a这个目录，请把libjpush.so也复制一份到这个目录。

如果您的应用需要支持 x86、mips 架构的CPU 需要下载对应的SDK，下载路径：[http://docs.jpush.cn/display/dev/Android](http://docs.jpush.cn/display/dev/Android) 

![](image/dictionary_path.png)

### The permission should be defined 

![](image/permission.jpg)

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

![](image/none_target.png)

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

