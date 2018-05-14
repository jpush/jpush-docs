# Android API 

## Set debug mode API

### API - setDebugMode

Set debug mode

**Note: ** This interface needs to be called before the init interface to avoid the situation where some logs are not printed. In the case of multi-process, it is recommended to call onCreate in the custom Application.

#### Interface definition

```
public static void setDebugMode(boolean debug);
```

#### Parameter Description

+ Debug will print the debug level log when it indicates true, and only print the log above the warning level when it indicates false.


##  Initializing the Push Service API

### API - init

Initialize the push service.

After calling this API, the JPush push service will start to initialize. It is recommended to call it in onCreate in the custom Application.

#### Interface definition

```
public static void init(Context context);
```

#### Parameter Description

+ ApplicationContext in the context application

**Note: ** If you do not want to initialize the JPush SDK at this time, do not call init and call stopPush when the application is initialized

## Stopping and Restoring the Push Service API

### Supported versions

Supported version: 1.3.3

### Function Description
The push service provided by the JPush SDK is enabled by default.

The developer app can stop the JPush service by calling the stop push service API. When you need to use the JPush Service again, you must call the Restore Push Service API.

This feature is a completely local state operation. In other words: The status of stopping the push service will not be saved to the server.
If the developer app is reinstalled after you stop the push service, the JPush SDK will resume normal default behavior.
The behavior of this function is similar to the effect of network interruption, that is, the message pushed during the stop of push service.
After the push service is resumed, the client receives an offline message if the pushed message is still within the retained duration.

### API - stopPush

Stop push service

After calling this API, the JPush push service is completely stopped. Specifically:

+ Failed to receive push messages
+ ll other API calls of JPush are invalid and can not be recovered by JPushInterface.init but by calling resumePush.

#### Interface definition
```
public static void stopPush(Context context);
```

#### Parameter Description

+ ApplicationContext in the context application

### API - resumePush

Resume push service.

After this API is called, JPush will fully resume normal operation.

#### Interface definition

```
public static void resumePush(Context context);
```

#### Parameter Description
```
context 应用的 ApplicationContext
```

### API - isPushStopped

Used to check whether the Push Service has been stopped

+ Support SDK 1.5.2 or later

#### Interface definition
```
public static boolean isPushStopped(Context context);
```

### Parameter Description
+ ApplicationContext in the context application

### Code example

The following code is from the JPush Android Example.

```
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
```

## Receive and Push Message Receiver

### Supported versions

The initial version: Initially.

### Function Description

The JPush SDK receives the push and forwards it to the developer App via broadcast so that the developer can handle it flexibly.

This action is not necessary. The user defines the Receiver class to handle broadcasts from the SDK when he has needs.

If you do not do this, that is, you do not write a custom Receiver, nor do you configure this Receiver in AndroidManifest.xml, then the default behavior is:

+ Custom message frome receiving to push is not processed
+ You can receive the notification normally. The user clicks to open the main application interface.

### Accept broadcast

If all types of broadcasts are received, you need to add the following configuration information in AndroidManifest.xml:

```
<receiver
    android:name="Your Receiver"
    android:enabled="true">
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
```

Each Receiver action is explained in detail as follows.

#### Action - JPushInterface.ACTION\_REGISTRATION\_ID

##### String value
```
"cn.jpush.android.intent.REGISTRATION"
```

##### Functional Description

Registration ID obtained after SDK registered in the JPush Server.

In general, this broadcast information may not be processed.

To deeply integrate JPush, when developers want to save their relationship between App users and JPush users, they accept the broadcast, obtain the Registration ID, and save the relationship with App uid to the developer's own application server.

Using the alias and tag function provided by JPush is a simpler and lighter way to bind App users and JPush users. Please refer to the document:[ Alias and Tag Usage Tutorial.](android_senior/#_1)

##### IntentParameter

+ JPushInterface.EXTRA\_REGISTRATION\_ID
    + Globally unique ID obtained after SDK registered in the JPush Server. This ID can be used to send messages and notifications to the corresponding client.

            Bundle bundle = intent.getExtras();
            String title = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);


#### Action - JPushInterface.ACTION_MESSAGE_RECEIVED
##### String value

    "cn.jpush.android.intent.MESSAGE_RECEIVED"

##### Functional Description

Received a custom message Push.

The SDK only passes the custom message, and there will not be any interface display.

If the developer wants to push a custom message Push, then he needs to configure the Receiver action in AndroidManifest.xml and receive process in the BroadcastReceiver he writes.

##### Intent Parameter

+ JPushInterface.EXTRA_TITLE
    + Save the title of the message pushed by the server.
    + Corresponding title field of the API message content.
    + No display in Portal push message

            Bundle bundle = intent.getExtras();
            String title = bundle.getString(JPushInterface.EXTRA_TITLE);

+ JPushInterface.EXTRA_MESSAGE
    + Save the message content pushed by the server.
    + Corresponding message field of the API message content.
    + Corresponding "Custom Message Content" field on the Portal Push Message interface.

            Bundle bundle = intent.getExtras();
            String message = bundle.getString(JPushInterface.EXTRA_MESSAGE);

+ JPushInterface.EXTRA_EXTRA
    + Save additional fields pushed by the server. This is a JSON string.
    + Corresponding extras field of API message content.
    + Corresponding additional fields in the "optional settings" on the push message interface of Portal.

            Bundle bundle = intent.getExtras();
            String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);

+ JPushInterface.EXTRA_MSG_ID
    + Support SDK 1.6.1 or later.
    + ID that uniquely identifies the message, which can be used to report statistics.

            Bundle bundle = intent.getExtras();
            String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

#### Action - JPushInterface.ACTION_NOTIFICATION_RECEIVED.

##### String value

    "cn.jpush.android.intent.NOTIFICATION_RECEIVED"

##### Functional Description

Received a notification Push.

If the content of the notification is empty, no notification will be displayed on the notification bar.

However, this broadcast Intent will still be there. Developers can get other information outside the notification content.

##### Intent Parameter
+ JPushInterface.EXTRA_NOTIFICATION_TITLE
	+ Save the title of the notification pushed by the server.
	+ Corresponding title field of the API notification content.
	+ Corresponding "Notification Title" field on the push notification interface of Portal.
        
            Bundle bundle = intent.getExtras();         
            String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
            
+ JPushInterface.EXTRA_ALERT
	+ Save the notifications pushed by the server.
	+ Corresponding alert field of API notification content.
	+ Corresponding "notification content" field on the push notification interface of Portal.
            
            Bundle bundle = intent.getExtras();
            String content = bundle.getString(JPushInterface.EXTRA_ALERT);

+ JPushInterface.EXTRA_EXTRA
	+ Support SDK 1.2.9 or later.
	+ Save additional fields pushed by the server. This is a JSON string.
	+ Corresponding extras field of API notification content.
	+ Corresponding additional fields in the "optional settings" on the push message interface of Portal.
        
            Bundle bundle = intent.getExtras();
            String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);

+ JPushInterface.EXTRA_NOTIFICATION_ID
	+ Support SDK 1.3.5 or later.
	+ Notification ID of the notification bar, which can be used to clear notifications
	+ If the server alert field is empty, the notification id is 0
       
            Bundle bundle = intent.getExtras();
            int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);

+ JPushInterface.EXTRA_RICHPUSH_HTML_PATH
	+ Support SDK 1.4.0 or later.
	+ The rich media notification pushes the downloaded file path of the HTML for displaying the WebView.
            
            Bundle bundle = intent.getExtras();
            String fileHtml = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_PATH);
            
+ JPushInterface.EXTRA_RICHPUSH_HTML_RES
	+ Support SDK 1.4.0 or later.
	+ The rich media notification pushes the file name of the downloaded image resource. Multiple file names are separated by “,”. Same path as "JPushInterface.EXTRA_RICHPUSH_HTML_PATH".
            
            Bundle bundle = intent.getExtras();
            String fileStr = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_RES);
            String[] fileNames = fileStr.split(",");

+ JPushInterface.EXTRA_MSG_ID
	+ Support SDK 1.6.1 or later.
	+ The ID that uniquely identifies the notification message, which can be used to report statistics.
        
            Bundle bundle = intent.getExtras();
            String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

+ JPushInterface.EXTRA_BIG_TEXT
	+ Support SDK 3.0.0 or later supports rom 16 or more.
	+ The content of large text in large text notification styles.
        
            Bundle bundle = intent.getExtras();
            String bigText = bundle.getString(JPushInterface.EXTRA_BIG_TEXT);

+ JPushInterface.EXTRA_BIG_PIC_PATH
	+ Support SDK 3.0.0 or later, and support rom 16 or later.
	+ Support the path of the local picture, or fill in the address of network picture.
	+ The path/address of the large picture in the big picture notification style.
        
            Bundle bundle = intent.getExtras();
            String bigPicPath = bundle.getString(JPushInterface.EXTRA_BIG_PIC_PATH);

+ JPushInterface.EXTRA_INBOX
	+ Support SDK 3.0.0 or later, and supports rom 16 or later.
	+ Obtain a JSONObject. The value of each key of json will be displayed as a text entry.
	+ Inbox content in the style of the inbox notification.
        
            Bundle bundle = intent.getExtras();
            String inboxJson = bundle.getString(JPushInterface.EXTRA_INBOX);

+ JPushInterface.EXTRA_NOTI_PRIORITY
	+ Support SDK 3.0.0 or later，and support rom 16 or more.
	+ When the default is 0 and the range is -2 to 2 , other values will be ignored and defaulted.
	+ Notification priority
        
            Bundle bundle = intent.getExtras();
            String prio = bundle.getString(JPushInterface.EXTRA_NOTI_PRIORITY);

+ JPushInterface.EXTRA_NOTI_CATEGORY
	+ Support SDK 3.0.0 or later, and support rom of api 21 or later.
	+ Rely on the rom vendor's processing strategy for each category, such as the sorting of the notification bar.
	+  Notification classification.
        
            Bundle bundle = intent.getExtras();
            String prio = bundle.getString(JPushInterface.EXTRA_NOTI_CATEGORY);

#### Action - JPushInterface.ACTION\_NOTIFICATION\_OPENED

##### String value
    "cn.jpush.android.intent.NOTIFICATION_OPENED"
    
#####Functional Description

The user clicked on the notification. 

In general, users do not need to configure this receiver action.

If the developer does not configure this receiver action in AndroidManifest.xml, then the SDK will open the application's main activity by default, which is equivalent to the effect of the user clicking on the desktop icon.

If the developer configures this receiver action in AndroidManifest.xml, then the SDK will not act when the user clicks on the notification. Developers should deal with their own BroadcastReceiver class, such as opening an Activity.

##### Intent Parameter

+ JPushInterface.EXTRA\_NOTIFICATION\_TITLE

	+ Save the title of the notification pushed by the server.
	+ Corresponding title field of the API notification content.
	+ Corresponding "Notification Title" field on the push notification interface of Portal.
        
            Bundle bundle = intent.getExtras();
            String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);

+ JPushInterface.EXTRA_ALERT
	+ Save the notifications pushed by the server.
	+ Corresponding alert field of the API notification content.
	+ Corresponding "notification content" field on the push notification interface of Portal.
        
            Bundle bundle = intent.getExtras();
            String content = bundle.getString(JPushInterface.EXTRA_ALERT);

+ JPushInterface.EXTRA_EXTRA
	+ Support SDK 1.2.9 or later.
	+ Save additional fields pushed by the server. This is a JSON string.
	+ Corresponding extras field of API message content.
	+ Corresponding additional fields in the "optional settings" on the push message interface of Portal.
        
            Bundle bundle = intent.getExtras();
            String type = bundle.getString(JPushInterface.EXTRA_EXTRA);

+ JPushInterface.EXTRA_NOTIFICATION_ID
	+ Support SDK 1.3.5 or later.
	+ Notification ID of the notification bar, which can be used to clear notifications
            
            Bundle bundle = intent.getExtras();
            int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);

+ JPushInterface.EXTRA_MSG_ID
	+ Support SDK 1.6.1 or later.
	+ ID that uniquely identifies the adjustment message, which can be used to report statistics, etc.
            
            Bundle bundle = intent.getExtras();
            String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

#### Action - JPushInterface.ACTION\_NOTIFICATION\_CLICK\_ACTION

##### String value

    "cn.jpush.android.intent.NOTIFICATION_CLICK_ACTION"

##### Functional Description

The user clicked on the custom button in the notification bar. (Support SDK 3.0.0 or later)

Developers using normal notifications do not need to configure this receiver action. Only when the developer uses MultiActionsNotificationBuilder to build a notification that carries a button's notification bar, he can use this action to capture the user's click on the notification bar button and do it himself.

##### Intent Parameter
+ JPushInterface.EXTRA_NOTIFICATION_ACTION_EXTRA
	+ Support SDK 3.0.0 or later.
	+ Get additional information carried by clicking notification bar button.
	+ Use corresponding button information added by using MultiActionsNotificationBuilder.addJPushAction.

            private void setAddActionsStyle() {
                MultiActionsNotificationBuilder builder = new MultiActionsNotificationBuilder(PushSetActivity.this);
                builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "first", "my_extra1");
                builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "second", "my_extra2");
                builder.addJPushAction(R.drawable.jpush_ic_richpush_actionbar_back, "third", "my_extra3");
                JPushInterface.setPushNotificationBuilder(10, builder);

                Toast.makeText(PushSetActivity.this, "AddActions Builder - 10", Toast.LENGTH_SHORT).show();
            }

	+ Get the corresponding additional information, and determine which button to handle by yourself.

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

##### String value

    "cn.jpush.android.intent.CONNECTION"

##### Functional Description

The connection status of the JPush service changed. (Note: This does not mean the network connection status of the Android system.)

##### Intent Parameter

+ JPushInterface.EXTRA_CONNECTION_CHANGE

	+ Support SDK 1.6.3 or later.
	+ Get the connection status of the current JPush service.
        
            Bundle bundle = intent.getExtras();
            boolean connected = bundle.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);

###  Samples of Developer Custom Receiver Code 

```
public void onReceive(Context context, Intent intent) {
    Bundle bundle = intent.getExtras();
    Log.d(TAG, "onReceive - " + intent.getAction());

    if (JPushInterface.ACTION_REGISTRATION_ID.equals(intent.getAction())) {
        String regId = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);
        Log.d(TAG, "[MyReceiver] 接收Registration Id : " + regId);
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
```

For more example code, refer to the example project in the Android SDK archive.

## Aliases and Tags API

### Function Description

```
Tips, please pay attention to deal with the call back results when seting the labela and aliases. Only the setting is successful, can push to the target. Otherwise the server API will return a 1011 error.
```

#### Alias
For the user who installed the application, identify the individual name by alias. When the Push message is given to this user later, it can be specified with this alias.

Each user can only specify one alias.

Within the same application, different aliases are recommended for different users. In this way, users are uniquely identified based on their aliases.

The system does not restrict one alias to only one user. If an alias is assigned to more than one user, [the server-side API](../../server/push/rest_api_v3_push) will send messages to multiple users when specifying the alias.

Example: In a game where the user wants to log in, it is possible to set the alias as userid. When the game is running, it is found that the user has not played the game for 3 days. Then, [the server-side API](../../server/push/rest_api_v3_push) is called to notify the user by the notification on the client based on the userid.

#### Tag

Label the user who installed the application. Its purpose is mainly to facilitate developers to deliver Push messages in batches according to labels.

Multiple tags can be played for each user.

Example: game, old_page, women

### Method - filterValidTag

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Recommendations
 <br>
 <p>When tags are set, if one of the tags is invalid, the entire setup process fails.
 <br>
 <p>If the app tags are set dynamically during the run, and there are invalid characters specified in the JPush SDK tag,
 <p>It is possible that an invalid tag will cause the update failure of all tags in this call.
 <br>
 <p>You can call this method filterValidTags to filter out invalid tags and get valid tags.
 <p>Then call the set tags / alias method of the JPush SDK.
</div>

#### Supported versions

Supported version: 1.5.0

#### Definition of the Interface

    public static Set<String> filterValidTags(Set<String> tags);

#### Interface Return

Valid tag collection

## New Alias and Tag Interfaces

The new alias and tag interface supports the addition, deletion, and modification functions. It supports the 3.0.7 version. The interfaces of the old version alias and tag are no longer maintained from the 3.0.7 version.

#### Callback Instructions

Callback of the alias and tag interface triggers cn.jpush.android.service.JPushMessageReceiver. For detailed callback methods, please refer to [the description of new message callback mode](#new-callback).

### Method - setAlias

Call this API to set the alias.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

#### Supported Versions

Supported version: 3.0.7

#### Interface Definition

    public static void setAlias(Context context, int sequence, String alias);

Parameter Definition

+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.
+ alias
	+ Each call sets a valid alias, overwriting previous settings.
	+ Valid aliases are composed of letters (case-sensitive), numbers, underscores, Chinese characters, special characters @!#$&*+=.|. 
	+ Limitation: The alias name length is limited to 40 bytes. (UTF-8 encoded is required to determine the length)


### Method - deleteAlias

Call this API to delete the alias.

#### Supported Versions

Supported version: 3.0.7

#### Interface Definition

```
public static void deleteAlias(Context context,int sequence);
```

Parameter Definition

+ sequence
    + The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.

### Method - getAlias

Call this API to query for aliases.

#### Supported Versions

Supported version: 3.0.7

#### Interface Definition

    public static void getAlias(Context context,int sequence);

Parameter Definition

+ sequence
    + The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.

### Method - setTags

Call this API to set the label.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

#### Supported Versions

Supported Version: 3.0.7

#### Interface Definition

    public static void setTags(Context context, int sequence,Set<String> tags);

#### Parameter Definition

+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.

+ tags
	+ Set at least one tag per call, overwriting previous settings, not new.
	+ Valid label components: letters (case-sensitive), numbers, underscores, Chinese characters, special characters @!#$&*+=.|.
	+ Restrictions: Each tag has a named length of 40 bytes and can support up to 1000 tags. The total length of a single operation must not exceed 5000 bytes. (UTF-8 encoded is required to determine the length)
        +  A single device supports up to 1000 tags. There is no limit to the number of App global tags.

### Method - addTags

Call this API to add a tag.

#### Supported Versions

开始支持的版本：3.0.7 Supported Version: 3.0.7

#### Interface Definition

    public static void addTags(Context context, int sequence,Set<String> tags);

#### Parameter Definition
+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.
+ tags
	+ Add at least one tag for each call.
	+ Valid label components: letters (case-sensitive), numbers, underscores, Chinese characters, special characters @!#$&*+=.|.
	+ Restrictions: Each tag has a named length of 40 bytes and can support up to 1000 tags. The total length of a single operation must not exceed 5000 bytes. (UTF-8 encoded is required to determine the length)
    	+ A single device supports up to 1000 tags. There is no limit to the number of App global tags.

### Method - deleteTags

Call this API to delete the specified tag

#### Supported Versions

Supported Version: 3.0.7

#### Interface Definition

    public static void deleteTags(Context context, int sequence,Set<String> tags);

#### Parameter Definition
+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.
+ tags
	+ Delete at least one tag for each call.
	+ Valid label components: letters (case-sensitive), numbers, underscores, Chinese characters, special characters @!#$&*+=.|.
	+ Restrictions: Each tag has a named length of 40 bytes and can support up to 1000 tags. The total length of a single operation must not exceed 5000 bytes. (UTF-8 encoded is required to determine the length)
    	+ A single device supports up to 1000 tags. There is no limit to the number of App global tags.

### Method - cleanTags

Call this API to clear all tags.

#### Supported Versions

Supported Version: 3.0.7

#### Interface Definition

    public static void cleanTags(Context context, int sequence);

#### Parameter Definition

+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.

### Method - getAllTags

Call this API to query all tags.

#### Supported Versions

Supported Version: 3.0.7

#### Interface Definition

    public static void getAllTags(Context context, int sequence);

#### Parameter Definition

+ sequence
    + User-defined operation serial number, which returned with the operation result, used to identify the uniqueness of an operation

### Method - checkTagBindState

Call this API to query the status of binding of the specified tag to the current user

#### Supported Versions

Supported Version: 3.0.7

#### Interface Definition

    public static void checkTagBindState(Context context,int sequence,String tag);

#### Parameter Definition

+ sequence
    + The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.
+ tag
    + The tag being queried

## Set Mobile Number Interface

The 3.1.1 version started to provide an interface for setting the mobile phone number, which is used for [the SMS supplement function.](../../guideline/push-SMS-intro.md)

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Note: SMS supplements only support domestic services. The number format is 11 digits, with or without +86 as prefix.
</div>


### Method - setMobileNumber

Call this API to set the phone number. The interface controls the frequency of the call up to a maximum of three times within 10s.

#### Supported Versions

Supported Version: 3.1.1

#### Method Definition

    public static void setMobileNumber(Context context,int sequence, String mobileNumber);

#### Parameter Definition
+ context
	+ ApplicationContext of the application.
+ sequence
	+ The user-defined operation sequence number, which returned with the operation result, is used to identify the uniqueness of an operation.
+ mobileNumber
	+ Mobile number. If null or null string is passed, the number binding operation is cancelled.
	+ Restrictions: can only begin with "+" or a digit; the following content can only contain "-" and digits.

#### Callback Instructions
The interface callback triggers cn.jpush.android.service.JPushMessageReceiver. For detailed callback methods, please refer to the description [of new message callback method.](#new-callback)


##<span id="new-callback">New Message Callback Method Description</span>

Added callbacks after version 3.0.7.

### Class - cn.jpush.android.service.JPushMessageReceiver

1. The related callback class in the new message callback method.
2. The new tag and alias operation callbacks are triggered in the developer-defined subclass of this class.
3. Callbacks for mobile number settings are triggered in a developer-defined subclass of this class.

This class is the callback parent class. The developer needs to inherit the class and configure the corresponding implementation class in the Manifest. The result of the interface operation will be called back in the following method of the configured class.

### Method - onTagOperatorResult

Tag addition, deletion, and search will call back the result in this method.

####  Supported Versions

Supported version: 3.0.7

####  Interface Definition

    public void onTagOperatorResult(Context context, JPushMessage jPushMessage);

####  Parameter Definition
+ jPushMessage
	+ For the message result body returned by the tag-related operation, please refer to the description of the JPushMessage class.

### Method - onCheckTagOperatorResult

Checking the binding status of a tag with the current user will call back the result in this method.

#### Interface Definition

    public void onCheckTagOperatorResult(Context context, JPushMessage jPushMessage);

#### Parameter Definition

+ jPushMessage
	+ For the message result body returned by the check tag and the binding state of the current user, please refer to the description of the JPushMessage class.

### Method - onAliasOperatorResult

Alias-related operations call back the result in this method.

#### Method Definition

    public void onAliasOperatorResult(Context context, JPushMessage jPushMessage);

#### Parameter Definition

+ jPushMessage
	+ For the message result body returned by the alias-related operation, please refer to the description of the JPushMessage class.

### Method - onMobileNumberOperatorResult

Setting the phone number will call back the result in this method.

####  Supported Versions

Supported Version: 3.1.1

####  Method Definition

    public void onMobileNumberOperatorResult(Context context, JPushMessage jPushMessage)

####  Parameter Definition

+ context
	+ Application Context of the application.
+ jPushMessage
	+ About setting the message result body returned by the mobile phone number, please refer to the description of the JPushMessage class.

### Class - cn.jpush.android.api.JPushMessage

1. The result of the related callback in the new message callback method. Use this class object to obtain the corresponding operation result.
2. Currently only operation callbacks of new tag and alias will involve in this class.

### Method - getAlias

Developers pass or query the aliases

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public String getAlias();

### Method - getTags

Developers pass or query the tags.

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public Set<String> getTags();

### Method - getErrorCode

Corresponding to the operation of the return code, 0 is successful, other return code please refer to the error code definition.

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public int getErrorCode();

### Method - getSequence

Through the sequence passed in when developer calls the interface, developer can get the corresponding operation from the developer's own cache.

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public int getSequence();

### Method - getTagCheckStateResult

The status of the tag that the developer wants to query is bound to the current user.

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public boolean getTagCheckStateResult();

### Method - getCheckTag

The developer wants to query the tag in the binding state.

####  Supported Versions

Supported Version: 3.0.7

####  Method Definition

    public String getCheckTag();

### Method - getMobileNumber

The developer calls the incoming phone number when setting the interface.

#### Supported Versions

Supported Version: 3.1.1

####  Method Definition

    public String getMobileNumber();

## Old Alias and Tag Interface

The aliases and tag interfaces provided in the 1.5.0 to 3.0.6 versions are overriding logic. Starting from 3.0.7, they are no longer maintained (but will still remain). Developers are advised to use the new tag and alias interfaces provided by 3.0.7.

### Method - setAliasAndTags (with Callback)

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting

After the previous call, if you need to rechange the alias and label, you only need to call this API again.

####  Supported Versions

Supported Version: 1.5.0

####  Interface Definition
```
public static void setAliasAndTags(Context context, 
                                   String alias, 
                                   Set<String> tags, 
                                   TagAliasCallback callback);
```

####  Parameter Definition
+ alias
	
    + null: This value is not set for this call. (Note: Not the string "null")
	+ "" (empty string) indicates the setting before cancellation.
	+ Each call sets a valid alias, overwriting previous settings.
	+ Valid aliases are composed of letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.6 support) @!#$&*+=.|.
	+ Limitation: The alias name length is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

+ tags

	+ null: This value is not set for this call. (Note: Not the string "null")
	+ An empty array or list indicates the setting before cancellation.
	+ Set at least one tag per call, overwriting previous settings, not new.
	+ Valid label components: letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.6 support) @!#$&*+=.|.
	+ Restrictions: Each tag has a named length of 40 bytes and can support up to 1000 tags. The total length of a single operation must not exceed 7000 bytes. (UTF-8 encoded is required to determine the length)

+ callback

	+ The getResult method of TagAliasCallback returns to the corresponding parameters alias, tags, and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code.

### Method - setAlias

Call this API to set the alias.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

#### Supported Versions

Supported Version: 1.5.0

#### Interface Definition

```
public static void setAlias(Context context, String alias, TagAliasCallback callback)
```

#### Parameter Definition

+ alias
    * "" (empty string) indicates the setting before cancellation.
    * Each call sets a valid alias, overwriting previous settings.
    * Valid aliases are composed of letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.6 support) @!#$&*+=.|.
    * Limitation: The alias name length is limited to 40 bytes. (UTF-8 encoded is required to determine the length)
+ callback
    * The gotResult method of TagAliasCallback returns to the corresponding parameters alias, tags, and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code

### Method - setTags

Call this API to set the label.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Recommendations
 <br>
 <p>If the alias/tags to be set are dynamic, it is possible that the entire calls fails when calling setAliasAndTags because the alias / tags are invalid.
 <br>
 <p>Calling this method just sets tags to eliminate the effect of potentially invalid aliases on this call.
</div>

#### Supported Versions

Supported Version: 1.5.0

#### Interface Definition

    public static void setTags(Context context, Set<String> tags, TagAliasCallback callback)

#### Parameter Definition

+ tags
    * An empty array or list indicates the setting before cancellation.
    * Set at least one tag per call, and overwrite previous settings, not new.
    * Valid label components: letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.6 support) @!#$&*+=.|.
    * Restrictions: Each tag has a named length of 40 bytes and can support up to 1000 tags. The total length of a single operation must not exceed 7000 bytes. (UTF-8 encoded is required to determine the length)
            ▪ A single device supports up to 1000 tags. There is no limit to the number of App global tags.
+ callback
    * The getResult method of TagAliasCallback returns the corresponding parameters alias, tags, and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code.

### Class - TagAliasCallback

Set the callback class for the alias and tag methods to get the result of the callback on the gotResult method. If callback responseCode = 0, then confirm the setting is successful.

####  Supported Versions

Supported Version: 1.5.0

####  Interface Definition

    public void gotResult(int responseCode, String alias, Set<String> tags);

####  
Parameter Definition

+ responseCode
    * 0 indicates successful call.
    * For other return codes, please refer to the definition of error codes.
+ alias
    * The original alias
+ tags
    * The Original label

### Error Code Definition

Please skip to [the list of error code definition](#client_error_code)

### Related Documents

+ [Android SDK Tag and Alias API](../../client/Android/android_api/#api_3)
+ [iOS SDK Tag and Alias API](../../client/iOS/ios_api/#api-ios)

## Obtain the RegistrationID API

### Supported Versions

Supported Version: 1.6.0

### Function Description


#### RegistrationID Definition

When the application that integrates the JPush SDK successfully registers to the JPush server for the first time, the JPush server will return a unique device identifier, RegistrationID, to the client. The JPush SDK sends the RegistrationID to the application as a broadcast.

The application can save this RegistrationID on its own application server, and then it can push messages or notifications to the device based on the RegistrationID.

### API - getRegistrationID

Call this API to get the application's corresponding RegistrationID.__The corresponding value is only returned when the application successfully registers to the server of JPush, otherwise an empty string is returned.__

#### Supported Versions

Supported Version: 1.6.0

#### Interface Definition

```
//SDK 初次注册成功后，开发者通过在自定义的 Receiver 里监听 Action - cn.jpush.android.intent.REGISTRATION 来获取对应的 RegistrationID。注册成功后，也可以通过此函数获取public static String getRegistrationID(Context context)
```

### Additional Information

#### Point-to-point push with RegistrationID

You can use the RegistrationID to push messages and notifications. Referring to the document Push API v2, when receiver_type = 5 and receiver_value is set to RegistrationID, it can be pushed according to the RegistrationID.

Note: To use this feature, the client app must integrate JPush Android SDK version 1.6.0 and above.

## Statistical Analysis API

#### Supported Versions

Supported Version: 1.6.0

#### Function Description

This API is used for statistics of "user usage duration", "active user", and "user opening times", and is reported to the server and displayed to developers on the portal.

#### API - onResume / onPause

##### Interface Definition

```
public static void onResume(final Activity activity)
public static void onPause(final Activity activity)
```

##### Parameter Description

+ The activity in which the activity is currently located.

##### Call Description

+ Should be called in all Activity's onResume / onPause methods.

##### Code Example

```
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
```

#### API - reportNotificationOpened

##### Started version

+ Android SDK 1.6.1

##### Function Description

The notification bar for reporting to the user is opened, or is used to report events that the user needs to collect such as the user-defined message being displayed.

##### Interface Definition

```
public static void reportNotificationOpened(Context context, String msgId)
```

Parameter Description

+ context: ApplicationContext of the application
+ msgId: Push each message and notification with a unique ID. (msgId is derived from the Extra field for sending messages and notifications. JPushInterface.EXTRA_MSG_ID. Please refer to Receiver)

##### Code Example

```
   JPushInterface.reportNotificationOpened(context,bundle.getString(JPushInterface.EXTRA_MSG_ID));
```

## Clear Notification API

#### Supported Versions

Supported Version: 1.3.5

#### Function Description

When the notification is pushed to the client, the JPush SDK presents the notification to the notification bar.

This API provides the ability to clear notifications, including: Clearing all notifications displayed by JPush (excluding the notifications displayed by non-Jushush SDK); Clearing the specified notification.

#### API - clearAllNotifications

##### Interface Definition

```
public static void clearAllNotifications(Context context);
```

##### Parameter Description

+ Context context: ApplicationContext of the application

#### API - clearNotificationById

##### Interface Definition

    public static void clearNotificationById(Context context, int notificationId);

##### Parameter Description

+ Context context：应用的ApplicationContext  ApplicationContext of the application
+ int notificationId：通知ID  Notification ID

```
 此 notificationId 来源于intent参数 JPushInterface.EXTRA_NOTIFICATION_ID，可参考文档 接收推送消息Receiver  The notificationId is derived from the intent parameter JPushInterface.EXTRA_NOTIFICATION_ID. For reference, please view the Receiver.
```

## Set the Time Allowed to Push API

#### Supported Versions

Initial Version: Initial

#### Function Description

By default, users could push at any time. That is, any time there is a push, the client could receive it and display it.

Developers can call this API to set the time allowed to push.

If you do not receive a message within this period of time, the treatment of SDK is: **The notifications pushed to it are discarded.**

```
 This is a realization of pure client, so it doesn't matter with the client time, time zone, etc.
 And the interface is only valid for notifications, and custom messages are not affected.
```

API - setPushTime

##### Interface Definition

    public static void setPushTime(Context context, Set<Integer> weekDays, int startHour, int endHour)

##### Parameter Description

+ ApplicationContext of the Context context application
+ Set days, 0 means Sunday, 1 means Monday, and so on. (7-day system, the int range in the Set collection is 0 to 6)
+ The value of set is null, and you can receive notification at any time. The size of the set is 0, indicating that no notification is received at any time.
+ int startHour: starting time for push (24-hour format: startHour has a range of 0 to 23)
+ int endHour: ending time for push(24 hour format: endHour range 0 to 23)

##### Code Example

```
Set<Integer> days = new HashSet<Integer>();
days.add(1);
days.add(2);
days.add(3);
days.add(4);
days.add(5);
JPushInterface.setPushTime(getApplicationContext(), days, 10, 23);
This code means that it can be pushed from Monday to Friday, from 10:00 to 23:00
```

## Set API for Notifying Silence Time

### Supported Versions

Supported Version: 1.4.0

### Function Description

By default, when the user receives a push notification, the client may experience a vibration, a ring, and other prompts. However, the user wants to be a "do-not-disturb" mode at the time of sleeping, meeting, etc, which is also a concept of silence period.

Developers can call this API to set silence periods. If you receive a message within this time period: There will be no ringing or shaking.

### API - setSilenceTime

#### Interface Definition

```
public static void setSilenceTime(Context context, int startHour, int startMinute, int endHour, int endMinute)
```

#### Parameter Description
+ ApplicationContext of the Context context application
+ int startHour: starting time of silence period - hours (24-hour format, range: 0~23)
+ int startMinute: starting time of silence period - minutes (range: 0~59)
+ int endHour: ending time of silence period - hours (24-hour format, range: 0~23)
+ int endMinute: ending time of the silence period - minutes (range: 0~59)

#### Code Example

```
JPushInterface.setSilenceTime(getApplicationContext(), 22, 30, 8, 30);
```

This code indicates a silence period from 10:30 in the evening to 8:30 in the morning.

## Interface for Application Permission (Android 6.0 and above)

### Supported Versions

Supported Version: 2.1.0

### Function Description

On Android 6.0 and above systems, it is necessary to request some of the privileges that are used. Some of the JPush SDKs need to request the following permissions, because these permissions are needed to make statistics more accurate and feature richer. We recommend developers to call them.

```
"android.permission.READ_PHONE_STATE"
"android.permission.WRITE_EXTERNAL_STORAGE"
"android.permission.READ_EXTERNAL_STORAGE"
"android.permission.ACCESS_FINE_LOCATION"
```

### API - requestPermission

#### Interface Definition

```
public static void requestPermission(Context context);
```

#### Parameter Description

+ The context of the currently applied Activity

## Set Whether Power Saving Mode Is Enabled

### Supported Versions

Supported Version: 3.0.9

### Function Description

JPush SDK enables and disables the power saving mode. The default is off.

### API - setPowerSaveMode

####Interface Definition

```
public static void setPowerSaveMode(Context context,boolean enable);
```

#### Parameter Description

+ The context of the currently applied Activity
+ Enable- whether needs to be on or off, true is on, false is off

## Customization API of Notification Bar Style

### Supported Versions

Supported Version: Initial

### Function Description

In most cases, the developer does not need to call the custom notification bar API here to define the notification bar style. He only needs to use the default SDK.

If you want to:

+ Change the ringtone, vibration, display, and disappearance behavior in Notification
+ Display Styles of Custom Notification Bar 
+ Different Push notifications have different Notification styles

Please use this notification bar to customize the capabilities provided by the API

### Tutorials and code examples

Please refer to the document: [Style Tutorial of Custom Notification Bar ](android_senior/#_8)

### API - Set building class of default notification bar style 

```
public static void setDefaultPushNotificationBuilder(DefaultPushNotificationBuilder builder)
```

This method can be called when the user needs to customize the default notification bar style.

The JPush SDK provides 3 building classes for customizing the notification bar style:

+ BasicPushNotificationBuilder
    * Basic is used to customize basic styles (behavior) such as defaults / flags / icon in Android Notification
+ CustomPushNotificationBuilder
    * Inherit Basic to further lets developers customize Notification Layout
+ MultiActionsNotificationBuilder
    * Inherit DefaultPushNotificationBuilder to further allow developers to customize Notification Layout

If you do not call this method to customize, the default notification bar style of JPush SDK is: notification bar prompts in Android standard.

### API - Set notification bar style building classes in a number 

```
public static void setPushNotificationBuilder(Integer notificationBuilderId, BasicPushNotificationBuilder builder)
```

When the developer needs to specify different notification bar styles (behaviors) for different notifications, this method needs to be called to set multiple notification bar building classes.

Version 3.0.0 adds MultiActionsNotificationBuilder, a notification bar building class with buttons that can be set via this api.

When setting, the developer maintains the number of the notificationBuilderId himself. When the notification is delivered, the number is specified by using n_builder_id. Thus, the Push SDK calls the specified number of notification bar building class set in the developer application to customize the style of the notification bar.

## Set Retained Notifications API Recently

### Supported Versions

Supported Version: 1.3.0

### Function Description

When pushing a lot of notifications to the client with JPush, if the user does not deal with it, there will be a lot of reservations there.

The new version of the SDK (1.3.0) adds this feature to limit the number of notifications retained. The default is to keep the last 5 notifications.

Developers can define different quantities by calling this API.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
 <p>Only valid for notifications. The so-called retention of the latest means that if there is a new notification, the oldest one in the previous list will be removed.
 <br>
 <p>For example, set to keep the last 5 notifications. Suppose there are already 5 items in the notification bar. When the 6th item arrives, the 1st item will be removed.
</div>


### API - setLatestNotificationNumber

#### Interface Definition

```
public static void setLatestNotificationNumber(Context context, int maxNum)
```

#### Parameter Description
+ ApplicationContext of the ApplicationContext
+ maxNum: The maximum number of displays

#### Call Description

This interface can be called anywhere after JPushInterface.init. It can be called multiple times. The SDK uses the last called value.

#### Code Example

```
JPushInterface.init(context);
JPushInterface.setLatestNotificationNumber(context, 3);
```
<a name="client_error_code"></a>
## Definition of Client Error Code


<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th >Description</th>
			<th>Detailed Explanation</th>
		</tr>
		<tr >
			<td>6001</td>
			<td>Invalid setting, tag/alias should not be null, new tag/alias interface starting from 3.0.7 This error code indicates that the tag/alias parameter cannot be null</td>
			<td></td>
		</tr>
		<tr >
			<td>6002</td>
			<td>Set timeout</td>
			<td>Recommend to try again</td>
		</tr>
		<tr >
			<td>6003</td>
			<td>Alias string is illegal</td>
			<td>Valid aliases and labels are composed of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.6 support) @!#$&*+=.|</td>
		</tr>
		<tr >
			<td>6004</td>
			<td>Alias is too long. Up to 40 bytes</td>
			<td>Chinese UTF-8 is 3 bytes</td>
		</tr>
		<tr >
			<td>6005</td>
			<td>One of the tag strings is illegal</td>
			<td>Valid aliases and labels are composed of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.6 support) @!#$&*+=.|</td>
		</tr>
		<tr >
			<td>6006</td>
			<td>One tag is extremely long. One tag up to 40 bytes</td>
			<td>Chinese UTF-8 is 3 bytes</td>
		</tr>
		<tr >
			<td>6007</td>
			<td>The number of tags exceeds the limit. Up to 1000</td>
			<td>This is a device limitation. There is no limitations on the number of tags in per application.</td>
		</tr>
		<tr >
			<td>6008</td>
			<td>Tag exceeds the total length limit</td>
			<td>The new added tag/alias interface in the 3.0.7 version has a maximum length of up to 5000 bytes and the old interface of tag/alias has a total length of up to 7000 bytes.</td>
		</tr>
		<tr >
			<td>6009</td>
			<td>Unknown mistake</td>
			<td>PushService startup exception due to permission problem</td>
		</tr>
		<tr >
			<td>6011</td>
			<td>Set tag or alias greater than 10 times within 10s, or set mobile number greater than 3 times within 10s</td>
			<td>Operation is too frequent in a short time</td>
		</tr>
		<tr >
			<td>6012</td>
			<td>Set tag or alias or mobile phone number in stop state of JPush service </td>
			<td>New error code for version 3.0.0. Developers can do relevant processing or hints based on this error code information</td>
		</tr>
		<tr >
			<td>6013</td>
			<td>Time axis of user device is abnormal</td>
			<td>New error code for version 3.0.6. Abnormal changes in the device's local time axis affect the set frequency</td>
		</tr>
        <tr >
			<td>6014</td>
			<td>The server is busy and it is recommended to try again</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6015</td>
			<td>Appkey in the blacklist</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6016</td>
			<td>Invalid user</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6017</td>
			<td>Invalid request</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6018</td>
			<td>The number of tags accumulated in the backend exceeds 1000. It is recommended that some tags be cleared first.</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6019</td>
			<td>Query request expired</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6020</td>
			<td>Tag/alias operation paused. It is recommended to set it again </td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6021</td>
			<td>Tags operation is in progress, and other tags operations are temporarily unavailable</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
        <tr >
			<td>6022</td>
			<td>The alias operation is in progress, and other alias operations are temporarily unavailable</td>
			<td>New error code for Version 3.0.7</td>
		</tr>
		 <tr >
			<td>6023</td>
			<td>Invalid mobile phone number</td>
			<td>Can only start with "+" or digit; the following content can only contain "-" and digits; new error code added in Version 3.1.1 </td>
		</tr>
		 <tr >
			<td>6024</td>
			<td>Server internal error</td>
			<td>Server internal error, please retry later; new error code added in Version 3.1.1</td>
		</tr>
		 <tr >
			<td>6025</td>
			<td>Phone number is too long</td>
			<td>The mobile phone number is too long. The maximum length of the current Jiguang detection mobile phone number is 20. new error code added in Version 3.1.1.</td>
		</tr>
		<tr >
			<td>-997</td>
			<td>Registration failed/login failed</td>
			<td>(Usually due to lack of network) If you keep the network of the device properly, and still encounter this problem, that the JPush server refuses to register is another reason. The reason for this is generally that the Android package name of your current App, as well as the appKey, is different from the Android package name and AppKey of the application you registered on the Portal.</td>
		</tr>
		<tr >
			<td>1005</td>
			<td>Package name and AppKey do not match</td>
			<td></td>
		</tr>
		<tr >
			<td>1008</td>
			<td>AppKey is illegal</td>
			<td>Please go to the official website to check the appkey in this app details and confirm it is correct</td>
		</tr>
		<tr >
			<td>1009</td>
			<td>Android app is not created under current appkey</td>
			<td>Please go to the official website to check the application details of this application</td>
		</tr>
		<tr >
			<td>-996</td>
			<td>Disconnected network</td>
			<td>If you ensure that the device network is normal, it may be because the package name is incorrect, and the server is forced to disconnect the client.</td>
		</tr>
		<tr >
			<td>-994</td>
			<td>Network connection timeout</td>
			<td></td>
		</tr>
	</table>
</div>



## CrashLog Collection and Reporting

### Supported Versions

+ 2.1.8 and later, the default is open, and add stopCrashHandler interface.

### Function Description

The SDK captures the crash log through Thread.UncaughtExceptionHandler and reports it in real time when the program crashes. If the real-time report fails, it will be sent to the server when the program starts next time. Call this method if you need the crash log function.

### API - stopCrashHandler (turn off CrashLog reporting)

#### Interface Definition

```
public static void stopCrashHandler(Context context)
```

#### Parameter Description
+ Context ApplicationContext of Context application

### API - initCrashHandler (Open CrashLog)

#### Interface Definition

```
public static void initCrashHandler(Context context);
```

#### Parameter Description
+ ApplicationContext of the Context application

## Get Connection Status of Push 

### Supported Versions

Supported Version: 1.6.3

### Function Description

Developers can use this function to get the connection status of the current Push service.

When the connection status changes (connected, disconnected), a broadcast will be issued. Developers can monitor cn.jpush.android.intent.CONNECTION in the custom Receiver to obtain the status of changes, and can also be actively obtained through the API.

### API getConnectionState

#### Function Description

Get current connection status

#### Interface Definition

```
public static boolean getConnectionState(Context context);
```
#### Parameter Description

+ ApplicationContext of the Context application

#### ACTION cn.jpush.android.intent.CONNECTION

##### Intent Parameter
JPushInterface.EXTRA_CONNECTION_CHANGE: the value passed by broadcast when Push connection status changes

```
boolean connected = bundle.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
```

##### Sample Code

Add the following code in the MyReceiver onReceive method of JPush Demo:

```
else if(JPushInterface.ACTION_CONNECTION_CHANGE.equals(intent.getAction())) {
            boolean connected = intent.getBooleanExtra(JPushInterface.EXTRA_CONNECTION_CHANGE, false);
            Log.e(TAG, "[MyReceiver]" + intent.getAction() +" connected:"+connected);
        }
```

## Local Notification API

### Supported Versions

Supported Version: 1.6.4

### Function Description

Through the JPush SDK, developers only need to simply call a few interfaces and they can send local notifications in the application at regular intervals.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>The local notification API does not depend on the network and can still be triggered under non-network conditions
<br>
<p>Local notifications and web push notifications are independent of each other and are not subject to the limit of the number of recent retained notifications 
<br>
<p>The timing time of local notification is calculated from the time of sending and is not affected by operations such as intermediate shutdown.
</div>


### API addLocalNotification: Add a local notification

#### Interface Definition

```
public static void addLocalNotification(Context context, JPushLocalNotification notification)
```

#### Parameter Description

+ context is the application's ApplicationContext
+ notification is the object of local notification 

Call Description
This interface can be called anywhere after JPushInterface.init

### API removeLocalNotification: Remove the specified local notification

#### Interface Definition
```
public static void removeLocalNotification(Context context, long notificationId)
```

#### Parameter Description
+ context is the application's ApplicationContext
+ notificationId is the local notification ID to remove

#### Call Description

This interface can be called anywhere after JPushInterface.init

### API clearLocalNotifications: Removes all local notifications

#### Interface Definition
```
public static void clearLocalNotifications(Context context)
```

#### Parameter Description

+ context is the application's ApplicationContext

#### Call Description

This interface can be called anywhere after JPushInterface.init

#### Local Notification Related Settings

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

### Sample Code

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
