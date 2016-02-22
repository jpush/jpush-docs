# IM SDK for iOS

+ [极光IM iOS 错误码](../client/im_errorcode/#jmessage-ios)

### Summary 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)。要集成 iOS SDK 请参考文档：[JMessage iOS 集成指南](../../guideline/jmessage_ios_guide)。


### Functions 功能

极光IM 最核心的功能是 IM 即时消息的功能。

+ 保证消息及时下发；
+ 单聊，群聊；
+ 消息类型：文本、语音、图片；
+ 用户未在线时保存离线消息；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

### API 接口
#### 初始化

JMessage.h 里定义的 setupJMessage 方法，需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。


```
JMessage.h

+ (void)setupJMessage:(NSDictionary *)launchOptions
               appKey:(NSString *)appKey
              channel:(NSString *)channel
     apsForProduction:(BOOL)isProduction
             category:(NSSet *)category;
```
参数说明

+ launchOptions 启动参数。可直接传 AppDelegate 的启动参数
+ appKey 必填。极光 AppKey，用于唯一地标识应用。
+ channel 发行渠道。可不填。
+ isProduction 当前App的发布状态。如果是上线 Apple Store，应该为 YES。
+ category APNs推送的启动参数

#### 通知监听

JMessage SDK 采用 Delegate 的机制给 App 发通知，而不是采用 iOS 平台通用的通知方式。Delegate 的方式更加直接、易用。

可以在 App 的任何类里，调用以下方法来监听事件通知。

	[JMessage addDelegate:self withConversation:nil]

为了上述这行有效，则需要在当前类的头文件里声明实现 JMessageDelegate 协议。以下示例在 AppDelegate 里加监听。

	@interface AppDelegate : UIResponder <UIApplicationDelegate,JMessageDelegate>

监听通知上述 2 个动作外，另外一个动作就是实现你需要监听的事件的方法。比如监听数据库升级：

	- (void)onDBMigrateStart {
	  NSLog(@"onDBmigrateStart in appdelegate");
	  _isDBMigrating = YES;
	}

由于 JMessage SDK 会在 setup 时检测数据库升级，如果有需要就发出通知。所以建议在 AppDelegate 里调用 setupJMessage 之前就添加监听。

另外一个建议在 AppDelegate 里监听的通知是当前用户被踢出登录。

	- (void)onLoginUserKicked;

#### 结果回调

#### 结果回调

JMessage SDK 提供的大部分接口都以异步方式返回，其回调都是一个类型为 JMSGCompletionHandler 的 block。

JMSGCompletionHandler 有 2 个参数：

+ id resultObject 返回的结果对象
+ NSError *error 返回的错误

如果 error 不为 nil，则表示调用出错，error -> code 定义了错误码，error -> description 有错误的详细说明。也可以从文档里根据错误码找到进一步的错误说明信息。

如果 error 为 nil，则调用成功，resultObject 是返回结果对象。每个接口 resultObject 的实际类型不同，在每个接口的定义文档里会指定。实际使用时，应把该 resultObject 转型为该接口的正常对象。

#### 注册与登录

相应的头文件： JMSGUser.h

##### 注册

```
+ (void)registerWithUsername:(NSString *)username
                    password:(NSString *)password
           completionHandler:(JMSGCompletionHandler)handler;
           
```
参数说明

+ NSString* username 用户名，或者说用户帐号。长度 4~128 位，支持的字符：字母、数字、下划线、英文减号、英文点、@符号，首字母只允许是字母或者数字。
+ NSString* password 用户密码。长度 4~128 位，字符不限。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也是 nil。

##### 登录

```
+ (void)loginWithUsername:(NSString *)username
                 password:(NSString *)password
        completionHandler:(JMSGCompletionHandler)handler;

```
参数说明

+ NSString* username 用户名。定义参照注册接口。
+ NSString* password 用户密码。定义参照注册接口。
* JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也是 nil。

##### 登出

```
+ (void)logoutWithCompletionHandler:(JMSGCompletionHandler)handler;
```

#### 获取用户信息

```
+ (void)getUserInfoWithUsername:(NSString *)username
              completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* username 用户名。
+ JMSGCompletionHandler handler 结果回调。resultObject 对象类型为 JMSGUser。

##### 获取我的信息

```
+ (JMSGUser *)getMyInfo;
```

参数说明

+ 无

结果返回

+ 用户对象

##### 获取原始头像

```
+ (void)getOriginAvatarImage:(JMSGUser *)userInfo
           completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ JMSGUser* userInfo 待获取头像的用户
+ JMSGCompletionHandler handler 结果回调。resultObject 对象类型为 JMSGUser，其中大图的本地路径。

##### 更新我的信息

```
+ (void)updateMyInfoWithParameter:(id)parameter
                         withType:(JMSGUpdateUserInfoType)type
                completionHandler:(JMSGCompletionHandler)handler;           
```
参数说明

+ id parameter 更新的值。除 kJMSGGender 性别类型，需要传入 JMSGUserGender 包装成 NSNumber 的对象，其他类型传 NSString 类型的对象。
+ JMSGUpdateUserInfoType 用户属性类型。这是一个 enum 类型。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也是 nil。

##### 更新我的密码

```
+ (void)updatePasswordWithNewPassword:(NSString *)newPassword
                          oldPassword:(NSString *)oldPassword
                    completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* username 新密码
+ NSString* password 旧密码
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也是 nil。


#### 聊天会话

相应的头文件： JMSGConversation.h

##### 获取某条消息

```
- (void)getMessage:(NSString *)messageId
 completionHandler:(JMSGCompletionHandler)handler;
```

参数说明 

+ NSString* messageId 消息ID。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 JMSGMessage。

##### 获取全部消息

// 当前用户退出登录
+ (void)logout:

// 获取我的信息（当前登录用户）
+ (JMSGUser *)myInfo

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSArray<JMSGMessage>。

// 更新我的信息（当前登录用户）
// 只支持每次更新一个 UserInfo 字符。需要根据 type 去定义要更新的字段类型。
+ (void)updateMyInfoWithParameter:userFieldType:completionHandler:

```
- (void)deleteAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;
```

// 获取头像缩略图
- (void)thumbAvatarData:

// 获取头像大图
- (void)largeAvatarData:

// 展示名
- (NSString *)displayName

```

参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也为 nil。

##### 获取某个会话

```
+ (void)getConversation:(NSString *)targetId
               withType:(JMSGConversationType)conversationType
      completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* targetId 会话对象ID。单聊为 username，群聊为 gid（群组ID）。
+ JMSGConversationType conversationType 会话类型。可选为：单聊、群聊。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 JMSGConversation。

##### 创建会话

```
+ (void)createConversation:(NSString *)targetId
                  withType:(JMSGConversationType)conversationType
         completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* targetId 会话对象ID。单聊为 username，群聊为 gid（群组ID）。
+ JMSGConversationType conversationType 会话类型。可选为：单聊、群聊。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 JMSGConversation。

##### 删除会话

```
+ (void)deleteConversation:(NSString *)targetId
                  withType:(JMSGConversationType)conversationType      
         completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* targetId 会话对象ID。单聊为 username，群聊为 gid（群组ID）。
+ JMSGConversationType conversationType 会话类型。可选为：单聊、群聊。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 JMSGConversation。

// 获取单条消息
- (JMSGMessage *)messageWithMessageId:
 
// 获取多条消息（同步接口）
// 建议使用这个接口时，每次取出的条数（limit）不要太大，否则可能存在性能问题

```
+ (void)getConversationListWithCompletionHandler:(JMSGCompletionHandler)handler;

```
参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSArray<JMSGConversation>。

// 删除单条消息
- (BOOL)deleteMessageWithMessageId:(NSString *)msgId

// 删除全部消息
- (BOOL)deleteAllMessages:

#### 聊天消息

相应的头文件： JMSGMessage.h

##### 发送消息

```
+ (void)sendMessage:(JMSGMessage *)message;
```

参数说明

+ JMSGMessage* message 待发送的消息。JMSGMessage 有多个子类，分别表示不同的消息类型，如：文本、图片、语音。

##### 下载图片消息原图

```
+ (void)downloadOriginImage:(JMSGImageMessage *)message
               withProgress:(NSProgress *)progress
          completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ JMSGImageMessage* message 图片消息
+ NSProgress* progress 下载进度
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSURL，内容为图片文件路径。

##### 下载图片消息缩略图

默认收到图片消息时 SDK 会自动下载缩略图。

如果自动下载失败，则 App 可以发起再次下载。

```
+ (void)downloadThumbImage:(JMSGImageMessage *)message
              withProgress:(NSProgress *)progress
         completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ JMSGImageMessage* message 图片消息
+ NSProgress* progress 下载进度
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSURL，内容为图片文件路径。

##### 下载语音消息文件

默认收到语音消息时 SDK 会自动下载语音文件。

如果自动下载失败，则 App 可以发起再次下载。

```
+ (void)downloadVoice:(JMSGVoiceMessage *)message
         withProgress:(NSProgress *)progress
    completionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ JMSGVoiceMessage* message 图片消息
+ NSProgress* progress 下载进度
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSURL，内容为语音文件路径。

#### 群组维护

// 发送单聊文本消息
// 如果最简单地使用 SDK 的发消息功能，这是最快捷的方式：不必先获取会话，不必先创建 JMSGMessage 对象
+ (void)sendSingleTextMessage:toUser:

// 发送单聊图片消息
+ (void)sendSingleImageMessage:toUser:

// 发送单聊语音消息
+ (void)sendSingleVoiceMessage:voiceDuration:toUser:

// 发送群聊文本消息
+ (void)sendGroupTextMessage:toGroup:

// 发送群聊图片消息
+ (void)sendGroupImageMessage:toGroup:

// 发送群聊语音消息
+ (void)sendGroupVoiceMessage:voiceDuration:toGroup:

```
+ (void)createGroup:(JMSGGroup *)group
  completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ JMSGGroup* group 待创建的群组。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultOjbect 内容也为 nil。

// 获取消息的 JSON 字符串
- (NSString *)toJsonString
- 
```

参数说明

+ JMSGGroup* group 待更新的群组信息
+ JSMGCompletionHandler handler 结果回调。正常返回时 resultObject 内容也为 nil。

##### 获取群组信息

```
+ (void)getGroupInfo:(NSString *)groupId
   completionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ NSString* groupId 群组ID。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 JMSGGroup。

##### 我退出群组

```
+ (void)exitGoup:(NSString *)groupId
    completionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ NSString* groupId 待退出的群组。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 内容也为 nil。

##### 增加群组成员

```
+ (void)addMembers:(NSString *)groupId
           members:(NSString *)members
 completionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ NSString* groupId 群组ID。
+ NSString* members 群组成员。成员使用 username，多个用逗号隔开。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 内容也为 nil。

// 获取展示名称
- (NSString *)displayName 
```

### 实现回调 
#### Conversation 回调
```
// optional
// 收到此通知后, 建议处理: 如果 App 当前在会话列表页，刷新整个列表；如果在聊天界面，刷新聊天标题。
- (void)onConversationChanged:(JMSGConversation *)conversation;

// optional
// 未读消息数变更
- (void)onUnreadChanged:(NSUInteger)newCount;
```

#### Group 回调
```
// optional
// 群信息详情被改变
- (void)onGroupInfoChanged:(JMSGGroup *)group;
```

#### User 回调
```
// optional
// 用户在其他设备上登录，当前设备被踢出登录。
- (void)onLoginUserKicked;
```

#### Database Migrate 回调
```
// optional
// 数据库开始升级
 (void)onDBMigrateStart;

// optional
// 数据库升级结束，如果 Error 为 nil 代表升级成功，否则为失败
- (void)onDBMigrateFinishedWithError:(NSError *)error;
```
+ (void)deleteGroupMember:(NSString *)groupId
                  members:(NSString *)members
        completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* groupId 群组ID。
+ NSString* members 需要加入的群组成员(username)。多个成员时使用,(逗号)隔开。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 内容也为 nil。


##### 获取群组成员列表

```
+ (void)getGroupMemberList:(NSString *)groupId
         completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ NSString* groupId 群组ID。
+ JMSGCompletionHandler handler 结果回调。正常返回时resultObject对象类型为NSArray，成员为JMSGGroup类型。


### Example 代码样例

#### 发文本消息

```
JMSGContentMessage *message = [[JMSGContentMessage alloc] init];
message.target_name = @"javen";
message.contentText = @"Hello";
[JMSGMessageManager sendMessage:message];
```



### See Also 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [JMessage iOS 集成指南](../../guideline/jmessage_ios_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)

