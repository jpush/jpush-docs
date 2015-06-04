# IM SDK for iOS
iOS SDK download coming soon. 
### Summary 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)


### Functions 功能

与 Android 集类似。

### API 接口列表

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


#### 注册与登录

```
JMSGUser.h

+ (void)registerWithUsername:(NSString *)username
                    password:(NSString *)password
           completionHandler:(JMSGCompletionHandler)handler;

+ (void)loginWithUsername:(NSString *)username
                 password:(NSString *)password
        completionHandler:(JMSGCompletionHandler)handler;
        
+ (void)logoutWithCompletionHandler:(JMSGCompletionHandler)handler;

+ (void)getUserInfoWithUsername:(NSString *)username
              completionHandler:(JMSGCompletionHandler)handler;
              
+ (JMSGUser *)getMyInfo;

+ (void)getOriginAvatarImage:(JMSGUser *)userInfo
           completionHandler:(JMSGCompletionHandler)handler;

+ (void)updateMyInfoWithParameter:(id)parameter
                         withType:(JMSGUpdateUserInfoType)type
                completionHandler:(JMSGCompletionHandler)handler;           

+ (void)updatePasswordWithNewPassword:(NSString *)newPassword
                          oldPassword:(NSString *)oldPassword
                    completionHandler:(JMSGCompletionHandler)handler;

              
```
#### 聊天会话

```
JMSGConversation.h

/// 当前会话相关的消息操作

- (void)getMessage:(NSString *)messageId
 completionHandler:(JMSGCompletionHandler)handler;

- (void)getAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;

- (void)deleteAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;

- (void)resetUnreadMessageCountWithCompletionHandler:(JMSGCompletionHandler)handle;

/// 会话维护

+ (void)getConversation:(NSString *)targetId
               withType:(JMSGConversationType)conversationType
      completionHandler:(JMSGCompletionHandler)handler;

+ (void)createConversation:(NSString *)targetId
                  withType:(ConversationType)conversationType
         completionHandler:(JMSGCompletionHandler)handler;

+ (void)deleteConversation:(NSString *)targetId
                  withType:(JMSGConversationType)conversationType      
         completionHandler:(JMSGCompletionHandler)handler;

+ (void)getConversationListWithCompletionHandler:(JMSGCompletionHandler)handler;

```

#### 聊天消息

```
JMSGMessage.h

+ (void)sendMessage:(JMSGMessage *)message;

+ (void)downloadOriginImage:(JMSGImageMessage *)message
               withProgress:(NSProgress *)progress
          completionHandler:(JMSGCompletionHandler)handler;

+ (void)downloadThumbImage:(JMSGImageMessage *)message
              withProgress:(NSProgress *)progress
         completionHandler:(JMSGCompletionHandler)handler;

+ (void)downloadVoice:(JMSGVoiceMessage *)message
         withProgress:(NSProgress *)progress
    completionHandler:(JMSGCompletionHandler)handler;

```

### 群组维护

```
/// 我的所有群组列表
+ (void)getGroupListWithCompletionHandler:(JMSGCompletionHandler)handler;

+ (void)createGroup:(JMSGGroup *)group
  completionHandler:(JMSGCompletionHandler)handler;
  
+ (void)updateGroupInfo:(JMSGGroup *)group
      completionHandler:(JMSGCompletionHandler)handler;
      
+ (void)getGroupInfo:(NSString *)groupId
   completionHandler:(JMSGCompletionHandler)handler;

/// 我退出群组
+ (void)exitGoup:(NSString *)groupId
    completionHandler:(JMSGCompletionHandler)handler;

+ (void)addMembers:(NSString *)groupId
           members:(NSString *)members
 completionHandler:(JMSGCompletionHandler)handler;
 
+ (void)deleteGroupMember:(NSString *)groupId
                  members:(NSString *)members
        completionHandler:(JMSGCompletionHandler)handler;

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

#### 包含 JPush SDK

JMessage SDK 包含 JPush SDK 的全部功能，所以其依赖与配置也是包含关系。

请参考 JPush SDK 的文档来做相应的依赖与配置：[JPush iOS SDK 集成指南](http://docs.jpush.io/guideline/ios_guide/)

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


### See Also 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)

