# Android API

## 停止与恢复推送服务 API

### 支持的版本

开始的版本：v1.3.3

### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者App可以通过调用停止推送服务API来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。
 <p>如果停止推送服务后，开发者App被卸载重新安装，JPush SDK 会恢复正常的默认行为。
 <p>而清理应用数据的情况，还是必须要调用恢复服务接口才能恢复。
<br> 
 <p>本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息，
 <p>恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。
</div>

### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

+ JPush Service 不在后台运行
+ 收不到推送消息
+ 极光推送所有的其他 API 调用都无效,不能通过 JPushInterface.init 恢复，需要调用resumePush恢复。

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

###参数说明

+ context 应用的 ApplicationContext

###代码示例
	
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
	
## 接收推送消息Receiver
	
### 支持的版本

开始的版本：最初。

### 功能说明

JPush SDK 收到推送，通过广播的方式，转发给开发者App，这样开发者就可以灵活地进行处理。

这个动作不是必须的。用户有需要才定义 Receiver 类来处理 SDK过来的广播。

如果不做这个动作，即不写自定义 Receiver，也不在 AndroidManifest.xml 里配置这个 Receiver，则默认的行为是：

+ 接收到推送的自定义消息，则没有被处理
+ 可以正常收到通知，用户点击打开应用主界面

### 接受广播

如果全部类型的广播都接收，则需要在 AndroidManifest.xml 里添加如下的配置信息：

	<receiver
	    android:name="Your Receiver"
	    android:enabled="true">
	    <intent-filter>
	        <action android:name="cn.jpush.android.intent.REGISTRATION" />
	        <action android:name="cn.jpush.android.intent.MESSAGE_RECEIVED" />
	        <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED" />
	        <action android:name="cn.jpush.android.intent.NOTIFICATION_OPENED" />
	        <category android:name="You package Name" />
	    </intent-filter>
	</receiver>
	
每个 Receiver action 详细解释如下。

#### Action - cn.jpush.android.intent.REGISTRATION

SDK 向 JPush Server 注册所得到的注册 ID 。

一般来说，可不处理此广播信息。

要深入地集成极光推送，开发者想要自己保存App用户与JPush 用户关系时，则接受此广播，取得 Registration ID 并保存与App uid 的关系到开发者自己的应用服务器上。

使用极光推送提供的别名与标签功能，是更加简单轻便的绑定App用户与JPush用户的方式，请参考文档：[别名与标签使用教程。]()

##### Intent 参数

+ JPushInterface.EXTRA_REGISTRATION_ID
	+ SDK 向 JPush Server 注册所得到的注册 全局唯一的 ID ，可以通过此 ID 向对应的客户端发送消息和通知。
	


			Bundle bundle = intent.getExtras();
			String title = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);

#### Action - cn.jpush.android.intent.MESSAGE_RECEIVED
	
收到了自定义消息 Push 。

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
	+ 对应 Portal 推送消息界面上的"自定义消息内容”字段。
	
			Bundle bundle = intent.getExtras();
			String message = bundle.getString(JPushInterface.EXTRA_MESSAGE);

+ JPushInterface.EXTRA_EXTRA
	+ 保存服务器推送下来的附加字段。这是个 JSON 字符串。
	+ 对应 API 消息内容的 extras 字段。
	+ 对应 Portal 推送消息界面上的“可选设置”里的附加字段。
	
			Bundle bundle = intent.getExtras();
			String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);
			
			
+ JPushInterface.EXTRA_CONTENT_TYPE
	+ 保存服务器推送下来的内容类型。
	+ 对应 API 消息内容的 content_type 字段。	

			Bundle bundle = intent.getExtras();
			String type = bundle.getString(JPushInterface.EXTRA_CONTENT_TYPE);

+ JPushInterface.EXTRA_RICHPUSH_FILE_PATH
	+ SDK 1.4.0 以上版本支持。
	+ 富媒体通消息推送下载后的文件路径和文件名。
	
			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_RICHPUSH_FILE_PATH);
			
+ JPushInterface.EXTRA_MSG_ID
	+ SDK 1.6.1 以上版本支持。
	+ 唯一标识消息的 ID, 可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);
			
#### Action - cn.jpush.android.intent.NOTIFICATION_RECEIVED

收到了通知 Push。

```
 如果通知的内容为空，则在通知栏上不会展示通知。
 但是，这个广播 Intent 还是会有。开发者可以取到通知内容外的其他信息。
```
##### Intent 参数

+ JPushInterface.EXTRA_NOTIFICATION_TITLE
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
			

+ JPushInterface.EXTRA_NOTIFICATION_ID
	+ SDK 1.3.5 以上版本支持。
	+ 通知栏的Notification ID，可以用于清除Notification
	+ 如果服务端内容（alert）字段为空，则notification id 为0

			Bundle bundle = intent.getExtras();
			int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);
			
+ JPushInterface.EXTRA_CONTENT_TYPE
	+ 保存服务器推送下来的内容类型。
	+ 对应 API 消息内容的 content_type 字段。 
	+ Portal 上暂时未提供输入字段。

			Bundle bundle = intent.getExtras();
			String type = bundle.getString(JPushInterface.EXTRA_CONTENT_TYPE);
			
						
+ JPushInterface.EXTRA_RICHPUSH_HTML_PATH
	+ SDK 1.4.0 以上版本支持。
	+ 富媒体通知推送下载的HTML的文件路径,用于展现WebView。

			Bundle bundle = intent.getExtras();
			String fileHtml = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_PATH);
			
+ JPushInterface.EXTRA_RICHPUSH_HTML_RES
	+ SDK 1.4.0 以上版本支持。
	+ 富媒体通知推送下载的图片资源的文件名,多个文件名用 “，” 分开。 与 “JPushInterface.EXTRA_RICHPUSH_HTML_PATH” 位于同一个路径。

			Bundle bundle = intent.getExtras();
			String fileStr = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_RES);
			String[] fileNames = fileStr.split(",");
			
+ JPushInterface.EXTRA_MSG_ID
	+ SDK 1.6.1 以上版本支持。  
	+ 唯一标识通知消息的 ID, 可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);
			
#### Action - cn.jpush.android.intent.NOTIFICATION_OPENED
			
用户点击了通知。

一般情况下，用户不需要配置此 receiver action。

如果开发者在 AndroidManifest.xml 里未配置此 receiver action，那么，SDK 会默认打开应用程序的主 Activity，相当于用户点击桌面图标的效果。

如果开发者在 AndroidManifest.xml 里配置了此 receiver action，那么，当用户点击通知时，SDK 不会做动作。开发者应该在自己写的 BroadcastReceiver 类里处理，比如打开某 Activity 。

##### Intent 参数

+ JPushInterface.EXTRA_NOTIFICATION_TITLE

	+ 保存服务器推送下来的通知的标题。
	+ 对应 API 通知内容的 title 字段。
	+ 对应 Portal 推送通知界面上的“通知标题”字段。

			Bundle bundle = intent.getExtras();
			String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
				
+ JPushInterface.EXTRA_ALERT

	+ 保存服务器推送下来的通知内容。
	+ 对应 API 通知内容的alert字段。
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
			
							
+ JPushInterface.EXTRA_NOTIFICATION_ID
	
	+ SDK 1.3.5 以上版本支持。
	+ 通知栏的Notification ID，可以用于清除Notification
	
			Bundle bundle = intent.getExtras();
			int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID
			  
+ JPushInterface.EXTRA_MSG_ID
	+ SDK 1.6.1 以上版本支持。
	+ 唯一标识调整消息的 ID, 可用于上报统计等。

			Bundle bundle = intent.getExtras();
			String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);
			
			
### 代码示例

	public void onReceive(Context context, Intent intent) {
	        Bundle bundle = intent.getExtras();
	        Log.d(TAG, "onReceive - " + intent.getAction());

	        if (JPushInterface.ACTION_REGISTRATION_ID.equals(intent.getAction())) {
	        }else if (JPushInterface.ACTION_MESSAGE_RECEIVED.equals(intent.getAction())) {
	            System.out.println("收到了自定义消息。消息内容是：" + bundle.getString(JPushInterface.EXTRA_MESSAGE));
	            // 自定义消息不会展示在通知栏，完全要开发者写代码去处理
	        } else if (JPushInterface.ACTION_NOTIFICATION_RECEIVED.equals(intent.getAction())) {
	            System.out.println("收到了通知");
	            // 在这里可以做些统计，或者做些其他工作
	        } else if (JPushInterface.ACTION_NOTIFICATION_OPENED.equals(intent.getAction())) {
	            System.out.println("用户点击打开了通知");
	            // 在这里可以自己写代码去定义用户点击后的行为
	            Intent i = new Intent(context, TestActivity.class);  //自定义打开的界面
	            i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
	            context.startActivity(i);
	        } else {
	            Log.d(TAG, "Unhandled intent - " + intent.getAction());
	  }
	}

## 别名与标签 API	

### 功能说明

```
温馨提示，设置标签别名请注意处理call back结果。只有call back 返回值为 0 才设置成功，
才可以向目标推送。否则服务器 API 会返回1011错误。
```	

#### 别名 alias

为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。

每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，[服务器端API](../../server/push/rest_api_v3_push)会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用[服务器端API](../../server/push/rest_api_v3_push)发通知到客户端提醒用户。

#### 标签 tag

为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page,  women

### Method - setAliasAndTags (with Callback)

调用此 API 来同时设置别名与标签。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

#### 支持的版本

开始支持的版本：1.5.0.

#### 接口定义

	
	public static void setAliasAndTags(Context context, 
	                                   String alias, 
	                                   Set<String> tags, 
	                                   TagAliasCallback callback)

#### 参数定义

+ alias

	+ null 此次调用不设置此值。（注：不是指的字符串"null"）
	+ "" （空字符串）表示取消之前的设置。
	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）

+ tags

	+ null 此次调用不设置此值。（注：不是指的字符串"null"）
    + 空数组或列表表示取消之前的设置。
	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）

+ callback

	+ 在 TagAliasCallback 的 gotResult 方法，返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。

### Method - setAlias

调用此 API 来设置别名。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

#### 支持的版本

开始支持的版本：1.5.0.

#### 接口定义

	public static void setAlias(Context context, String alias, TagAliasCallback callback)

参数定义

+ alias

	+ "" （空字符串）表示取消之前的设置。
	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）
	
+ callback

	+ 在TagAliasCallback 的 gotResult 方法，返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。
	
	
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

开始支持的版本：1.5.0.

#### 接口定义

	public static void setTags(Context context, Set<String> tags, TagAliasCallback callback)

#### 参数定义

+ tags

	+ 空数组或列表表示取消之前的设置。
	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）
		+ 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。
		
+ callback

	+ 在 TagAliasCallback 的 gotResult 方法，返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。 




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

1.5.0

#### 接口的定义

	public static Set<String> filterValidTags(Set<String> tags)
	
#### 接口返回

有效的 tag 集合。

### Class - TagAliasCallback

设置别名与标签方法的回调类，可在 gotResult 方法上得到回调的结果。回调 responseCode = 0，则确认设置成功。

####  支持的版本

1.5.0

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

###  相关文档

+ Android[别名与标签使用教程](/client/android_api/#api_1)
+ [标签与别名 API (iOS)](/client/ios_api/#api-ios)

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

+ 用于上报用户的通知栏被打开，或者用于上报用户自定义消息被展示等客户端需要统计的事件。

##### 接口定义

	public static void reportNotificationOpened(Context context, String msgId)

参数说明

+ context：应用的 ApplicationContext
+ msgId：推送每一条消息和通知对应的唯一 ID。（msgId 来源于发送消息和通知的 Extra 字段 JPushInterface.EXTRA_MSG_ID，参考 接收推送消息Receiver）

##### 代码示例	

	   JPushInterface.reportNotificationOpened(context,bundle.getString(JPushInterface.EXTRA_MSG_ID));
	        

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

```
 此 notificationId 来源于intent参数 JPushInterface.EXTRA_NOTIFICATION_ID，可参考文档 接收推送消息Receiver
```

## 设置允许推送时间 API

#### 支持的版本

开始的版本：最初。

#### 功能说明

默认情况下用户在任何时间都允许推送。即任何时候有推送下来，客户端都会收到，并展示。

开发者可以调用此 API 来设置允许推送的时间。

如果不在该时间段内收到消息，当前的行为是：推送到的通知会被扔掉。

```
 这是一个纯粹客户端的实现。
 所以与客户端时间是否准确、时区等这些，都没有关系。
```

#### API - setPushTime

##### 接口定义

	public static void setPushTime(Context context, Set<Integer> weekDays, int startHour, int endHour)

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

## 申请权限接口（Android 6.0 及以上）
###支持的版本
开始的版本：v2.1.0

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

### 教程与代码示例

请参考文档：[自定义通知栏样式教程](/client/android_tutorials/#_11)

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


## 设置保留最近通知条数 API


### 支持的版本
开始的版本：v1.3.0


### 功能说明
通过极光推送，推送了很多通知到客户端时，如果用户不去处理，就会有很多保留在那里。

新版本 SDK (v1.3.0) 增加此功能，限制保留的通知条数。默认为保留最近 5 条通知。

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
本接口可以在 JPushInterface.init 之后任何地方调用。可以调用多次。SDK使用最后调用的数值。

#### 代码示例

```
JPushInterface.init(context);
JPushInterface.setLatestNotificationNumber(context, 3);
```	

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
			<td>无效的设置，tag/alias 不应参数都为 null</td>
			<td></td>
		</tr>
		<tr >
			<td>6002</td>
			<td>设置超时</td>
			<td>建议重试</td>
		</tr>
		<tr >
			<td>6003</td>
			<td>alias 字符串不合法</td>
			<td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥</td>
		</tr>
		<tr >
			<td>6004</td>
			<td>alias超长。最多 40个字节</td>
			<td>中文 UTF-8 是 3 个字节</td>
		</tr>
		<tr >
			<td>6005</td>
			<td>某一个 tag 字符串不合法</td>
			<td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符(v2.1.6支持)@!#$&*+=.|￥</td>
		</tr>
		<tr >
			<td>6006</td>
			<td>某一个 tag 超长。一个 tag 最多 40个字节</td>
			<td>中文 UTF-8 是 3 个字节</td>
		</tr>
		<tr >
			<td>6007</td>
			<td>tags 数量超出限制。最多 1000个</td>
			<td>这是一台设备的限制。一个应用全局的标签数量无限制。</td>
		</tr>
		<tr >
			<td>6008</td>
			<td>tag 超出总长度限制</td>
			<td>总长度最多 7K 字节</td>
		</tr>
		<tr >
			<td>6009</td>
			<td>未知错误</td>
			<td>由于权限问题，导致的PushService启动异常。</td>
		</tr>
		<tr >
			<td>6011</td>
			<td>10s内设置tag或alias大于10次</td>
			<td>短时间内操作过于频繁</td>
		</tr>
		<tr >
			<td>-997</td>
			<td>注册失败</td>
			<td>（一般是由于没有网络造成的）如果确保设备网络正常，还是一直遇到此问题，则还有另外一个原因：JPush 服务器端拒绝注册。而这个的原因一般是：你当前的 App 的 Android 包名，以及 appKey ，与你在 Portal 上注册的应用的 Android 包名与 AppKey 不相同。</td>
		</tr>
		<tr >
			<td>1005</td>
			<td>包名和AppKey 不匹配</td>
			<td></td>
		</tr>
		<tr >
			<td>1008</td>
			<td>AppKey非法</td>
			<td>请到官网检查此应用详情中的appkey，确认无误</td>
		</tr>
		<tr >
			<td>1009</td>
			<td>当前的appkey下没有创建Android应用。</td>
			<td>请到官网检查此应用的应用详情</td>
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


## CrashLog收集并上报
###支持的版本

+ v2.1.8版本及以后版本，默认为开启状态，并增加 stopCrashHandler接口。

### 功能说明
SDK通过Thread.UncaughtExceptionHandler  捕获程序崩溃日志，并在程序奔溃时实时上报如果实时上报失败则会在程序下次启动时发送到服务器。 如需要程序崩溃日志功能可调用此方法。

### API - stopCrashHandler（关闭CrashLog上报）

#### 接口定义
    public static void stopCrashHandler(Context context)

#### 参数说明
+ Context 应用的 Applicationcontext

### API - initCrashHandler（开启CrashLog上报）

#### 接口定义
	public static void initCrashHandler(Context context);
#### 参数说明
+ Context 应用的 Applicationcontext


## 获取推送连接状态
### 支持的版本

开始的版本：1.6.3。

### 功能说明
开发者可以使用此功能获取当前Push服务的连接状态

当连接状态发生变化时（连接，断开），会发出一个广播，开发者可以在自定义的Receiver监听cn.jpush.android.intent.CONNECTION获取变化的状态，也可通过API主动获取。

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

##### intent参数
JPushInterface.EXTRA_CONNECTION_CHANGE
Push连接状态变化广播传过来的值
```
boolean connected = bundle.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
```

##### 示例代码
在JPush Demo 的MyReceiver onReceive方法添加下面代码：
```
else if(JPushInterface.ACTION_CONNECTION_CHANGE.equals(intent.getAction())) {
            boolean connected = intent.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
            Log.e(TAG, "[MyReceiver]" + intent.getAction() +" connected:"+connected);
        }
```

##本地通知API
### 支持的版本
开始的版本：v1.6.4

###功能说明
通过极光推送的SDK，开发者只需要简单调用几个接口，便可以在应用中定时发送本地通知

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>本地通知API不依赖于网络，无网条件下依旧可以触发
<br>
<p>本地通知与网络推送的通知是相互独立的，不受保留最近通知条数上限的限制
<br>
<p>本地通知的定时时间是自发送时算起的，不受中间关机等操作的影响
</div>

### API  addLocalNotification 添加一个本地通知

####接口定义
```
public static void addLocalNotification(Context context, JPushLocalNotification notification)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ notification 是本地通知对象

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

### API  removeLocalNotification 移除指定的本地通知
#### 接口定义
```
public static void removeLocalNotification(Context context, long notificationId)
```

#### 参数说明
+ context 是应用的 ApplicationContext
+ notificationId是要移除的本地通知的ID

#### 调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

### API  clearLocalNotifications 移除所有的本地通知

####接口定义
```
public static void clearLocalNotifications(Context context)
```
####参数说明
+ context 是应用的 ApplicationContext

####调用说明
本接口可以在 JPushInterface.init 之后任何地方调用

###本地通知相关设置
```
//设置本地通知样式
 
public void setBuilderId(long)
 
//设置本地通知的title
 
public void setTitle(String paramString)
 
//设置本地通知的content
 
public void setContent(String paramString)
 
//设置额外的数据信息extras为json字符串
 
public void setExtras(String extras)
 
//设置本地通知的ID
 
public void setNotificationId(long notificationId)
 
//设置本地通知触发时间
 
public void setBroadcastTime(long broadCastTime)
 
public void setBroadcastTime(Date date)
 
public void setBroadcastTime(int year, int month, int day, int hour, int minute, int second)
```
###示例代码
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