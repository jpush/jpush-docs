I# IM SDK for iOS

### Summary 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM 整体的信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)。要集成 iOS SDK 请参考文档：[JMessage iOS 集成指南](../../guideline/jmessage_ios_guide)。


### Functions 功能

极光IM 最核心的功能是 IM 即时消息的功能。

+ 单聊，群聊；
+ 消息类型：文本、语音、图片；
+ 用户未在线时保存离线消息；
+ 保证消息及时下发；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

### API 接口

需要了解完整的 SDK API，有二种方式：

+ 直接查看 JMessage.framework 里的 Headers 文件。这些头文件定义了 SDK 提供的对外接口，带有完善的注释与说明，甚至样例代码。
+ 下载 docset 文档。我们使用 Appledoc 工具基于上述 Headers 文件生成了 docset。可以使用 Xcode 直接打开查看，或者使用 Dash 查看。我们建议使用 Dash 效果更好。

以下简要地列举 SDK API 提供的功能，同时简要地描述 API 的设计思路、使用场景。

#### 设计思路

- 能用同步返回的，尽可能同步返回，不用异步接口；
- 尽可能减少 App 的工作量。例如：媒体文件的路径维护、下载更新等；

#### 初始化 JMessage.h

需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。

```
+ (void)setupJMessage:appKey:channel:apsForProduction:category:
```

这个调用是必须的。否则 SDK 将不能正常工作。

#### 结果回调

JMessage SDK 提供的很多接口都以异步方式返回，其回调都是一个类型为 JMSGCompletionHandler 的 block，其定义为

		typedef void (^JMSGCompletionHandler)(id resultObject, NSError *error);

JMSGCompletionHandler 有 2 个参数：

+ id resultObject 返回的结果对象
+ NSError *error 返回的错误

如果 error 不为 nil，则表示调用出错，error -> code 定义了错误码，error -> description 有错误的详细说明。也可以从文档里根据错误码找到进一步的错误说明信息。

如果 error 为 nil，则调用成功，resultObject 是返回结果对象。每个接口 resultObject 的实际类型不同，在每个接口的定义文档里会指定。实际使用时，应把该 resultObject 转型为该接口的正常对象。

与 JMSGCompletionHandler 类似的，还有另外一个 block 叫 JMSGAsyncDataHandler，用于返回媒体文件数据。

#### 注册与登录、用户信息 JMSGUser.h

```

// 新用户注册
+ (void)registerWithUsername:password:completionHandler:

// 用户登录
+ (void)loginWithUsername:password:completionHandler:

// 当前用户退出登录
+ (void)logoutWithCompletionHandler:

// 获取我的信息（当前登录用户）
+ (JMSGUser *)getMyInfo

// 获取用户详情（批量接口）
+ (void)userInfoArrayWithUsernameArray:completionHandler:

// 更新我的信息（当前登录用户）
// 只支持每次更新一个 UserInfo 字符。需要根据 type 去定义要更新的字段类型。
+ (void)updateMyInfoWithParameter:type:completionHandler:

// 更新密码（当前登录用户）
+ (void)updateMyPasswordWithNewPassword:oldPassword:completionHandler:

// 获取头像缩略图
- (void)thumbAvatarData:handler:

// 获取头像大图
- (void)largeAvatarData:handler:
```

#### 会话 JMSGConversation.h

```

// 获取单聊会话
+ (JMSGConversation *)singleConversationWithUsername:

// 获取群聊会话
+ (JMSGConversation *)groupConversationWithGroupId:

// 创建单聊会话
+ (vodi)createSingleConversationWithUsername:completionHandler:

// 创建群聊会话
+ (void)createGroupConversationWithGroupId:completionHandler:

// 删除单聊会话
+ (BOOL)deleteSingleConversationWithUsername:

// 删除群聊会话
+ (BOOL)deleteGroupConversationWithGroupId:

// 获取全部会话列表
// 暂未提供分页方式。性能上考虑了优化，应该不会有问题
+ (void)allConversations:

// 获取单条消息
- (JMSGMessage *)messageWithMessageId:
- 
// 获取多条消息（同步接口）
// 建议使用这个接口时，每次取出的条数（limit）不要太大，否则可能存在性能问题

- (NSArray)messageArrayFromNewestWithOffset:limit:

// 获取全部消息（异步接口）
// 一次性取出来一个会话里全部消息。如果预计消息条数不是太多，可以使用此接口。使用上相对简单。
- (void)allMessages:

// 删除全部消息
- (BOOL)deleteAllMessages:

// 创建消息对象
// 需要先创建消息内容（content）。这是同步接口，创建媒体消息尤其是图片时可能会卡。
- (JMSGMessage *)createMessageWithContent:

// 创建消息对象
// 异步接口，专用于创建图片消息，因为创建消息时 SDK 要保存到文件，并且要做缩略图，有一定的性能损耗
- (void)createMessageAsyncWithImageContent:completionHandler:

// 发送消息。基于创建好的消息对象
- (void)sendMessage:

// 发送文本消息。不需要预先创建好消息对象。
- (vodi)sendTextMessage:

// 发送图片消息。不需要预先创建好消息对象。
- (void)sendImageMessage:

// 发送语音消息。不需要预先创建好消息对象。
- (void)sendVoiceMessage:duration:

// 获取会话头像
- (void)avatarData:

// 清除会话未读数
- (vodi)clearUnreadCount

// 获取最后一条消息的文本描述。一般用于显示在会话列表上
- (NSString *)latestMessageContentText

// 判断某条消息是否属于当前会话
- (BOOL)isMessageForThisConversation:

// 刷新会话对象的信息（从服务器）
- (void)refreshTargetInfoFromServer:

```

#### 消息 JMSGMessage.h

```

// 创建单聊消息
+ (JMSGMessage *)createSingleMessageWithContent:username:

// 创建群聊消息
+ (JMSGMessage *)createGroupMessageWithContent:groupId:

// 发送消息。发送创建好的消息对象
+ (void)sendMessage:

// 发送单聊文本消息
// 如果最简单地使用 SDK 的发消息功能，这是最快捷的方式：不必先获取会话，不必先创建 JMSGMessage 对象
+ (void)sendSingleTextMessage:username:

// 发送单聊图片消息
+ (void)sendSingleImageMessage:username:

// 发送单聊语音消息
+ (void)sendSingleVoiceMessage:voiceDuration:username:

// 发送群聊文本消息
+ (void)sendGroupTextMessage:groupId:

// 发送群聊图片消息
+ (void)sendGroupImageMessage:groupId:

// 发送群聊语音消息
+ (void)sendGroupVoiceMessage:voiceDuration:groupId:

// 设置消息的来源用户
- (void)setFromName:

// 更新消息标志
- (void)updateFlag:

// 获取消息的 JSON 字符串
- (NSString *)toJsonString
```


#### 群组 JMSGGroup.h

```

// 创建群组
+ (void)createGroupWIthName:desc:memberArray:completionHandler:

// 更新群组信息
+ (void)updateGroupInfoWIthGroupId:name:desc:completionhandler:

// 获取群组详情（不包含群组成员）
+ (void)groupInfoWithGroupId:completionHandler:

// 获取我的群组列表
+ (vodi)myGroupArray:

// 获取当前群组成员列表
- (NSArray *)memberArray

// 添加群组成员
- (void)addMembersWithUsernameArray:completionHandler:

// 删除群组成员
- (void)removeMembersWithUsernameArray:completionHandler:

// 退出群组（当前用户）
- (void)exit:

// 获取展示名称
- (NSString *)displayName 

```

### Example 代码样例

更多样例请参考 JChat 开放源代码项目。

#### 单聊发文本消息

```
NSString *text = @"Hello, JMessage";
NSString *username = @"alice";

// 最简单的方式
[JMSGMessage sendSingleTextMessage:text];

// 要为消息内容附加字段
JMSGTextContent *textContent = [[JMSGTextContent alloc] initWIthText:text];
[textConent addStringExtra:@"extraValue" forKey:@"extraKey"];

// 不关注会话的情况
JMSGMessage *message = [JMSGMessage createSingleMessageWithContent:textContent username:username];
[JMSGMessage sendMessage:message];

// 要处理会话的情况
JMSGConversation *conv = [JMSGConversation createSingleConversationWithUsername:username];
JMSGMessage *message2 = [conv createMessageWithContent:textContent];
[conv sendMessage:message2];

```


### See Also 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [JMessage iOS 集成指南](../../guideline/jmessage_ios_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)

