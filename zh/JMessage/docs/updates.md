# 最近更新
### JMessage Android SDK v1.4.1
#### 更新时间
+ 2016-09-14

#### JMessage SDK Change Log

##### Bug Fix

+ 修复某些型号的手机应用启动时会弹出位置权限授权框的问题

#### 升级指南

+ jar包更新至jmessage-sdk-1.4.1.jar更新时需删除老版本jar包
+ 将so库更新至 libjpush220.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置


### JMessage iOS SDK v2.1.7

#### 更新时间
+ 2016-09-09

#### Change Log
##### Bug Fix
+ 修复：在32位系统下，message的时间戳不正确的问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### JMessage Android SDK v1.4.0
#### 更新时间
+ 2016-09-09

#### JMessage SDK Change Log

##### Bug Fix

+ 修复跨应用添加用户进黑名单时可添加自己进黑名单
+ 修复跨应用免打扰中自己可以给自己设置免打扰
+ 修复上层应用进程崩溃重启后，导致im请求发送超时。
+ 修复点击通知栏时，有一定几率message对象为空
+ 修复特殊用户名下，相关内部逻辑错误
+ 修复本地会话过多时，数据库访问的问题。

##### New Feature

+ 新增好友模块
+ 新增用户备注名和备注信息设置
+ 新增文件信息发送接口
+ 新增位置信息发送接口
+ GroupInfo中增加获取群主用户所属应用appkey的实例接口
+ getConversationList默认按时间降序排序。
+ 优化接口执行效率

##### 新增接口

+ ContactManager 好友管理接口入口类。
	+ 具体定义见api doc: [ContactManager](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/ContactManager.html)
+ UserInfo类中新增实例接口：
	+ 设置备注名：[updateNotename](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#updateNoteName(java.lang.String,%20cn.jpush.im.api.BasicCallback))
	+ 设置备注信息：[updateNoteText](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#updateNoteText(java.lang.String,%20cn.jpush.im.api.BasicCallback))
	+ 将用户从好友列表中移除：[removeFromFriendList](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/UserInfo.html#removeFromFriendList(cn.jpush.im.api.BasicCallback))
   
+ ContactNotifyEvent 好友相关通知事件类
	+ 具体定义见api doc: [ContactNotifyEvent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/event/ContactNotifyEvent.html)
   
+ 增加两种message content类型：
	+ 文件消息：[FileContent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/content/FileContent.html)
	+ 位置消息：[LocationContent](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/content/LocationContent.html)

+ GroupInfo类中新增实例接口：[getOwnerAppkey](http://docs.jiguang.cn/jmessage/client/im_android_api_docs/cn/jpush/im/android/api/model/GroupInfo.html#getOwnerAppkey())

##### 注意
从此版本开始，JChat源码将不再作为sdk zip的一部分随sdk发布，取而代之的是一个界面简化的仅仅用来展示接口用法的JMessage Demo。

之前JChat的源码见[GitHub](https://github.com/jpush/jchat-android)


#### 升级指南

+ jar包更新至jmessage-sdk-1.4.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush219.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### JMessage iOS SDK v2.1.6

#### 更新时间
+ 2016-09-01

#### Change Log
##### Bug Fix
+ 修复：网络或者后台出现问题导致的下发重复消息问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### JMessage JS SDK v1.1.2

#### 更新时间
+ 2016-08-31

#### Change Log
+ 添加类型转换，iOS端接收消息问题

#### 升级提示
+ 建议升级！


### JMessage JS SDK v1.1.1

#### 更新时间
+ 2016-08-30

#### Change Log
+ 修复发送群组消息问题

#### 升级提示
+ 建议升级！

### JMessage JS SDK v1.1.0

#### 更新时间
+ 2016-08-26

#### Change Log
##### New Feature
+ 增加免打扰功能
+ 支持图片，音频消息的接收功能

#### 升级提示
+ 建议升级！

### JMessage JS SDK v1.0.1

#### 更新时间
+ 2016-08-19

#### Change Log
##### New Feature
+ 增加获取用户信息的跨应用接口
+ 增加发送单聊消息的跨应用接口

#### 升级提示
+ 可选升级！


### JMessage IOS SDK v2.1.5
#### 更新时间
+ 2016-08-13

#### JMessage SDK Change Log

##### BugFix:
+ 修复本地时间和服务器时间不一致时，消息顺序错乱的问题

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### JMessage Android SDK v1.3.1
#### 更新时间
+ 2016-08-13

#### JMessage SDK Change Log

##### Bug Fix

+ 修复：本地时间与后台时间不一致导致的消息顺序错乱


#### JChat Change Log
+ 适配JMessage SDK 1.3.1


#### 升级指南

+ jar包更新至jmessage-sdk-1.3.1.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush216.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### JMessage IOS SDK v2.1.3

#### 更新时间
+ 2016-07-15

#### JMessage SDK Change Log

##### New Feature
+ 新增：本应用和跨应用的免打扰功能；
+ 新增：跨应用群聊功能；
+ 新增：本应用和跨应用的黑名单功能；
+ 新增：暴露event msg作用对象的username(s),用户开发者定制event msg；
+ 新增：JMGGroup 增加一个属性 max_member_count，表示当前群成员最大人数；
+ 新增：JMGGroup 增加一个属性 ownerAppKey，表示当前群群主的appKey。
+ 新增接口：
	+ JMessage
		+ +(void)noDisturbList:(JMSGCompletionHandler)handler;//用户免打扰列表
		设置全局免打扰标识。
        + +(BOOL)isSetGlobalNoDisturb;//获取全局免打扰状态
        + +(void)setIsGlobalNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置是否全局免打扰
        + +(void)balckList:(JMSGCompletionHandler)handler;//获取黑名单列表
    + JMSGUser
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//获取免打扰状态
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置用户免打扰（支持跨应用设置）
        + @property(nonatomic, assign, readonly) BOOL isInBlacklist;//获取黑名单状态
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray completionHandler:(JMSGCompletionHandler)handler;//添加黑名单
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray completionHandler:(JMSGCompletionHandler)handler;//删除黑名单
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//跨应用添加黑名单
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//跨应用删除黑名单
    + JMSGGroup
        + @property(nonatomic, copy, readonly) NSString *ownerAppKey;//群主的appKey
        + @property(nonatomic, strong, readonly) NSString     *maxMemberCount;//获取群组人数上限
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//获取免打扰状态
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//设置群组消息免打扰（支持跨应用设置）
    + JMSGEventContent
        + -(NSString *JMSG_NULLABLE)getEventFromUsername;//获取事件发起者的用户名
        + -(NSArray *JMSG_NULLABLE)getEventToUsernameList;//获取事件作用对象用户名列表
    + JMSGMessage
        + +(void)sendSingleTextMessage:(NSString *)text toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊文本消息
        + (void)sendSingleImageMessage:(NSData *)imageData toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊图片消息
        + (void)sendSingleVoiceMessage:(NSData *)voiceData voiceDuration:(NSNumber *)duration toUser:(NSString *)username appKey:(NSString *)userAppKey; //发送跨应用单聊语音消息
    + 跨应用群聊
        + -(void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//添加群组跨应用成员
        + -(void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//删除群组跨应用成员

##### Bug Fix

+ 修复：群event msg 事件不能定制问题；

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件！

### JMessage JS SDK v1.0.0

#### 更新时间
+ 2016-07-13

#### Change Log
+ JMessage JS SDK 首次发布
+ 聊天支持：单聊，群聊
+ 聊天内容：文本
+ 提供用户管理 ，群组管理，会话列表获取功能

#### 升级提示
+ 可选升级！


### JMessage Android SDK v1.3.0

#### 更新时间
+ 2016-07-12

#### JMessage SDK Change Log

##### New Feature
+ 增加群组、黑名单、免打扰功能的跨应用能力
+ 新增全局免打扰接口
+ 新增接口：
	+ JMessageClient
		+ setNoDisturbGlobal
		设置全局免打扰标识。
		+ getNoDisturbGlobal
		获取全局免打扰标识
		+ addGroupMembers
		添加群成员（跨应用)
		+ removeGroupMembers
		移出群成员（跨应用）
		+ addUsersToBlacklist
		将用户加入黑名单（跨应用）
		+ delUsersFromBlacklist 
		将用户移出黑名单（跨应用）
	+ GroupInfo
		+ getGroupMemberInfo
		获取群成员信息（跨应用）


##### Bug Fix

+ 修复：小概率出现的无法收到消息的问题
+ 修复：偶现的native层崩溃


#### JChat Change Log
+ 适配JMessage SDK 1.3.0

##### New Feature

+ 适配：群聊、黑名单、免打扰的跨应用功能
+ 新增：全局免打扰功能


#### 升级指南

+ jar包更新至jmessage-sdk-1.3.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush216.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 demo 来更新 AndroidManifest.xml 文件配置。


### JMessage iOS SDK v2.1.1

#### 更新时间
* 2016-06-15

#### 版本号
* JMessage SDK 2.1.1
* JChat 1.1.0b1893

#### Change Log

+ 新增：对IPv6网络的支持。

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件




### JMessage Android SDK v1.2.5

#### 更新时间
+ 2016-06-12

#### JMessage SDK Change Log

##### New Feature
+ Conversation对象新增设置本地未读消息数的接口
+ 新增接口：
	+ conversation.setUnReadMessageCnt
	
##### Bug Fix

+ 修复：群成员退群时，其他成员处显示的提示文字不正确
+ 修复：群主退群后，本地群主信息没有更新。
+ 修复：用户首次收到消息，打印收到的message 中targetName为空
+ 修复：概率出发送群聊消息，应用崩溃
+ 修复：登录一个帐号A，快速再登录帐号B概率出现数据库操作异常
+ 修复：dev api移除群聊免打扰后，sdk没有更新状态
+ 修复：SDK接收到group event后messageid字段值为0
+ 优化：有大量群成员的群组中，数据的处理效率


#### JChat Change Log
+ 适配 JMessage SDK 1.2.5
								
##### Bug Fix

+ 修复：1.2.9下拉刷新bug
+ 修复：1.2.9收到消息后可能出现会话丢失的bug
+ 优化：收到大量离线消息后UI卡顿现象

#### 升级指南

+ jar包更新至jmessage-sdk-1.2.5.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush211.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。


### JMessage iOS SDK v2.1.0

#### 更新时间
* 2016-05-10

#### 版本号
* JMessage SDK 2.1.0
* JChat 1.1.0b1870

#### Change Log
+ 实现跨应用单聊
+ 支持VIP用户群组上限突破200

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件
### JMessage Android SDK v1.2.3

#### 更新时间
+ 2016-04-07

#### JMessage SDK Change Log

##### Bug Fix

+ 修复：从旧版本升级到1.2.1导致的崩溃问题


#### JChat Change Log
+ 更新JMessage jar到1.2.3
								


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.3.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush213.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
### JMessage Android SDK v1.2.1

#### 更新时间
+ 2016-03-31

#### JMessage SDK Change Log

##### New Feature
+ 新增免打扰功能
+ 支持VIP用户群组上限突破200
	+ groupInfo中新增max_member_count属性，表示当前群成员最大人数。
+ 对外接口中需要传List作为参数的，对List size做限制。
+ 新增接口：
	+ JMessageClient
		+ JMessageClient.getNoDisturbList(GetNoDisturbListCallback callback) 获取用户的免打扰名单
	+ UserInfo
		+ userinfo.setNoDisturb(int noDisturb,Callback callback) 设置用户的免打扰状态
		+ userinfo.getNoDisturb() 获取用户的免打扰状态
		
	+ GroupInfo：
		+ groupinfo.setNoDisturb（int noDisturb,Callback callback）设置群组的免打扰状态
		+ groupinfo.getNoDisturb() 获取群组的免打扰状态
		+ groupinfo.getMaxMemberCount() 获取群成员的最大上限
 


##### Bug Fix

+ 修复：api 调用GetGroupInfo 获取一个已经被销毁的群组，返回码为0
+ 修复：消息正在发送的过程中，调用Login有可能导致数据库报错


#### JChat Change Log
+ 适配JMessage SDK 1.2.1
								
##### New Feature

+ 新增免打扰功能.

##### Bug Fix

+ 修复compileSdkVersion 改到23（android 6.0）后，工程报错。
+ 修复添加群组成员，界面无变化
+ 群成员搜索优化


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.1.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush211.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。

### JMessage iOS SDK v2.0.1

#### 更新时间
* 2016-03-22

#### 版本号
* JMessage SDK 2.0.1
* JChat 1.1.0b1611

#### Change Log
+ 修复：由于切换设备变更群成员， 群组信息不同步引起的消息发送失败。

#### 升级提示

+ 建议升级！
+ 由于 API 与 Model 层面很大范围的变更，建议参考 JChat 项目来适配新的 JMessage iOS SDK。

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件


### JMessage Android SDK v1.2.0

#### 更新时间

+ 2016-03-07

#### JMessage SDK Change Log

##### New Feature
+ 实现跨应用聊天
+ message中新增getServerMessageId接口
+ 新增setDebugMode接口
+ 新增服务器修改用户密码的event处理
+ 新增接口
	+ Conversation
		+ conversation.getTargetAppkey 获取会话对象的appkey（仅单聊）
		+ Conversation.createSingleConversation(username,appkey) 创建指定appkey的跨应用会话。
		+ JMessageClient.getSingleConversation(username,appkey) 获取与指定appkey下user的会话。
		+ JMessageClient.enterSingleConversation(username,appkey) 进入与指定appkey下user的会话。
		+ JMessageClient.deleteSingleConversation(username,appkey) 删除与指定appkey下user的会话
	+ Message
		+ message.getTargetAppKey 获取消息对象的appkey.（仅单聊消息）
		+ message.getFromAppKey 获取消息发送这个的appkey。
		+ message.getServerMessageId 获取消息对应服务端的messageId。
	+ UserInfo
		+ userinfo.getAppKey 获取用户所属的appkey。
		+ JMessageClient.getUserInfo(username,appkey,callback) 获取指定appkey下的用户信息。
	+ JMessageClient
		+ setDebugMode 打开JMessage的debug模式，作用等同于JPush的setDebugMode.

	+ 已过时接口
		+ JMessageClient.enterSingleConversaion 接口名拼写错误，使用JMessageClient.enterSingleConversation替代。
		+ JMessageClient.exitConversaion 接口名拼写错误, 使用JMessageClient.exitConversation替代。
		+ UserDeletedEvent 、 UserLogoutEvent 统一使用LoginStateChangeEvent替代。


##### Bug Fix

+ 修复通过getGroupList拿到gid之后，直接拿groupMembers返回空的问题
+ 修复删除会话时未删除通知栏消息
+ 修复conversation 接口名拼写错误
+ 修复首次收到消息创建会话的title错误。
+ 修复createConversation接口没有做登陆验证。
+ 修复跨应用某种情况下会出现循环获取userinfo的bug
+ 修复多次调用login而不调logout导致上一个登陆用户的缓存信息未清掉

#### JChat Change Log
+ 适配JMessage SDK 1.2.0
								
##### New Feature

+ 会话列表提供断网提示
+ 草稿可以在会话列表显示

##### Bug Fix

+ 修复：某些机型拍照上传图片失败bug
+ 修复：App启动时抛出WindowWarning的bug
+ 修复：对话框裁剪成圆角后有黑色阴影的bug
+ 修复：删除本地跨应用会话，对应通知栏消息未清掉
+ 修复：群聊天详情里，点击删除成员，进入到聊天成员中，群成员不显示用户名
+ 修复：群聊天详情界面中，点击全部群成员界面添加不存在的用户，界面停留在转圈的状态
+ 修复：用户主动退出群，退出群时会被系统桌面覆盖


#### 升级指南

+ jar包更新至jmessage-sdk-1.2.0.jar更新时需删除老版本jar包。
+ 将so库更新至 libjpush207.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
+ 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
+ 如果是从更早起的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。

### JMessage iOS SDK v2.0.0

#### 更新时间
* 2016-02-22

#### 版本号
* JMessage SDK 2.0.0
* JChat 1.1.0b1460

#### Change Log
+ 消息结构调整：现在一条消息由一个 JMSGMessage 类加上多个类型的 Content 组成，如 JMSGTextContent;
+ 对象化：会话里有 target 对象（JMSGUser 或者 JMSGGroup），消息里有 target JMSGUser 对象，fromUser 对象；
+ 通知调整：由之前的 NSNotification 换成 Delegate 的方式，使用更简单、直观；
+ 性能优化：对常用的信息，SDK内部做了缓存，以减少文件、网络访问；
+ 对外 API 头文件加了完善的文档注释，包含使用建议。

#### 升级提示

+ 建议升级！
+ 由于 API 与 Model 层面很大范围的变更，建议参考 JChat 项目来适配新的 JMessage iOS SDK。

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

### JMessage Android SDK v1.1.5

#### 更新时间

* 2015-12-11

#### JMessage SDK Change Log

##### New Feature

* 群成员变化event全部上抛sdk不过滤
* 用户小头像sdk内部作缓存
* 内部并发线程数控制，防止太多线程并发执行导致问题
* 优化网络任务执行效率
* 本地媒体文件存储按会话分类，方便之后清理。
* 新增接口:
	* ImageContent 新增通过传Bitmap来构造实例的接口
	* Conversation.CreateMessage 新增自定义FromName的接口，开发者可以自定义message的FromName
	* UserInfo 新增获取头像bitmap的异步接口getAvatarBitmap、getBigAvatarBitmap，并且sdk会在内部会对小头像的bitmap做缓存。
* 已过时接口:
	* EventNotificationContent.containsGroupOwner
	* UserInfo.getAvatarFileAsync


##### Bug Fix


* 使用自定义类继承BasicCallback时，请求会报错
* 一些对外接口没有做登陆检查,未登录时调用接口会有问题
* 修复发送大语音文件，对方收到后下载失败的bug
* 修复首次收到群消息展示的群组的ID
* 修复同时调用拿大头像和小头像时，其中有一个返回Null。

#### JChat Change Log
* 适配JMessage1.1.5

#### New Feature


* 发送多张图片时，逐张发送
* 相册按照修改时间进行排序
* 上传头像时进行裁剪
* 优化：一次发送9张图片，能发送成功，但效率比较低
* 优化：点击jchat 用户在【我】处查看自己头像，提示正在加载，体验待优化


##### Bug Fix


* 修复：加载上一页消息时如果不存在上一页消息，会多次刷新的问题
* 修复：单聊清空聊天记录异常的问题
* 修复：发送多张图片有时出现NPE异常
* 修复：发送9张图片，可能会卡在正在发送的提示界面，图片实际没有发送成功
* 修复：小米4手机更新头像，从文件管理处选择图片无法更新头像


#### 升级提示

+ 建议升级！

#### 升级指南
* 将jar包更新至 jmessage-sdk-1.1.5.jar更新时需删除老版本jar包。
* 将so库更新至 libjpush205.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
* 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
* 如果是从更早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。
### JMessage Android SDK v1.1.4
#### 更新时间

* 2015-09-28

#### JMessage SDK Change Log

##### New Feature

* 新增黑名单功能
* 新增用户被删除事件
* 收到群聊消息时，通知栏的tickerText显示消息发送者的displayName而不是群名
* 新增接口：createGroupConversation(long)、createSingleConversation(String)、getTargetInfo()、getLatestMessage()
* 过时接口：createConversation(ConversationType,long)、createConversation(ConversationType,String)、getTargetID()、getLatestMsgDate()
getLatestType()、getLatestText()
* 新增接口：getTargetInfo()、getFromUser()
* 已过时接口：getTargetID()、getTargetName()、getFromID()、getFromName()、getFromType()
* 新增接口：ImageContent类中新增createImageContentAsync异步创建ImageContent的接口

##### Bug Fix

* 修复dev api 添加删除群用户，群的聊天详情UI没有更新
* 修复customContent.setContentType方法文档没有说明其作用
* 修复昵称设置仅仅是表情会出现异常，返回服务端错误
* 修复调用stopPush后IM无法登录。
* 修复JMessage配置文件包名和appkey不匹配的，Demo APP依然能注册成功。
* 修复createSendMessage接口在用户未登录时调用直接崩溃。
* 修复用户发媒体信息时被踢下线，之前发送的消息状态一直处于"sending"
* 修复dev api添加/删除群用户时，相应事件未抛给上层
* 修复收到富媒体推送时，点击通知栏没有跳转的问题

#### JChat Change Log

#### New Feature

* 聊天消息支持分页加载
* 增加"关于"页面
* 优化聊天、聊天详情界面加载的性能
* 被拉黑时，使用自定义消息"消息已发出，但被对方拒收了"提示用户

##### Bug Fix

* 修复发送图片成功，但UI界面显示100%
* 修复群主点击进入群【聊天详情】，减号有时候加载5/6s才显示
* 修复如果一个会话窗口的消息过多，点击会话出现加载无响应的情况
* 修复软键盘弹出后，点击软键盘上的收起按钮，界面不会收回的bug
* 修复在被踢下线后，点击确定按钮抛出WindowLeak异常的bug
* 修复在启动APP后可能出现的异常：RuntimeException：Performing stop activity that is not resume
* 修复某些手机设置录音为询问或禁止时，点击录音崩溃bug
* 修复聊天标题设置emoji后显示不正常bug
* 修复在聊天界面预览大图与聊天界面图片消息顺序不一致bug
* 修复通过接口不填写昵称时，进入聊天界面不显示用户名的bug
* 修复选择图片后，点击原图后发送图片，APP崩溃bug
* 修复发送图片时，通过聊天详情再次进入聊天界面时，图片进度不更新bug
* 图片发送成功后，删除生成的图片
* 修复接收离线消息时，APP崩溃bug

#### 升级提示

+ 建议升级！

#### 升级指南
* 将jar包更新至 jmessage-sdk-1.1.4.jar更新时需删除老版本jar包。
* 将so库更新至 libjpush205.so 同时删除原来老版本so。注意不同的cpu型号对应的结构
* 由于富媒体的展示需求，SDK 中增加一个res文件夹存放资源文件。用户需将对应文件夹下的资源文件放入工程的目录中。
* 如果是从更早的版本升级过来，建议参考 SDK下载包最新版本的 example 来更新 AndroidManifest.xml 文件配置。




### JMessage iOS SDK v1.0.6

#### 更新时间
* 2015-09-14

#### 版本号
* JMessage 1.0.6b283
* JChat 1.0.2b11

#### Change Log
+ 收发消息过多时引起的bug
+ 解决引用第三方库冲突
+ 七牛Token失效无法恢复。
+ 发送语音或者图片七牛上传时候崩溃
+ 接收宽图收到为长图
+ 下载原图实际为缩略图
+ 解决custom类型消息收发崩溃问题
+ 播放语音和录制语音不能同时进行
+ 修复iOS端发送给安卓端无法下载大图
+ 修复语音不能正常下载问题
+ 修复了APNS用户不显示昵称而是username问题
+ 修复了转换json错误信息
+ 增加了API的登陆校验
+ 解决badge上报bug

#### 升级提示

+ 建议升级！

#### 升级指南
+ 使用新版本的JMessage.framework文件替换原工程下的同名旧文件

### JMessage Android SDK v1.1.3

#### 更新时间
2015-08-17

#### Change Log
+ 修复断开网络，群聊的会话界面里，进入【聊天详情】的按钮会消失
+ 修复发送自定义类型消息，jchat 接收方通知栏会有展示
+ 修复异步获取用户头像的接口getAvatarFileAsync，获取无头像的用户信息，返回码不合理
+ 修复没有昵称的群主在邀请人进群后，被邀请方显示的通知中没有显示群主的username
+ 修复收到加群事件时，由于网络不稳定导致事件有小概率丢失
+ JChat:修复收到的首张图片不会自动下载
+ JChat:修复从群详情里，选择里面的群成员发送消息，应用崩溃


#### 升级提示

+ 建议升级！

#### 升级指南
+ jar包更新至jmessage-android-1.1.3.jar，更新时需删除老版本jar
+ so库更新，/libs/armeabi/libjpush205.so.同时删除原来老版本的so
### JMessage Android SDK v1.0.18
#### 更新时间
2015-04-01

#### Change Log
+ JMesssage Android SDK 首次发布
+ 聊天支持：单聊，群聊
+ 聊天内容：文本，图片，语音对讲
+ 提供用户管理 ，群组管理功能

#### 升级提示

可选升级！

#### 升级指南

+ 打开后请按照AndroidManifest的提示替换您的包名和APPKey；
+ 全局替换："import cn.jpush.im.android.demo.R;" 替换为 "import 您的包名.R;"
+ 如果是Android Studio用户注意检查 build.gradle 中的 applicationId 与你的包名一致
