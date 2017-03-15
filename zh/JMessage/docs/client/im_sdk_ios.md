<h1>iOS SDK 开发指南</h1>

## 概述

极光 IM（英文名JMessage）为开发者提供易用可靠的 IM 开发框架，开发者可集成SDK，快速实现即时通讯功能。JMessage iOS SDK 支持 iOS 7 以上系统。要了解极光 IM 的详细信息，请参考文档：[JMessage 产品简介](https://docs.jiguang.cn/jmessage/guideline/jmessage_guide/)


### 功能

极光IM 最核心的功能是 IM 即时消息的功能。

+ 单聊，群聊；
+ 消息类型：文本、语音、图片、文件、位置等；
+ 用户未在线时保存离线消息；
+ 保证消息及时下发；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

## API 接口

需要了解完整的 SDK API，有三种方式：

+ 直接查看 JMessage.framework 里的 Headers 文件。这些头文件定义了 SDK 提供的对外接口，带有完善的注释与说明，甚至样例代码。
+ 下载 docset 文档。我们使用 Appledoc 工具基于上述 Headers 文件生成了 docset。可以使用 Xcode 直接打开查看，或者使用 Dash 查看。我们建议使用 Dash 效果更好。
+ 使用 Appledoc 生成的文档的在线版本：<a href="http://docs-test.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/" target="_blank">iOS SDK APIs</a>

以下简要地列举 SDK API 提供的功能，同时提供部分简单的例子。

### SDK初始化

JMessage.h 里定义的 setupJMessage 方法，需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。


#### 初始化 JMessage SDK

```
/*!
 * @abstract 初始化 JMessage SDK(此方法在JMessage 3.1.0 版本已过期)
 * 此方法被[setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:]取代
 */
+ (void)setupJMessage:(NSDictionary *)launchOptions
               appKey:(NSString *)appKey
              channel:(NSString *)channel
     apsForProduction:(BOOL)isProduction
             category:(NSSet *)category;
```

#### 注册远程推送
```
/*!
 * @abstract 注册远程推送
 * @param types 通知类型
 * @param categories 类别组
 * @discussion 此方法必须被调用，如果有集成JPush或其他远程推送注册方法，请不要再调用此方法
 *
 */
+ (void)registerForRemoteNotificationTypes:(NSUInteger)types
                                categories:(NSSet *)categories;
                                                            
```

#### 注册DeviceToken
```
/*!
 * @abstract 注册DeviceToken
 * @param deviceToken 从注册推送回调中拿到的DeviceToken
 * @discussion 此方法必须被调用
 *
 */
+ (void)registerDeviceToken:(NSData *)deviceToken;
```

####设置角标(到服务器)
```
/*!
 * @abstract 设置角标(到服务器)
 *
 * @param value 新的值. 会覆盖服务器上保存的值(这个用户)
 *
 * @discussion 本接口不会改变应用本地的角标值.
 * 本地仍须调用 UIApplication:setApplicationIconBadgeNumber 函数来设置脚标.
 *
 * 该功能解决的问题是, 服务器端推送 APNs 时, 并不知道客户端原来已经存在的角标是多少, 指定一个固定的数字不太合理.
 *
 * APNS 服务器端脚标功能提供:
 *
 * - 通过本 API 把当前客户端(当前这个用户的) 的实际 badge 设置到服务器端保存起来;
 * - 调用服务器端 API 发 APNs 时(通常这个调用是批量针对大量用户),
 *   使用 "+1" 的语义, 来表达需要基于目标用户实际的 badge 值(保存的) +1 来下发通知时带上新的 badge 值;
 */
+ (BOOL)setBadge:(NSInteger)value;
```

####重置角标(到服务器)
```
/*!
 * @abstract 重置角标(为0)
 *
 * @discussion 相当于 [setBadge:0] 的效果.
 * 参考 [JMessage setBadge:] 说明来理解其作用.
 */
+ (void)resetBadge;
```

###SDK初始化(设置漫游)

***Since v3.1.0***  
SDK 初始化时，可设置是否启用消息记录漫游。  
打开消息漫游之后，用户多个设备之间登陆时，SDK会自动将历史消息同步到本地，同步完成之后SDK会以 Conversation 为单位触发代理方法`onSyncRoamingMessageConversation:`通知上层刷新,具体方法见[消息同步监听代理](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncConversation:offlineMessages:roamingMessages:)

```
/*!
 * @abstract 初始化 JMessage SDK
 *
 * @param launchOptions    AppDelegate启动函数的参数launchingOption(用于推送服务)
 * @param appKey           appKey(应用Key值,通过JPush官网可以获取)
 * @param channel          应用的渠道名称
 * @param isProduction     是否为生产模式
 * @param category         iOS8新增通知快捷按钮参数
 * @param isRoaming        是否启用消息漫游,默认关闭
 *
 * @discussion 此方法必须被调用, 以初始化 JMessage SDK
 *
 * 如果未调用此方法, 本 SDK 的所有功能将不可用.
 */
+ (void)setupJMessage:(NSDictionary *)launchOptions
               appKey:(NSString *)appKey
              channel:(NSString *)channel
     apsForProduction:(BOOL)isProduction
             category:(NSSet *)category
       messageRoaming:(BOOL)isRoaming;

```
	 
##### 例子	  
	[JMessage setupJMessage:launchOptions
	                 appKey:@"用户的AppKey"
	                channel:@"应用的渠道名称"
	       apsForProduction:NO
	               category:nil 
	         messageRoaming:NO];  

这个调用是必须的。否则 SDK 将不能正常工作。

### 注册与登录
#### 用户注册
	/*!
	 * @abstract 新用户注册
	 *
	 * @param username 用户名. 长度 4~128 位.
	 *                 支持的字符: 字母,数字,下划线,英文减号,英文点,@邮件符号. 首字母只允许是字母或者数字.
	 * @param password 用户密码. 长度 4~128 位.
	 * @param handler 结果回调. 返回正常时 resultObject 为 nil.
	 */
	+ (void)registerWithUsername:(NSString *)username
	                    password:(NSString *)password
	           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	[JMSGUser registerWithUsername:@"用户名"
	                      password:@"密码"
	                     completionHandler:^(id resultObject, NSError *error) {
	                         if (!error) {
	                             //注册成功
	                         } else {
	                            //注册失败
	                         }
	                     }];
#### 用户登录
	/*!
	 * @abstract 用户登录
	 *
	 * @param username 登录用户名. 规则与注册接口相同.
	 * @param password 登录密码. 规则与注册接口相同.
	 * @param handler 结果回调
	 *
	 * - resultObject 简单封装的user对象
	 * - error 错误信息
	 *
	 * 注意：上层不要直接使用 resultObject 对象做操作, 因为 resultOjbect 只是一个简单封装的user对象.
	 */

	+ (void)loginWithUsername:(NSString *)username
	                 password:(NSString *)password
	        completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	[JMSGUser loginWithUsername:@"用户名"
	                           password:@"密码"
	                  completionHandler:^(id resultObject, NSError *error) {
	                      if (!error) {
	                         //登录成功
	                      } else {
	                         //登录失败
	                      }
	                  }];
	                  
#### 退出登录
	/*!
	 * @abstract 当前用户退出登录
	 *
	 * @param handler 结果回调。正常返回时 resultObject 也是 nil。
	 *
	 * @discussion 这个接口一般总是返回成功，即使背后与服务器端通讯失败，SDK 也总是会退出登录的。
	 * 建议 App 也不必确认 SDK 返回, 就实际退出登录状态.
	 */
	+ (void)logout:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	//退出当前登录的用户
	        [JMSGUser logout:^(id resultObject, NSError *error) {
	            if (!error) {
	             	//退出登录成功
	            } else {
	                //退出登录失败
	            }
	        }];
	        
### 用户管理
#### 批量获取用户信息
	/*!
	 * @abstract 批量获取用户信息
	 *
	 * @param usernameArray 用户名列表。NSArray 里的数据类型为 NSString
	 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里的数据类型为 JMSGUser
	 *
	 * @discussion 这是一个批量接口。
	 */
	+ (void)userInfoArrayWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
	                     completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	[JMSGUser userInfoArrayWithUsernameArray:@[@"username1", @"username2"] completionHandler:^(id resultObject, NSError *error) {
	        if (!error) {
	            //成功获取用户信息，resultObject为JMSGUser类型的数组
	        } else {
	            //获取用户信息失败   
	        }
	    }];
	  
#### 获取用户个人信息
	/*!
	 * @abstract 获取用户本身个人信息
	 *
	 * @return 当前登陆账号个人信息
	 */
	+ (JMSGUser *)myInfo;
##### 例子
	JMSGUser *user = [JMSGUser myInfo];

#### 更新用户信息
	/*!
	 * @abstract 更新用户信息接口
	 *
	 * @param parameter     新的属性值
	 *        Birthday&&Gender 是NSNumber类型, Avatar NSData类型 其他 NSString
	 * @param type          更新属性类型
	 * @param handler       更新用户信息回调接口函数
	 */
	+ (void)updateMyInfoWithParameter:(id)parameter
	                    userFieldType:(JMSGUserField)type
	                completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	/*
            userFieldType:
            kJMSGUserFieldsNickname: 用户名
            kJMSGUserFieldsBirthday: 生日
            kJMSGUserFieldsSignature: 签名
            kJMSGUserFieldsGender: 性别
            kJMSGUserFieldsRegion: 区域
            kJMSGUserFieldsAvatar: 头像
      */
	[JMSGUser updateMyInfoWithParameter:parameter userFieldType:kJMSGUserFieldsGender completionHandler:^(id resultObject, NSError *error) {
	            if (!error) {
	                //updateMyInfoWithPareter success
	            } else {
	                //updateMyInfoWithPareter fail
	            }
	        }];

#### 更新密码
	/*!
	 * @abstract 更新密码接口
	 *
	 * @param newPassword   用户新的密码
	 * @param oldPassword   用户旧的密码
	 * @param handler       更新密码回调接口函数
	 */
	+ (void)updateMyPasswordWithNewPassword:(NSString *)newPassword
	                            oldPassword:(NSString *)oldPassword
	                      completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	[JMSGUser updateMyPasswordWithNewPassword:self.passwordField.text
	                                      oldPassword:self.oldpassword.text
	                                completionHandler:^(id resultObject, NSError *error) {
	                                    if (!error) {
	                                        //更新密码成功
	                                    } else {
	                                        //更新密码失败
	                                    }
	                                }];

#### 获取头像缩略图
	/*!
	 * @abstract 获取头像缩略图文件数据
	 *
	 * @param handler 结果回调。回调参数:
	 *
	 * - data 头像数据;
	 * - objectId 用户username;
	 * - error 不为nil表示出错;
	 *
	 * 如果 error 为 ni, data 也为 nil, 表示没有头像数据.
	 *
	 * @discussion 需要展示缩略图时使用。
	 * 如果本地已经有文件，则会返回本地，否则会从服务器上下载。
	 */
	- (void)thumbAvatarData:(JMSGAsyncDataHandler)handler;
##### 例子
	JMSGUser *user = [JMSGUser myInfo];
    [user thumbAvatarData:^(NSData *data, NSString *objectId, NSError *error) {
        if (!error) {
            //下载成功
        } else {
			//下载失败
        }
    }];

#### 获取头像大图
	/*!
	 * @abstract 获取头像大图文件数据
	 *
	 * @param handler 结果回调。回调参数:
	 *
	 * - data 头像数据;
	 * - objectId 用户username;
	 * - error 不为nil表示出错;
	 *
	 * 如果 error 为 ni, data 也为 nil, 表示没有头像数据.
	 *
	 * @discussion 需要展示大图图时使用
	 * 如果本地已经有文件，则会返回本地，否则会从服务器上下载。
	 */
	- (void)largeAvatarData:(JMSGAsyncDataHandler)handler;
##### 例子
	JMSGUser *user = [JMSGUser myInfo];
	[user largeAvatarData:^(NSData *data, NSString *objectId, NSError *error) {
	                            if (!error) {
	           						 //下载成功
	       						 } else {
									//下载失败
	        					 }
	                        }];

#### 获取用户展示名
	/*!
	 * @abstract 用户展示名
	 *
	 * @discussion 如果 nickname 存在则返回 nickname，否则返回 username
	 */
	- (NSString *)displayName;
##### 例子
	JMSGUser *user = [JMSGUser myInfo];
	NSString myName = [user displayName];

#### 修改好友的备注名、备注信息	
	/*!
	 * @abstract 修改好友备注名
	 *
	 * @param noteName 备注名
	 *
	 * @discussion 注意：这是建立在是好友关系的前提下，修改好友的备注名
	 */
	- (void)updateNoteName:(NSString *)noteName completionHandler:(JMSGCompletionHandler)handler;
	
	/*!
	 * @abstract 修改好友备注信息
	 *
	 * @param noteText 备注信息
	 *
	 * @discussion 注意：这是建立在是好友关系的前提下，修改好友的备注信息
	 */
	- (void)updateNoteText:(NSString *)noteText completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	// 修改备注名
	[friendUser updateNoteName:@"备注名" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        [MBProgressHUD showMessage:@"修改备注成功" view:self.view];
	    }else{
	        [MBProgressHUD showMessage:@"修改备注失败" view:self.view];
	    }
	 }]; 

### 从3.1.0版本开始接收消息的变化
JMessage SDK 3.1.0 版本开始，SDK 将消息下发分为在线下发和离线下发两种类型，离线下发包含了离线消息和漫游消息。 先明确这几个概念：

+ 在线消息：IM 用户在线期间，所有收到的消息称为在线消息。
+ 离线消息：IM 用户离线期间（包括登出或者网络断开）收到的消息，会暂存在极光服务器上，当用户再次上线，SDK 会将这部分消息拉取下来，这部分消息就称为离线消息。
+ 漫游消息：IM 用户在多个设备之间登陆时，SDK 会将其他设备已接收的消息视为漫游。

有了这几个概念的区分之后，SDK 对于这两种消息的处理方式也有了不同：

SDK版本 | 在线消息  | 离线消息 | 漫游消息
------- | ------- | ------- |---------
Version < 3.1.0 | 逐条下发，每次都触发[onReceiveMessage:]()|逐条下发，每次都触发[onReceiveMessage:]()|无
Version >= 3.1.0 | 逐条下发，每次都触发[onReceiveMessage:]()|以会话为单位，触发一次下发[onSyncOfflineMessageConversation:]()|以会话为单位，触发一次下发[onSyncRoamingMessageConversation:]()  


**总结**  
对于消息同步，以会话为单位，不管会话有多少离线消息，SDK只触发一次消息同步的代理方法，这个代理方法返回值中包含了具体某个会话、离线消息这些相关数据信息，上层通过这个方法可监听到每个会话完成消息同步的情况，从而去刷新UI，这样会大大减轻上层处理事件的压力。


SDK 升级到 3.1.0 版本后（或之后的版本），上层只需要做以下变动：

+ 设置消息漫游，调用 [新的 SDK 初始化](./jmessage_ios_appledoc_html/Classes/JMessage.html#//api/name/setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:) 设置消息漫游（<font color= BurlyWood>不需要消息漫游的开发者可忽略此操作</font>）。
+ 漫游消息的代理方法 [onSyncRoamingMessageConversation:]() 通过此方法可以监听到漫游消息同步情况，从而刷新UI（<font color= BurlyWood>不需要漫游消息的开发者可忽略此操作</font>）。
+ 离线消息的代理方法 [onSyncOfflineMessageConversation:](./jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncConversation:offlineMessages:roamingMessages:) 通过此方法可以监听到离线消息同步情况，从而刷新UI。


### 消息管理
#### 创建单聊消息
	/*!
	 * @abstract 创建单聊消息
	 *
	 * @param content 消息内容对象
	 * @param username 单聊用户 username
	 *
	 * @discussion 不关心会话时的直接创建聊天消息的接口。一般建议使用 JMSGConversation -> createMessageWithContent:
	 */
	+ (JMSGMessage *)createSingleMessageWithContent:(JMSGAbstractContent *)content
	                                       username:(NSString *)username;
##### 例子
	JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:@"textContent"];
	JMSGMessage *message = [JMSGMessage createSingleMessageWithContent:textContent username:@"username"];

#### 创建群聊消息
	/*!
	 * @abstract 创建群聊消息
	 *
	 * @param content 消息内容对象
	 * @param groupId 群聊ID
	 *
	 * @discussion 不关心会话时的直接创建聊天消息的接口。一般建议使用 JMSGConversation -> createMessageWithContent:
	 */
	+ (JMSGMessage *)createGroupMessageWithContent:(JMSGAbstractContent *)content
	                                       groupId:(NSString *)groupId;
##### 例子
	JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:@"textContent"];
	JMSGMessage *message = [JMSGMessage createGroupMessageWithContent:textContent groupId:@"groupId"];

#### 发送消息
	/*!
	 * @abstract 发送消息（已经创建好的）
	 *
	 * @param message 消息对象。
	 *
	 * @discussion 此接口与 createMessage:: 相关接口配合使用，创建好后使用此接口发送。
	 */
	+ (void)sendMessage:(JMSGMessage *)message;

#### 发送单聊文本消息
	/*!
	 * @abstract 发送单聊文本消息
	 *
	 * @param text 文本内容
	 * @param username 单聊对象 username
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleTextMessage:(NSString *)text
	                       toUser:(NSString *)username;

#### 发送单聊图片消息
	/*!
	 * @abstract 发送单聊图片消息
	 *
	 * @param imageData 图片数据
	 * @param username 单聊对象 username
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleImageMessage:(NSData *)imageData
	                        toUser:(NSString *)username;

#### 发送单聊语音消息
	/*!
	 * @abstract 发送单聊语音消息
	 *
	 * @param voiceData 语音数据
	 * @param duration 语音时长
	 * @param username 单聊对象 username
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleVoiceMessage:(NSData *)voiceData
	                 voiceDuration:(NSNumber *)duration
	                        toUser:(NSString *)username;
	                       
#### 发送单聊文件消息
	/*!
	 * @abstract 发送单聊文件消息
	 *
	 * @param fileData 文件数据数据
	 * @param fileName 文件名
	 * @param username 单聊对象 username
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleFileMessage:(NSData *)fileData
	                     fileName:(NSString *)fileName
	                       toUser:(NSString *)username;

#### 发送单聊位置消息
	/*!
	 * @abstract 发送单聊地理位置消息
	 * @param latitude 纬度
	 * @param longitude 经度
	 * @param scale 缩放比例
	 * @param address 详细地址
	 * @param username 单聊对象
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleLocationMessage:(NSNumber *)latitude
	                        longitude:(NSNumber *)longitude
	                            scale:(NSNumber *)scale
	                          address:(NSString *)address
	                           toUser:(NSString *)username;

#### 发送群聊文本消息
	/*!
	 * @abstract 发送群聊文本消息
	 *
	 * @param text 文本内容
	 * @param groupId 群聊目标群组ID
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendGroupTextMessage:(NSString *)text
	                     toGroup:(NSString *)groupId;

#### 发送群聊图片消息
	/*!
	 * @abstract 发送群聊图片消息
	 *
	 * @param imageData 图片数据
	 * @param groupId 群聊目标群组ID
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendGroupImageMessage:(NSData *)imageData
	                      toGroup:(NSString *)groupId;

#### 发送群聊语音消息
	/*!
	 * @abstract 发送群聊语音消息
	 *
	 * @param voiceData 语音数据
	 * @param duration 语音时长
	 * @param groupId 群聊目标群组ID
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendGroupVoiceMessage:(NSData *)voiceData
	                voiceDuration:(NSNumber *)duration
	                      toGroup:(NSString *)groupId;
	                      
#### 发送群聊文件消息
	/*!
	 * @abstract 发送群聊文件消息
	 *
	 * @param fileData 文件数据
	 * @param fileName 文件名
	 * @param groupId 群聊目标群组ID
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendGroupFileMessage:(NSData *)fileData
	                    fileName:(NSString *)fileName
	                     toGroup:(NSString *)groupId;

#### 发送群聊位置消息
	/*!
	 * @abstract 发送群聊地理位置消息
	 * @param latitude 纬度
	 * @param longitude 经度
	 * @param scale 缩放比例
	 * @param address 详细地址
	 * @param groupId 群聊目标群组ID
	 */
	+ (void)sendGroupLocationMessage:(NSNumber *)latitude
	                       longitude:(NSNumber *)longitude
	                           scale:(NSNumber *)scale
	                         address:(NSString *)address
	                         toGroup:(NSString *)groupId;
	                         
#### 设置消息的FromName
	/*!
	 * @abstract 设置消息的 fromName(即:通知栏的展示名称)
	 *
	 * @param fromName 本条消息在接收方通知栏的展示名称
	 *
	 * @discussion fromName填充在发出的消息体里，对方收到该消息通知时,在通知栏显示的消息发送人名称就是该字段的值.
	 *
	 */
	- (void)setFromName:(NSString * JMSG_NULLABLE)fromName;
	
#### 更新 message 中的extra
	/*!
	 * @abstract 更新 message 中的 extra
	 *
	 * @param value   待更新的value,不能为null,类型只能为 NSNumber 和 NSString
	 * @param key     待更新value对应的key,不能为null
	 *
	 */
	- (BOOL)updateMessageExtraValue:(id)value forKey:(NSString *)key;

### 会话管理
会话相关的操作：
#### 获取单聊会话
	/*!
	 * @abstract 获取单聊会话
	 *
	 * @param username 单聊对象 username
	 *
	 * @discussion 如果会话还不存在，则返回 nil
	 */
	+ (JMSGConversation * JMSG_NULLABLE)singleConversationWithUsername:(NSString *)username;
	

#### 获取群聊会话
	/*!
	 * @abstract 获取群聊会话
	 *
	 * @param groupId 群聊群组ID。此 ID 由创建群组时返回的。
	 *
	 * @discussion 如果会话还不存在，则返回 nil
	 */
	+ (JMSGConversation * JMSG_NULLABLE)groupConversationWithGroupId:(NSString *)groupId;

#### 创建单聊会话
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
##### 例子
	[JMSGConversation createSingleConversationWithUsername:@"username" completionHandler:^(id resultObject, NSError *error) {
		                if (!error) {
		                   //创建单聊会话成功， resultObject为创建的会话
		                } else {
		                    //创建单聊会话失败
		                }
		            }];
		            
#### 创建群聊会话
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
##### 例子
	[JMSGConversation createGroupConversationWithGroupId:@"groupId" completionHandler:^(id resultObject, NSError *error) {
			                if (!error) {
			                   //创建群聊用会话成功， resultObject为创建的会话
			                } else {
			                    //创建群聊会话失败
			                }
			            }];

#### 删除单聊会话
	/*!
	 * @abstract 删除单聊会话
	 *
	 * @param username 单聊用户名
	 *
	 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
	 */
	+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username;
	

#### 删除群聊会话
	/*!
	 * @abstract 删除群聊会话
	 *
	 * @param groupId 群聊群组ID
	 *
	 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
	 */
	+ (BOOL)deleteGroupConversationWithGroupId:(NSString *)groupId;

#### conversation列表
	/*!
	 * @abstract 返回 conversation 列表（异步,已经排序）
	 *
	 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里成员的类型为 JMSGConversation
	 *
	 * @discussion 当前是返回所有的 conversation 列表，默认是已经排序。
	 * 
	 */
	 + (void)allConversations:(JMSGCompletionHandler)handler;
##### 例子
	[JMSGConversation allConversations:^(id resultObject, NSError *error) {
            if (!error) {
               //获取成功，resultObject为会话对的数组
            } else {
				//获取失败
            }
	    }];
	    
消息相关操作：
#### 获取某条消息
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

#### 分页获取消息
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
	- (NSArray JMSG_GENERIC(__kindof JMSGMessage *) *)messageArrayFromNewestWithOffset:(NSNumber *JMSG_NULLABLE)offset
	                                                                             limit:(NSNumber *JMSG_NULLABLE)limit;
#### 获取所有消息记录
	/*!
	 * @abstract 异步获取所有消息记录
	 *
	 * @param handler 结果回调。正常返回时 resultObject 类型为 NSArray，数据成员类型为 JMSGMessage。
	 *
	 * @discussion 排序规则：最新
	 */
	- (void)allMessages:(JMSGCompletionHandler)handler;
##### 例子
	//_conversation 为Conversation的实例对象 
	[conversation allMessages:^(id resultObject, NSError *error) {
	        NSArray *array = (NSArray *)resultObject;
	        LogInfo(@"消息数：%ld", (long)array.count);
	    }];

#### 删除消息
	/*!
	 * @abstract 删除一条消息
	 *
	 * @param msgId 本地消息ID
	 */
	- (BOOL)deleteMessageWithMessageId:(NSString *)msgId;

#### 删除全部消息
	/*!
	 * @abstract 删除全部消息
	 *
	 * @discussion 清空当前会话的所有消息。
	 */
	- (BOOL)deleteAllMessages;

#### 创建消息对象
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

#### 创建图片消息对象
	/*!
	 * @abstract 创建消息对象（图片，异步）
	 *
	 * @param content 准备好的图片内容
	 * @param handler 结果回调. 正常返回时 resultObject 类型为 JMSGMessage.
	 *
	 * @discussion 对于图片消息，因为 SDK 要做缩图有一定的性能损耗，图片文件很大时存储落地也会较慢。
	 * 所以创建图片消息，建议使用这个异步接口。
	 */
	- (void)createMessageAsyncWithImageContent:(JMSGImageContent *)content
	                         completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	//_conversation 为Conversation的实例对象 
	[_conversation createMessageAsyncWithImageContent:imageContent completionHandler:^(id resultObject, NSError *error) {
	            if (!error) {
	            	//创建成功
	            	//resultObject 为Message内容
	            }
	        }];

#### 发送消息
	/*!
	 * @abstract 发送消息（已经创建好对象的）
	 *
	 * @param message 通过消息创建类接口，创建好的消息对象
	 *
	 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 xxx 方法来注册消息发送结果。
	 */
	- (void)sendMessage:(JMSGMessage *)message;

#### 发送文本消息
	/*!
	 * @abstract 发送文本消息
	 * @param text 文本消息内容
	 * @discussion 快捷发消息接口。如果发送文本消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendTextMessage:(NSString *)text;

#### 发送图片消息
	/*!
	 * @abstract 发送图片消息
	 * @param imageData 图片消息数据
	 * @discussion 快捷发送消息接口。如果发送图片消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendImageMessage:(NSData *)imageData;

#### 发送语音消息
	/*!
	 * @abstract 发送语音消息
	 * @param voiceData 语音消息数据
	 * @param duration 语音消息时长（秒）. 长度必须大于 0.
	 * @discussion 快捷发送消息接口。如果发送语音消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendVoiceMessage:(NSData *)voiceData
	                duration:(NSNumber *)duration;
	                
#### 发送文件消息
	/*!
	 * @abstract 发送文件消息
	 * @param voiceData 文件消息数据
	 * @param fileName 文件名
	 * @discussion 快捷发送消息接口。如果发送文件消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendFileMessage:(NSData *)fileData
	               fileName:(NSString *)fileName;

#### 发送位置消息
	/*!
	 * @abstract 发送地理位置消息
	 * @param latitude 纬度
	 * @param longitude 经度
	 * @param scale 缩放比例
	 * @param address 详细地址
	 * @discussion 快捷发送消息接口。如果发送文件消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendLocationMessage:(NSNumber *)latitude
	                  longitude:(NSNumber *)longitude
	                      scale:(NSNumber *)scale
	                    address:(NSString *)address;

#### 获取会话头像
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
	 * @discussion 会话的头像来自于聊天对象, 单聊就是用户的头像, 群聊是群组头像.
	 * 建议在会话列表时, 使用此接口来显示会话的头像, 而不要使用 target 属性里的用户头像.
	 */
	- (void)avatarData:(JMSGAsyncDataHandler)handler;
##### 例子
	//_conversation 为Conversation的实例对象 
	[_conversation avatarData:^(NSData *data, NSString *objectId, NSError *error) {
	        if (!error) {
	        	//获取成功
	        } else {
	        	//获取失败   
	        }];

#### 获取所有会话的未读消息的总数	

	/*!
	 * @abstract 获取当前所有会话的未读消息的总数
	 *
	 * @discussion 获取所有会话未读消息总数
	 */
	+ (NSNumber *)getAllUnreadCount;
	
#### 清除会话未读数
	/*!
	 * @abstract 清除会话未读数
	 *
	 * @discussion 把未读数设置为 0
	 */
	- (void)clearUnreadCount;

#### 所有会话的未读消息的总数

	/*!
	 * @abstract 获取当前所有会话的未读消息的总数
	 *
	 * @discussion 获取所有会话未读消息总数
	 */
	+ (NSNumber *)getAllUnreadCount;

#### 获取最后一条消息的内容文本
	/*!
	 * @abstract 获取最后一条消息的内容文本
	 *
	 * @discussion 通常用来展示在会话列表的第 2 行. 如果是图片消息,通常是文本 [图片] 之类. CustomContent 可以定制这个文本.
	 */
	- (NSString *)latestMessageContentText;
##### 例子
	//_conversation 为Conversation的实例对象 
	NSString *latestMessageText = [_conversation latestMessageContentText];

#### 判断消息是否属于这个Conversation
	/*!
	 * @abstract 判断消息是否属于这个 Conversation
	 *
	 * @param message 待判断的消息对象
	 *
	 * @discussion 当前在聊天界面时，接收到消息通知，需要通过这个接口判断该消息是否属于当前这个会话，从而做不同的动作
	 *
	 * 如果注册消息接收事件时，只注册接收当前会话的消息，则不需要用此接口判断.
	 */
	- (BOOL)isMessageForThisConversation:(JMSGMessage *)message;

#### 从服务器端刷新会话信息
	/*!
	 * @abstract 从服务器端刷新会话信息
	 *
	 * @param handler 结果回调。返回正常时 resultObject 为当前 conversation 对象.
	 *
	 * @discussion 会话信息的 title/avatar 信息, 单聊来自于 UserInfo，对于群聊来自于 GroupInfo。
	 * 建议在进入聊天界面时，调用此接口，来更新会话属性。
	 * 典型的情况是, 此接口返回时, 刷新单聊界面顶部的会话标题. (有可能聊天对方昵称改变了, 或者群组名称改变了, 聊天标题需要刷新)
	 *
	 * 此接口供暂时使用。JMessage 整体的 Sync 机制生效后，将不需要客户端主动去刷新信息。
	 */
	- (void)refreshTargetInfoFromServer:(JMSGCompletionHandler)handler;
##### 例子
	//_conversation 为Conversation的实例对象 
	[_conversation refreshTargetInfoFromServer:^(id resultObject, NSError *error) {
	    if (!error) {
	      //success
	    } else {
	      //刷新失败
	    }
	  }];
	  
	  /*!


### 群组管理
#### 创建群组
	/*!
	 * @abstract 创建群组
	 *
	 * @param groupName 群组名称
	 * @param groupDesc 群组描述信息
	 * @param usernameArray 初始成员列表。NSArray 里的类型是 NSString
	 * @param handler 结果回调。正常返回 resultObject 的类型是 JMSGGroup。
	 *
	 * @discussion 向服务器端提交创建群组请求，返回生成后的群组对象.
	 * 返回群组对象, 群组ID是App 需要关注的, 是后续各种群组维护的基础.
	 */
	+ (void)createGroupWithName:(NSString * JMSG_NULLABLE )groupName
	                       desc:(NSString *JMSG_NULLABLE)groupDesc
	                memberArray:(NSArray JMSG_GENERIC(__kindof NSString *) *JMSG_NULLABLE)usernameArray
	          completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	//	创建群组
	[JMSGGroup createGroupWithName:@"群名" desc:@"群描述" memberArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            NSLog(@"创建群组成功!");
            JMSGGroup *group = (JMSGGroup *)resultObject;
        }
    }];

#### 更新群组信息	
	/*!
	 * @abstract 更新群组信息
	 *
	 * @param groupId 待更新的群组ID
	 * @param groupName 新名称
	 * @param groupDesc 新描述
	 * @param handler 结果回调. 正常返回时, resultObject 为 nil.
	 */
	+ (void)updateGroupInfoWithGroupId:(NSString *)groupId
	                              name:(NSString *)groupName
	                              desc:(NSString *)groupDesc
	                 completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	// 更新群组信息
	[JMSGGroup updateGroupInfoWithGroupId:@"group.gid" name:@"新群名" desc:@"新群描述" completionHandler:^(id resultObject, NSError *error) {
                if (!error) {
                    NSLog(@"更新群组信息成功!");
                }
    }];
    
#### 获取群组信息		
	/*!
	 * @abstract 获取群组信息
	 *
	 * @param groupId 待获取详情的群组ID
	 * @param handler 结果回调. 正常返回时 resultObject 类型是 JMSGGroup.
	 *
	 * @discussion 该接口总是向服务器端发起请求, 即使本地已经存在.
	 * 如果考虑性能损耗, 在群聊时获取群组信息, 可以获取 JMSGConversation -> target 属性.
	 */
	+ (void)groupInfoWithGroupId:(NSString *)groupId
	           completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	// 获取群组信息
	[JMSGGroup groupInfoWithGroupId:@"群组ID" completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            JMSGGroup *group = (JMSGGroup *)resultObject;
            NSLog(@"获取群组信息成功");
        }
    }];
#### 获取我的群组列表	
	/*!
	 * @abstract 获取我的群组列表
	 *
	 * @param handler 结果回调。正常返回时 resultObject 的类型是 NSArray，数组里的成员类型是JMSGGroup的gid
	 *
	 * @discussion 该接口总是向服务器端发起请求。
	 */
	+ (void)myGroupArray:(JMSGCompletionHandler)handler;          
##### 例子
	// 获取我的群组列表（实际返回的群组的gid列表）
	[JMSGGroup myGroupArray:^(id resultObject, NSError *error) {
        if (!error) {
            NSArray *groupGidArray = (NSArray *)resultObject;
            NSLog(@"获取我的群组成功!");
            NSLog(@"返回值是gid数组，开发者需要获取每个群完整信息的话，需要通过返回的gid再调用获取群信息接口");
        }
    }];
#### 获取群组成员列表	
	/*!
	 * @abstract 获取群组成员列表
	 *
	 * @return 成员列表. NSArray 里成员类型是 JMSGUser.
	 *
	 * @discussion 一般在群组详情界面调用此接口，展示群组的所有成员列表。
	 * 本接口只是在本地请求成员列表，不会发起服务器端请求。
	 */
	- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)memberArray;

#### 添加群组成员	
	/*!
	 * @abstract 添加群组成员
	 *
	 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
	
##### 例子
	// 添加群组成员
	[group addMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            NSLog(@"添加群成员成功！");
        }
    }];
#### 删除群组成员
	/*!
	 * @abstract 删除群组成员
	 *
	 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	// 删除群组成员
	[group removeMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            NSLog(@"删除群成员成功!");
        }
    }];
#### 退出当前群组	
	/*!
	 * @abstract 退出当前群组(当前用户)
	 *
	 * @param handler 结果回调。正常返回时 resultObject 为 nil。
	 */
	- (void)exit:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	// 退出当前群组(当前用户)
	[deletedGroup exit:^(id resultObject, NSError *error) {
        if (error == nil) {
            NSLog(@"退出群组成功!");
        }
    }];
#### 获取群组的展示名	
	/*!
	 * @abstract 获取群组的展示名
	 *
	 * @discussion 如果 group.name 为空, 则此接口会拼接群组前 5 个成员的展示名返回.
	 */
	- (NSString *)displayName;

### 群组@功能
消息发送方可以发一条带有@list的消息。  
接收方收到带有@list的消息之后，如果@list中包含了自己，则在sdk默认弹出的通知栏提示中会有相应的提示，如"xxx在群中@了你"。  
#### JMSGMessage
#### 创建@群成员的消息
	/*!
	 * @abstract 创建@人的群聊消息
	 *
	 * @param content 消息内容对象
	 * @param groupId 群聊ID
	 * @param at_list @对象的数组
	 *
	 * @discussion 不关心会话时的直接创建聊天消息的接口。一般建议使用 JMSGConversation -> createMessageWithContent:
	 */
	+ (JMSGMessage *)createGroupMessageWithContent:(JMSGAbstractContent *)content
	                                       groupId:(NSString *)groupId
	                                       at_list:(NSArray<__kindof JMSGUser *> *)at_list;

#### 判断消息是否@了自己
	/*!
	 * @abstract 是否是@自己的消息（只针对群消息，单聊消息无@功能）
	 */
	- (BOOL)isAtMe;
#### 获取消息中@的群成员列表
	/*!
	 * @abstract 获取消息体中所有@对象（只针对群消息，单聊消息无@功能）
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion 从服务器获取，返回消息的所有@对象。
	 */
	- (void)getAt_List:(JMSGCompletionHandler)handler;
#### JMSGConversation
#### 发送@人的消息
	/*!
	 * @abstract 发送@人消息（已经创建好对象的）
	 *
	 * @param message 通过消息创建类接口，创建好的消息对象
	 * @param at_list @对象的数组
	 *
	 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 JMSGMessageDelegate中的onReceiveMessage: error:方法来注册消息发送结果。
	 */
	- (void)sendMessage:(JMSGMessage *)message at_list:(NSArray<__kindof JMSGUser *> *)userList;
##### 例子
```
// 创建@群成员的消息
JMSGTextContent *textContent1 = [[JMSGTextContent alloc] initWithText:@"at他人的消息"];
JMSGMessage *atMessage = [JMSGMessage createGroupMessageWithContent:textContent1 groupId:@"gid" at_list:[NSArray arrayWithObjects:user1,user2, nil]];

// 消息中@的群成员列表
[atMessage getAt_List:^(id resultObject, NSError *error) {
     NSArray *atList = (NSArray *)resultObject;
 }];

// 发送@人的消息
JMSGTextContent *textContent2 = [[JMSGTextContent alloc] initWithText:@"创建好的消息"];
JMSGMessage *message = [JMSGMessage createGroupMessageWithContent:textContent2 groupId:@"gid"];
[conversation sendMessage: message atMessage at_list:[NSArray arrayWithObjects:user1,user2, nil]]    
```

### 群消息屏蔽
群组被设置为屏蔽之后，将收不到该群的消息，但是群成员变化事件还是能正常收到。
#### JMSGGroup
#### 判断群组是否被屏蔽
	/*!
	 * @abstract 该群是否已被设置为消息屏蔽
	 *
	 * @discussion YES:是 , NO: 否
	 */
	@property(nonatomic, assign, readonly) BOOL isShieldMessage
#### 设置群消息屏蔽
	/*!
	 * @abstract 设置群组消息屏蔽
	 *
	 * @param isShield 是否群消息屏蔽 YES:是 NO: 否
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 相应对象
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion 针对单个群组设置群消息屏蔽
	 */
	- (void)setIsShield:(BOOL)isShield handler:(JMSGCompletionHandler)handler;

#### 获取当前用户的群屏蔽列表
	/*!
	 * @abstract 获取所有设置群消息屏蔽的群组
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGGroup
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion 从服务器获取，返回所有设置群消息屏蔽的群组。
	 */
	+ (void)shieldList:(JMSGCompletionHandler)handler;

###<span id="JMSGFriendManager">好友管理</span>

添加、删除、接受、拒绝好友等操作 SDK 会作为通知事件下发,上层通过 [onReceiveNotificationEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveNotificationEvent:) 类中的方法监听此类事件. [使用示例](#监听下发事件实例)然后做出相应的处理，

#### JMSGFriendManager
#### 获取好友列表
	/*!
	 * @abstract 获取好友列表
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion 从服务器获取，异步返回结果，返回用户的好友列表。
	 * 建议开发者在 SDK 完全启动之后，再调用此接口获取数据
	 */
	+ (void)getFriendList:(JMSGCompletionHandler)handler;
##### 例子
	// get friend list
	[JMSGFriendManager getFriendList:^(id resultObject, NSError *error) {
		if(!error){
			NSArray *friendList = (NSArray *)resultObject;
			NSLog(@"获取好友列表：%@",friendList)
		}
	}];		
#### 发送添加好友请求
	/*!
	 * @abstract 发送添加好友请求
	 *
	 * @param username 对方用户名
	 * @param userAppKey 对方所在应用appkey,不传则默认是本应用
	 * @param reason 添加好友时的备注，可不填
	 *
	 * @param handler 结果回调。回调参数
	 *
	 * - resultObject 相应的返回对象
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion 在对方未做回应的前提下，允许重复发送添加好友的请求。
	 */
	+ (void)sendInvitationRequestWithUsername:(NSString *)username
	                                   appKey:(NSString *)userAppKey
	                                   reason:(NSString *)reason
	                        completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	[JMSGFriendManager sendInvitationRequestWithUsername:username appKey:appkey reason:nil completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSLog(@"发送邀请成功");
	    } else {
	        NSLog(@"发送邀请失败");
	    }
	}];

#### 接受好友邀请
	/*!
	 * @abstract 接受好友邀请
	 *
	 * @param username 对方用户名
	 * @param userAppKey 对方所在应用appkey,不传则默认是本应用
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 相应的返回对象
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 */
	+ (void)acceptInvitationResponseWithUsername:(NSString *)username
	                                      appKey:(NSString *)userAppKey
	                           completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	// 接受好友邀请
	[JMSGFriendManager acceptInvitationWithUsername:username appKey:appKey completionHandler:^(id resultObject, NSError *error) {
		dispatch_async(dispatch_get_main_queue(), ^{
	        if (!error) {
	            NSLog(@"接受成功");
	        }
	        else{
	            NSLog(@"接受失败");
	        }
	    });
	}];

#### 拒绝好友邀请
	/*!
	 * @abstract 拒绝好友邀请
	 *
	 * @param username 对方用户名
	 * @param userAppKey 对方所在应用appkey,不传则默认是本应用
	 * @param reason 拒绝理由，可不传
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 相应的返回对象
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 */
	+ (void)rejectInvitationWithUsername:(NSString *)username
	                              appKey:(NSString *)userAppKey
	                              reason:(NSString *)reason
	                   completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	// 拒绝好友邀请
	[JMSGFriendManager rejectInvitationWithUsername:username appKey:appKey reason:nil completionHandler:^(id resultObject, NSError *error) {
	    dispatch_async(dispatch_get_main_queue(), ^{
	        if (!error) {
	            NSLog(@"拒绝成功");
	        }
	        else{
	            NSLog(@"拒绝失败");
	        }
	    });
    }];
#### 删除好友
	/*!
	 * @abstract 删除好友
	 *
	 * @param username 好友username
	 * @param userAppKey 好友所在应用appkey,不传则默认是本应用
	 *
	 * @param handler 结果回调。回调参数：
	 *
	 * - resultObject 相应对象
	 * - error 错误信息
	 *
	 * 如果 error 为 nil, 表示设置成功
	 * 如果 error 不为 nil,表示设置失败
	 *
	 * @discussion
	 */
	+ (void)removeFriendWithUsername:(NSString *)username
	                          appKey:(NSString *)userAppKey
	               completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	// 比如将你好友列表里的 user 移除
	[JMSGFriendManager removeFriendWithUsername:user.username appKey:user.appkey completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
	       NSLog(@"删除好友成功");
	    }
	    else{
	       NSLog(@"删除好友失败");
	    }
    }];
		                        
### 黑名单

将用户加入黑名单后，将不在收到对方发来的任何消息。例如：A 用户将 B 用户加入黑名单，B 用户发送的消息，A 用户将收不到，A 用户发送的消息,B 用户依然可以看到。
#### 获取黑名单列表

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
##### 例子

```
//获取黑名单列表
[JMessage blackList:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 黑名单列表: %@ \n",resultObject);
    }
}];

```

#### 添加黑名单		

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
##### 例子

```
//添加黑名单
[JMSGUser addUsersToBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 添加黑名单成功:%@ \n ",resultObject);
    }
}];

```
	
#### 删除黑名单	

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
##### 例子

```
//删除黑名单
[JMSGUser delUsersFromBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
            NSLog(@"\n 添加黑名单成功:%@ \n ",resultObject);
        }
    }];

```
	             
### 免打扰

可以将用户/群组添加到“免打扰”列表中，收到免打扰用户/群组发过来的消息时，将不会有通知栏通知，但消息事件照常下发。
设置全局免打扰之后，收到所有消息都将不会有通知栏通知，效果类似。

#### 免打扰列表

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
	
##### 例子

```
//获取当前用户免打扰列
[JMessage noDisturbList:^(id resultObject, NSError *error) {
     if (!error) {
         NSLog(@"\n 免打扰列表: \n %@",resultObject);
     }
 }];
 
```  
#### 全局免打扰设置

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

##### 例子
 
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
	 
#### <span id="用户免打扰设置">用户免打扰设置</span>

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

##### 例子

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

#### 群组免打扰设置

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

##### 例子

```
使用方法参考“用户免打扰”例子

```

### 事件处理
#### 通知事件类型

	typedef NS_ENUM(NSInteger, JMSGEventNotificationType) {
    
	    /// 用户登录状态变更事件
	    /// 事件类型: 登录被踢
	    kJMSGEventNotificationLoginKicked = 1,
	    /// 事件类型: 非客户端修改密码强制登出事件
	    kJMSGEventNotificationServerAlterPassword = 2,
	    /// 事件类型：用户登录状态异常事件（需要重新登录）
	    kJMSGEventNotificationUserLoginStatusUnexpected = 70,
	    
	    /// 事件类型：当前登录用户信息变更通知事件(非客户端修改)
		 kJMSGEventNotificationCurrentUserInfoChange = 40,
	    
	    /// 好友相关事件
	    /// 事件类型: 收到好友邀请
	    kJMSGEventNotificationReceiveFriendInvitation   = 51,
	    /// 事件类型: 对方接受了你的好友邀请
	    kJMSGEventNotificationAcceptedFriendInvitation  = 52,
	    /// 事件类型: 对方拒绝了你的好友邀请
	    kJMSGEventNotificationDeclinedFriendInvitation  = 53,
	    /// 事件类型: 对方将你从好友中删除
	    kJMSGEventNotificationDeletedFriend             = 6,
		 /// 事件类型：非客户端修改好友关系收到好友更新事件
		 kJMSGEventNotificationReceiveServerFriendUpdate = 7,
	    
	    /// 消息事件
	    /// 事件类型: 群组被创建
	    kJMSGEventNotificationCreateGroup = 8,
	    /// 事件类型: 退出群组
	    kJMSGEventNotificationExitGroup = 9,
	    /// 事件类型: 群组添加新成员
	    kJMSGEventNotificationAddGroupMembers = 10,
	    /// 事件类型: 群组成员被踢出
	    kJMSGEventNotificationRemoveGroupMembers = 11,
	    /// 事件类型: 群信息更新
	    kJMSGEventNotificationUpdateGroupInfo = 12,
	};
	

* 消息事件，如：群事件，SDK会作为一个特殊的消息类型处理，上层通过[onReceiveMessage:error:](./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:)可监听到此事件。
* 非消息事件，如：被踢、加好友等,SDK会作为通知事件下发,上层通过 [onReceiveNotificationEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveNotificationEvent:) 类中的方法监听此类事件. [使用示例](#监听下发事件实例)

#### 用户登录状态变更事件
#### JMSGNotificationEvent
	/*!
	 * @abstract 事件类型
	 * @discussion 参考事件类型的定义 JMSGEventNotificationType
	 */
	@property(nonatomic, assign, readonly) JMSGEventNotificationType eventType;
	
	/*!
	 * @abstract 事件的描述信息
	 * @discussion 下发事件的文字描述，可能为空
	 */
	@property(nonatomic, strong, readonly) NSString *eventDescription;

#### 好友管理事件
#### JMSGFriendNotificationEvent 
	/*!
	 * @abstract 获取事件发生的理由
	 *
	 * @discussion 该字段由对方发起请求时所填，对方如果未填则将返回默认字符串
	 */
	- (NSString *JMSG_NULLABLE)getReason;
	 /*!
	  * @abstract 事件发送者的username
	  *
	  * @discussion 该字段由对方发起请求时所填，对方如果未填则将返回默认字符串
	  * 如果设置了noteName、nickname，返回优先级为noteName、nickname；否则返回username
	  */
	- (NSString *JMSG_NULLABLE)getFromUsername;
	
	/*!
	 * @abstract 获取事件发送者user
	 */
	- (JMSGUser *JMSG_NULLABLE)getFromUser;

##### 例子
	// 对方拒绝你的好友邀请，会有事件下发，可通过这个接口获取对方所填拒绝理由
	NSString *reason = [friendEvent getReason];
	// 获取事件发送者称呼，注意：返回优先级 备注名 -> 昵称 -> username
	NSString *name = [friendEvent getFromUsername];
	// 获取事件发送对象user
	JMSGUser *user = [friendEvent getFromUser];
		
#### 消息事件 
#### JMSGEventContent
	/*!
	 @abstract 展示此事件的文本描述
	
	 @discussion SDK 根据事件类型，拼接成完整的事件描述信息。
	 */
	- (NSString * JMSG_NONNULL)showEventNotification;  
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
##### 例子
	// 事件的文本描述
	if (message.contentType == kJMSGContentTypeEventNotification) {
		NSString *showText = [((JMSGEventContent *)message.content) showEventNotification];
	    //比如，在群group中，用户A邀请用户B加入了群,showText 如下：
	    //showText = "A邀请B加入了群组"
    }
	
	//根据事件类型，定制相应描述（以事件类型: 添加新成员为例子）
	JMSGEventContent *eventContent = (JMSGEventContent*)message.content;
	NSString *fromUsername = [eventContent getEventFromUsername];
	NSArray *toUsernameList = [eventContent getEventToUsernameList];
	if(eventContent.eventType == kJMSGEventNotificationAddGroupMembers) {
		NSString *showText = [NSString stringWithFormat:@"%@邀请了%@加入了群聊",fromUsername,[toUsernameList componentsJoinedByString:@","]];
	}


### 通知监听

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

	- (void)onLoginUserKicked;（此方法已过期，建议使用下面的新方法）
	
	// 通过event.eventType 判断事件类型,如：被踢事件、好友相关事件等
	- (void)onReceiveNotificationEvent:(JMSGNotificationEvent *)event;

<span id="监听下发事件实例"></span>
##### 示例代码
	// 通知事件监听
	- (void)onReceiveNotificationEvent:(JMSGNotificationEvent *)event{
	    switch (event.eventType) {
		     case kJMSGEventNotificationCurrentUserInfoChange:
		     	  NSLog(@"Current user info change Event ");
		     	  break;
	        case kJMSGEventNotificationReceiveFriendInvitation:
	            NSLog(@"Receive Friend Invitation Event ");
	            break;
	        case kJMSGEventNotificationAcceptedFriendInvitation:
	            NSLog(@"Accepted Friend Invitation Event ");
	            break;
	        case kJMSGEventNotificationDeclinedFriendInvitation:
	            NSLog(@"Declined Friend Invitation Event ");
	            break;
	        case kJMSGEventNotificationDeletedFriend:
	            NSLog(@"Deleted Friend Event ");
	            break;
            case kJMSGEventNotificationReceiveServerFriendUpdate:
	            NSLog(@"Receive Server Friend Update Event ");
	            break;
	        case kJMSGEventNotificationLoginKicked:
	            NSLog(@"Login Kicked Event ");
	            break;
	        case kJMSGEventNotificationServerAlterPassword:
	            NSLog(@"Server Alter Password Event ");
	            break;
	        case kJMSGEventNotificationUserLoginStatusUnexpected:
	            NSLog(@"User login status unexpected Event ");
	            break;
	        default:
		        NSLog(@"Other Notification Event ");
	            break;
	    }
	}	

### 结果回调

JMessage SDK 提供的很多接口都以异步方式返回，其回调都是一个类型为 JMSGCompletionHandler 的 block，其定义为

		typedef void (^JMSGCompletionHandler)(id resultObject, NSError *error);

JMSGCompletionHandler 有 2 个参数：

+ id resultObject 返回的结果对象
+ NSError *error 返回的错误

如果 error 不为 nil，则表示调用出错，error -> code 定义了错误码，error -> description 有错误的详细说明。也可以从文档里根据错误码找到进一步的错误说明信息。

如果 error 为 nil，则调用成功，resultObject 是返回结果对象。每个接口 resultObject 的实际类型不同，在每个接口的定义文档里会指定。实际使用时，应把该 resultObject 转型为该接口的正常对象。

与 JMSGCompletionHandler 类似的，还有另外一个 block 叫 JMSGAsyncDataHandler，用于返回媒体文件数据。



### 代理方法 

#### JMSGConversationDelegate
<span id="JMSGConversationDelegate"></span>

	/*!
	 * @abstract 会话信息变更通知
	 *
	 * @param conversation 变更后的会话对象
	 *
	 * @discussion 当前有二个属性: 会话标题(title), 会话图标
	 *
	 * 收到此通知后, 建议处理: 如果 App 当前在会话列表页，刷新整个列表；如果在聊天界面，刷新聊天标题。
	 */
	@optional
	- (void)onConversationChanged:(JMSGConversation *)conversation;
	
	/*!
	 * @abstract 当前剩余的全局未读数
	 *
	 * @param newCount 变更后的数量
	 */
	@optional
	- (void)onUnreadChanged:(NSUInteger)newCount;

***消息同步代理方法 Since v3.1.0***  
<span id="onSyncConversation:"></span>

```
/*!
 * @abstract 同步离线消息通知
 *
 * @param conversation    同步离线消息的会话
 * @param offlineMessages 离线消息数组
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
 * 注意一个会话只会上抛一个会话,这样会大大减轻上层在收到消息事件需要刷新 UI 的应用场景下,UI 刷新的压力.
 *
 * 上层通过此代理方法监听离线消息同步的会话,详见官方文档.
 *
 * @since 3.1.0
 */
@optional
- (void)onSyncOfflineMessageConversation:(JMSGConversation *)conversation
                         offlineMessages:(NSArray JMSG_GENERIC(__kindof JMSGMessage *)*)offlineMessages;
```
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

	
#### JMSGMessageDelegate
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
- (void)onSendMessageResponse:(JMSGMessage *)message
                        error:(NSError *)error;
```
<span id="onReceiveMessage:error:"></span>

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
 * 收到的消息里, 也包含服务器端下发的各类事件, 比如有人被加入了群聊. 这类事件处理为特殊的 JMSGMessage 类型.
 *
 * 事件类的消息, 基于 JMSGMessage 类里的 contentType 属性来做判断,
 * contentType = kJMSGContentTypeEventNotification.
 */
@optional
- (void)onReceiveMessage:(JMSGMessage *)message
                   error:(NSError *)error;
```
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
#### JMSGGroupDelegate
	/*!
	 * @abstract 群组信息 (GroupInfo) 信息通知
	 *
	 * @param group 变更后的群组对象
	 *
	 * @discussion 如果想要获取通知, 需要先注册回调. 具体请参考 JMessageDelegate 里的说明.
	 */
	@optional
	- (void)onGroupInfoChanged:(JMSGGroup *)group;

#### JMSGUserDelegate（方法已过期，建议使用JMSGEventDelegate）
	/*!
	 * @abstract 当前登录用户被踢下线通知(方法已过期，建议使用新方法)
	 *
	 * @discussion 一般可能是, 该用户在其他设备上登录, 把当前设备的登录踢出登录.
	 *
	 * SDK 收到服务器端下发事件后, 会内部退出登录.
	 * App 也应该退出登录. 否则所有的 SDK API 调用将失败, 因为 SDK 已经退出登录了.
	 *
	 * 注意: 这是旧版本的监听方法，建议不要使用,已经过期,
	 * 使用 JMSGEventDelegate 类中的 onReceiveNotificationEvent 新的监听方法.
	 */
	@optional
	- (void)onLoginUserKicked;

<span id="JMSGEventDelegate"></span>

#### JMSGEventDelegate 
	/*!
	 * @abstract 监听通知事件
	 *
	 * @param event 下发的通知事件
	 *
	 * @discussion SDK 收到服务器端下发事件后，会以通知代理的方式给到上层,通过event.eventType判断事件类型.
	 *
	 * 注意：
	 * 消息事件，如：群事件，SDK会作为一个特殊的消息类型下发，上层依旧通过 JMSGMessageDelegate 监听消息事件.
	 *
	 * 非消息事件，如：被踢下线、加好友，SDK会作为通知事件下发,上层通过本类 JMSGEventDelegate 的方法可监听此类事件.
	 */
	@optional
	- (void)onReceiveNotificationEvent:(JMSGNotificationEvent *)event;

	
#### JMSGDBMigrateDelegate 
	/*!
	 * @abstract 数据库升级开始
	 */
	@optional
	- (void)onDBMigrateStart;
	
	/*!
	 * @abstract 数据库升级完成
	 *
	 * @param error 如果升级失败, 则 error 不为 nil. 反之 error 为 nil 时升级成功.
	 *
	 * @discussion SDK会有自动重试, 竭力避免失败. 如果实在返回失败, 建议提示用户重新安装 App.
	 */
	@optional
	- (void)onDBMigrateFinishedWithError:(NSError *)error;
	
### 跨应用API接口
##### 跨应用通信是指允许同一开发者账号下的不同应用能互相通信，以满足开发者对于不同appKey下应用通信的需求。

#### 跨应用用户管理
批量获取跨应用的用户信息

	/*!
	 * @abstract 批量获取跨应用的用户信息
	 *
	 * @param usernameArray 用户名列表。NSArray 里的数据类型为 NSString
	 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里的数据类型为 JMSGUser
	 *
	 * @discussion 这是一个批量接口。
	 */
	+ (void)userInfoArrayWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
	                                appKey:( NSString *JMSG_NULLABLE)userAppKey
	                     completionHandler:(JMSGCompletionHandler)handler;
##### 例子	                     
	// 批量获取跨应用的用户信息
	// 注：usernameArray 里的username都应该是在你所填userAppKey应用的user
	[JMSGUser userInfoArrayWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"appkey" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSArray *userList =(NSArray *)resultObject;
	        NSLog(@"userList:%@",userList);
	    }
	}];
#### 跨应用消息管理
1、发送跨应用单聊文本消息
	
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
	
2、发送跨应用单聊图片消息

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
	
3、发送跨应用单聊语音消息

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
	                        
4、发送跨应用单聊文件消息

	/*!
	 * @abstract 发送跨应用单聊文件消息
	 *
	 * @param fileData 文件数据数据
	 * @param fileName 文件名
	 * @param username 单聊对象 username
	 *
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleFileMessage:(NSData *)fileData
	                     fileName:(NSString *)fileName
	                       toUser:(NSString *)username
	                       appKey:(NSString *)userAppKey;

5、发送跨应用单聊位置消息

	/*!
	 * @abstract 发送跨应用单聊地理位置消息
	 * @param latitude 纬度
	 * @param longitude 经度
	 * @param scale 缩放比例
	 * @param address 详细地址
	 * @param username 单聊对象
	 * @param userAppKey 单聊对象的appKey
	 * @discussion 快捷方法，不需要先创建消息而直接发送。
	 */
	+ (void)sendSingleLocationMessage:(NSNumber *)latitude
	                        longitude:(NSNumber *)longitude
	                            scale:(NSNumber *)scale
	                          address:(NSString *)address
	                           toUser:(NSString *)username
	                           appKey:(NSString *)userAppKey;

#### 跨应用会话管理
1、获取跨应用单聊会话

	/*!
	 * @abstract 会话目标用户所在的 appKey
	 *
	 * @discussion 这是为了跨应用聊天而新增的一个字段.
	 * 如果此字段为空, 则表示为默认的主应用.
	 *
	 * 单聊会话时, 如果单聊对象用户不属于主应用, 则此字段会有值.
	 */
	@property(nonatomic, strong, readonly) NSString *targetAppKey;
	
	/*!
	 * @abstract 获取跨应用单聊会话
	 *
	 * @param username 单聊对象的username
	 * @param userAppKey 单聊对象的appkey
	 *
	 * @discussion 如果会话还不存在，则返回 nil
	 *
	 */
	+ (JMSGConversation * JMSG_NULLABLE)singleConversationWithUsername:(NSString *)username
	  
                                                          appKey:(NSString *)userAppKey;
2、创建跨应用单聊会话

	/*!
	 * @abstract 创建跨应用单聊会话
	 *
	 * @param username 单聊对象的username
	 * @param userAppKey 单聊对象的appkey
	 * @param handler 结果回调。正常返回时 resultObject 类型为 JMSGConversation。
	 *
	 * @discussion 如果会话已经存在，则直接返回。如果不存在则创建。
	 */
	+ (void)createSingleConversationWithUsername:(NSString *)username
	                                      appKey:(NSString *)userAppKey
	                           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
	                           
##### 例子
	// 创建跨应用会话
	[JMSGConversation createSingleConversationWithUsername:@"username" appKey:@"appkey"  completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
	        NSLog(@"创建跨应用会话成功");
        } else {
            NSLog(@"创建跨应用会话失败");
        }
	}];
		            
3、删除跨应用单聊会话

	/*!
	 * @abstract 删除跨应用单聊会话
	 *
	 * @param username 单聊用户名
	 * @param userAppKey 单聊用户的appkey
	 *
	 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
	 */
	+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username
	                                      appKey:(NSString *)userAppKey;                          

#### 跨应用群组管理
1、添加群组跨应用成员

	/*!
	 * @abstract 添加群组跨应用成员
	 *
	 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                             appKey:userAppKey
	                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	[group addMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被添加用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSLog(@"\n 添加群组跨应用成员 成功");
	    }
	}];

2、删除群组跨应用成员

	/*!
	 * @abstract 删除群组跨应用成员
	 *
	 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                                appKey:userAppKey
	                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
	
##### 例子
	[group removeMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被删除用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSLog(@"\n 添删除组跨应用成员 成功");
	    }
	}];
#### 跨应用黑名单管理
1、跨应用添加黑名单	

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
##### 例子

```
//添加黑名单
[JMSGUser addUsersToBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被添加用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
       if (!error) {
           NSLog(@"\n 跨应用添加黑名单成功:%@ \n ",resultObject);
       }
   }];

```	   
2、跨应用删除黑名单	

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
	            
##### 例子         

```
//删除黑名单
[JMSGUser delUsersFromBlacklist:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被删除用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        NSLog(@"\n 跨应用删除黑名单成功:%@ \n ",resultObject);
    }
}];
 
``` 
#### 跨应用免打扰管理
跨应用用户免打扰设置

本应用用户免打扰设置中支持跨应用功能，详细使用请查看["用户免打扰设置"](#用户免打扰设置)。
#### 跨应用好友管理
本应用的好友管理接口支持跨应用，详细请查看[“好友管理”](#JMSGFriendManager)

## 错误码定义

参考文档：[IM iOS SDK 错误码列表](https://docs.jiguang.cn/jmessage/client/im_errorcode_ios/)

