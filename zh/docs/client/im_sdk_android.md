# IM SDK for Android

### 概述

JPush IM SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 Push SDK（只提供 Push 功能的 SDK）。

### Demo App

JPush IM SDK 提供一个完整的 Demo App，它就是一个 IM App。或者说，如果你的 App 需求只是 IM 功能，可以只做这样两个变更就是你自己的 IM App 了：1）换 Logo； 2）在 JPush Web 控制上注册应用，获取到的 Appkey 更新到 Demo App 里。


### 功能

#### 用户

开发者的用户，基于 username / password 注册到 JPush IM。

SDK 侧可以发起注册用户，也可由服务器端批量发起注册。

用户登录 App，也同时登录到 JPush IM。登录后，就可以向其他 username 发聊天消息。

用户 A 是否有权限向用户 B 发消息，由 App 逻辑自己控制。（由 JPush IM 提供好友关系时，JPush IM 会做控制）

可选让用户把头像等用户属性更新到 JPush IM。

#### 群组

可以把多个 username 加入到一个群组里，向群组发群聊消息。

#### 好友（还未提供）


### 基本概念

参考文档：[JPush IM 指南](../../guideline/jpush_im_guide)




### API 列表

#### 注册与登录

##### 注册

	public static void register(String username, String password, BasicCallback callback);
	
参数说明

+ username 用户名
+ password 用户密码
+ BasicCallback 结果回调

##### 登录

	public static void login(String username, String password, BasicCallback callback);
	
参数说明
 
+ username 用户名
+ password 用户密码
+ BasicCallback 结果回调

##### 退出登录

	public static void logout();
	
参数说明

无

#### 用户属性维护

##### 获取用户信息

	public static void getUserInfo(String username, GetUserInfoCallback callback);
	
参数说明

+ username 用户名
+ callback 结果回调

##### 更新用户信息

	public static void updateUserInfo(UserInfo info, BasicCallback callback);
	
参数说明

+ info 用户信息（对象）
+ callback 结果回调

#### 会话与发送消息

##### 发送消息

向服务器给发送对象发送消息，并且保存到本地会话。

	public static void sendMessage(Message message);
	
参数说明

+ message 消息（对象）

##### 获取会话列表

从本地数据库取得。同步返回。

	public java.util.List<Conversation> getConversationList();
	
参数说明

+ 无

返回说明

+ List<Conversation> 会话列表。暂未有分页。

#### 接收消息

SDK 从服务器端接收到消息，先会保存地本地数据库。然后以广播的形式通知 App。 App 需要注册一个 BroadcastReceiver，来处理 IM SDK 发出的消息。

+ action: JPushIMInterface.ACTION_RECEIVE_CONVERSATION_MESSAGE
+ extras: 
	* key: target_type 目标类型。单聊或者群聊。
	* key: target_id 目标ID。单聊则是 username，群聊则是 groupId。
	* key: msg_id

代码示例

```
MyMessageBroadcastReceiver msgReceiver = new MyMessageBroadcastReceiver (); 
IntentFilter intentFilter = new IntentFilter(JPushIMInterface.ACTION_RECEIVE_CONVERSATION_MESSAGE); 
IntentFilter.addCategory(context.getPackageName());
registerReceiver(msgReceiver, intentFilter);
 
private class MyMessageBroadcastReceiver extends BroadcastReceiver { 
    @Override
    public void onReceive(Context context, Intent intent) { 
        //消息id 
        String msgId = intent.getStringExtra("msg_id"); 
        //发消息的对象的id
        String target = intent.getStringExtra("target"); 
        //通过target和messageID拿到Message对象。
        Conversation conv = JPushIMInterface.getConversation(target);
        Message msg = conv.getMessage(msgId);
    } 
}
```


### 类定义

#### 聊天与消息

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

##### GetUserInfoCallback

```
public static abstract class GetUserInfoCallback extends BasicCallback {
    protected GetUserInfoCallback() {}

    protected GetUserInfoCallback(boolean isRunInUIThread) {
        super(isRunInUIThread);
    }

    public abstract void gotResult(int responseCode, String responseMessage, UserInfo info);

}

```


### 错误码定义



### 相关文档

+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [JPush IM 指南](../../guideline/jpush_im_guide/)
+ [JPush IM REST API](../../server/rest_api_im/)

