# iOS SDK API
##SDK 接口说明

1. JANALYTICSService类，包含统计SDK的所有接口
2. JANALYTICSLaunchConfig类，统计SDK启动配置模型
3. JANALYTICSEventObject类，统计事件模型

---

##SDK SDK初始化
+ ***\+ (void)setupWithConfig:(JANALYTICSLaunchConfig \*)config***
	+ 接口说明：
		+ 初始化接口,建议在application:didFinishLaunchingWithOptions:中调用

	+ 参数说明：
		+ config：JANALYTICSLaunchConfig类

	+ 调用示例：

~~~
	JANALYTICSLaunchConfig * config = [[JANALYTICSLaunchConfig alloc] init];
 
	config.appKey = @"your appkey";
	 
	config.channel = @"channel";
	 
	[JANALYTICSService setupWithConfig:config];
~~~
<a name="pageflow"></a>
##SDK 页面流统计
+ ***\+ (void)startLogPageView:(NSString \*)pageName***
	+ 接口说明：
		+ 页面流统计开始接口，建议在ViewControler的viewDidAppear:方法中调用

	+ 参数说明：
		+ pageName：要开始统计的页面名

	+ 调用示例：

~~~
- (void)viewDidAppear:(BOOL)animated {
    [JANALYTICSService startLogPageView:@"first_page_flow"];
    [super viewDidAppear:animated];
}
~~~

+ ***\+ (void)stopLogPageView:(NSString \*)pageName***
	+ 接口说明：
		+ 页面流统计结束接口，建议在ViewControler的viewDidDisappear:方法中调用；结束后，默认即时上报此页面。可通过[setFrequency:]方法更改为周期性上报策略

	+ 参数说明：
		+ pageName：要结束统计的页面名

	+ 调用示例：

~~~
- (void)viewDidDisappear:(BOOL)animated {
    [JANALYTICSService stopLogPageView:@"first_page_flow"];
    [super viewDidDisappear:animated];
}
~~~

##SDK 地理位置统计
+ ***\+ (void)setLatitude:(double)latitude longitude:(double)longitude***
	+ 接口说明：
		+ 上报LBS信息

	+ 参数说明：
		+ latitude：纬度
		+ longitude： 经度

调用示例：

~~~
	[JANALYTICSService setLatitude:116.46 longitude:39.92];
~~~
+ ***\+ (void)setLocation:(CLLocation \*)location***
	+ 接口说明：
		+ 上报LBS信息

	+ 参数说明：
		+ 	location: CoreLocation.framework框架中的LBS类

调用示例：

~~~
	CLLocation * location = [[CLLocation alloc] initWithCoordinate:CLLocationCoordinate2DMake(116.46, 39.92) altitude:50 horizontalAccuracy:50 verticalAccuracy:50 timestamp:[NSDate date]];
	[JANALYTICSService setLocation:location];
~~~

##SDK 崩溃日志统计
+ ***\+ (void)crashLogON***
	+ 接口说明：
		+ 开启crash日志收集，默认是关闭状态

调用示例：

~~~
	[JANALYTICSService crashLogON];
~~~

##SDK 日志等级设置
+ ***\+ (void)setDebug:(BOOL)enable***
	+ 接口说明：
		+ 设置是否打印sdk产生的Debug级log信息, 默认为NO(不打印log)

	+ 参数说明：
		+ enable：设置为YES开启，设置为NO关闭

调用示例：

~~~
	[JANALYTICSService setDebug:YES];
~~~

##事件统计
+ ***\+ (void)eventRecord:(JANALYTICSEventObject \*)event***
	+ 接口说明：
		+ 自定义事件。通过传入不同的事件模型来进行各种事件的统计，具体的事件模型请查看事件模型介绍

	+ 参数说明：
		+ event：事件统计对象

**关于事件统计的说明：**

1. 模板属性值分为非空和可选，参考下面介绍
2. 字符串属性以及自定义属性（extra中的key与value）限制大小不超过256字节，当存在越界时该事件将会被丢弃.
3. 自定义键值对数目不能超过10个，超过10个限制该事件将会被丢弃.
4. 默认即时上报事件。可通过[setFrequency:]方法更改为周期性上报策略

+ ***JANALYTICSEventObject***

该模型是通用的父模型，不能单独使用
参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:-----:|:----:|
|extra|	NSDictionary<NSString *, NSString *>|自定义属性|


<a name="login"></a>
##登录事件模型
+ ***JANALYTICSLoginEvent***

该模型是登录事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:-----:|:----:|
|method|	NSString|登录方式(非空)|
|success|BOOL|登录是否成功(非空)|

调用示例:

~~~
	JANALYTICSLoginEvent * event = [[JANALYTICSLoginEvent alloc] init];
	 
	event.success = YES;
	 
	event.method = @"login type";
	 
	event.extra = @{@"custom key1":@"custom value"};
	 
	[JANALYTICSService eventRecord:event];
~~~

**注意：**

     登录事件模型中扩展参数中不能使用以下 key 值：
     login_method
     login_success
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="register"></a>
##注册事件模型
+ ***JANALYTICSRegisterEvent***

该模型是注册事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|method|	NSString	|注册方式(非空)|
|success|BOOL|注册是否成功(非空)|

调用示例:

~~~
    JANALYTICSRegisterEvent * event = [[JANALYTICSRegisterEvent alloc] init];
 
    event.success = YES;
 
    event.method = @"register type";
 
    event.extra = @{@"custom key1":@"custom value"};
 
    [JANALYTICSService eventRecord:event];
~~~

**注意：**

	注册事件模型中扩展参数中不能使用以下 key 值:
	register_method
	register_success
	此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="purchase"></a>
##购买事件模型
+ ***JANALYTICSPurchaseEvent***

该模型是购买事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|goodsID|NSString	|商品id|
|goodsName|NSString|	商品名称|
|price|CGFloat|购买价格(非空)|
|success|BOOL|购买是否成功(非空)|
|currency|JANALYTICSPurchaseCurrency|货币类型，目前只支持CNY/USD,具体请参考JANALYTICSPurchaseEvent头文件|
|goodsType|NSString|商品类型|
|quantity|NSInteger|商品数量|

调用示例:

~~~
    JANALYTICSPurchaseEvent * event = [[JANALYTICSPurchaseEvent alloc] init];
 
    event.success = NO;
 
    event.price = 5388.0;
 
    event.goodsName = @"iphone7";
 
    event.goodsType = @"phone";
 
    event.quantity = 1000.1;
 
    event.goodsID = @"123456";
 
    event.currency = JANALYTICSCurrencyCNY;
 
    event.extra = @{@"custom key1":@"custom value"};
 
    [JANALYTICSService eventRecord:event];
~~~

**注意：**

    购买事件模型中扩展参数中不能使用以下 key 值：
    purchase_goods_id
    purchase_goods_name
    purchase_price
    purchase_currency
    purchase_goods_type
    purchase_quantity
    purchase_success
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="content"></a>
##浏览事件模型
+ ***JANALYTICSBrowseEvent***

该模型是浏览事件模型，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|contentID|NSString|浏览内容id|
|name|NSString|内容名称(非空)|
|type|NSString|内容类型|
|duration|CGFloat|浏览时长|

调用示例:

~~~
  JANALYTICSBrowseEvent * event = [[JANALYTICSBrowseEvent alloc] init];
 
  event.name = @"browse name";
 
  event.type = @"browse type";
 
  event.contentID = @"browse id";
 
  event.duration = 1.2;
 
  event.extra = @{@"custom key1":@"custom value"};
 
  [JANALYTICSService eventRecord:event];
~~~

**注意：**

    浏览事件模型中扩展参数中不能使用以下 key 值：
    browse_content_id
    browse_name
    browse_type
    browse_duration
    此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="times"></a>
##计数事件模型
+ ***JANALYTICSCountEvent***

该模型是自定义计数事件模型，可以设置参数进行数据上报。

参数说明：

| 参数名称 | 参数类型 | 参数说明 |
|:-------:|:------:|:-------:|
| eventID | NSString |事件ID(非空)|

调用示例:

~~~
  JANALYTICSCountEvent * event = [[JANALYTICSCountEvent alloc] init];
 
  event.eventID = @"event id";
 
  event.extra = @{@"custom key1":@"custom value"};
 
  [JANALYTICSService eventRecord:event];
~~~

**注意：**

		自定义计数事件模型中扩展参数中不能使用以下 key 值：
		event_id
		此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.
<a name="count"></a>
##计算事件模型
+ ***JANALYTICSCalculateEvent***

该模型是自定义计算事件模型，计算事件会通过相同的事件不同的值进行累加，可以设置参数进行数据上报。

参数说明：

|参数名称|参数类型|参数说明|
|:------:|:----:|:-----:|
|eventId|String|事件Id(非空)|
|value|CGFloat|事件的值(非空)|

调用示例:

~~~
  JANALYTICSCalculateEvent * event = [[JANALYTICSCalculateEvent alloc] init];
 
  event.eventID = @"event id";
 
  event.value = 10.2;
 
  event.extra = @{@"custom key1":@"custom value"};
 
  [JANALYTICSService eventRecord:event];
~~~

**注意：**

     自定义计算事件模型中扩展参数中不能使用以下 key 值：
     event_id
     event_value
     此类 key 已被模型使用，如果使用则会导致统计到的数据不准确.


##SDK 设置用户信息
+ ***\+ (void)identifyAccount:(JANALYTICSUserInfo \*)userInfo with:(void (\^)(NSInteger err, NSString \* msg))completion***
	+ 接口说明：
		+ 绑定用户维度

	+ 参数说明：
		+ userInfo：用户信息模型
		+ completion： 错误码和错误信息callback

调用示例：

~~~
  JANALYTICSUserInfo * userinfo = [[JANALYTICSUserInfo alloc] init];
  userinfo.accountID = @"janalyticsID1";
  userinfo.creationTime = [[NSDate date] timeIntervalSince1970];
  userinfo.sex = JANALYTICSSexMale;
  userinfo.paid = JANALYTICSPaidPaid;
  userinfo.email = @"test@jiguang.cn";
  [userinfo setExtraObject:@"extraObj1" forKey:@"extrakey1"];
  
  [JANALYTICSService identifyAccount:userinfo with:^(NSInteger err, NSString *msg) {
    if (err) {
      NSLog(@"identify ERR:%ld|%@", err, msg);
    }else {
      NSLog(@"identify success");
    }
  }];
~~~
***JANALYTICSUserInfo***模型的使用方法请参考对应头文件

##SDK 解绑当前的用户信息
+ ***\+ (void)detachAccount:(void (\^)(NSInteger err, NSString \* msg))completion***
	+ 接口说明：
		+ 解绑当前绑定的用户维度

	+ 参数说明：
		+ completion： 错误码和错误信息callback

调用示例：

~~~
  [JANALYTICSService detachAccount:^(NSInteger err, NSString *msg) {
    if (err) {
      NSLog(@"detach ERR:%ld|%@", err, msg);
    }else {
      NSLog(@"detach success");
    }
  }];
~~~

##SDK 设置上报频率
+ ***\+ (void)setFrequency:(NSUInteger)frequency***
	+ 接口说明：
		+ 设置页面流/事件等周期上报频率
		+ 默认为未设置频率，即时上报
		+ 可以设置为0，即表示取消周期上报，改为即时上报

	+ 参数说明：
		+ frequency： 定时上报频率单位秒
		<br/>频率允许区间：0，或者 10 - 24\*60\*60的区间

调用示例：

~~~
//e.g. 十分钟上报一次 
[JANALYTICSService setFrequency:600];
~~~

##开启圈选埋点
+ ***\+ (BOOL)handleUrl:(NSURL \*)url***
	+ 接口说明：
		+ 扫码后，跳转至应用，调用此接口开启圈选埋点

	+ 参数说明：
		+ url： 圈选启动链接，请直接透传给sdk解析

调用示例：

~~~
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {
    if ([JANALYTICSService handleUrl:url]) {
        return YES;
    }
    return NO;
}
~~~

## 技术支持

邮件联系：<support@jiguang.cn>


