# QuickApp SDK API

##SDK 初始化 API

+ ***JAnalyticsInterface.init(context,appkey:string,channel:string)***
	+ 接口说明：
		+ 初始化接口。需app.ux的onCreate中调用。之后在其它模块中可使用this.$app.JAnalyticsInterface方式进行其它接口调用。
	+ 参数说明：
		+ context：应用上下文
		+ appkey：官网中创建应用后分配的appkey
		+ channel：渠道名称，默认值为:default-channel
		
	+ 调用示例：
	
~~~			
	this.JAnalyticsInterface=JAnalyticsInterface.init(this,"官网中创建应用后分配的appkey","自定义channel");
~~~

+ ***JAnalyticsInterface.setDebugMode(enable:boolean)***
	+ 接口说明：
		+ 设置是否开启debug模式。true则会打印更多的日志信息。设置false则会关闭sdk的所有日志打印,建议在init接口之前调用。
	+ 参数说明：
		+ enable：debug开关 
	+ 调用示例：

~~~
	JAnalyticsInterface.setDebugMode(true);
~~~

<a name="pageflow"></a>
##页面流统计 API

+ ***JAnalyticsInterface.onPageStart(pageName:string)***
	+ 接口说明：
		+ 页面启动接口。在页面的相关生命周期内调用，和onPageEnd需要成对调用。页面生命周期方法可参考[Quick App官方文档](https://doc.quickapp.cn/tutorial/framework/lifecycle.html)
	+ 参数说明：
		+ pageName：页面名称 
	+ 调用示例：
	
~~~
	this.$app.JAnalyticsInterface.onPageStart("page1");
~~~

+ ***JAnalyticsInterface.onPageEnd(pageName:string)***
	+ 接口说明：
		+ 页面结束接口。在页面的相关生命周期内调用，和onPageStart需要成对调用。
	+ 参数说明：
		+ pageName：页面名称 
	+ 调用示例：
	
~~~	
	this.$app.JAnalyticsInterface.onPageEnd("page1");
~~~
 
##自定义事件统计 API

+ ***JAnalyticsInterface.onEvent(event:Event)***
	+ 接口说明：
		+ 自定义事件。通过传入不同的事件模型来进行各种事件的统计，具体的事件模型请查看事件模型介绍
	+ 参数说明：
		+ event:事件模型，支持CountEvent(计数事件)、CalculateEvent(计算事件)、RegisterEvent(注册事件)、LoginEvent(登录事件)、BrowseEvent(浏览事件)、PurchaseEvent(购买事件)

**关于自定义事件做如下说明：**

1. 字符串字段（key与 value）限制大小不超过256字节，超过限制的key或value该事件将会被丢弃.
2. 自定义键值对数目不能超过10个，超过10个限制该事件将会被丢弃.

<a name="times"></a>
##计数事件模型
+ ***CountEvent***

该模型是自定义计数事件模型，可以设置参数进行数据上报。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| eventId | String |事件Id(非空)|
| extMap | Map | 扩展参数 |
 
调用示例:

~~~
	let { CountEvent } = this.$app.JAnalyticsInterface.Event;
	let cEvent = new CountEvent("eventId",{"key_count_event_extra1":"value_extra1"});
	this.$app.JAnalyticsInterface.onEvent(cEvent);
~~~

**注意：**

		自定义计数事件模型中扩展参数中不能使用以下 key 值：
		event_id
		此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="count"></a>
##计算事件模型
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
	let { CalculateEvent } = this.$app.JAnalyticsInterface.Event;
	let cEvent = new CalculateEvent("test2_event_id","test2_event_value");
	cEvent.setEventValue(1.1).addKeyValue("key1","value1").addKeyValue("key2","value2");
	this.$app.JAnalyticsInterface.onEvent(cEvent);
~~~

**注意：**
     
     自定义计算事件模型中扩展参数中不能使用以下 key 值：
     event_id
     event_value
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="login"></a>
##登录事件模型
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
	let { LoginEvent } = this.$app.JAnalyticsInterface.Event;
	let lEvent = new LoginEvent("qq",true);
	lEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
	this.$app.JAnalyticsInterface.onEvent(lEvent);
~~~

**注意：**

     登录事件模型中扩展参数中不能使用以下 key 值：
     login_method
     login_success
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="register"></a>
##注册事件模型
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
	let { RegisterEvent } = this.$app.JAnalyticsInterface.Event;
	let rEvent = new RegisterEvent("sina",true);
	rEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
	this.$app.JAnalyticsInterface.onEvent(rEvent);
~~~

**注意：**

	注册事件模型中扩展参数中不能使用以下 key 值:
	register_method
	register_success
	此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="content"></a>
##浏览事件模型
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
	let { BrowseEvent } = this.$app.JAnalyticsInterface.Event;
	let bEvent = new BrowseEvent("browse_id","深圳热点新闻","news",30);
	bEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
	this.$app.JAnalyticsInterface.onEvent(bEvent);
~~~

**注意：**

    浏览事件模型中扩展参数中不能使用以下 key 值：
    browse_content_id
    browse_name
    browse_type
    browse_duration
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="purchase"></a>
##购买事件模型
+ ***PurchaseEvent***

该模型是购买事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|purchaseGoodsid|String	|商品id|
|purchaseGoodsName|String|	商品名称|
|purchasePrice|double|购买价格(非空)|
|purchaseSuccess|boolean|购买是否成功(非空)|
|purchaseCurrency|String|货币类型(目前仅支持CNY及USD两种) |
|purchaseGoodsType|String|商品类型|
|purchaseGoodsCount|int	|商品数量|
|extMap|Map|扩展参数|
 
调用示例:

~~~
	let { PurchaseEvent } = this.$app.JAnalyticsInterface.Event;
	let pEvent = new PurchaseEvent("goodsId","篮球",300,true,"CNY","sport",1);
	pEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
	this.$app.JAnalyticsInterface.onEvent(pEvent);
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

## 账户维度模型介绍
开发者可以为用户增加账户信息，使统计数据可以以账户维度做统计分析 现开发的属性有：


| 中文名 |	英文名	|类型	|鉴权/备注|
|----- |----------|-----|-------|
|账号ID	|accountID	|String	|
|账号创建时间|	creationTime	|long	|时间戳
|姓名|	name|	String	|
|性别|	sex|	int|	0未知 1男 2女/不能为其他数字，默认为0
|是否付费	|paid	|int	|0未知 1是 2否/不能为其他数字，默认为0
|出生年月|	birthdate	|long|	yyyyMMdd格式校验
|手机号码|	phone	|String|	手机号码校验
|电子邮件|	email	|String|	邮箱格式校验
|新浪微博ID|	weiboID|	String	
|微信ID	|wechatID	|String	
|QQ ID	|qqID|	String	
|自定义维度	|extra	|key-value	|key只能为字符串，value只能为字符串或数字类型或null类型； 当value设置为空类型时，将该key从服务器上删除 key不能使用极光内部namespace（符号$）

具体使用方法，是先调用Account设置属性，再调用JAnalyticsInterface.identifyAccount(context, account, callback)登记账户信息
也可以只设置部分属性，再次调用identifyAccount修改账户信息
调用示例：

```
let { Account } = this.$app.JAnalyticsInterface.Account;、
let account = new Account("account001");    //account001为账号id
account.setCreationTime(1513749859);        //账户创建的时间戳
account.setName("张三");
account.setSex(1);
account.setPaid(1);
account.setBirthdate("19880920");       //"19880920"是yyyyMMdd格式的字符串
account.setPhone("13800000000");
account.setEmail("support@jiguang.cn");
account.setExtraAttr("attr1","value1");  //key如果为空，或者以极光内部namespace(符号$)开头，会设置失败并打印日志
this.$app.JAnalyticsInterface.identifyAccount(this, account, 	new function(code,msg) {
        console.log("code = " + code  + " msg =" + msg);
    }
})
```

###错误码

|code	|message	|备注
|------|---------|---|
|0	|调用成功	
|1001	|account_id |can not be empty	accountID为关键参数，不能填写null或""
|1002	|detach |failed because account_id is empty	当前没有绑定accountID时调用了解绑接口
|1003|	operation is too busy	|10s内请求频率不能超过30次
|1004|	account_id is too long, please make it less than 255 characters	|accountID长度不能超过255字符
|1005|	failed, please call JAnalyticsInterface.init(context) first	|SDK尚未初始化，应先调用init()方法
|1101|	the value of $sex should be in [0,2]	|0未知 1男 2女/不能为其他数字，默认为0
|1101	|the value of $birthdate should be date as yyyyMMdd	|yyyyMMdd格式校验
|1101|	the value of $paid should be in [0,2]	|0未知 1是 2否/不能为其他数字，默认为0
|1101	|the value of $phone is NOT a phone number	|电话号码格式校验（含国际号码）
|1101	| the value of $creation_time should be number|帐号创建时间必须为数字类型
|1101|	the value of $email is NOT email address	|邮箱格式校验
|1101	|the key={key} in extra is invalid	|自定义属性key不能为空，不能使用极光内部namespace(符号$)
|1101	|the value of {key} in extra should be String or Number	|自定义属性value只能为字符串或数字类型或null类型
如果要解绑当前用户信息，调用JAnalyticsInterface.detachAccount(context, callback);
调用示例：

```
this.$app.JAnalyticsInterface.detachAccount(this, function(code,msg){
	console.log("code = " + code  + " msg =" + msg);
})
```