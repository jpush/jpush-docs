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
JMSGUser.h

@interface JMSGUser : NSObject

 @property (atomic,strong, readonly) NSString *address;
 @property (atomic,strong, readonly) NSString *avatarResourcePath;
 @property (atomic,strong, readonly) NSString *avatarThumbPath;
 @property (atomic,strong, readonly) NSString *birthday;
 @property (atomic,strong, readonly) NSNumber *userGender;
 @property (atomic,strong, readonly) NSString *cTime;

 @property (atomic,assign, readonly) NSInteger star;
 @property (atomic,assign, readonly) NSInteger blackList;
 @property (atomic,strong, readonly) NSString *region;
 @property (atomic,strong, readonly) NSString *nickname;
 @property (atomic,strong, readonly) NSString *noteName;
 @property (atomic,strong, readonly) NSString *noteText;
 @property (atomic,strong, readonly) NSString *signature;
 @property (atomic,assign, readonly) SInt64    uid;
 @property (atomic,strong, readonly) NSString *username;
 @property (atomic,strong, readonly) NSString *password;

@end

```

#### 会话

```
JMSGConversation.h

@interface JMSGConversation : NSObject

 @property (atomic, strong) NSString *Id;//聊天会话ID
 @property (atomic, strong) NSString *type;//聊天会话类型
 @property (atomic, strong) NSString *target_id;//聊天会话目标id
 @property (atomic, strong) NSString *target_displayName;//聊天对象的昵称

 @property (atomic, strong) NSString *latest_type;//最后消息的内容类型
 @property (atomic, strong) NSString *latest_text;//最后消息内容
 @property (atomic, strong) NSString *latest_date;//最后消息日期
 @property (atomic, strong) NSString *latest_displayName;
 @property (atomic, assign) MessageStatusType latest_text_state;

 @property (atomic, strong) NSNumber *unread_cnt;//未读消息数量
 @property (atomic, assign) MessageStatusType latest_messageStatus;//最后消息状态
 @property (atomic, strong) NSString *latest_target_displayName;//最后消息展示名
 @property (atomic, strong) NSString *msg_table_name;//该会话所对应的Message表的表名

 @property(readonly, strong, nonatomic) NSString *targetName;
 @property(readonly, strong, nonatomic) NSString *avatarThumb;
 @property(readonly, assign, nonatomic) ConversationType chatType;


/**
 *  获取指定消息id的消息
 *
 *  @param messageId  消息ID
 *  @param handler    用户获取消息回调接口(resultObject为JMSGMessage类型)
 *
 */
- (void)getMessage:(NSString *)messageId
 completionHandler:(JMSGCompletionHandler)handler;

/**
 *  获取会话所有消息
 *
 *  @param handler    用户获取所有消息回调接口(resultObject为JMSGMessage类型的数组)
 *
 */
- (void)getAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;


/**
 *  删除会话所有消息
 *
 *  @param handler    删除所有消息回调接口
 *
 */
- (void)deleteAllMessageWithCompletionHandler:(JMSGCompletionHandler)handler;

/**
 *  将会话中的未读消息数清零
 *
 *  @param handler    清空未读消息回调接口
 *
 */
- (void)resetUnreadMessageCountWithCompletionHandler:(JMSGCompletionHandler)handle;

@end


```

#### 消息

```
JMSGMessage.h

@interface JMSGMessage : NSObject <NSCopying>

 @property (atomic, strong, readonly) NSString            *messageId;   //聊天ID
 @property (atomic, strong) NSString                    *target_name;
 @property (atomic, strong, getter=display_name) NSString *display_name;

 @property (atomic, strong)   NSDictionary                *extra;
 @property (atomic, strong)   NSDictionary                *custom;

 @property (assign, readonly) MessageContentType           messageType;
 @property (atomic, strong  ) JMSGConversation            *conversation;
 @property (atomic, strong  ) NSNumber                    *timestamp;  //消息时间戳
 @property (strong, readonly) NSNumber                    *status;     //消息的状态


 - (instancetype)init;

@end

@interface JMSGMediaMessage : JMSGMessage <NSCopying>

 @property (atomic, strong)JMSGonProgressUpdate   progressCallback;
 @property (atomic, strong)NSString              *resourcePath;
 @property (atomic, assign)CGSize                 imgSize;

@end

@interface JMSGContentMessage : JMSGMessage <NSCopying>

 @property(atomic, strong)NSString                *contentText;

@end

@interface JMSGImageMessage : JMSGMediaMessage <NSCopying>

 @property(atomic, strong)NSString                *thumbPath;

@end

@interface JMSGVoiceMessage : JMSGMediaMessage <NSCopying>

 @property(atomic, strong)NSString                *duration;

@end


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

