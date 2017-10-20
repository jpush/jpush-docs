<h1>Android SDK 开发指南</h1>


## 概述

极光 IM（英文名JMessage）为开发者提供易用可靠的 IM 开发框架，开发者可集成SDK，快速实现即时通讯功能。SDK 支持Android 2.3或以上版本的手机系统。  
要了解极光 IM 的详细信息，请参考文档：[JMessage 产品简介](https://docs.jiguang.cn/jmessage/guideline/jmessage_guide/)

### 消息

极光 IM 最核心的功能是即时通讯功能。

- 保证消息及时下发；
- 单聊，群聊；
- 消息类型：文本、语音、图片、文件、位置等；
- 用户未在线时保存离线消息；
- 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

### 用户

- 开发者的用户，基于 username / password 注册到 JMessage，SDK 侧可以发起注册用户，也可由服务器端批量发起注册。

- 用户登录 App，也同时登录到 JMessage，登录后，就可以向其他 username 发聊天消息，也可以收到来自其他 username 的消息，或者群组消息了。用户 A 是否有权限向用户 B 发消息，由 App 逻辑自己控制。

- 可选让用户把头像等用户属性更新到 JMessage。

### 群组

可以把多个 username 加入到一个群组里，向群组发群聊消息。

- 创建群组、退出群组；
- 加群组成员、移除群组成员；


### 好友
+ jmessage android sdk 从1.4.0版本开始提供接口实现对用户好友关系的托管，以及相关好友请求的发送和接收。

<font color= SteelBlue>说明：除此之外的任何建立在好友关系之上的功能（如仅限于好友之间才能进行的聊天等），需要开发者的应用层自己实现。</font>

### 字符串规范
此处定义JMessage产品里字段属性与规范，用于校验与规范化。  

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >字符说明</th>
			<th >长度限制</th>
		</tr>
		<tr >
			<td>app_key</td>
			<td>由 JPush Web Portal 生成的 24位字符串。字母或者数字，不区分大小写</td>
			<td></td>
		</tr>
		<tr >
			<td>username</td>
			<td>以字母或者数字开头。支持字母、数字、下划线、英文点、减号、 @。</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>password</td>
			<td>不限</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>group_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>nickname</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>note_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>other</td>
			<td>其他未明确指定的 String 类型字段，都按照这个处理。  
支持字符：全部</td>
			<td>Byte(0~250)</td>
		</tr>
	</table>
</div>

## API 列表

以下列出主要的 JMessage SDK 提供的 API。完整的 API 与 类信息，请访问：<a href="../im_android_api_docs/" target="_blank">API Java docs</a>

###SDK初始化

在调用IM其他接口前必须先调此接口初始化SDK，推荐在application类中调用。默认关闭消息漫游。
```
JMessageClient.init(Context context)
```

参数说明

+ Context context 应用程序上下文对象。

### SDK初始化(设置消息记录漫游)
***Since 2.1.0***  
SDK初始化,同时指定是否启用消息记录漫游。  
打开消息漫游之后，用户多个设备之间登录时，sdk会自动将当前登录用户的历史消息同步到本地，同步完成之后sdk会发送一个`ConversationRefreshEvent`事件通知上层刷新，具体事件处理方法见[事件处理](#Event)一节。

```
JMessageClient.init(Context context, boolean msgRoaming)
```
参数说明

+ Context context 应用程序上下文对象。
+ boolean msgRoaming 是否启用消息漫游，true - 启用，false - 关闭。 


### 注册与登录

#### 注册
```
JMessageClient.register(String username, String password, BasicCallback callback);

/**
 * 注册同时指定用户信息中的其他字段
 * @since 2.3.0
 */
JMessageClient.register(String userName, String password, RegisterOptionalUserInfo optionalUserInfo, BasicCallback callback);
```

参数说明

+ String username 用户名
+ String password 用户密码
+ RegisterOptionalUserInfo optionalUserInfo 注册时的用户其他信息
+ BasicCallback callback 结果回调


#### 登录
```
JMessageClient.login(String username, String password, BasicCallback callback);
```

参数说明

+ String username 用户名
+ String password 用户密码
+ BasicCallback callback 结果回调

#### 退出登录
```
JMessageClient.logout();
```

### 多端同时在线
SDK从2.3.0版本开始支持多端同时在线，具体规则见[多端在线说明](../guideline/faq/#_5)


### 用户属性维护

#### 获取用户信息
```
JMessageClient.getUserInfo(String username, GetUserInfoCallback callback);
```

参数说明

+ String username 用户名
+ GetUserInfoCallback callback 结果回调

回调

```
JMessageClient.gotResult(int responseCode, String responseMessage, UserInfo userInfo);
```

+ UserInfo userInfo 用户信息

#### 获取用户信息(跨应用)
获取用户信息，此接口可用来获取不同appKey下用户的信息,如果appKey为空，则默认获取当前appKey下的用户信息。

```
JMessageClient.getUserInfo(String username, String appKey, GetUserInfoCallback callback);
```
  
参数说明

+ String username 用户名
+ String appKey 指定的appKey
+ GetUserInfoCallback callback 结果回调

#### 从本地获取当前登录账号的用户信息
```
JMessageClient.getMyInfo();
```
参数说明

+ 无

返回

+ UserInfo  当前登录用户的用户信息。

#### 更新用户信息
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

#### 更新用户密码
```
JMessageClient.updateUserPassword(String oldPassword, String newPassword, BasicCallback callback);
```

参数说明

+ String oldPassword 更新前密码
+ String newPassword 更新后密码
+ BasicCallback callback 结果回调

#### 更新用户头像
```
JMessageClient.updateUserAvatar(File avatar, BasicCallback callback);
```

参数说明

+ File avatar 用户头像文件
+ BasicCallback callback 结果回调


### 本地会话管理

#### 创建单聊会话
创建单聊会话，如果本地已存在对应会话，则不会重新创建，直接返回本地会话对象。通过指定appkey，可以实现给其他appkey下的用户发消息。

```
	Conversation.createSingleConversation(String username, String appkey)
```
参数说明

+ String username 会话对象的username.
+ String appkey 用户所属应用的appkey,如果填空则默认为本应用的appkey

#### 创建群聊会话
创建群聊会话，如果本地已存在对应会话对象，则不会重新创建，直接返回本地会话对象。

```
	Conversation.createGroupConversation(long groupID)
```
参数说明

+ long groupID 会话对象群组的groupID

#### 获取会话列表

从本地数据库中获取会话列表，默认按照会话的最后一条消息的时间，降序排列
```
JMessageClient.getConversationList();
```
参数说明

+ 无

返回

+ `List<Conversation>` 会话列表。

#### 获取单个单聊会话
获取与指定appkey下username的单聊会话信息,如果appkey为空则默认取本应用appkey下对应username用户的会话。
```
JMessageClient.getSingleConversation(String username, String appkey);
```
参数说明

+ String username 目标的用户用户名。
+ String appkey 用户所属应用的appkey

返回

+ Conversation 根据参数匹配得到的单聊会话对象。


#### 获取单个群聊会话
```
JMessageClient.getGroupConversation(long groupID);
```

参数说明

+ long groupID 目标的群的群ID。

返回

+ Conversation 根据参数匹配得到的群聊会话对象。



#### 删除单个单聊会话
删除与指定appkey下username的单聊的会话，同时删除掉本地聊天记录。,如果appkey为空则默认尝试删除本应用appkey下对应username的会话。
```  
JMessageClient.deleteSingleConversation(String username, String appkey);
```

参数说明

+ String username 目标的用户用户名。
+ String appkey 用户所属应用的appkey

返回

+ boolean 是否删除成功。


#### 删除单个群聊会话
```  
JMessageClient.deleteGroupConversation(long groupID);
```
参数说明

+ long groupID 目标群的群ID。

返回

+ boolean 是否删除成功。

#### 获取单个会话未读消息数
```
conversation.getUnReadMsgCnt();
```
返回

+ int 当前会话的未读消息数

#### 重置单个会话未读消息数
```
conversation.resetUnreadCount();
```
返回

+ boolean true表示重置成功，其他情况下返回false.

#### 手动设置会话未读消息数
```
conversation.setUnReadMessageCnt(int count);
```
参数说明

+ int count 指定的未读消息数

返回

+ boolean true表示设置成功，其他情况下返回false.

#### 获取所有会话未读消息总数
```
JMessageClient.getAllUnReadMsgCount();
```
返回

+ int 当前用户所有会话的未读消息总数


### 消息管理

#### 创建文字消息
```
 	/**
     * 创建一条单聊文本消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param username 聊天对象用户名
     * @param appKey   聊天对象所属应用的appKey
     * @param text     文本内容
     * @return 消息对象
     */
	JMessageClient.createSingleTextMessage(String username, String appKey, String text)

    /**
     * 创建一条群聊文本信息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupID 群组的groupID
     * @param text    文本内容
     * @return 消息对象
     */
    JMessageClient.createGroupTextMessage(long groupID, String text)
```

#### 创建图片消息
```
    /**
     * 创建一条单聊图片信息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param username  聊天对象的用户名
     * @param appKey    聊天对象所属应用的appKey
     * @param imageFile 图片文件
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createSingleImageMessage(String username, String appKey, File imageFile) throws FileNotFoundException

    /**
     * 创建一条群聊图片信息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupID   群组的groupID
     * @param imageFile 图片文件
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createGroupImageMessage(long groupID, File imageFile) throws FileNotFoundException
```

#### 创建语音消息
```
    /**
     * 创建一条单聊语音信息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param username  聊天对象的用户名
     * @param appKey    聊天对象所属应用的appKey
     * @param voiceFile 语音文件
     * @param duration  语音文件时长
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createSingleVoiceMessage(String username, String appKey, File voiceFile, int duration) throws FileNotFoundException

    /**
     * 创建一条群聊语音信息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupID   群组groupID
     * @param voiceFile 语音文件
     * @param duration  语音文件时长
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createGroupVoiceMessage(long groupID, File voiceFile, int duration) throws FileNotFoundException
```

#### 创建位置消息

```
    /**
     * 创建一条单聊地理位置消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param username  聊天对象的用户名
     * @param appKey    聊天对象所属应用的appKey
     * @param latitude  纬度信息
     * @param longitude 经度信息
     * @param scale     地图缩放比例
     * @param address   详细地址信息
     * @return 消息对象
     */
    JMessageClient.createSingleLocationMessage(String username, String appKey, double latitude, double longitude, int scale, String address)

    /**
     * 创建一条群聊地理位置消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupId   群组groupID
     * @param latitude  纬度信息
     * @param longitude 经度信息
     * @param scale     地图缩放比例
     * @param address   详细地址信息
     * @return 消息对象
     */
    JMessageClient.createGroupLocationMessage(long groupId, double latitude, double longitude, int scale, String address)
```

#### 创建文件消息

```
	/**
     * 创建一条单聊file消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param userName 聊天对象的用户名
     * @param appKey   聊天对象所属应用的appKey
     * @param file     发送的文件
     * @param fileName 指定发送的文件名称,如果不填或为空，则默认使用文件原名。
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createSingleFileMessage(String userName, String appKey, File file, String fileName) throws FileNotFoundException, JMFileSizeExceedException

    /**
     * 创建一条群聊file消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupID  群组groupID
     * @param file     发送的文件
     * @param fileName 指定发送的文件名称,如果不填或为空，则默认使用文件原名。
     * @return 消息对象
     * @throws FileNotFoundException
     */
    JMessageClient.createGroupFileMessage(long groupID, File file, String fileName) throws FileNotFoundException, JMFileSizeExceedException
```

#### 创建自定义消息
```
 /**
     * 创建一条单聊自定义消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param username  聊天对象username
     * @param appKey    聊天对象所属应用的appKey
     * @param valuesMap 包含自定义键值对的map.
     * @return 消息对象
     */
JMessageClient.createSingleCustomMessage(String username, String appKey, Map<? extends String, ? extends String> valuesMap)

 /**
  * 创建一条群聊自定义消息
  *
  * @param groupID   群组groupID
  * @param valuesMap 包含了自定义键值对的map
  * @return  消息对象
  */
JMessageClient.createGroupCustomMessage(long groupID,
  Map<? extends String, ?> valuesMap)
```

#### 消息发送结果监听
消息发送完成后，会回调这里的接口通知上层。
```
message.setOnSendCompleteCallback(BasicCallback sendCompleteCallback)
```
参数说明

+ BasicCallback sendCompleteCallback 回调接口

#### 消息发送

向服务器给发送对象发送消息，并且保存到本地会话。使用默认的配置参数发送
```
JMessageClient.sendMessage(Message message);
```
参数说明

+ Message message 消息对象

#### 附带控制参数的消息发送
***Since 2.2.0***  
针对此次消息发送操作，支持一些可选参数的配置，具体参数见[MessageSendingOptions](./im_android_api_docs/cn/jpush/im/android/api/options/MessageSendingOptions.html)

```
JMessageClient.sendMessage(Message message, MessageSendingOptions options);
```
参数说明

+ Message message 消息对象
+ MessageSendingOptions options 消息发送时的控制选项。

##### 代码示例
```
Message message = mConversation.createSendMessage(new TextContent(“Hello jmessage.”));
message.setOnSendCompleteCallback(new BasicCallback() {
    @Override
    public void gotResult(int responseCode, String responseDesc) {
        if (responseCode == 0) {
            //消息发送成功
        } else {
            //消息发送失败
        }
    }
});

MessageSendingOptions options = new MessageSendingOptions();
options.setRetainOffline(false);

JMessageClient.sendMessage(message);//使用默认控制参数发送消息
//JMessageClient.sendMessage(message,options);//使用自定义的控制参数发送消息
```

#### 本地消息记录获取
任何的消息都从属某一会话，所以要获取本地消息记录，首先需要获取到会话对象`conversation`,进而获取该会话下的消息记录。

**获取会话中所有消息**

```
	/**
     * 获取会话中所有消息，消息按照时间升序排列.<br/>
     *
     * @return 包含会话中所有消息的List
     */
	conversation.getAllMessage();
```


**按条件获取消息列表**

```
	/**
     * 会话中消息按时间降序排列，从其中的offset位置，获取limit条数的消息.
     *
     * @param offset 获取消息的起始位置
     * @param limit  获取消息的条数
     * @return 符合查询条件的消息List, 如果查询失败则返回空的List。
     */
	conversation.getMessagesFromNewest(int offset, int limit)
	
	/**
     * 会话中消息按时间升序排列，从其中的offset位置，获取limit条数的消息.<br/>
     *
     * @param offset 获取消息的起始位置
     * @param limit  获取消息的条数
     * @return 符合查询条件的消息List, 如果查询失败则返回空的List。
     */
    conversation.getMessagesFromOldest(int offset, int limit);
```


#### 接收消息
sdk收到消息时，会上抛消息事件[MessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) 或 [OfflineMessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html)，开发者可以通过这个事件来拿到具体的Message对象，进而执行UI刷新或者其他相关逻辑。具体事件处理方法见[事件处理](#Event)一节


### 从2.1.0版本开始接收消息的变化
2.1.0版本开始，sdk将消息下发分为在线下发和离线下发两种类型。 先明确两个概念：

+ 在线消息：im用户在线期间，所有收到的消息称为在线消息。
+ 离线消息：im用户离线期间（包括登出或者网络断开）所产生的消息，会暂存在极光服务器上。当用户再次上线，sdk会将这部分消息拉取下来，这部分消息就称为离线消息。

有了这两个概念的区分之后，sdk对于这两种消息的处理方式也有了不同：  


版本 | 在线消息 | 离线消息 
--- | ------- | ------
2.1.0之前 | 每收到一条消息上抛一个[MessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) | 和在线消息一样，有多少条离线消息就上抛多少个[MessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank)|
2.1.0开始 | 每收到一条消息上抛一个[MessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) | 以会话为单位，该会话如果有离线消息，sdk就会上抛一个[OfflineMessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html)。就算同会话中有多条离线消息，sdk也只会上抛一个[OfflineMessageEvent](./im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html),这个Event中就包含了所有离线消息的相关信息。这样会大大减轻上层处理事件的压力。



**总结**  

sdk升级到2.1.0版本（或以上）后，上层需要针对消息接收的处理做以下变动：

+ 除了`MessageEvent`之外，新增一个事件类型`OfflineMessageEvent`的接收,用来接收离线消息事件。
+ 对于需要消息漫游的开发者，还需增加`ConversationRefreshEvent`事件的接收，当会话中的漫游消息同步完成后，sdk会触发此事件通知上层刷新会话。


**代码示例：**

```
    /**
      类似MessageEvent事件的接收，上层在需要的地方增加OfflineMessageEvent事件的接收
      即可实现离线消息的接收。
    **/
    public void onEvent(OfflineMessageEvent event) {
        //获取事件发生的会话对象
        Conversation conversation = event.getConversation();
        List<Message> newMessageList = event.getOfflineMessageList();//获取此次离线期间会话收到的新消息列表
        System.out.println(String.format(Locale.SIMPLIFIED_CHINESE, "收到%d条来自%s的离线消息。\n", newMessageList.size(), conversation.getTargetId()));
    }


    /**
      如果在JMessageClient.init时启用了消息漫游功能，则每当一个会话的漫游消息同步完成时
      sdk会发送此事件通知上层。
    **/
    public void onEvent(ConversationRefreshEvent event) {
        //获取事件发生的会话对象
        Conversation conversation = event.getConversation();
        //获取事件发生的原因，对于漫游完成触发的事件，此处的reason应该是
        //MSG_ROAMING_COMPLETE
        ConversationRefreshEvent.Reason reason = event.getReason();
        System.out.println(String.format(Locale.SIMPLIFIED_CHINESE, "收到ConversationRefreshEvent事件,待刷新的会话是%s.\n", conversation.getTargetId()));
        System.out.println("事件发生的原因 : " + reason);
    }
```


### 消息撤回

#### 撤回会话中某条消息
***Since 2.2.0***  
由消息发送方发起调用

```
	conversation.retractMessage(Message message, BasicCallback callback)
```

参数说明

+ Message message 需要被撤回的消息的消息实体
+ BasicCallback callback 回调接口

#### 被撤回方事件通知
***Since 2.2.0***  
消息发送方发起撤回后，被撤回方会收到一条事件通知[MessageRetractEvent](./im_android_api_docs/cn/jpush/im/android/api/event/MessageRetractEvent.html)，具体事件处理方式见[事件处理](#Event)一节


**注意：** 无论是撤回方还是被撤回方，消息被撤回后，对应message content会被替换为[PromtContent](./im_android_api_docs/cn/jpush/im/android/api/content/PromptContent.html)类型，消息之前内容变成不可见。

### 消息已读回执

#### 已读回执设置
消息发送方可以在发送消息时，针对单条消息设置是否需要接收方发送已读回执。默认行为为false  
***Since 2.3.0***  

```
	messageSendingOptions.setNeedReadReceipt(boolean needReadReceipt)
```

参数说明

+ boolean needReadReceipt 是否需要接收方发送已读回执. true - 是,false - 否.

#### 获取当前未发送已读回执的人数
当一条需要接收方发送已读回执的消息成功发出之后，消息发送方可以查看这条消息当前尚未发送已读回执的人数.  
***Since 2.3.0***  

```
	message.getUnreceiptCnt()
```

接口返回

+ int 当前尚未发送已读回执的人数.  
当所有接收者均已读，或者这条消息不是一条需要已读回执的消息时,返回0

#### 获取当前已读回执详情
当一条需要接收方发送已读回执的消息成功发出之后，消息发送方可以查看这条消息当前已读回执的详情.详情中包含当前已发送已读回执和未发送已读回执的用户`UserInfo`列表等信息  
***Since 2.3.0***  

```
	message.getReceiptDetails(GetReceiptDetailsCallback callback)
```

参数说明

+ GetReceiptDetailsCallback callback 结果回调

#### 消息接收方将消息标记为已读
对于消息接收方，可以将一条消息标记为已读，标记成功后，这条消息的已读状态会记录在本地。
当这条消息是一条需要已读回执的消息时，sdk还将主动发送一个通知事件`MessageReceiptStatusChangeEvent`给消息发送方，通知对方这条消息的已读回执人数发生变化。  
注意这个已读状态只会保存在本地，当本地数据被清除，或者用户更换设备登陆之后，已读状态会被重置为false。  
***Since 2.3.0***  

```
	message.setHaveRead(BasicCallback callback)
```

参数说明

+ BasicCallback callback 结果回调


#### 获取消息是否是已读状态
对于消息接收方，可以通过此接口获取到这条消息是否是已读的状态。
默认所有收到的消息已读状态都为`false`。在成功调用`message.setHaveRead(BasicCallback callback)`接口后，消息的已读状态变成`true`  
注意这个已读状态只会保存在本地，当本地数据被清除，或者用户更换设备登陆之后，已读状态会被重置为false。  
***Since 2.3.0***  

```
	message.haveRead()
```

接口返回

+ boolean 消息的已读状态. true - 已读,false - 未读

#### 消息回执状态变更事件

```
MessageReceiptStatusChangeEvent
```

对于消息发送方发送的需要接收方发送已读回执的消息，接收方通过`message.setHaveRead(BasicCallback callback)`接口成功发送已读回执后，sdk会上抛这个事件通知消息发送方。发送方通过这个事件可以知道是哪个会话中的哪条消息的未回执人数发生了变化。  
具体处理方法见[事件处理](#Event)一节

**回执相关代码示例：**

```
//消息发送方：
//===========发送带已读回执的消息：
final Message message = mConversation.createSendMessage(new TextContent(“这是一条需要对方发送已读回执的消息.”));
message.setOnSendCompleteCallback(new BasicCallback() {
    @Override
    public void gotResult(int responseCode, String responseDesc) {
        if (responseCode == 0) {
            //消息发送成功
            message.getUnreceiptCnt();//带回执的消息发送成功后，可以查看当前尚未发送已读回执的人数
            message.getReceiptDetails(...);//获取当前已读回执详情,具体包括已读和未读用户的UserInfo列表。callback中代码略
        } else {
            //消息发送失败
        }
    }
});
MessageSendingOptions options = new MessageSendingOptions();
options.setNeedReadReceipt(true);//针对这条消息打开已读回执功能
JMessageClient.sendMessage(message,options);//使用自定义的控制参数发送消息
//===========

//===========消息发送方监听回执状态变化：
public void onEventMainThread(MessageReceiptStatusChangeEvent event) {
        Conversation conv = event.getConversation();
        tv_refreshEvent.append(String.format(Locale.SIMPLIFIED_CHINESE, "\n收到MessageReceiptStatusChangeEvent事件,会话对象是%s\n", conv.getTargetId()));
        for (MessageReceiptStatusChangeEvent.MessageReceiptMeta meta : event.getMessageReceiptMetas()) {
            tv_refreshEvent.append(String.format(Locale.SIMPLIFIED_CHINESE,
                    "回执数有更新的消息serverMsgID：%d\n当前未发送已读回执的人数：%d", meta.getServerMsgId(), meta.getUnReceiptCnt()));
        }
}
//===========


//消息接收方
//===========将消息标记为已读
if(!message.haveRead()){ //当消息的haveRead状态为false时，调用setHaveRead,将消息标记为已读
	msg.setHaveRead(new BasicCallback() {
        @Override
        public void gotResult(int responseCode, String responseMessage) {
            Toast.makeText(MessageReceiptActivity.this, "成功将消息标记为已读. responseCode = " + responseCode + " responseMessage =" + responseMessage, Toast.LENGTH_SHORT).show();
        }
    });
}
//===========

```

### 命令透传
***Since 2.3.0***  
命令透传发送的命令后台不会为其离线保存，只会在对方用户在线的前提下将命令推送给对方。sdk收到命令之后也不会本地保存，不发送通知栏通知，整体快速响应。  
开发者可以通过命令透传拓展一些在线场景下的辅助功能，如：实现输入状态提示等。

#### 发送命令透传

```
	/**
     * 发送消息透传给个人。
     * 消息不会进入到后台的离线存储中去，仅当对方用户当前在线时，透传消息才会成功送达。
     * 透传命令送达时，接收方会收到一个{@link CommandNotificationEvent}事件通知。
     * sdk不会将此类透传消息内容本地化。
     *
     * @param username 目标的用户名
     * @param appKey   目标的appKey, 如果传入null或空字符串，则默认用本应用的appKey
     * @param msg      发送的消息内容
     * @param callback 回调函数
     * @since 2.3.0
     */
	JMessageClient.sendSingleTransCommand(String username, appkey, String cmd,  BasicCallback callback)
	
	/**
     * 发送消息透传给群。
     * 消息不会进入到后台的离线存储中去，仅当对方用户当前在线时，透传消息才会成功送达。
     * 透传命令送达时，接收方会收到一个{@link CommandNotificationEvent}事件通知。
     * sdk不会将此类透传消息内容本地化。
     *
     * @param gid      群组的gid
     * @param msg      发送的消息内容
     * @param callback 回调函数
     * @since 2.3.0
     */
    JMessageClient.sendGroupTransCommand(long gid, String msg, BasicCallback callback)
```


###<span id="Event">事件处理</span>
#### 事件接收类的注册
```
JMessageClient.registerEventReceiver(Object receiver);
JMessageClient.registerEventReceiver(Object receiver, int priority);
```

参数说明

+ Object receiver 消息接收类对象
+ int priority 定义事件接收者接收事件的优先级，默认值为0，优先级越高将越先接收到事件。（优先级只对同一个线程模式中的接收者有效）

#### 事件接收类的解绑
```
JMessageClient.unRegisterEventReceiver(Object receiver);
```

参数说明

+ Object receiver 消息接收类对象，对象解绑之后将不再接收到任何event。

#### 事件接收
注册事件接收类之后，需要在消息接收类中实现如下方法来接收对应消息。sdk将根据实现方法的方法名来区分不同的线程模式，常用的线程模式有onEvent(默认线程模式)和onEventMainThread(主线程模式)两种。

可以通过定义不同类型的参数，来接收不同种类的事件。具体事件类型定义见 “事件类型” 一节

##### 默认线程（子线程）模式
```
public void onEvent(EventEntity event){
  //do your own business
}
```
方法体将在默认线程（子线程）中被调用， 可以用来处理耗时操作。

参数定义

+ EventEntity event 事件对象。（ 定义不同类型参数可以接收不同种类事件，具体用法可以参考“示例代码“。）

##### 主线程模式
```
public void onEventMainThread(EventEntity event){
  //do your own business
}
```
方法体将在主线程中被调用，可以用来刷新UI。
参数定义

+ EventEntity event 事件对象。


#### 事件类型

消息事件实体类 MessageEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">方法</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMessage()</td>
      <td >Message</td>
      <td >获取消息对象</td>
    </tr>
  </table>
</div>

</br>

离线消息事件实体类 OfflineMessageEvent
***Since 2.1.0***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">方法</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取收到离线消息的会话对象</td>
    </tr>
    <tr >
      <td >getNewMessageList()</td>
      <td >List<Message></td>
      <td >获取收到的离线消息列表,包含了该会话此次离线收到的所有离线消息列表。其中也有可能包含自己发出去的消息。</td>
    </tr>
    <tr >
      <td >getOfflineMsgCnt()</td>
      <td >int</td>
      <td >获取此次事件中该会话的离线消息总数。</td>
    </tr>
  </table>
</div>

</br>

会话刷新事件实体类 ConversationRefreshEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">方法</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取需要被刷新的会话对象</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >Reason</td>
      <td >获取事件发生的原因</td>
    </tr>
  </table>
</div>

</br>

当前登录用户信息被更新事件实体类 MyInfoUpdatedEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">方法</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取更新之后的我的userinfo</td>
    </tr>
    </table>
</div>

</br>

通知栏点击事件实体类NotificationClickEvent

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="30px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMessage()</td>
      <td >Message</td>
      <td >获取点击的通知所对应的消息对象</td>
    </tr>
  </table>
</div>

</br>

用户下线事件UserLogoutEvent **(已过时，请使用LoginStateChangeEvent代替)**

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前被登出账号的信息</td>
    </tr>
  </table>
</div>

</br>

用户被删除事件UserDeletedEvent **(已过时，请使用LoginStateChangeEvent代替)**

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前被删除账号的信息</td>
    </tr>
  </table>
</div>

</br>

用户登录状态变更事件LoginStateChangeEvent
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前登录状态改变的账号的信息</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >Reason</td>
      <td >获取登录状态变更原因。</td>
    </tr>
  </table>
</div>

消息被对方撤回通知事件MessageRetractEvent
***Since 2.2.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取被撤回消息所属的会话对象</td>
    </tr>
    <tr >
      <td >getRetractedMessage()</td>
      <td >Message</td>
      <td >获取被撤回的message对象.  
      (注意!此时获取到的Message的MessageContent对象已经从撤回前的真正的消息内容变为了PromptContent类型的提示文字)</td>
    </tr>
  </table>
</div>

消息未回执人数变更事件MessageReceiptStatusChangeEvent
***Since 2.3.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >`Conversation`</td>
      <td >获取未回执数变更的消息所属的会话对象</td>
    </tr>
    <tr >
      <td >getMessageReceiptMetas()</td>
      <td >`List<MessageReceiptMeta>`</td>
      <td >获取未回执数发生变化的消息的MessageReceiptMeta。其中包括了消息的serverMsg Id、当前的未回执人数、以及未回执人数更新的时间</td>
    </tr>
  </table>
</div>

命令透传事件CommandNotificationEvent
***Since 2.3.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getSenderUserInfo()</td>
      <td >`UserInfo`</td>
      <td >获取命令透传消息发送者的UserInfo</td>
    </tr>
    <tr >
      <td >getType()</td>
      <td >`Type`</td>
      <td >获取命令透传消息对象的类型，单聊是`Type.single`,群聊则是`Type.group`</td>
    </tr>    
    <tr >
      <td >getTargetInfo()</td>
      <td >`Objcet`</td>
      <td >获取命令透传消息发送对象的Info。若对象是单聊用户则是`UserInfo`,对象是群组则是`GroupInfo`，使用时强制转型</td>
    </tr>
    <tr >
      <td >getMsg()</td>
      <td >`String`</td>
      <td >获取命令透传消息的实际内容</td>
    </tr>
  </table>
</div>


#### 示例代码
接收消息事件
```Java
class MessageEventReceiver extends Activity{

  @Override
  protected void onCreate() {
    super.onCreate(savedInstanceState);
    //这里只是为了展示注册事件接受者接口的用法，实际上开发者可以在任意类中注册事件接收者
    //，而不仅仅在Activity中。 下同
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
            customContent.getNumberValue("custom_num"); //获取自定义的值
            customContent.getBooleanValue("custom_boolean");
            customContent.getStringValue("custom_string");
            break;
        case eventNotification:
        //处理事件提醒消息
        EventNotificationContent eventNotificationContent = (EventNotificationContent)msg.getContent();
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
            case group_info_updated://since 2.2.1
            //群信息变更事件
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
用户登录状态变更事件
```
class UserLogoutEventReceiver extends Activity{
    @Override
    protected void onCreate() {
        super.onCreate(savedInstanceState);
        JMessageClient.registerEventReceiver(this);
    }
    @Override
    protected void onDestroy() {
        JMessageClient.unRegisterEventReceiver(this);
        super.onDestroy();``
    }
    public void onEvent(LoginStateChangeEvent event){
        LoginStateChangeEvent.Reason reason = event.getReason();//获取变更的原因
        UserInfo myInfo = event.getMyInfo();//获取当前被登出账号的信息
        switch (reason) {
            case user_password_change:
            	//用户密码在服务器端被修改
                break;
            case user_logout:
            	//用户换设备登录
                break;
            case user_deleted:
            	//用户被删除
                break;
        }
     }

}
```



### 群组信息维护

#### 创建群组
```
JMessageClient.createGroup(String groupName, String groupDesc, CreateGroupCallback callback);

@since 2.3.0
JMessageClient.createGroup(String groupName, String groupDesc, File groupAvatarFile, String format, CreateGroupCallback callback)
```  
参数说明

+ String groupName 群名称
+ String groupDesc 群描述
+ File groupAvatarFile 群头像文件
+ String format 头像文件扩展名，注意名称中不要包括"."
+ CreateGroupCallback callback 结果回调

回调
```
  public abstract void gotResult(int responseCode, String responseMsg, long groupId);
```  
+ long groupId 新创建成功的群组ID（resopnseCode = 0 时）。

#### 获取群组列表
```
JMessageClient.getGroupIDList(GetGroupListCallback callback)
```
回调
```
public abstract void gotResult(int responseCode, String responseMessage,
            List<Long> groupIDList)
```
+ `List<Long>` groupIDList  当前用户所加入的群组的groupID的list


#### 获取群组信息
```
JMessageClient.getGroupInfo(long groupId, GetGroupInfoCallback callback)
```
参数说明

+ long groupId 群ID
+ GetGroupInfoCallback callback 结果回调

回调
```
  public void gotResult(int responseCode, String responseMessage, GroupInfo groupInfo)
```
+ GroupInfo groupInfo 返回的群组信息对象

#### 更新群组名称
```
groupInfo.updateName(String groupName, BasicCallback callback);
```
参数说明

+ String groupName 新的名称
+ BasicCallback callback 结果回调

#### 更新群组描述
```
groupInfo.updateDescription(String groupDesc, BasicCallback callback);
```
参数说明

+ String groupName 新的群组详情描述
+ BasicCallback callback 结果回调

#### 更新群组头像
**Since 2.3.0**
```
groupInfo.updateAvatar(File avatar, String format, BasicCallback callback);
```
参数说明

+ File avatar 群头像文件
+ String format 文件扩展名，注意名称中不要包含“.”
+ BasicCallback callback 结果回调


#### 添加群组成员
```
JMessageClient.addGroupMembers(long groupID, String appKey, List<String> userNameList, BasicCallback callback)
```  
参数说明

+ long groupId 待加群的群组ID。创建群组时返回的。
+ String appkey 被添加的群成员所属的appkey，不填则默认为本应用appkey
+ List usernameList 群组成员列表，使用成员 username。
+ BasicCallback callback 结果回调

#### 移除群组成员
```
JMessageClient.removeGroupMembers(long groupId, String appKey, List<String> usernameList, BasicCallback callback);
```
参数说明

+ long groupId 待删除成员的群ID。
+ String appkey 被移除的群成员所属的appkey，不填则默认为本应用appkey
+ List usernameList 待删除的成员列表。
+ BasicCallback callback 结果回调。

#### 退出群组
```
JMessageClient.exitGroup(long groupId, BasicCallback callback);
```
参数说明

+ long groupId 待退出的群ID。
+ BasicCallback callback 结果回调。

#### 获取群组成员列表
```
JMessageClient.getGroupMembers(long groupID,
      GetGroupMembersCallback callback)
```
参数说明

+ long groupId 群组ID
+ GetGroupMembersCallback callback

回调
```
  public void gotResult(int responseCode, String responseMessage, List<String> members);
```  
+ List members 成员列表(username)。

### 群消息屏蔽
群组被设置为屏蔽之后，将收不到该群的消息。但是群成员变化事件还是能正常收到  
***Since 2.1.0***
#### 设置群消息屏蔽
```
groupinfo.setBlockGroupMessage(int blocked, BasicCallback callback)
```
参数说明

+ int blocked 是否屏蔽群消息。 1 - 屏蔽，0 - 取消屏蔽
+ BasicCallback callback 结果回调。

#### 判断群组是否被屏蔽
```
groupinfo.isGroupBlocked();
```
返回

+ int 1 - 已被屏蔽，0 - 未被屏蔽

#### 获取当前用户的群屏蔽列表
```
JMessageClient.getBlockedGroupsList(GetGroupInfoListCallback callback)
```
参数说明

+ GetGroupInfoListCallback callback 结果回调。

### 群组@功能
消息发送方可以发一条带有@list的消息。  
接收方收到带有@list的消息之后，如果@list中包含了自己，或者是@全体成员，则在sdk默认弹出的通知栏提示中会有相应的提示，如"xxx在群中@了你"。  
#### 创建@群成员的消息
***Since 2.1.0***  
```
conversation.createSendMessage(MessageContent content, List<UserInfo> atList, String customFromName)
```
参数说明

+ MessageContent content 消息内容对象
+ List<UserInfo> atList 被@用户的userInfo list
+ String customFromName 自定义fromName

返回

+ Message 消息对象。

#### 创建@全体群成员的消息
***Since 2.2.0***  
```
conversation.createSendMessageAtAllMember(MessageContent content, String customFromName)
```
参数说明

+ MessageContent content 消息内容对象
+ String customFromName 自定义fromName

返回

+ Message 一条包含@全体成员信息的消息对象。

#### 判断消息是否@了自己
***Since 2.1.0***  
```
message.isAtMe()
```
返回

+ boolean true - atList中包含了自己， false - atList中不包含自己

#### 判断消息是否是@全体成员
***Since 2.2.0***  
```
message.isAtAll()
```
返回

+ boolean true - 是@全体成员， false - 不是@全体成员

#### 获取消息中@的群成员列表
***Since 2.1.0***  
```
message.getAtUserList(GetUserInfoListCallback callback)
```
参数说明

+ GetUserInfoListCallback callback 获取用户列表的回调接口。注意当这条消息是一条@全体成员的消息时，此接口将返回空。

#### 代码示例

``` java
	//消息发送方
    Conversation conv = Conversation.createGroupConversation(gid);
    GroupInfo groupInfo = (GroupInfo) conv.getTargetInfo();
    List<UserInfo> atList = new ArrayList<UserInfo>();
    atList.add(groupInfo.getGroupMemberInfo("user1", appkey));//获取到被@的群成员的userinfo，并填充到atList中去。
    atList.add(groupInfo.getGroupMemberInfo("user2", appkey));
    
    //创建一条带有atList的消息。
    Message msg = conv.createSendMessage(new TextContent("a message with atList!"), atList, null);
    JMessageClient.sendMessage(msg);//发送消息



	//消息接收方
	public void onEvent(MessageEvent event){
		Message msg = event.getMessage();//收到消息事件，从消息事件中拿到消息对象
		msg.isAtMe(); //判断这条消息是否@了我
		
		//获取消息中包含的完整的atList
		msg.getAtUserList(new GetUserInfoListCallback() {
		    @Override
		    public void gotResult(int responseCode, String responseMessage, List<UserInfo> userInfoList) {
		        if(responseCode == 0){
		        	//获取atList成功
		        }else{
		        	//获取atList失败
		        }
		    }
      });
	}
```


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

+ int flag  显示通知的模式,包括[FLAG_NOTIFY_WITH_SOUND](./im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_SOUND)、[FLAG_NOTIFY_WITH_VIBRATE](./im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_VIBRATE)、[FLAG_NOTIFY_WITH_LED](./im_android_api_docs/cn/jpush/im/android/api/JMessageClient.html#FLAG_NOTIFY_WITH_LED)等类型，支持使用 '|' 符号联结各个参数


#### 获取通知栏展示类型
***Since 2.2.0***

```
JMessageClient.getNotificationFlag();
```
返回

+ int 当前设置的通知栏的展示类型。

#### 进入单聊会话
进入单聊会话。默认进入的是本应用appKey下用户的会话。
	UI在进入单聊会话页面时需要调用此函数，SDK会根据传入的username来决定是否需要发送通知

```
JMessageClient.enterSingleConversation(String username)
```
参数定义

  + String username 单聊聊天对象的username

#### 进入单聊会话(跨应用)
在进入聊天会话界面时调用，设置当前正在聊天的对象，sdk用来判断notification是否需要展示。若appKey为空则默认填充本应用的appKey。
	UI在进入单聊会话页面时需要调用此函数，SDK会根据传入的username来决定是否需要发送通知

```
JMessageClient.enterSingleConversation(String username,String appKey)
```
参数定义

  + String username 单聊聊天对象的username
  + String appKey 聊天对象所属appKey

#### 进入群聊会话

进入群聊会话。UI在进入群聊会话页面时需要调用此函数，SDK会根据传入的groupID来决定是否需要发送通知

```
JMessageClient.enterGroupConversation(long groupID)
```

参数定义

  + long groupID 群聊聊天对象的群ID


#### 退出会话
退出会话。UI在退出会话页面时需要调用此函数。
```
JMessageClient.exitConversation();
```
#### 通知栏点击事件监听
用户可以通过接受通知栏点击事件NotificationClickEvent，来实现自定义跳转，该事件如果没有接收者，点击通知栏时SDK将默认跳转到程序主界面。

事件接收方法见[事件处理](#Event)一节


### 好友列表管理
jmessage sdk 好友模块仅实现对用户好友关系的托管，以及相关好友请求的发送和接收。除此之外的任何建立在好友关系之上的功能（如仅限于好友之间才能进行的聊天等），需要开发者的应用层自己实现。

#### 发送好友添加请求
发送添加好友请求。在对方未做回应的前提下，允许重复发送添加好友的请求。请求发送后对方会收到一条好友请求的[ContactNotifyEvent](#ContactEvent)事件。

```
public static void sendInvitationRequest(final String targetUsername,String appKey, final String reason, final BasicCallback callback)
```

参数定义

+ String targetUsername 被邀请方用户名
+ String appKey 被邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ String reason 申请理由
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.sendInvitationRequest("test_user", "test_appkey", "hello", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //好友请求请求发送成功
                } else {
                    //好友请求发送失败
                }
            }
        });
```


#### 接受好友请求
接受对方的好友请求，操作成功后，对方会出现在自己的好友列表中，双方建立起好友关系。请求发送后对方会收到一条好友请求被接受的[ContactNotifyEvent](#ContactEvent)事件。

```
ContactManager.acceptInvitation(final String targetUsername, String appKey, final BasicCallback callback)
```

参数定义

+ String targetUsername 邀请方的用户名
+ String appKey 邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.acceptInvitation("test_user", "test_appkey", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //接收好友请求成功
                } else {
                    //接收好友请求失败
                }
            }
        });
```


#### 拒绝好友请求
拒绝对方的好友请求。请求发送后对方会收到一条好友请求被拒绝的[ContactNotifyEvent](#ContactEvent)事件。

```
ContactManager.declineInvitation(final String targetUsername, String appKey, String reason, final BasicCallback callback)
```

参数定义

+ String targetUsername 邀请方用户名
+ String appKey 邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ String reason 拒绝理由
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.declineInvitation("test_user", "test_appkey", "sorry~", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //拒绝好友请求成功
                } else {
                    //拒绝好友请求失败
                }
            }
        });
```

#### 获取好友列表
获取当前登录用户的好友列表，异步返回结果。

```
ContactManager.getFriendList(final GetUserInfoListCallback callback)
```

参数定义

+ GetUserInfoListCallback callback 结果回调。

代码示例：

```
ContactManager.getFriendList(new GetUserInfoListCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage, List<UserInfo> userInfoList) {
                if (0 == responseCode) {
                    //获取好友列表成功
                } else {
                    //获取好友列表失败
                }
            }
        });
```

#### 删除好友
将用户从你的好友列表中移除，移除成功后，对方会收到一条好友被移除的[ContactNotifyEvent](#ContactEvent)事件。

```
userinfo.removeFromFriendList(BasicCallback callback)
```

参数定义

+ BasicCallback callback 结果回调

代码示例：

```
userinfo.removeFromFriendList(new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //移出好友列表成功
                } else {
                    //移出好友列表失败
                }
            }
        });
```

#### 更新用户备注名/备注信息
仅当用户存在于你的好友列表中时，才能更新其用户备注名和备注信息。

```
userinfo.updateNoteName(String noteName, BasicCallback callback)

userinfo.updateNoteText(String noteText, BasicCallback callback)
```

参数定义：

+ String noteName 新的备注名
+ String noteText 新的备注信息
+ BasicCallback callback 结果回调

代码示例：

```
userinfo.updateNoteName("new_note_name", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //更新备注名成功
                } else {
                    //更新备注名失败
                }
            }
        });
```

#### <span id="ContactEvent">联系人相关通知事件</span>

新增联系人相关通知事件`ContactNotifyEvent`,具体事件处理方法见：[事件处理](#Event)一节
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getType()</td>
      <td >ContactNotifyEvent.Type</td>
      <td >获取联系人通知事件的具体类型，具体类型见[Type](./im_android_api_docs/cn/jpush/im/android/api/event/ContactNotifyEvent.html)定义</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >String</td>
      <td >获取事件发生的理由，该字段由对方发起请求时所填，对方如果未填则将返回默认字符串</td>
    </tr>
    <tr >
      <td >getFromUsername()</td>
      <td >String</td>
      <td >获取事件发送者的username</td>
    </tr>
    <tr >
      <td >getFromUserAppKey()</td>
      <td >String</td>
      <td >获取事件发送者用户所属应用的appKey</td>
    </tr>
  </table>
</div>


示例代码：

```
class ContactNotifyEventReceiver extends Activity{

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
  
  public void onEvent(ContactNotifyEvent event) {
        String reason = event.getReason();
        String fromUsername = event.getFromUsername();
        String appkey = event.getfromUserAppKey();

        switch (event.getType()) {
            case invite_received://收到好友邀请
                //...
                break;
            case invite_accepted://对方接收了你的好友邀请
                //...
                break;
            case invite_declined://对方拒绝了你的好友邀请
                //...
                break;
            case contact_deleted://对方将你从好友中删除
                //...
                break;
            default:
                break;
        }
    }

}

```

### 免打扰相关
可以将用户/群组添加到“免打扰”列表中，收到免打扰用户/群组发过来的消息时，sdk不会弹出默认的通知提示，但消息事件照常下发。

#### 获取免打扰列表
```
JMessageClient.getNoDisturblist(GetNoDisurbListCallback callback)
```
参数定义

+ GetNoDisurbListCallback callback 回调接口。
	
#### 设置普通免打扰
见api doc中[UserInfo](./im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html)和[GroupInfo](./im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html)相关接口


#### 设置全局免打扰
设置全局免打扰之后，收到所有消息都将不会有通知栏通知，效果类似<br> `setNotificationMode(JMessageClient.NOTI_MODE_NO_NOTIFICATION)`，但是此设置在用户换设备之后也会生效。

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

### <span id="CrossApp">跨应用通信</span>
<font color= SteelBlue>说明：跨应用通信是指允许同一开发者账号下的不同应用能互相通信，以满足开发者对于不同appKey下应用通信的需求。</font>
</br>JMessage Android SDK在v1.2.0版本中实现了单聊跨应用，v1.3.0版本中实现了群聊以及其他一些功能的跨应用，
具体对应关系见下表：

<table>
	<tr>
		<th>Since</th>
		<th>实现功能</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>v1.2.0</td>
		<td>1.跨应用获取用户信息<br>2.跨应用单聊</td>
		<td>1.实现跨应用获取用户信息<br>2.实现跨应用给用户发送单聊消息</td>
	</tr>
	<tr>
		<td>v1.3.0</td>
		<td>1.跨应用群聊<br>2.跨应用黑名单设置<br>3.跨应用免打扰设置</td>
		<td>1.群组中允许加入来自不同应用下的用户，使跨应用群聊成为可能*<br>2.允许跨应用加用户至黑名单，以屏蔽来自不同应用下用户的消息<br>3. 实现跨应用添加和移除免打扰</td>
	</tr>	
</table>


**：实现跨应用群聊的关键在于群组中加入跨应用的群成员，而创建会话和发送消息的流程和普通的群聊实现方式一致。*

#### 跨应用相关接口摘要

跨应用接口与非跨应用接口区别主要在于：跨应用接口增加了appkey作为参数。
详细接口说明请前往极光IM [Android API Java docs](./im_android_api_docs/)

##### Conversation

创建单聊跨应用会话

```
createSingleConversation(String userName, String appKey)
```  

##### JMessageClient

跨应用获取用户信息

```
getUserInfo(String username,String appKey,GetUserInfoCallback callback)  
```
    
跨应用添加群成员

```
addGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback)            
``` 

跨应用踢出群成员

```
removeGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback)
```
    
跨应用添加user进黑名单

```
addUsersToBlacklist(List<String> usernames,String appKey,BasicCallback callback)  
```    


跨应用将user移出黑名单

```
delUsersFromBlacklist(List<String> usernames,String appKey,BasicCallback callback)  
```    

##### GroupInfo

获取群成员信息

```
getGroupMemberInfo(String username, String appKey)  
```    


#### 跨应用相关具体实现

##### 跨应用获取用户信息

通过指定appKey可以实现获取跨应用用户信息。

```
JMessageClient.getUserInfo(java.lang.String username,java.lang.String appKey,GetUserInfoCallback callback)
```

参数定义:

* username - 开发者注册的用户名
* appKey - 指定的appKey,如果为空则在本应用appKey下查找用户
* callback - 获取用户信息的回调接口

代码示例：

```
JMessageClient.getUserInfo("username", "appKey", new GetUserInfoCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage, UserInfo info) {
         // 获取到跨应用的用户信息
         ...
    }
});
```

##### 跨应用单聊实现

创建单聊会话时指定对方用户所属appKey，即可建立起一个和跨应用用户的单聊会话。

```
Conversation.createSingleConversation(String targetUsername, String appKey)
```

参数定义：

* targetUsername - 用户的username
* appKey - 指定的appKey,如果为空则默认填本应用appKey

创建跨应用会话后，创建消息发送即可。下面以创建一条单聊文本消息为例

代码示例：

```
//创建跨应用会话
Conversation con = Conversation.createSingleConversation("username", "appKey");
MessageContent content = new TextContent("hello");
//创建一条消息 
Message message = con.createSendMessage(content);
//发送消息 
JMessageClient.sendMessage(message);
```

##### 跨应用群聊实现

实现跨应用群聊的关键在于群组中加入跨应用的群成员，而创建会话和发送消息的流程和普通的群聊实现方式一致。

下面列出了和跨应用操作群成员相关的接口

1.跨应用添加群成员  

```
JMessageClient.addGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback);
```
参数:

* groupID - 群组的groupID
* appKey - usernameList中user所属的appKey,如果为空则在本应用appKey下查找用户
* userNameList - 添加进群组的成员username集合
* callback - 回调接口
 
2.跨应用踢出群成员

```
JMessageClient.removeGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback);
```
参数:

* groupID - 群组的groupID
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* userNameList - 踢出群组成员的username集合
* callback - 回调接口

3.获取群成员信息 

```
//此接口是实例对象上的接口
groupInfo.getGroupMemberInfo(String username, String appKey)
```
参数:

* username - 指定群成员的username 
* appKey - 群成员所属的appKey


下面以向已有群组中添加跨应用群成员，然后创建会话发送消息为例:

代码示例：

```
//添加跨应用用户到群组
JMessageClient.addGroupMembers(testGid, "appKey", userNameList, new BasicCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage) {
         //添加跨应用群成员成功之后，创建会话，发送消息。 
         if(0 == responseCode){
             Conversation conversation = Conversation.createGroupConversation(testGid);
             Message msg = conversation.createSendTextMessage("hello");
             JMessageClient.sendMessage(msg);
         }
     }
});
```

##### 跨应用添加黑名单实现

通过以下接口在操作黑名单列表时指定appKey，即可实现将跨应用的用户加入黑名单。

1.添加user进黑名单

```
JMessageClient.addUsersToBlacklist(List<String> usernames,String appKey,BasicCallback callback);
```
参数:

* usernames -添加进黑名单的username集合
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* callback - 回调接口

2.将user移出黑名单

```
JMessageClient.delUsersFromBlacklist(List<String> usernames,String appKey,BasicCallback callback)
```
参数:

* usernames - 移出黑名单的username集合
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* callback - 回调接口


代码示例：

```
//跨应用添加用户至黑名单
JMessageClient.addUsersToBlacklist(usernames, "appKey",new BasicCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage) {
         if (0 == responseCode）{
             //成功跨应用添加用户至黑名单
             ... 
         } 
     }
}); 
```


##### 跨应用免打扰实现

原有接口无需变动。免打扰相关接口是在userinfo对象上的实例接口，也就是说只要获取到的user是跨应用的用户，直接调用该userinfo对象的免打扰接口就可实现跨应用

```
userinfo.setNoDisturb(int noDisturb,BasicCallback callback)
```
参数:

  * noDisturb - 1 -- 免打扰，其他 -- 非免打扰（设置免打扰时将参数设置为1，取消免打扰时将参数设置为0）
  * callback - 回调接口

代码示例：

```
//跨应用获取用户信息
JMessageClient.getUserInfo("username", "appKey", new GetUserInfoCallback() {
    @Override
    public void gotResult(int responseCode, String responseMessage, UserInfo info) {
        //跨应用获取用户信息成功，设置用户的免打扰属性 
        if(0 == responseCode){
            info.setNoDisturb(1,null);
        }
    }
});
```

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
if (null == conv) {
  conv = Conversation.createSingleConversation("tom");
}
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
cn.jpush.im.api.content.LocationContent
cn.jpush.im.api.content.FileContent
cn.jpush.im.api.content.CustomContent
```

使用举例

```
// 参数：文本内容
TextContent text = new TextContent("Hi, JMessage");

// 参数：语音文件对象，语音文件时长
VoiceContent voice = new VoiceContent(new File("/sdcard/voice.amr"), 21);

// 参数：图片文件对象
ImageContent image = new ImageContent(new File("/sdcard/image.png"));

// 参数：任意文件对象
FileContent fileContent = new FileContent(new File("/sdcard/file.xxx"));

// 参数：经度，纬度，缩放比例，地址详情
LocationContent locationContent = new LocationContent(111.1,222.2,500,"xx省xx市xx区xx街xx号");
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

    /**
     * 默认callback会在主线程中回调，如果需要在子线程回调，则在构造方法的参数中传入false
     * @param isRunInUIThread 是否在主线程中执行回调，默认为true。
     */
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

参考文档：[IM Android SDK 错误码列表](./im_errorcode_android)

