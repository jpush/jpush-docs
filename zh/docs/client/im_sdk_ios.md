# IM SDK for iOS

### Summary 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)


### Functions 功能

与 Android 集类似。

暂缺少群组相关功能。Comming soon.


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

+ launchOptions 


#### 注册与登录

```
JMSGUserManager.h

+ (void)registerWithUsername:(NSString *)username
                    password:(NSString *)password
           completionHandler:(JMSGCompletionHandler)handler;

+ (void)loginWithUsername:(NSString *)username
                 password:(NSString *)password
        completionHandler:(JMSGCompletionHandler)handler;

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
JMSGConversationManager.h

+ (void)getConversation:(NSString *)targetUserName
      completionHandler:(JMSGCompletionHandler)handler;

+ (void)createConversation:(NSString *)targetUserName
                  withType:(ConversationType)conversationType
         completionHandler:(JMSGCompletionHandler)handler;

+ (void)deleteConversation:(NSString *)targetUserName
         completionHandler:(JMSGCompletionHandler)handler;

+ (void)getConversationListWithCompletionHandler:(JMSGCompletionHandler)handler;

```

#### 聊天消息

```
JMSGMessageManager.h

+ (void)sendMessage:(JMSGMessage *)message;

+ (void)getMetaImageFromMessage:(JMSGImageMessage *)message
                   withProgress:(NSProgress *)progress
              completionHandler:(JMSGCompletionHandler)handler;

+ (void)getThumbImageFromMessage:(JMSGImageMessage *)message
                    withProgress:(NSProgress *)progress
               completionHandler:(JMSGCompletionHandler)handler;

+ (void)getVoiceFromMessage:(JMSGVoiceMessage *)message
               withProgress:(NSProgress *)progress
          completionHandler:(JMSGCompletionHandler)handler;

```


### Classes 类定义

#### 用户

```

```

#### 会话

```

```

#### 消息

```

```


### Guideline 集成指南



### See Also 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)
