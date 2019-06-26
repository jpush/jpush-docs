# Web SDK API

## SDK 初始化 API

+ ***window.JAnalyticsInterface.init(Object)***
	+ 接口说明：
		+ 初始化接口。需要在页面 DOM 加载完毕后，或者在收到页面事件 onload 后调用初始化。之后页面可使用 JAnalyticsInterface 方式进行其它接口调用。
	+ 参数说明：
		+ Object：初始化参数	
	+ 调用示例：
	
~~~			
window.JAnalyticsInterface.init({
    appkey: "极光后台注册的 appkey",
    debugMode: true,
    channel:"default-channel",
    loc:false,
    singlePage:false
  });
~~~

初始化参数说明:

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| appkey | String |极光后台分配的 appkey(必填) |
| debugMode | boolean | 是否打开 debug 模式,默认 false |
| channel | String | 渠道名称，默认为 default-channel |
| loc | boolean | 是否收集位置信息，默认为 true |
| singlePage | boolean | 是否为单页面应用，默认为 false |
 
## 自定义事件统计 API

+ ***window.JAnalyticsInterface.onEvent(event:Event)***
	+ 接口说明：
		+ 自定义事件。通过传入不同的事件模型来进行各种事件的统计，请严格按照参数类型传输，具体的事件模型请查看事件模型介绍
	+ 参数说明：
    + event:事件模型，支持CountEvent(计数事件)、CalculateEvent(计算事件)、RegisterEvent(注册事件)、LoginEvent(登录事件)、BrowseEvent(浏览事件)、PurchaseEvent(购买事件)




**关于自定义事件做如下说明：**

1. 字符串字段（key 与 value）限制大小不超过 256 字节，超过限制的 key 或 value 该事件将会被丢弃。
2. 自定义键值对数目不能超过 10 个，超过 10 个限制该事件将会被丢弃。
3. SDK 参数类型校验中，数值类型(int,double,long)统一归为 number 类型判断。
4. 数值类型整型范围为 long,浮点型范围为 double，请务必检查数值范围，超出安全范围的数值上报可能导致后台统计到的数据不准确。


<a name="times"></a>
## 计数事件模型
+ ***CountEvent***

该模型是自定义计数事件模型，可以设置参数进行数据上报。

扩展参数说明：

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| event_id | String |事件Id(非空)|
 
调用示例:


~~~
    var  CountEvent  = window.JAnalyticsInterface.Event.CountEvent;
    var cEvent = new CountEvent("count_id");
    cEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(cEvent);
~~~
**注意：**

		自定义计数事件模型中扩展参数中不能使用以下 key 值：
		event_id
		此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

<a name="count"></a>
## 计算事件模型
+ ***CalculateEvent***

该模型是自定义计算事件模型，计算事件会通过相同的事件不同的值进行累加，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:------:|:----:|:-----:|
|event_id|String|事件Id(非空)|
|event_value| double |事件的值(非空)|


调用示例:

~~~
    var  CalculateEvent  = window.JAnalyticsInterface.Event.CalculateEvent;
    var cEvent = new CalculateEvent("calculate_id", 24.8);
    cEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(cEvent);
~~~

**注意：**
     
     自定义计算事件模型中扩展参数中不能使用以下 key 值：
     event_id
     event_value
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

<a name="login"></a>
## 登录事件模型
+ ***LoginEvent***

该模型是登录事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:-----:|:----:|
|login_method|	String|登录方式(非空)|
|login_success|boolean|登录是否成功(非空)|
 
调用示例:

~~~
    var  LoginEvent  = window.JAnalyticsInterface.Event.LoginEvent;
    var lEvent = new LoginEvent("wx", true);
    lEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(lEvent);
~~~

**注意：**

     登录事件模型中扩展参数中不能使用以下 key 值：
     login_method
     login_success
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

<a name="register"></a>
## 注册事件模型
+ ***RegisterEvent***

该模型是注册事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|register_method|	String	|注册方式(非空)|
|register_success|boolean|注册是否成功(非空)|
 
调用示例:

~~~
    var  RegisterEvent  = window.JAnalyticsInterface.Event.RegisterEvent;
    var rEvent = new RegisterEvent("sina", false);
    rEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(rEvent);
~~~

**注意：**

	注册事件模型中扩展参数中不能使用以下 key 值:
	register_method
	register_success
	此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

<a name="content"></a>
## 浏览事件模型
+ ***BrowseEvent***
 
该模型是浏览事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|browse_content_id|String	|浏览内容 id|
|browse_name|String|内容名称(非空)|
|browse_type|String|内容类型|
|browse_duration|long|浏览时长，单位秒，最大 86400（1天）,超出范围记为 0|
 
调用示例:

```
    var  BrowseEvent  = window.JAnalyticsInterface.Event.BrowseEvent;
    var bEvent = new BrowseEvent("browse_id", "深圳热点新闻", "news", 30);
    bEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(bEvent);
```

**注意：**

    浏览事件模型中扩展参数中不能使用以下 key 值：
    browse_content_id
    browse_name
    browse_type
    browse_duration
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.

<a name="purchase"></a>
## 购买事件模型
+ ***PurchaseEvent***

该模型是购买事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|purchase_goods_id|String	|商品 id|
|purchase_goods_name|String|	商品名称|
|purchase_price|double|购买价格(非空)|
|purchase_success|boolean|购买是否成功(非空)|
|purchase_currency|String|货币类型(目前仅支持 CNY 及 USD 两种) |
|purchase_goods_type|String|商品类型|
|purchase_quantity|long	|商品数量|
 
调用示例:

~~~
    var  PurchaseEvent  = window.JAnalyticsInterface.Event.PurchaseEvent;
    var pEvent = new PurchaseEvent("goodsId", "篮球", 300, true, "CNY", 'sport', 2);
    pEvent.addKeyValue("key1", "value1").addKeyValue("key2", "value2");
    window.JAnalyticsInterface.onEvent(pEvent);
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