<h1>会话与消息</h1>


## 概述

### 会话概述

与一个聊天对象（用户、群组、聊天室等）的整个聊天上下文我们称之为一个会话。会话是消息的载体，消息一定是从属与某个会话对象的。

### 消息概述

极光 IM 最核心的功能是消息功能。核心核心能力包含以下：

- 保证消息及时下发；
- 单聊，群聊；
- 消息类型：文本、语音、图片、文件、位置等；
- 用户未在线时保存离线消息；
- 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；


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


### 创建消息

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

#### 创建视频消息
```
    /**
     * 创建一条单聊video消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param userName      聊天对象用户名
     * @param appKey        聊天对象所属应用appkey
     * @param thumbImage    视频缩略图，可不填。
     * @param thumbFormat   视频缩略图格式名
     * @param videoFile     视频文件对象
     * @param videoFileName 视频文件名称，如果不填或为空，则默认使用文件原名
     * @param duration      视频时长
     * @return 消息对象
     * @throws IOException
     * @since 2.6.0
     */
    JMessageClient.createSingleVideoMessage(String userName, String appKey, Bitmap thumbImage, String thumbFormat, File videoFile, String videoFileName, int duration) throws IOException

	/**
     * 创建一条群聊video消息，此方法是创建message的快捷接口，对于不需要关注会话实例的开发者可以使用此方法
     * 快捷的创建一条消息。其他的情况下推荐使用{@link Conversation#createSendMessage(MessageContent)}
     * 接口来创建消息
     *
     * @param groupID       群组groupID
     * @param thumbImage    视频缩略图，可不填。
     * @param thumbFormat   视频缩略图格式名
     * @param videoFile     视频文件对象
     * @param videoFileName 视频文件名称，如果不填或为空，则默认使用文件原名
     * @param duration      视频时长
     * @return 消息对象
     * @throws IOException
     * @since 2.6.0
     */
    JMessageClient.createGroupVideoMessage(long groupID, Bitmap thumbImage, String thumbFormat, File videoFile, String videoFileName, int duration) throws IOException
```


### 消息发送结果监听
消息发送完成后，会回调这里的接口通知上层。
```
message.setOnSendCompleteCallback(BasicCallback sendCompleteCallback)
```
参数说明

+ BasicCallback sendCompleteCallback 回调接口

### 发送消息

向服务器给发送对象发送消息，并且保存到本地会话。使用默认的配置参数发送
```
/**
 * 发送消息，使用默认发送配置参数.<br/>
 * 注意只有创建的消息和发送失败的消息可以被发送{@link MessageStatus}，<br/>
 * 发送成功或收到的消息再次发送需调用转发接口{@link JMessageClient#forwardMessage(Message, Conversation, MessageSendingOptions, RequestCallback)}.
 *
 * @param message 消息对象
 */
JMessageClient.sendMessage(Message message);
```
参数说明

+ Message message 消息对象

#### 附带控制参数的消息发送
***Since 2.2.0***  
针对此次消息发送操作，支持一些可选参数的配置，具体参数见[MessageSendingOptions](../im_android_api_docs/cn/jpush/im/android/api/options/MessageSendingOptions.html)

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

### 接收消息
sdk收到消息时，会上抛消息事件[MessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) 或 [OfflineMessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html)，开发者可以通过这个事件来拿到具体的Message对象，进而执行UI刷新或者其他相关逻辑。具体事件处理方法见[事件处理](./event)一节


#### 从2.1.0版本开始接收消息的变化
2.1.0版本开始，sdk将消息下发分为在线下发和离线下发两种类型。 先明确两个概念：

+ 在线消息：im用户在线期间，所有收到的消息称为在线消息。
+ 离线消息：im用户离线期间（包括登出或者网络断开）所产生的消息，会暂存在极光服务器上。当用户再次上线，sdk会将这部分消息拉取下来，这部分消息就称为离线消息。

有了这两个概念的区分之后，sdk对于这两种消息的处理方式也有了不同：  


版本 | 在线消息 | 离线消息 
--- | ------- | ------
2.1.0之前 | 每收到一条消息上抛一个[MessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) | 和在线消息一样，有多少条离线消息就上抛多少个[MessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank)|
2.1.0开始 | 每收到一条消息上抛一个[MessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html?_blank) | 以会话为单位，该会话如果有离线消息，sdk就会上抛一个[OfflineMessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html)。就算同会话中有多条离线消息，sdk也只会上抛一个[OfflineMessageEvent](../im_android_api_docs/cn/jpush/im/android/api/event/OfflineMessageEvent.html),这个Event中就包含了所有离线消息的相关信息。这样会大大减轻上层处理事件的压力。



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


### 本地消息记录获取
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



### 撤回消息

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
消息发送方发起撤回后，被撤回方会收到一条事件通知[MessageRetractEvent](../im_android_api_docs/cn/jpush/im/android/api/event/MessageRetractEvent.html)，具体事件处理方式见[事件处理](#Event)一节


**注意：** 无论是撤回方还是被撤回方，消息被撤回后，对应message content会被替换为[PromtContent](../im_android_api_docs/cn/jpush/im/android/api/content/PromptContent.html)类型，消息之前内容变成不可见。

### 转发消息

#### 转发会话中的某条消息
```
    /**
     * 转发消息,只有发送成功或收到的消息才可转发
     *
     * @param message  需要转发的消息对象
     * @param conv     目标会话
     * @param options  消息转发时的控制选项，仅对此次发送生效, null则使用默认配置
     * @param callback 回调函数
     * @since 2.3.0
     * @deprecated deprecated since jmessage 2.6.0 use {@link JMessageClient#forwardMessage(Message, Conversation, MessageSendingOptions, RequestCallback)} instead.
     */
    JMessageClient.forwardMessage(Message message, Conversation conv, MessageSendingOptions options, BasicCallback callback);

    /**
     * 转发消息,注意支持转发的消息{@link Message#isSupportForward()}才可转发,符合转发要求后会创建新的消息发送，
     * 创建的消息会在回调中返回（无论发送是否成功），如果不符合转发要求则不会创建新消息 message返回null。<br/>
     *
     * @param message  需要转发的消息对象
     * @param conv     目标会话
     * @param options  消息转发时的控制选项，仅对此次发送生效, null则使用默认配置
     * @param callback 回调函数
     * @since 2.6.0
     */
    JMessageClient.forwardMessage(Message message, Conversation conv, MessageSendingOptions options, final RequestCallback<Message> callback);
```

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
具体处理方法见[事件处理](./event)一节

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
	
	/**
     * 发送透传消息给当前用户在其他平台已登录的设备。
     * 消息不会进入到后台的离线存储中去，仅当对方用户当前在线时，透传消息才会成功送达。
     * 透传命令送达时，接收方会收到一个{@link CommandNotificationEvent}事件通知。
     * sdk不会将此类透传消息内容本地化。
     *
     * @param platformType 平台类型，其中{@link PlatformType#all}表示发送给当前多端在线的其他所有设备（不包括本设备）。
     * @param msg          发送的消息内容
     * @param callback     回调函数
     * @since 2.5.0
     */
    JMessageClient.sendCrossDeviceTransCommand(PlatformType platformType, String msg, BasicCallback callback)
```
