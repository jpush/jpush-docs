# MiniProgram SDK API

## SDK 初始化 API

+ ***JAnalyticsInterface.init(context)***
	+ 接口说明：
		+ 初始化接口。需在应用入口 app.js 的 App.onLaunch 方法调用。之后在其它模块中可使用 app.JAnalyticsInterface 方式进行其它接口调用。
	+ 参数说明：
		+ context：应用上下文	
	+ 调用示例：
	
~~~			
	JAnalyticsInterface.init(this);
~~~
 
## 自定义事件统计 API

+ ***app.JAnalyticsInterface.onEvent(Object)***
	+ 接口说明：
		+ 自定义事件。通过传入不同的事件模型来进行各种事件的统计，请严格按照参数类型传输，具体的事件模型请查看事件模型介绍
	+ 支持自定义事件：
		+ 计数事件、计算事件、注册事件、登录事件、浏览事件、购买事件
    

Object 参数说明

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| type | String |事件类型(必填)|
| attributes | Object | 扩展参数 |


**关于自定义事件做如下说明：**

1. 字符串字段（key 与 value）限制大小不超过 256 字节，超过限制的 key 或 value 该事件将会被丢弃。
2. 自定义键值对数目不能超过 10 个，超过 10 个限制该事件将会被丢弃。
3. SDK 参数类型校验中，数值类型(int,double,long)统一归为 number 类型判断。
4. 数值类型(int,double,long)是对应数值参数安全范围的标识，SDK 不做范围限制，请务必检查数值范围，超出安全范围的数值上报可能导致后台统计到的数据不准确。


<a name="times"></a>
## 计数事件模型
+ ***type = custom_counting***

该模型是自定义计数事件模型，可以设置参数进行数据上报。

扩展参数说明：

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| event_id | String |事件Id(非空)|
 
调用示例:

~~~
app.JAnalyticsInterface.onEvent({
    type: 'custom_counting',
    attributes: {
      event_id: 'count_id',
      // 用户自定义 key - value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
~~~

<a name="count"></a>
## 计算事件模型
+ ***type = custom_calculate***

该模型是自定义计算事件模型，计算事件会通过相同的事件不同的值进行累加，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:------:|:----:|:-----:|
|event_id|String|事件Id(非空)|
|event_value| double |事件的值(非空)|


调用示例:

~~~
app.JAnalyticsInterface.onEvent({
    type: 'custom_calculate',
    attributes: {
      event_id: 'calculate_id',
      event_value: 67.7,
      // 用户自定义 key - value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
~~~

<a name="login"></a>
## 登录事件模型
+ ***type = custom_login***

该模型是登录事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:-----:|:----:|
|login_method|	String|登录方式(非空)|
|login_success|boolean|登录是否成功(非空)|
 
调用示例:

~~~
app.JAnalyticsInterface.onEvent({
    type: 'custom_login',
    attributes: {
      login_method: 'wx',
      login_success:true,
      //用户自定义 key-value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
~~~

<a name="register"></a>
## 注册事件模型
+ ***type = custom_register***

该模型是注册事件模型，可以设置参数进行数据上报。

扩展参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|register_method|	String	|注册方式(非空)|
|register_success|boolean|注册是否成功(非空)|
 
调用示例:

~~~
app.JAnalyticsInterface.onEvent({
    type: 'custom_register',
    attributes: {
      register_method: 'wx',
      register_success: true,
      //用户自定义key-value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
~~~

<a name="content"></a>
## 浏览事件模型
+ ***type = custom_browse***
 
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
app.JAnalyticsInterface.onEvent({
    type: 'custom_browse',
    attributes: {
      browse_content_id: 'browse_id',
      browse_name:'深圳热点新闻',
      browse_type:'news',
      browse_duration:30,
      // 用户自定义 key - value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
```

<a name="purchase"></a>
## 购买事件模型
+ ***type = custom_purchase***

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
|purchase_quantity|int	|商品数量|
 
调用示例:

~~~
app.JAnalyticsInterface.onEvent({
    type: 'custom_purchase',
    attributes: {
      purchase_goods_id: 'goodsId',
      purchase_goods_name: '篮球',
      purchase_price: 300,
      purchase_success: true,
      purchase_currency: 'CNY',
      purchase_goods_type: 'sport',
      purchase_quantity: 1,
      // 用户自定义 key - value，不能与上面的 key 重复
      custom_key:'custom_value',
      ...
    }
  })
~~~