# IM SDK for iOS
iOS SDK download coming soon. 
### Summary 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)


### Functions 功能

与 Android 集类似。

### API 接口

#### 初始化

需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。


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

```
- (void)getAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSArray<JMSGMessage>。

##### 删除全部消息

```
- (void)deleteAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 也为 nil。

##### 重置未读消息数

```
- (void)resetUnreadMessageCountWithCompletionHandler:(JMSGCompletionHandler)handle;
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

##### 获取会话列表

```
+ (void)getConversationListWithCompletionHandler:(JMSGCompletionHandler)handler;

```
参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSArray<JMSGConversation>。


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

相应的头文件： JMSGGroup.h

##### 获取我的群组列表

```
+ (void)getGroupListWithCompletionHandler:(JMSGCompletionHandler)handler;
```

参数说明

+ JMSGCompletionHandler handler 结果回调。正常返回时 resultObject 对象类型为 NSArray<JMSGGroup>。

##### 创建一个群组

```
+ (void)createGroup:(JMSGGroup *)group
  completionHandler:(JMSGCompletionHandler)handler;
```
参数说明

+ JMSGGroup* group 待创建的群组。
+ JMSGCompletionHandler handler 结果回调。正常返回时 resultOjbect 内容也为 nil。

##### 更新群组信息

```
+ (void)updateGroupInfo:(JMSGGroup *)group
      completionHandler:(JMSGCompletionHandler)handler;
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


##### 删除群组成员

```
+ (void)deleteGroupMember:(NSString *)groupId
                  members:(NSString *)members
        completionHandler:(JMSGCompletionHandler)handler;
```



##### 获取群组成员列表

```
+ (void)getGroupMemberList:(NSString *)groupId
         completionHandler:(JMSGCompletionHandler)handler;
```



### Example 代码样例

#### 发文本消息

```
JMSGContentMessage *message = [[JMSGContentMessage alloc] init];
message.target_name = @"javen";
message.contentText = @"Hello";
[JMSGMessageManager sendMessage:message];
```



### Guideline 集成指南

#### 支持的 iOS 系统版本

iOS 7.0 以上。

#### 包含 JPush SDK

JMessage SDK 包含 JPush SDK 的全部功能。

如果您原来代码里集成过 JPush iOS SDK，则可大部分保持不变。变更部分如下：

+ 集成到项目工程里的 JPush SDK 的文件删除掉，包括头文件：APService.h，库文件  libPushSDK.a。JMessage.framework 里已经包含 Push 部分，不删除掉会冲突。
+ 配置文件 PushConfig.plist 文件删除掉。不再使用配置文件，而是用代码调用提供基本参数。
+ 原来调用 APService 里 setupWithOption 做初始化，现在要换成 JMessage 里相应的方法。

未集成使用过 JPush iOS SDK 的，请参考 JPush SDK 的文档来做相应的依赖与配置：[JPush iOS SDK 集成指南](http://docs.jpush.io/guideline/ios_guide/)。但上述变更依然有效。

#### 导入依赖

对于库与框架的依赖，除了 JPush SDK 所需要的，JMessage SDK 增加了如下几个的依赖：

+ AudioToolboxFramework
+ CoreAudioFramework
+ libsqlite3.0.dylib

#### 导入 JMessage SDK

JMessage SDK 也是以 framework 的方式提供的，所以类似于增加系统的框架依赖，需要增加 JMessage.framework。

#### 项目配置

在项目配置，Build Settings，Other Linker Flags 里增加如下 2 项：

    -ObjC
    -all_load

#### 初始化

JMessage 初始化只需要加上下述调用。

```
  [JMessage setupJMessage:launchOptions
                   appKey:JMSSAGE_APPKEY
                  channel:CHANNEL 
                  apsForProduction:NO
                 category:nil];

```


### See Also 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)

