<h1>跨应用通信</h1>


## 概述
跨应用通信是指允许同一开发者账号下的不同应用能互相通信，以满足开发者对于不同 appKey 下应用通信的需求。

跨应用接口与非跨应用接口区别主要在于：跨应用接口增加了[appkey](../../guideline/faq/#getappkey)作为参数。只要接口中需要传[appkey](../../guideline/faq/#getappkey)作为参数的，均可以支持跨应用通信，详细接口说明请前往极光IM [iOS API docs](./ios_doc)。这里仅列举一些常用的跨应用接口和实现。

### 跨应用用户管理
#### 获取用户信息
通过指定appKey可以实现获取跨应用用户信息。

```
/*!
 * @abstract 批量获取用户信息
 *
 * @param usernameArray 用户名列表。NSArray 里的数据类型为 NSString
 * @param userAppKey 用户所在 AppKey
 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里的数据类型为 JMSGUser
 *
 * @discussion 这是一个批量接口。
 */
+ (void)userInfoArrayWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                                appKey:( NSString *JMSG_NULLABLE)userAppKey
                     completionHandler:(JMSGCompletionHandler)handler;
```
#### 免打扰设置
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

#### 黑名单设置
##### 添加
```
/*!
 * @abstract 跨应用添加黑名单
 * @param usernameArray 作用对象的username数组
 * @param userAppKey 应用的appKey
 * @param handler 结果回调。回调参数：error 为 nil, 表示设置成功
 *
 * @discussion 可以一次添加多个用户
 */
+ (void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                     appKey:(NSString *)userAppKey
          completionHandler:(JMSGCompletionHandler)handler;
```
##### 删除
```
/*!
 * @abstract 跨应用删除黑名单
 * @param usernameArray 作用对象的username数组
 * @param userAppKey 应用的appKey
 * @param handler 结果回调。回调参数：error 为 nil, 表示设置成功
 *
 * @discussion 可以一次删除多个黑名单用户
 */
+ (void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *)*)usernameArray
                       appKey:(NSString *)userAppKey
            completionHandler:(JMSGCompletionHandler)handler;
```

### 跨应用群组管理
实现跨应用群聊的关键在于群组中加入跨应用的群成员，而创建会话和发送消息的流程和普通的群聊实现方式一致。这里只列举部分常用的跨应用接口

#### 群成员管理
##### 添加

```
/*!
 * @abstract 添加群组成员
 *
 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
 * @param userAppKey    用户的 AppKey，这批添加的成员必须在同一个 AppKey 下的用户
 * @param reason        邀请原因，可选
 *
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                             appKey:(NSString *JMSG_NULLABLE)userAppKey
                             reason:(NSString *JMSG_NULLABLE)reason
                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

##### 删除

```
/*!
 * @abstract 删除群组跨应用成员
 *
 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                                appKey:(NSString *)userAppKey
                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 管理员管理
##### 添加

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
- (void)addGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                            appKey:(NSString *JMSG_NULLABLE)appkey
                 completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

##### 删除

```
/*!
 * @abstract 删除管理员
 *
 * @param username 用户名
 * @param appkey   用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 */
- (void)deleteGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                               appKey:(NSString *JMSG_NULLABLE)appkey
                    completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 黑名单管理
##### 添加

```
/*!
 * @abstract 添加群黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 黑名单上限100个，超出将无法设置成功，被拉入黑名单用户会被主动踢出群组，且无法再次加入.
 * @since 3.8.0
 */
- (void)addGroupBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                                appKey:(NSString *JMSG_NULLABLE)appKey
                               handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

##### 删除

```
/*!
 * @abstract 删除群黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @since 3.8.0
 */
- (void)deleteGroupBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                                   appKey:(NSString *JMSG_NULLABLE)appKey
                                  handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 跨应用消息管理

##### 发送跨应用单聊文本消息

```
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
```

##### 发送跨应用单聊图片消息

```
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
```

##### 发送跨应用单聊语音消息

```
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

##### 发送跨应用单聊文件消息

```
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
```

##### 发送跨应用单聊位置消息

```
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
```

### 跨应用会话管理
创建会话时指定对方用户所属 appKey，即可建立起一个和跨应用用户的会话。
##### 获取跨应用单聊会话

```
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
```

##### 创建跨应用单聊会话

```
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
```
 
##### 删除跨应用单聊会话
 
```
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
```

