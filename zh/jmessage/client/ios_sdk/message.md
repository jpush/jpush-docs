<h1>会话与消息</h1>

## 概述

### 会话

与一个聊天对象（用户、群组、聊天室等）之间的聊天。我们称之为一个会话。会话是消息的载体，消息一定是从属于某个会话对象的。

### 消息

极光 IM 最核心的功能是消息功能。核心能力包含以下：

- 消息的及时下发；
- 单聊，群聊，聊天室；
- 消息类型：文本、语音、图片、文件、位置等；
- 保存消息记录；
- 用户离线时保存离线消息；
- 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

### 本地会话管理
会话都是本地保存和管理的，不会上传到服务器。
#### 创建会话
创建会话时，如果本地已存在对应会话，则不会重复创建，将直接返回本地会话对象。通过指定 appkey，可以实现给其他 appkey 下的用户发消息。
##### 创建单聊会话
```
/*!
 * @abstract 创建单聊会话
 *
 * @param username 单聊对象 username
 * @param handler 结果回调。正常返回时 resultObject 类型为 JMSGConversation。
 *
 * @discussion 如果会话已经存在，则直接返回。如果不存在则创建。
 * 创建会话时如果发现该 username 的信息本地还没有，则需要从服务器上拉取。
 * 服务器端如果找不到该 username，或者某种原因查找失败，则创建会话失败。
 */
+ (void)createSingleConversationWithUsername:(NSString *)username
                           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
##### 创建群聊会话
```
/*!
 * @abstract 创建群聊会话
 *
 * @param groupId 群聊群组ID。由创建群组时返回。
 * @param handler 结果回调。正常返回时 resultObject 类型为 JMSGConversation。
 *
 * @discussion 如果会话已经存在，则直接返回。如果不存在则创建。
 * 创建会话时如果发现该 groupId 的信息本地还没有，则需要从服务器端上拉取。
 * 如果从服务器上获取 groupId 的信息不存在或者失败，则创建会话失败。
 */
+ (void)createGroupConversationWithGroupId:(NSString *)groupId
                         completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 获取会话
##### 获取单聊会话
获取与指定appkey下username的单聊会话信息,如果appkey为空则默认取本应用appkey下对应username用户的会话

```
/*!
 * @abstract 获取单聊会话
 *
 * @param username 单聊对象 username
 * @param appKey   应用appKey
 *
 * @discussion 如果会话还不存在，则返回 nil
 */
+ (JMSGConversation * JMSG_NULLABLE)singleConversationWithUsername:(NSString *)username
                                                            appKey:(NSString *)userAppKey;
```
##### 获取群聊会话
```
/*!
 * @abstract 获取群聊会话
 *
 * @param groupId 群聊群组ID。此 ID 由创建群组时返回的。
 *
 * @discussion 如果会话还不存在，则返回 nil
 */
+ (JMSGConversation * JMSG_NULLABLE)groupConversationWithGroupId:(NSString *)groupId;
```
##### 获取会话列表
从本地数据库中获取会话列表，默认按照会话的最后一条消息的时间，降序排列

```
/*!
 * @abstract 返回 conversation 列表（异步,已排序）
 *
 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里成员的类型为 JMSGConversation
 *
 * @discussion 当前是返回所有的 conversation 列表，不包括聊天室会话，默认是已经排序。
 */
+ (void)allConversations:(JMSGCompletionHandler)handler;
```

#### 删除会话
删除本地会话数据，删除会话时，与会话相关的多媒体消息文件也会从本地删除。
##### 删除单聊会话
```
/*!
 * @abstract 删除单聊会话
 *
 * @param username 单聊用户名
 *
 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
 */
+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username;

/*!
 * @abstract 删除跨应用单聊会话
 */
+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username
                                      appKey:(NSString *)userAppKey;
```
##### 删除群聊会话
```
/*!
 * @abstract 删除群聊会话
 *
 * @param groupId 群聊群组ID
 *
 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
 */
+ (BOOL)deleteGroupConversationWithGroupId:(NSString *)groupId;
```

#### 会话未读数
会话未读分为：

+ 单个会话的未读数
+ 全局的消息未读数，即：所有会话的未读数总和

##### 会话全局未读数
```
/*!
 * @abstract 获取当前所有会话的未读消息的总数
 *
 * @discussion 获取所有会话未读消息总数，开启免打扰的会话未读数不会加入计数
 */
+ (NSNumber *)getAllUnreadCount;
```
##### 单个会话未读数
```
/*!
 * @abstract 未读数
 * @discussion 有新消息来时, SDK 会对未读数自动加 1
 */
@property(nonatomic, strong, readonly) NSNumber * JMSG_NULLABLE unreadCount;
```
##### 重置单个会话未读数
```
/*!
 * @abstract 清除会话未读数
 *
 * @discussion 把未读数设置为 0
 */
- (void)clearUnreadCount;
```

#### 会话头像
```
 /*!
 * @abstract 异步获取会话头像
 *
 * @param handler 结果回调。回调参数:
 *
 * - data 头像数据;
 * - objectId 为 targetId_conversationType 的组合, 用下划线隔开.
 *   其中 targetId 单聊时为 username_targetAppKey,
 *                 群聊时为 groupId
 * - error 不为nil表示出错;
 *
 * 如果 error 为 ni, data 也为 nil, 表示没有数据.
 *
 * @discussion 会话的头像来自于聊天对象, 单聊就是用户的头像.
 * 建议在会话列表时, 使用此接口来显示会话的头像, 而不要使用 target 属性里的用户头像.
 */
- (void)avatarData:(JMSGAsyncDataHandler)handler;
```

```
/*!
 * @abstract 获取会话头像的本地路径
 *
 * @return 返回本地路，返回值只有在下载完成之后才有意义
 */
- (NSString *JMSG_NULLABLE)avatarLocalPath;
```

### 创建消息
创建消息可分为两部分：先创建 content，再创建 message。

+ ***step 1：*** 先创建 content
```	
	JMSGTextContent  *content = [[JMSGTextContent alloc] initWithText:@"text"];
```	
+ ***step 2：*** 再创建 message
```
	message = [JMSGMessage createSingleMessageWithContent:content username:@"username"];
```

#### 创建 content

+ JMSGTextContent

```
/*!
 * @abstract 基于文本初始化内容对象
 *
 * @param text 纯文本内容
 *
 * @discussion 这是预设的创建文本类型内容的方法
 */
- (instancetype)initWithText:(NSString *)text;
```

+ JMSGImageContent

```
/*!
 * @abstract 初始化消息图片内容
 *
 * @param data 图片数据
 *
 * @discussion 这是预设的初始化方法. 创建一个图片内容对象, 必须要传入图片数据.
 *
 * 对于图片消息, 一般来说创建此图片内容的数据, 是对拍照原图经过裁减处理的, 否则发图片消息太大.
 * 这里传入的图片数据, SDK视为大图. 方法 largeImageDataWithProgress:completionHandler 下载到的,
 * 就是这个概念上的图片数据.
 */
- (nullable instancetype)initWithImageData:(NSData * JMSG_NONNULL)data;
```
+ JMSGVoiceContent

```
/*!
 * @abstract 初始化语音内容
 *
 * @param data 该语音内容的数据. 不允许为 nil, 并且内容长度应大于 0, 否则失败
 * @param duration 该语音内容的持续时长. 单位是秒. 不允许为 nil, 并且应大于 0.
 *
 * @discussion 这是预设的初始化方法, 创建一条语音内容, 必然传入语音数据, 以及时长.
 */
- (instancetype)initWithVoiceData:(NSData *)data
                    voiceDuration:(NSNumber *)duration;
```
+ JMSGVideoContent

```
/*!
 * @abstract 初始化视频消息内容
 *
 * @param data      该视频内容的数据
 * @param thumbData 缩略图，建议：缩略图上层要控制大小，避免上传过大图片
 * @param duration  该视频内容的持续时长，长度应大于 0
 *
 * @discussion 建议：缩略图上层要控制大小，避免上传过大图片.
 */
- (instancetype)initWithVideoData:(NSData *)data
                        thumbData:(NSData *JMSG_NULLABLE)thumbData
                         duration:(NSNumber *)duration;
```
+ JMSGLocationContent

```
/**
 *  初始化地理位置消息内容
 *
 *  @param latitude  纬度
 *  @param longitude 经度
 *  @param scale     缩放比例
 *  @param address   详细地址信息
 *
 *  @return 地理位置消息内容
 */
- (instancetype)initWithLatitude:(NSNumber *)latitude
                       longitude:(NSNumber *)longitude
                           scale:(NSNumber *)scale
                        address:(NSString *)address;
```
+ JMSGFileContent

```
/**
 *  初始化文件内容
 *
 *  @param data     文件数据
 *  @param fileName 文件名
 *
 */
- (instancetype)initWithFileData:(NSData *)data
                        fileName:(NSString *)fileName;
```

#### 创建 message
创建消息的接口在 `JMSGMessage` 和 `JMSGConversation` 类中都有，具体的区别请查看具体接口的接口描述信息。

##### JMSGMessage 类中创建 message 的接口

这里只列举普通消息创建接口，如：创建@人消息、创建@所有人消息 等，具体请查看 `JMSGMessage` 类，或者查看 [群组管理模块 - 群组@功能](./group#group-@function)

+ 创建单聊消息

```
/*!
 * @abstract 创建单聊消息（快捷接口）
 *
 * @param content 消息内容对象
 * @param username 单聊用户 username
 *
 * #### 注意：
 *
 * 1、单独调用此接口创建消息，SDK 不会本地保存消息，再调用发送接口时才会保存；
 *
 * 2、如果上层希望创建消息时就本地化保存，请使用 [JMSGConversation createMessageWithContent:]
 */
+ (JMSGMessage *)createSingleMessageWithContent:(JMSGAbstractContent *)content
                                       username:(NSString *)username;
```

+ 创建群聊消息

```
/*!
 * @abstract 创建群聊消息
 *
 * @param content 消息内容对象
 * @param groupId 群聊ID
 *
 * #### 注意：
 *
 * 1、单独调用此接口创建消息，SDK 不会本地保存消息，再调用发送接口时才会保存；
 *
 * 2、如果上层希望创建消息时就本地化保存，请使用 [JMSGConversation createMessageWithContent:]
 */
+ (JMSGMessage *)createGroupMessageWithContent:(JMSGAbstractContent *)content
                                       groupId:(NSString *)groupId;
```

##### JMSGConversation 类中创建 message 的接口
***注意：*** `JMSGMessage` 类中创建 `message` 的接口在创建时，是不会直接入库保存的，需在调用发送接口时才会保存，但是，通过 `JMSGConversation` 类中创建 `message` 接口创建消息时，在创建时就会入库保存，该区别可用于上层实现草稿状态的消息。

```
/*!
 * @abstract 创建消息对象
 *
 * @param content 消息的内容对象。当前直接的内容对象有:
 * JMSGTextContent, JMSGImageContent, JMSGVoiceContent, JMSGCustomContent
 *
 * @return JMSGMessage对象。该对象里包含了 content。
 *
 * @discussion 这是推荐的创建新的消息拿到 JMSGMessage 对象接口。
 *
 * 此接口创建消息后, SDK 会进行落地, 包括: 消息保存数据库, 媒体文件保存到文件系统.
 * 这意味着, 这个创建后的消息对象, App 可以用来放到 UI 上展示.
 *
 * 新创建的消息对象, 其消息状态 status 为: kJMSGMessageStatusSendDraft
 *
 * 调用此接口前需要先创建消息内容，以作为 content 参数传入。举例：
 *
 *    ```
 *    NSData *imageData = … // 可能来自拍照或者相册
 *    JMSGImageContent *imageContent = [[JMSGImageContent alloc] initWithImageData:imageData];
 *    ```
 *
 * 另外更快捷的作法是，不通过此接口创建 JMSGMessage 而是直接调用具体的发送接口，如 sendSingleTextMessage.
 *
 * 通过此接口先创建 JMSGMessage 的好处是，可以对 JMSGMessage 做更多的定制控制，比如加附加字段。举例：
 *
 *    ```
 *    [imageContent addExtraValue:@"extra_value" forKey:@"extra_key"]
 *    ```
 *
 * 注意：如果创建消息的内容是图片，并且图片可能比较大，则建议不要使用这个同步接口，
 * 改用 createMessageAsyncWithImageContent:completionHandler: 方法。
 */
- (JMSGMessage * JMSG_NULLABLE)createMessageWithContent:(JMSGAbstractContent *)content;
```

### <span id="send-message-delegate">消息发送结果监听</span>
发送消息之后，上层可以监听发送消息的发送状态，通过添加代理方式来监听发送结果。

#### 添加代理
第二个参数 `conversation` 如果不传则会监听所有会话的消息，如果传，则只会监听当前传入 `conversation` 的消息。

```	
[JMessage addDelegate: withConversation: ]
```	

#### 实现代理

```
/*!
 * @abstract 发送消息结果返回回调
 *
 * @param message 原发出的消息对象
 * @param error 不为nil表示发送消息出错
 *
 * @discussion 应检查 error 是否为空来判断是否出错. 如果未出错, 则成功.
 */
@optional
- (void)onSendMessageResponse:(JMSGMessage *)message error:(NSError *)error;
```


### <span id="send-message">发送消息</span>
发送消息有比较多的接口可以使用，主要是在 `JMSGMessage` 和 `JMSGConversation` 两个类中。

+ JMSGMessage 里的发送接口，不需要先创建会话，可以直接发送 message
+ JMSGConversation 里的发送接口，需要先创建会话，通过会话实例对象发送 message

这里只列举 `JMSGConversation` 类中的发送接口：
#### 通用发送接口

```
/*!
 * @abstract 发送消息（已经创建好对象的）
 *
 * @param message 通过消息创建类接口，创建好的消息对象
 *
 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 JMSGMessageDelegate中的onReceiveMessage: error:方法来注册消息发送结果
 */
- (void)sendMessage:(JMSGMessage *)message;
```

#### <span id="send-message-option">附带控制参数的发送接口</span>
SDK 在发消息时，提供了部分控制参数供上层使用，比如：控制离线消息存储、自定义通知栏内容、消息已读回执等，具体可控制参数请查看 [JMSGOptionalContent 类](./jmessage_ios_appledoc_html/Classes/JMSGOptionalContent.html)

```
/*!
 * @abstract 发送消息（附带可选功能，如：控制离线消息存储、自定义通知栏内容、消息已读回执等）
 *
 * @param message           通过消息创建类接口，创建好的消息对象
 * @param optionalContent   可选功能，具体请查看 JMSGOptionalContent 类
 *
 * @discussion 可选功能里可以设置离线消息存储、自定义通知栏内容、消息已读回执等，具体请查看 JMSGOptionalContent 类。
 *
 */
- (void)sendMessage:(JMSGMessage *)message optionalContent:(JMSGOptionalContent *)optionalContent;
```

#####  代码示例
```    
JMSGOptionalContent *option = [[JMSGOptionalContent alloc] init];
option.noSaveOffline = YES;//不保存离线消息
option.noSaveNotification = YES;//不在状态栏显示消息
option.needReadReceipt = YES;//否需要对方发送已读回执
option.messageCount = 1;//设置消息发送时的未读数，默认为 1
    
JMSGCustomNotification *custion = [[JMSGCustomNotification alloc] init];
custion.enabled = YES;//是否启用自定义通知栏
custion.title = @"title";//自定义消息通知栏的标题
custion.alert = @"alert";//自定义消息通知栏的内容
custion.atPrefix = @"atPrefix";//被@目标的通知内容前缀
    
option.customNotification = custion;
    
JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:@"text"];    
JMSGMessage *message = [self.conversation createMessageWithContent:textContent];
[self.conversation sendMessage:message optionalContent:option]
```

### 取消消息发送
上层在发送多媒体消息时，可能会有中途想取消发送的需求，此时就可以调用下面接口来完成对发送的消息取消发送。

```
/*!
 * @abstract 取消正在发送的消息
 *
 * @discussion 在消息发送结果监听 [JMSGMessageDelegate onSendMessageResponse:error:] 里会返回对应的错误信息和错误码。
 *
 * @since 3.8.1
 */
- (void)cancelSendingMessage;
```

### <span id="accept-message">接收消息<span>
SDK 收到消息时会上抛消息，上层通过 [onReceiveMessage:error:](./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:) 或 [onSyncOfflineMessageConversation:offlineMessages:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:)，开发者可以通过代理方法来拿到具体的 `message` 对象，进而执行 UI 刷新或者其他相关逻辑。[接收消息代理方法汇总](#message-accept-function)

#### <span id="message-sync">从3.1.0版本开始接收消息的变化</span>
`JMessage SDK 3.1.0` 版本开始，SDK 将消息下发分为在线下发和离线下发两种类型，离线下发包含了离线消息和漫游消息。 先明确这几个概念：

+ 在线消息：IM 用户在线期间，所有收到的消息称为在线消息。
+ 离线消息：IM 用户离线期间（包括登出或者网络断开）收到的消息，会暂存在极光服务器上，当用户再次上线，SDK 会将这部分消息拉取下来，这部分消息就称为离线消息。
+ 漫游消息：IM 用户在多个设备之间登录时，SDK 会将其他设备已接收的消息视为漫游。

有了这几个概念的区分之后，SDK 对于这两种消息的处理方式也有了不同：

<table class="table">
  <thead>
    <tr>
      <th>SDK版本</th>
      <th>在线消息</th>
      <th>离线消息</th>
      <th>漫游消息</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Version < 3.1.0</td>
      <td>
        逐条下发，每次都触发
        <a href="./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:
        </a>
      </td>
      <td>
        逐条下发，每次都触发
        <a href="./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:</a>
      </td>
      <td>无</td>
    </tr>
    <tr>
      <td>Version >= 3.1.0</td>
      <td>
        逐条下发，每次都触发
        <a href="./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:</a>
      </td>
      <td>
        以会话为单位，触发一次下发
        <a href="./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:">
          onSyncOfflineMessageConversation:</a>
      </td>
      <td style="word-break: break-all;">
        以会话为单位，触发一次下发
        <a href="./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncRoamingMessageConversation:">
          onSyncRoamingMessageConversation:</a>
      </td>
    </tr>
  </tbody>
</table>


**总结**

对于消息同步，以会话为单位，不管会话有多少离线消息，SDK只触发一次消息同步的代理方法，这个代理方法返回值中包含了具体某个会话、离线消息这些相关数据信息，上层通过这个方法可监听到每个会话完成消息同步的情况，从而去刷新UI，这样会大大减轻上层处理事件的压力。
<br />
SDK 升级到 3.1.0 版本后（或之后的版本），上层只需要做以下变动：

+ 设置消息漫游，调用 [新的 SDK 初始化](./jmessage_ios_appledoc_html/Classes/JMessage.html#//api/name/setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:) 设置消息漫游。
+ 添加漫游消息的代理方法 [onSyncRoamingMessageConversation:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncRoamingMessageConversation:) 通过此方法可以监听到漫游消息同步情况，从而刷新UI（不需要漫游消息的开发者可忽略此操作）。
+ 添加离线消息的代理方法 [onSyncOfflineMessageConversation:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:) 通过此方法可以监听到离线消息同步情况，从而刷新UI。

**注意:** 

`JMessage SDK 3.2.1` 版本开始（包括3.2.1），离线事件也会走消息同步策略。
离线事件分为：

+ 群事件：如果有离线的群事件，也会触发一次[离线消息的代理方法](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:)
+ 非群事件：其他事件还是不变，走以前的代理方法。


#### <span id="message-accept-function">接收消息代理方法汇总</span>
+ 在线消息接收方法

```
/*!
 * @abstract 接收消息(服务器端下发的)回调
 *
 * @param message 接收到下发的消息
 * @param error 不为 nil 表示接收消息出错
 *
 * @discussion 应检查 error 是否为空来判断有没有出错. 如果未出错, 则成功.
 * 留意的是, 这里的 error 不包含媒体消息下载文件错误. 这类错误有单独的回调 onReceiveMessageDownloadFailed:
 *
 * 收到的消息里, 也包含服务器端下发的各类消息事件, 比如有人被加入了群聊. 这类消息事件处理为特殊的 JMSGMessage 类型.
 *
 * 事件类的消息, 基于 JMSGMessage 类里的 contentType 属性来做判断,
 * contentType = kJMSGContentTypeEventNotification.
 */
@optional
- (void)onReceiveMessage:(JMSGMessage *)message error:(NSError *)error;
```

+ 离线消息接收方法

```
/*!
 * @abstract 同步离线消息、离线事件通知
 *
 * @param conversation    同步离线消息的会话
 * @param offlineMessages 离线消息、离线事件数组
 *
 * @discussion 注意：
 *
 * SDK 会将消息下发分为在线下发和离线下发两种情况,
 * 其中用户在离线状态(包括用户登出或者网络断开)期间所收到的消息我们称之为离线消息.
 *
 * 当用户上线收到这部分离线消息后,这里的处理与之前版本不同的是:
 *
 * 3.1.0 版本之前: SDK 会和在线时收到的消息一样,每收到一条消息都会上抛一个在线消息 JMSGMessage 来通知上层.
 *
 * 3.1.0 版本之后: SDK 会以会话为单位，不管该会话有多少离线消息，SDK同步完成后每个会话只上抛一次.
 *
 * 3.2.1 版本之后: SDK 会以会话为单位，不管该会话有多少离线事件，SDK同步完成后每个会话只上抛一次
 *
 * 注意：一个会话最多触发两次这个代理，即：离线消息和离线事件各一次,这样会大大减轻上层在收到消息刷新 UI 的压力.
 *
 * 上层通过此代理方法监听离线消息同步的会话,详见官方文档.
 *
 */
@optional
- (void)onSyncOfflineMessageConversation:(JMSGConversation *)conversation
                         offlineMessages:(NSArray JMSG_GENERIC(__kindof JMSGMessage *)*)offlineMessages;
```
+ 漫游消息接收

```
/*!
 * @abstract 同步漫游消息通知
 *
 * @param conversation 同步漫游消息的会话
 *
 * @discussion 注意：
 *
 * 当 SDK 触发此函数时，说明该会话有同步下漫游消息，并且已经存储到本地数据库中，
 * 上层可通过 JMSGConversation 类中的获取message的方法刷新UI.
 *
 * @since 3.1.0
 */
@optional
- (void)onSyncRoamingMessageConversation:(JMSGConversation *)conversation;
```

+ 多媒体下载失败回调

```
/*!
 * @abstract 接收消息媒体文件下载失败的回调
 *
 * @param message 下载出错的消息
 *
 * @discussion 因为对于接收消息, 最主要需要特别做处理的就是媒体文件下载, 所以单列出来. 一定要处理.
 *
 * 通过的作法是: 如果是图片, 则 App 展示一张特别的表明未下载成功的图, 用户点击再次发起下载. 如果是语音,
 * 则不必特别处理, 还是原来的图标展示. 用户点击时, SDK 发现语音文件在本地没有, 会再次发起下载.
 */
@optional
- (void)onReceiveMessageDownloadFailed:(JMSGMessage *)message;
```

### 取消多媒体消息下载
上层在调用接口下载多媒体源文件时，如果在下载过程中想取消下载，可以调用此接口来实现。
取消下载不一定是会成功的。

```
/*!
 * @abstract 取消正在下载的多媒体文件
 *
 * @discussion 对于正在下载的多媒体源文件，可以调用此接口取消下载，现只能取消下载：大图、文件、视频等；下载接口的回调里会返回对应的错误码和错误信息。
 *
 * @since 3.8.1
 */
- (void)cancelDownloadOriginMedia;
```

### 撤回消息
由消息发送方发起调用，在一定时间内，SDK 可以撤回会话中某条消息。

#### 消息撤回接口
+ JMSGMessage

```
/*!
 * @abstract 消息撤回
 *
 * @param message 需要撤回的消息
 * @param handler 结果回调
 *
 * - resultObject 撤回后的消息
 * - error        错误信息
 *
 * @discussion 注意：SDK可撤回3分钟内的消息
 */
+ (void)retractMessage:(JMSGMessage *)message completionHandler:(JMSGCompletionHandler)handler;
```
+ JMSGConversation

```
/*!
 * @abstract 消息撤回
 *
 * @param message 需要撤回的消息
 * @param handler 结果回调
 *
 * - resultObject 撤回后的消息
 * - error        错误信息
 *
 * @discussion 注意：SDK可撤回3分钟内的消息
 */
- (void)retractMessage:(JMSGMessage *)message completionHandler:(JMSGCompletionHandler)handler;
```

#### 消息撤回事件
消息发送方发起撤回后，上层会收到一条事件通知 [JMSGMessageRetractEvent](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveMessageRetractEvent:)，具体事件处理方式见[事件处理](./event#message-retract-event)一节

**注意：** 无论是撤回方还是被撤回方，消息被撤回后，对应 message content 会被替换为[JMSGPromptContent](./jmessage_ios_appledoc_html/Classes/JMSGPromptContent.html)类型，消息之前内容变成不可见。


### 消息转发
+ JMSGMessage 

```
/*!
 * @abstract 消息转发
 *
 * @param message         需要转发的消息
 * @param target          目标 target，只能为 JMSGUser 或 JMSGGroup
 * @param optionalContent 可选功能，具体请查看 JMSGOptionalContent 类
 *
 * @discussion 注意：只能转发消息状态为 SendSucceed 和 ReceiveSucceed 的消息。
 */
+ (void)forwardMessage:(JMSGMessage *)message
                target:(id)target
       optionalContent:(JMSGOptionalContent *JMSG_NULLABLE)optionalContent;
```

### 消息已读回执
SDK 支持对单条消息设置已读回执，即：可以查看某条消息已读、未读的用户和数量，默认行为为 NO.

#### 已读回执设置
已读回执设置是在发送消息时设置的，通过 `JMSGOptionalContent` 设置

```
@interface JMSGOptionalContent : NSObject
/*!
 * @abstract 设置这条消息的发送是否需要对方发送已读回执，NO，默认值
 */
@property(nonatomic, assign) BOOL needReadReceipt;
@end
```

发送消息时设置请查看 [附带控制参数的发送接口](#send-message-option)

#### 获取当前未发送已读回执的人数
即：当前未读该条消息的人数

```
/*!
 * @abstract 消息未读人数
 *
 * @discussion 只针对消息发送方有效
 *
 * 注意：只有发送方调用 [+sendMessage:optionalContent:] 方法设置 message 需要已读回执，此方法才有意义。
 */
- (NSInteger)getMessageUnreadCount;
```

#### 获取当前已读回执详情
当一条需要接收方发送已读回执的消息成功发出之后，消息发送方可以查看这条消息当前已读回执的详情.详情中包含当前已发送已读回执和未发送已读回执的用户 `JMSGUser` 列表等信息 

```
/*!
 * @abstract 已读未读用户列表
 *
 * @param handler 结果回调。回调参数:
 *
 * - unreadUsers  未读用户列表
 * - readsUsers   读用户列表
 * - error        不为nil表示出错
 *
 * @discussion 只针对消息发送方有效
 *
 * 注意：只有发送方调用 [+sendMessage:optionalContent:] 方法设置 message 需要已读回执，此方法才有意义。
 */
- (void)messageReadDetailHandler:(void(^)(NSArray *JMSG_NULLABLE readUsers, NSArray *JMSG_NULLABLE unreadUsers, NSError *JMSG_NULLABLE error))handler;
```

#### 消息接收方将消息标记为已读
对于消息接收方，可以将一条消息标记为已读，标记成功后，这条消息的已读状态会记录在本地。
当这条消息是一条需要已读回执的消息时，SDK 还将主动发送一个通知事件 [JMSGMessageReceiptStatusChangeEvent](./jmessage_ios_appledoc_html/Classes/JMSGMessageReceiptStatusChangeEvent.html) 给消息发送方，通知对方这条消息的已读回执人数发生变化。  
注意：这个已读状态只会保存在本地，当本地数据被清除，或者用户更换设备登陆之后，已读状态会被重置为false。 

```
/*!
 * @abstract 设置为已读
 *
 * @param handler 回调
 *
 * - resultObject 返回对应的 message，不过成功失败都会返回 message 对象
 * - error        不为 nil 表示操作失败
 *
 * @discussion 注意: 只针对消息接收方有效
 * 
 * 这是一个异步接口;
 *
 * 1、接收方：设置消息为已读状态后，isHaveRead 属性也会被设置为 YES，
 *
 * 2、发送方：会收到消息已读状态变更事件，SDK 会更新消息的未读人数。
 *
 * 注意：只有发送方调用 [+sendMessage:optionalContent:] 方法设置 message 需要已读回执，此方法才有效。
 */
- (void)setMessageHaveRead:(JMSGCompletionHandler)handler;
```

#### 消息回执状态变更事件

```
JMSGMessageReceiptStatusChangeEvent
```

对于消息发送方发送的需要接收方发送已读回执的消息，接收方通过`[message setMessageHaveRead:]` 接口成功发送已读回执后，SDK 会上抛这个事件通知消息发送方。发送方通过这个事件可以知道是哪个会话中的哪条消息的未回执人数发生了变化。  
具体处理方法见[事件处理](./event#message-receipt-change-event)一节

### 本地消息记录获取
+ 获取所有消息

```
/*!
 * @abstract 异步获取所有消息记录
 *
 * @param handler 结果回调。正常返回时 resultObject 类型为 NSArray，数据成员类型为 JMSGMessage。
 *
 * @discussion 排序规则：最新
 */
- (void)allMessages:(JMSGCompletionHandler)handler;
```

+ 获取单条消息

```
/*!
 * @abstract 获取某条消息
 *
 * @param msgId 本地消息ID
 *
 * @discussion 这个接口在正常场景下不需要单独使用到. 获取消息一般应使用 [JSMGConversation messageArrayFromNewestWithOffset::]
 *
 * 注意: 这里的 msgId 概念同 [JMSGMessage msgId], 是本地生成的消息ID, 而非 [JMSGMessage serverMessageId]
 */
- (JMSGMessage * JMSG_NULLABLE)messageWithMessageId:(NSString *)msgId;
```

+ 批量获取消息

```
/*!
 * @abstract 同步分页获取最新的消息
 *
 * @param offset 开始的位置。nil 表示从最初开始。
 * @param limit 获取的数量。nil 表示不限。
 *
 * @return 返回消息列表（数组）。数组成员的类型是 JMSGMessage*
 *
 * @discussion 排序规则是：最新
 *
 * 参数举例：
 *
 * - offset = nil, limit = nil，表示获取全部。相当于 allMessages。
 * - offset = nil, limit = 100，表示从最新开始取 100 条记录。
 * - offset = 100, limit = nil，表示从最新第 100 条开始，获取余下所有记录。
 */
- (NSArray JMSG_GENERIC(__kindof JMSGMessage *) *)messageArrayFromNewestWithOffset:(NSNumber *JMSG_NULLABLE)offset limit:(NSNumber *JMSG_NULLABLE)limit;
```

### 命令透传
命令透传发送的命令后台不会为其离线保存，只会在对方用户在线的前提下将命令推送给对方。SDK 收到命令之后也不会本地保存，不发送通知栏通知，整体快速响应。  

开发者可以通过命令透传拓展一些在线场景下的辅助功能，如：实现输入状态提示、控制其他端下线等。

#### 发送会话间的命令透传

+ JMSGConversaion

```
/*!
 * @abstract 消息透传
 *
 * @param transparentText 用户自定义透传内容，仅限 NSString 类型
 * @param handler 回调，error=nil 表示成功
 *
 * @discussion 注意：
 *
 *  1. 消息透传功能，消息不会进入到后台的离线存储中去，仅当对方用户当前在线时才会成功送达，可以快速响应，方便开发者拓展自定义行为；
 *
 *  2. 可用来快速实现一些在线场景下的辅助功能 ：输入状态提示、位置信息提示、开发者自定义等。
 *
 *  3. 透传命令到达是，接收方通过 [JMSGEventDelegate onReceiveMessageTransparentEvent:] 方法监听
 */
- (void)sendTransparentMessage:(NSString *JMSG_NONNULL)transparentText
             completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 发送设备间的透传命令

+ JMessage

```
/*!
 * @abstract 发送透传消息给自己在线的其他设备
 *
 * @param message   发送的内容
 * @param platform  设备类型
 * @param handler   回调
 *
 * @discussion 注意：
 *
 *  1. 消息透传功能，消息不会进入到后台的离线存储中去，仅当对方用户当前在线时才会成功送达，SDK 不会将此类消息内容存储；
 *
 *  2. 透传命令到达是，接收方通过 [JMSGEventDelegate onReceiveMessageTransparentEvent:] 方法监听。
 *
 * @since 3.5.0
 */
+ (void)sendCrossDeviceTransMessage:(NSString *)message
                           platform:(JMSGPlatformType)platform
                            handler:(JMSGCompletionHandler)handler;
```    