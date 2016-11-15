# 极光统计 Android SDK 集成指南

##使用提示

本文是JAnalytics Android SDK 标准的集成指南文档。

匹配的 SDK 版本为：v1.0.0及以后版本。

+ 如果您想要快速地测试、请参考本文在几分钟内跑通Demo。
+ 极光推送文档网站上，有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
+ [极光社区](http://community.jiguang.cn/)网站：大家除了文档之外，还有问题与疑问，会到这里来提问题，以及时地得到解答。

##产品功能说明
利用事件模版统计App用户的行为事件并上报给极光服务器，极光提供加工过的数据通过WebPortal展示给开发者，让开发者更加了解自己的产品在用户手中的使用情况。
###主要场景：

	1.统计页面流
	2.统计自定义计数事件
	3.统计自定义计算事件
	
###集成压缩包内容

+ AndroidManifest.xml
	+ 客户端嵌入SDK参考的配置文件
+ libs/jcore-android_v1.x.x.jar
	+ sdk 核心包
+ libs/xxx/xx.so
	+ sdk需要用的so文件
+ libs/janalytics-android-sdk_v1.x.x.jar
	+ SDK analysis 开发包
+ example
	+ 是一个完整的 Android 项目，通过这个演示了 JAnalysis SDK 的基本用法，可以用来做参考。
	
###Android SDK 版本
目前SDK只支持Android 2.3或以上版本的手机系统.

##SDK集成步骤
+ 解压压缩包，将libs下的所有文件复制到工程的libs下面.
+ 配置AndroidManifest:
	+ 配置权限：

			<uses-permission android:name="android.permission.RECEIVER_USER_PRESENT" />
			<uses-permission android:name="android.permission.INTERNET" />
			<uses-permission android:name="android.permission.READ_PHONE_STATE" />
			<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
			<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
			<uses-permission android:name="android.permission.WRITE_SETTINGS" />
			<uses-permission android:name="android.permission.VIBRATE" />
			<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
			<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
			<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
			<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
			<uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
			<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
			<uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
			<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
			<uses-permission android:name="android.permission.GET_TASKS" />
 
	+ 配置appkey：

			<meta-data android:name="JPUSH_APPKEY" android:value="Your AppKey"/>
			<meta-data android:name="JPUSH_CHANNEL" android:value="Your Channel"/>

	+ 混淆相关：

			-keep public class cn.jiguang.analytics.android.api.** {
    			*;
			}

 
##SDK 接口说明
JAnalyticsInterface类:对外的类，包含统计sdk的所有接口

+ ***JAnalyticsInterface.init(Context context)***
	+ 接口说明：
		+ 初始化接口。建议在Application的onCreate中调用
	+ 参数说明：
		+ context：android的上下文
	+ 调用示例：
	
~~~			
	JAnalyticsInterface.init(this);
~~~

+ ***JAnalyticsInterface.onPageStart(Context context,String pageName)***
	+ 接口说明：
		+ 页面启动接口。在页面(activity和fragment)的相关生命周期内调用，和onPageEnd需要成对调用，关于activity和fragment的不同情况下会对生命周期造成影响，详细请见说明
	+ 参数说明：
		+ context：activity的上下文
		+ pageName：页面名称 
	+ 调用示例：
	
~~~
	JAnalyticsInterface.onPageStart(this,this.getClass().getCanonicalName());
~~~

+ ***JAnalyticsInterface.onPageEnd(Context context,String pageName)***
	+ 接口说明：
		+ 页面结束接口。在页面(activity和fragment)的相关生命周期内调用，和onPageStart需要成对调用，关于activity和fragment的不同情况下会对生命周期造成影响，详细请见说明
	+ 参数说明：
		+ context：activity的上下文
		+ pageName：页面名称 
	+ 调用示例：
	
~~~	
	JAnalyticsInterface.onPageEnd(this,this.getClass().getCanonicalName());
~~~
 
**关于页面流做如下说明：**

1. 开发者自己决定activity和fragment是否是一个页面。在相应的方法调用onPageStart和onPageEnd方法，并且需要是成对调用
	
2. 当activity中包含多个fragment，每个fragment都需当做页面统计时，基于fragment的切换模式，提供以下建议
	+ replace模式:这种模式切换fragment，则是正常进行onResume和onPause的生命周期。
	+ viewpage中包号多个fragment进行切换：这种模式切换需在fragment中监听 setUserVisibleHint接口，通过其返回的参数进行onPageStart和onPageEnd的调用
	+ show/hide模式:这种模式下切换fragment需要监听onHiddenChanged接口来确认fragment是否显示。并需要在onResume中也需要调用onPageStart(onPause不需要调用onPageEnd)

+ ***JAnalyticsInterface.setDebugModel(boolean enable)***
	+ 接口说明：
		+ 设置是否开启debug模式。true则会打印更多的日志信息
	+ 参数说明：
		+ enable：debug开关 
	+ 调用示例：

~~~
	JAnalyticsInterface.setDebugModel(true);
~~~

+ ***JAnalyticsInterface.onEvent(Context context,Event event)***
	+ 接口说明：
		+ 自定义事件。通过传入不同的事件模型来进行各种事件的统计，具体的事件模型请查看事件模型介绍
	+ 参数说明：
		+ context：上下文
		+ event:事件模型，支持CountEvent(计数事件)、CalculateEvent(计算事件)、RegisterEvent(注册事件)、LoginEvent(登录事件)、BrowseEvent(浏览事件)、PurchaseEvent(购买事件)

**关于自定义事件做如下说明：**

1. 字符串字段（key与 value）限制大小不超过256字节，超过限制的key或value该事件将会被丢弃.
2. 自定义键值对数目不能超过10个，超过10个限制该事件将会被丢弃.

调用示例：

~~~
	CountEvent cEvent = new CountEvent("eventId","eventName");
	JAnalyticsInterface.onEvent(cEvent);
~~~

##事件模型介绍
+ ***CountEvent***

该模型是自定义计数事件模型，可以设置参数进行数据上报。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| eventId | String |事件Id(非空)|
| extMap | Map | 扩展参数 |
 
调用示例:

~~~
	CountEvent cEvent = new Event("test1_event_id","test1_event_name");
	cEvent.addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**

		自定义计数事件模型中扩展参数中不能使用以下 key 值：
		event_id
		此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

+ ***CalculateEvent***

该模型是自定义计算事件模型，计算事件会通过相同的事件不同的值进行累加，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:------:|:----:|:-----:|
|eventId|String|事件Id(非空)|
|eventValue| double |事件的值(非空)|
|extMap|Map|扩展参数|

调用示例:

~~~
	CalculateEvent cEvent = new CalculateEvent("test2_event_id","test2_event_name");
	cEvent.setEventValue(1.1).addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**
     
     自定义计算事件模型中扩展参数中不能使用以下 key 值：
     event_id
     event_value
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

+ ***LoginEvent***

该模型是登录事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:-----:|:----:|
|loginMethod|	String|登录方式(非空)|
|loginSuccess|boolean|登录是否成功(非空)|
|extMap|Map|扩展参数|
 
调用示例:

~~~
	LoginEvent lEvent = new LoginEvent("qq",true);
	lEvent.addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**

     登录事件模型中扩展参数中不能使用以下 key 值：
     login_method
     login_success
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

+ ***RegisterEvent***

该模型是注册事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|registerMethod|	String	|注册方式(非空)|
|registerSuccess|boolean|注册是否成功(非空)|
|extMap|Map|扩展参数|
 
调用示例:

~~~
	RegisterEvent rEvent = new RegisterEvent("sina",true);
	rEvent.addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**

	注册事件模型中扩展参数中不能使用以下 key 值:
	register_method
	register_success
	此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

+ ***BrowseEvent***
 
该模型是浏览事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|browseId|String	|浏览内容id|
|browseName|String|内容名称(非空)|
|browseType|String|内容类型|
|browseDuration|long|浏览时长，单位秒|
|extMap|Map|扩展参数|
 
调用示例:

~~~
	BrowseEvent bEvent = new BrowseEvent("browse_id","深圳热点新闻","news",30);
	bEvent.addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**

    浏览事件模型中扩展参数中不能使用以下 key 值：
    browse_content_id
    browse_name
    browse_type
    browse_duration
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

+ ***PurchaseEvent***

该模型是购买事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|purchaseGoodsid|String	|商品id|
|purchaseGoodsName|String|	商品名称|
|purchasePrice|double|购买价格(非空)|
|purchaseSuccess|boolean|购买是否成功(非空)|
|purchaseCurrency|Currency|货币类型，一个枚举类|
|purchaseGoodsType|String|商品类型|
|purchaseGoodsTime|long|购买时间，单位毫秒|
|purchaseGoodsCount|int	|商品数量|
|extMap|Map|扩展参数|
 
调用示例:

~~~
	PurchaseEvent pEvent = new PurchaseEvent("goodsId","篮球",300,true,Currency.CNY,"sport,System.currentTimeMillis(),1);
	pEvent.addKeyValue("key1","value1").addKeyVaule("key2","value2");
~~~

**注意：**

    购买事件模型中扩展参数中不能使用以下 key 值：
    purchase_goods_id
    purchase_goods_name
    purchase_price
    purchase_currency
    purchase_goods_type
    purchase_quantity
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
    
## 技术支持

邮件联系：<support@jpush.cn>

问答社区：[极光社区](http://community.jiguang.cn/)