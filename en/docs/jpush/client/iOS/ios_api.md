# iOS API

## Tag and Alias ​​API (iOS)

### Function Description

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">

<p>Tips, please pay attention to deal with the call back results when setting the label alias.

<p>Only if the call back returns a value of 0, you could set successfully and then push to the target. Otherwise the server API will return a 1011 error. All callback functions run on the main thread.
</div>

<br>

Provide several related APIs for manipulating aliases and tags.

These APIs can be called anywhere in the App.

#### Alias

For the user who installed the application, identify the individual name by alias. When the Push message is given to this user later, it can be specified with this alias.

Each user can only specify one alias.

Within the same application, different aliases are recommended for different users. In this way, users are uniquely identified based on their aliases.

The system does not restrict one alias to only one user. If an alias is assigned to more than one user, the server-side API will send messages to multiple users when specifying the alias.

Example: In a game where the user need to log in, it is possible to set the alias as userid. When the game is running, it is found that the user has not played the game for 3 days. Then, the server side API will send a notification to the client to remind the user according to the userid.

#### Tag

Label the user who installed the application. Its purpose is mainly to facilitate developers to deliver Push messages in batches according to labels.

Multiple tags can be played for each user.

Example: game, old\_page, women

### Method - addTags:completion:seq:

Call this API to add tags and return results in block

Note: This interface is to add logic, not override logic

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition
```
+ (void)addTags:(NSSet<NSString *> *)tags
 completion:(JPUSHTagsOperationCompletion)completion
        seq:(NSInteger)seq;
```
#### Parameter Description

-   tags

    -   can not set nil or empty set (\[NSSet set\])

    -   Collection member type need to be NSString type

    -   Set at least one tag for each call

    -   Components of valid labels: letters (case-sensitive), numbers, underscores, kanji, special characters @!\#$&\*+=.\|

    -   Restrictions: Each tag has a limited length of 40 bytes and can support up to 1000 tags, but the total length must not exceed 5K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of app global tags

-   completion

    -   Used for the callback to return the corresponding parameters tags and return the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - setTags:completion:seq:

Call this API to set the label and return the result in the block

Note: This interface is overriding logic, not adding logic. Calling this interface will override all previously labels

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)setTags:(NSSet<NSString *> *)tags
 completion:(JPUSHTagsOperationCompletion)completion
        seq:(NSInteger)seq;
```

#### Parameter Description

-   tags

    -   Can not set nil or empty set (\[NSSet set\])

    -   Collection member type needs to be NSString type

    -   Set at least one tag for each call

    -   Components of valid labels: letters (case-sensitive), numbers, underscores, kanji, special characters @!\#$&\*+=.\|

    -   Restrictions: Each tag has a limited length of 40 bytes and can support up to 1000 tags, but the total length must not exceed 5K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of app global tags

-   completion

    -   Used for the callback to return the corresponding parameters tags and return the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - deleteTags:completion:seq:

Call this API to remove the tag and return the result in the block

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)deleteTags:(NSSet<NSString *> *)tags
 completion:(JPUSHTagsOperationCompletion)completion
        seq:(NSInteger)seq;
``` 

#### Parameter Description

-   tags

    -   Can not set nil or empty set (\[NSSet set\])

    -   Collection member type needs to be NSString type

    -   Delete at least one tag for each call

    -   Components of valid labels: letters (case-sensitive), numbers, underscores, kanji, special characters @!\#$&\*+=.\|

    -   Restrictions: Each tag is limited to 40 bytes in length and supports the deletion of up to 1000 tags, but the total length must not exceed 5 Kbytes. (UTF-8 encoded is required to determine the length)

-   completion

    -   The callback returns the corresponding parameter tags and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - cleanTags:completion:seq:

Call this API to clear all tags and return results in block

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)cleanTags:(JPUSHTagsOperationCompletion)completion
        seq:(NSInteger)seq;
```

#### Parameter Description

-   completion

    -   The tag returned by the callback is nil. Return the corresponding status code: 0 is successful, please refer to the definition of error code for other return codes. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - getAllTags:completion:seq:

Call this API to get all the tags and return the result in the block

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)getAllTags:(JPUSHTagsOperationCompletion)completion
        seq:(NSInteger)seq;
```

seq:(NSInteger)seq;

#### Parameter Description

-   completion

    -   The tags returned by the callback are the result of the query. Return the corresponding status code: 0 is successful, please refer to the definition of error code for other return codes. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - validTag:completion:seq:

Call this API to verify that if the target tag is set

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)validTag:(NSString *)tag
 completion:(JPUSHTagValidOperationCompletion)completion
        seq:(NSInteger)seq;
```

#### Parameter Description

-   tag

    -   Can not set nil or empty string

    -   Components of valid labels: letters (case-sensitive), numbers, underscores, kanji, special characters @!\#$&\*+=.\|

    -   Restrictions: Each tag has a limited length of 40 bytes (UTF-8 encoded is required to determine the length)

-   completion

    -   The callback returns the corresponding parameter tag and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code. Seq is the serial number session passed in at the time of the call

    -   Check the isBind property in the callback to see if it is set. YES is already set

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Tags Block

```
typedef void (^JPUSHTagsOperationCompletion)(NSInteger iResCode, NSSet *iTags, NSInteger seq);
typedef void (^JPUSHTagValidOperationCompletion)(NSInteger iResCode, NSSet *iTags, NSInteger seq, BOOL isBind);
```

### 

### Method - setAlias:completion:seq:

Call this API to set an alias

#### upported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)setAlias:(NSString *)alias
  completion:(JPUSHAliasOperationCompletion)completion
         seq:(NSInteger)seq;
```

#### Parameter Description

-   alias

    -   Cannot set nil or empty string @""

    -   Each call to set a valid alias, overwriting previous settings

    -   Valid aliases are composed of letters (case-sensitive), numbers, underscores, Chinese characters, special characters @!\#$&\*+=.\|

    -   Limitation: The length of alias name is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

-   completion

    -   The callback returns the corresponding parameter alias and the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - deleteAlias:completion:seq:

Call this API to remove the alias and return the result in the block

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)deleteAlias:(JPUSHAliasOperationCompletion)completion
            seq:(NSInteger)seq;
```

#### Parameter Description

-   completion

    -   The tag returned by the callback is nil. Return the corresponding status code: 0 is successful, please refer to the definition of error code for other return codes. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Method - getAlias:completion:seq:

Call this API to query the current alias and return the result in the block

#### Supported Versions

Supported Version: 3.0.6

#### Interface Definition

```
+ (void)getAlias:(JPUSHAliasOperationCompletion)completion
         seq:(NSInteger)seq;
```

seq:(NSInteger)seq;

#### Parameter Description

-   completion

    -   The tags returned by the callback are the result of the query. Return the corresponding status code: 0 is successful, please refer to the definition of error code for other return codes. Seq is the serial number session passed in at the time of the call

-   seq

    -   The serial number passed in on the request will be returned when the callback is made

### Alias Block

```
typedef void (^JPUSHAliasOperationCompletion)(NSInteger iResCode, NSString *iAlias, NSInteger seq);
```

### 

### Method - setTagsWithAlias (with Callback)

Call this API to set up aliases and tags at the same time, to support callback functions.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

After the previous call, if you need to rechange the alias and label, you only need to call this API again

#### Supported Versions

Supported Version: 1.4.0

#### Interface Definition

```
+ (void)setTags:(NSSet *)tags alias:(NSString *)alias callbackSelector:(SEL)cbSelector object:(id)theTarget;
```

#### Parameter Description

-   alias

    -   nil - This call does not set this value.

    -   An empty string (@"") indicates that the previous setting was canceled.

    -   Each call sets a valid alias, overwriting previous settings.

    -   Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Limitation: The length of alias name is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

-   tags

    -   nil - This call does not set this value.

    -   An empty set (\[NSSet set\]) indicates that the previous setting was canceled.

    -   Collection member type needs to be NSString type

    -   Set at least one tag per call, overwriting previous settings, but not adding new settings.

    -   Components of valid labels: letters (case sensitive), numbers, underscore, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Restrictions: Each tag is limited to a 40-byte named length and supports up to 1000 tags, but the total length must not exceed 7K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of global tags in the App.

-   callbackSelector

    -   nil - Callback is not required for this call.

    -   Used to call back the corresponding parameters alias, tags, and return the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code

    -   For callback function, please refer to the implementation of SDK.

-   theTarget

    -   The parameter value is the instance object that implements the callbackSelector.

    -   nil - Callback is not required for this call.

```
-(void)tagsAliasCallback:(int)iResCode
                    tags:(NSSet*)tags
                   alias:(NSString*)alias
{
    NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias);
}
```

### 

### Method - setTagsWithAlias (background)

Call this API to set aliases and tags at the same time in the back-end. No need to process the setting result. The SDK will automatically retry.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

After the previous call, if you need to rechange the alias and label, you only need to call this API again.

It should be noted that the background mode settings and non-background settings are two different settings that do not affect each other, meaning that non-background settings will not terminate the current background setting unless another background setting occurs.

#### Supported Versions

Supported Version: 2.1.0

#### Interface Definition

```
+ (void)setTags:(NSSet *)tags aliasInbackground:(NSString *)alias;
```

#### Parameter Description

-   alias

    -   nil - This call does not set this value.

    -   An empty string (@"") indicates that the previous setting was canceled.

    -   Each call sets a valid alias, overwriting previous settings.

    -   Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Limitation: The length of alias name is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

-   tags

    -   nil - This call does not set this value.

    -   An empty set (\[NSSet set\]) indicates that the previous setting was canceled.

    -   Collection member type needs to be NSString type

    -   Set at least one tag per call, overwriting previous settings but not adding new settings.

    -   Components of valid labels: letters (case sensitive), numbers, underscore, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Restrictions: Each tag is limited to a 40-byte named length and supports up to 1000 tags, but the total length must not exceed 7K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of app global tags


```
[JPUSHService setTags:tags aliasInbackground:alias];
```

### 

### Method - setTagsWithAlias (with block)

Call this API to set up aliases and labels at the same time, and return the result of setting aliases and labels via block.

It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.

After the previous call, if you need to rechange the alias and label, you only need to call this API again.

#### Supported Versions

Supported Version: 2.1.0

#### Interface Definition

```
+ (void)setTags:(NSSet *)tags alias:(NSString *)alias fetchCompletionHandle:(void (^)(int iResCode, NSSet *iTags, NSString *iAlias))completionHandler
```

#### Parameter Description

-   alias

    -   nil - This call does not set this value.

    -   An empty string (@"") indicates that the previous setting was canceled.

    -   Each call sets a valid alias, overwriting previous settings.

    -   Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Limitation: The length of alias name is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

-   tags

    -   nil - This call does not set this value.

    -   An empty set (\[NSSet set\]) indicates that the previous setting was canceled.

    -   Collection member type needs to be NSString type

    -   Set at least one tag per call, overwriting previous settings, but not adding new settings.

    -   Components of valid labels: letters (case sensitive), numbers, underscore, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Restrictions: Each tag is limited to a 40-byte named length and supports up to 1000 tags, but the total length must not exceed 7K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of App global tags.

-   (void (\^)(int iResCode, NSSet *iTags, NSString *iAlias))completionHandler

    -   completionHandler is used to process the result set

    -   iResCode- Result code returned

    -   iTags and iAlias ​​return set tag and alias

```
[JPUSHService setTags:tags alias:alias fetchCompletionHandle:^(int iResCode, NSSet *iTags, NSString *iAlias){
 NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, iTags, iAlias);
}];
```

### 

### Method - setTags

Call this API to set labels and support callback functions.

This method is a simplified version of setTagsWithAlias (with Callback), used only to change the label.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p> Recommendations
<br>
<p> If the alias/tags to be set are dynamic, it is possible that the entire call fails when calling setTagsWithAlias because alias/tags are invalid.
<br>

<p>Calling this method just sets tags to eliminate the effect of possible invalid aliases on this call.

</div>

#### Supported Versions

Supported Version: 1.4.0

#### Interface Definition

```
+ (void)setTags:(NSSet *)tags callbackSelector:(SEL)cbSelector object:(id)theTarget;
```

#### Parameter Description

-   tags

    -   nil - This call does not set this value.

    -   An empty set (\[NSSet set\]) indicates that the previous setting was canceled.

    -   Set at least one tag per call, overwriting previous settings, but not adding new settings.

    -   Components of valid labels: letters (case sensitive), numbers, underscore, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Restrictions: Each tag has a limited length of 40 bytes and can support up to 1000 tags, but the total length must not exceed 7K bytes. (UTF-8 encoded is required to determine the length)

    -   A single device supports up to 1000 tags. There is no limit to the number of App global tags.

-   callbackSelector

    -   nil - Callback is not required for this call.

    -   Used to call back the corresponding parameters alias, tags. And return the corresponding status code: 0 is successful, other return code please refer to the definition of error code.

    -   For callback function, please refer to the SDK implementation.

-   theTarget

-   The parameter value is the instance object that implements the callbackSelector.

-   nil – This Call does not require the callback.


```
- (void)tagsAliasCallback:(int)iResCode tags:(NSSet*)tags alias:(NSString*)alias {
                NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias);}
```

### 

### Method - setAlias

Call this API to set up aliases and support callback functions.

This method is a simplified version of setTagsWithAlias (with Callback) for changing only aliases.

#### Supported versions

Supported version: 1.4.0

#### Interface Definition

```
+ (void)setAlias:(NSString *)alias callbackSelector:(SEL)cbSelector object:(id)theTarget;
```

#### Parameter Description

-   alias

    -   An empty string (@"") indicates that the previous setting was canceled.

    -   Each call sets a valid alias, overwriting previous settings.

    -   Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters (2.1.9 support) @!\#$&\*+=.\|.

    -   Limitation: The length of alias name is limited to 40 bytes. (UTF-8 encoded is required to determine the length)

-   callbackSelector

    -   nil - Callback is not required for this call.

    -   Used to call back the corresponding parameters alias, tags, and return the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code.

    -   For callback function, please refer to the SDK implementation

-   theTarget

    -   The parameter value is the instance object that implements the callbackSelector.

    -   nil - Callback is not required for this call.

```
- (void)tagsAliasCallback:(int)iResCode tags:(NSSet*)tags alias:(NSString*)alias {
        NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias)        }
```

### 

### Method - filterValidTags

Used to filter out the correct available tags

If the total number exceeds the maximum limit, the maximum number of top available tags is returned.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>Recommendations
<br>
 <p>When setting tags, if one of the tags is invalid, the entire setup process fails. 
<br>
 <p>If the app tags are set dynamically during the run and there are invalid characters specified in the JPush SDK tag, it is possible that an invalid tag results in the failure of all tag updates in this call.
<br>
 <p>At this time, you can call this method filterValidTags to filter out invalid tags, get valid tags, and then call JPush SDK's set tags / alias method.
</div>


#### Supported Versions

Supported Version: 1.4.0

#### Interface Definition

```
+ (NSSet*)filterValidTags:(NSSet*)tags;
```

#### Parameter Description

-   tags

    -   Original tag collection

#### Interface return

A valid tag collection.

Reference of return error code: [Definition of Error Code](#client_error_code)

## Get APNs (Notifications) Push Content

### Supported Versions

The initial version

### Function Description

When the iOS device receives a push (APNs), and the user clicks on the push notification to open the application, the application will perform processing according to different statuses. You need to add code to get the apn content in the following two methods in AppDelegate.

-   If the App state is not running, this function will be called. If the launchOptions contains UIApplicationLaunchOptionsRemoteNotificationKey, it indicates that the user clicked on the apn notification to cause the app to start running; if there is no corresponding key value, then the App is not started by clicking on apn, while it may be opened by a direct click on Icon or other.
```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// apn 内容获取：
NSDictionary *remoteNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsRemoteNotificationKey]
```

-   Based on the version iOS 6 and below system, if the App status is in the foreground or click the notification message in the notification bar, then this function will be called. Whether the application is running in the foreground can be determined by whether the application state of the AppDelegate is UIApplicationStateActive. This situation is handled in this function：
```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo;
```

-   Based on version iOS 7 and above system, if you are using iOS 7's Remote Notification feature, the handler function needs to be used.

```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler;
```

-   Based on version iOS 10 and above system, the original \[application: didReceiveRemoteNotification:\] will be discarded by the system and replaced by the \[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:\] or \[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:\] method in the newly added UserNotifications Framework. The JPUSHRegisterDelegate protocol method for SDK encapsulation in versions 2.1.9 and later can be adapted to the new delegate protocol method of iOS 10. That is the following two methods：

```
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(NSInteger))completionHandler; 
// NSDictionary * userInfo = notification.request.content.userInfo; 
// APNs内容为userInfo

- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)())completionHandler; 
// NSDictionary * userInfo = response.notification.request.content.userInfo; 
// APNs内容为userInfo
```

### Code Example
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
- (void)application:(UIApplication *)application didReceiveRemoteNotification:  (NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
     
  NSLog(@"this is iOS7 Remote Notification");
         
  // iOS 10 以下 Required
  [JPUSHService handleRemoteNotification:userInfo];
  completionHandler(UIBackgroundFetchResultNewData);
}

#pragma mark- JPUSHRegisterDelegate // 2.1.9版新增JPUSHRegisterDelegate,需实现以下两个方法

// iOS 10 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center  willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(NSInteger))completionHandler {
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

Reference Document:

[Handling Local and Remote Notifications](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194-CH3-SW1)

## Get Push Content of Custom Message

### Supported Versions

After r1.2.5

### Function Description

The push of a custom message can only be received when the front-end is running.

Get user-push custom message content, titles and additional fields from the jpush server.

### Implementation Method

Getting iOS push content requires registering notifications in the delegate class and implementing callback methods.

Add the following code in method - (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*) launchOptions：

```
    NSNotificationCenter *defaultCenter = [NSNotificationCenter defaultCenter];
    [defaultCenter addObserver:self selector:@selector(networkDidReceiveMessage:) name:kJPFNetworkDidReceiveMessageNotification object:nil];
```

Implement the callback method networkDidReceiveMessage

```
    - (void)networkDidReceiveMessage:(NSNotification *)notification {
        NSDictionary * userInfo = [notification userInfo];
        NSString *content = [userInfo valueForKey:@"content"];
        NSString *messageID = [userInfo valueForKey:@"_j_msgid"];
        NSDictionary *extras = [userInfo valueForKey:@"extras"]; 
        NSString *customizeField1 = [extras valueForKey:@"customizeField1"]; //服务端传递的Extras附加字段，key是自己定义的
     
    }
```

#### Parameter Description：

content：Get push content

extras：Get user-defined parameters

customizeField1： Get a custom value based on the custom key

More implementation, please refer to demo of SDK download package.

## Get RegistrationID

#### Definition of RegistrationID 

When the application that integrates the JPush SDK successfully and registers to the JPush server for the first time, the JPush server will return a unique device identifier, RegistrationID, to the client. The JPush SDK will send the RegistrationID to the application as a broadcast.

The application can save this RegistrationID on its own application server, and then it can push messages or notifications to the device based on the RegistrationID.

### API - registrationIDCompletionHandler:(with block)

#### Supported Versions

Supported Version: 2.1.9

#### Interface Definition

```
+ (void)registrationIDCompletionHandler:(void(^)(int resCode,NSString *registrationID))completionHandler;
```

#### Parameter Description

-   (void(\^)(int resCode,NSString \*registrationID))completionHandler

    -   completionHandler is used to process the result of set

    -   resCode - Result code returned

    -   registrationID- registrationID returned

```
[JPUSHService registrationIDCompletionHandler:^(int resCode, NSString *registrationID) {
    NSLog(@"resCode : %d,registrationID: %@",resCode,registrationID);
}];
```

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>Tips:
  <br>
<p>It is recommended to use this interface to obtain the registrationID. This interface is called in the simulator and the resCode returns 1011. The registrationID returns nil.
</div>


### 

### API - registrationID

Call this API to get the application's corresponding RegistrationID. Only when the application successfully registers to the server of JPush, the corresponding value will be returned, otherwise it returns an empty string

#### Supported Versions

Supported Version: 1.7.0

#### Interface Definition

+(NSString *)registrationID

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">

<p>Tips:

  <br>

<p>Uninstallation and reinstallation of application in iOS 9 system will cause changes to devicetoken returned by APNs, so the developer needs to obtain the device's latest Registration ID. Please call the "RegistrationID" interface in the implementation of kJPFNetworkDidLoginNotification to obtain the RegistrationID.

</div>


### Additional Information

#### Push messages and notifications via RegistrationID

You can use the RegistrationID to push messages and notifications. Refer to the document [Push API v3](../../server/push/rest_api_v3_push/#audience). When the audience parameter is RegistrationID, it can be pushed according to the RegistrationID.

Note： 

To use this feature, the client app must integrate JPush iOS SDK with r1.7.0 and above.

## Set Badge

### Supported Versions

V1.7.4 and later versions

### Function Description

Badge is a number that iOS uses to mark the status of the application and appears in the top right corner of the program icon. JPush encapsulates the badge function, allowing the application to upload the badge value to the JPush server. The JPush background helps manage the corresponding push value of each user, simplifying the operation of setting and pushing the badge.

In practical applications, the developer can directly increase or decrease the value of the badge without having to maintain the correspondence between the user and the badge value.

### API setBadge

Set the badge value stored in the JPush server

#### Interface Definition

```
+ (BOOL)setBadge:(int)value
```

#### Parameter Description

-   Value range: \[0,99999\]

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">

<p>Setting the badge value, the UIApplication:setApplicationIconBadgeNumber function must still be called locally</p>
</div>
<br>

-   Return value

    -   Return TRUE in the value's range, otherwise FALSE will be returned

### API resetBadge

Clear the badge value stored in the JPush server, \[setBadge:0\]

#### Interface Definition
```
+ (void)resetBadge
```
## Local Notification

### Supported Versions

V1.8.0 and later. v2.1.9 is updated

### Function Description

When the user clicks the notification to open the application after his iOS device receives a local notification, the application will process according to the status. You need to add the code in the following two methods in AppDelegate to get the local notification content.

-   If the App state is not running, this function will be called. If the launchOptions contains UIApplicationLaunchOptionsLocalNotificationKey, it indicates that the user clicked on the local notification to cause the app to start running; if there is no corresponding key value, then the App is not started due to clicking local notification, but by a direct Click on the icon or other.

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// 本地通知内容获取：NSDictionary *localNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsLocalNotificationKey]

```

-   If the App state is running in the foreground or in the background, then this function will be called. Whether the program is running in the foreground can be determined by whether the application state of the AppDelegate is UIApplicationStateActive. This situation is handled in this function：

```
// NS_DEPRECATED_IOS(4_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] or -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]")
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification;
// 本地通知为notification
```

-   The above method will be discarded by iOS 10 and above system, replacing by -\[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:\] or -\[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:\] method in the new UserNotifications Framework. For this purpose, the SDK encapsulates the JPUSHRegisterDelegate protocol, and the corresponding protocol method can be implemented to adapt the new delegate method of iOS 10, which is consistent with the above-mentioned remote push new callback method, that is, the following method.：

```
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^) (NSInteger))completionHandler; 
   // if (![notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { 
   // 本地通知为notification 
   // }

- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler: (void (^)())completionHandler; 
  // if (![response.notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { 
  // 本地通知为response.notification 
  // }
``` 

### Method AddNotification

#### Supported Versions

V2.1.9 and later versions

#### Function Description

API is used to register or update push (supports iOS10 and is compatible with iOS10 or lower)

#### Interface Definition

```
+ (void)addNotification:(JPushNotificationRequest *)request;
```

#### Parameter Description

-   request - [JPushNotificationRequest] entity type to pass the properties of push

#### Call Description

Pass the incoming request.requestIdentifier in the request and update the existing push, otherwise the new push is registered.

#### Code Example

```
- (void)testAddNotification {
  JPushNotificationContent *content = [[JPushNotificationContent alloc] init];
  content.title = @"Test Notifications";
  content.subtitle = @"2016";
  content.body = @"This is a test code";
  content.badge = @1;
  content.categoryIdentifier = @"Custom Category Name";
  
  // 5s后提醒 iOS 10 以上支持
  JPushNotificationTrigger *trigger1 = [[JPushNotificationTrigger alloc] init];
  trigger1.timeInterval = 5;
  //每小时重复 1 次 iOS 10 以上支持
  JPushNotificationTrigger *trigger2 = [[JPushNotificationTrigger alloc] init];
  trigger2.timeInterval = 3600;
  trigger2.repeat = YES;
  
  //每周一早上8：00提醒，iOS10以上支持
  NSDateComponents *components = [[NSDateComponents alloc] init];
  components.weekday = 2;
  components.hour = 8;
  JPushNotificationTrigger *trigger3 = [[JPushNotificationTrigger alloc] init];
  trigger3.dateComponents = components;
  trigger3.repeat = YES;
  
  //#import <CoreLocation/CoreLocation.h>
  //一到某地点提醒，iOS8以上支持
  CLRegion *region = [[CLRegion alloc] initCircularRegionWithCenter:CLLocationCoordinate2DMake(0, 0) radius:0 identifier:@"test"];
  JPushNotificationTrigger *trigger4 = [[JPushNotificationTrigger alloc] init];
  trigger4.region = region;
  
  //5s后提醒，iOS10以下支持
  JPushNotificationTrigger *trigger5 = [[JPushNotificationTrigger alloc] init];
  trigger5.fireDate = [NSDate dateWithTimeIntervalSinceNow:5];

  JPushNotificationRequest *request = [[JPushNotificationRequest alloc] init];
  request.requestIdentifier = @"sampleRequest";
  request.content = content;
  request.trigger = trigger1;//trigger2;//trigger3;//trigger4;//trigger5;
  request.completionHandler = ^(id result) {
    NSLog(@"结果返回：%@", result);
  };
  [JPUSHService addNotification:request];
}

```

### Method RemoveNotification

#### Supported Versions

V2.1.9 and later versions

#### Function Description

The API is used to remove pushes that are to be pushed or displayed in the notification center (supports iOS10 and is compatible with iOS10 or lower)

#### Interface Definition

```
+ (void)removeNotification:(JPushNotificationIdentifier *)identifier;
```
#### Parameter Description

-   identifier - [JPushNotificationIdentifier] entity type

#### Call Description

-   If identifier in the iOS10 or later is set to nil, remove all push and push request displayed in the notification center. You can also remove the corresponding push or push request in the notification center by setting identifier.delivered and identifier.identifiers. If set identifier.identifiers to nil or an empty array, remove all push or push requests in the notification center under the corresponding flag; if identifier in the iOS10 or less is set to nil, then remove all pushes since the property of identifier.delivered is invalid. You can also remove this push by the identifier.notificationObj passing into a specific push object

-   Code Example

```
- (void)testRemoveNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = YES;  //iOS10以上有效，等于YES则在通知中心显示的里面移除，等于NO则为在待推送的里面移除；iOS10以下无效
  [JPUSHService removeNotification:identifier];
}


- (void)testRemoveAllNotification {
  [JPUSHService removeNotification:nil];  // iOS10以下移除所有推送；iOS10以上移除所有在通知中心显示推送和待推送请求

//  //iOS10以上支持
//  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
//  identifier.identifiers = nil;
//  identifier.delivered = YES;  //等于YES则移除所有在通知中心显示的，等于NO则为移除所有待推送的
//  [JPUSHService removeNotification:identifier];
}
```

### Method FindNotification

#### Supported Versions

V2.1.9 and later versions

#### Function Description

API is used to find push (supports iOS10 and is compatible with iOS10 and below)

#### Interface Definition

```
+ (void)findNotification:(JPushNotificationIdentifier *)identifier;
```

#### Parameter Description

-   identifier - \[JPushNotificationIdentifier\] entity type

#### Call Description

-   In iOS10 or above, you can find the corresponding push or push request in Notification Center by setting identifier.delivered and identifier.identifiers. If the identifier.identifiers is set to nil or an empty array, all the push or push request under the corresponding flag will be displayed in the notification center. identifier.delivered property is invalid in iOS10 or below, and identifier.identifiers returns all pushes if nil or empty array is set.

-   You must set the identifier.findCompletionHandler callback to get the search result. Return an array of corresponding objects by (NSArray \*results).

#### Code Example

```
- (void)testFindNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = YES;  //iOS10以上有效，等于YES则在通知中心显示的里面查找，等于NO则在待推送的里面查找；iOS10以下无效
  identifier.findCompletionHandler = ^(NSArray *results) {
  NSLog(@"返回结果为：%@", results); // iOS10以下返回UILocalNotification对象数组，iOS10以上根据delivered传入值返回UNNotification或UNNotificationRequest对象数组
};
  [JPUSHService findNotification:identifier];
}

- (void)testFindAllNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = nil;
  identifier.delivered = YES;  //iOS10以上有效，等于YES则查找所有在通知中心显示的，等于NO则为查找所有待推送的；iOS10以下无效
  identifier.findCompletionHandler = ^(NSArray *results) {
  NSLog(@"返回结果为：%@", results); // iOS10以下返回UILocalNotification对象数组，iOS10以上根据delivered传入值返回UNNotification或UNNotificationRequest对象数组
};
  [JPUSHService findNotification:identifier];
}
```

### Method SetLocalNotification

#### Function Description

API is used to register local notifications

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
V2.1.9 will be deprecated and replaced by AddNotification method. It is recommended to abandon the use as soon as possible.
</div>




#### Interface Definition

```
+ (UILocalNotification *)setLocalNotification:(NSDate *)fireDate
                                    alertBody:(NSString *)alertBody
                                        badge:(int)badge
                                  alertAction:(NSString *)alertAction
                                identifierKey:(NSString *)notificationKey
                                     userInfo:(NSDictionary *)userInfo
                                    soundName:(NSString *)soundName;
```

New parameters of iOS8 use the API. Non-iOS8 version or do not need to use iOS8 new features, please use the above API

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

#### Parameter Description

-   fireDate - Time triggered local push

-   alertBody - content of local push needs to be displayed

-   badge - The number of badges. If you do not need to change the corner mark -1

-   alertAction - The content displayed by the button in the alertAction popup (iOS 8 defaults to "Open", other defaults to "Start")

-   notificationKey - Local push identifier

-   userInfo - Custom parameters that can be used to identify pushes and add additional information

-   soundName - Sound name setting of local notification, empty defaults sound

-   region

-   regionTriggersOnce

-   category

#### Call Description

fireDate must be greater than the current time and cannot be empty at the same time. Number of registration notices must be less than 64

#### Code Example

```
[JPUSHService setLocalNotification:[NSDate dateWithTimeIntervalSinceNow:100]
                      alertBody:@"alert content"
                          badge:1
                    alertAction:@"buttonText"
                  identifierKey:@"identifierKey"
                       userInfo:nil
                      soundName:nil];
```

### Method showLocalNotificationAtFront

#### Function Description

The API is used to display the notification when the APP is running in the foreground. (Style is UIAlertView)

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
The following iOS10 can continue to use, iOS10 or more in the \[JPUSHRegisterDelegate jpushNotificationCenter:willPresentNotification:withCompletionHandler:\] method calls completionHandler (UNNotificationPresentationOptionSound \| UNNotificationPresentationOptionAlert); Yes, it will be abandoned after v2.1.9, it is recommended to give up early.
</div>


#### Interface Definition

```
+ (void)showLocalNotificationAtFront:(UILocalNotification *)notification
                       identifierKey:(NSString *)notificationKey;
```

#### Parameter Description

-   notification - UILocalNotification currently triggered

-   notificationKey - Filter notifications that do not need to be displayed in the foreground. Only the notification of the notificationKey identifier will be displayed in the foreground. If all need to be displayed, this parameter is passed nil.

#### Call Description

The API must be placed in - (void)application:(UIApplication \*)application didReceiveLocalNotification:(UILocalNotification \*)notification(AppDelegate.m) Apple's callback function.

#### Code Example

```
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification { [JPUSHService showLocalNotificationAtFront:notification identifierKey:@"identifierKey"]; }
```

### 

### Delegate Method findLocalNotificationWithIdentifier

#### Function Description

API is used to get UILocationNotification object of custom identifierKey identifier

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
Version 2.1.9 will be deprecated and replaced by FindNotification method. It is recommended to give up as soon as possible.
</div>

#### Interface Definition

```
+ (NSArray *)findLocalNotificationWithIdentifier:(NSString *)notificationKey;
```

#### Parameter Description

-   notificationKey - Identifier of the notification object

#### Call Description

The API returns an array containing all LocalNotification objects that match the identifierKey, or an empty array object if not found

#### Code Example

```
NSArray *LocalNotifications = [JPUSHService findLocalNotificationWithIdentifier:@"identifierKey"];
```

### Delegate Method deleteLocalNotification

#### Function Description

API is used to delete a specified LocalNotification object

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
V2.1.9 will be deprecated and replaced by RemoveNotification method. It is recommended to abandon the use as soon as possible.
</div>

#### Interface Definition

```
+ (void)deleteLocalNotification:(UILocalNotification *)localNotification;
```

#### Parameter Description

-   localNotification - Local notification object which is deleted

#### Call Description

The API parameter localNotification cannot be nil.

#### Code Example

```
[JPUSHService deleteLocalNotification:localNotification];
```

### Delegate Method deleteLocalNotificationWithIdentifierKey

#### Function Description

API is used to delete notification objects that specify all identifierKey identifiers

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
V2.1.9 will be obsolete and replaced by RemoveNotification method. It is recommended to give up early
</div>

#### Interface Definition

```
+ (void)deleteLocalNotificationWithIdentifierKey:(NSString *)notificationKey;
```

#### Parameter Description

notificationKey - Identifier of the deleted notification

**Call Description**

API parameter notificationKey cannot be nil.

#### Code Example

```
[JPUSHService deleteLocalNotificationWithIdentifierKey:@"identifierKey"]; 
```

### Delegate Method clearAllLocalNotification

#### Function Description

API is used to clear all registered notifications

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
V2.1.9 will be deprecated and replaced by RemoveNotification method. It is recommended to give up early.
</div>

#### Interface Definition

```
+ (void)clearAllLocalNotifications;
```

#### Code Example
```
[JPUSHService clearAllLocalNotifications];
```

## Level Settings of Log

### Supported Versions

From V1.8.0 version

### Method - setDebugMode

#### Function Description

API is used to enable Debug mode and display more log information

#### Interface Definition

```
+ (void)setDebugMode;
```

#### Call description

When you need to know more debugging information, call API to enable Debug mode

#### Code Example

```
[JPUSHService setDebugMode];
```

### 

### Method setLogOFF

#### Function Description

API used to turn off log information (except for necessary error messages)

#### Interface Definition

```
+ (void)setLogOFF;
```

#### Call Description

Call this API when there is no need for any debugging information (It is recommended to call this API at the time of publishing to shield log information and save performance)

#### Code Example

```
[JPUSHService setLogOFF];
```
## Page Statistics

### Supported Versions

From R1.7.0 version

### Function Description

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">

This API is used to count "user-specified page usage time", reports it to the server, and shows it to developers on the portal. The page statistics integration is correct, can developers obtain the correct data of page access path and access depth (PV).

</div>


### API

#### Interface Definition

```
+ (void)startLogPageView:(NSString*)pageName;
+ (void)stopLogPageView:(NSString*)pageName;
+ (void)beginLogPageView:(NSString*)pageName duration:(int)seconds;
```

#### Parameter Description

-   pageName - custom name of pages need to be counted

-   duration - custom page time

#### Call Description

viewWillAppear and viewWillDisappear of all the pages that need to be counted should have startLogPageView and stopLogPageView added to count the dwell time of current pages.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">

<p>Or simply use beginLogPageView to define the information of joined page and time.
</div>

### Code Example

```
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
```

## Geographical Statistics

### Supported Versions

From V1.8.0 version

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
On iOS11, the original NSLocationAlwaysUsageDeion was demoted to NSLocationWhenInUseUsageDeion. Therefore, you need to configure NSLocationAlwaysAndWhenInUseUsageDeion in the plist file. Then the system will pop up a prompt window when you get the positioning. It is recommended that the old and new key values be configured in the plist.
</div>


### Method SetLatitude: longitude

#### Function Description

The API is used to count user geographic information.

#### Interface Definition

```
+ (void)setLatitude:(double)latitude longitude:(double)longitude;
```

#### Parameter Description

-   latitude

-   longitude

#### Call description

Need to join the CoreLocation.framework library, and introduce the <CoreLocation/CoreLocation.h> header file (#import \<CoreLocation/CoreLocation.h >)

Longitude and latitude will be obtained by the developer to call their Apple's geolocation information API.

#### Code Example

```
[JPUSHService setLatitude:100.0 longitude:100.0];
```

### Method setLocation

#### Function Description

API is used to count geographic information

#### Interface Definition
```
+ (void)setLocation:(CLLocation *)location;
```

#### Parameter Description

-   location - CLLocation object of the current location

#### Call Description

Need to join CoreLocation.framework library, and import <CoreLocation/CoreLocation.h> header file (#import <CoreLocation/CoreLocation.h>)

The CLLocation object will be obtained by the developer to call Apple's geolocation information API.

#### Code Example

```
Build Phases中Link Binary With Libraries添加CoreLocation.framework
应用的plist增加NSLocationAlwaysUsageDescription或NSLocationWhenInUseUsageDescription字段，内容为是否允许alert的内容
 
#import <CoreLocation/CoreLocation.h>
@interface xxx : UIViewController<CLLocationManagerDelegate>
@property(nonatomic, strong) CLLocationManager *currentLoaction;
 
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

## Crash Log Statistics

### Supported Versions

From V1.8.0 version

### Method crashLogON

#### Function Description

API is used to count crash logs of user application

#### Interface Definition

```
+ (void)crashLogON;
```

#### Call Description

If you need to count Log information, please call this interface. When you need to collect error information yourself, remember not to call this interface.

#### Code Example

```
[JPUSHService crashLogON];
```
## Set the Phone Number

### Supported Versions

From V3.0.8 version

### Function Description

Used for SMS supplement function. After the mobile phone number is set, the notification mode of “Not Pushing to SMS” can be implemented to increase the rate of delivery.

#### Interface Definition

```
+ (void)setMobileNumber:(NSString *)mobileNumber completion:(void (^)(NSError *error))completion
```

#### Parameter Description

-   mobileNumber - It can only start with a "+" or a digit, and the following content can only contain a "-" and a digit, with its length cannot exceeding 20. If nil or empty string is passed, the number binding operation is cancelled.

-   completion - Response callback. It means success if error is empty, and it means failure if error contains an error code and error information. For the details of the error code, refer to the definition of the error code.

#### Call Description

There is a limit to the frequency of this interface call, up to three times within 10 seconds. It is recommended to call this interface after successful login. The result information is returned asynchronously by completion, or you can set completion to nil without processing the result information.

#### Code Example

```
[JPUSHService setMobileNumber:@"xxx" completion:^(NSError *error) {
        if (error) {
          NSLog(@"error:%@", error);
        }
        else {
        	// success
        }
      }];
```

## Related Interfaces of Notification Service Extension

### Supported Versions

Notification Service Extension SDK v1.0.0 (posted with JPush iOS SDK 3.0.7) and later

### Function Description

Using the Notification Service Extension SDK to report push delivery

### jpushSetAppkey:

Must be called in advance when setting the appkey interface.

#### Interface Definition

```
+ (void)jpushSetAppkey:(NSString *)appkey
```

#### Parameter Description

-   appkey needs to be consistent with the appkey of the JPush SDK in the main app

### jpushReceiveNotificationRequest:with:

The message is delivered to the statistics interface, and the interface is called to report the JPush related data in the APNs message body.

#### Interface Definition

```
+ (void)jpushReceiveNotificationRequest:(UNNotificationRequest *)request with:(void (^)(void))completion
```

#### Parameter Description

-   request UNNotificationRequest

-   completion - reporting callback of message delivery. Please perform operations such as displaying APNs in the callback

### setLogOff

Close log. It defaults to turned on by default, It is recommended to close it during release to reduce unnecessary IO

#### Interface Definition

```
+ (void)setLogOff
```

**Definition of Client Error Code **

| **Code** | **Description**                                                                                         | **Detailed Explanation**                                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1005     | AppKey does not exist                                                                                   |                                                                                                                                                        |
| 1008     | AppKey is illegal                                                                                       | Please go to the official website to check the appkey in this app details and confirm it is correct                                                    |
| 1009     | The current appkey has no corresponding application                                                     | There is no iOS application created under the current appkey. Please go to the official website to check the application details of this application   |
| 6001     | Invalid setting, tag/alias should not be null                                                           |                                                                                                                                                        |
| 6002     | Set timeout                                                                                             | Recommend to try again                                                                                                                                 |
| 6003     | Alias string is illegal                                                                                 | Valid aliases, labels consist of: letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\| |
| 6004     | Alias is too long. Up to 40 bytes                                                                       | Chinese UTF-8 is 3 bytes                                                                                                                               |
| 6005     | One of the tag strings is illegal                                                                       | Valid aliases, labels consist of: letters (case-sensitive), numbers, underscores, Chinese characters, special characters (2.1.9 support) @!\#$&\*+=.\| |
| 6006     | One tag is extremely long. One tag cannot exceed 40 bytes                                               | Chinese UTF-8 is 3 bytes                                                                                                                               |
| 6007     | The number of tags exceeds the limit. Up to 1000                                                        | This is the limitation of a device. There is no limit to the number of tags that can be applied globally.                                              |
| 6008     | Tag exceeds total length limit                                                                          | Total length up to 7K bytes                                                                                                                            |
| 6009     | Unknown mistake                                                                                         | Unexpected exception occurred in SDK                                                                                                                   |
| 6011     | Set tag or alias greater than 10 times within 10s, or set mobile number greater than 3 times within 10s | Operation is too frequent in a short time                                                                                                              |
| 6012     | Set tag or alias or mobile phone number in JPush service stop state                                     | Developers can do relevant processing or hints based on this error code information                                                                    |
| 6013     | Time axis of user device is abnormal                                                                    | Abnormal changes to the device's local timeline affect the setting of mobile numbers                                                                   |
| 6014     | Request busy                                                                                            | The request frequency is too high. This request failed. Please re-initiate the request.                                                                |
| 6015     | Blacklist                                                                                               | Users are blacklisted                                                                                                                                  |
| 6016     | This user is invalid                                                                                    | Failed user request failed                                                                                                                             |
| 6017     | This request is invalid                                                                                 | This request has an unexpected parameter and the request is invalid                                                                                    |
| 6018     | Too many Tags                                                                                           | The user tags have been more than 1000 and cannot be set                                                                                               |
| 6019     | Failed to get Tags                                                                                      | An exception occurred while getting all tags                                                                                                           |
| 6020     | Request failed                                                                                          | A special issue caused the request to fail                                                                                                             |
| 6021     | Tags operation is in progress                                                                           | The last tag request is still waiting for a response, so the next request is temporarily unable to execute                                             |
| 6022     | Alias operation is in progress                                                                          | The last alias request is still waiting for a response, so the next request is temporarily unable to execute                                           |
| 6023     | Invalid mobile phone number                                                                             | Can only start with a "+" or number, and the following content can only contain "-" and numbers                                                        |
| 6024     | Internal error of server                                                                                | Internal error of server, try again after some time                                                                                                    |
| 6025     | Phone number is too long                                                                                | The phone number is too long. The current maximum length of mobile phone number detected by Jiguang is 20                                              |

For more instructions, please refer to Apple's official documentation.
