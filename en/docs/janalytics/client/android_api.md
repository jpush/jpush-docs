# Android SDK API

## SDK Initializes API

+ ***JAnalyticsInterface.init(Context context)***
	+ Interface Description
		+ Initialize the interface. It is recommended to call in onCreate of the Application
	+ Parameter Description:
		+ context：Android context
	+ Call Example:

```
    JAnalyticsInterface.init(this);
```

+ ***JAnalyticsInterface.setDebugMode(boolean enable)***
	+ Interface Description
		+ Set whether to enable debug mode. True will print more log information. It is recommended to call before the init interface.
	+ Parameter Description
		+ enable：Debug switch
	+ Call Example

```
    JAnalyticsInterface.setDebugMode(true);
```
+ ***AnalyticsInterface.initCrashHandler(Context context)***
	+ Interface Description
		+ Turn on log reporting of crashlog
	+ Parameter Description
		+ context: Android context
	+ Call Example

```
    JAnalyticsInterface.initCrashHandler(this);
```

+ ***JAnalyticsInterface.stopCrashHandler(Context context)***
	+ Interface Description
		+ Turn off log reporting of crashlog
	+ Parameter Description
		+ context: Android context
	+ Call Example

```
    JAnalyticsInterface.stopCrashHandler(this);
```

<a name="pageflow"></a>
## Page Flow Statistics API

+ ***JAnalyticsInterface.onPageStart(Context context,String pageName)***
	+ Interface Description
		+ Interface to launch the page. Calls in the page (activity and fragment) related life cycle, need to be in pairs with onPageEnd. Different circumstances of the activity and fragment will affect the life cycle, please see the instructions
	+ Parameter Description
		+ context：The context of activity
		+ pageName：Page name
	+ Call Example

```
    JAnalyticsInterface.onPageStart(this,this.getClass().getCanonicalName());
```

+ ***JAnalyticsInterface.onPageEnd(Context context,String pageName)***
	+ Interface Description
		+ Interface to close the page. Calls in the page (activity and fragment) related life cycle, need to be in pairs with onPageStart. Different circumstances of the activity and fragment will affect the life cycle, please see the instructions
	+ Parameter Description
		+ context：The context of activity
		+ pageName：Page name
	+ Call Example

```
    JAnalyticsInterface.onPageEnd(this,this.getClass().getCanonicalName());
```

**Instructions about the page flow:**

1.	The developer decides whether the activity and fragment are a page. The onPageStart and onPageEnd methods are called in the corresponding method and need to be called in pairs
2.	When the activity contains multiple fragments, and each fragment needs to be treated as page statistics, the following suggestions are provided based on the switching pattern of fragment:
	+ Replace mode: Switching the fragment with this mode, is normal for the life cycle of onResume and onPause
	+ Switching multiple fragments in the viewpage: In this mode, switching needs to listen to the setUserVisibleHint interface in the fragment, and call the onPageStart and onPageEnd parameters through the returned parameters.
	+ Show/hide mode: In this mode, switching the fragment needs to monitor the onHiddenChanged interface to confirm whether the fragment is displayed. And need to call onPageStart in onResume (onPause does not need to call onPageEnd)

## Custom Event Statistics API

+ ***JAnalyticsInterface.onEvent(Context context,Event event)***
	+ Interface Description
		+ Custom events. Statistics of various events need to introduce different event models. For the specific event models, please see the event model description
	+ Parameter Description
		+ context：Context of the event
		+ event: Event models that support CountEvent, CalculateEvent, RegisterEvent, LoginEvent, BrowseEvent and PurchaseEvent

**Instructions about custom events**

1.	The size of the string field (key and value) does not exceed 256 bytes. The event will be discarded if it exceeds the limited key or value.
2.	The number of custom key pairs cannot exceed 10. More than 10 restrictions will be discarded.

Call Example

```
    CountEvent cEvent = new CountEvent("eventId","eventName");
    JAnalyticsInterface.onEvent(context, cEvent);
```

<a name="times"></a>
##Count Event Model

+ CountEvent

The model is a custom count event model, which can set parameters to report data

Parameter Description：

| Parameter Name | Parameter Type | Parameter Description |
|:-------:|:------:|:-------:|
| eventId | String |Event id (not empty)|
| extMap | Map | Extended parameters |


Call Example:

```
    CountEvent cEvent = new Event("test1_event_id");
    cEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note:：**

    The following key values cannot be used in extended parameters in a custom count event model:
    event_id
    This type of key is already used by the model, and using them will result in inaccurate statistics.

<a name="count"></a>
## Calculate Event Model
+ CalculateEvent

This model is a custom calculate event model. The calculate event will be accumulated by different values of the same event. You can set the parameters to report the data.

Parameter Description:

|Parameter Name|Parameter Type|Parameter Description|
|:------:|:----:|:-----:|
|eventId|String|Event id (not empty)|
|eventValue| double |The value of the event (not empty)|
|extMap|Map|Extended parameters|

Call Example:

```
    CalculateEvent cEvent = new CalculateEvent("test2_event_id","test2_event_value");
    cEvent.setEventValue(1.1).addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note：**
```
 The following key values cannot be used in extended parameters in a custom calculate event model：
 event_id
 event_value
 This type of key is already used by the model, and using them will result in inaccurate statistics.
```
<a name="login"></a>
##Login Event Model
+ LoginEvent

This model is a login event model, which can set parameters for data reporting.

Parameter Description：

|Parameter Name|Parameter Type|Parameter Description|
|:-----:|:-----:|:----:|
|loginMethod|	String|Login method (not empty)|
|loginSuccess|boolean|Whether login is successful (not empty)|
|extMap|Map|Extended parameters|

Call Example:

```
    LoginEvent lEvent = new LoginEvent("qq",true);
    lEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note：**

```
 The following key values cannot be used in extension parameters in the login event model:
 login_method
 login_success
 This type of key is already used by the model, and using them will result in inaccurate statistics.
```

<a name="register"></a>
##
Register Event Model
+ RegisterEvent

This model is a register event model that can set parameters for data reporting

Parameter Description：

|Parameter Name|Parameter Type|Parameter Description|
|:-----:|:----:|:-----:|
|registerMethod|	String	|Registration method (non-empty)|
|registerSuccess|boolean|Whether the registration is successful (non-empty)|
|extMap|Map|Extended parameters|


Call Example:

```
    RegisterEvent rEvent = new RegisterEvent("sina",true);
    rEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note：**

```
The following key values cannot be used in extended parameters in the register event model:
register_method
register_success
This type of key is already used by the model, and using them will result in inaccurate statistics.
```

<a name="content"></a>
##Browse Event Model
+ BrowseEvent

This model is a browse event model, which can set parameters for data reporting.

Parameter Description：

|Parameter Name|Parameter Type|Parameter Description|
|:-----:|:----:|:-----:|
|browseId|String	|Browse content id|
|browseName|String|Content name (not empty)|
|browseType|String|Content type|
|browseDuration|long|Browse duration, in seconds|
|extMap|Map|Extended parameters|

Call Example:

```
    BrowseEvent bEvent = new BrowseEvent("browse_id","深圳热点新闻","news",30);
    bEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note:**
```
The following key values cannot be used in the extended parameters in the browse event model:
browse_content_id
browse_name
browse_type
browse_duration
This type of key is already used by the model, and using them will result in inaccurate statistics.
```

<a name="purchase"></a>
##Purchase Event Model
+ PurchaseEvent

This model is a purchase event model, which can set parameters for data reporting.

Parameter Description：

|Parameter Name|Parameter Type|Parameter Description|
|:-----:|:----:|:-----:|
|purchaseGoodsid|String	|Product id|
|purchaseGoodsName|String|	Product name|
|purchasePrice|double|Purchase price (non-empty)|
|purchaseSuccess|boolean|Whether the purchase is successful (not empty)|
|purchaseCurrency|Currency|Currency type, an enumeration class|
|purchaseGoodsType|String|Product types|
|purchaseGoodsCount|int	|Product quantity|
|extMap|Map|Extended parameters|


Call Example

```
    PurchaseEvent pEvent = new PurchaseEvent("goodsId","篮球",300,true,Currency.CNY,"sport",1);
    pEvent.addKeyValue("key1","value1").addKeyValue("key2","value2");
```

**Note:**

```
The following key values cannot be used in extended parameters in the purchase event model
purchase_goods_id
purchase_goods_name
purchase_price
purchase_currency
purchase_goods_type
purchase_quantity
This type of key is already used by the model, and using them will result in inaccurate statistics.
```

## Statistics Report Period API

+ ***JAnalyticsInterface.setAnalyticsReportPeriod(int period)***
	+ Interface description:
		+ Set the automatic cycle for statistics reporting, which defaults the period to 60 seconds before being called
	+ Parameter description
		+ Period: In seconds. The minimum is 10 seconds, and the maximum is 1 day. Out of range will print call failure log
	+ Call Example：

~~~
	JAnalyticsInterface.setAnalyticsReportPeriod(getApplicationContext(), 60);
~~~

## Introduction of Account Dimension Model

Developers can increase account information for users, so that statistical data can be statistically analyzed with account dimensions.

Currently development attributes are:

|CN Name|EN Name|Type|Authentication/Remarks|
|:-----:|:----:|:-----:|:-----:|
|Account ID|accountID|String	||
|Account creation time|creationTime|long|Timestamps|
|Name|name|String||
|Gender|sex|int|0 for unknown, 1 for male, 2 for female. Cannot be other numbers, and the default is 0|
|Whether is free|paid|int|0 for unknown, 1 for yes, 2 for no. Cannot be other numbers, and the default is 0|
|Year of birth|birthdate|long|yyyyMMdd format verification|
|Phone number|phone|String|Phone number verification|
|E-mail|email|String|Mailbox format verification|
|Sina Weibo ID|weiboID|String||
|WeChat ID|wechatID|String||
|QQ ID|qqID|String||
|Custom dimension|extra	|key-value|Key can only be a string,  and value can only be a string or numeric type or null type; when the value is set to an empty type, removing the key from the server cannot use Jiguang internal namespace (symbol $)|


The specific use method is to first call the cn.jiguang.analytics.android.api.Account setting properties.

Then call JAnalyticsInterface.identifyAccount(account, callback) to register account information

Can also set only some of the properties, and call identifyAccount to modify account information again

Call Example：

```
Account account = new Account("account001");    //account001为账号id
account.setCreationTime(1513749859);        //账户创建的时间戳
account.setName("张三");
account.setSex(1);
account.setPaid(1);
account.setBirthdate("19880920");       //"19880920"是yyyyMMdd格式的字符串
account.setPhone("13800000000");
account.setEmail("support@jiguang.cn");
account.setExtraAttr("attr1","value1");
JAnalyticsInterface.identifyAccount(account, new AccountCallback() {
    @Override
    public void callback(int code, String msg) {
        Log.d("tag", "code = " + code  + " msg =" + msg);
    }
})
```

AccountCallback is a callback method, which can get the success/failure of the call according to the returned code and msg

### Error Code
|code|message|Remarks|
|:-----:|:----:|:-----:|
|0|Call success||
|1001|account_id can not be empty|accountID is a key parameter and cannot be filled with null or ""|
|1002|detach failed because account_id is empty|Call to know the binding interface when no accountID is currently bound|
|1003|operation is too busy|Request frequency within 10s cannot exceed 30 times
|1004|account_id is too long, please make it less than 255 characters|Length of accountID cannot exceed 255 characters|
|1005|failed, please call JAnalyticsInterface.init(context) first|SDK not been init,should be inited first|
|1101|the value of $sex should be in [0,2]|0 for unknown, 1 for male, 2 for female. Cannot be other numbers, and the default is 0|
|1101|the value of $birthdate should be date as yyyyMMdd|yyyyMMdd format check|
|1101|the value of $paid should be in [0,2]|0 for unknown, 1 for yes, 2 for no. Cannot be other numbers, and the default is 0|
|1101|the value of $phone is NOT a phone number|Format verification of telephone number (including international number) |
|1101|the value of $email is NOT email address|Mailbox format check|
|1101|the key={key} in extra is invalid|The custom property key cannot be empty and the Jiguang internal namespace (symbol $) cannot be used|
|1101|the value of {key} in extra should be String or Number|Custom property value can only be a string or numeric type or null type|


If you want to unbind the current user information, call JAnalyticsInterface.detachAccount(callback);

Call Example：
```
JAnalyticsInterface.detachAccount(new AccountCallback() {
    @Override
    public void callback(int code, String msg) {
        Log.d("tag", "code = " + code  + " msg =" + msg);
    }
})
```
