# Android API

## 停止与恢复推送服务 API
### 支持的版本

开始的版本：v1.3.3

### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者App可以通过调用停止推送服务API来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。如果停止推送服务后，开发者App被重新安装，或者被清除数据，JPush SDK 会恢复正常的默认行为。（因为保存在本地的状态数据被清除掉了）。
> 
> 本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息，恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。

### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

+ JPush Service 不在后台运行
+ 收不到推送消息
+ 不能通过 JPushInterface.init 恢复，需要调用resumePush恢复。
+ 极光推送所有的其他 API 调用都无效

#### 接口定义

	public static void stopPush(Context context);
	
#### 参数说明

+ context 应用的 ApplicationContext

### API - resumePush

恢复推送服务。

调用了此 API 后，极光推送完全恢复正常工作。

#### 接口定义

	public static void resumePush(Context context);
	
#### 参数说明

	context 应用的 ApplicationContext

### API - isPushStopped

用来检查 Push Service 是否已经被停止

+ SDK 1.5.2 以上版本支持。

#### 接口定义

	public static boolean isPushStopped(Context context);

####参数说明

+ context 应用的 ApplicationContext

###代码示例
	
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
	
## 接收推送消息Receiver
	
## 别名与标签 API	

## 获取 RegistrationID API
### 支持的版本

r1.6.0 开始支持。

### 功能说明


#### RegistrationID 定义

集成了 JPush SDK 的应用程序在第一次成功注册到 JPush 服务器时，JPush 服务器会给客户端返回一个唯一的该设备的标识 - RegistrationID。JPush SDK 会以广播的形式发送 RegistrationID 到应用程序。

应用程序可以把此 RegistrationID 保存以自己的应用服务器上，然后就可以根据 RegistrationID 来向设备推送消息或者通知。



### API - getRegistrationID

调用此 API 来取得应用程序对应的 RegistrationID。 __只有当应用程序成功注册到 JPush 的服务器时才返回对应的值，否则返回空字符串。__

#### 支持的版本

开始支持的版本：1.6.0。

#### 接口定义

	//SDK 初次注册成功后，开发者通过在自定义的 Receiver 里监听 Action - cn.jpush.android.intent.REGISTRATION 来获取对应的 RegistrationID。注册成功后，也可以通过此函数获取
	public static String getRegistrationID(Context context)
	


### 附加说明

#### 通过 RegistrationID 进行点对点推送

可以通过 RegistrationID 来推送消息和通知， 参考文档 Push API v2， 当 receiver_type = 5 并且设置 receiver_value 为 RegistrationID 时候即可根据 RegistrationID 推送。

注：要使用此功能，客户端 App 一定要集成有 r1.6.0 及以上版本的 JPush Android SDK。

## 统计分析 API

#### 支持的版本

r1.6.0 版本开始。


#### 功能说明

本 API 用于“用户使用时长”，“活跃用户”，“用户打开次数”的统计，并上报到服务器，在 Portal 上展示给开发者。



#### API - onResume / onPause

##### 接口定义

	public static void onResume(final Activity activity)
	public static void onPause(final Activity activity)

##### 参数说明
		
+ Activity activity 当前所在的Activity。

##### 调用说明

应在所有的 Activity 的 onResume / onPause 方法里调用。

##### 代码示例

	@Override
	protected void onResume() {
		super.onResume();
		JPushInterface.onResume(this);
	}
	@Override
	protected void onPause() {
		super.onPause();
		JPushInterface.onPause(this);
	}




#### API - reportNotificationOpened

##### 开始版本

+ Android SDK 1.6.1

##### 功能说明

+ 用于上报用户的通知栏被打开，或者用户自定义消息被展示等客户端需要统计的事件。

##### 接口定义

	public static void reportNotificationOpened(Context context, String msgId)

参数说明

+ context：应用的 ApplicationContext
+ msgId：推送每一条消息和通知对应的唯一 ID。（msgId 来源于发送消息和通知的 Extra 字段 JPushInterface.EXTRA_MSG_ID，参考 接收推送消息Receiver）

##### 代码示例
	
	if (JPushInterface.ACTION_NOTIFICATION_OPENED.equals(intent.getAction())) {
	
	            Log.d(TAG, "[MyReceiver] 用户点击打开了通知");
	            //打开自定义的Activity
	            
	            Intent i = new Intent(context, TestActivity.class);
	            i.putExtras(bundle);
	 
	            i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
	            context.startActivity(i);         
	            // Activity 被打开，上报服务器统计。
	            
	            JPushInterface.reportNotificationOpened(
	            	context, 	                  
	            	bundle.getString(JPushInterface.EXTRA_MSG_ID));
	        }

## 清除通知 API

#### 支持的版本

开始的版本：1.3.5。

#### 功能说明

推送通知到客户端时，由 JPush SDK 展现通知到通知栏上。

此 API 提供清除通知的功能，包括：清除所有 JPush 展现的通知（不包括非 JPush SDK 展现的）；清除指定某个通知。

#### API - clearAllNotifications

##### 接口定义

	public static void clearAllNotifications(Context context);

##### 参数说明

+ Context context： 应用的ApplicationContext

	
#### API - clearNotificationById

##### 接口定义
	public static void clearNotificationById(Context context, int notificationId);

##### 参数说明

	+ Context context：应用的ApplicationContext
	+ int notificationId：通知ID

`此 notificationId 来源于intent参数 JPushInterface.EXTRA_NOTIFICATION_ID，可参考文档 接收推送消息Receiver

## 设置允许推送时间 API

#### 支持的版本

开始的版本：最初。

#### 功能说明

默认情况下用户在任何时间都允许推送。即任何时候有推送下来，客户端都会收到，并展示。

开发者可以调用此 API 来设置允许推送的时间。

如果不在该时间段内收到消息，当前的行为是：推送到的通知会被扔掉。

	这是一个纯粹客户端的实现。

	所以与客户端时间是否准确、时区等这些，都没有关系。
#### API - setPushTime

##### 接口定义

	public static void setPushTime(Context context, Set<Integer> weekDays, int startHour, int int endHour)

##### 参数说明

+ Context context 应用的ApplicationContext
+ Set<Integer> days  0表示星期天，1表示星期一，以此类推。 （7天制，Set集合里面的int范围为0到6）
	+ Sdk1.2.9 – 新功能:set的值为null,则任何时间都可以收到消息和通知，set的size为0，则表示任何时间都收不到消息和通知.
+ int startHour 允许推送的开始时间 （24小时制：startHour的范围为0到23）
+ int endHour 允许推送的结束时间 （24小时制：endHour的范围为0到23）

##### 代码示例

	Set<Integer> days = new HashSet<Integer>();
	days.add(1);
	days.add(2);
	days.add(3);
	days.add(4);
	days.add(5);
	JPushInterface.setPushTime(getApplicationContext(), days, 10, 23);

此代码表示周一到周五、上午10点到晚上23点，都可以推送。

## 设置通知静默时间 API
### 支持的版本

开始的版本：v1.4.0

### 功能说明

默认情况下用户在收到推送通知时，客户端可能会有震动，响铃等提示。但用户在睡觉、开会等时间点希望为 "免打扰" 模式，也是静音时段的概念。

开发者可以调用此 API 来设置静音时段。如果在该时间段内收到消息，则：不会有铃声和震动。


### API - setSilenceTime

#### 接口定义

	public static void setSilenceTime(Context context, int startHour, int startMinute, int endHour, int endMinute)
	
#### 参数说明
	
+ Context context 应用的ApplicationContext
+ int startHour 静音时段的开始时间 - 小时 （24小时制，范围：0~23 ）
+ int startMinute 静音时段的开始时间 - 分钟（范围：0~59 ）
+ int endHour 静音时段的结束时间 - 小时 （24小时制，范围：0~23 ）
+ int endMinute 静音时段的结束时间 - 分钟（范围：0~59 ）

#### 代码示例
	
	JPushInterface.setSilenceTime(getApplicationContext(), 22, 30, 8, 30);

此代码表示晚上10：30点到第二天早上8：30点为静音时段。

## 通知栏样式定制 API
### 支持的版本
开始的版本：最初。


### 功能说明
大多数情况下，开发者不需要调用这里的定制通知栏 API 来自定义通知栏样式，只需要使用 SDK 默认的即可。

如果您想：

+ 改变 Notification 里的铃声、震动、显示与消失行为
+ 自定义通知栏显示样式
+ 不同的 Push 通知，Notification样式不同

则请使用本通知栏定制API提供的能力。

### API - 设置默认通知栏样式构建类
	public static void setDefaultPushNotificationBuilder(BasicPushNotificationBuilder builder)

当用户需要定制默认的通知栏样式时，则可调用此方法。

极光 Push SDK 提供了 2 个用于定制通知栏样式的构建类：

+ BasicPushNotificationBuilder
	+ Basic 用于定制 Android Notification 里的 defaults / flags / icon 等基础样式（行为）
+ CustomPushNotificationBuilder
	+ 继承 Basic 进一步让开发者定制 Notification Layout
	
	
如果不调用此方法定制，则极光Push SDK 默认的通知栏样式是：Android标准的通知栏提示。



### API - 设置某编号的通知栏样式构建类


public static void setPushNotificationBuilder(Integer notificationBuilderId, BasicPushNotificationBuilder builder)

当开发者需要为不同的通知，指定不同的通知栏样式（行为）时，则需要调用此方法设置多个通知栏构建类。

设置时，开发者自己维护 notificationBuilderId 这个编号，下发通知时使用 n_builder_id 指定该编号，从而 Push SDK 会调用开发者应用程序里设置过的指定编号的通知栏构建类，来定制通知栏样式。


### 教程与代码示例

请参考文档：[自定义通知栏样式教程](../android_tutorials)

## 设置保留最近通知条数 API


### 支持的版本
开始的版本：v1.3.0


### 功能说明
通过极光推送，推送了很多通知到客户端时，如果用户不去处理，就会有很多保留在那里。

新版本 SDK (v1.3.0) 增加此功能，限制保留的通知条数。默认为保留最近 5 条通知。

开发者可通过调用此 API 来定义为不同的数量。

> 所谓保留最近的，意思是，如果有新的通知到达，之前列表里最老的那条会被移除。
> 
> 例如，设置为保留最近 5 条通知。假设已经有 5 条显示在通知栏，当第 6 条到达时，第 1 条将会被移除。


### API - setLatestNotificationNumber

#### 接口定义
	public static void setLatestNotifactionNumber(Context context, int maxNum)
#### 参数说明
+ context 应用的 ApplicationContext
+ maxNum 最多显示的条数

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用。可以调用多次。SDK使用最后调用的数值。

#### 代码示例

```
JPushInterface.init(context);
JPushInterface.setLatestNotificationNumber(context, 3);
```	


## 富文本页面 Javascript 回调API
### 支持的版本

开始的版本：1.4.0。

### 功能说明
富媒体推送通知时，用户可以用自定义的Javascript 函数来控制页面，如关闭当前页面，点击按钮跳转到指定的 Activity，通知应用程序做一些指定的动作等。

此 API 提供的回调函数包括：关闭当前页面，打开应用的主 Activity, 根据 Activity 名字打开对应的 Activity，以广播的形式传递页面参数到应用程序等功能。


### API - 关闭当前页面
	JPushWeb.close();
在HTML中调用此函数后,当前页面将会被关闭。

### API - 打开主Activity

	JPushWeb.startMainActivity(String params)
	
在HTML中调用此函数后,会打开程序的主Activity， 并在对应的 Intent 传入参数 ”params“ ，Key 为 JPushInterface.EXTRA_EXTRA。

对应 Activity 获取 params 示例代码：

```
Intent intent = getIntent();
if (null != intent ) {
    String params = intent.getStringExtra(JPushInterface.EXTRA_EXTRA);
}
 
```

### API - 触发App里执行动作

	JPushWeb.triggerNativeAction(String params)
在HTML中调用此函数后,会以广播的形式传递 ”params“ 到应用程序并触发客户端动作。

客户端 AndroidManifest.xml 配置：

```
<receiver  android:name="MyReceiver">
     ................
     <intent-filter>
    <action android:name="cn.jpush.android.intent.ACTION_RICHPUSH_CALLBACK" /> 
    <category android:name="com.example.jpushdemo" />
     </intent-filter>
</receiver>
```	
 在 MyReceiver 中获取 ”params“  代码示例：

```
if (JPushInterface.ACTION_RICHPUSH_CALLBACK.equals(intent.getAction())) {
        Log.d(TAG, "用户收到到RICH PUSH CALLBACK: " + bundle.getString(JPushInterface.EXTRA_EXTRA));
        //在这里根据 JPushInterface.EXTRA_EXTRA 的内容触发客户端动作，比如打开新的Activity 、打开一个网页等.     
   }
```

### HTML 代码示例 
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
  <title>JPush Webview Test</title>
  <script>
       function clickButton() {
         JPushWeb.close();
       }
 
      function openUrl() {
         var json = "{'action':'open', 'url':'www.jpush.cn'}";
         JPushWeb.triggerNativeAction(json);
         JPushWeb.close(); //客服端在广播中收到json 后，可以打开对应的URL。
      }
 </script>
 </head>
 <body>
     <button onclick="javascript:clickButton(this);return false;">Close</button>
     <button onclick="javascript:JPushWeb.startMainActivity('test - startMainActivity');return false;">StartMainActivity</button>
     <button onclick="javascript:JPushWeb.triggerNativeAction('test - triggerNativeAction');Javascript:JPushWeb.close();">triggerNativeAction and Close current webwiew</button>
     <button onclick="javascript:JPushWeb.startActivityByName('com.example.jpushdemo.TestActivity','test - startActivityByName');">startActivityByName</button>
     <button onclick="javascript:openUrl();">open a url</button>
 </body>
</html>
```


## 客户端错误码定义
|错误码|错误描述|
|-|-|
|-997	|注册失败（一般是由于没有网络造成的）<p>如果确保设备网络正常，还是一直遇到此问题，则还有另外一个原因：JPush 服务器端拒绝注册。<p>而这个的原因一般是：你当前的 App 的 Android 包名，以及 appKey ，与你在 Portal 上注册的应用的 Android 包名与 appKey 不相同。|
|1005	|包名和Appkey不匹配|
|-996	|网络连接断开<p>如果确保设备网络正常，可能是由于包名不正确，服务器强制断开客户端的连接。|
|-994	|网络连接超时|
