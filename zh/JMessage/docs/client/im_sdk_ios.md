# IM SDK for iOS

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

需要了解完整的 SDK API，有三种方式：

+ 直接查看 JMessage.framework 里的 Headers 文件。这些头文件定义了 SDK 提供的对外接口，带有完善的注释与说明，甚至样例代码。
+ 下载 docset 文档。我们使用 Appledoc 工具基于上述 Headers 文件生成了 docset。可以使用 Xcode 直接打开查看，或者使用 Dash 查看。我们建议使用 Dash 效果更好。
+ 使用 Appledoc 生成的文档的在线版本：[JMessage iOS SDK APIs](jmessage_ios_appledoc_html/)

以下简要地列举 SDK API 提供的功能，同时简要地描述 API 的设计思路、使用场景。

#### 设计思路

- 能用同步返回的，尽可能同步返回，不用异步接口；
- 尽可能减少 App 的工作量。例如：媒体文件的路径维护、下载更新等；

#### 初始化

JMessage.h 里定义的 setupJMessage 方法，需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。

```
+ (void)setupJMessage:appKey:channel:apsForProduction:category:
```

这个调用是必须的。否则 SDK 将不能正常工作。

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
+ (void)logout:

// 获取我的信息（当前登录用户）
+ (JMSGUser *)myInfo

// 获取用户详情（批量接口）
+ (void)userInfoArrayWithUsernameArray:completionHandler:

// 更新我的信息（当前登录用户）
// 只支持每次更新一个 UserInfo 字符。需要根据 type 去定义要更新的字段类型。
+ (void)updateMyInfoWithParameter:userFieldType:completionHandler:

// 更新密码（当前登录用户）
+ (void)updateMyPasswordWithNewPassword:oldPassword:completionHandler:

// 获取头像缩略图
- (void)thumbAvatarData:

// 获取头像大图
- (void)largeAvatarData:

// 展示名
- (NSString *)displayName

```

#### 会话 JMSGConversation.h

```

// 获取单聊会话
+ (JMSGConversation *)singleConversationWithUsername:

// 获取群聊会话
+ (JMSGConversation *)groupConversationWithGroupId:

// 创建单聊会话
+ (void)createSingleConversationWithUsername:completionHandler:

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
 
// 获取多条消息（同步接口）
// 建议使用这个接口时，每次取出的条数（limit）不要太大，否则可能存在性能问题

- (NSArray)messageArrayFromNewestWithOffset:limit:

// 获取全部消息（异步接口）
// 一次性取出来一个会话里全部消息。如果预计消息条数不是太多，可以使用此接口。使用上相对简单。
- (void)allMessages:

// 删除单条消息
- (BOOL)deleteMessageWithMessageId:(NSString *)msgId

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

// 设置消息的来源用户
- (void)setFromName:

// 更新消息标志
- (void)updateFlag:

// 获取消息的 JSON 字符串
- (NSString *)toJsonString
- 
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


### 针对跨应用的变更

#### JMSGConverstaion
```
// 获取跨应用单聊会话
+ (JMSGConversation * JMSG_NULLABLE)singleConversationWithUsername:(NSString *)username
                                                            appKey:(NSString *)userAppKey;

// 创建跨应用单聊会话
+ (void)createSingleConversationWithUsername:(NSString *)username
                                      appKey:(NSString *)userAppKey
                           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;

// 删除跨应用单聊会话
+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username
                                      appKey:(NSString *)userAppKey;

// 会话目标用户所在的 appKey
@property(nonatomic, strong, readonly) NSString *targetAppKey;

```

#### JMSGMessage
```
// 消息发送目标应用
@property(nonatomic, strong, readonly) NSString *targetAppKey;

// 消息来源用户 Appkey
@property(nonatomic, strong, readonly) NSString *fromAppKey;

/*!
 * @abstract 发送跨应用单聊文本消息
 *
 * @param text 文本内容
 * @param username 单聊对象 username
 *
 * @discussion 快捷方法，不需要先创建消息而直接发送。
 */
+ (void)sendSingleTextMessage:(NSString *)text
                       toUser:(NSString *)username
                       appKey:(NSString *)userAppKey;
                       
/*!
 * @abstract 发送跨应用单聊图片消息
 *
 * @param imageData 图片数据
 * @param username 单聊对象 username
 *
 * @discussion 快捷方法，不需要先创建消息而直接发送。
 */
+ (void)sendSingleImageMessage:(NSData *)imageData
                        toUser:(NSString *)username
                        appKey:(NSString *)userAppKey;
           
/*!
 * @abstract 发送跨应用单聊语音消息
 *
 * @param voiceData 语音数据
 * @param duration 语音时长
 * @param username 单聊对象 username
 *
 * @discussion 快捷方法，不需要先创建消息而直接发送。
 */
+ (void)sendSingleVoiceMessage:(NSData *)voiceData
                 voiceDuration:(NSNumber *)duration
                        toUser:(NSString *)username
                        appKey:(NSString *)userAppKey;

```

#### JMSGUser
```
// 批量获取跨应用的用户信息
+ (void)userInfoArrayWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                                appKey:( NSString *JMSG_NULLABLE)userAppKey
                     completionHandler:(JMSGCompletionHandler)handler;


// 此用户所在的 appKey
@property(nonatomic, copy, readonly) NSString * JMSG_NULLABLE appKey;
```

#### JMSGGroup
##### 添加群组跨应用成员

```
/*!
 * @abstract 添加群组跨应用成员
 *
 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                             appKey:userAppKey
                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
                  
```
###### 例子

```
[group addMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被添加用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 添加群组跨应用成员 成功");
    }
}];

```
##### 删除群组跨应用成员

```
/*!
 * @abstract 删除群组跨应用成员
 *
 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                                appKey:userAppKey
                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;

```
###### 例子

```
[group removeMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被删除用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 添删除组跨应用成员 成功");
    }
}];

```
	
### 免打扰

#### JMessage
##### 免打扰列表

```
/*!
 * @abstract 用户免打扰列表
 *
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser、JMSGGroup
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 从服务器获取，返回用户的免打扰列表。
 */
+ (void)noDisturbList:(JMSGCompletionHandler)handler;
```
	
###### 例子

```
//获取当前用户免打扰列
[JMessage noDisturbList:^(id resultObject, NSError *error) {
     if (!error) {
         NSLog(@"\n 免打扰列表: \n %@",resultObject);
     }
 }];
 
```  
##### 全局免打扰设置

```
/*!
 * @abstract 判断是否设置全局免打扰
 *
 * @return YES/NO
 */
+ (BOOL)isSetGlobalNoDisturb;

/*!
 * @abstract 设置是否全局免打扰
 *
 * @param isNoDisturb 是否全局免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应返回对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 此函数为设置全局的消息免打扰
 */
+ (void)setIsGlobalNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;

```

###### 例子
 
```
 //获取是否设置全局免打扰
 BOOL isNoDisturb = [JMessage isSetGlobalNoDisturb];
 //设置全局免打扰（开启：YES,关闭:NO）
 [JMessage setIsGlobalNoDisturb:!isNoDisturb handler:^(id resultObject, NSError *error) { 
     if (!error) {
         NSLog(@"\n 全局免打扰设置成功:\n%@",resultObject);
     }
 }];
 
```
	 
#### JMSGUser
##### 用户免打扰设置

```
/*!
 * @abstract 该用户是否已被设置为免打扰
 *
 * @discussion YES:是 , NO: 否
 */
@property(nonatomic, assign, readonly) BOOL isNoDisturb;

/*!
 * @abstract 设置用户免打扰（支持跨应用设置）
 *
 * @param isNoDisturb 是否全局免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 针对单个用户设置免打扰
 * 这个接口支持跨应用设置免打扰
 */
- (void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;

```

###### 例子

```
//获取 user 对象是否设置了免打扰
BOOL isAlreadSet = user.isNoDisturb;

//开启或关闭 user 免打扰设置
[user setIsNoDisturb:!isAlreadSet handler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n消息免打扰设置成功:\n%@\n",resultObject);
    }
}];
注：如果user对象已经开启(关闭)免打扰，再对user设置开启(关闭)免打扰，会返回失败，所以在设置设置免打扰时，先获取user对象的isNoDisturb值，再进行设置

```

#### JMSGGroup
##### 群组免打扰设置

```
/*!
 * @abstract 该群是否已被设置为免打扰
 *
 * @discussion YES:是 , NO: 否
 */
@property(nonatomic, assign, readonly) BOOL isNoDisturb;

/*!
 * @abstract 设置群组消息免打扰（支持跨应用设置）
 *
 * @param isNoDisturb 是否免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 针对单个群组设置免打扰
 * 这个接口支持跨应用设置免打扰
 */
- (void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;

```

###### 例子

```
使用方法参考“用户免打扰”例子

```

### 黑名单

#### JMessage
##### 获取黑名单列表

```
/*!
 * @abstract 黑名单列表
 *
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 从服务器获取，返回用户的黑名单列表。
 */
+ (void)blackList:(JMSGCompletionHandler)handler;

```
###### 例子

```
//获取黑名单列表
[JMessage blackList:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 黑名单列表: %@ \n",resultObject);
    }
}];

```

#### JMSGUser
##### 添加黑名单		

```
/*!
 * @abstract 添加黑名单
 * @param usernameArray 作用对象的username数组
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 可以一次添加多个用户
 */
+ (void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
          completionHandler:(JMSGCompletionHandler)handler;

```
###### 例子

```
//添加黑名单
[JMSGUser addUsersToBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 添加黑名单成功:%@ \n ",resultObject);
    }
}];

```
	
##### 删除黑名单	

```
/*!
 * @abstract 删除黑名单
 * @param usernameArray 作用对象的username数组
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 可以一次删除多个黑名单用户
 */
+ (void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
            completionHandler:(JMSGCompletionHandler)handler;

```	            
###### 例子

```
//删除黑名单
[JMSGUser delUsersFromBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            NSLog(@"\n 添加黑名单成功:%@ \n ",resultObject);
        }
    }];

```
	            
##### 跨应用添加黑名单	

```
/*!
 * @abstract 跨应用添加黑名单
 * @param usernameArray 作用对象的username数组
 * @param appKey 应用的appKey
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 可以一次添加多个用户
 */
+ (void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                     appKey:(NSString *)userAppKey
          completionHandler:(JMSGCompletionHandler)handler;

```
###### 例子

```
//添加黑名单
[JMSGUser addUsersToBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被添加用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
       if (!error) {
           NSLog(@"\n 跨应用添加黑名单成功:%@ \n ",resultObject);
       }
   }];

```	   
##### 跨应用删除黑名单	

```
/*!
 * @abstract 跨应用删除黑名单
 * @param usernameArray 作用对象的username数组
 * @param appKey 应用的appKey
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 可以一次删除多个黑名单用户
 */
+ (void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                       appKey:(NSString *)userAppKey
            completionHandler:(JMSGCompletionHandler)handler;

```
	            
###### 例子         

```
//删除黑名单
[JMSGUser delUsersFromBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被删除用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 跨应用删除黑名单成功:%@ \n ",resultObject);
    }
}];
 
```   
###  事件处理

__事件类型的消息内容__

* 服务器端下发的事件通知, 比如用户被踢下线,群组里加了人, SDK 作为一个特殊的消息类型处理
* SDK 以消息的形式通知到 App. 详情参见 JMessageDelegate

#### JMSGEventContent

```
/*!
 * @abstract 事件类型
 * @discussion 参考事件类型的定义 JMSGEventNotificationType
 */
@property(nonatomic, assign, readonly) JMSGEventNotificationType eventType;

//通知事件类型
typedef NS_ENUM(NSInteger, JMSGEventNotificationType) {
  /// 事件类型: 登录被踢
  kJMSGEventNotificationLoginKicked = 1,
  /// 事件类型: 群组被创建
  kJMSGEventNotificationCreateGroup = 8,
  /// 事件类型: 退出群组
  kJMSGEventNotificationExitGroup = 9,
  /// 事件类型: 添加新成员
  kJMSGEventNotificationAddGroupMembers = 10,
  /// 事件类型: 成员被踢出
  kJMSGEventNotificationRemoveGroupMembers = 11,
  /// 事件类型: 群信息更新
  kJMSGEventNotificationUpdateGroupInfo = 12,
};

```

##### 事件的文本描述 

```
/*!
 @abstract 展示此事件的文本描述

 @discussion SDK 根据事件类型，拼接成完整的事件描述信息。
 */
- (NSString * JMSG_NONNULL)showEventNotification;  

```

###### 例子

```	
if (message.contentType == kJMSGContentTypeEventNotification) {
     NSString *showText = [((JMSGEventContent *)message.content) showEventNotification];
}
//比如，在群group中，用户A邀请用户B加入了群,showText 如下：
//showText = "A邀请B加入了群组"

```

##### 自定义事件的文本描述

```
/*!
 * @abstract 获取事件发起者的用户名
 * @return 正常返回事件发起者的用户名，如果是系统事件则返回“系统消息”
 *
 * @discussion 如果设置了nickname，则返回nickname，否则返回username
 * 可以用于定制 event message，拼接成完整的事件描述信息。
 */
- (NSString *JMSG_NULLABLE)getEventFromUsername;

/*!
 * @abstract 获取事件作用对象用户名列表
 * @return 返回类型为 NSArray，数组成员为事件作用对象的用户名
 *
 * @discussion 如果设置了nickname，则返回nickname，否则返回username
 * 可以用于定制 event message，拼接成完整的事件描述信息。
 */
- (NSArray *JMSG_NULLABLE)getEventToUsernameList;

```

###### 例子

```
JMSGEventContent *eventContent = (JMSGEventContent*)message.content;
//获取发起事件的用户名
NSString *fromUsername = [eventContent getEventFromUsername];
//获取事件作用对象用户名列表
NSArray *toUsernameList = [eventContent getEventToUsernameList];
//根据事件类型，定制相应描述（以事件类型: 添加新成员为例子）
if(eventContent.eventType == kJMSGEventNotificationAddGroupMembers) {
	NSString *showText = [NSString stringWithFormat:@"%@邀请了%@加入了群聊",fromUsername,[toUsernameList componentsJoinedByString:@","]];
}

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

