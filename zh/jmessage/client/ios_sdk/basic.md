<h1>iOS IM SDK 基础功能</h1>


## 概述
JMessage iOS IM SDK的基础功能。了解极光 IM 的详细信息，请参考文档：[JMessage 产品简介](../../guideline/jmessage_guide)


### 字符串规范
此处定义JMessage产品里字段属性与规范，用于校验与规范化。  

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >字符说明</th>
			<th >长度限制</th>
		</tr>
		<tr >
			<td>app_key</td>
			<td>由 JPush Web Portal 生成的 24位字符串。字母或者数字，不区分大小写</td>
			<td></td>
		</tr>
		<tr >
			<td>username</td>
			<td>以字母或者数字开头。支持字母、数字、下划线、英文点、减号、 @。</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>password</td>
			<td>不限</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>group_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>nickname</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>note_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>other</td>
			<td>其他未明确指定的 String 类型字段，都按照这个处理。  
支持字符：全部</td>
			<td>Byte(0~250)</td>
		</tr>
	</table>
</div>

### SDK 初始化

+ `setupJMessage:` 方法，需要在应用初始化时调用
+ SDK 初始化时，可设置是否启用消息记录漫游
		
打开消息漫游之后，用户多个设备之间登录时，SDK会自动将历史消息同步到本地，同步完成之后SDK会触发代理方法`onSyncRoamingMessageConversation:`通知上层刷新,具体方法见[消息同步](./message#message-sync)

```
/*!
 * @abstract 初始化 JMessage SDK
 *
 * @param launchOptions    AppDelegate启动函数的参数launchingOption(用于推送服务)
 * @param appKey           appKey(应用Key值,通过jiguang官网可以获取)
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

### 监听代理
JMessage SDK 采用 Delegate 的机制给 App 发通知，而不是采用 iOS 平台通用的通知方式。

#### 添加代理

可以在 App 的任何类里，调用以下方法来监听事件通知。

	[JMessage addDelegate:self withConversation:nil]

为了上述这行有效，则需要在当前类的头文件里声明实现 JMessageDelegate 协议。

以下示例在 AppDelegate 里加监听：

	@interface AppDelegate : UIResponder <UIApplicationDelegate,JMessageDelegate>

另外，需要实现你需要监听的事件的方法。比如监听数据库升级：

	- (void)onDBMigrateStart {
	  NSLog(@"onDBmigrateStart in appdelegate");
	  _isDBMigrating = YES;
	}

***注意：*** 由于 JMessage SDK 会在 setup 时检测数据库升级，如果有需要就发出通知。所以建议在 AppDelegate 里调用 setupJMessage 之前就添加监听。

#### 移除代理
为了避免内存损耗和不必要的监听，在上层不需要监听时，可以调用一下接口移除监听：

	+(void)removeDelegate: withConversation:

更多监听代理的使用可以查看 [事件管理](./event) 

### 注册
直接通过 `username` 和 `password` 来注册 im 账号

```
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
```

也可以在注册用户时，携带用户其他信息字段一起注册，可携带字段请查看 [JMSGUserInfo](./jmessage_ios_appledoc_html/Classes/JMSGUserInfo.html)

```
/*!
 * @abstract 新用户注册(支持携带用户信息字段)
 *
 * @param username  用户名. 长度 4~128 位.
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
```

### 登录

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

### 退出登录
如果上层不主动调用 logout 接口，原则上是一直处于登录的。

```
/*!
 * @abstract 当前用户退出登录
 *
 * @param handler 结果回调。正常返回时 resultObject 也是 nil。
 *
 */
+ (void)logout:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 通知管理
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

#### 重置角标(到服务器)
```
/*!
 * @abstract 重置角标(为0)
 *
 * @discussion 相当于 [setBadge:0] 的效果.
 * 参考 [JMessage setBadge:] 说明来理解其作用.
 */
+ (void)resetBadge;
```

#### 自定义通知栏展示逻辑
上层开发者可以对通知栏进行一些定制，如：控制离线消息的存储、自定义通知栏内容等，具体的功能可以想象查看 `JMSGOptionalContent` 类里面的说明。  
在 [发送消息 - 附带可控参数](./message#send-message-option) 模块会具体说明实现。


### 登录设备记录
登录时可以获取到设备的登录记录。

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

##### DeviceInfo
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">属性</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >platformType</td>
      <td >`JMSGPlatformType`</td>
      <td >获取设备所属平台类型</td>
    </tr>
	<tr >
      <td >isLogin</td>
      <td >`BOOL`</td>
      <td >判断设备当前是否处于登陆状态, YES:登陆，NO:登出</td>
    </tr>
    <tr >
      <td >online</td>
      <td >`UInt32`</td>
      <td >获取设备在线状态，0不在线，1在线</td>
    </tr>
	<tr >
      <td >mtime</td>
      <td >`NSNumber`</td>
      <td > 获取设备最近一次登陆时间，单位-秒</td>
    </tr>
	<tr >
      <td >flag</td>
      <td >`NSInteger`</td>
      <td > 默认为0，1表示该设备被当前登录设备踢出</td>
    </tr>
    </table>
</div>


### 多端同时在线

SDK从3.3.0版本开始支持多端同时在线，具体规则见[多端在线说明](../../guideline/faq/#multi-platfrom)