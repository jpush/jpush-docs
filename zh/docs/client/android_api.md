# Android API

### 停止与恢复推送服务 API

#### 支持的版本

开始的版本：v1.3.3

#### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者App可以通过调用停止推送服务API来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。如果停止推送服务后，开发者App被重新安装，或者被清除数据，JPush SDK 会恢复正常的默认行为。（因为保存在本地的状态数据被清除掉了）。

> 本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息，恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。

#### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

* JPush Service 不在后台运行
* 收不到推送消息
* 不能通过 JPushInterface.init 恢复，需要调用resumePush恢复。
* 极光推送所有的其他 API 调用都无效

##### 接口定义

    public static void stopPush(Context context);
    

##### 参数说明

* context 应用的 ApplicationContext

#### API - resumePush

恢复推送服务。

调用了此 API 后，极光推送完全恢复正常工作。

##### 接口定义

    public static void resumePush(Context context);
    

##### 参数说明

    context 应用的 ApplicationContext
    

#### API - isPushStopped

用来检查 Push Service 是否已经被停止

* SDK 1.5.2 以上版本支持。

##### 接口定义

    public static boolean isPushStopped(Context context);
    

#### 参数说明

* context 应用的 ApplicationContext

### 代码示例

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

* 接收到推送的自定义消息，则没有被处理
* 可以正常收到通知，用户点击打开应用主界面

### 接受广播

如果全部类型的广播都接收，则需要在 AndroidManifest.xml 里添加如下的配置信息：

每个 Receiver action 详细解释如下。

#### Action - cn.jpush.android.intent.REGISTRATION

SDK 向 JPush Server 注册所得到的注册 ID 。

一般来说，可不处理此广播信息。

要深入地集成极光推送，开发者想要自己保存App用户与JPush 用户关系时，则接受此广播，取得 Registration ID 并保存与App uid 的关系到开发者自己的应用服务器上。

使用极光推送提供的别名与标签功能，是更加简单轻便的绑定App用户与JPush用户的方式，请参考文档：别名与标签使用教程。

##### Intent 参数

* JPushInterface.EXTRA_REGISTRATION_ID


  * SDK 向 JPush Server 注册所得到的注册 全局唯一的 ID ，可以通过此 ID 向对应的客户端发送消息和通知。

    Bundle bundle = intent.getExtras();
    String title = bundle.getString(JPushInterface.EXTRA_REGISTRATION_ID);

#### Action - cn.jpush.android.intent.MESSAGE_RECEIVED

收到了自定义消息 Push 。

SDK 对自定义消息，只是传递，不会有任何界面上的展示。

如果开发者想推送自定义消息 Push，则需要在 AndroidManifest.xml 里配置此 Receiver action，并且在自己写的 BroadcastReceiver 里接收处理。

##### Intent 参数

* JPushInterface.EXTRA_TITLE


  * 保存服务器推送下来的消息的标题。
  * 对应 API 消息内容的 title 字段。
  * Portal 推送消息界上不作展示

    Bundle bundle = intent.getExtras();
    String title = bundle.getString(JPushInterface.EXTRA_TITLE);
* JPushInterface.EXTRA_MESSAGE


  * 保存服务器推送下来的消息内容。
  * 对应 API 消息内容的 message 字段。
  * 对应 Portal 推送消息界面上的"自定义消息内容”字段。

    Bundle bundle = intent.getExtras();
    String message = bundle.getString(JPushInterface.EXTRA_MESSAGE);
* JPushInterface.EXTRA_EXTRA


  * 保存服务器推送下来的附加字段。这是个 JSON 字符串。
  * 对应 API 消息内容的 extras 字段。
  * 对应 Portal 推送消息界面上的“可选设置”里的附加字段。

    Bundle bundle = intent.getExtras();
    String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);
* JPushInterface.EXTRA_CONTENT_TYPE


  * 保存服务器推送下来的内容类型。
  * 对应 API 消息内容的 content_type 字段。 

    Bundle bundle = intent.getExtras();
    String type = bundle.getString(JPushInterface.EXTRA_CONTENT_TYPE);
* JPushInterface.EXTRA_RICHPUSH_FILE_PATH


  * SDK 1.4.0 以上版本支持。
  * 富媒体通消息推送下载后的文件路径和文件名。

    Bundle bundle = intent.getExtras();
    String file = bundle.getString(JPushInterface.EXTRA_RICHPUSH_FILE_PATH);
* JPushInterface.EXTRA_MSG_ID


  * SDK 1.6.1 以上版本支持。
  * 唯一标识消息的 ID, 可用于上报统计等。

    Bundle bundle = intent.getExtras();
    String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

#### Action - cn.jpush.android.intent.NOTIFICATION_RECEIVED

收到了通知 Push。

> 如果通知的内容为空，则在通知栏上不会展示通知。但是，这个广播 Intent 还是会有。开发者可以取到通知内容外的其他信息。

##### Intent 参数

* JPushInterface.EXTRA_NOTIFICATION_TITLE


  * 保存服务器推送下来的通知的标题。
  * 对应 API 通知内容的 n_title 字段。
  * 对应 Portal 推送通知界面上的“通知标题”字段。

    Bundle bundle = intent.getExtras();         
    String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
* JPushInterface.EXTRA_ALERT


  * 保存服务器推送下来的通知内容。
  * 对应 API 通知内容的 n_content 字段。
  * 对应 Portal 推送通知界面上的“通知内容”字段。

    Bundle bundle = intent.getExtras();
    String content = bundle.getString(JPushInterface.EXTRA_ALERT);
* JPushInterface.EXTRA_EXTRA


  * SDK 1.2.9 以上版本支持。
  * 保存服务器推送下来的附加字段。这是个 JSON 字符串。
  * 对应 API 通知内容的 n_extras 字段。
  * 对应 Portal 推送消息界面上的“可选设置”里的附加字段。

    Bundle bundle = intent.getExtras();
    String extras = bundle.getString(JPushInterface.EXTRA_EXTRA);
* JPushInterface.EXTRA_NOTIFICATION_ID


  * SDK 1.3.5 以上版本支持。
  * 通知栏的Notification ID，可以用于清除Notification

    Bundle bundle = intent.getExtras();
    int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID);
* JPushInterface.EXTRA_CONTENT_TYPE


  * 保存服务器推送下来的内容类型。
  * 对应 API 消息内容的 content_type 字段。
  * Portal 上暂时未提供输入字段。

    Bundle bundle = intent.getExtras();
    String type = bundle.getString(JPushInterface.EXTRA_CONTENT_TYPE);
* JPushInterface.EXTRA_RICHPUSH_HTML_PATH


  * SDK 1.4.0 以上版本支持。
  * 富媒体通知推送下载的HTML的文件路径,用于展现WebView。

    Bundle bundle = intent.getExtras();
    String fileHtml = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_PATH);
* JPushInterface.EXTRA_RICHPUSH_HTML_RES


  * SDK 1.4.0 以上版本支持。
  * 富媒体通知推送下载的图片资源的文件名,多个文件名用 “，” 分开。 与 “JPushInterface.EXTRA_RICHPUSH_HTML_PATH” 位于同一个路径。

    Bundle bundle = intent.getExtras();
    String fileStr = bundle.getString(JPushInterface.EXTRA_RICHPUSH_HTML_RES);
    String[] fileNames = fileStr.spilt(",");
* JPushInterface.EXTRA_MSG_ID


  * SDK 1.6.1 以上版本支持。
  * 唯一标识通知消息的 ID, 可用于上报统计等。

    Bundle bundle = intent.getExtras();
    String file = bundle.getString(JPushInterface.EXTRA_MSG_ID);

#### Action - cn.jpush.android.intent.NOTIFICATION_OPENED

用户点击了通知。

一般情况下，用户不需要配置此 receiver action。

如果开发者在 AndroidManifest.xml 里未配置此 receiver action，那么，SDK 会默认打开应用程序的主 Activity，相当于用户点击桌面图标的效果。

如果开发者在 AndroidManifest.xml 里配置了此 receiver action，那么，当用户点击通知时，SDK 不会做动作。开发者应该在自己写的 BroadcastReceiver 类里处理，比如打开某 Activity 。

##### Intent 参数

* JPushInterface.EXTRA_NOTIFICATION_TITLE


  * 保存服务器推送下来的通知的标题。
  * 对应 API 通知内容的 n_title 字段。
  * 对应 Portal 推送通知界面上的“通知标题”字段。

    Bundle bundle = intent.getExtras();
    String title = bundle.getString(JPushInterface.EXTRA_NOTIFICATION_TITLE);
* JPushInterface.EXTRA_ALERT


  * 保存服务器推送下来的通知内容。
  * 对应 API 通知内容的n_content字段。
  * 对应 Portal 推送通知界面上的“通知内容”字段。

    Bundle bundle = intent.getExtras();
    String content = bundle.getString(JPushInterface.EXTRA_ALERT);
* JPushInterface.EXTRA_EXTRA 


  * SDK 1.2.9 以上版本支持。
  * 保存服务器推送下来的附加字段。这是个 JSON 字符串。
  * 对应 API 消息内容的 n_extras 字段。
  * 对应 Portal 推送消息界面上的“可选设置”里的附加字段。

    Bundle bundle = intent.getExtras();
    String type = bundle.getString(JPushInterface.EXTRA_EXTRA);
* JPushInterface.EXTRA_NOTIFICATION_ID


  * SDK 1.3.5 以上版本支持。
  * 通知栏的Notification ID，可以用于清除Notification

    Bundle bundle = intent.getExtras();
    int notificationId = bundle.getInt(JPushInterface.EXTRA_NOTIFICATION_ID
* JPushInterface.EXTRA_MSG_ID


  * SDK 1.6.1 以上版本支持。
  * 唯一标识调整消息的 ID, 可用于上报统计等。

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
                Log.d(TAG, "Unhandled intent - " + intent.getAcion());
      }
    }
    

## 别名与标签 API

### 功能说明

> 温馨提示，设置标签别名请注意处理call back结果。只有call back 返回值为 0 才设置成功，才可以向目标推送。否则服务器 API 会返回1011错误。

#### 别名 alias

为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。

每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，[服务器端API][0]会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用[服务器端API][0]发通知到客户端提醒用户。

#### 标签 tag

为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

不同应用程序、不同的用户，可以打同样的标签。

举例： game, old_page, women

### Method - setAliasAndTags (with Callback)

调用此 API 来同时设置别名与标签。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

#### 支持的版本

开始支持的版本：1.5.0.

#### 接口定义

    public static void setAliasAndTags(Context context, 
                                       String alias, 
                                       Set
    

[0]: ../../server_apis/server_sdks