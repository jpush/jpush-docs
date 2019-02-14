<h1>聊天室管理</h1>


## 概述

JMessage iOS SDK 从 3.4.0 版本开始提供聊天室功能，包括查询基本信息，加入聊天室，退出聊天室等。

+ 主要特点
	+ 聊天室的消息没有推送通知和离线保存
	+ 没有常驻成员的概念，只要进入聊天室即可接收消息，开始聊天
	+ 一旦退出聊天室，不再会接收到任何消息、通知和提醒
 
+ 发送消息
	+ 聊天室消息的发送与单聊、群聊是一样的，通用的发送接口

+ 接收消息
	+ 聊天室消息的接收与单聊、群聊做了区分，聊天室消息的接收将通过 `JMSGConversationDelegate` 类里的 [onReceiveChatRoomConversation:messages:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onReceiveChatRoomConversation:messages:) 方法通知到上层


<font color= SteelBlue>注意：进入聊天室会自动获取最近50条消息。客户端目前不支持创建聊天室</font>

### 聊天室对象
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">属性/方法</th>
      <th width="20px">类型/返回值</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >roomID</td>
      <td >NSString</td>
      <td >聊天室 id</td>
    </tr>
    <tr >
      <td >name</td>
      <td >NSString</td>
      <td >名称</td>
    </tr>
    <tr >
      <td >appkey</td>
      <td >NSString</td>
      <td >聊天室所属应用 AppKey</td>
    </tr>
    <tr >
      <td >desc</td>
      <td >NSString</td>
      <td >描述信息</td>
    </tr>
    <tr >
      <td >totalMemberCount</td>
      <td >NSInteger</td>
      <td >聊天室人数</td>
    </tr>
    <tr >
      <td >maxMemberCount</td>
      <td >NSString</td>
      <td >聊天室最大人数限制</td>
    </tr>
    <tr >
      <td >ctime</td>
      <td >NSNumber</td>
      <td >聊天室的创建时间</td>
    </tr>
  </table>
</div>

### 获取应用下聊天室列表
可以获取对应 AppKey 应用下的聊天室列表，不传 AppKey 则默认是当前应用。

```
/*!
 * @abstract 分页获取聊天室详情
 *
 * @param appKey  选填，为 nil 则获取当前应用下的聊天室
 * @param start   分页获取的下标，第一页从  index = 0 开始
 * @param count   一页的数量，每页最大值是 50
 * @param handler 结果回调. 正常返回时 resultObject 类型是 NSArray<JMSGChatRoom>
 *
 * @discussion 该接口总是向服务器端发起请求.
 */
+ (void)getChatRoomListWithAppKey:(NSString *JMSG_NULLABLE)appKey
                            start:(NSInteger)start
                            count:(NSInteger)count
                completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 获取当前用户加入的聊天室列表

```
/*!
 * @abstract 获取当前用户已加入的聊天室列表
 *
 * @param handler 结果回调. 正常返回时 resultObject 类型是 NSArray<JMSGChatRoom>
 *
 * @discussion 该接口总是向服务器端发起请求.
 */
+ (void)getMyChatRoomListCompletionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 查询指定roomID的聊天室信息

```
/*!
 * @abstract 获取聊天室详情
 *
 * @param roomIds   待获取详情的聊天室 ID 数组
 * @param handler   结果回调. 正常返回时 resultObject 类型是 NSArray<JMSGChatRoom>
 *
 * @discussion 该接口总是向服务器端发起请求.
 */
+ (void)getChatRoomInfosWithRoomIds:(NSArray *JMSG_NONNULL)roomIds
                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 进入聊天室
成功进入聊天室之后，会将聊天室中最近 50 条聊天记录同步下来，并上抛通知上层，上层可以通过  [onReceiveChatRoomConversation:messages:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onReceiveChatRoomConversation:messages:) 监听并获取返回的消息列表。

```
/*!
 * @abstract 加入聊天室
 *
 * @param roomId    聊天室 id
 * @param handler   结果回调. error = nil 表示加入成功，resultObject 为 JMSGConversation 类型
 *
 * @discussion 成功进入聊天室之后，会将聊天室中最近若干条聊天记录同步下来并以 onReceiveChatRoomConversation: 事件的形式通知到上层，进入聊天室会自动获取最近50条消息。
 */
+ (void)enterChatRoomWithRoomId:(NSString *JMSG_NONNULL)roomId
              completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 离开聊天室
注意：退出聊天室后获取不到任何消息和通知

```
/*!
 * @abstract 退出聊天室
 *
 * @param roomId    聊天室 id
 * @param handler   结果回调. error = nil 表示加入成功.
 *
 * @discussion 退出聊天室后获取不到任何消息和通知.
 */
+ (void)leaveChatRoomWithRoomId:(NSString *JMSG_NONNULL)roomId
              completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 获取聊天室会话

```
/*!
 * @abstract 返回聊天室 conversation 列表（异步,已排序）
 *
 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里成员的类型为 JMSGConversation
 *
 * @discussion 当前是返回所有的chatroom conversation 列表，不包括单聊和群聊会话，默认是已经排序。
 */
+ (void)allChatRoomConversation:(JMSGCompletionHandler)handler;
```

```
/*!
 * @abstract 获取聊天室会话
 *
 * @param roomId 聊天室 ID
 *
 * @discussion 如果会话还不存在，则返回 nil
 */
+ (JMSGConversation * JMSG_NULLABLE)chatRoomConversationWithRoomId:(NSString *)roomId;
```

### 创建聊天室会话

```
/*!
 * @abstract 创建聊天室会话
 *
 * @param roomId  聊天室 ID。
 * @param handler 结果回调。正常返回时 resultObject 类型为 JMSGConversation。
 *
 * @discussion 如果会话已经存在，则直接返回。如果不存在则创建。
 * 创建会话时如果发现该 roomId 的信息本地还没有，则需要从服务器端上拉取。
 * 如果从服务器上获取 roomId 的信息不存在或者失败，则创建会话失败。
 */
+ (void)createChatRoomConversationWithRoomId:(NSString *)roomId
                           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 删除聊天室会话

```
/*!
 * @abstract 删除聊天室会话
 *
 * @param roomId  聊天室 ID
 *
 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
 */
+ (BOOL)deleteChatRoomConversationWithRoomId:(NSString *)roomId;
```

### 聊天室消息
#### 聊天室消息发送
聊天室消息的发送接口与单聊、群里的发送接口是共用的，接口请查看[会话与消息 - 发送消息](./message#send-message)

#### 聊天室消息接收

```
/*!
 * @abstract 接收聊天室消息
 *
 * @param conversation 聊天室会话
 * @param messages      接收到的消息数组，元素是 JMSGMessage
 *
 * @discussion 注意：
 *
 * 接收聊天室的消息与单聊、群聊消息不同，聊天室消息都是通过这个代理方法来接收的。
 *
 * @since 3.4.0
 */
- (void)onReceiveChatRoomConversation:(JMSGConversation *)conversation
                             messages:(NSArray JMSG_GENERIC(__kindof JMSGMessage *)*)messages;
```

### 聊天室管理员
#### 添加
```
/*!
 * @abstract 添加黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @since 3.8.0
 */
- (void)addBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                           appKey:(NSString *JMSG_NULLABLE)appKey
                          handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
#### 删除
```
/*!
 * @abstract 删除黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @since 3.8.0
 */
- (void)deleteBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                              appKey:(NSString *JMSG_NULLABLE)appKey
                             handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
#### 获取列表
```
/*!
 * @abstract 聊天室的黑名单列表
 *
 * @param handler 结果回调. resultObject 是 NSArray 类型，元素是 JMSGUser
 *
 * @since 3.8.0
 */
- (void)chatRoomBlacklist:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 聊天室黑名单
#### 添加
```
/*!
 * @abstract 添加管理员
 *
 * @param usernames 用户名列表
 * @param appkey    用户 AppKey，不填则默认为本应用 AppKey
 * @param handler   结果回调。error 为 nil 表示成功.
 *
 * @discussion 注意：非 VIP 应用最多设置 15 个管理员，不包括群主本身
 *
 * @since 3.8.0
 */
- (void)addAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                       appKey:(NSString *JMSG_NULLABLE)appkey
                      handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
#### 删除
```
/*!
 * @abstract 删除管理员
 *
 * @param usernames 用户名列表
 * @param appkey    用户 AppKey，不填则默认为本应用 AppKey
 * @param handler   结果回调。error 为 nil 表示成功.
 *
 * @since 3.8.0
 */
- (void)deleteAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                          appKey:(NSString *JMSG_NULLABLE)appkey
                         handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
#### 获取列表
```
/*!
 * @abstract 管理员列表
 *
 * @param handler 结果回调. resultObject 是 NSArray 类型，元素是 JMSGUser
 *
 * @discussion 注意：返回列表中不包含房主.
 *
 * @since 3.8.0
 */
- (void)chatRoomAdminList:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 聊天室通知事件
聊天室事件目前有管理员变更事件、黑名单变更事件，具体事件详情和监听请查看[事件与代理 - 聊天室事件](./event#chatroom-event)

