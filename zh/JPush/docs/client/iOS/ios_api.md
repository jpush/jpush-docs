# iOS API

## 标签与别名 API (iOS)

### 功能说明

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示，设置标签别名请注意处理call back结果。
<p>只有call back 返回值为 0 才设置成功，才可以向目标推送。否则服务器 API 会返回1011错误。所有回调函数都在主线程运行。
</div>

<br>

提供几个相关 API 用来设置别名（alias）与标签（tags）。

这几个 API 可以在 App 里任何地方调用。

#### 别名 alias

为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。  
每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，服务器端API会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用服务器端API发通知到客户端提醒用户。

#### 标签 tag

为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page, women

### Method - setTagsWithAlias (with Callback)

调用此 API 来同时设置别名与标签，支持回调函数。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

#### 支持的版本

开始支持的版本：1.4.0

#### 接口定义

    + (void)setTags:(NSSet *)tags alias:(NSString *)alias callbackSelector:(SEL)cbSelector object:(id)theTarget;
    

#### 参数说明

- alias
    - nil 此次调用不设置此值。
    - 空字符串 （@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为NSString类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* callbackSelector 

    * nil 此次调用不需要 Callback。
    * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。
    * 回调函数请参考SDK 实现。

* theTarget

    * 参数值为实现了callbackSelector的实例对象。
    * nil 此次调用不需要 Callback。

```
-(void)tagsAliasCallback:(int)iResCode
                    tags:(NSSet*)tags
                   alias:(NSString*)alias
{
    NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias);
}

```

### Method - setTagsWithAlias (background)

调用此 API 在后台同时设置别名与标签，不需要处理设置结果，SDK会自动进行失败重试

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

需要注意，该background模式的设置和非background的设置是两种不同的设置，互相不影响，意味着，非background的设置不会终止当前进行的background设置，除非另一个background设置发生。

#### 支持的版本

开始支持的版本：2.1.0

#### 接口定义

```
+ (void)setTags:(NSSet *)tags aliasInbackground:(NSString *)alias;
```

#### 参数说明

- alias
    - nil 此次调用不设置此值。
    - 空字符串 （@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为NSString类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

```
[JPUSHService setTags:tags aliasInbackground:alias];
```

### Method - setTagsWithAlias (with block)

调用此 API 来同时设置别名与标签，通过block来返回设置别名与标签的结果。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

#### 支持的版本

开始支持的版本：2.1.0

#### 接口定义

```
+ (void)setTags:(NSSet *)tags alias:(NSString *)alias fetchCompletionHandle:(void (^)(int iResCode, NSSet *iTags, NSString *iAlias))completionHandler
```

#### 参数说明

- alias
    - nil 此次调用不设置此值。
    - 空字符串 （@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为NSString类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* (void (^)(int iResCode, NSSet *iTags, NSString *iAlias))completionHandler
    
    * completionHandler用于处理设置返回结果
    * iResCode返回的结果状态码
    * iTags和iAlias返回设置的tag和alias

```
[JPUSHService setTags:tags alias:alias fetchCompletionHandle:^(int iResCode, NSSet *iTags, NSString *iAlias){
 NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, iTags, iAlias);
}];
```

### Method - setTags

调用此 API 来设置标签，支持回调函数。

该方法是 setTagsWithAlias (with Callback) 的简化版本，用于只变更标签的情况。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>使用建议
<br>
<p>如果待设置的 alias / tags 是动态的，有可能在调用 setTagsWithAlias 时因为 alias / tags 无效而整调用失败。
<br>
<p>调用此方法只设置 tags，可以排除可能的无效的 alias 对本次调用的影响。
</div>

#### 支持的版本

开始支持的版本：1.4.0

#### 接口定义

    + (void)setTags:(NSSet *)tags callbackSelector:(SEL)cbSelector object:(id)theTarget;
    

#### 参数说明

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个tag，但总长度不得超过7K字节。（判断长度需采用UTF-8编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* callbackSelector

    * nil 此次调用不需要 Callback。
    * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。
    * 回调函数请参考SDK 实现。

* theTarget

   * 参数值为实现了callbackSelector的实例对象。
   * nil 此次调用不需要 Callback。

```
    - (void)tagsAliasCallback:(int)iResCode tags:(NSSet*)tags alias:(NSString*)alias {
                NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias);}
```

### Method - setAlias

调用此 API 来设置别名，支持回调函数。

该方法是 setTagsWithAlias (with Callback) 的简化版本，用于只变更别名的情况。

#### 支持的版本

开始支持的版本：1.4.0

#### 接口定义

        + (void)setAlias:(NSString *)alias callbackSelector:(SEL)cbSelector object:(id)theTarget;
    

#### 参数说明

* alias 
     * 空字符串 （@""）表示取消之前的设置。
     * 每次调用设置有效的别名，覆盖之前的设置。
     * 有效的别名组成：字母（区分大小写）、数字、下划线、汉字。
     * 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）
* callbackSelector 
     * nil 此次调用不需要 Callback。
     * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。
     * 回调函数请参考SDK 实现。
* theTarget


     * 参数值为实现了callbackSelector的实例对象。
     * nil 此次调用不需要 Callback。

```
    - (void)tagsAliasCallback:(int)iResCode tags:(NSSet*)tags alias:(NSString*)alias {
            NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias)        }
```

### Method - filterValidTags

用于过滤出正确可用的 tags。

如果总数量超出最大限制则返回最大数量的靠前的可用tags。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>使用建议
<br>
 <p>设置 tags 时，如果其中一个 tag 无效，则整个设置过程失败。
<br>
 <p>如果 App 的 tags 会在运行过程中动态设置，并且存在对 JPush SDK tag 规定的无效字符，则有可能一个 tag 无效导致这次调用里所有的 tags 更新失败。
<br>
 <p>这时你可以调用本方法 filterValidTags 来过滤掉无效的 tags，得到有效的 tags，再调用 JPush SDK 的 set tags / alias 方法。
</div>

#### 支持的版本

开始支持的版本：1.4.0

#### 接口定义

    + (NSSet*)filterValidTags:(NSSet*)tags;
    

#### 参数说明

* tags 
     * 原 tag 集合。

#### 接口返回

有效的 tag 集合。

返回错误码参考： [错误码定义](#client_error_code)



## 获取 APNs（通知） 推送内容

### 支持的版本

最初的版本。

### 功能说明

iOS 设备收到一条推送（APNs），用户点击推送通知打开应用时，应用程序根据状态不同进行处理需在 AppDelegate 中的以下两个方法中添加代码以获取apn内容

* 如果 App 状态为未运行，此函数将被调用，如果launchOptions包含UIApplicationLaunchOptionsRemoteNotificationKey表示用户点击apn 通知导致app被启动运行；如果不含有对应键值则表示 App 不是因点击apn而被启动，可能为直接点击icon被启动或其他。

```
- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// apn 内容获取：
NSDictionary *remoteNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsRemoteNotificationKey]
```

* 基于iOS 6 及以下的系统版本，如果 App状态为正在前台或者点击通知栏的通知消息，那么此函数将被调用，并且可通过AppDelegate的applicationState是否为UIApplicationStateActive判断程序是否在前台运行。此种情况在此函数中处理：

```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo;
```
* 基于iOS 7 及以上的系统版本，如果是使用 iOS 7 的 Remote Notification 特性那么处理函数需要使用

```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler;
```
* 基于iOS 10及以上的系统版本，原[application: didReceiveRemoteNotification:]将会被系统废弃，  
由新增UserNotifications Framework中的[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:]  
或者[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]方法替代。  
在2.1.9版本以后可实现SDK封装的JPUSHRegisterDelegate协议方法，适配iOS10新增的delegate协议方法。  
即以下两个方法：

```
- (void)jpushNotificationCenter:(UNUserNotificationCenter )center willPresentNotification:(UNNotification )notification withCompletionHandler:(void (^)(NSInteger))completionHandler; 
// NSDictionary * userInfo = notification.request.content.userInfo; 
// APNs内容为userInfo

- (void)jpushNotificationCenter:(UNUserNotificationCenter )center didReceiveNotificationResponse:(UNNotificationResponse )response withCompletionHandler:(void (^)())completionHandler; 
// NSDictionary * userInfo = response.notification.request.content.userInfo; 
// APNs内容为userInfo
```

### 示例代码

```
// NS_DEPRECATED_IOS(3_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] or -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:] for user visible notifications and -[UIApplicationDelegate application:didReceiveRemoteNotification:fetchCompletionHandler:] for silent remote notifications")
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {
  // 取得 APNs 标准信息内容
  NSDictionary *aps = [userInfo valueForKey:@"aps"];
  NSString *content = [aps valueForKey:@"alert"]; //推送显示的内容
  NSInteger badge = [[aps valueForKey:@"badge"] integerValue]; //badge数量
  NSString *sound = [aps valueForKey:@"sound"]; //播放的声音
         
  // 取得Extras字段内容
  NSString *customizeField1 = [userInfo valueForKey:@"customizeExtras"]; //服务端中Extras字段，key是自己定义的
  NSLog(@"content =[%@], badge=[%d], sound=[%@], customize field  =[%@]",content,badge,sound,customizeField1);
         
  // iOS 10 以下 Required
  [JPUSHService handleRemoteNotification:userInfo];
}

//iOS 7 Remote Notification
- (void)application:(UIApplication *)application didReceiveRemoteNotification:  (NSDictionary *)userInfo fetchCompletionHandler:(void (^)   (UIBackgroundFetchResult))completionHandler {
     
  NSLog(@"this is iOS7 Remote Notification");
         
  // iOS 10 以下 Required
  [JPUSHService handleRemoteNotification:userInfo];
  completionHandler(UIBackgroundFetchResultNewData);
}

#pragma mark- JPUSHRegisterDelegate // 2.1.9版新增JPUSHRegisterDelegate,需实现以下两个方法

// iOS 10 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center  willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)  (NSInteger))completionHandler {
  // Required
  NSDictionary * userInfo = notification.request.content.userInfo;
  if([notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) {
    [JPUSHService handleRemoteNotification:userInfo];
  }
  else {
     // 本地通知
  }
  completionHandler(UNNotificationPresentationOptionAlert); // 需要执行这个方法，选择是否提醒用户，有Badge、Sound、Alert三种类型可以选择设置
}

// iOS 10 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler: (void (^)())completionHandler {
  // Required
  NSDictionary * userInfo = response.notification.request.content.userInfo;
  if([response.notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) {
    [JPUSHService handleRemoteNotification:userInfo];
  }
  else {
     // 本地通知
  }
  completionHandler();  // 系统要求执行这个方法
}
```

参考文档：[Handling Local and Remote Notifications][0]

## 获取自定义消息推送内容
<a name="message"></a>

### 支持的版本

r1.2.5 以后。

### 功能说明

只有在前端运行的时候才能收到自定义消息的推送。

从jpush服务器获取用户推送的自定义消息内容和标题以及附加字段等。

### 实现方法

获取iOS的推送内容需要在delegate类中注册通知并实现回调方法。

 在方法- (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*) launchOptions 加入下面的代码：

```

    NSNotificationCenter *defaultCenter = [NSNotificationCenter defaultCenter];
    [defaultCenter addObserver:self selector:@selector(networkDidReceiveMessage:) name:kJPFNetworkDidReceiveMessageNotification object:nil];
```

 实现回调方法 networkDidReceiveMessage

```
    - (void)networkDidReceiveMessage:(NSNotification *)notification {
        NSDictionary * userInfo = [notification userInfo];
        NSString *content = [userInfo valueForKey:@"content"];
        NSDictionary *extras = [userInfo valueForKey:@"extras"]; 
        NSString *customizeField1 = [extras valueForKey:@"customizeField1"]; //服务端传递的Extras附加字段，key是自己定义的
     
    }
```

#### 参数描述：

content：获取推送的内容

extras：获取用户自定义参数

customizeField1：根据自定义key获取自定义的value

更多实现参考 SDK下载压缩包中的 demo。

## 获取 RegistrationID


#### RegistrationID 定义

集成了 JPush SDK 的应用程序在第一次成功注册到 JPush 服务器时，JPush 服务器会给客户端返回一个唯一的该设备的标识 - RegistrationID。JPush SDK 会以广播的形式发送 RegistrationID 到应用程序。

应用程序可以把此 RegistrationID 保存以自己的应用服务器上，然后就可以根据 RegistrationID 来向设备推送消息或者通知。

### API - registrationIDCompletionHandler:(with block)
#### 支持的版本

开始支持的版本：2.1.9。

#### 接口定义

```
+ (void)registrationIDCompletionHandler:(void(^)(int resCode,NSString *registrationID))completionHandler;

```
#### 参数说明

+ (void(^)(int resCode,NSString *registrationID))completionHandler
	+ completionHandler用于处理设置返回结果
	+ resCode返回的结果状态码
	+ registrationID返回registrationID

```
[JPUSHService registrationIDCompletionHandler:^(int resCode, NSString *registrationID) {
    NSLog(@"resCode : %d,registrationID: %@",resCode,registrationID);
}];
```

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示：
  <br>
<p>建议使用此接口获取registrationID，模拟器中调用此接口resCode返回1011,registrationID返回nil.
</div>

### API - registrationID

调用此 API 来取得应用程序对应的 RegistrationID。 只有当应用程序成功注册到 JPush 的服务器时才返回对应的值，否则返回空字符串。

#### 支持的版本

开始支持的版本：1.7.0。

#### 接口定义

+(NSString *)registrationID
    
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示：
  <br>
<p>iOS 9系统，应用卸载重装，APNs返回的devicetoken会发生变化，开发者需要获取设备最新的Registration id。请在kJPFNetworkDidLoginNotification的实现方法里面调用"RegistrationID"这个接口来获取 RegistrationID。
</div>

### 附加说明

#### 通过 RegistrationID 推送消息和通知

可以通过 RegistrationID 来推送消息和通知， 参考文档 [Push API v3](../../server/push/rest_api_v3_push/#audience)， 当audience 参数为 RegistrationID 时候即可根据 RegistrationID 推送。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>注：
  <br>
  <p>要使用此功能，客户端 App 一定要集成有 r1.7.0 及以上版本的 JPush iOS SDK
</div>

## 设置Badge

### 支持的版本

v1.7.4及后续版本

### 功能说明

badge是iOS用来标记应用程序状态的一个数字，出现在程序图标右上角。
JPush封装badge功能，允许应用上传badge值至JPush服务器，由JPush后台帮助管理每个用户所对应的推送badge值，简化了设置推送badge的操作。

实际应用中，开发者可以直接对badge值做增减操作，无需自己维护用户与badge值之间的对应关系。

### API setBadge

设置JPush服务器中存储的badge值

#### 接口定义

```
+ (BOOL)setBadge:(int)value
```
#### 参数说明

* value 取值范围：[0,99999]

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>设置badge值，本地仍须调用UIApplication:setApplicationIconBadgeNumber函数
</div>

<br>

* 返回值 
     * 在value的取值区间内返回 TRUE，否则返回FALSE

### API resetBadge

清空JPush服务器中存储的badge值，即 [setBadge:0]

#### 接口定义

```
+ (void)resetBadge
```


## 本地通知

### 支持的版本

v1.8.0及后续版本，v2.1.9版本有更新

### 功能说明


iOS 设备收到一条本地通知，用户点击通知打开应用时，应用程序根据状态不同进行处理需在 AppDelegate 中的以下两个方法中添加代码以获取本地通知内容

+ 如果 App 状态为未运行，此函数将被调用，如果launchOptions包含UIApplicationLaunchOptionsLocalNotificationKey表示用户点击本地通知导致app被启动运行；如果不含有对应键值则表示 App 不是因点击本地通知而被启动，可能为直接点击icon被启动或其他。

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// 本地通知内容获取：NSDictionary *localNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsLocalNotificationKey]
```

+ 如果 App状态为正在前台或者后台运行，那么此函数将被调用，并且可通过AppDelegate的applicationState是否为UIApplicationStateActive判断程序是否在前台运行。此种情况在此函数中处理：

```
// NS_DEPRECATED_IOS(4_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] or -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]")
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification;
// 本地通知为notification
```
+ 在iOS 10以上上述方法将被系统废弃，由新增UserNotifications Framework中的-[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] 或者 -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]方法替代。为此，SDK封装了JPUSHRegisterDelegate协议，只需实现相应的协议方法即可兼容系统新的delegate方法，实现新的回调方式。与上述远程推送新回调方法一致，如下实现代码：

```
#pragma mark- JPUSHRegisterDelegate (2.1.9版新增JPUSHRegisterDelegate,需实现以下两个方法)

	// iOS 10 Support Required
	- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center 	willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)	(NSInteger))completionHandler {
  		NSDictionary * userInfo = notification.request.content.userInfo;
  		if([notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { // 可以此判断是本地通知还是远程通知
    		[JPUSHService handleRemoteNotification:userInfo];
  		}
  		else {
  			// 本地通知
  		}
  		completionHandler(UNNotificationPresentationOptionBadge|UNNotificationPresentationOptionSound|UNNotificationPresentationOptionAlert); //括号内为可选项，分别代表角标、声音、显示提醒
	}

	// iOS 10 Support Required
	- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:	(void (^)())completionHandler {
  		NSDictionary * userInfo = response.notification.request.content.userInfo;
  		if([response.notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { // 可以此判断是本地通知还是远程通知
    		[JPUSHService handleRemoteNotification:userInfo];
  		}
  		else {
  			// 本地通知
  		}
  		completionHandler();
	}
	
```

### Method  AddNotification

#### 支持版本
v2.1.9及后续版本

#### 功能说明
API 用于注册或更新推送（支持iOS10，并兼容iOS10以下版本）

#### 接口定义

```
+ (void)addNotification:(JPushNotificationRequest *)request;
```
#### 参数说明
+ request [JPushNotificationRequest](../client/ios_tutorials/#_JPushNotificationRequest)实体类型，可传入推送的属性

#### 调用说明
request中传入已有推送的request.requestIdentifier即更新已有的推送，否则为注册新推送。

#### 代码示例

```
- (void)testAddNotification {
  JPushNotificationContent *content = [[JPushNotificationContent alloc] init];
  content.title = @"Test Notifications";
  content.subtitle = @"2016";
  content.body = @"This is a test code";
  content.badge = @1;
  content.categoryIdentifier = @"Custom Category Name";
  
  // iOS 10 以上支持
  //5s后提醒
  JPushNotificationTrigger *trigger1 = [[JPushNotificationTrigger alloc] init];
  trigger1.timeInterval = 5;
  //每小时重复 1 次
  JPushNotificationTrigger *trigger2 = [[JPushNotificationTrigger alloc] init];
  trigger2.timeInterval = 3600;
  trigger2.repeat = YES;
  
  //每周一早上8：00提醒
  NSDateComponents *components = [[NSDateComponents alloc] init];
  components.weekday = 2;
  components.hour = 8;
  JPushNotificationTrigger *trigger3 = [[JPushNotificationTrigger alloc] init];
  trigger3.dateComponents = components;
  trigger3.repeat = YES;
  
  //#import <CoreLocation/CoreLocation.h>
  //一到某地点提醒
  CLRegion *region = [[CLRegion alloc] initCircularRegionWithCenter:CLLocationCoordinate2DMake(0, 0) radius:0 identifier:@"test"];
  JPushNotificationTrigger *trigger4 = [[JPushNotificationTrigger alloc] init];
  trigger4.region = region;
  
  // iOS 10 以下支持
  //5s后提醒
  JPushNotificationTrigger *trigger5 = [[JPushNotificationTrigger alloc] init];
  trigger5.fireDate = [NSDate dateWithTimeIntervalSinceNow:5];
  
  JPushNotificationRequest *request = [[JPushNotificationRequest alloc] init];
  request.requestIdentifier = @"sampleRequest";
  request.content = content;
  request.trigger = trigger1;//trigger2;//trigger3;//trigger4;//trigger5;
  [JPUSHService addNotification:request];
}
```

### Method  RemoveNotification

#### 支持版本
v2.1.9及后续版本

#### 功能说明
API 用于移除待推送或已在通知中心显示的推送（支持iOS10，并兼容iOS10以下版本）

#### 接口定义

```
+ (void)removeNotification:(JPushNotificationIdentifier *)identifier;
```
#### 参数说明
+ identifier [JPushNotificationIdentifier](../client/ios_tutorials/#_ JPushNotificationIdentifier)实体类型

#### 调用说明
- 通过identifier来传入需要移除的推送，其中通过identifier.identifiers传入需要移除的推送标识，传入nil或空数组即移除所有待推送或已在通知中心显示的推送，通过identifier.delivered传入待推送或已在通知中心显示的标志，@(YES)为已在通知中心显示的，@(NO)为待推送的。
- iOS10以下系统还可以通过identifier.notificationObj传入特定推送对象来移除此推送。

#### 代码示例

```
- (void)testRemoveNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = @(YES);  // iOS 10 以上支持
  [JPUSHService removeNotification:identifier];
}
```

### Method  FindNotification

#### 支持版本
v2.1.9及后续版本

#### 功能说明
API 用于查找推送（支持iOS10，并兼容iOS10以下版本）

#### 接口定义

```
+ (void)findNotification:(JPushNotificationIdentifier *)identifier;
```
#### 参数说明
+ identifier [JPushNotificationIdentifier](ios_tutorials/#_ JPushNotificationIdentifier)实体类型

#### 调用说明
- 通过identifier来传入需要查找的推送，其中通过identifier.identifiers传入需要查找的推送标识，传入nil或空数组即查找所有待推送或已在通知中心显示的推送，通过identifier.delivered传入待推送或已在通知中心显示的标志，@(YES)为已在通知中心显示的，@(NO)为待推送的。
- 须要设置identifier.findCompletionHandler才能得到查找的结果，通过(NSArray *oResults, NSArray *nResults)返回推送对象数组，iOS10以下为同步查找返回结果oResults数组（包含UILocalNotification类型元素），此时nResults为空，iOS10以上为异步查找返回结果nResults数组（包含UNNotificationRequest类型元素），此时oResults为空。

#### 代码示例

```
- (void)testFindNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = @(YES);
  identifier.findCompletionHandler = ^(NSArray *oResults, NSArray *nResults) {
    NSLog(@"iOS10以下返回结果为：%@", oResults);
    NSLog(@"iOS10以上返回结果为：%@", nResults);
  };
  [JPUSHService findNotification:identifier];
}
```

### Method  SetLocalNotification

#### 功能说明
API 用于注册本地通知
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9版后将会被废弃，由AddNotification方法取代，建议及早放弃使用。
</div>

#### 接口定义

```
+ (UILocalNotification *)setLocalNotification:(NSDate *)fireDate
                                    alertBody:(NSString *)alertBody
                                        badge:(int)badge
                                  alertAction:(NSString *)alertAction
                                identifierKey:(NSString *)notificationKey
                                     userInfo:(NSDictionary *)userInfo
                                    soundName:(NSString *)soundName;
```
iOS8 新参数使用API。非iOS8版本或者不需要使用iOS8新功能请使用上面的API 

```

+ (UILocalNotification *)setLocalNotification:(NSDate *)fireDate
                                    alertBody:(NSString *)alertBody
                                        badge:(int)badge
                                  alertAction:(NSString *)alertAction
                                identifierKey:(NSString *)notificationKey
                                     userInfo:(NSDictionary *)userInfo
                                    soundName:(NSString *)soundName
                                       region:(CLRegion *)region
                           regionTriggersOnce:(BOOL)regionTriggersOnce
                                     category:(NSString *)category
```
#### 参数说明

+ fireDate 本地推送触发的时间
+ alertBody 本地推送需要显示的内容
+ badge 角标的数字。如果不需要改变角标传-1
+ alertAction 弹框的按钮显示的内容（iOS 8默认为"打开",其他默认为"启动"）
+ notificationKey 本地推送标示符
+ userInfo 自定义参数，可以用来标识推送和增加附加信息
+ soundName 本地通知声音名称设置，空为默认声音
+ region
+ regionTriggersOnce
+ category

#### 调用说明

fireDate必须大于当前时间，同时不能为空。注册通知数目必须小于64个。

#### 代码示例

```
[JPUSHService setLocalNotification:[NSDate dateWithTimeIntervalSinceNow:100]
                      alertBody:@"alert content"
                          badge:1
                    alertAction:@"buttonText"
                  identifierKey:@"identifierKey"
                       userInfo:nil
                      soundName:nil];
```

### Method  showLocalNotificationAtFront

#### 功能说明
API用来在APP前台运行时，仍然将通知显示出来。(样式为UIAlertView)
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
iOS10以下还可继续使用，iOS10以上在[JPUSHRegisterDelegate jpushNotificationCenter:willPresentNotification:withCompletionHandler:]方法中调用completionHandler(UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert);即可，故v2.1.9版后将会被废弃，建议及早放弃使用。
</div>

#### 接口定义

```
+ (void)showLocalNotificationAtFront:(UILocalNotification *)notification
                       identifierKey:(NSString *)notificationKey;
```

#### 参数说明
+ notification  当前触发的UILocalNotification
+ notificationKey  过滤不需要前台显示的通知。只有notificationKey标示符的通知才会在前台显示。如果需要全部都显示，该参数传nil。

#### 调用说明

API必须放在 - (void)application:(UIApplication \*)application didReceiveLocalNotification:(UILocalNotification \*)notification（AppDelegate.m) 苹果的回调函数下。

#### 代码示例

```
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification { [JPUSHService showLocalNotificationAtFront:notification identifierKey:@"identifierKey"]; }
```

### Delegate Method  findLocalNotificationWithIdentifier

#### 功能说明
API 用于获取自定义的identifierKey标示符的UILocationNotification对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9版后将会被废弃，由FindNotification方法取代，建议及早放弃使用。
</div>

#### 接口定义

```
+ (NSArray *)findLocalNotificationWithIdentifier:(NSString *)notificationKey;

```
#### 参数说明

+ notificationKey  获取通知对象的标示符

#### 调用说明
API返回数组，包含所有和identifierKey匹配的LocalNotification对象，如果没找到，则为一个空的数组对象。

#### 代码示例

```

NSArray *LocalNotifications = [JPUSHService findLocalNotificationWithIdentifier:@"identifierKey"];
```

### Delegate Method  deleteLocalNotification

#### 功能说明
API 用于删除指定的LocalNotification对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9版后将会被废弃，由RemoveNotification方法取代，建议及早放弃使用。
</div>

#### 接口定义

```
+ (void)deleteLocalNotification:(UILocalNotification *)localNotification;
```
#### 参数说明

+ localNotification 删除的本地通知对象

#### 调用说明

API参数localNotification不能为nil.

#### 代码示例

```
[JPUSHService deleteLocalNotification:localNotification];
```

### Delegate Method  deleteLocalNotificationWithIdentifierKey

#### 功能说明
API 用于删除指定所有identifierKey标示符的通知对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9版后将会被废弃，由RemoveNotification方法取代，建议及早放弃使用。
</div>

#### 接口定义
```
+ (void)deleteLocalNotificationWithIdentifierKey:(NSString *)notificationKey;
```

#### 参数说明

+ notificationKey  删除的通知拥有的标示符

#### 调用说明

API参数notificationKey不能为nil.

#### 代码示例
```
[JPUSHService deleteLocalNotificationWithIdentifierKey:@"identifierKey"]; 
```

### Delegate Method  clearAllLocalNotification

#### 功能说明

API 用于清除所有注册的通知
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9版后将会被废弃，由RemoveNotification方法取代，建议及早放弃使用。
</div>

#### 接口定义
```
+ (void)clearAllLocalNotifications;
```

#### 代码示例
```
[JPUSHService clearAllLocalNotifications];
```


## 日志等级设置

### 支持版本
v1.8.0 版本开始

### Method - setDebugMode

#### 功能说明

API 用于开启Debug模式，显示更多的日志信息

#### 接口定义

```
+ (void)setDebugMode;
```
#### 调用说明

当需要了解更多的调试信息时候，调用API开启Debug模式

#### 代码示例

```
[JPUSHService setDebugMode];
```
### Method  setLogOFF

#### 功能说明

API用来关闭日志信息（除了必要的错误信息）

#### 接口定义
```
+ (void)setLogOFF;
```

#### 调用说明

不需要任何调试信息的时候，调用此API （发布时建议调用此API，用来屏蔽日志信息，节省性能消耗)

#### 代码示例

```
[JPUSHService setLogOFF];
```
## 页面的统计

### 支持的版本

r1.7.0 版本开始。

### 功能说明

本 API 用于“用户指定页面使用时长”的统计，并上报到服务器，在 Portal 上展示给开发者。页面统计集成正确，才能够获取正确的页面访问路径、访问深度（PV）的数据。

### API

#### 接口定义

    + (void)startLogPageView:(NSString*)pageName;
    + (void)stopLogPageView:(NSString*)pageName;
    + (void)beginLogPageView:(NSString*)pageName duration:(int)seconds;
    

#### 参数说明

* pageName 需要统计页面自定义名称
* duration 自定义的页面时间

#### 调用说明

应在所有的需要统计得页面得 viewWillAppear 和 viewWillDisappear 加入 startLogPageView 和 stopLogPageView 来统计当前页面的停留时间。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>或者直接使用 beginLogPageView 来自定义加入页面和时间信息。
</div>

### 代码示例

    - (void)viewWillAppear:(BOOL)animated
        {
            [super viewWillAppear:animated];
            [JPUSHService startLogPageView:@"PageOne"];
        }
    - (void)viewWillDisappear:(BOOL)animated 
        {
            [super viewWillDisappear:animated];
            [JPUSHService stopLogPageView:@"PageOne"];
        }   
    －(void)trackView
       {
           [JPUSHService beginLogPageView:@"PageTwo" duration:10];
       }
    


## 地理位置统计

### 支持版本
v1.8.0版本开始

### Method  SetLatitude: longitude

#### 功能说明

API 用于统计用户地理信息

#### 接口定义

```
+ (void)setLatitude:(double)latitude longitude:(double)longitude;
```

#### 参数说明

+ latitude   地理位置纬度
+ longitude  地理位置经度


#### 调用说明

需要加入 CoreLocation.framework库， 并且引入 <CoreLocation/CoreLocation.h\>头文件（#import <CoreLocation/CoreLocation.h \>）

经度和纬度需要开发者自己调用苹果的地理位置信息API获取。

#### 代码示例
```

[JPUSHService setLatitude:100.0 longitude:100.0];
```

### Method  setLocation
#### 功能说明
API用来统计地理位置信息

#### 接口定义
```
+ (void)setLocation:(CLLocation *)location;
```

#### 参数说明

+ location   当前地理位置的CLLocation对象

#### 调用说明

需要加入 CoreLocation.framework库， 并且引入<CoreLocation/CoreLocation.h\>头文件（#import <CoreLocation/CoreLocation.h\>）

CLLocation对象需要开发者自己调用苹果的地理位置信息API获取。

#### 代码示例

```
Build Phases中Link Binary With Libraries添加CoreLocation.framework
应用的plist增加NSLocationAlwaysUsageDescription或NSLocationWhenInUseUsageDescription字段，内容为是否允许alert的内容
 
.h
#import <CoreLocation/CoreLocation.h>
@interface xxx : UIViewController<CLLocationManagerDelegate>
@property(nonatomic, strong) CLLocationManager *currentLoaction;
 
.m
 
- (void)viewDidLoad {
  //注册LocationManager
  _currentLoaction = [[CLLocationManager alloc] init];
  _currentLoaction.delegate = self;
#ifdef __IPHONE_8_0
  if ([[UIDevice currentDevice].systemVersion floatValue] >= 8.0) {
    [_currentLoaction requestAlwaysAuthorization];
  }
#endif
    if ([CLLocationManager locationServicesEnabled]) {
        NSLog(@"您的设备的［设置］－［隐私］－［定位］已开启");
        [_currentLoaction startUpdatingLocation];
    }
    else{
        NSLog(@"您的设备的［设置］－［隐私］－［定位］尚未开启");
  }
}
 
#ifdef __IPHONE_6_0
- (void)locationManager:(CLLocationManager *)manager
     didUpdateLocations:(NSArray *)locations {
  if ([[UIDevice currentDevice].systemVersion floatValue] >= 6.0) {
    CLLocation *newLocation = [locations lastObject];
    float longtitude = newLocation.coordinate.longitude;
    float latitude = newLocation.coordinate.latitude;
    [JPUSHService setLocation:newLocation];
    //[JPUSHService setLatitude:latitude longitude:longtitude];
    [manager stopUpdatingLocation];
  }
}
#endif
 
- (void)locationManager:(CLLocationManager *)manager
    didUpdateToLocation:(CLLocation *)newLocation
           fromLocation:(CLLocation *)oldLocation {
  if ([[UIDevice currentDevice].systemVersion floatValue] < 6.0) {
    float longtitude = newLocation.coordinate.longitude;
    float latitude = newLocation.coordinate.latitude;
    [JPUSHService setLocation:newLocation];
    //[JPUSHService setLatitude:latitude longitude:longtitude];
    [manager stopUpdatingLocation];
  }
}
 
- (void)locationManager:(CLLocationManager *)manager   
       didFailWithError:(NSError *)error{
//获取地理位置错误处理
}
```

## 崩溃日志统计

### 支持版本
v1.8.0版本开始

### Method  crashLogON
#### 功能说明

API 用于统计用户应用崩溃日志

#### 接口定义
```
+ (void)crashLogON;
```

#### 调用说明

如果需要统计Log信息，调用该接口。当你需要自己收集错误信息时，切记不要调用该接口。

#### 代码示例

```
[JPUSHService crashLogON];
```

## 客户端错误码定义
<A NAME="client_error_code"></a>

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >描述</th>
      <th >详细解释</th>
    </tr>
    <tr >
      <td>1005</td>
      <td>AppKey不存在</td>
      <td></td>
    </tr>
    <tr >
      <td>1008</td>
      <td>AppKey非法</td>
      <td>请到官网检查此应用详情中的appkey，确认无误</td>
    </tr>
    <tr >
      <td>1009</td>
      <td>当前appkey无对应应用</td>
      <td>当前的appkey下没有创建iOS应用。请到官网检查此应用的应用详情</td>
    </tr>
        <tr >
      <td>6001</td>
      <td>无效的设置，tag/alias 不应参数都为 null</td>
      <td></td>
    </tr>
    <tr >
      <td>6002</td>
      <td>设置超时</td>
      <td>建议重试</td>
    </tr>
    <tr >
      <td>6003</td>
      <td>alias 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字</td>
    </tr>
    <tr >
      <td>6004</td>
      <td>alias超长。最多 40个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6005</td>
      <td>某一个 tag 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字</td>
    </tr>
    <tr >
      <td>6006</td>
      <td>某一个 tag 超长。一个 tag 最多 40个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6007</td>
      <td>tags 数量超出限制。最多 1000个</td>
      <td>这是一台设备的限制。一个应用全局的标签数量无限制。</td>
    </tr>
    <tr >
      <td>6008</td>
      <td>tag 超出总长度限制</td>
      <td>总长度最多 7K 字节</td>
    </tr>
    <tr >
      <td>6011</td>
      <td>10s内设置tag或alias大于10次</td>
      <td>短时间内操作过于频繁</td>
    </tr>
  </table>
</div>




更多地说明请参考Apple的官方文档






[0]: https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/IPhoneOSClientImp.html#//apple_ref/doc/uid/TP40008194-CH103-SW4
[1]: https://github.com/ylechelle/OpenUDID
