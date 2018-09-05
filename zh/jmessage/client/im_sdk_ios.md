<h1>iOS SDK 开发指南</h1>

## 概述

极光 IM（英文名JMessage）为开发者提供易用可靠的 IM 开发框架，开发者可集成SDK，快速实现即时通讯功能。JMessage iOS SDK 支持 iOS 7 以上系统。
要了解极光 IM 的详细信息，请参考文档：[JMessage 产品简介](https://docs.jiguang.cn/jmessage/guideline/jmessage_guide/)


### 功能

极光IM 最核心的功能是 IM 即时消息的功能。

+ 单聊，群聊；
+ 消息类型：文本、语音、图片、文件、位置等；
+ 用户未在线时保存离线消息；
+ 保证消息及时下发；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

## API 接口

需要了解完整的 SDK API，有两种方式：

+ 直接查看 JMessage.framework 里的 Headers 文件。这些头文件定义了 SDK 提供的对外接口，带有完善的注释与说明，甚至样例代码。
+ 使用 Appledoc 生成的文档的在线版本：<a href="https://docs.jiguang.cn/jmessage/client/jmessage_ios_appledoc_html/" target="_blank">iOS SDK APIs</a>

以下简要地列举 SDK API 提供的功能，同时提供部分简单的例子。

### SDK初始化

JMessage.h 里定义的 setupJMessage 方法，需要在应用初始化时调用。	
SDK 初始化时，可设置是否启用消息记录漫游。		
打开消息漫游之后，用户多个设备之间登录时，SDK会自动将历史消息同步到本地，同步完成之后SDK会以 Conversation 为单位触发代理方法`onSyncRoamingMessageConversation:`通知上层刷新,具体方法见[消息同步监听代理](#消息同步版本说明)

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
 * 本地仍须调用 UIApplication:setApplicationIconBadgeNumber 函数来设置角标.
 *
 * 该功能解决的问题是, 服务器端推送 APNs 时, 并不知道客户端原来已经存在的角标是多少, 指定一个固定的数字不太合理.
 *
 * APNS 服务器端角标功能提供:
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

### 注册与登录
#### 用户注册
	/*!
	 * @abstract 新用户注册(支持携带用户信息字段)
	 *
	 * @param userInfo  用户名. 长度 4~128 位.
	 *                  支持的字符: 字母,数字,下划线,英文减号,英文点,@邮件符号. 首字母只允许是字母或者数字.
	 * @param password  用户密码. 长度 4~128 位.
	 * @param userInfo  用户信息类，注册时携带用户信息字段，除用户头像字段
	 * @param handler   结果回调. 返回正常时 resultObject 为 nil.
	 *
	 * @discussion 注意: 注册时不支持上传头像，其他信息全部支持
	 */
	+ (void)registerWithUsername:(NSString *)username
	                    password:(NSString *)password
	                    userInfo:(JMSGUserInfo *JMSG_NULLABLE)userInfo
	           completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	JMSGUserInfo *info = [[JMSGUserInfo alloc]init];
	info.nickname = @"昵称";
	info.signature = @"签名";
	//···
	[JMSGUser registerWithUsername:@"用户名" password:@"密码" userInfo:info completionHandler:^(id resultObject, NSError *error) {
         if (!error) {
             //注册成功
         } else {
            //注册失败
         }
     }];
#### 用户登录

+ 回调中返回登录设备信息

```
/*!
 * @abstract 用户登录，返回登录设备信息
 *
 * @param username    登录用户名. 规则与注册接口相同.
 * @param password    登录密码. 规则与注册接口相同.
 * @param devicesInfo 登录设备回调，返回数据为 NSArray<JMSGDeviceInfo>
 * @param handler     结果回调
 *
 * - resultObject 简单封装的user对象，上层不要直接使用 resultObject 对象做操作, 因为它只是一个简单封装的user对象
 * - error 错误信息
 *
 * @discussion 回调中 devices 返回的是设备信息，具体属性请查看 JMSGDeviceInfo 类
 */
+ (void)loginWithUsername:(NSString *)username
                 password:(NSString *)password
              devicesInfo:(nullable void(^)(NSArray <__kindof JMSGDeviceInfo *>*devices))devicesInfo
        completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

```
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
```        
        
##### 例子
	[JMSGUser loginWithUsername:@"用户名" password:@"密码" completionHandler:^(id resultObject, NSError *error) {
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

### 多端同时在线
SDK 从 3.3.0版本开始支持多端同时在线，具体规则见[多端在线说明](../guideline/faq/#_5)

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
#### 统一上传用户信息更新
	/*!
	 * @abstract 更新用户信息（支持将字段统一上传）
	 *
	 * @param userInfo  用户信息对象，类型是 JMSGUserInfo
	 * @param handler   更新用户信息回调接口函数
	 *
	 * @discussion 参数 userInfo 是 JMSGUserInfo 类，JMSGUserInfo 仅可用于修改用户信息
	 */
	+ (void)updateMyInfoWithUserInfo:(JMSGUserInfo *)userInfo
	               completionHandler:(JMSGCompletionHandler)handler;
##### 例子
	JMSGUserInfo *userInfo = [[JMSGUserInfo alloc] init];
    userInfo.nickname = @"new nick name";
    userInfo.address = @"new address";
    [JMSGUser updateMyInfoWithUserInfo:userInfo completionHandler:^(id resultObject, NSError *error) {
        //
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

<span id="消息同步版本说明"></span>
### 从3.1.0版本开始接收消息的变化
JMessage SDK 3.1.0 版本开始，SDK 将消息下发分为在线下发和离线下发两种类型，离线下发包含了离线消息和漫游消息。 先明确这几个概念：

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
        <a href="../jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:
        </a>
      </td>
      <td>
        逐条下发，每次都触发
        <a href="../jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:</a>
      </td>
      <td>无</td>
    </tr>
    <tr>
      <td>Version >= 3.1.0</td>
      <td>
        逐条下发，每次都触发
        <a href="../jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:">
          onReceiveMessage:</a>
      </td>
      <td>
        以会话为单位，触发一次下发
        <a href="../jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncOfflineMessageConversation:offlineMessages:">
          onSyncOfflineMessageConversation:</a>
      </td>
      <td style="word-break: break-all;">
        以会话为单位，触发一次下发
        <a href="../jmessage_ios_appledoc_html/Protocols/JMSGConversationDelegate.html#//api/name/onSyncRoamingMessageConversation:">
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

SDK 3.2.1 版本开始（包括3.2.1），离线事件也会走消息同步策略。
离线事件分为：

+ 群事件：如果有离线的群事件，也会触发一次离线消息的代理方法。
+ 非群事件：其他事件还是不变，走以前的代理方法。

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
	
#### 创建文本消息
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
+ 创建消息

```
JMSGTextContent *content = [[JMSGTextContent alloc] initWithText:@"textContent"];
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```

#### 创建图片消息
+ JMSGImageContent 

```
/*!
 * @abstract 初始化消息图片内容
 *
 * @param data 图片数据
 */
- (nullable instancetype)initWithImageData:(NSData * JMSG_NONNULL)data;
```
+ 创建消息

```
JMSGImageContent *content = [[JMSGImageContent alloc] initWithImageData:imageData];
content.format = @"png";//可选设置
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```
#### 创建语音消息
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
+ 创建消息

```
JMSGVoiceContent *content = [[JMSGVoiceContent alloc] initWithVoiceData:data voiceDuration:@(10)];
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```
#### 创建视频消息
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
+ 创建消息

```
JMSGVideoContent *content = [[JMSGVideoContent alloc] initWithVideoData:videoData thumbData:thumbData duration:@(10)];
content.format = @"mp4";//可选设置
content.fileName = @"myvideofile";//可选设置
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```
#### 创建文件消息
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
+ 创建消息

```
JMSGFileContent *content = [[JMSGFileContent alloc] initWithFileData:data fileName:@"myvideofile"];
content.format = @"doc";//可选设置
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```
#### 创建位置消息
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
+ 创建消息

```
JMSGLocationContent *content = [[JMSGLocationContent alloc] initWithLatitude:@(100) longitude:@(100) scale:@(1) address:@"address"];
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```
#### 创建自定义消息
+ JMSGCustomContent 

```
/*!
 * @abstract 预期使用的初始化方法
 *
 * @param customDict 初始化时指定的字典
 */
- (instancetype)initWithCustomDictionary:(NSDictionary * JMSG_NULLABLE)customDict;

// 添加一个键值对
- (BOOL)addObjectValue:(NSObject *)value forKey:(NSString *)key;

// 快捷添加 String 类型 value 的方法
- (BOOL)addStringValue:(NSString *)value forKey:(NSString *)key;

// 快捷添加 Number 类型 value 的方法
- (BOOL)addNumberValue:(NSNumber *)value forKey:(NSString *)key;

/*!
 * @abstract 设置该自定义消息内容的文本描述
 * @param contentText 内容文本描述
 * @discussion 用于展示在会话列表, 文本地简要描述这条消息.如果未设置, 则默认值为 "[自定义消息]"
 */
- (void)setContentText:(NSString *)contentText;
```
+ 创建消息

```
JMSGCustomContent *content = [[JMSGCustomContent alloc] initWithCustomDictionary:@{@"key":@"value"}];
[content addNumberValue:@(1) forKey:@"number_key"];
[content addStringValue:@"string" forKey:@"string_key"];
[content setContentText:@"自定的消息"];
JMSGMessage *singleMessage = [JMSGMessage createSingleMessageWithContent: content username:@"username"];
JMSGMessage *groupMessage = [JMSGMessage createGroupMessageWithContent: content groupId:@"groupId"];
```

#### 发送消息
	/*!
	 * @abstract 发送消息（已经创建好的）
	 *
	 * @param message 消息对象。
	 *
	 * @discussion 此接口与 createMessage:: 相关接口配合使用，创建好后使用此接口发送。
	 */
	+ (void)sendMessage:(JMSGMessage *)message;

#### 消息转发
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

#### 消息撤回
***Since 3.2.0***

由消息撤回方发起调用，在一定时间内，SDK 可以撤回会话中某条消息。


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

#### 获取聊天室会话

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

#### 创建聊天室会话			            

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

#### 删除聊天室会话

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

#### 会话列表列表
	/*!
	 * @abstract 返回 conversation 列表（异步,已经排序）
	 *
	 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里成员的类型为 JMSGConversation
	 *
	 * @discussion 当前是返回所有的 conversation 列表，不包括聊天室会话，默认是已经排序。
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

#### 聊天室会话列表

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

#### 创建多媒体消息对象

```
/*!
 * @abstract 创建消息对象（多媒体消息，异步）
 *
 * @param content 准备好的多媒体内容，如：图片、语音、文件等
 * @param handler 结果回调. 正常返回时 resultObject 类型为 JMSGMessage.
 *
 * @discussion 注意：对于多媒体消息，因为 SDK 要做缩图有一定的性能损耗，图片文件很大时存储落地也会较慢。
 * 所以创建图片消息，建议使用这个异步接口。
 */
- (void)createMessageAsyncWithMediaContent:(JMSGMediaAbstractContent *)content
                         completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
##### 例子
	//_conversation 为Conversation的实例对象
	[_conversation createMessageAsyncWithMediaContent:mediaContent completionHandler:^(id resultObject, NSError *error) {
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
#### 发送视频消息

```
/*!
 * @abstract 发送视频消息
 *
 * @param videoData 视频消息数据
 * @param thumbData 视频封面图片
 * @param videoFormat 视频格式，如：mp4、mov
 * @param duration  视频消息时长（秒）. 长度必须大于 0.
 *
 * @discussion 快捷发送消息接口。如果发送语音消息不需要附加 extra，则使用此接口更方便。
 */
- (void)sendVideoMessage:(NSData *)videoData
               thumbData:(NSData *JMSG_NULLABLE)thumbData
             videoFormat:(NSString *JMSG_NULLABLE)videoFormat
                duration:(NSNumber *)duration;
```

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
群组分为私有群和公开群，群的类型在创建成功之后就不能修改，公开群需要申请，等管理员审批同意之后方可入群。

#### 群组成员
群组成员是由 `JMSGUser` 对象组成的，但是群成员有更多的独有属性，如：群昵称、入群时间等，所以从 JMessage v3.7.0 开始新建群组成员信息类 `JMSGGroupMemberInfo`。	
在 `JMSGGroupMemberInfo `类中包含了群成员 JMSGUser 对象、群昵称、入群时间、成员角色等属性。

```
/*!
 * 群成员信息类
 *
 * #### 可通过 [JMSGGroup memberInfoList:]和 [JMSGGroup memberInfoWithUsername:appkey:] 两个接口获取群成员信息
 */
@interface JMSGGroupMemberInfo : NSObject

/// 成员用户信息
@property(nonatomic, strong, readonly) JMSGUser *JMSG_NULLABLE user;
/// 入群时间
@property(nonatomic, assign, readonly) UInt64 ctime;
/// 群昵称
@property(nonatomic, strong, readonly) NSString *JMSG_NULLABLE groupNickname;
/// 群组成员的身份
@property(nonatomic, assign, readonly) JMSGGroupMemberType memberType;

/*!
 * @abstract 获取群成员的展示名
 *
 * @discussion 展示优先级：群昵称 > 好友备注(user.noteName) > 用户昵称(user.nickname) > 用户名(user.username)
 *
 * #### 同接口 [JMSGGroup memberDisplayName:] 相同效果
 */
- (NSString *JMSG_NULLABLE)displayName;
@end
```

#### 创建群组（(只能创建私有群)）
	/*!
	 * @abstract 创建群组(只能创建私有群)
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
#### 创建群组（可创建私有群、公开群）

```
/*!
 * @abstract 创建群组（可创建私有群、公开群）
 *
 * @param groupInfo     群信息类，如：群名、群类型等，详细请查看 JMSGGroupInfo 类
 * @param usernameArray 初始成员列表。NSArray 里的类型是 NSString
 * @param handler       结果回调。正常返回 resultObject 的类型是 JMSGGroup。
 *
 * @discussion 向服务器端提交创建群组请求，返回生成后的群组对象.
 * 返回群组对象, 群组ID是App 需要关注的, 是后续各种群组维护的基础.
 */
+ (void)createGroupWithGroupInfo:(JMSGGroupInfo *)groupInfo
                     memberArray:(NSArray JMSG_GENERIC(__kindof NSString *) *JMSG_NULLABLE)usernameArray
               completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

##### 例子

```
JMSGGroupInfo *info = [[JMSGGroupInfo alloc] init];
info.name =@"公开群001";
info.groupType = kJMSGGroupTypePublic;
info.desc = @"这个群组是公开群";
[JMSGGroup createGroupWithGroupInfo:info memberArray:nil completionHandler:^(id resultObject, NSError *error) {
    if (!error) {
        myGroup = resultObject;
    }
}];
```


#### 获取公开群列表

支持分页获取 AppKey 下的公开群信息，注意接口返回的数组元素是 JMSGGroupInfo ，而不是 JMSGGroup ，需要获取群组的属性值和调用群组接口，则需要通过 JMSGGroupInfo 中的 gid 获取到 JMSGGroup 对象先，然后再操作

```
/*!
 * @abstract 分页获取 appkey 下所有公开群信息
 *
 * @param appkey    群组所在的 AppKey，不填则默认为当前应用 AppKey
 * @param start     分页获取的下标，第一页从  index = 0 开始
 * @param count     每一页的数量，最大值为500
 * @param handler   结果回调，NSArray<JMSGGroupInfo>
 *
 * #### 注意：返回数据中不是 JMSGGroup 类型，而是 JMSGGroupInfo 类型，只能用于展示信息，如果想要调用相关群组 API 接口则需要通过 gid 获取到 JMSGGroup 对象才可以调用
 */
+ (void)getPublicGroupInfoWithAppKey:(NSString *JMSG_NULLABLE)appkey
                               start:(NSInteger)start
                               count:(NSInteger)count
                   completionHandler:(JMSGCompletionHandler)handler;
```

#### 更新群组信息
	/*!
	 * @abstract 更新群组信息
	 *
	 * @param groupId 待更新的群组ID
	 * @param groupName 新名称
	 * @param groupDesc 新描述
	 * @param handler 结果回调. 正常返回时, resultObject 为 nil.
	 *
	 * @discussion 注意：name 和 desc 不允许传空字符串
	 */
	+ (void)updateGroupInfoWithGroupId:(NSString *)groupId
	                              name:(NSString *JMSG_NULLABLE)groupName
	                              desc:(NSString *JMSG_NULLABLE)groupDesc
	                 completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
##### 例子
	// 更新群组信息
	[JMSGGroup updateGroupInfoWithGroupId:@"group.gid" name:@"新群名" desc:@"新群描述" completionHandler:^(id resultObject, NSError *error) {
                if (!error) {
                    NSLog(@"更新群组信息成功!");
                }
    }];
    
#### 更新群组信息（统一字段上传）
	/*!
	 * @abstract 更新群信息（统一字段上传）
	 *
	 * @param gid         群组 id
	 * @param groupInfo   群信息类，详细请查看 JMSGGroupInfo 类
	 * @param handler     结果回调. 正常返回时, resultObject 为 nil.
	 *
	 * @discussion 注意：修改群名称和群描述时参数不允许传空字符串
	 */
	+ (void)updateGroupInfoWithGid:(NSString *)gid
	                     groupInfo:(JMSGGroupInfo *)groupInfo
	             completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;    
#### 更新头像
	/*!
	 * @abstract 更新群头像（支持传图片格式）
	 *
	 * @param groupId         待更新的群组ID
	 * @param avatarData      头像数据
	 * @param avatarFormat    头像格式，可以为空，不包括"."
	 * @param handler         回调
	 *
	 * @discussion 头像格式参数直接填格式名称，不要带点。正确：@"png"，错误：@".png"
	 */
	+ (void)updateGroupAvatarWithGroupId:(NSString *JMSG_NONNULL)groupId
	                          avatarData:(NSData *JMSG_NONNULL)avatarData
	                        avatarFormat:(NSString *JMSG_NULLABLE)avatarFormat
	                   completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;    

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
    
 
#### 添加群组成员
 
	/*!
	 * @abstract 添加群组成员
	 *
	 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
    
#### 删除群组成员

	/*!
	 * @abstract 删除群组成员
	 *
	 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
	        

#### 设置群管理员

+ 范围：私有群和公开群都增加管理员角色。
+ 描述：仅群主可对群管理员进行管理，可指定群内任意成员成为管理员，也可取消管理员身份。
+ 管理员权限：拥有普通群成员的所有基础功能和权限，除此之外还拥有更高的权限:设置禁言、审批入群.

```
/*!
 * @abstract 添加管理员
 *
 * @param username 用户名
 * @param appkey   用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 注意：非 VIP 应用最多设置 15 个管理员，不包括群主本身
 */
- (void)addGroupAdminWithUsername:(NSString *JMSG_NONNULL)username
                           appKey:(NSString *JMSG_NULLABLE)appkey
                completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;

/** @abstract 批量添加管理员*/
- (void)addGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                            appKey:(NSString *JMSG_NULLABLE)appkey
                 completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
```
/*!
 * @abstract 删除管理员
 *
 * @param username 用户名
 * @param appkey   用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 */
- (void)deleteGroupAdminWithUsername:(NSString *)username
                              appKey:(NSString *JMSG_NULLABLE)appkey
                   completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
                              
/** @abstract 批量删除管理员*/
- (void)deleteGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                               appKey:(NSString *JMSG_NULLABLE)appkey
                    completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;                   
```

```
/*!
 * @abstract 判断用户是否是管理员
 *
 * @param username  待判断用户的用户名
 * @param appKey    待判断用户的appKey，若传入空则默认使用本应用appKey
 */
- (BOOL)isAdminMemberWithUsername:(NSString *JMSG_NONNULL)username
                           appKey:(NSString *JMSG_NULLABLE)appKey;

/*!
 * @abstract 管理员列表
 *
 * @return 管理员列表. NSArray 里成员类型是 JMSGUser
 *
 * @discussion 注意：返回列表中包含群主；仅在获取群成员成功后此接口才有效
 */
- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)groupAdminMembers;
```

    
#### 修改群类型
创建群组之后，可以通过此接口修改群的类型，公开群、私有群相互切换

```
/*!
 * @abstract 修改群组类型
 *
 * @param type    群类型，公开群、私有群
 * @param handler 结果回调。error = nil 表示成功
 *
 * @discussion 对于已经创建的群组，可以通过此接口来修改群组的类型
 */
- (void)changeGroupType:(JMSGGroupType)type handler:(JMSGCompletionHandler)handler;
```
    
#### 移交群主
+ 群主可选择群内任意一位成员进行群主变更，把群主权限移交给他，移交后之前的群主变为普通群成员。
+ 适用群组类型：私有群和公开群都拥有此功能
+ 仅群主有此权限

```
/*!
 * @abstract 移交群主
 *
 * @param username 新群主用户名
 * @param appkey   新群主用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 */
- (void)transferGroupOwnerWithUsername:(NSString *JMSG_NONNULL)username
                                appKey:(NSString *JMSG_NULLABLE)appkey
                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 申请入群
对于公开群，需要申请或者其他群成员邀请，并由管理员审批同意才可以入群

```
/*!
 * @abstract 申请加入群组
 *
 * @param gid     群组 gid
 * @param reason   申请原因
 * @param handler 结果回调
 *
 * @discussion 只有公开群需要申请才能加入，私有群不需要申请。
 */
+ (void)applyJoinGroupWithGid:(NSString *JMSG_NONNULL)gid
                       reason:(NSString *JMSG_NULLABLE)reason
            completionHandler:(JMSGCompletionHandler)handler;
```

#### 管理员审批入群申请
当有用户申请加入群组，管理员会接收到入群申请事件 [JMSGApplyJoinGroupEvent](#跳转-入群申请事件) ，管理员需要对该申请做一个审批，如果管理员拒绝了该申请，则申请人和被申请人都会收到一个管理员拒绝入群申请事件 [JMSGGroupAdminRejectApplicationEvent](#跳转-管理员拒绝入群申请事件)。

```
/*!
 * @abstract 管理员审批入群申请
 *
 * @patam eventId     入取申请事件的 id，详情请查看 JMSGApplyJoinGroupEvent 类
 * @param gid         群组 gid
 * @param joinUser    入群的用户
 * @param applyUser   发起申请的的用户，如果是主动申请入群则和 member 是相同的
 * @param isAgree     是否同意申请，YES : 同意， NO: 不同意
 * @param reason      拒绝申请的理由，选填
 * @param handler     结果回调
 *
 * @discussion 只有管理员才有权限审批入群申请，SDK 不会保存申请入群事件(JMSGApplyJoinGroupEvent)，上层可以自己封装再保存，或则归档直接保存，以便此接口取值调用。
 */
+ (void)processApplyJoinGroupEventID:(NSString *JMSG_NONNULL)eventId
                                 gid:(NSString *JMSG_NONNULL)gid
                            joinUser:(JMSGUser *JMSG_NONNULL)joinUser
                           applyUser:(JMSGUser *JMSG_NONNULL)applyUser
                             isAgree:(BOOL)isAgree
                              reason:(NSString *JMSG_NULLABLE)reason
                             handler:(JMSGCompletionHandler)handler;
```
```
/*!
 * @abstract 管理员审批入群申请（批量接口）
 *
 * @patam events      入取申请事件的 eventId 数组，详情请查看 JMSGApplyJoinGroupEvent 类
 * @param isAgree     是否同意申请，YES : 同意， NO: 不同意
 * @param reason      拒绝申请的理由，选填
 * @param isSendInviter 是否将结果通知给邀请方，默认是 NO
 * @param handler     结果回调
 *
 * @discussion 批量处理接口，event 下包含的所有被邀请者会被一起审批处理。只有管理员才有权限审批入群申请。
 */
+ (void)processApplyJoinGroupEvents:(NSArray <__kindof NSString *>*)events
                            isAgree:(BOOL)isAgree
                             reason:(NSString *JMSG_NULLABLE)reason
                        sendInviter:(BOOL)isSendInviter
                            handler:(JMSGCompletionHandler)handler;
```

#### 群成员禁言

```
/*!
 * @abstract 群成员禁言设置
 *
 * @param isSilence 是否禁言， YES:是 NO: 否
 * @param username  带设置的用户的 username
 * @param username  带设置的用户的 appKey,若传入空则默认使用本应用appKey
 * @param handler   结果回调
 *
 * @discussion 注意: 目前 SDK 只支持群主设置群里某个用户禁言
 */
- (void)setGroupMemberSilence:(BOOL)isSilence
                     username:(NSString *JMSG_NONNULL)username
                       appKey:(NSString *JMSG_NULLABLE)appKey
                      handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```


```
/*!
 * @abstract 判断用户在该群内是否被禁言
 *
 * @param username  待判断用户的用户名
 * @param appKey    待判断用户的appKey，若传入空则默认使用本应用appKey
 */
- (BOOL)isSilenceMemberWithUsername:(NSString *JMSG_NONNULL)username
                             appKey:(NSString *JMSG_NULLABLE)appKey;
```


```
/*!
 * @abstract 禁言列表
 *
 * @return 禁言的成员列表. NSArray 里成员类型是 JMSGUser
 */
- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)groupSilenceMembers;
```

#### 群消息屏蔽
群组被设置为屏蔽之后，将收不到该群的消息，但是群成员变化事件还是能正常收到。


```
/*!
 * @abstract 该群是否已被设置为消息屏蔽
 *
 * @discussion YES:是 , NO: 否
 */
@property(nonatomic, assign, readonly) BOOL isShieldMessage
```

```
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

```

```
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

```


#### 成员群昵称

```
/*!
 * @abstract 设置成员群昵称
 *
 * @param nickname 群昵称
 * @param username 目标用户的 username
 * @param appKey   目标用户的 appKey,若传入空则默认使用本应用appKey
 */
- (void)setGroupNickname:(NSString *JMSG_NULLABLE)nickname
                username:(NSString *JMSG_NONNULL)username
                  appKey:(NSString *JMSG_NULLABLE)appKey
                 handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

```
/*!
 * @abstract 获取成员的群昵称
 *
 * @param  username 群成员 username
 * @patam  appKey   群成员 appKey，不传则默认是本应用 appkey
 * @return 群昵称
 *
 * @discussion 还可以通过获取群成员信息 JMSGGroupMemberInfo 来获取群昵称
 */
- (NSString *JMSG_NULLABLE)groupNicknameWithUsername:(NSString *)username
                                              appKey:(NSString *JMSG_NULLABLE)appKey;
```
                                           
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
	 * @abstract 获取所有群成员信息列表
	 *
	 * @handler 成员列表. 类型为 NSArray，里面元素为 JMSGGroupMemberInfo.
	 *
	 * @discussion 返回数据中的 JMSGGroupMemberInfo 包含了成员 user 信息、入群时间、群昵称等
	 */
	- (void)memberInfoList:(JMSGCompletionHandler JMSG_NULLABLE)handler;

#### 获取群成员(单个)
	
	/*!
	 * @abstract 获取单个群成员信息
	 *
	 * @param  username 目标用户 username
	 * @param  appkey   目标用户 appkey，不传则默认本应用 appkey
	 * @return 群成员信息对象
	 *
	 * @discussion JMSGGroupMemberInfo 包含了成员 user 信息、入群时间、群昵称等
	 */
	- (JMSGGroupMemberInfo *JMSG_NULLABLE)memberInfoWithUsername:(NSString *JMSG_NONNULL)username
	                                                      appkey:(NSString *JMSG_NULLABLE)appkey;


    
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
    
    
#### 解散群组
+ 群组类型：普通群和受限群都拥有此功能
+ 权限：仅群主可解散，普通群成员和管理员无此权限

```
/*!
 * @abstract 解散群组
 *
 * @patam gid     需要解散的群组 id
 * @param handler 结果回调,error = nil 表示操作成功
 *
 * @discussion 只有群主才有权限解散群。
 */
+ (void)dissolveGroupWithGid:(NSString *)gid handler:(JMSGCompletionHandler)handler;
```

#### 获取群组的展示名
	/*!
	 * @abstract 获取群组的展示名
	 *
	 * @discussion 如果 group.name 为空, 则此接口会拼接群组前 5 个成员的展示名返回.
	 */
	- (NSString *)displayName;

#### 群成员展示名

```
/*!
 * @abstract 获取群成员的展示名
 *
 * @param memberUid 群成员的 uid（即：[JMSGUser uid]）
 *
 * @discussion 展示优先级：群昵称 > 好友备注(user.noteName) > 用户昵称(user.nickname) > 用户名(user.username)
 */
- (NSString *)memberDisplayName:(UInt64)memberUid;
```

### 聊天室管理
***Since 3.4.0***

+ 主要特点：聊天室的消息没有推送通知和离线保存，也没有常驻成员的概念，只要进入聊天室即可接收消息，开始聊天，一旦退出聊天室，不再会接收到任何消息、通知和提醒。
+ 发送消息：聊天室消息的发送与单聊、群聊是一样的，通用的发送接口
+ 接收消息：聊天室消息的接收与单聊、群聊做了区分，聊天室消息的接收将通过 JMSGConversationDelegate 类里的 [onReceiveChatRoomConversation:messages:](#跳转-聊天室接收消息代理方法) 方法通知到上层
+ 进入聊天室会自动获取最近 50 条消息

#### 分页获取聊天室

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
#### 获取已加入的聊天室

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
#### 获取聊天室详情

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
#### 加入聊天室

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
#### 退出聊天室

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

#### 接收聊天室消息

+ 发送消息：发送消息的接口与单聊、群里一样
+ 接收消息：聊天室消息的接收的代理方法与单聊、群里的做了区分，定义了新的接口[接收聊天室消息](#跳转-聊天室接收消息代理方法)


### 消息已读回执
***Since 3.3.0***
#### 已读回执设置
消息发送方可以在发送消息时，针对单条消息设置是否需要接收方发送已读回执。默认行为为 NO。

通过设置 JMSGOptionalContent 类中的 needReadReceipt 属性来设置是否需要已读回执。

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

#### 获取未发送已读回执的人数

当一条需要接收方发送已读回执的消息成功发出之后，消息发送方可以查看这条消息当前尚未发送已读回执的人数.

	/*!
	 * @abstract 消息未读人数
	 *
	 * @discussion 只针对消息发送方有效
	 *
	 * 注意：只有发送方调用 [+sendMessage:optionalContent:] 方法设置 message 需要已读回执，此方法才有意义。
	 */
	- (NSInteger)getMessageUnreadCount;

#### 获取已读回执详情

发送方可以查看这条消息当前已读回执的详情,详情中包含当前已发送已读回执和未发送已读回执的用户 User 列表等信息

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

对于消息接收方，可以将一条消息标记为已读，标记成功后，这条消息的已读状态会记录在本地。 当这条消息是一条需要已读回执的消息时，SDK 还将主动发送一个通知事件 [JMSGMessageReceiptStatusChangeEvent:](./jmessage_ios_appledoc_html/Classes/JMSGMessageReceiptStatusChangeEvent.html) 给消息发送方，通知对方这条消息的已读回执人数发生变化。

***注意：***这个已读状态只会保存在本地，当本地数据被清除，或者用户更换设备登陆之后，已读状态会被重置为NO。

上层通过方法监听此事件.

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
#### 获取消息是否是已读状态

对于消息接收方，可以通过此接口获取到这条消息是否是已读的状态。 默认所有收到的消息已读状态都为NO。在成功调用  -(void)setMessageHaveRead: 接口后，消息的已读状态变成 YES.

注意:这个已读状态只会保存在本地，当本地数据被清除，或者用户更换设备登陆之后，已读状态会被重置为NO。

```
/*!
 * @abstract 是否已读(只针对接收的消息)
 *
 * @discussion 该属性与实例方法 [-(void)setMessageHaveRead:] 是对应的。
 *
 * 注意：只有发送方调用 [+sendMessage:optionalContent:] 方法设置 message 需要已读回执，此属性才有意义。
 */
@property(nonatomic, assign, readonly) BOOL isHaveRead;
```

#### 消息回执状态变更事件
对于消息发送方,发送的需要接收方发送已读回执的消息，接收方通过 setMessageHaveRead: 接口成功发送已读回执后，SDK 会上抛这个事件通知消息发送方。发送方通过监听这个事件可以知道是哪个会话中的哪条消息的未回执人数发生了变化。

发送方添加监听：

```
/*!
 * @abstract 消息回执状态变更事件
 *
 * @param receiptEvent 下发的通知事件，事件类型请查看 JMSGMessageReceiptStatusChangeEvent 类
 *
 * @discussion 上层可以通过 receiptEvent 获取相应信息
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageReceiptStatusChangeEvent:(JMSGMessageReceiptStatusChangeEvent *)receiptEvent;
```
##### 消息回执相关示例

```
//发送方
1、设置消息需要回执功能
JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:text];
JMSGOptionalContent *optionalCon = [[JMSGOptionalContent alloc] init];
optionalCon.needReadReceipt = YES;    
[conversation sendMessage:message optionalContent:optionalCon];

2、获取未回执人数
NSInteger count =  [self.message getMessageUnreadCount];
NSLog(@"消息未读人数:%ld",count);

3、获取消息回执详情
[self.message messageReadDetailHandler:^(NSArray * _Nullable readUsers, NSArray * _Nullable unreadUsers, NSError * _Nullable error) {
  NSLog(@"\n 已读列表：%@，\n 未读列表：%@",readUsers,unreadUsers);
 }];
 
 4、监听已读回执变更事件
 - (void)onReceiveMessageReceiptStatusChangeEvent:(JMSGMessageReceiptStatusChangeEvent *)receiptEvent{
    NSArray *messages =receiptEvent.messages;
    JMSGConversation *conversation = receiptEvent.conversation;
}
                
//接收方
1、设置消息已读
[self.message setMessageHaveRead:^(id resultObject, NSError *error) {
    NSLog(@"发送已读回执:%@",error?@"失败":@"成功");
 }];
 
2、查看消息已读状态
BOOL status = self.message.isHaveRead;
NSLog(@"消息是否已读:%@", status?@"是":@"否");
```

### 消息透传命令

消息透传发送的内容后台不会为其离线保存，只会在对方用户在线的前提下将内容推送给对方。SDK 收到命令之后也不会本地保存，不发送通知栏通知，整体快速响应。  
开发者可以通过消息透传拓展一些在线场景下的辅助功能，如：实现输入状态提示等。

#### 透传命令分类：

```
/*!
 * 发送消息透传的的类型
 */
typedef NS_ENUM(NSInteger,JMSGTransMessageType) {
  /// 单聊透传消息
  kJMSGTransMessageTypeSingle        = 1,
  /// 群里透传消息
  kJMSGTransMessageTypeGroup        = 2,
  /// 设备间透传消息
  kJMSGTransMessageTypeCrossDevice  = 3,
};
```
#### 设备间消息透传
支持同用户下不同设备之间消息透传

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

#### 会话间消息透传

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
 */
- (void)sendTransparentMessage:(NSString *JMSG_NONNULL)transparentText
             completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 监听透传消息

```
/*!
 * @abstract 消息透传事件
 *
 * @param transparentEvent 下发的通知事件，事件类型请查看 JMSGMessageTransparentEvent 类
 *
 * @discussion 上层可以通过 transparentEvent 获取相应信息，如自定义的透传信息、会话
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageTransparentEvent:(JMSGMessageTransparentEvent *)transparentEvent;
```

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
#### 发送@所有人的消息
```
/*!
 * @abstract 发送@所有人消息（已经创建好对象的）
 *
 * @param message 通过消息创建类接口，创建好的消息对象
 *
 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 JMSGMessageDelegate中的onReceiveMessage: error:方法来注册消息发送结果
 */
- (void)sendAtAllMessage:(JMSGMessage *)message;
```


### 通知栏管理
#### JMSGConversation
发送消息时，SDK 可以控制离线消息的存储、自定义通知栏内容等，具体的功能可以想象查看 [JMSGOptionalContent](./jmessage_ios_appledoc_html/Classes/JMSGOptionalContent.html#) 类里面的说明。

```
/*!
 * @abstract 发送消息（附带可选功能，如：控制离线消息存储、自定义通知栏内容等）
 *
 * @param message           通过消息创建类接口，创建好的消息对象
 * @param optionalContent   可选功能，具体请查看 JMSGOptionalContent 类
 *
 * @discussion 可选功能里可以设置离线消息存储、自定义通知栏内容等，具体请查看 JMSGOptionalContent 类。
 *
 */
- (void)sendMessage:(JMSGMessage *)message optionalContent:(JMSGOptionalContent *)optionalContent;
```

```
/*!
 * @abstract 发送消息（附带可选功能，如：控制离线消息存储、自定义通知栏内容等）
 *
 * @param message           通过消息创建类接口，创建好的消息对象
 * @param optionalContent   可选功能，具体请查看 JMSGOptionalContent 类
 *
 * @discussion 可选功能里可以设置离线消息存储、自定义通知栏内容等，具体请查看 JMSGOptionalContent 类。
 *
 */
+ (void)sendMessage:(JMSGMessage *)message optionalContent:(JMSGOptionalContent *)optionalContent;
```

###<span id="JMSGFriendManager">好友管理</span>

添加、删除、接受、拒绝好友等操作 SDK 会作为通知事件下发,上层通过 [onReceiveNotificationEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveFriendNotificationEvent:) 类中的方法监听此类事件. 

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
		 
		 /// 事件类型: 消息撤回
		 kJMSGEventNotificationMessageRetract = 55,
		 /// 事件类型: 消息透传
		 kJMSGEventNotificationMessageTransparent = 58,
		 /// 事件类型: 消息回执变更
		 kJMSGEventNotificationMessageReceiptStatusChange = 68,
	    
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
* 非消息事件，如：用户登录状态变更、好友相关事件等,SDK会作为通知事件下发,每一类事件都有对应的代理方法，上层通过对应方法监听事件.

#### 用户登录状态变更事件

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

##### 代理方法
[监听该事件的代理方法：onReceiveUserLoginStatusChangeEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGUserDelegate.html#//api/name/onReceiveUserLoginStatusChangeEvent:)
	
<span id="监听好友管理事件"></span>

#### 好友管理事件

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

##### 代理方法
[监听该事件的代理方法: onReceiveFriendNotificationEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveFriendNotificationEvent:)	

#### 消息撤回事件

	/*!
	 * @abstract 消息撤回事件
	 *
	 * @discussion 上层通过 JMSGEventDelegate 类中的 -(void)onReceiveNotificationEvent: 代理方法监听此事件,详见官方文档.
	 */
	@interface JMSGMessageRetractEvent : JMSGNotificationEvent
	
	/**
	 * @abstract 消息撤回所属会话
	 */
	@property(nonatomic, strong, readonly) JMSGConversation *conversation;
	
	/**
	 * @abstract 撤回之后的消息
	 */
	@property(nonatomic, strong, readonly) JMSGMessage *retractMessage;

##### 代理方法
[监听该事件的代理方法: onReceiveMessageRetractEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveMessageRetractEvent:)
	
#### 消息透传事件

	/*!
	 * @abstract 消息透传事件
	 */
	@interface JMSGMessageTransparentEvent : JMSGNotificationEvent
	/*!
	 * @abstract 消息所属会话
	 */
	@property(nonatomic, strong, readonly) JMSGConversation *conversation;
	/*!
	 * @abstract 用户自定义透传内容
	 */
	@property(nonatomic, strong, readonly) NSString *transparentText;
	@end
	
##### 代理方法
[监听该事件的代理方法: onReceiveMessageTransparentEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveMessageTransparentEvent:)
	
#### 消息回执变更事件	

	/*!
	 * @abstract 消息已读回执状态变更事件
	 */
	@interface JMSGMessageReceiptStatusChangeEvent : JMSGNotificationEvent
	/**
	 * @abstract 消息所属会话
	 */
	@property(nonatomic, strong, readonly) JMSGConversation *conversation;
	/**
	 * @abstract 已读回执变更的消息列表
	 */
	@property(nonatomic, strong, readonly) NSArray <__kindof JMSGMessage *>*messages;
	@end
	
##### 代理方法
[监听该事件的代理方法: onReceiveMessageReceiptStatusChangeEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGEventDelegate.html#//api/name/onReceiveMessageReceiptStatusChangeEvent:)

<span id="跳转-入群申请事件"></span>
#### 入群申请事件	

```
@interface JMSGApplyJoinGroupEvent : JMSGNotificationEvent
/// 事件的 id
@property(nonatomic, strong, readonly) NSString *eventID;
/// 群 gid
@property(nonatomic, strong, readonly) NSString *groupID;
/// 是否是用户主动申请入群，YES：主动申请加入，NO：被邀请加入
@property(nonatomic, assign, readonly) BOOL isInitiativeApply;
/// 发起申请的 user，如果 isInitiativeApply = YES，则与 sendApplyUser 和 joinGroupUser 是相同的
@property(nonatomic, strong, readonly) JMSGUser *sendApplyUser;
/// 被邀请入群的 user，如果 isInitiativeApply = YES，则与 sendApplyUser 和 joinGroupUser 是相同的
@property(nonatomic, strong, readonly) JMSGUser *joinGroupUser;
/// 原因
@property(nonatomic, strong, readonly) NSString *reason;
@end
```

##### 代理方法
[监听该事件的代理方法: onReceiveApplyJoinGroupApprovalEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGGroupDelegate.html#//api/name/onReceiveApplyJoinGroupApprovalEvent:)
	

<span id="跳转-管理员拒绝入群申请事件"></span>
#### 管理员拒绝入群申请事件	

```
@interface JMSGGroupAdminRejectApplicationEvent : JMSGNotificationEvent
/// 群 gid
@property(nonatomic, strong, readonly) NSString *groupID;
/// 拒绝原因
@property(nonatomic, strong, readonly) NSString *rejectReason;
/// 操作的管理员
@property(nonatomic, strong, readonly) JMSGUser *groupManager;
@end
```
	
##### 代理方法
[监听该事件的代理方法: onReceiveGroupAdminRejectApplicationEvent:](./jmessage_ios_appledoc_html/Protocols/JMSGGroupDelegate.html#//api/name/onReceiveGroupAdminRejectApplicationEvent:)

#### 群成员群昵称变更事件

```
/*!
 * @abstract 群成员昵称修改事件
 *
 * @discussion 如果是离线事件， memberInfoList 里会包含群成员每一次的修改记录
 */
@interface JMSGGroupNicknameChangeEvent : NSObject
/// 群组
@property(nonatomic, strong, readonly) JMSGGroup *group;
/// 修改昵称的群成员
@property(nonatomic, strong, readonly) JMSGGroupMemberInfo *fromMemberInfo;
/// 被修改昵称的群成员
@property(nonatomic, strong, readonly) JMSGGroupMemberInfo *toMemberInfo;
/// 事件时间
@property(nonatomic, assign, readonly) UInt64 ctime;
@end
```

##### 代理方法
[监听该事件的代理方法: onReceiveGroupNicknameChangeEvents:](./jmessage_ios_appledoc_html/Protocols/JMSGGroupDelegate.html#//api/name/onReceiveGroupNicknameChangeEvents:)
	
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
[监听该事件的代理方法: onReceiveMessage:error:](./jmessage_ios_appledoc_html/Protocols/JMSGMessageDelegate.html#//api/name/onReceiveMessage:error:)

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

#### 会话信息变更通知
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

#### 消息同步代理方法 
<span id="onSyncConversation:"></span>

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

<span id="跳转-聊天室接收消息代理方法"></span>
#### 聊天室接收消息代理方法

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
<span id="监听JMSGEventContent"></span>

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

```
/*!
 * @abstract 群组信息 (GroupInfo) 信息通知
 *
 * @param group 变更后的群组对象
 *
 * @discussion 如果想要获取通知, 需要先注册回调. 具体请参考 JMessageDelegate 里的说明.
 */
@optional
- (void)onGroupInfoChanged:(JMSGGroup *)group;
```

<span id="监听-JMSGApplyJoinGroupEvent"></span>

```
/*!
 * @abstract 监听申请入群通知
 *
 * @param event 申请入群事件
 *
 * @discussion 只有群主和管理员能收到此事件；申请入群事件相关参数请查看 JMSGApplyJoinGroupEvent 类，在群主审批此事件时需要传递事件的相关参数
 *
 * @since 3.4.0
 */
@optional
- (void)onReceiveApplyJoinGroupApprovalEvent:(JMSGApplyJoinGroupEvent *)event;
```

<span id="监听-JMSGGroupAdminRejectApplicationEvent"></span>

```
/*!
 * @abstract 监听管理员拒绝入群申请通知
 *
 * @param event 拒绝入群申请事件
 *
 * @discussion 只有申请方和被申请方会收到此事件；拒绝的相关描述和原因请查看 JMSGGroupAdminRejectApplicationEvent 类
 *
 * @since 3.4.0
 */
@optional
- (void)onReceiveGroupAdminRejectApplicationEvent:(JMSGGroupAdminRejectApplicationEvent *)event;
```

<span id="监听-JMSGGroupAdminApprovalEvent"></span>

```
/*!
 * @abstract 监听管理员审批通知
 *
 * @param event 管理员审批事件
 *
 * @discussion 只有管理员才会收到该事件；当管理员同意或拒绝了某个入群申请事件时，其他管理员就会收到该事件，相关属性请查看 JMSGGroupAdminApprovalEvent 类
 *
 * @since 3.5.0
 */
@optional
- (void)onReceiveGroupAdminApprovalEvent:(JMSGGroupAdminApprovalEvent *)event;
```

<span id="监听-JMSGGroupNicknameChangeEvent"></span>

```
/*!
 * @abstract 群成员群昵称变更通知
 *
 * @param events 群成员昵称变更事件列表
 *
 * @discussion 如果是离线事件，SDK 会将所有的修改记录加入数组上抛。事件具体相关属性请查看 JMSGGroupNicknameChangeEvent 类
 *
 * @since 3.7.0
 */
@optional
- (void)onReceiveGroupNicknameChangeEvents:(NSArray<__kindof JMSGGroupNicknameChangeEvent*>*)events;
```


<span id="监听-JMSGUserLoginStatusChangeEvent"></span>

#### JMSGUserDelegate
	/*!
	 * @abstract 监听当前用户登录状态变更事件
	 *
	 * @discussion 可监听：当前登录用户被踢、非客户端修改密码强制登出、登录状态异常、被删除、被禁用、信息变更等事件
	 *
	 * @since 3.5.0
	 */
	@optional
	- (void)onReceiveUserLoginStatusChangeEvent:(JMSGUserLoginStatusChangeEvent *)event;

<span id="监听-JMSGFriendNotificationEvent"></span>

#### JMSGEventDelegate

```
/*!
 * @abstract 监听好友相关事件
 *
 * @discussion 可监听：加好友、删除好友、好友更新等事件
 *
 * @since 3.5.0
 */
@optional
- (void)onReceiveFriendNotificationEvent:(JMSGFriendNotificationEvent *)event;
```

<span id="监听-JMSGMessageRetractEvent"></span>

```
/*!
 * @abstract 监听消息撤回事件
 *
 * @param retractEvent 下发的通知事件，事件类型请查看 JMSGMessageRetractEvent 类
 *
 * @since 3.2.0
 */
@optional
- (void)onReceiveMessageRetractEvent:(JMSGMessageRetractEvent *)retractEvent;
```
<span id="监听-JMSGMessageReceiptStatusChangeEvent"></span>

```
/*!
 * @abstract 监听消息回执状态变更事件
 *
 * @param receiptEvent 下发的通知事件，事件类型请查看 JMSGMessageReceiptStatusChangeEvent 类
 *
 * @discussion 上层可以通过 receiptEvent 获取相应信息
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageReceiptStatusChangeEvent:(JMSGMessageReceiptStatusChangeEvent *)receiptEvent;
```
<span id="监听-JMSGMessageTransparentEvent"></span>

```
/*!
 * @abstract 监听消息透传事件
 *
 * @param transparentEvent 下发的通知事件，事件类型请查看 JMSGMessageTransparentEvent 类
 *
 * @discussion 消息透传的类型：单聊、群聊、设备间透传消息
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageTransparentEvent:(JMSGMessageTransparentEvent *)transparentEvent;
```



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

