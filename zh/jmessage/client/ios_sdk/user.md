<h1>用户信息管理</h1>


## 概述

+ 开发者应用的用户，通过username / password 注册到 JMessage后，SDK 侧可以发起注册，服务器端也可发起批量注册。+ 用户登录 App，也同时登录 JMessage。登录后可以向其他 username 发聊天消息，也可以收到来自其他 username 或者群组的消息。+ 用户 A 是否有权限向用户 B 发消息，需由开发者的App 自己控制。+ 开发者可选择将用户头像等用户信息同步更新到 JMessage。



### 获取当前登录账号的用户信息
此接口会直接从本地返回当前已经登录的用户的信息

```
/*!
 * @abstract 获取用户本身个人信息接口
 *
 * @return 当前登陆账号个人信息
 *
 * @discussion 注意：返回值有可能为空
 */
+ (JMSGUser *)myInfo;
```

### 获取用户信息
#### 批量获取用户信息
异步从后台获取用户信息，此接口可用来获取不同appkey下用户的信息,如果appKey为空，则默认获取当前appkey下的用户信息

```
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
```

#### 获取本地用户信息
可以通过 `uid` 快速获取本地用户信息。
	
	+(JMSGUser *JMSG_NULLABLE)userWithUid:(SInt64)uid;
	
#### 获取当前用户信息
获取当前登录用户的信息，可以用户上层判断本地是否登录，可能返回为空。

```
/*!
 * @abstract 获取用户本身个人信息接口
 *
 * @return 当前登陆账号个人信息
 *
 * @discussion 注意：返回值有可能为空
 */
+ (JMSGUser *)myInfo;
```

### 更新用户信息
用户的昵称、性别、生日、签名等，可通过此接口更新

```
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
```

### 更新用户密码

```
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
```

### 用户头像管理
#### <span id="update-avatar">更新用户头像</span>
头像更新，也可以使用此接口更新

```
/*!
 * @abstract 更新头像（支持传图片格式）
 *
 * @param avatarData      头像数据
 * @param avatarFormat    头像格式，可以为空，不包括"."
 * @param handler         回调
 *
 * @discussion 头像格式参数直接填格式名称，不要带点。正确：@"png"，错误：@".png"
 */
+ (void)updateMyAvatarWithData:(NSData *)avatarData
                  avatarFormat:(NSString *)avatarFormat
             completionHandler:(JMSGCompletionHandler)handler;
```


#### 获取头像
```
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
```
#### 上传头像
与更新头像相同 [更新头像](#update-avatar)

#### 获取头像本地路径
```
/*!
 * @abstract 获取头像缩略文件的本地路径
 *
 * @return 返回本地路，返回值只有在下载完成之后才有意义
 */
- (NSString *JMSG_NULLABLE)thumbAvatarLocalPath;
```

### 黑名单管理
#### 添加黑名单
```
/*!
 * @abstract 添加黑名单
 * @param usernameArray 作用对象的username数组
 * @param handler 结果回调。回调参数： error 为 nil, 表示设置成功
 *
 * @discussion 可以一次添加多个用户
 */
+ (void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
          completionHandler:(JMSGCompletionHandler)handler;
```
#### 删除删除
```
/*!
 * @abstract 删除黑名单
 * @param usernameArray 作用对象的username数组
 * @param handler 结果回调。回调参数：error 为 nil, 表示设置成功
 *
 * @discussion 可以一次删除多个黑名单用户
 */
+ (void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
            completionHandler:(JMSGCompletionHandler)handler;
```
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
 * 建议开发者在 SDK 完全启动之后，再调用此接口获取数据
 */
+ (void)blackList:(JMSGCompletionHandler)handler;
```

### 免打扰设置
可以将用户/群组添加到“免打扰”列表中，收到免打扰用户/群组发过来的消息时，将不会有通知栏通知，但消息事件照常下发。 设置全局免打扰之后，收到所有消息都将不会有通知栏通知，效果类似。

#### 用户设置免打扰

```
/*!
 * @abstract 设置用户免打扰（支持跨应用设置）
 *
 * @param isNoDisturb 是否全局免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数： error 为 nil, 表示设置成功
 *
 * @discussion 针对单个用户设置免打扰，这个接口支持跨应用设置免打扰
 */
- (void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;
```

#### 获取免打扰列表

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
 * 建议开发者在 SDK 完全启动之后，再调用此接口获取数据
 */
+ (void)noDisturbList:(JMSGCompletionHandler)handler;
```

#### 设置全局免打扰
设置全局免打扰后，APP 将不会收到任何通知

```
/*!
 * @abstract 设置是否全局免打扰
 *
 * @param isNoDisturb 是否全局免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数：error 不为 nil,表示设置失败
 *
 * @discussion 此函数为设置全局的消息免打扰，建议开发者在 SDK 完全启动之后，再调用此接口获取数据
 */
+ (void)setIsGlobalNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;
```