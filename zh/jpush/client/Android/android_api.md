# Android API

## 设置调试模式 API

### API - setDebugMode

设置调试模式。

 注：该接口需在 init 接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的 Application 中 onCreate 中调用。

#### 接口定义

	public static void setDebugMode(boolean debug);

#### 参数说明

+ debug 为 true 则会打印 debug 级别的日志，false 则只会打印 warning 级别以上的日志


## 初始化推送服务 API

### API - init

初始化推送服务。

调用了本 API 后，JPush 推送服务进行初始化。建议在自定义的 Application 中的 onCreate 中调用。
#### 接口定义

	public static void init(Context context);
	
#### 参数说明

+ context 应用的 ApplicationContext

**注：** 如果暂时不希望初始化 JPush SDK ，不要调用 init， 并且在应用初始化的时候就调用 stopPush。

## 停止与恢复推送服务 API

### 支持的版本

开始支持的版本：1.3.3

### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者 App 可以通过调用停止推送服务 API 来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。
 <p>如果停止推送服务后，开发者 App 被卸载重新安装，JPush SDK 会恢复正常的默认行为。
 <p>本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息。
 <p>恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。
</div>

### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

+ 收不到推送消息
+ 极光推送所有的其他 API 调用都无效，不能通过 JPushInterface.init 恢复，需要调用 resumePush 恢复。

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

#### 参数说明

+ context 应用的 ApplicationContext

#### 代码示例
	
以下代码来自于 JPush Android Example。

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

## 配置 Channel API
### API - setChannel

动态配置 channel，优先级比 AndroidManifest 里配置的高

+ SDK 3.1.5 以上版本支持。

#### 接口定义

	public static void setChannel(Context context, String channel);

#### 参数说明

+ context 应用的 ApplicationContext
+ channel 希望配置的 channel，传 null 表示依然使用 AndroidManifest 里配置的 channel

#### 代码示例

	JPushInterface.setChannel(this, "channel_1");


## 接收推送消息 Receiver
	
### 支持的版本

开始的版本：最初。

**注：** 3.3.0开始使用[新的消息回调方式](https://docs.jiguang.cn/jpush/client/Android/android_api/#_66)
如果你依然需要在这个Receiver里接收到回调，则使用新的回调方式以后，不重写对应回调的方法，或者重写回调方法且调用super方法
如果你不需要在这个Receiver接收，则使用新的回调方式，然后重写对应回调方法，不调用super方法。
具体请参考新的消息回调方式。


### 功能说明

JPush SDK 收到推送，通过广播的方式，转发给开发者 App，这样开发者就可以灵活地进行处理。

这个动作不是必须的。用户有需要才定义 Receiver 类来处理 SDK 过来的广播。

如果不做这个动作，即不写自定义 Receiver，也不在 AndroidManifest.xml 里配置这个 Receiver，则默认的行为是：

+ 接收到推送的自定义消息，则没有被处理
+ 可以正常收到通知，用户点击打开应用主界面

### 接收广播

如果全部类型的广播都接收，则需要在 AndroidManifest.xml 里添加如下的配置信息：

	<receiver
	    android:name="Your Receiver"
	    android:enabled="true"
	    android:exported="false">
	    <intent-filter>
	        <action android:name="cn.jpush.android.intent.REGISTRATION" />
	        <action android:name="cn.jpush.android.intent.MESSAGE_RECEIVED" />
	        <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED" />
	        <action android:name="cn.jpush.android.intent.NOTIFICATION_OPENED" />
	        <action android:name="cn.jpush.android.intent.NOTIFICATION_CLICK_ACTION" />
	        <action android:name="cn.jpush.android.intent.CONNECTION" />
	        <category android:name="You package Name" />
	    </intent-filter>
	</receiver>
	
每个 Receiver action 详细解释如下。

#### Action - JPushInterface.ACTION\_REGISTRATION\_ID
##### 字符串值
	"cn.jpush.android.intent.REGISTRATION"

##### 功能描述
SDK 向 JPush Server 注册所得到的注册 ID。

一般来说，可不处理此广播信息。

要深入地集成极光推送，开发者想要自己保存 App 用户与 JPush 用户关系时，则接受此广播，取得 Registration ID 并保存与 App uid 的关系到开发者自己的应用服务器上。

使用极光推送提供的别名与标签功能，是更加简单轻便的绑定App用户与 JPush 用户的方式，请参考文档：[别名与标签使用教程。](android_senior/#_1)

##### Intent 参数

+ JPushInterface.EXTRA\_REGISTRATION\_ID
	+ SDK 向 JPush Server 注册所得到的注册 全局唯一的 ID ，可以通过此 ID 向对应的客户端发送消息和通知。
	
			Bundle bundle = intent.getExtras();
			String title = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);

#### Action - JPushInterface.ACTION\_MESSAGE\_RECEIVED
##### 字符串值
	"cn.jpush.android.intent.MESSAGE_RECEIVED"

##### 功能描述	
收到了自定义消息 Push。

SDK 对自定义消息，只是传递，不会有任何界面上的展示。

如果开发者想推送自定义消息 Push，则需要在 AndroidManifest.xml 里配置此 Receiver action，并且在自己写的 BroadcastReceiver 里接收处理。

##### Intent 参数

+ JPushInterface.EXTRA_TITLE
	+ 保存服务器推送下来的消息的标题。
	+ 对应 API 消息内容的 title 字段。
    +  Portal 推送消息界上不作展示

			Bundle bundle = intent.getExtras();
			String title = bundle.getString(JPushInterface.EXTRA_TITLE);
			
+ JPushInterface.EXTRA_MESSAGE
	+ 保存服务器推送下来的消息内容。
	+ 对应 API 消息内容的 message 字段。
	+ 对应 Portal 推送消息界面上的“自定义消息内容”字段。
	
			Bundle bundle = intent.getExtras();
			String message = bundle.getString(JPushInterface.EXTRA_MESSAGE);

+ JPushInterface.EXTRA_EXTRA
	+ 保存服务器推送下来的附加字段。这是个 JSON 字符串。
	+ 对应 API 消息内容的 extras 字段。
	+ 对应 Portal 推送消息界面上的“可选设置”里的附加字段。
	
			Bundle bundle = intent.getExtras();
			String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);
			
			
+ JPushInterface.EXTRA\_MSG\_ID
	+ SDK 1.6.1 以上版本支持。
	+ 唯一标识消息的 ID, 可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);
			
#### Action - JPushInterface.ACTION\_NOTIFICATION\_RECEIVED.
##### 字符串值
	"cn.jpush.android.intent.NOTIFICATION_RECEIVED"

##### 功能描述
收到了通知 Push。

如果通知的内容为空，则在通知栏上不会展示通知。

但是，这个广播 Intent 还是会有。开发者可以取到通知内容外的其他信息。

##### Intent 参数

+ JPushInterface.EXTRA\_NOTIFICATION\_TITLE
	+ 保存服务器推送下来的通知的标题。
	+ 对应 API 通知内容的 title 字段。
	+ 对应 Portal 推送通知界面上的“通知标题”字段。

			Bundle bundle = intent.getExtras();			
			String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
			
+ JPushInterface.EXTRA_ALERT
	+ 保存服务器推送下来的通知内容。
	+ 对应 API 通知内容的 alert 字段。
	+ 对应 Portal 推送通知界面上的“通知内容”字段。

			Bundle bundle = intent.getExtras();
			String content = bundle.getString(JPushInterface.EXTRA_ALERT);
			

+ JPushInterface.EXTRA_EXTRA
	+ SDK 1.2.9 以上版本支持。
	+ 保存服务器推送下来的附加字段。这是个 JSON 字符串。
	+ 对应 API 通知内容的 extras 字段。
	+ 对应 Portal 推送消息界面上的“可选设置”里的附加字段。

			Bundle bundle = intent.getExtras();
			String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);
			

+ JPushInterface.EXTRA\_NOTIFICATION\_ID
	+ SDK 1.3.5 以上版本支持。
	+ 通知栏的 Notification ID，可以用于清除 Notification
	+ 如果服务端内容（alert）字段为空，则 Notification ID 为 0

			Bundle bundle = intent.getExtras();
			int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);
			
									
+ JPushInterface.EXTRA\_RICHPUSH\_HTML\_PATH
	+ SDK 1.4.0 以上版本支持。
	+ 富媒体通知推送下载的 HTML 的文件路径，用于展现 WebView。

			Bundle bundle = intent.getExtras();
			String fileHtml = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_PATH);
			
+ JPushInterface.EXTRA\_RICHPUSH\_HTML\_RES
	+ SDK 1.4.0 以上版本支持。
	+ 富媒体通知推送下载的图片资源的文件名，多个文件名用 “，” 分开。与 “JPushInterface.EXTRA\_RICHPUSH\_HTML\_PATH” 位于同一个路径。

			Bundle bundle = intent.getExtras();
			String fileStr = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_RES);
			String[] fileNames = fileStr.split(",");
			
+ JPushInterface.EXTRA\_MSG\_ID
	+ SDK 1.6.1 以上版本支持。  
	+ 唯一标识通知消息的 ID，可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);
			
+ JPushInterface.EXTRA\_BIG\_TEXT
	+ SDK 3.0.0 以上版本支持，支持 api 16 以上的 rom。
	+ 大文本通知样式中大文本的内容。
	
			Bundle bundle = intent.getExtras();
			String bigText = bundle.getString(JPushInterface.EXTRA_BIG_TEXT);
						

+ JPushInterface.EXTRA\_BIG\_PIC\_PATH
    + SDK 3.0.0 以上版本支持，支持 api 16 以上的 rom。
    + 可支持本地图片的路径，或者填网络图片地址。
    + 大图片通知样式中大图片的路径/地址。
    
			Bundle bundle = intent.getExtras();
			String bigPicPath = bundle.getString(JPushInterface.EXTRA_BIG_PIC_PATH);    
 
+ JPushInterface.EXTRA_INBOX
    + SDK 3.0.0 以上版本支持，支持 api 16 以上的 rom。
    + 获取的是一个 JSONObject，json 的每个 key 对应的 value 会被当作文本条目逐条展示。
    + 收件箱通知样式中收件箱的内容。

			Bundle bundle = intent.getExtras();
			String inboxJson = bundle.getString(JPushInterface.EXTRA_INBOX);

+ JPushInterface.EXTRA\_NOTI\_PRIORITY
    + SDK 3.0.0 以上版本支持，支持 api 16 以上的 rom。
    + 默认为 0，范围为 -2～2，其他值将会被忽略而采用默认。
    + 通知的优先级。

			Bundle bundle = intent.getExtras();
			String prio = bundle.getString(JPushInterface.EXTRA_NOTI_PRIORITY);    

+ JPushInterface.EXTRA\_NOTI\_CATEGORY	
	+ SDK 3.0.0 以上版本支持，支持 api 21 以上的 rom。
	+ 完全依赖 rom 厂商对每个 category 的处理策略，比如通知栏的排序。
	+ 通知分类。

			Bundle bundle = intent.getExtras();
			String prio = bundle.getString(JPushInterface.EXTRA_NOTI_CATEGORY); 	
			
#### Action - JPushInterface.ACTION\_NOTIFICATION\_OPENED
##### 字符串值
	"cn.jpush.android.intent.NOTIFICATION_OPENED"

##### 功能描述			
用户点击了通知。
一般情况下，用户不需要配置此 receiver action。

如果开发者在 AndroidManifest.xml 里未配置此 receiver action，那么，SDK 会默认打开应用程序的主 Activity，相当于用户点击桌面图标的效果。

如果开发者在 AndroidManifest.xml 里配置了此 receiver action，那么，当用户点击通知时，SDK 不会做动作。开发者应该在自己写的 BroadcastReceiver 类里处理，比如打开某 Activity 。

##### Intent 参数

+ JPushInterface.EXTRA\_NOTIFICATION\_TITLE

	+ 保存服务器推送下来的通知的标题。
	+ 对应 API 通知内容的 title 字段。
	+ 对应 Portal 推送通知界面上的“通知标题”字段。

			Bundle bundle = intent.getExtras();
			String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
				
+ JPushInterface.EXTRA_ALERT

	+ 保存服务器推送下来的通知内容。
	+ 对应 API 通知内容的 alert 字段。
	+ 对应 Portal 推送通知界面上的“通知内容”字段。

			Bundle bundle = intent.getExtras();
			String content = bundle.getString(JPushInterface.EXTRA_ALERT);
			
+ JPushInterface.EXTRA_EXTRA	

	+ SDK 1.2.9 以上版本支持。
	+ 保存服务器推送下来的附加字段。这是个 JSON 字符串。
	+ 对应 API 消息内容的 extras 字段。
	+ 对应 Portal 推送消息界面上的“可选设置”里的附加字段。
	
			Bundle bundle = intent.getExtras();
			String type = bundle.getString(JPushInterface.EXTRA_EXTRA);
			
							
+ JPushInterface.EXTRA\_NOTIFICATION\_ID
	
	+ SDK 1.3.5 以上版本支持。
	+ 通知栏的 Notification ID，可以用于清除 Notification
	
			Bundle bundle = intent.getExtras();
			int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);
			  
+ JPushInterface.EXTRA\_MSG\_ID
	+ SDK 1.6.1 以上版本支持。
	+ 唯一标识调整消息的 ID，可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

#### Action - JPushInterface.ACTION\_NOTIFICATION\_CLICK\_ACTION
##### 字符串值
	"cn.jpush.android.intent.NOTIFICATION_CLICK_ACTION"

##### 功能描述
用户点击了通知栏中自定义的按钮。（SDK 3.0.0 以上版本支持）

使用普通通知的开发者不需要配置此 receiver action。只有开发者使用了 MultiActionsNotificationBuilder 构建携带按钮的通知栏的通知时，可通过该 action 捕获到用户点击通知栏按钮的操作，并自行处理。

##### Intent 参数

+ JPushInterface.EXTRA\_NOTIFICATION\_ACTION\_EXTRA

	+ SDK 3.0.0 以上版本支持。
	+ 获取通知栏按钮点击事件携带的附加信息。
	+ 对应使用 MultiActionsNotificationBuilder.addJPushAction 添加的按钮信息。
	
			private void setAddActionsStyle() {
				MultiActionsNotificationBuilder builder = new MultiActionsNotificationBuilder(PushSetActivity.this);
        		builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "first", "my_extra1");
        		builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "second", "my_extra2");
        		builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "third", "my_extra3");
        		JPushInterface.setPushNotificationBuilder(10, builder);

        		Toast.makeText(PushSetActivity.this, "AddActions Builder - 10", Toast.LENGTH_SHORT).show();
    		}
			
	+ 获取到对应的附加信息，确定是哪个按钮后自行处理。

			else if (JPushInterface.ACTION_NOTIFICATION_CLICK_ACTION.equals(intent.getAction())){
				Log.d(TAG, "[MyReceiver] 用户点击了通知栏按钮");
				String nActionExtra = intent.getExtras().getString(JPushInterface.EXTRA_NOTIFICATION_ACTION_EXTRA);

				//开发者根据不同 Action 携带的 extra 字段来分配不同的动作。
				if(nActionExtra==null){
					Log.d(TAG,"ACTION_NOTIFICATION_CLICK_ACTION nActionExtra is null");
					return;
				}
				if (nActionExtra.equals("my_extra1")) {
					Log.d(TAG, "[MyReceiver] 用户点击通知栏按钮一");
				} else if (nActionExtra.equals("my_extra2")) {
					Log.d(TAG, "[MyReceiver] 用户点击通知栏按钮二");
				} else if (nActionExtra.equals("my_extra3")) {
					Log.d(TAG, "[MyReceiver] 用户点击通知栏按钮三");
				} else {
					Log.d(TAG, "[MyReceiver] 用户点击通知栏按钮未定义");
				}
			}		

#### Action - JPushInterface.ACTION\_CONNECTION\_CHANGE
##### 字符串值	
	"cn.jpush.android.intent.CONNECTION"
	
##### 功能描述
JPush 服务的连接状态发生变化。（注：不是指 Android 系统的网络连接状态。）

##### Intent 参数

+ JPushInterface.EXTRA_CONNECTION_CHANGE

	+ SDK 1.6.3 以上版本支持。
	+ 获取当前 JPush 服务的连接状态。

			Bundle bundle = intent.getExtras();
			boolean connected = bundle.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);

			
### 开发者自定义 Receiver 代码示例

	public void onReceive(Context context, Intent intent) {
		Bundle bundle = intent.getExtras();
	    Log.d(TAG, "onReceive - " + intent.getAction());

	    if (JPushInterface.ACTION_REGISTRATION_ID.equals(intent.getAction())) {
	        String regId = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);
	        Log.d(TAG, "[MyReceiver] 接收 Registration Id : " + regId);
	    }else if (JPushInterface.ACTION_MESSAGE_RECEIVED.equals(intent.getAction())) {
	        Log.d(TAG, "收到了自定义消息。消息内容是：" + bundle.getString(JPushInterface.EXTRA_MESSAGE));
	        // 自定义消息不会展示在通知栏，完全要开发者写代码去处理
	    } else if (JPushInterface.ACTION_NOTIFICATION_RECEIVED.equals(intent.getAction())) {
	        Log.d(TAG, "收到了通知");
	        // 在这里可以做些统计，或者做些其他工作
	    } else if (JPushInterface.ACTION_NOTIFICATION_OPENED.equals(intent.getAction())) {
	        Log.d(TAG, "用户点击打开了通知");
	        // 在这里可以自己写代码去定义用户点击后的行为
	        Intent i = new Intent(context, TestActivity.class);  //自定义打开的界面
	        i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
	        context.startActivity(i);
	    } else {
	        Log.d(TAG, "Unhandled intent - " + intent.getAction());
	    }
	}
	
更多示例代码请参考[ Android SDK 压缩包](https://docs.jiguang.cn/jpush/resources/)中的 example 工程。
	
## 别名与标签 API	

### 功能说明

```
温馨提示，设置标签别名请注意处理 call back 结果，只有设置成功才可以向目标推送，否则服务器 API 会返回 1011 错误。
从 3.0.7 版本开始，别名和标签是异步回调，注意在 Androidmanifest 里面配置自定义广播接收器
```	

#### 别名 alias

为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。

每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，[服务器端 API ](../../server/push/rest_api_v3_push)会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用[服务器端 API ](../../server/push/rest_api_v3_push)发通知到客户端提醒用户。

#### 标签 tag

为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page,  women

### Method - filterValidTag

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>使用建议
 <br>
 <p>设置 tags 时，如果其中一个 tag 无效，则整个设置过程失败。
 <br>
 <p>如果 App 的 tags 会在运行过程中动态设置，并且存在对 JPush SDK tag 规定的无效字符，
 <p>则有可能一个 tag 无效导致这次调用里所有的 tags 更新失败。
 <br>
 <p>这时你可以调用本方法 filterValidTags 来过滤掉无效的 tags，得到有效的 tags，
 <p>再调用 JPush SDK 的 set tags / alias 方法。
</div>

#### 支持的版本

开始支持的版本：1.5.0

#### 接口的定义

	public static Set<String> filterValidTags(Set<String> tags);
	
#### 接口返回

有效的 tag 集合。


## 新别名 alias 与标签 tag 接口
新别名与标签接口支持增删改查的功能，从 3.0.7 版本开始支持，老版本别名与标签的接口从 3.0.7 版本开始不再维护。
#### 回调说明
新别名 alias 与标签 tag 接口回调触发 cn.jpush.android.service.JPushMessageReceiver，详细的回调方法请参考[新的消息回调方式说明](#new-callback)。

### Method - setAlias

调用此 API 来设置别名。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void setAlias(Context context, int sequence, String alias);

参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。

+ alias

	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）


### Method - deleteAlias

调用此 API 来删除别名。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void deleteAlias(Context context,int sequence);

参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。

### Method - getAlias

调用此 API 来查询别名。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void getAlias(Context context,int sequence);

参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。


### Method - setTags

调用此 API 来设置标签。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void setTags(Context context, int sequence,Set<String> tags);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。

+ tags

	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，且单次操作总长度不得超过 5000 字节。（判断长度需采用 UTF-8 编码）
		+ 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。


### Method - addTags

调用此 API 来新增标签。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void addTags(Context context, int sequence,Set<String> tags);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。

+ tags

	+ 每次调用至少新增一个 tag。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，且单次操作总长度不得超过 5000 字节。（判断长度需采用 UTF-8 编码）
		+ 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。


### Method - deleteTags

调用此 API 来删除指定标签。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void deleteTags(Context context, int sequence,Set<String> tags);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号,  同操作结果一起返回，用来标识一次操作的唯一性。

+ tags

	+ 每次调用至少删除一个 tag。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，且单次操作总长度不得超过 5000 字节。（判断长度需采用 UTF-8 编码）
		+ 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。


### Method - cleanTags

调用此 API 来清除所有标签。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void cleanTags(Context context, int sequence);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。


### Method - getAllTags

调用此 API 来查询所有标签。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void getAllTags(Context context, int sequence);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。


### Method - checkTagBindState

调用此 API 来查询指定 tag 与当前用户绑定的状态。

#### 支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public static void checkTagBindState(Context context,int sequence,String tag);

#### 参数定义

+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。

+ tag
	+ 被查询的 tag

## 设置手机号码接口

3.1.1 版本开始提供设置手机号码的接口，用于[短信补充功能](../../guideline/push-SMS-intro.md)。  
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>注：短信补充仅支持国内业务，号码格式为 11 位数字，有无 +86 前缀皆可。
</div>


### Method - setMobileNumber 

调用此 API 设置手机号码。该接口会控制调用频率，频率为 10s 之内最多 3 次。

#### 支持的版本

开始支持的版本：3.1.1

#### 方法定义

	public static void setMobileNumber(Context context,int sequence, String mobileNumber);

#### 参数定义
+ context
	+ 应用的ApplicationContext。
+ sequence
	+ 用户自定义的操作序列号，同操作结果一起返回，用来标识一次操作的唯一性。 
+ mobileNumber
	+ 手机号码。如果传 null 或空串则为解除号码绑定操作。
	+ 限制：只能以 “+” 或者 数字开头；后面的内容只能包含 “-” 和数字。

#### 回调说明
接口回调触发 cn.jpush.android.service.JPushMessageReceiver，详细的回调方法请参考[新的消息回调方式说明](#new-callback)。

## <span id="new-callback">新的消息回调方式说明</span>
3.0.7 版本之后新增的回调方式。
### Class - cn.jpush.android.service.JPushMessageReceiver
1. 新的消息回调方式中相关回调类。
2. 新的 tag 与 alias 操作回调会在开发者定义的该类的子类中触发。
3. 手机号码设置的回调会在开发者定义的该类的子类中触发。
4. 新回调方式与旧的自定义Receiver兼容：  
配置了此Receiver以后，默认是也会发广播给旧Receiver的  
对于onMessage、onNotifyMessageArrived、onNotifyMessageOpened、onMultiActionClicked  
如果重写了这些方法，则需要调用super才会发给旧Receiver  

该类为回调父类，开发者需要继承该类并[在 Manifest 中配置](https://docs.jiguang.cn/jpush/client/Android/android_guide/#_5)您对应实现的类，接口操作的结果会在您配置的类中的如下方法中回调。



### Method - onTagOperatorResult

tag 增删查改的操作会在此方法中回调结果。

####  支持的版本

开始支持的版本：3.0.7

#### 接口定义

	public void onTagOperatorResult(Context context, JPushMessage jPushMessage);

#### 参数定义

+ jPushMessage
	+ tag 相关操作返回的消息结果体，具体参考 JPushMessage 类的说明。

### Method - onCheckTagOperatorResult

查询某个 tag 与当前用户的绑定状态的操作会在此方法中回调结果。

#### 接口定义

	public void onCheckTagOperatorResult(Context context, JPushMessage jPushMessage);

#### 参数定义

+ jPushMessage
	+ check tag 与当前用户绑定状态的操作返回的消息结果体，具体参考 JPushMessage 类的说明。

### Method - onAliasOperatorResult

alias 相关的操作会在此方法中回调结果。

#### 方法定义

	public void onAliasOperatorResult(Context context, JPushMessage jPushMessage);

#### 参数定义

+ jPushMessage
	+ alias 相关操作返回的消息结果体，具体参考 JPushMessage 类的说明。

### Method - onMobileNumberOperatorResult

设置手机号码会在此方法中回调结果。

####  支持的版本

开始支持的版本：3.1.1

#### 方法定义

	 public void onMobileNumberOperatorResult(Context context, JPushMessage jPushMessage)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ jPushMessage
	+ 设置手机号码返回的消息结果体，具体参考 JPushMessage 类的说明。

### Class - cn.jpush.android.api.JPushMessage

1. 新的消息回调方式中相关回调的结果类，使用该类对象可获取对应的操作结果。
2. 当前仅仅新的 tag 与 alias 操作回调会涉及到该类。

### Method - getAlias

开发者传或查询得到的 alias。

####  支持的版本

开始支持的版本：3.0.7

#### 方法定义

	public String getAlias();
    
### Method - getTags

开发者传或查询得到的 tags。

####  支持的版本

开始支持的版本：3.0.7

#### 方法定义

	public Set<String> getTags();

### Method - getErrorCode

对应操作的返回码，0 为成功，其他返回码请参考错误码定义。

####  支持的版本

开始支持的版本：3.0.7

#### 方法定义

	public int getErrorCode();


### Method - getSequence

开发者调用接口时传入的 sequence，通过该 sequence 开发者可以从开发者自己缓存中获取到对应的操作。

####  支持的版本

开始支持的版本：3.0.7

#### 方法定义

	public int getSequence();

### Method - getTagCheckStateResult

开发者想要查询的 tag 与当前用户绑定的状态。

#### 支持的版本

开始支持的版本：3.0.7


#### 方法定义

	public boolean getTagCheckStateResult();

### Method - getCheckTag

 开发者想要查询绑定状态的 tag。

####  支持的版本

开始支持的版本：3.0.7


#### 方法定义

	public String getCheckTag();

### Method - getMobileNumber

开发者调用设置接口时传入的手机号码。
####  支持的版本

开始支持的版本：3.1.1

#### 方法定义

	public String getMobileNumber();

### Method - onMessage

收到自定义消息回调

####  支持的版本

开始支持的版本：3.3.0  
*** 说明 *** 
如果需要在旧版本的Receiver接收cn.jpush.android.intent.MESSAGE_RECEIVED广播  
可以不重写此方法，或者重写此方法且调用super.onMessage  
如果重写此方法，没有调用super，则不会发送广播到旧版本Receiver  

#### 方法定义

     public void onMessage(Context context, CustomMessage customMessage)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ CustomMessage
	+ 接收自定义消息内容

### Method - onNotifyMessageArrived

收到通知回调

####  支持的版本

开始支持的版本：3.3.0  
*** 说明 *** 
如果需要在旧版本的Receiver接收cn.jpush.android.intent.NOTIFICATION_RECEIVED广播  
可以不重写此方法，或者重写此方法且调用super.onNotifyMessageArrived  
如果重写此方法，没有调用super，则不会发送广播到旧版本Receiver  

#### 方法定义

	public void onNotifyMessageArrived(Context context, NotificationMessage message)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ NotificationMessage
	+ 接收到的通知内容

### Method - onNotifyMessageOpened

点击通知回调

####  支持的版本

开始支持的版本：3.3.0  
*** 说明 *** 
如果需要在旧版本的Receiver接收cn.jpush.android.intent.NOTIFICATION_OPENED广播  
可以不重写此方法，或者重写此方法且调用super.onNotifyMessageOpened  
如果重写此方法，没有调用super，则不会发送广播到旧版本Receiver    

#### 方法定义

	public void onNotifyMessageOpened(Context context, NotificationMessage message)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ NotificationMessage
	+ 点击的通知内容

### Method - onNotifyMessageDismiss

清除通知回调

####  支持的版本

开始支持的版本：3.3.0

说明:

1.同时删除多条通知，可能不会多次触发清除通知的回调

2.只有用户手动清除才有回调，调接口清除不会有回调

#### 方法定义

	public void onNotifyMessageDismiss(Context context, NotificationMessage message)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ NotificationMessage
	+ 清除的通知内容

### Method - onRegister

注册成功回调

####  支持的版本

开始支持的版本：3.3.0

#### 方法定义

	public void onRegister(Context context, String registrationId)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ registrationId
	+ 注册id

### Method - onConnected

长连接状态回调

####  支持的版本

开始支持的版本：3.3.0

#### 方法定义

	public void onConnected(Context context, boolean isConnected)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ isConnected
	+ 长连接状态

### Method - onCommandResult

注册失败回调

####  支持的版本

开始支持的版本：3.3.0

#### 方法定义

	public void onCommandResult(Context context, CmdMessage cmdMessage)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ CmdMessage
	+ 错误信息


### Method - onMultiActionClicked

通知的MultiAction回调

####  支持的版本

开始支持的版本：3.3.2  
*** 说明 *** 
如果需要在旧版本的Receiver接收cn.jpush.android.intent.NOTIFICATION_CLICK_ACTION广播  
可以不重写此方法，或者重写此方法且调用super.onMultiActionClicked  
如果重写此方法，没有调用super，则不会发送广播到旧版本Receiver  


#### 方法定义

	 public void onMultiActionClicked(Context context,Intent intent)

#### 参数定义

+ context
	+ 应用的 Application Context。
+ intent
	+ 点击后触发的Intent	
	
***说明*** 注意这个方法里面禁止再调super.onMultiActionClicked,因为会导致逻辑混乱


## 老别名 alias 与标签 tag 接口
1.5.0 ～ 3.0.6 版本提供的别名与标签接口都是覆盖的逻辑，从 3.0.7 版本开始不再维护（但仍会继续保留）。建议开发者使用 3.0.7 开始提供的新 tag、alias 接口。


### Method - setAliasAndTags (with Callback)

调用此 API 来同时设置别名与标签。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

#### 支持的版本

开始支持的版本：1.5.0

#### 接口定义

	
	public static void setAliasAndTags(Context context, 
	                                   String alias, 
	                                   Set<String> tags, 
	                                   TagAliasCallback callback);

#### 参数定义

+ alias

	+ null 此次调用不设置此值。（注：不是指的字符串 "null" ）
	+ ""（空字符串）表示取消之前的设置。
	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.6 支持）@!#$&*+=.|。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）

+ tags

	+ null 此次调用不设置此值。（注：不是指的字符串 "null" ）
    + 空数组或列表表示取消之前的设置。
	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.6 支持）@!#$&*+=.|。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，且单次操作总长度不得超过 7000 字节。（判断长度需采用 UTF-8 编码）

+ callback

	+ 在 TagAliasCallback 的 gotResult 方法，返回对应的参数 alias、tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。

### Method - setAlias

调用此 API 来设置别名。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

#### 支持的版本

开始支持的版本：1.5.0

#### 接口定义

	public static void setAlias(Context context, String alias, TagAliasCallback callback)

参数定义

+ alias

	+ ""（空字符串）表示取消之前的设置。
	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.6 支持）@!#$&*+=.|。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）
	
+ callback

	+ 在TagAliasCallback 的 gotResult 方法，返回对应的参数 alias、tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。
	
	
### Method - setTags

调用此 API 来设置标签。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>使用建议
 <br>
 <p>如果待设置的 alias / tags 是动态的，有可能在调用 setAliasAndTags 时因为 alias / tags 无效而整调用失败。
 <br>
 <p>调用此方法只设置 tags，可以排除可能无效的 alias 对本次调用的影响。
</div>

#### 支持的版本

开始支持的版本：1.5.0

#### 接口定义

	public static void setTags(Context context, Set<String> tags, TagAliasCallback callback)

#### 参数定义

+ tags

	+ 空数组或列表表示取消之前的设置。
	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.6 支持）@!#$&*+=.|。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，且单次操作总长度不得超过 7000 字节。（判断长度需采用 UTF-8 编码）
		+ 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。
		
+ callback

	+ 在 TagAliasCallback 的 gotResult 方法，返回对应的参数 alias, tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。 


### Class - TagAliasCallback

设置别名与标签方法的回调类，可在 gotResult 方法上得到回调的结果。回调 responseCode = 0，则确认设置成功。

#### 支持的版本

开始支持的版本：1.5.0

#### 接口定义

	public void gotResult(int responseCode, String alias, Set<String> tags);

#### 参数定义

+ responseCode
	+ 0 表示调用成功。
	+ 其他返回码请参考错误码定义。
+ alias
	+ 原设置的别名
+ tags
	+ 原设置的标签

### 错误码定义
请跳转至[错误码定义列表](#client_error_code)

### 相关文档

+ [Android SDK 标签与别名 API](../../client/Android/android_api/#api_3)
+ [iOS SDK 标签与别名 API](../../client/iOS/ios_api/#api-ios)

## 获取 RegistrationID API
### 支持的版本

开始支持的版本：1.6.0 

### 功能说明


#### RegistrationID 定义

集成了 JPush SDK 的应用程序在第一次成功注册到 JPush 服务器时，JPush 服务器会给客户端返回一个唯一的该设备的标识 - RegistrationID。JPush SDK 会以广播的形式发送 RegistrationID 到应用程序。

应用程序可以把此 RegistrationID 保存以自己的应用服务器上，然后就可以根据 RegistrationID 来向设备推送消息或者通知。



### API - getRegistrationID

调用此 API 来取得应用程序对应的 RegistrationID。 __只有当应用程序成功注册到 JPush 的服务器时才返回对应的值，否则返回空字符串。__

#### 支持的版本

开始支持的版本：1.6.0

#### 接口定义

	SDK 初次注册成功后，开发者通过在自定义的 Receiver 里监听 Action - cn.jpush.android.intent.REGISTRATION 来获取对应的 RegistrationID。
	注册成功后，也可以通过函数 public static String getRegistrationID(Context context) 获取
	


### 附加说明

#### 通过 RegistrationID 进行点对点推送

可以通过 RegistrationID 来推送消息和通知，参考文档 Push API v3，[设置 Audience ](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#audience)为 RegistrationID 时即可根据 RegistrationID 推送。

注：要使用此功能，客户端 App 一定要集成有 1.6.0 及以上版本的 JPush Android SDK。

## 统计分析 API

#### 支持的版本

开始支持的版本：1.6.0


#### 功能说明

本 API 用于“用户使用时长”，“活跃用户”，“用户打开次数”的统计，并上报到服务器，在 Portal 上展示给开发者。



#### API - onResume / onPause

##### 接口定义

	public static void onResume(final Activity activity)
	public static void onPause(final Activity activity)

##### 参数说明
		
+ Activity activity 当前所在的 Activity。

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

+ 用于上报用户的通知栏被打开，或者用于上报用户自定义消息被展示等客户端需要统计的事件。

##### 接口定义

	public static void reportNotificationOpened(Context context, String msgId)

参数说明

+ context：应用的 ApplicationContext
+ msgId：推送每一条消息和通知对应的唯一 ID。（ msgId 来源于发送消息和通知的 Extra 字段 JPushInterface.EXTRA_MSG_ID，参考 接收推送消息 Receiver ）

##### 代码示例	

	   JPushInterface.reportNotificationOpened(context,bundle.getString(JPushInterface.EXTRA_MSG_ID));
	        

## 清除通知 API

#### 支持的版本

开始支持的版本：1.3.5

#### 功能说明

推送通知到客户端时，由 JPush SDK 展现通知到通知栏上。

此 API 提供清除通知的功能，包括：清除所有 JPush 展现的通知（不包括非 JPush SDK 展现的）；清除指定某个通知。

#### API - clearAllNotifications

##### 接口定义

	public static void clearAllNotifications(Context context);

##### 参数说明

+ Context context： 应用的 ApplicationContext

	
#### API - clearNotificationById

##### 接口定义
	public static void clearNotificationById(Context context, int notificationId);

##### 参数说明

	+ Context context：应用的 ApplicationContext
	+ int notificationId：通知 ID

```
此 notificationId 来源于 intent 参数 JPushInterface.EXTRA_NOTIFICATION_ID，可参考文档：接收推送消息 Receiver
```

## 设置允许推送时间 API

#### 支持的版本

开始的版本：最初

#### 功能说明

默认情况下用户在任何时间都允许推送。即任何时候有推送下来，客户端都会收到，并展示。

开发者可以调用此 API 来设置允许推送的时间。

如果不在该时间段内收到消息，SDK 的处理是：**推送到的通知会被扔掉。**

```
 这是一个纯粹客户端的实现，所以与客户端时间是否准确、时区等这些，都没有关系。
 而且该接口仅对通知有效，自定义消息不受影响。
```

#### API - setPushTime

##### 接口定义

	public static void setPushTime(Context context, Set<Integer> weekDays, int startHour, int endHour)

##### 参数说明

+ Context context 应用的 ApplicationContext
+ Set<Integer> days  0 表示星期天，1 表示星期一，以此类推。 （ 7 天制，Set 集合里面的 int 范围为 0 到 6 ）
	+ set 的值为 null，则任何时间都可以收到通知，set 的 size 为 0，则表示任何时间都收不到通知。
+ int startHour 允许推送的开始时间 （ 24 小时制：startHour 的范围为 0 到 23 ）
+ int endHour 允许推送的结束时间 （ 24 小时制：endHour 的范围为 0 到 23 ）

##### 代码示例

	Set<Integer> days = new HashSet<Integer>();
	days.add(1);
	days.add(2);
	days.add(3);
	days.add(4);
	days.add(5);
	JPushInterface.setPushTime(getApplicationContext(), days, 10, 23);

此代码表示周一到周五、上午 10 点到晚上 23 点，都可以推送。

## 设置通知静默时间 API
### 支持的版本

开始支持的版本：1.4.0

### 功能说明

默认情况下用户在收到推送通知时，客户端可能会有震动，响铃等提示。但用户在睡觉、开会等时间点希望为“免打扰”模式，也是静音时段的概念。

开发者可以调用此 API 来设置静音时段。如果在该时间段内收到消息，则：不会有铃声和震动。


### API - setSilenceTime

#### 接口定义

	public static void setSilenceTime(Context context, int startHour, int startMinute, int endHour, int endMinute)
	
#### 参数说明
	
+ Context context 应用的ApplicationContext
+ int startHour 静音时段的开始时间 - 小时 （ 24 小时制，范围：0~23 ）
+ int startMinute 静音时段的开始时间 - 分钟（范围：0~59 ）
+ int endHour 静音时段的结束时间 - 小时 （ 24 小时制，范围：0~23 ）
+ int endMinute 静音时段的结束时间 - 分钟（范围：0~59 ）

#### 代码示例
	
	JPushInterface.setSilenceTime(getApplicationContext(), 22, 30, 8, 30);

此代码表示晚上 10：30 点到第二天早上 8：30 点为静音时段。

## 申请权限接口（ Android 6.0 及以上）
### 支持的版本
开始支持的版本：2.1.0

### 功能说明
在 Android 6.0 及以上的系统上，需要去请求一些用到的权限，JPush SDK 用到的一些需要请求如下权限，因为需要这些权限使统计更加精准，功能更加丰富，建议开发者调用。


	"android.permission.READ_PHONE_STATE"
	"android.permission.WRITE_EXTERNAL_STORAGE"
	"android.permission.READ_EXTERNAL_STORAGE"
	"android.permission.ACCESS_FINE_LOCATION"



### API - requestPermission

#### 接口定义
	public static void requestPermission(Context context);
#### 参数说明
+ context 当前应用的 Activity 的上下文

## 设置是否开启省电模式
###支持的版本
开始支持的版本：3.0.9

### 功能说明
JPush SDK 开启和关闭省电模式，默认为关闭。

### API - setPowerSaveMode

#### 接口定义
	public static void setPowerSaveMode(Context context,boolean enable);
#### 参数说明
+ context 当前应用的 Activity 的上下文
+ enable 是否需要开启或关闭，true 为开启，false 为关闭


## 通知栏样式定制 API
### 支持的版本
开始支持的版本：最初


### 功能说明
大多数情况下，开发者不需要调用这里的定制通知栏 API 来自定义通知栏样式，只需要使用 SDK 默认的即可。

如果您想：

+ 改变 Notification 里的铃声、震动、显示与消失行为
+ 自定义通知栏显示样式
+ 不同的 Push 通知，Notification 样式不同

则请使用本通知栏定制 API 提供的能力。

### 教程与代码示例

请参考文档：[自定义通知栏样式教程](android_senior/#_8)

### API - 设置默认通知栏样式构建类
	public static void setDefaultPushNotificationBuilder(DefaultPushNotificationBuilder builder)

当用户需要定制默认的通知栏样式时，则可调用此方法。

极光 Push SDK 提供了 3 个用于定制通知栏样式的构建类：

+ BasicPushNotificationBuilder
	+ Basic 用于定制 Android Notification 里的 defaults / flags / icon 等基础样式（行为）
+ CustomPushNotificationBuilder
	+ 继承 Basic 进一步让开发者定制 Notification Layout
+ MultiActionsNotificationBuilder
	+ 继承 DefaultPushNotificationBuilder 进一步让开发者定制 Notification Layout
	
	
如果不调用此方法定制，则极光 Push SDK 默认的通知栏样式是：Android 标准的通知栏提示。



### API - 设置某编号的通知栏样式构建类


public static void setPushNotificationBuilder(Integer notificationBuilderId, BasicPushNotificationBuilder builder)

当开发者需要为不同的通知，指定不同的通知栏样式（行为）时，则需要调用此方法设置多个通知栏构建类。

3.0.0 版本新增 MultiActionsNotificationBuilder，即带按钮的通知栏构建类，可通过该 api 设置。

设置时，开发者自己维护 notificationBuilderId 这个编号，下发通知时使用[ builder_id ](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#notification)指定该编号，从而 Push SDK 会调用开发者应用程序里设置过的指定编号的通知栏构建类，来定制通知栏样式。


## 设置保留最近通知条数 API


### 支持的版本
开始支持的版本：1.3.0


### 功能说明
通过极光推送，推送了很多通知到客户端时，如果用户不去处理，就会有很多保留在那里。

从 v 1.3.0 版本开始 SDK 增加此功能，限制保留的通知条数。默认为保留最近 5 条通知。

开发者可通过调用此 API 来定义为不同的数量。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
 <p>仅对通知有效。所谓保留最近的，意思是，如果有新的通知到达，之前列表里最老的那条会被移除。
 <br>
 <p>例如，设置为保留最近 5 条通知。假设已经有 5 条显示在通知栏，当第 6 条到达时，第 1 条将会被移除。
</div>

### API - setLatestNotificationNumber

#### 接口定义

	public static void setLatestNotificationNumber(Context context, int maxNum)

#### 参数说明
+ context 应用的 ApplicationContext
+ maxNum 最多显示的条数

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用。可以调用多次。SDK 使用最后调用的数值。

#### 代码示例

```
JPushInterface.init(context);
JPushInterface.setLatestNotificationNumber(context, 3);
```	


## 自定义 Receiver 接收被拉起回调

自定义一个Receiver组件，继承cn.jpush.android.service.WakedResultReceiver类,复写onWake(int wakeType)或onWake(Context context, int wakeType)方法(注：开发者二选一复写)以监听被拉起,直接在AndroidManifest配置即可。
详细配置参考 AndroidManifest 示例。
### onWake 方法参数说明
+ 应用被拉起时回调 onWake(int wakeType) 方法，wakeType 是拉起的类型，其取值对应的拉起方式如下：

wakeType值 | 拉起方式
---|---
1|START_SERVICE
2|BIND_SERVICE
4|CONTENTPROVIDER

+ 应用被拉起时回调 onWake(Context context, int wakeType) 方法，context 是上下文，wakeType 是拉起的类型，其取值对应的拉起方式如下：

wakeType值 | 拉起方式
---|---
1|START_SERVICE
2|BIND_SERVICE
4|CONTENTPROVIDER



<a name="client_error_code"></a>
## 客户端错误码定义


<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th >描述</th>
			<th>详细解释</th>
		</tr>
		<tr >
			<td>6001</td>
			<td>无效的设置</td>
			<td>3.0.7 以前的旧接口设置 tag/alias 不应参数都为 null，3.0.7 开始的新 tag/alias 接口报此错误码表示 tag/alias 参数不能为空</td>
		</tr>
		<tr >
			<td>6002</td>
			<td>设置超时</td>
			<td>建议重试，一般出现在网络不佳、初始化尚未完成时。</td>
		</tr>
		<tr >
			<td>6003</td>
			<td>alias 字符串不合法</td>
			<td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符( 2.1.6 支持)@!#$&*+=.|</td>
		</tr>
		<tr >
			<td>6004</td>
			<td>alias 超长。最多 40 个字节</td>
			<td>中文 UTF-8 是 3 个字节</td>
		</tr>
		<tr >
			<td>6005</td>
			<td>某一个 tag 字符串不合法</td>
			<td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符( 2.1.6 支持)@!#$&*+=.|</td>
		</tr>
		<tr >
			<td>6006</td>
			<td>某一个 tag 超长。一个 tag 最多 40个字节</td>
			<td>中文 UTF-8 是 3 个字节</td>
		</tr>
		<tr >
			<td>6007</td>
			<td>tags 数量超出限制。最多 1000 个</td>
			<td>这是一台设备的限制。一个应用全局的标签数量无限制。</td>
		</tr>
		<tr >
			<td>6008</td>
			<td>tag 超出总长度限制</td>
			<td>3.0.7 版本中新增 tag/alias 接口最长度最多 5000 字节，tag/alias 老接口总长度最多 7000 字节</td>
		</tr>
		<tr >
			<td>6009</td>
			<td>未知错误</td>
			<td>由于权限问题，导致的 PushService 启动异常，客户端日志中将有详细的报错信息，可据此排查。</td>
		</tr>
		<tr >
			<td>6011</td>
			<td>短时间内操作过于频繁</td>
			<td>10s 内设置 tag 或 alias 大于 10 次，或 10s 内设置手机号码大于 3 次</td>
		</tr>
		<tr >
			<td>6012</td>
			<td>在 JPush 服务 stop 状态下设置了 tag 或 alias 或手机号码</td>
			<td>3.0.0 版本新增的错误码，调了 stopPush 必须调用 resumePush 恢复服务后方可调用其他的 API，开发者可根据这个错误码的信息做相关处理或者提示。</td>
		</tr>
		<tr >
			<td>6013</td>
			<td>用户设备时间轴异常</td>
			<td>3.0.6 版本新增的错误码。设备本地时间轴异常变化影响了设置频率。</td>
		</tr>
        <tr >
			<td>6014</td>
			<td>服务器繁忙,建议重试</td>
			<td>3.0.7 版本新增的错误码</td>
		</tr>
        <tr >
			<td>6015</td>
			<td>appkey 在黑名单中</td>
			<td>3.0.7 版本新增，该 appkey 在黑名单中，请联系 support 解除</td>
		</tr>
        <tr >
			<td>6016</td>
			<td>无效用户</td>
			<td>3.0.7 版本新增的错误码</td>
		</tr>
        <tr >
			<td>6017</td>
			<td>无效请求</td>
			<td>3.0.7 版本新增的错误码</td>
		</tr>
        <tr >
			<td>6018</td>
			<td>Tags 过多</td>
			<td>3.0.7 版本新增，该设备设置的 tag 数超过 1000 个，建议先清除部分 tag</td>
		</tr>
        <tr >
			<td>6019</td>
			<td>查询请求已过期</td>
			<td>3.0.7 版本新增的错误码</td>
		</tr>
        <tr >
			<td>6020</td>
			<td>tag/alias 操作暂停</td>
			<td>3.0.7 版本新增的错误码，建议过一段时间再设置</td>
		</tr>
        <tr >
			<td>6021</td>
			<td>tags 操作正在进行中，暂时不能进行其他 tags 操作</td>
			<td>3.0.7 版本新增的错误码，多次调用 tag 相关的 API，请在获取到上一次调用回调后再做下一次操作；在未取到回调的情况下，等待 20 秒后再做下一次操作。</td>
		</tr>
        <tr >
			<td>6022</td>
			<td>alias 操作正在进行中，暂时不能进行其他 alias 操作</td>
			<td>3.0.7 版本新增的错误码，多次调用 alias 相关的 API，请在获取到上一次调用回调后再做下一次操作；在未取到回调的情况下，等待 20 秒后再做下一次操作。</td>
		</tr>
		 <tr >
			<td>6023</td>
			<td>手机号码不合法</td>
			<td>3.1.1 版本新增的错误码；只能以 “+” 或者 数字开头；后面的内容只能包含 “-” 和 数字。</td>
		</tr>
		 <tr >
			<td>6024</td>
			<td>服务器内部错误</td>
			<td>3.1.1 版本新增的错误码；服务器内部错误，过一段时间再重试。</td>
		</tr>
		 <tr >
			<td>6025</td>
			<td>手机号码太长</td>
			<td>3.1.1 版本新增的错误码；手机号码过长，目前极光检测手机号码的最大长度为 20。</td>
		</tr>
		 <tr >
			<td>6026</td>
			<td>数据包体过大</td>
			<td>3.1.5 版本新增的错误码；数据包体过大，目前极光支持的数据通信包体最大为 8128。</td>
		</tr>
		<tr >
			<td>-997</td>
			<td>注册失败/登录失败</td>
			<td>（一般是由于没有网络造成的）如果确保设备网络正常，还是一直遇到此问题，则还有另外一个原因：JPush 服务器端拒绝注册。而这个的原因一般是：你当前 App 的 Android 包名以及 AppKey，与你在 Portal 上注册的应用的 Android 包名与 AppKey 不相同。</td>
		</tr>
		<tr >
			<td>1005</td>
			<td>包名和 AppKey 不匹配</td>
			<td>请检查客户端配置的包名与官网对应 Appkey 应用下配置的包名是否一致</td>
		</tr>
		<tr >
			<td>1008</td>
			<td>AppKey 非法</td>
			<td>请到官网检查此应用信息中的 appkey，确认无误</td>
		</tr>
		<tr >
			<td>1009</td>
			<td>当前的 appkey 下没有创建 Android 应用；你所使用的 SDK 版本低于 1.8.2。</td>
			<td>请到官网检查此应用的应用详情；更新应用中集成的极光 SDK 至最新。</td>
		</tr>
		<tr >
			<td>-996</td>
			<td>网络连接断开</td>
			<td>如果确保设备网络正常，可能是由于包名不正确，服务器强制断开客户端的连接。</td>
		</tr>
		<tr >
			<td>-994</td>
			<td>网络连接超时</td>
			<td></td>
		</tr>
	</table>
</div>


## CrashLog 收集并上报
### 支持的版本

+ 2.1.8 及以后版本，默认为开启状态，并增加 stopCrashHandler 接口。

### 功能说明
SDK 通过 Thread.UncaughtExceptionHandler 捕获程序崩溃日志，并在程序奔溃时实时上报如果实时上报失败则会在程序下次启动时发送到服务器。如需要程序崩溃日志功能可调用此方法。

### API - stopCrashHandler（关闭 CrashLog 上报）

#### 接口定义
    public static void stopCrashHandler(Context context)

#### 参数说明
+ Context 应用的 Applicationcontext

### API - initCrashHandler（开启 CrashLog 上报）

#### 接口定义
	public static void initCrashHandler(Context context);
#### 参数说明
+ Context 应用的 Applicationcontext


## 获取推送连接状态
### 支持的版本

开始支持的版本：1.6.3

### 功能说明
开发者可以使用此功能获取当前 Push 服务的连接状态

当连接状态发生变化时（连接，断开），会发出一个广播，开发者可以在自定义的 Receiver 监听 cn.jpush.android.intent.CONNECTION 获取变化的状态，也可通过 API 主动获取。

### API getConnectionState

#### 功能说明
获取当前连接状态

#### 接口定义

```
public static boolean getConnectionState(Context context);
```

#### 参数说明
+ context 应用的 ApplicationContext

#### ACTION  cn.jpush.android.intent.CONNECTION

##### intent 参数
JPushInterface.EXTRA_CONNECTION_CHANGE
Push 连接状态变化广播传过来的值
```
boolean connected = bundle.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
```

##### 示例代码
在 JPush Demo 的 MyReceiver onReceive 方法添加下面代码：
```
else if(JPushInterface.ACTION_CONNECTION_CHANGE.equals(intent.getAction())) {
            boolean connected = intent.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
            Log.e(TAG, "[MyReceiver]" + intent.getAction() +" connected:"+connected);
        }
```

## 本地通知 API
### 支持的版本
开始支持的版本：1.6.4

### 功能说明
通过极光推送的 SDK，开发者只需要简单调用几个接口，便可以在应用中定时发送本地通知

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>本地通知 API 不依赖于网络，无网条件下依旧可以触发
<br>
<p>本地通知与网络推送的通知是相互独立的，不受保留最近通知条数上限的限制
<br>
<p>本地通知的定时时间是自发送时算起的，不受中间关机等操作的影响
</div>

### API  addLocalNotification 添加一个本地通知

#### 接口定义
```
public static void addLocalNotification(Context context, JPushLocalNotification notification)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ notification 是本地通知对象；建议notificationId设置为正整数，为0或者负数时会导致本地通知无法清除。

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

### API  removeLocalNotification 移除指定的本地通知
#### 接口定义
```
public static void removeLocalNotification(Context context, long notificationId)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ notificationId 是要移除的本地通知的 ID，注意notificationId为0或者负数的通知无法移除

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

### API  clearLocalNotifications 移除所有的本地通知，注意notificationId为0或者负数时通知无法移除

#### 接口定义
```
public static void clearLocalNotifications(Context context)
```
#### 参数说明
+ context 是应用的 ApplicationContext

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

### 本地通知相关设置
```
//设置本地通知样式
 
public void setBuilderId(long)
 
//设置本地通知的 title
 
public void setTitle(String paramString)
 
//设置本地通知的 content
 
public void setContent(String paramString)
 
//设置额外的数据信息 extras 为 json 字符串
 
public void setExtras(String extras)
 
//设置本地通知的 ID
 
public void setNotificationId(long notificationId)
 
//设置本地通知触发时间
 
public void setBroadcastTime(long broadCastTime)
 
public void setBroadcastTime(Date date)
 
public void setBroadcastTime(int year, int month, int day, int hour, int minute, int second)
```
### 示例代码
```
JPushLocalNotification ln = new JPushLocalNotification();
ln.setBuilderId(0);
ln.setContent("hhh");
ln.setTitle("ln");
ln.setNotificationId(11111111) ;
ln.setBroadcastTime(System.currentTimeMillis() + 1000 * 60 * 10);
 
Map<String , Object> map = new HashMap<String, Object>() ;
map.put("name", "jpush") ;
map.put("test", "111") ;
JSONObject json = new JSONObject(map) ;
ln.setExtras(json.toString()) ;
JPushInterface.addLocalNotification(getApplicationContext(), ln);
```

## NotificationChannel配置
### 支持的版本
开始支持的版本：3.3.4
### 功能说明：
Android8.0以后通知都走NotificationChannel了。开发者可以自行定义NotificationChannel，然后在API推送的时候可以指定channelId推送；
在Android8.0及以上的机型，通知会先查找对应channelId的channel，通知的重要等级、声音、震动、呼吸灯由channel决定；
如果没有找到channelId，或者处于静默时间内，则走默认的极光channel。

自定义NotificationChannel示例
```
    private void initChannel(){
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationManager nm = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
            if (nm != null){
                NotificationChannelGroup notificationChannelGroup = new NotificationChannelGroup("MyGroupId", "自定义通知组");
                nm.createNotificationChannelGroup(notificationChannelGroup);

                NotificationChannel notificationChannel = new NotificationChannel("MyChannelId", "自定义通知", NotificationManager.IMPORTANCE_HIGH);
                notificationChannel.setGroup("MyGroupId");
                notificationChannel.enableLights(true);
                notificationChannel.enableVibration(true);
                nm.createNotificationChannel(notificationChannel);
            }
        }
    }
```

##地理围栏 API
### 支持的版本
开始支持的版本：3.1.8

### 功能说明
JPush SDK 提供地理围栏功能，当设备进入或离开相应的地理区域才触发通知或自定义消息。开发者可以通过此功能对SDK提供的地理围栏功能进行设置。

### API  setGeofenceInterval 

#### 功能说明
设置地理围栏监控周期，最小3分钟，最大1天。默认为15分钟，当距离地理围栏边界小于1000米周期自动调整为3分钟。设置成功后一直使用设置周期，不会进行调整。

#### 接口定义
```
 public static void setGeofenceInterval(Context context, long interval)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ interval 监控周期，单位是毫秒。


### API  setMaxGeofenceNumber 
#### 功能说明
设置最多允许保存的地理围栏数量，超过最大限制后，如果继续创建先删除最早创建的地理围栏。默认数量为10个，允许设置最小1个，最大100个。

#### 接口定义
```
public static void setMaxGeofenceNumber(Context context, int maxNumber)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ maxNumber 最多允许保存的地理围栏个数

### API  deleteGeofence 
#### 功能说明
删除指定id的地理围栏

#### 接口定义
```
public static void deleteGeofence(Context context, String geofenceid)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ geofenceid 地理围栏的id
