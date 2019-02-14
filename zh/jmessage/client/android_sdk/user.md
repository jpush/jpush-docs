<h1>用户信息管理</h1>


## 概述

+ 开发者应用的用户，通过username / password 注册到 JMessage后，SDK 侧可以发起注册，服务器端也可发起批量注册。+ 用户登录 App，也同时登录 JMessage。登录后可以向其他 username 发聊天消息，也可以收到来自其他 username 或者群组的消息。+ 用户 A 是否有权限向用户 B 发消息，需由开发者的App 自己控制。+ 开发者可选择将用户头像等用户信息同步更新到 JMessage。


### 获取用户信息
异步从后台获取用户信息，此接口可用来获取不同[appkey](../../guideline/faq/#getappkey)下用户的信息,如果appKey为空，则默认获取当前[appkey](../../guideline/faq/#getappkey)下的用户信息。

```
JMessageClient.getUserInfo(String username, String appKey, GetUserInfoCallback callback);
```
  
参数说明

+ String username 用户名
+ String appKey 指定的appKey
+ GetUserInfoCallback callback 结果回调

### 获取当前登录账号的用户信息
此接口会直接从本地返回当前已经登录的用户的信息。

```
JMessageClient.getMyInfo();
```
参数说明

+ 无

返回

+ UserInfo  当前登录用户的用户信息。

### 更新用户信息
更新当前已登录用户的用户信息
```
JMessageClient.updateMyInfo(UserInfo.Field updateField, UserInfo info, BasicCallback callback);
```

参数说明

+ UserInfo.Field updateField 枚举类型，表示需要更新的用户信息字段。包括：

	  - nickname 昵称
	  - birthday 生日
	  - signature 签名
	  - gender 性别
	  - region 地区
	  - address 地址
	  - all 以上全部

+ UserInfo userInfo 待更新的用户信息（对象）。SDK将根据field参数来判断需要将哪个属性更新到服务器上去。
+ BasicCallback callback 结果回调

### 更新用户密码
更新当前已登录用户的密码
```
JMessageClient.updateUserPassword(String oldPassword, String newPassword, BasicCallback callback);
```

参数说明

+ String oldPassword 更新前密码
+ String newPassword 更新后密码
+ BasicCallback callback 结果回调

### 更新用户头像
更新当前已登录用户的头像
```
JMessageClient.updateUserAvatar(File avatar, BasicCallback callback);
```

参数说明

+ File avatar 用户头像文件
+ BasicCallback callback 结果回调



### 黑名单管理
可以将对方用户加入到“黑名单”列表中，加入之后，我方依然能给对方发消息，但是对方给我发消息时会返回指定错误码，发送消息失败。
#### 将用户加入黑名单
```
JMessageClient.addUsersToBlacklist(List<String> usernames, BasicCallback callback)
```
参数说明

+ List<String> usernames 被加入黑名单的用户username列表
+ BasicCallback callback 回调接口

#### 将用户移出黑名单
```
JMessageClient.delUsersFromBlacklist(List<String> usernames, BasicCallback callback)
```
参数说明

+ List<String> usernames 被移出黑名单的用户username列表
+ BasicCallback callback 回调接口

#### 获取被当前用户加入黑名单的用户列表
```
JMessageClient.getBlacklist(GetBlacklistCallback callback)
```
参数说明

+ GetBlacklistCallback 获取黑名单回调接口

回调
```
  public abstract void gotResult(int responseCode,
    String responseMessage, List<UserInfo> userInfos);
```
+ `List<UserInfo>` userInfos  被拉入黑名单的用户的UserInfo


### 通知栏管理
#### 设置通知展示类型
```
JMessageClient.setNotificationFlag(int flag);
```
参数说明

+ int flag  显示通知的模式,包括[FLAG_NOTIFY_WITH_SOUND](../im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_SOUND)、[FLAG_NOTIFY_WITH_VIBRATE](../im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_VIBRATE)、[FLAG_NOTIFY_WITH_LED](../im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_LED)等类型，支持使用 '|' 符号联结各个参数


#### 获取通知栏展示类型
***Since 2.2.0***

```
JMessageClient.getNotificationFlag();
```
返回

+ int 当前设置的通知栏的展示类型。

#### 通知栏点击事件监听
用户可以通过接受通知栏点击事件NotificationClickEvent，来实现自定义跳转，该事件如果没有接收者，点击通知栏时SDK将默认跳转到程序主界面。

事件接收方法见[事件处理](./event)一节


#### 进入单聊会话
UI层在进入聊天会话界面时调用，设置当前正在聊天的对象，调用此接口之后，收到对应用户发来的消息时，sdk不会弹出通知栏提示。  
同时还会清掉与该聊天对象会话的未读消息数，以及通知栏通知。  
此接口传入的数据采用覆盖逻辑，后面传入的参数会覆盖掉之前的设置。
```
JMessageClient.enterSingleConversation(String username,String appKey)
```
参数定义

  + String username 单聊聊天对象的username
  + String appKey 聊天对象所属appKey，若appkey为空则默认填充本应用的appkey

#### 进入群聊会话

UI层在进入聊天会话界面时调用，设置当前正在聊天的对象，调用此接口之后，收到对应群组中发来的消息时，sdk不会弹出通知栏提示。  
同时还会清掉与该聊天对象会话的未读消息数，以及通知栏通知。  
此接口传入的数据采用覆盖逻辑，后面传入的参数会覆盖掉之前的设置。

```
JMessageClient.enterGroupConversation(long groupID)
```

参数定义

  + long groupID 群聊聊天对象的群ID


#### 退出会话
退出会话。UI层在退出聊天会话界面时调用，清除当前正在聊天的对象，之后收到对应的用户或群组发来的消息时，会正常展示通知栏通知。
```
JMessageClient.exitConversation();
```



### <span id="Nodisturb">免打扰设置</span>
可以将用户/群组添加到“免打扰”列表中，收到免打扰用户/群组发过来的消息时，sdk不会弹出默认的通知提示，但[消息事件](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html)照常下发。

#### 获取免打扰列表
```
JMessageClient.getNoDisturblist(GetNoDisurbListCallback callback)
```
参数定义

+ GetNoDisurbListCallback callback 回调接口。
	
#### 设置普通免打扰

```
    /**
     * 将此用户设置为免打扰。
     *
     * @param noDisturb 1 -- 免打扰，其他 -- 非免打扰
     * @param callback  回调接口
     */
    public abstract void setNoDisturb(int noDisturb, BasicCallback callback);
    
```
具体见api doc中[UserInfo](../im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html)和[GroupInfo](../im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html)相关接口


#### 设置全局免打扰
设置全局免打扰之后，收到所有消息都将不会有通知栏通知，效果类似<br> `JMessageClient.setNotificationFlag(JMessageClient.FLAG_NOTIFY_DISABLE)`，但是此设置在用户换设备之后也会生效。

```
JMessageClient.setNoDisturbGlobal(int noDisturbGlobal, BasicCallback callback)
```
参数定义

+ int noDisturbGlobal 全局免打扰标志，1表示设置，其他表示取消设置。
+ BasicCallback callback 回调接口

#### 获取全局免打扰标识

```
JMessageClient.getNoDisturbGlobal(IntegerCallback callback)
```
参数定义

+ IntegerCallback callback 回调接口。

