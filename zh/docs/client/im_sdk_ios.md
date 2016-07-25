### 概述

极光IM（英文名JMessage） SDK 基于 JPush 推送 SDK 开发，提供了 Push SDK 的完整功能，并提供 IM 即时通讯功能。

App 集成了 IM SDK 就不应再集成 JPush SDK（只提供 Push 功能的 SDK）。

要了解极光IM 整体的信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)。要集成 iOS SDK 请参考文档：[JMessage iOS 集成指南](../../guideline/jmessage_ios_guide)。


### 功能

极光IM 最核心的功能是 IM 即时消息的功能。

+ 单聊，群聊；
+ 消息类型：文本、语音、图片；
+ 用户未在线时保存离线消息；
+ 保证消息及时下发；
+ 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

### API 接口

需要了解完整的 SDK API，有三种方式：

+ 直接查看 JMessage.framework 里的 Headers 文件。这些头文件定义了 SDK 提供的对外接口，带有完善的注释与说明，甚至样例代码。
+ 下载 docset 文档。我们使用 Appledoc 工具基于上述 Headers 文件生成了 docset。可以使用 Xcode 直接打开查看，或者使用 Dash 查看。我们建议使用 Dash 效果更好。
+ 使用 Appledoc 生成的文档的在线版本：[JMessage iOS SDK APIs](jmessage_ios_appledoc_html/)

以下简要地列举 SDK API 提供的功能，同时提供部分简单的例子。

#### SDK初始化

JMessage.h 里定义的 setupJMessage 方法，需要在应用初始化时调用。建议在 AppDelegate 里应用加载完成时调用。

#####初始化 JMessage SDK
	/*!
	 * @abstract 初始化 JMessage SDK
	 *
	 * @param launchOptions    AppDelegate启动函数的参数launchingOption(用于推送服务)
	 * @param appKey           appKey(应用Key值,通过JPush官网可以获取)
	 * @param channel          应用的渠道名称
	 * @param isProduction     是否为生产模式
	 * @param category         iOS8新增通知快捷按钮参数
	 *
	 * @discussion 此方法必须被调用, 以初始化 JMessage SDK
	 *
	 * 如果未调用此方法, 本 SDK 的所有功能将不可用.
	 */
	+ (void)setupJMessage:(NSDictionary *)launchOptions
	               appKey:(NSString *)appKey
	              channel:(NSString *)channel
	     apsForProduction:(BOOL)isProduction
	             category:(NSSet *)category;
#####例子	  
	[JMessage setupJMessage:launchOptions
	                 appKey:@"用户的AppKey"
	                channel:@"应用的渠道名称"
	       apsForProduction:NO
	               category:nil];  

这个调用是必须的。否则 SDK 将不能正常工作。

####登录、注册
#####用户登录
	/*!
	 * @abstract 用户登录
	 *
	 * @param username 登录用户名. 规则与注册接口相同.
	 * @param password 登录密码. 规则与注册接口相同.
	 * @param handler 结果回调. 正常返回时 resultOjbect 为 nil.
	 */
	
	+ (void)loginWithUsername:(NSString *)username
	                 password:(NSString *)password
	        completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
#####例子
	[JMSGUser loginWithUsername:@"用户名"
	                           password:@"密码"
	                  completionHandler:^(id resultObject, NSError *error) {
	                      if (!error) {
	                         //登录成功
	                      } else {
	                         //登录失败
	                      }
	                  }];
	                  
#####退出登录
	/*!
	 * @abstract 当前用户退出登录
	 *
	 * @param handler 结果回调。正常返回时 resultObject 也是 nil。
	 *
	 * @discussion 这个接口一般总是返回成功，即使背后与服务器端通讯失败，SDK 也总是会退出登录的。
	 * 建议 App 也不必确认 SDK 返回, 就实际退出登录状态.
	 */
	+ (void)logout:(JMSGCompletionHandler JMSG_NULLABLE)handler;
#####例子
	//退出当前登录的用户
	        [JMSGUser logout:^(id resultObject, NSError *error) {
	            if (!error) {
	             	//退出登录成功
	            } else {
	                //退出登录失败
	            }
	        }];
	        
#####用户注册
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
#####例子
	[JMSGUser registerWithUsername:@"用户名"
	                      password:@"密码"
	                     completionHandler:^(id resultObject, NSError *error) {
	                         if (!error) {
	                             //注册成功
	                         } else {
	                            //注册失败
	                         }
	                     }];
####用户信息管理
#####批量获取用户信息
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
#####例子
	[JMSGUser userInfoArrayWithUsernameArray:@[@"username1", @"username2"] completionHandler:^(id resultObject, NSError *error) {
	        if (!error) {
	            //成功获取用户信息，resultObject为JMSGUser类型的数组
	        } else {
	            //获取用户信息失败   
	        }
	    }];
	  
#####获取用户个人信息
	/*!
	 * @abstract 获取用户本身个人信息
	 *
	 * @return 当前登陆账号个人信息
	 */
	+ (JMSGUser *)myInfo;
#####例子
	JMSGUser *user = [JMSGUser myInfo];

#####更新用户信息
	/*!
	 * @abstract 更新用户信息接口
	 *
	 * @param parameter     新的属性值
	 *        Birthday&&Gender 是NSNumber类型, Avatar NSData类型 其他 NSString
	 * @param type          更新属性类型
	 * @param handler       用户注册回调接口函数
	 */
	+ (void)updateMyInfoWithParameter:(id)parameter
	                    userFieldType:(JMSGUserField)type
	                completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
#####例子
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

#####更新密码
	/*!
	 * @abstract 更新密码接口
	 *
	 * @param newPassword   用户新的密码
	 * @param oldPassword   用户旧的密码
	 * @param handler       用户注册回调接口函数
	 */
	+ (void)updateMyPasswordWithNewPassword:(NSString *)newPassword
	                            oldPassword:(NSString *)oldPassword
	                      completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
#####例子
	[JMSGUser updateMyPasswordWithNewPassword:self.passwordField.text
	                                      oldPassword:self.oldpassword.text
	                                completionHandler:^(id resultObject, NSError *error) {
	                                    if (!error) {
	                                        //更新密码成功
	                                    } else {
	                                        //更新密码失败
	                                    }
	                                }];

#####获取头像缩略图
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
#####例子
	JMSGUser *user = [JMSGUser myInfo];
    [user thumbAvatarData:^(NSData *data, NSString *objectId, NSError *error) {
        if (!error) {
            //下载成功
        } else {
			//下载失败
        }
    }];

#####获取头像大图
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
#####例子
	JMSGUser *user = [JMSGUser myInfo];
	[user largeAvatarData:^(NSData *data, NSString *objectId, NSError *error) {
	                            if (!error) {
	           						 //下载成功
	       						 } else {
									//下载失败
	        					 }
	                        }];

#####获取用户展示名
	/*!
	 * @abstract 用户展示名
	 *
	 * @discussion 如果 nickname 存在则返回 nickname，否则返回 username
	 */
	- (NSString *)displayName;
#####例子
	JMSGUser *user = [JMSGUser myInfo];
	NSString myName = [user displayName];
####消息管理
#####创建单聊消息
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
#####例子
	JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:@"textContent"];
	JMSGMessage *message = [JMSGMessage createSingleMessageWithContent:textContent username:@"username"];

#####创建群聊消息
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
#####例子
	JMSGTextContent *textContent = [[JMSGTextContent alloc] initWithText:@"textContent"];
	JMSGMessage *message = [JMSGMessage createGroupMessageWithContent:textContent groupId:@"groupId"];

#####发送消息
	/*!
	 * @abstract 发送消息（已经创建好的）
	 *
	 * @param message 消息对象。
	 *
	 * @discussion 此接口与 createMessage:: 相关接口配合使用，创建好后使用此接口发送。
	 */
	+ (void)sendMessage:(JMSGMessage *)message;

#####发送单聊文本消息
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

#####发送单聊图片消息
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

#####发送单聊语音消息
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

#####发送群聊文本消息
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

#####发送群聊图片消息
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

#####发送群聊语音消息
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
####会话管理
会话相关的操作：
#####获取单聊会话
	/*!
	 * @abstract 获取单聊会话
	 *
	 * @param username 单聊对象 username
	 *
	 * @discussion 如果会话还不存在，则返回 nil
	 */
	+ (JMSGConversation * JMSG_NULLABLE)singleConversationWithUsername:(NSString *)username;
	

#####获取群聊会话
	/*!
	 * @abstract 获取群聊会话
	 *
	 * @param groupId 群聊群组ID。此 ID 由创建群组时返回的。
	 *
	 * @discussion 如果会话还不存在，则返回 nil
	 */
	+ (JMSGConversation * JMSG_NULLABLE)groupConversationWithGroupId:(NSString *)groupId;

#####创建单聊会话
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
#####例子
	[JMSGConversation createSingleConversationWithUsername:@"username" completionHandler:^(id resultObject, NSError *error) {
		                if (!error) {
		                   //创建单聊会话成功， resultObject为创建的会话
		                } else {
		                    //创建单聊会话失败
		                }
		            }];
		            
#####创建群聊会话
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
#####例子
	[JMSGConversation createGroupConversationWithGroupId:@"groupId" completionHandler:^(id resultObject, NSError *error) {
			                if (!error) {
			                   //创建群聊用会话成功， resultObject为创建的会话
			                } else {
			                    //创建群聊会话失败
			                }
			            }];

#####删除单聊会话
	/*!
	 * @abstract 删除单聊会话
	 *
	 * @param username 单聊用户名
	 *
	 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
	 */
	+ (BOOL)deleteSingleConversationWithUsername:(NSString *)username;
	

#####删除群聊会话
	/*!
	 * @abstract 删除群聊会话
	 *
	 * @param groupId 群聊群组ID
	 *
	 * @discussion 除了删除会话本身，还会删除该会话下所有的聊天消息。
	 */
	+ (BOOL)deleteGroupConversationWithGroupId:(NSString *)groupId;

#####conversation列表
	/*!
	 * @abstract 返回 conversation 列表（异步）
	 *
	 * @param handler 结果回调。正常返回时 resultObject 的类型为 NSArray，数组里成员的类型为 JMSGConversation
	 *
	 * @discussion 当前是返回所有的 conversation 列表。
	 * 
	 */
	+ (void)allConversations:(JMSGCompletionHandler)handler;
#####例子
	[JMSGConversation allConversations:^(id resultObject, NSError *error) {
            if (!error) {
               //获取成功，resultObject为会话对的数组
            } else {
				//获取失败
            }
	    }];
	    
消息相关操作：
#####获取某条消息
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

#####分页获取消息
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
#####获取所有消息记录
	/*!
	 * @abstract 异步获取所有消息记录
	 *
	 * @param handler 结果回调。正常返回时 resultObject 类型为 NSArray，数据成员类型为 JMSGMessage。
	 *
	 * @discussion 排序规则：最新
	 */
	- (void)allMessages:(JMSGCompletionHandler)handler;
#####例子
	//_conversation 为Conversation的实例对象 
	[conversation allMessages:^(id resultObject, NSError *error) {
	        NSArray *array = (NSArray *)resultObject;
	        LogInfo(@"消息数：%ld", (long)array.count);
	    }];

#####删除消息
	/*!
	 * @abstract 删除一条消息
	 *
	 * @param msgId 本地消息ID
	 */
	- (BOOL)deleteMessageWithMessageId:(NSString *)msgId;

#####删除全部消息
	/*!
	 * @abstract 删除全部消息
	 *
	 * @discussion 清空当前会话的所有消息。
	 */
	- (BOOL)deleteAllMessages;

#####创建消息对象
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

#####创建图片消息对象
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
#####例子
	//_conversation 为Conversation的实例对象 
	[_conversation createMessageAsyncWithImageContent:imageContent completionHandler:^(id resultObject, NSError *error) {
	            if (!error) {
	            	//创建成功
	            	//resultObject 为Message内容
	            }
	        }];

#####发送消息
	/*!
	 * @abstract 发送消息（已经创建好对象的）
	 *
	 * @param message 通过消息创建类接口，创建好的消息对象
	 *
	 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 xxx 方法来注册消息发送结果。
	 */
	- (void)sendMessage:(JMSGMessage *)message;

#####发送文本消息
	/*!
	 * @abstract 发送文本消息
	 * @param text 文本消息内容
	 * @discussion 快捷发消息接口。如果发送文本消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendTextMessage:(NSString *)text;

#####发送图片消息
	/*!
	 * @abstract 发送图片消息
	 * @param imageData 图片消息数据
	 * @discussion 快捷发送消息接口。如果发送图片消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendImageMessage:(NSData *)imageData;

#####发送语音消息
	/*!
	 * @abstract 发送语音消息
	 * @param voiceData 语音消息数据
	 * @param duration 语音消息时长（秒）. 长度必须大于 0.
	 * @discussion 快捷发送消息接口。如果发送语音消息不需要附加 extra，则使用此接口更方便。
	 */
	- (void)sendVoiceMessage:(NSData *)voiceData
	                duration:(NSNumber *)duration;

#####获取会话头像
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
#####例子
	//_conversation 为Conversation的实例对象 
	[_conversation avatarData:^(NSData *data, NSString *objectId, NSError *error) {
	        if (!error) {
	        	//获取成功
	        } else {
	        	//获取失败   
	        }];

#####清除会话未读数
	/*!
	 * @abstract 清除会话未读数
	 *
	 * @discussion 把未读数设置为 0
	 */
	- (void)clearUnreadCount;

#####获取最后一条消息的内容文本
	/*!
	 * @abstract 获取最后一条消息的内容文本
	 *
	 * @discussion 通常用来展示在会话列表的第 2 行. 如果是图片消息,通常是文本 [图片] 之类. CustomContent 可以定制这个文本.
	 */
	- (NSString *)latestMessageContentText;
#####例子
	//_conversation 为Conversation的实例对象 
	NSString *latestMessageText = [_conversation latestMessageContentText];

#####判断消息是否属于这个Conversation
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

#####从服务器端刷新会话信息
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
#####例子
	//_conversation 为Conversation的实例对象 
	[_conversation refreshTargetInfoFromServer:^(id resultObject, NSError *error) {
	    if (!error) {
	      //success
	    } else {
	      //刷新失败
	    }
	  }];

####群组管理
##### 创建群组
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

##### 更新群组信息	
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
    
##### 获取群组信息		
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
##### 获取我的群组列表	
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
##### 获取群组成员列表	
	/*!
	 * @abstract 获取群组成员列表
	 *
	 * @return 成员列表. NSArray 里成员类型是 JMSGUser.
	 *
	 * @discussion 一般在群组详情界面调用此接口，展示群组的所有成员列表。
	 * 本接口只是在本地请求成员列表，不会发起服务器端请求。
	 */
	- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)memberArray;

##### 添加群组成员	
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
##### 删除群组成员
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
##### 退出当前群组	
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
##### 获取群组的展示名	
	/*!
	 * @abstract 获取群组的展示名
	 *
	 * @discussion 如果 group.name 为空, 则此接口会拼接群组前 5 个成员的展示名返回.
	 */
	- (NSString *)displayName;
	
####黑名单
##### 获取黑名单列表

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

##### 添加黑名单		

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
	
##### 删除黑名单	

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
	            
##### 跨应用添加黑名单	

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
##### 跨应用删除黑名单	

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
####免打扰
##### 免打扰列表

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
##### 全局免打扰设置

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
	 
##### 用户免打扰设置

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

##### 群组免打扰设置

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
####跨应用
##### JMSGConversation
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
##### 例子
	// 创建跨应用会话
	[JMSGConversation createSingleConversationWithUsername:@"username" appKey:@"appkey"  completionHandler:^(id resultObject, NSError *error) {
        if (!error) {
	        NSLog(@"创建跨应用会话成功");
        } else {
            NSLog(@"创建跨应用会话失败");
        }
	}];

##### JMSGMessage
	
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

		
##### JMSGUser
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
##### JMSGGroup	
	/*!
	 * @abstract 添加群组跨应用成员
	 *
	 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
	 * @param handler 结果回调。正常返回时 resultObject 为 nil.
	 */
	- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
	                             appKey:userAppKey
	                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
	                  
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
	[group addMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被添加用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSLog(@"\n 添加群组跨应用成员 成功");
	    }
	}];
	
	[group removeMembersWithUsernameArray:[NSArray arrayWithObjects:@"username1",@"username2", nil] appKey:@"被删除用户所在应用的appkey" completionHandler:^(id resultObject, NSError *error) {
	    if (!error) {
	        NSLog(@"\n 添删除组跨应用成员 成功");
	    }
	}];

####事件处理
__事件类型的消息内容__

* 服务器端下发的事件通知, 比如用户被踢下线,群组里加了人, SDK 作为一个特殊的消息类型处理
* SDK 以消息的形式通知到 App. 详情参见 JMessageDelegate

##### JMSGEventContent
	//通知事件类型
	typedef NS_ENUM(NSInteger, JMSGEventNotificationType) {
	  /// 事件类型: 登录被踢
	  kJMSGEventNotificationLoginKicked = 1,
	  /// 事件类型: 群组被创建
	  kJMSGEventNotificationCreateGroup = 8,
	  /// 事件类型: 退出群组
	  kJMSGEventNotificationExitGroup = 9,
	  /// 事件类型: 添加新成员
	  kJMSGEventNotificationAddGroupMembers = 10,
	  /// 事件类型: 成员被踢出
	  kJMSGEventNotificationRemoveGroupMembers = 11,
	  /// 事件类型: 群信息更新
	  kJMSGEventNotificationUpdateGroupInfo = 12,
	};
	
	/*!
	 * @abstract 事件类型
	 * @discussion 参考事件类型的定义 JMSGEventNotificationType
	 */
	@property(nonatomic, assign, readonly) JMSGEventNotificationType eventType;
	
	
##### 事件的文本描述 
	/*!
	 @abstract 展示此事件的文本描述
	
	 @discussion SDK 根据事件类型，拼接成完整的事件描述信息。
	 */
	- (NSString * JMSG_NONNULL)showEventNotification;  
##### 例子
	
	if (message.contentType == kJMSGContentTypeEventNotification) {
         NSString *showText = [((JMSGEventContent *)message.content) showEventNotification];
    }
    //比如，在群group中，用户A邀请用户B加入了群,showText 如下：
    //showText = "A邀请B加入了群组"
##### 自定义事件的文本描述
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
	JMSGEventContent *eventContent = (JMSGEventContent*)message.content;
	//获取发起事件的用户名
	NSString *fromUsername = [eventContent getEventFromUsername];
	//获取事件作用对象用户名列表
	NSArray *toUsernameList = [eventContent getEventToUsernameList];
	//根据事件类型，定制相应描述（以事件类型: 添加新成员为例子）
	if(eventContent.eventType == kJMSGEventNotificationAddGroupMembers) {
		NSString *showText = [NSString stringWithFormat:@"%@邀请了%@加入了群聊",fromUsername,[toUsernameList componentsJoinedByString:@","]];
	}
	
#### 通知监听

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

	- (void)onLoginUserKicked;

#### 结果回调

JMessage SDK 提供的很多接口都以异步方式返回，其回调都是一个类型为 JMSGCompletionHandler 的 block，其定义为

		typedef void (^JMSGCompletionHandler)(id resultObject, NSError *error);

JMSGCompletionHandler 有 2 个参数：

+ id resultObject 返回的结果对象
+ NSError *error 返回的错误

如果 error 不为 nil，则表示调用出错，error -> code 定义了错误码，error -> description 有错误的详细说明。也可以从文档里根据错误码找到进一步的错误说明信息。

如果 error 为 nil，则调用成功，resultObject 是返回结果对象。每个接口 resultObject 的实际类型不同，在每个接口的定义文档里会指定。实际使用时，应把该 resultObject 转型为该接口的正常对象。

与 JMSGCompletionHandler 类似的，还有另外一个 block 叫 JMSGAsyncDataHandler，用于返回媒体文件数据。


#### 实现回调 
##### Conversation 回调

	// optional
	// 收到此通知后, 建议处理: 如果 App 当前在会话列表页，刷新整个列表；如果在聊天界面，刷新聊天标题。
	- (void)onConversationChanged:(JMSGConversation *)conversation;
	
	// optional
	// 未读消息数变更
	- (void)onUnreadChanged:(NSUInteger)newCount;


##### Group 回调

	// optional
	// 群信息详情被改变
	- (void)onGroupInfoChanged:(JMSGGroup *)group;


##### User 回调

	// optional
	// 用户在其他设备上登录，当前设备被踢出登录。
	- (void)onLoginUserKicked;

##### Database Migrate 回调

	// optional
	// 数据库开始升级
	 (void)onDBMigrateStart;
	
	// optional
	// 数据库升级结束，如果 Error 为 nil 代表升级成功，否则为失败
	- (void)onDBMigrateFinishedWithError:(NSError *)error;


### 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [JMessage iOS 集成指南](../../guideline/jmessage_ios_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM REST API](../../server/rest_api_im/)

