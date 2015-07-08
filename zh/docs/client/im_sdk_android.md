<h1>极光IM SDK - Android</h1>

+ [极光IM 客户端 DEMO 下载](../../resources_jmessage/)

### 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)


### 集成

JMessage SDK 是基于 JPush SDK 开发的，完整支持 JPush 推送的全部功能。所以 IM SDK 的集成，是在 Push SDK 的集成操作基础上，附加少量的步骤来完成。

如果您之前未集成 JPush SDK（推送SDK），请参考其集成文档：[JPush Android SDK 集成指南](../../guideline/android_guide/)

在上述文档基础上，需要如下几个集成操作：

1. 复制 IM SDK jar 包文件：jmessage-sdk-v1.X.X.jar
2. 修改 AndroidManifest.xml 文件
3. 代码初始化

以上步骤以下详述。

#### jar 包文件

把 JMessage SDK 的 jar 包文件，放到您的应用工程里 libs/ 目录下。文件名规格为：

    jmessage-sdk-android-1.0.8.jar

其中 1.0.8 为版本号。随着版本升级，这个版本号会变更。

如果您的应用之前集成过 JPush (推送) SDK，则需要删除原来的 jar 包文件。如果这 2 个文件同时存在，Android 编译器会报错。

#### 修改 AndroidManifest.xml 文件

基于 JPush SDK 文档里描述的需要增加的部分，JMessage SDK 需要多加如下的关于广播的配置项。

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="您自己的包名"
    android:versionCode="XX"
    android:versionName="XX">

<permission
        android:name="您自己的包名.permission.JPUSH_MESSAGE"
        android:protectionLevel="signature" />

<!--Required 一些系统要求的权限，如访问网络等-->
<uses-permission android:name="您自己的包名.permission.JPUSH_MESSAGE" />
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />

<!-- Required Push SDK核心功能-->
        <service
            android:name="cn.jpush.android.service.PushService"
            android:enabled="true"
            android:exported="false"
            android:process=":remote">
            <intent-filter>
                <action android:name="cn.jpush.android.intent.REGISTER" />
                <action android:name="cn.jpush.android.intent.REPORT" />
                <action android:name="cn.jpush.android.intent.PushService" />
                <action android:name="cn.jpush.android.intent.PUSH_TIME" />
            </intent-filter>
        </service>

<!-- Required Push SDK核心功能-->
        <receiver
            android:name="cn.jpush.android.service.PushReceiver"
            android:enabled="true">
            <intent-filter android:priority="1000">
                <action android:name="cn.jpush.android.intent.NOTIFICATION_RECEIVED_PROXY" />
                <category android:name="您自己的包名" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.USER_PRESENT" />
                <action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
            </intent-filter>
            <!-- Optional -->
            <intent-filter>
                <action android:name="android.intent.action.PACKAGE_ADDED" />
                <action android:name="android.intent.action.PACKAGE_REMOVED" />

                <data android:scheme="package" />
            </intent-filter>
        </receiver>

<!-- Required Push SDK核心功能 -->
        <activity
            android:name="cn.jpush.android.ui.PushActivity"
            android:configChanges="orientation|keyboardHidden"
            android:theme="@android:style/Theme.Translucent.NoTitleBar">
            <intent-filter>
                <action android:name="cn.jpush.android.ui.PushActivity" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="您自己的包名" />
            </intent-filter>
        </activity>
<!-- Required Push SDK核心功能 -->
        <service
            android:name="cn.jpush.android.service.DownloadService"
            android:enabled="true"
            android:exported="false" />
<!-- Required Push SDK核心功能 -->
        <receiver android:name="cn.jpush.android.service.AlarmReceiver" />

<!-- IM Required IM SDK核心功能-->
        <receiver
            android:name="cn.jpush.im.android.helpers.IMReceiver"
            android:enabled="true"
            android:exported="false">
            <intent-filter android:priority="1000">
                <action android:name="cn.jpush.im.android.action.IM_RESPONSE" />
                <action android:name="cn.jpush.im.android.action.NOTIFICATION_CLICK_PROXY" />

                <category android:name="您自己的包名" />
            </intent-filter>
        </receiver>

<!-- Required. Enable it you can get statistics data with channel -->
        <meta-data
            android:name="JPUSH_CHANNEL"
            android:value="developer-default" />
<!-- Required. AppKey copied from Portal -->
        <meta-data
            android:name="JPUSH_APPKEY"
            android:value="您的APPKey" />
```
其中 category 部分的包名，应改为您应用的包名。

#### 代码初始化

在应用的自定义 Application 的 onCreate 方法里，加上如下的代码段，来初始化 JMessage SDK。

```
@Override
public void onCreate() {
    super.onCreate();
    Log.i("JMessageDemoApplication", "Application onCreate");
   
    JMessageClient.init(getApplicationContext());
    JPushInterface.setDebugMode(true);
}
```

**JPushInterface.init 方法不可缺少**

上述代码，即在原 JPush SDK 初始化调 JPushInterface.init 位置，替换为 JMessageClient.ini 方法，其他一样。



### 功能

#### Demo App

极光 IM SDK 提供一个完整的 Demo App，它就是一个 IM App。或者说，如果你的 App 需求只是 IM 功能，可以只做这样两个变更就是你自己的 IM App 了：

+ 换 Logo； 
+ 在 JPush Web 控制台上注册应用，获取到的 Appkey 更新到 Demo App 里。


#### IM 混淆

+ 请下载4.x版本的[proguard.jar](http://sourceforge.net/projects/proguard/files/proguard/)， 并替换你Android Sdk "tools\proguard\lib\proguard.jar"

+ 在你的proguard.cfg加上代码：如果是使用新版本的ADT 将project.properties的中“# proguard.config=${sdk.dir}/tools/proguard/proguard-android.txt:proguard-project.txt”的“#”注释去掉，然后在proguard-android.txt中配置

```
-dontwarn cn.jpush.**
-keepattributes  EnclosingMethod,Signature
-keep class cn.jpush.** { *; }
-keepclassmembers class ** {
    public void onEvent*(**);
}

```
    
<br />



#### 消息

极光IM 最核心的功能是 IM 即时消息的功能。

- 保证消息及时下发；
- 单聊，群聊；
- 消息类型：文本、语音、图片；
- 用户未在线时保存离线消息；
- 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

#### 用户

开发者的用户，基于 username / password 注册到 JMessage。

SDK 侧可以发起注册用户，也可由服务器端批量发起注册。

用户登录 App，也同时登录到 JMessage。登录后，就可以向其他 username 发聊天消息，也可以收到来自其他 username 的消息，或者群组消息了。

用户 A 是否有权限向用户 B 发消息，由 App 逻辑自己控制。（由 JMessage 提供好友关系时，JMessage 会做控制）

可选让用户把头像等用户属性更新到 JMessage。

#### 群组

可以把多个 username 加入到一个群组里，向群组发群聊消息。

- 创建群组、退出群组；
- 加群组成员、移除群组成员；


#### 好友（还未提供）



### API 列表

以下列出主要的 JMessage SDK 提供的 API。完整的 API 与 类信息，请访问 [API Java docs](./im_android_api_docs).

#####SDK初始化
在调用IM其他接口前必须先调此接口初始化SDK，推荐在application类中调用。
```
public static synchronized void init(Context context)
```
参数说明

+ Context context 应用程序上下文对象。

#### 注册与登录

##### 注册

	public static void register(String username, String password, BasicCallback callback);
	
参数说明

+ String username 用户名
+ String password 用户密码
+ BasicCallback callback 结果回调

##### 登录

	public static void login(String username, String password, BasicCallback callback);
	
参数说明
 
+ String username 用户名
+ String password 用户密码
+ BasicCallback callback 结果回调

##### 退出登录

	public static void logout();
	
参数说明

- 无

#### 用户属性维护

##### 获取用户信息

	public static void getUserInfo(String username, GetUserInfoCallback callback);
	
参数说明

+ String username 用户名
+ GetUserInfoCallback callback 结果回调

回调

	public abstract void gotResult(int responseCode, String responseMessage, UserInfo userInfo);

+ UserInfo userInfo 用户信息

##### 从本地获取当前登录账号的用户信息
	public static UserInfo getMyInfo();
参数说明

- 无

返回

- UserInfo  当前登录用户的用户信息。

##### 更新用户信息

	public static void updateMyInfo(UserInfo.Field updateField, UserInfo info, BasicCallback callback);
	
参数说明

+ UserInfo.Field updateField 枚举类型，表示需要更新的用户信息字段。包括：
	+ nickname
	+ birthday
	+ signature
	+ gender
	+ region
+ UserInfo userInfo 待更新的用户信息（对象）。SDK将根据field参数来判断需要将哪个属性更新到服务器上去。
+ BasicCallback callback 结果回调

##### 更新用户密码

	public static void updateUserPassword(String oldPassword, String newPassword, BasicCallback callback);
	
参数说明

+ String oldPassword 更新前密码
+ String newPassword 更新后密码
+ BasicCallback callback 结果回调
	
##### 更新用户头像

	public static void updateUserAvatar(File avatar, BasicCallback callback);
	
参数说明

+ File avatar 用户头像文件
+ BasicCallback callback 结果回调


#### 会话与发送消息

##### 创建文字消息
```
 /**
  * 创建一条单聊文本消息
  *
  * @param username  聊天对象用户名
  * @param text  文本内容
  * @return 消息对象
  */
public static Message createSingleTextMessage(String username, String text)

 /**
  * 创建一条群聊文本信息
  *
  * @param groupID  群组的groupID
  * @param text  文本内容
  * @return  消息对象
  */
public static Message createGroupTextMessage(long groupID, String text)
```

#####创建图片消息
```
 /**
  * 创建一条单聊图片信息
  *
  * @param username  聊天对象的用户名
  * @param imageFile 图片文件
  * @return  消息对象
  * @throws FileNotFoundException
  */
public static Message createSingleImageMessage(String username, File imageFile)


 /**
  * 创建一条群聊图片信息
  *
  * @param groupID  群组的groupID
  * @param imageFile 图片文件
  * @return  消息对象
  * @throws FileNotFoundException
  */
public static Message createGroupImageMessage(long groupID, File imageFile)
```

##### 创建语音消息
```
 /**
  * 创建一条单聊语音信息
  *
  * @param username  聊天对象的用户名
  * @param voiceFile 语音文件
  * @param duration  语音文件时长
  * @return  消息对象
  * @throws FileNotFoundException
  */
public static Message createSingleVoiceMessage(String username, 
	File voiceFile, int duration) throws FileNotFoundException
	
 /**
  * 创建一条群聊语音信息
  *
  * @param groupID   群组groupID
  * @param voiceFile 语音文件
  * @param duration  语音文件时长
  * @return  消息对象
  * @throws FileNotFoundException
  */
public static Message createGroupVoiceMessage(long groupID, 
	File voiceFile, int duration) throws FileNotFoundException
```

##### 创建自定义消息
```
 /**
  * 创建一条单聊自定义消息
  *
  * @param username  聊天对象username
  * @param valuesMap 包含自定义键值对的map.
  * @return 消息对象
  */
public static Message createSingleCustomMessage(String username,
	 Map<? extends String, ?> valuesMap)

 /**
  * 创建一条群聊自定义消息
  *
  * @param groupID   群组groupID
  * @param valuesMap 包含了自定义键值对的map
  * @return  消息对象
  */
public static Message createGroupCustomMessage(long groupID, 
	Map<? extends String, ?> valuesMap)
```

##### 发送消息

向服务器给发送对象发送消息，并且保存到本地会话。

	public static void sendMessage(Message message);
	
参数说明

+ Message message 消息（对象）


##### 获取会话列表

从本地数据库取得。同步返回。

	public List<Conversation> getConversationList();
	
参数说明

+ 无

返回

+ `List<Conversation>` 会话列表。

##### 获取单个单聊会话

	public static Conversation getSingleConversation(String username);

参数说明

+ String username 目标的用户用户名。

返回

- 根据参数匹配得到的单聊会话对象。

##### 获取单个群聊会话

	public static Conversation getGroupConversation(long groupID);

参数说明

+ long groupID 目标的群的群ID。

返回

- 根据参数匹配得到的群聊会话对象。


	
##### 删除单个单聊会话
	
	public static boolean deleteSingleConversation(String username);

参数说明

+ String username 目标的用户用户名。

返回

- 是否删除成功。

##### 删除单个群聊会话
	
	public static boolean deleteGroupConversation(long groupID);

参数说明

+ long groupID 目标群的群ID。

返回

- 是否删除成功。


#### 事件处理
##### 1、事件接收类的注册
	public static void registerEventReceiver(Object receiver);
	public static void registerEventReceiver(Object receiver, int priority);

参数说明

+ Object receiver 消息接收类对象
+ int priority 定义事件接收者接收事件的优先级，默认值为0，优先级越高将越先接收到事件。（优先级只对同一个线程模式中的接收者有效）

##### 2、事件接收类的解绑
	public static void unRegisterEventReceiver(Object receiver);

参数说明

+ Object receiver 消息接收类对象，对象解绑之后将不再接收到任何event。

##### 3、事件接收
注册事件接收类之后，需要在消息接收类中实现如下方法来接收对应消息。sdk将根据实现方法的方法名来区分不同的线程模式，常用的线程模式有onEvent(默认线程模式)和onEventMainThread(主线程模式)两种。

可以通过定义不同类型的参数，来接收不同种类的事件。具体事件类型定义见 “事件类型” 一节

###### 默认线程（子线程）模式
```
public void onEvent(EventEntity event){
	//do your own business
}
```
方法体将在默认线程（子线程）中被调用， 可以用来处理耗时操作。

参数定义

+ EventEntity event 事件对象。（ 定义不同类型参数可以接收不同种类事件，具体用法可以参考“示例代码“。）

###### 主线程模式
```
public void onEventMainThread(EventEntity event){
	//do your own business
}
```
方法体将在主线程中被调用，可以用来刷新UI。
参数定义

+ EventEntity event 事件对象。

##### 4、事件类型

消息事件实体类 MessageEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th style="padding: 0 5px; " width="20px">方法</th>
      <th style="padding: 0 5px; " width="40px">类型</th>
      <th style="padding: 0 5px; " width="300px">说明</th>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >getMessage()</td>
      <td style="padding: 0 5px; " >Message</td>
      <td style="padding: 0 5px; " >获取消息对象</td>
    </tr>
  </table>
</div>

</br>


会话刷新事件实体类 ConversationRefreshEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th style="padding: 0 5px; " width="10px">方法</th>
      <th style="padding: 0 5px; " width="20px">类型</th>
      <th style="padding: 0 5px; " width="370px">说明</th>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >getConversation()</td>
      <td style="padding: 0 5px; " >Conversation</td>
      <td style="padding: 0 5px; " >获取需要被刷新的会话对象</td>
    </tr>
  </table>
</div>

</br>

通知栏点击事件实体类NotificationClickEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th style="padding: 0 5px; " width="30px">方法</th>
      <th style="padding: 0 5px; " width="20px">类型</th>
      <th style="padding: 0 5px; " width="300px">说明</th>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >getMessage()</td>
      <td style="padding: 0 5px; " >Message</td>
      <td style="padding: 0 5px; " >获取点击的通知所对应的消息对象</td>
    </tr>
  </table>
</div>

</br>



#####5、示例代码
接收消息事件
```Java
class MessageEventReceiver extends Activity{
 
  @Override
  protected void onCreate() {
    super.onCreate(savedInstanceState);
    JMessageClient.registerEventReceiver(this);
  }
 
  @Override
  protected void onDestroy() {
    JMessageClient.unRegisterEventReceiver(this);
    super.onDestroy();
  }
 
  public void onEvent(MessageEvent event){
    Message msg = event.getMessage();
 
    switch (msg.getContentType()){
            case text:
                //处理文字消息
                TextContent textContent = (TextContent) msg.getContent();
                textContent.getText();
                break;
            case image:
                //处理图片消息
                ImageContent imageContent = (ImageContent) msg.getContent();
                imageContent.getLocalPath();//图片本地地址
                imageContent.getLocalThumbnailPath();//图片对应缩略图的本地地址
                break;
            case voice:
                //处理语音消息
                VoiceContent voiceContent = (VoiceContent) msg.getContent();
                voiceContent.getLocalPath();//语音文件本地地址
                voiceContent.getDuration();//语音文件时长
                break;
            case custom:
                //处理自定义消息
                CustomContent customContent = (CustomContent) msg.getContent();
                customContent.getValue("attr1");
                customContent.getValue("attr2");
                customContent.getAllValues();
                break;
            case eventNotification:
                //处理事件提醒消息
                EventNotificationContent eventNotificationContent  =
                        (EventNotificationContent)msg.getContent();
                switch (eventNotificationContent.getEventNotificationType()){
                    case group_member_added:
                        //群成员加群事件
                        break;
                    case group_member_removed:
                        //群成员被踢事件
                        break;
                    case group_member_exit:
                        //群成员退群事件
                        break;
                }
                break;
        }
  }
 }
```

接收通知栏点击事件
```Java
class NotificationClickEvent extends Activity{
    @Override
    protected void onCreate() {
        super.onCreate(savedInstanceState);
        JMessageClient.registerEventReceiver(this);
    }
    @Override
    protected void onDestroy() {
        JMessageClient.unRegisterEventReceiver(this);
        super.onDestroy();
    }
    public void onEvent(NotificationClickEvent event){
        Intent notificationIntent = new Intent(mContext, ChatActivity.class);
        mContext.startActivity(notificationIntent);//自定义跳转到指定页面
    }
  
}
```



#### 群组维护

##### 创建群组

	public static void createGroup(String groupName, String groupDesc, CreateGroupCallback callback);
	
参数说明 

+ String groupName 群名称
+ String groupDesc 群描述
+ CreateGroupCallback callback 结果回调

回调

	public abstract void gotResult(int responseCode, String responseMsg, long groupId);
	
+ long groupId 新创建成功的群组ID（resopnseCode = 0 时）。

##### 获取群组列表
```
public static void getGroupIDList(GetGroupListCallback callback)
```
回调
```
public abstract void gotResult(int responseCode, String responseMessage,
            List<Long> groupIDList)
```
+ `List<Long>` groupIDList  当前用户所加入的群组的groupID的list


##### 获取群组详情

	public static void getGroupInfo(long groupId, GetGroupInfoCallback callback)

参数说明

+ long groupId 群ID
+ GetGroupInfoCallback callback 结果回调

回调

	public void gotResult(int responseCode, String responseMessage, Group group)

+ Group group 返回的群组详情

##### 更新群组名称

	public static void updateGroupName(long groupID, 
			String groupName,BasicCallback callback);

参数说明

+ long groupID 待更新信息的群组ID
+ String groupName 新的名称
+ BasicCallback callback 结果回调

##### 更新群组详情

	public static void updateGroupDescription(long groupID, 
			String groupDesc,BasicCallback callback);

参数说明

+ long groupID 待更新信息的群组ID
+ String groupName 新的群组详情描述
+ BasicCallback callback 结果回调


##### 加群组成员

	public static void addGroupMembers(long groupId, List<String> usernameList, BasicCallback callback);
	
参数说明

+ long groupId 待加群的群组ID。创建群组时返回的。
+ List usernameList 群组成员列表，使用成员 username。
+ BasicCallback callback 结果回调

##### 移除群组成员

	public static void removeGroupMembers(long groupId, List<String> usernameList, BasicCallback callback);

参数说明

+ long groupId 待删除成员的群ID。
+ List usernameList 待删除的成员列表。
+ BasicCallback callback 结果回调。

##### 退出群组

	public static void exitGroup(long groupId, BasicCallback callback);

参数说明

+ long groupId 待退出的群ID。
+ BasicCallback callback 结果回调。
	
##### 获取群组成员列表

	public static void getGroupMembers(long groupID, 
			GetGroupMembersCallback callback)

参数说明

+ long groupId 群组ID
+ GetGroupMembersCallback callback

回调

	public void gotResult(int responseCode, String responseMessage, List<String> members);
	
+ List members 成员列表(username)。


#### 通知栏相关
##### 设置通知展示类型
```
public static void setNotificationMode(int mode);
```
参数说明

+ int mode  
    + 显示通知的模式

+ JMessageClient.NOTI_MODE_DEFAULT  
    + 显示通知，有声音，有震动。 

+ JMessageClient.NOTI_MODE_NO_SOUND 
    + 显示通知，无声音，有震动。

+ JMessageClient.NOTI_MODE_NO_VIBRATE 
    + 显示通知，有声音，无震动。

+ JMessageClient.NOTI_MODE_SILENCE 
    + 显示通知，无声音，无震动。

+ JMessageClient.NOTI_MODE_NO_NOTIFICATION 
    + 不显示通知。


##### 进入单聊回话
进入单聊会话。UI在进入单聊会话页面时需要调用此函数，SDK会根据传入的username来决定是否需要发送通知

```
public static void enterSingleConversaion(String username)
```
参数定义

  + String username 单聊聊天对象的username

##### 进入群聊会话

进入群聊会话。UI在进入群聊会话页面时需要调用此函数，SDK会根据传入的groupID来决定是否需要发送通知

```
public static void enterGroupConversation(long groupID)
```

参数定义

  + long groupID 群聊聊天对象的群ID


##### 退出会话
退出会话。UI在退出会话页面时需要调用此函数。
```
public static void exitConversaion();
```
##### 通知栏点击事件监听
用户可以通过接受通知栏点击事件NotificationClickEvent，来实现自定义跳转，该事件如果没有接收者，点击通知栏时SDK将默认跳转到程序主界面。

事件接收方法见"事件处理"一节

### 类定义

#### 会话与消息

```
cn.jpush.im.android.api.model.Conversation

public File getAvatar();
public String getDisplayName();
public Message getLatestMessage();
public List<Message> getAllMessage();
public List<Message> getNewMessagesFromNewest(int offset, int limit);

public Message createSendMessage(MessageContent content);
public Message createSendTextMessage(String text);
public Message createSendImageMessage(File imageFile) 
		throws FileNotFoundException
public Message createSendVoiceMessage(File voiceFile, int duration) 
		throws FileNotFoundException
public Message createSendCustomMessage(Map<? extends String, ?> valuesMap)
public boolean resetUnreadCount();


```

```
cn.jpush.im.android.api.model.Message

public String getFromID()
public MessageContent getContent()
public ContentType getContentType()
public MessageStatus getStatus()
public String getTargetID()
public long getCreateTime()

public void setOnContentUploadProgressCallback(ProgressUpdateCallback callback)
public void setOnContentDownloadProgressCallback(ProgressUpdateCallback callback)
public void setOnSendCompleteCallback(BasicCallback sendCompleteCallback)

```

使用举例

```
Conversation conv = JMessageClient.getSingleConversation("tom");

TextContent text = new TextContent("Hi, JMessage!");
Message message = conv.createSendMessage(text);

JMessageClient.sendMessage(message);
```

#### 聊天内容

聊天内容父类

    cn.jpush.im.api.content.MessageContent

当前支持的聊天内容类型

```
cn.jpush.im.api.content.TextContent
cn.jpush.im.api.content.VoiceContent
cn.jpush.im.api.content.ImageContent
cn.jpush.im.api.content.CustomContent
```

使用举例

```
// 参数：文本内容
TextContent text = new TextContent("Hi, JMessage");

// 参数：语音文件的路径，语音文件时长
VoiceContent voice = new VoiceContent("/sdcard/voice.amr", 21);

// 参数：图片文件路径
ImageContent image = new ImageContent("/sdcard/image.amr");
```

#### 回调定义

##### BasicCallback

```
public abstract class BasicCallback {

    private boolean isRunInUIThread = true;

    /**
     * Default is running in UI thread.
     */
    public BasicCallback() {
    }

    public BasicCallback(boolean isRunInUIThread) {
        this.isRunInUIThread = isRunInUIThread;
    }

    public boolean isRunInUIThread() {
        return this.isRunInUIThread;
    }

    /**
     * 异步调用返回结果。
     *
     * @param responseCode 0 表示正常。大于 0 表示异常，responseMessage 会有进一步的异常信息。
     * @param responseMessage 一般异常时会有进一步的信息提示。
     */
    public abstract void gotResult(int responseCode, String responseMessage);

}

```

### 错误码定义

参考文档：[IM 错误码列表](../im_errorcode)



### 相关文档
+ [JPush Android SDK 集成指南](../../guideline/android_guide/)
+ [JPush Android SDK 概述](../../client/android_sdk/)
+ [极光IM指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM 业务对象](../../advanced/im_objects/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [IM REST API](../../server/rest_api_im/)

