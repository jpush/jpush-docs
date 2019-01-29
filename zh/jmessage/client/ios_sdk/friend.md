<h1>好友管理</h1>


## 概述

JMessage iOS SDK 从 2.4.0 版本开始提供接口实现对用户好友关系的托管，以及相关好友请求的发送和接收。  

好友模块仅实现对用户好友关系的托管，以及相关好友请求的发送和接收。除此之外的任何建立在好友关系之上的功能（如：仅限于好友之间才能进行的聊天等），需要开发者的应用层自己实现。JMessage 本身是无好友通信模式。


### 发送好友添加请求
```
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
```

### 接受好友请求
```
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
+ (void)acceptInvitationWithUsername:(NSString *)username
                              appKey:(NSString *)userAppKey
                   completionHandler:(JMSGCompletionHandler)handler;
```

### 拒绝好友请求
```
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
```

### 获取好友列表
```
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
```


### 删除好友
```
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
```

### 更新好友备注名/备注信息
设置好友备注名和备注信息的接口在 [JMSGUser - 好友备注](./jmessage_ios_appledoc_html/Classes/JMSGUser.html#//api/name/updateNoteName:completionHandler:) 类中。

#### 好友备注名
##### 获取
```
/*!
 * @abstract 备注名
 */
@property(nonatomic, copy, readonly) NSString * JMSG_NULLABLE noteName;
```
##### 设置
```
/*!
 * @abstract 修改好友备注名
 *
 * @param noteName 备注名
 *
 * @discussion 注意：这是建立在是好友关系的前提下，修改好友的备注名
 */
- (void)updateNoteName:(NSString *)noteName completionHandler:(JMSGCompletionHandler)handler;
```

#### 好友备注信息
##### 获取
```
/*!
 * @abstract 备注信息
 */
@property(nonatomic, copy, readonly) NSString * JMSG_NULLABLE noteText;
```
##### 设置
```
/*!
 * @abstract 修改好友备注信息
 *
 * @param noteText 备注信息
 *
 * @discussion 注意：这是建立在是好友关系的前提下，修改好友的备注信息
 */
- (void)updateNoteText:(NSString *)noteText completionHandler:(JMSGCompletionHandler)handler;
```

### 好友相关通知事件
好友相关的事件具体请查看 [事件与代理 - 好友事件](./event#friend-event)

**注意：**好友相关事件 SDK 并没有做本地化存储，上层想要做记录这些事件，则需要上层自己实现存储。