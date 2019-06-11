# iOS API
## 标签与别名 API（iOS）

### 功能说明

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示，设置标签别名请注意处理 call back 结果。
<p>只有 call back 返回值为 0 才设置成功，才可以向目标推送。否则服务器 API 会返回 1011 错误。所有回调函数都在主线程运行。
</div>

<br>

提供几个相关 API 用来操作别名（alias）与标签（tags）。

这几个 API 可以在 App 里任何地方调用。

#### 别名 alias

为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。  
每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，服务器端 API 会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用服务器端 API 发通知到客户端提醒用户。

#### 标签 tag

为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page, women


### Method - addTags:completion:seq:

调用此 API 来增加标签，在 block 中返回结果

Note：这个接口是增加逻辑，而不是覆盖逻辑

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)addTags:(NSSet<NSString *> *)tags
     completion:(JPUSHTagsOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* tags

    * 不能设置 nil 或者空集合（[NSSet set]）
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少设置一个 tag
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过 5 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制

* completion 

    * 用于回调返回对应的参数 tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回

### Method - setTags:completion:seq:

调用此 API 来设置标签，在 block 中返回结果

Note：这个接口是覆盖逻辑，而不是增加逻辑，调用此接口会覆盖之前设置的全部标签

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)setTags:(NSSet<NSString *> *)tags
     completion:(JPUSHTagsOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* tags

    * 不能设置 nil 或者空集合（[NSSet set]）
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少设置一个 tag
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过 5 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制

* completion 

    * 用于回调返回对应的参数 tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - deleteTags:completion:seq:

调用此 API 来删除标签，在 block 中返回结果

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)deleteTags:(NSSet<NSString *> *)tags
     completion:(JPUSHTagsOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* tags

    * 不能设置 nil 或者空集合（[NSSet set]）
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少删除一个 tag
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持删除 1000 个 tag，但总长度不得超过 5 K 字节。（判断长度需采用 UTF-8 编码）

* completion 

    * 回调返回对应的参数 tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - cleanTags:completion:seq:

调用此 API 来清除所有标签，在 block 中返回结果

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)cleanTags:(JPUSHTagsOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* completion 

    * 回调返回的 tags 为 nil。返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - getAllTags:completion:seq:

调用此 API 来获取所有标签，在 block 中返回结果

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)getAllTags:(JPUSHTagsOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* completion 

    * 回调返回的 tags 为查询结果。返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - validTag:completion:seq:

调用此 API 来验证目标 tag 是否已经设置

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)validTag:(NSString *)tag
     completion:(JPUSHTagValidOperationCompletion)completion
            seq:(NSInteger)seq;
    
#### 参数说明

* tag

    * 不能设置 nil 或者空字符串
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|
    * 限制：每个 tag 命名长度限制为 40 字节（判断长度需采用 UTF-8 编码）

* completion 

    * 回调返回对应的参数 tag。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号
    * 在回调中查看 isBind 属性查看是否已经设置，YES 为已经设置

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Tags Block 
	typedef void (^JPUSHTagsOperationCompletion)(NSInteger iResCode, NSSet *iTags, NSInteger seq);
	typedef void (^JPUSHTagValidOperationCompletion)(NSInteger iResCode, NSSet *iTags, NSInteger seq, BOOL isBind);
        
### Method - setAlias:completion:seq:

调用此 API 来设置别名

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)setAlias:(NSString *)alias
      completion:(JPUSHAliasOperationCompletion)completion
             seq:(NSInteger)seq;
    
#### 参数说明

- alias
    - 不能设置 nil 或者空字符串 @""
    - 每次调用设置有效的别名，覆盖之前的设置
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）
    
* completion 
	
    * 回调返回对应的参数 alias。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - deleteAlias:completion:seq:

调用此 API 来删除别名，在 block 中返回结果

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)deleteAlias:(JPUSHAliasOperationCompletion)completion
                seq:(NSInteger)seq;
    
#### 参数说明

* completion 

    * 回调返回的 tags 为 nil。返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Method - getAlias:completion:seq:

调用此 API 来查询当前别名，在 block 中返回结果

#### 支持的版本

开始支持的版本：3.0.6

#### 接口定义

    + (void)getAlias:(JPUSHAliasOperationCompletion)completion
             seq:(NSInteger)seq;
    
#### 参数说明

* completion 

    * 回调返回的 tags 为查询结果。返回对应的状态码：0 为成功，其他返回码请参考错误码定义。seq 为调用时传入的会话序列号

* seq

    * 请求时传入的序列号，会在回调时原样返回
    
### Alias Block 
	typedef void (^JPUSHAliasOperationCompletion)(NSInteger iResCode, NSString *iAlias, NSInteger seq);

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
    - 空字符串（@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过 7 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* callbackSelector 

    * nil 此次调用不需要 Callback。
    * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。
    * 回调函数请参考 SDK 实现。

* theTarget

    * 参数值为实现了 callbackSelector 的实例对象。
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

需要注意，该 background 模式的设置和非 background 的设置是两种不同的设置，互相不影响，意味着，非 background 的设置不会终止当前进行的 background 设置，除非另一个 background 设置发生。

#### 支持的版本

开始支持的版本：2.1.0

#### 接口定义

```
+ (void)setTags:(NSSet *)tags aliasInbackground:(NSString *)alias;
```

#### 参数说明

- alias
    - nil 此次调用不设置此值。
    - 空字符串（@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过 7 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

```
[JPUSHService setTags:tags aliasInbackground:alias];
```

### Method - setTagsWithAlias (with block)

调用此 API 来同时设置别名与标签，通过 block 来返回设置别名与标签的结果。

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
    - 空字符串（@""）表示取消之前的设置。
    - 每次调用设置有效的别名，覆盖之前的设置。
    - 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    - 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）

* tags

    * nil 此次调用不设置此值。
    * 空集合（[NSSet set]）表示取消之前的设置。
    * 集合成员类型要求为 NSString 类型
    * 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个 tag，但总长度不得超过 7 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* (void (^)(int iResCode, NSSet *iTags, NSString *iAlias))completionHandler
    
    * completionHandler 用于处理设置返回结果
    * iResCode 返回的结果状态码
    * iTags 和 iAlias 返回设置的 tag 和 alias

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
    * 有效的标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
    * 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 1000 个tag，但总长度不得超过 7 K 字节。（判断长度需采用 UTF-8 编码）
    * 单个设备最多支持设置 1000 个 tag。App 全局 tag 数量无限制。

* callbackSelector

    * nil 此次调用不需要 Callback。
    * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。
    * 回调函数请参考 SDK 实现。

* theTarget

   * 参数值为实现了 callbackSelector 的实例对象。
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
     * 空字符串（@""）表示取消之前的设置。
     * 每次调用设置有效的别名，覆盖之前的设置。
     * 有效的别名组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|。
     * 限制：alias 命名长度限制为 40 字节。（判断长度需采用 UTF-8 编码）
* callbackSelector 
     * nil 此次调用不需要 Callback。
     * 用于回调返回对应的参数 alias, tags。并返回对应的状态码：0 为成功，其他返回码请参考错误码定义。
     * 回调函数请参考 SDK 实现。
* theTarget


     * 参数值为实现了 callbackSelector 的实例对象。
     * nil 此次调用不需要 Callback。

```
    - (void)tagsAliasCallback:(int)iResCode tags:(NSSet*)tags alias:(NSString*)alias {
            NSLog(@"rescode: %d, \ntags: %@, \nalias: %@\n", iResCode, tags , alias)        }
```

### Method - filterValidTags

用于过滤出正确可用的 tags。

如果总数量超出最大限制则返回最大数量的靠前的可用 tags。

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

iOS 设备收到一条推送（APNs），用户点击推送通知打开应用时，应用程序根据状态不同进行处理需在 AppDelegate 中的以下两个方法中添加代码以获取 apn 内容

* 如果 App 状态为未运行，此函数将被调用，如果 launchOptions 包含 UIApplicationLaunchOptionsRemoteNotificationKey 表示用户点击 apn 通知导致 app 被启动运行；如果不含有对应键值则表示 App 不是因点击 apn 而被启动，可能为直接点击 icon 被启动或其他。

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// apn 内容获取：
NSDictionary *remoteNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsRemoteNotificationKey]
```

* 基于 iOS 6 及以下的系统版本，如果 App 状态为正在前台或者点击通知栏的通知消息，那么此函数将被调用，并且可通过 AppDelegate 的 applicationState 是否为 UIApplicationStateActive 判断程序是否在前台运行。此种情况在此函数中处理：

```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo;
```
* 基于 iOS 7 及以上的系统版本，如果是使用 iOS 7 的 Remote Notification 特性那么处理函数需要使用

```
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler;
```
* 基于 iOS 10 及以上的系统版本，原 [application: didReceiveRemoteNotification:] 将会被系统废弃，  
由新增 UserNotifications Framework中的[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:]  
 或者 [UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:] 方法替代。  
在 2.1.9 版本及以上可实现 SDK 封装的 JPUSHRegisterDelegate 协议方法，适配 iOS10 新增的 delegate 协议方法。  
即以下两个方法：

```
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(NSInteger))completionHandler; 
// NSDictionary * userInfo = notification.request.content.userInfo; 
// APNs 内容为 userInfo

- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)())completionHandler; 
// NSDictionary * userInfo = response.notification.request.content.userInfo; 
// APNs 内容为 userInfo
```

### 示例代码

```
// NS_DEPRECATED_IOS(3_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] or -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:] for user visible notifications and -[UIApplicationDelegate application:didReceiveRemoteNotification:fetchCompletionHandler:] for silent remote notifications")
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo {
  // 取得 APNs 标准信息内容
  NSDictionary *aps = [userInfo valueForKey:@"aps"];
  NSString *content = [aps valueForKey:@"alert"]; //推送显示的内容
  NSInteger badge = [[aps valueForKey:@"badge"] integerValue]; //badge 数量
  NSString *sound = [aps valueForKey:@"sound"]; //播放的声音
         
  // 取得 Extras 字段内容
  NSString *customizeField1 = [userInfo valueForKey:@"customizeExtras"]; //服务端中 Extras 字段，key 是自己定义的
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

#pragma mark- JPUSHRegisterDelegate // 2.1.9 版新增JPUSHRegisterDelegate,需实现以下两个方法

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
  completionHandler(UNNotificationPresentationOptionAlert); // 需要执行这个方法，选择是否提醒用户，有 Badge、Sound、Alert 三种类型可以选择设置
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

* 基于iOS12以上的版本，UserNotifications Framework新增回调方法[userNotificationCenter:openSettingsForNotification:],在3.1.1及以上版本JPUSHRegisterDelegate同样新增了对应的回调方法。当从应用外部通知界面或通知设置界面进入应用时，该方法将回调。

```
// iOS 12 Support
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center openSettingsForNotification:(UNNotification *)notification{
  if (notification) {
    //从通知界面直接进入应用
  }else{
    //从通知设置界面进入应用
  }
}
```


参考文档：[Handling Local and Remote Notifications][0]

## 获取自定义消息推送内容
<a name="message"></a>

### 支持的版本

r1.2.5 以后。

### 功能说明

只有在前端运行的时候才能收到自定义消息的推送。

从 JPush 服务器获取用户推送的自定义消息内容和标题以及附加字段等。

### 实现方法

获取 iOS 的推送内容需要在 delegate 类中注册通知并实现回调方法。

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
        NSString *messageID = [userInfo valueForKey:@"_j_msgid"];
        NSDictionary *extras = [userInfo valueForKey:@"extras"]; 
        NSString *customizeField1 = [extras valueForKey:@"customizeField1"]; //服务端传递的 Extras 附加字段，key 是自己定义的  
    }
```

#### 参数描述：

content：获取推送的内容

messageID：获取推送的 messageID（key 为 @"_j_msgid"）

extras：获取用户自定义参数

customizeField1：根据自定义 key 获取自定义的 value

更多实现参考[ SDK 下载压缩包](https://docs.jiguang.cn/jpush/resources/)中的 demo。

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
	+ completionHandler 用于处理设置返回结果
	+ resCode 返回的结果状态码
	+ registrationID 返回 registrationID

```
[JPUSHService registrationIDCompletionHandler:^(int resCode, NSString *registrationID) {
    NSLog(@"resCode : %d,registrationID: %@",resCode,registrationID);
}];
```

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示：
  <br>
<p>建议使用此接口获取 registrationID，模拟器中调用此接口 resCode 返回 1011，registrationID 返回 nil。
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
<p>iOS 9 系统，应用卸载重装，APNs 返回的 devicetoken 会发生变化，开发者需要获取设备最新的 Registration id。请在 kJPFNetworkDidLoginNotification 的实现方法里面调用 "RegistrationID" 这个接口来获取 RegistrationID。
</div>

### 附加说明

#### 通过 RegistrationID 推送消息和通知

可以通过 RegistrationID 来推送消息和通知， 参考文档 [Push API v3](../../server/push/rest_api_v3_push/#audience)， 当 audience 参数为 RegistrationID 时候即可根据  RegistrationID 推送。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>注：要使用此功能，客户端 App 一定要集成有 r1.7.0 及以上版本的 JPush iOS SDK
</div>

## 设置 Badge

### 支持的版本

v1.7.4 及后续版本

### 功能说明

badge 是 iOS 用来标记应用程序状态的一个数字，出现在程序图标右上角。
JPush 封装 badge 功能，允许应用上传 badge 值至 JPush 服务器，由 JPush 后台帮助管理每个用户所对应的推送 badge 值，简化了设置推送 badge 的操作。

实际应用中，开发者可以直接对 badge 值做增减操作，无需自己维护用户与 badge 值之间的对应关系。
推送消息时，只需[设置角标 +1](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#notification)，极光会在服务器中存储的每个用户的 badge 值上自动 +1 后下发给用户。

### API setBadge

设置 JPush 服务器中存储的 badge 值

#### 接口定义

```
+ (BOOL)setBadge:(int)value
```
#### 参数说明

* value 取值范围：[0,99999]

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>本地仍须调用 UIApplication:setApplicationIconBadgeNumber 函数设置图标上显示的 badge 值
</div>

<br>

* 返回值 
     * 在 value 的取值区间内返回 TRUE，否则返回 FALSE

### API resetBadge

清空 JPush 服务器中存储的 badge 值，即 [setBadge:0]

#### 接口定义

```
+ (void)resetBadge
```


## 本地通知

### 支持的版本

v1.8.0 及后续版本，v2.1.9 版本有更新

### 功能说明


iOS 设备收到一条本地通知，用户点击通知打开应用时，应用程序根据状态不同进行处理需在 AppDelegate 中的以下两个方法中添加代码以获取本地通知内容

+ 如果 App 状态为未运行，此函数将被调用，如果 launchOptions 包含 UIApplicationLaunchOptionsLocalNotificationKey 表示用户点击本地通知导致 app 被启动运行；如果不含有对应键值则表示 App 不是因点击本地通知而被启动，可能为直接点击 icon 被启动或其他。

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions; 
// 本地通知内容获取：NSDictionary *localNotification = [launchOptions objectForKey: UIApplicationLaunchOptionsLocalNotificationKey]
```

+ 如果 App 状态为正在前台或者后台运行，那么此函数将被调用，并且可通过 AppDelegate的applicationState 是否为 UIApplicationStateActive 判断程序是否在前台运行。此种情况在此函数中处理：

```
// NS_DEPRECATED_IOS(4_0, 10_0, "Use UserNotifications Framework's -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] or -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:]")
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification;
// 本地通知为 notification
```
+ 在 iOS 10 以上上述方法将被系统废弃，由新增 UserNotifications Framework 中的 -[UNUserNotificationCenterDelegate willPresentNotification:withCompletionHandler:] 或者 -[UNUserNotificationCenterDelegate didReceiveNotificationResponse:withCompletionHandler:] 方法替代。为此，SDK 封装了 JPUSHRegisterDelegate 协议，只需实现相应的协议方法即可适配iOS10新增的delegate方法，与上述远程推送新回调方法一致，也即是如下方法：

```
- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^) (NSInteger))completionHandler; 
   // if (![notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { 
   // 本地通知为 notification 
   // }

- (void)jpushNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler: (void (^)())completionHandler; 
  // if (![response.notification.request.trigger isKindOfClass:[UNPushNotificationTrigger class]]) { 
  // 本地通知为 response.notification 
  // }	
```

### Method  AddNotification

#### 支持版本
v2.1.9 及后续版本

#### 功能说明
API 用于注册或更新推送（支持 iOS 10，并兼容 iOS 10 以下版本）

#### 接口定义

```
+ (void)addNotification:(JPushNotificationRequest *)request;
```
#### 参数说明
+ request [JPushNotificationRequest] 实体类型，可传入推送的属性

#### 调用说明
request 中传入已有推送的 request.requestIdentifier 即更新已有的推送，否则为注册新推送。

#### 代码示例

```
- (void)testAddNotification {
  JPushNotificationContent *content = [[JPushNotificationContent alloc] init];
  content.title = @"Test Notifications";
  content.subtitle = @"2016";
  content.body = @"This is a test code";
  content.badge = @1;
  content.categoryIdentifier = @"Custom Category Name";
  
  // 5s 后提醒 iOS 10 以上支持
  JPushNotificationTrigger *trigger1 = [[JPushNotificationTrigger alloc] init];
  trigger1.timeInterval = 5;
  //每小时重复 1 次 iOS 10 以上支持
  JPushNotificationTrigger *trigger2 = [[JPushNotificationTrigger alloc] init];
  trigger2.timeInterval = 3600;
  trigger2.repeat = YES;
  
  //每周一早上 8：00 提醒，iOS 10 以上支持
  NSDateComponents *components = [[NSDateComponents alloc] init];
  components.weekday = 2;
  components.hour = 8;
  JPushNotificationTrigger *trigger3 = [[JPushNotificationTrigger alloc] init];
  trigger3.dateComponents = components;
  trigger3.repeat = YES;
  
  //#import <CoreLocation/CoreLocation.h>
  //一到某地点提醒，iOS 8 以上支持
  CLLocationCoordinate2D cen = CLLocationCoordinate2DMake(37.335400, -122.009201);
  CLCircularRegion *region = [[CLCircularRegion alloc] initWithCenter:cen
                                                               radius:2000.0
                                                           identifier:@"jiguang"];
  JPushNotificationTrigger *trigger4 = [[JPushNotificationTrigger alloc] init];
  trigger4.region = region;
  
  //5s 后提醒，iOS 10 以下支持
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

### Method  RemoveNotification

#### 支持版本
v2.1.9 及后续版本

#### 功能说明
API 用于移除待推送或已在通知中心显示的推送（支持 iOS 10，并兼容 iOS 10 以下版本）

#### 接口定义

```
+ (void)removeNotification:(JPushNotificationIdentifier *)identifier;
```
#### 参数说明
+ identifier [JPushNotificationIdentifier]实体类型

#### 调用说明
+ iOS 10 以上 identifier 设置为 nil，则移除所有在通知中心显示推送和待推送请求，也可以通过设置 identifier.delivered 和 identifier.identifiers 来移除相应在通知中心显示推送或待推送请求，identifier.identifiers 如果设置为 nil 或空数组则移除相应标志下所有在通知中心显示推送或待推送请求；iOS 10 以下 identifier 设置为 nil，则移除所有推送，identifier.delivered 属性无效，另外可以通过 identifier.notificationObj 传入特定推送对象来移除此推送。

#### 代码示例

```
- (void)testRemoveNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = YES;  //iOS 10 以上有效，等于 YES 则在通知中心显示的里面移除，等于 NO 则为在待推送的里面移除；iOS 10 以下无效
  [JPUSHService removeNotification:identifier];
}


- (void)testRemoveAllNotification {
  [JPUSHService removeNotification:nil];  // iOS 10 以下移除所有推送；iOS 10 以上移除所有在通知中心显示推送和待推送请求

//  //iOS 10 以上支持
//  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
//  identifier.identifiers = nil;
//  identifier.delivered = YES;  //等于 YES 则移除所有在通知中心显示的，等于 NO 则为移除所有待推送的
//  [JPUSHService removeNotification:identifier];
}
```

### Method  FindNotification

#### 支持版本
v2.1.9 及后续版本

#### 功能说明
API 用于查找推送（支持 iOS 10，并兼容 iOS 10 以下版本）

#### 接口定义

```
+ (void)findNotification:(JPushNotificationIdentifier *)identifier;
```
#### 参数说明
+ identifier [JPushNotificationIdentifier]实体类型

#### 调用说明
- iOS 10 以上可以通过设置 identifier.delivered和identifier.identifiers 来查找相应在通知中心显示推送或待推送请求，identifier.identifiers 如果设置为 nil 或空数组则返回相应标志下所有在通知中心显示推送或待推送请求；iOS 10 以下 identifier.delivered 属性无效，identifier.identifiers 如果设置 nil 或空数组则返回所有未触发的推送。
- 须要设置 identifier.findCompletionHandler 回调才能得到查找结果，通过 (NSArray *results) 返回相应对象数组。

#### 代码示例

```
- (void)testFindNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = @[@"sampleRequest"];
  identifier.delivered = YES;  //iOS 10 以上有效，等于 YES 则在通知中心显示的里面查找，等于 NO 则在待推送的里面查找；iOS10 以下无效
  identifier.findCompletionHandler = ^(NSArray *results) {
  NSLog(@"返回结果为：%@", results); // iOS 10 以下返回 UILocalNotification 对象数组，iOS10 以上根据 delivered 传入值返回 UNNotification 或 UNNotificationRequest 对象数组
};
  [JPUSHService findNotification:identifier];
}

- (void)testFindAllNotification {
  JPushNotificationIdentifier *identifier = [[JPushNotificationIdentifier alloc] init];
  identifier.identifiers = nil;
  identifier.delivered = YES;  //iOS 10 以上有效，等于 YES 则查找所有在通知中心显示的，等于 NO 则为查找所有待推送的；iOS 10 以下无效
  identifier.findCompletionHandler = ^(NSArray *results) {
  NSLog(@"返回结果为：%@", results); // iOS 10 以下返回 UILocalNotification 对象数组，iOS 10 以上根据 delivered 传入值返回 UNNotification 或 UNNotificationRequest 对象数组
};
  [JPUSHService findNotification:identifier];
}
```

### Method  SetLocalNotification

#### 功能说明
API 用于注册本地通知
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9 版后将会被废弃，由 AddNotification 方法取代，建议及早放弃使用。
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
iOS 8 新参数使用 API。非 iOS 8 版本或者不需要使用 iOS 8 新功能请使用上面的 API 

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
+ badge 角标的数字。如果不需要改变角标传 -1
+ alertAction 弹框的按钮显示的内容（iOS 8 默认为"打开"，其他默认为"启动"）
+ notificationKey 本地推送标示符
+ userInfo 自定义参数，可以用来标识推送和增加附加信息
+ soundName 本地通知声音名称设置，空为默认声音
+ region
+ regionTriggersOnce
+ category

#### 调用说明

fireDate 必须大于当前时间，同时不能为空。注册通知数目必须小于 64 个。

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
API 用来在 APP 前台运行时，仍然将通知显示出来。（样式为 UIAlertView）
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
iOS 10 以下还可继续使用，iOS 10 以上在 [JPUSHRegisterDelegate jpushNotificationCenter:willPresentNotification:withCompletionHandler:] 方法中调用 completionHandler(UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert);即可，故 v2.1.9 版后将会被废弃，建议及早放弃使用。
</div>

#### 接口定义

```
+ (void)showLocalNotificationAtFront:(UILocalNotification *)notification
                       identifierKey:(NSString *)notificationKey;
```

#### 参数说明
+ notification  当前触发的 UILocalNotification
+ notificationKey  过滤不需要前台显示的通知。只有 notificationKey 标示符的通知才会在前台显示。如果需要全部都显示，该参数传 nil。

#### 调用说明

API必须放在 - (void)application:(UIApplication \*)application didReceiveLocalNotification:(UILocalNotification \*)notification（AppDelegate.m) 苹果的回调函数下。

#### 代码示例

```
- (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification { [JPUSHService showLocalNotificationAtFront:notification identifierKey:@"identifierKey"]; }
```

### Delegate Method  findLocalNotificationWithIdentifier

#### 功能说明
API 用于获取自定义的 identifierKey 标示符的 UILocationNotification 对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9 版后将会被废弃，由 FindNotification 方法取代，建议及早放弃使用。
</div>

#### 接口定义

```
+ (NSArray *)findLocalNotificationWithIdentifier:(NSString *)notificationKey;
```
#### 参数说明

+ notificationKey  获取通知对象的标示符

#### 调用说明
API 返回数组，包含所有和 identifierKey 匹配的 LocalNotification 对象，如果没找到，则为一个空的数组对象。

#### 代码示例

```
NSArray *LocalNotifications = [JPUSHService findLocalNotificationWithIdentifier:@"identifierKey"];
```

### Delegate Method  deleteLocalNotification

#### 功能说明
API 用于删除指定的 LocalNotification 对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9 版后将会被废弃，由 RemoveNotification 方法取代，建议及早放弃使用。
</div>

#### 接口定义

```
+ (void)deleteLocalNotification:(UILocalNotification *)localNotification;
```
#### 参数说明

+ localNotification 删除的本地通知对象

#### 调用说明

API 参数 localNotification 不能为 nil.

#### 代码示例

```
[JPUSHService deleteLocalNotification:localNotification];
```

### Delegate Method  deleteLocalNotificationWithIdentifierKey

#### 功能说明
API 用于删除指定所有 identifierKey 标示符的通知对象
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9 版后将会被废弃，由 RemoveNotification 方法取代，建议及早放弃使用。
</div>

#### 接口定义
```
+ (void)deleteLocalNotificationWithIdentifierKey:(NSString *)notificationKey;
```

#### 参数说明

+ notificationKey  删除的通知拥有的标示符

#### 调用说明

API 参数 notificationKey 不能为 nil.

#### 代码示例
```
[JPUSHService deleteLocalNotificationWithIdentifierKey:@"identifierKey"]; 
```

### Delegate Method  clearAllLocalNotification

#### 功能说明

API 用于清除所有注册的通知
<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
v2.1.9 版后将会被废弃，由 RemoveNotification 方法取代，建议及早放弃使用。
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

API 用于开启 Debug 模式，显示更多的日志信息

#### 接口定义

```
+ (void)setDebugMode;
```
#### 调用说明

当需要了解更多的调试信息时候，调用 API 开启 Debug 模式

#### 代码示例

```
[JPUSHService setDebugMode];
```
### Method  setLogOFF

#### 功能说明

API 用来关闭日志信息（除了必要的错误信息）

#### 接口定义
```
+ (void)setLogOFF;
```

#### 调用说明

不需要任何调试信息的时候，调用此 API （发布时建议调用此 API，用来屏蔽日志信息，节省性能消耗)

#### 代码示例

```
[JPUSHService setLogOFF];
```
## 页面的统计

### 支持的版本

r1.7.0 版本开始。

<div style="font-size:13px;background: #ffa07a;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 10;margin-bottom: 0;">
JPush 上该系列 api 的功能已废弃，如需页面流相关的统计请使用极光统计产品 <a href="https://docs.jiguang.cn/janalytics/client/ios_api/#sdk_1">JAnalytics</a> 。
</div>


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
v1.8.0 版本开始

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示: iOS 11 上要弹出获取地理位置的弹框，建议在 info.plist 配置以下 3 个 key。

<p>NSLocationAlwaysAndWhenInUseUsageDescription
<p>NSLocationAlwaysUsageDescription
<p>NSLocationWhenInUseUsageDescription
</div>

### Method  SetLatitude: longitude

#### 功能说明

API 用于统计用户地理信息。

#### 接口定义

```
+ (void)setLatitude:(double)latitude longitude:(double)longitude;
```

#### 参数说明

+ latitude   地理位置纬度
+ longitude  地理位置经度


#### 调用说明

需要加入 CoreLocation.framework 库， 并且引入 <CoreLocation/CoreLocation.h\> 头文件（#import <CoreLocation/CoreLocation.h \>）

经度和纬度需要开发者自己调用苹果的地理位置信息 API 获取。

#### 代码示例
```
[JPUSHService setLatitude:100.0 longitude:100.0];
```

### Method  setLocation
#### 功能说明
API 用来统计地理位置信息

#### 接口定义
```
+ (void)setLocation:(CLLocation *)location;
```

#### 参数说明

+ location   当前地理位置的 CLLocation 对象

#### 调用说明

需要加入 CoreLocation.framework 库， 并且引入 <CoreLocation/CoreLocation.h\> 头文件（#import <CoreLocation/CoreLocation.h\>）

CLLocation 对象需要开发者自己调用苹果的地理位置信息 API 获取。

#### 代码示例

```
Build Phases 中 Link Binary With Libraries 添加 CoreLocation.framework
应用的 plist 增加 NSLocationAlwaysUsageDescription 或 NSLocationWhenInUseUsageDescription 字段，内容为是否允许 alert 的内容
 
#import <CoreLocation/CoreLocation.h>
@interface xxx : UIViewController<CLLocationManagerDelegate>
@property(nonatomic, strong) CLLocationManager *currentLoaction;
 
- (void)viewDidLoad {
  //注册 LocationManager
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
v1.8.0 版本开始

### Method  crashLogON
#### 功能说明

API 用于统计用户应用崩溃日志

#### 接口定义
```
+ (void)crashLogON;
```

#### 调用说明

如果需要统计 Log 信息，调用该接口。当你需要自己收集错误信息时，切记不要调用该接口。

#### 代码示例

```
[JPUSHService crashLogON];
```
## 设置手机号码

### 支持的版本

v3.0.8 版本开始

### 功能说明

用于短信补充功能。设置手机号码后，可实现“推送不到短信到”的通知方式，提高推送达到率。

#### 接口定义

```
+ (void)setMobileNumber:(NSString *)mobileNumber completion:(void (^)(NSError *error))completion
```
#### 参数说明

* mobileNumber  手机号码。只能以 “+” 或者数字开头，后面的内容只能包含 “-” 和数字，并且长度不能超过 20。如果传 nil 或空串则为解除号码绑定操作
* completion 响应回调。成功则 error 为空，失败则 error 带有错误码及错误信息，具体错误码详见错误码定义

#### 调用说明

此接口调用频率有限制，10s 之内最多 3 次。建议在登录成功以后，再调用此接口。结果信息通过 completion 异步返回，也可将completion 设置为 nil 不处理结果信息。

#### 代码示例

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

##地理围栏
### 功能说明

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>温馨提示，使用地理围栏时注意先要配置位置权限，然后在BackgroundModes中选中Location updates。
iOS 11 以上版本必须有地理位置Always Use 权限，才能生效。
</div>

<br>
地理围栏（Geo-fencing）是LBS的一种新应用，就是用一个虚拟的栅栏围出一个虚拟地理边界。当手机进入或离开某个特定地理区域时，手机可以接收自动通知和警告。

### Method - registerLbsGeofenceDelegate: withLaunchOptions:

调用此 API 注入地理围栏触发时的回调方法

#### 支持的版本

开始支持的版本：3.1.2

#### 接口定义

    + (void)registerLbsGeofenceDelegate:(id<JPUSHGeofenceDelegate>)delegate withLaunchOptions:(NSDictionary *)launchOptions;

#### 参数说明

* delegate 
    * 代理 JPUSHGeofenceDelegate 类型
    * 有三个代理方法回调给开发者，具体使用参考下面的接口说明
*  launchOptions
    * NSDictionary 类型application:didFinishlaunchOptions: 中传入的字典。
    
#### 调用说明
在AppDelegate中application:didFinishlaunchOptions:  调用

``` 
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{
	[JPUSHService registerLbsGeofenceDelegate:self withLaunchOptions:launchOptions];
}
```

### Method - removeGeofenceWithIdentifier:

调用此 API 删除地理围栏

#### 支持的版本

开始支持的版本：3.2.1

#### 接口定义

    + (void)removeGeofenceWithIdentifier:(NSString *)geofenceId;

#### 参数说明

* geofenceId 
    * 字符串类型，地理围栏id，创建地理围栏时会产生地理围栏id。
    
#### 调用说明

``` 
[JPUSHService removeGeofenceWithIdentifier:@"geofenceId"];
```

### Delegate Method - jpushGeofenceIdentifer:didEnterRegion: error:

用户进入地理围栏区域触发的回调。
#### 支持的版本
开始支持的版本：3.1.2

#### 接口定义
	- (void)jpushGeofenceIdentifer:(NSString * _Nonnull)geofenceId didEnterRegion:(NSDictionary * _Nullable)userInfo error:(NSError * _Nullable)error;

#### 参数说明
* geofenceId 
    * 地理围栏唯一id
    * NSString 字符串类型
*  userInfo
    * NSDictionary 类型。
    * 触发地理围栏时回调的相关展示信息
* error
    * 错误信息

### Delegate Method - jpushGeofenceIdentifer:didExitRegion: error:

用户离开地理围栏区域触发的回调。
#### 支持的版本
开始支持的版本：3.1.2

#### 接口定义
	- (void)jpushGeofenceIdentifer:(NSString * _Nonnull)geofenceId didExitRegion:(NSDictionary * _Nullable)userInfo error:(NSError * _Nullable)error;

#### 参数说明
* geofenceId 
    * 地理围栏唯一id
    * NSString 字符串类型
*  userInfo
    * NSDictionary 类型。
    * 触发地理围栏时回调的相关展示信息
* error
    * 错误信息






### Method - setGeofenecMaxCount:

调用此 API 来设置最大的地理围栏监听个数，默认值为10

#### 支持的版本

开始支持的版本：3.1.2

#### 接口定义

    + (void)setGeofenecMaxCount:(NSInteger)count;

    
#### 参数说明

* count
    * 类型要求为NSInteger 类型
    * 默认值为10
    * iOS系统要求最大不能超过20个，否则会报错。




## Notification Service Extension 相关接口

### 支持的版本

Notification Service Extension SDK v1.0.0（随 JPush iOS SDK 3.0.7 版本发布）及以后的版本

### 功能说明

使用 Notification Service Extension SDK 上报推送送达情况

### jpushSetAppkey:

设置 appkey 接口，必须提前调用

#### 接口定义

```
+ (void)jpushSetAppkey:(NSString *)appkey
```
#### 参数说明

* appkey  需要和 main app 中的 JPush SDK 的 appkey 保持一致

### jpushReceiveNotificationRequest:with:

消息送达统计接口，调用该接口上报 APNs 消息体中的 JPush 相关数据

#### 接口定义

```
+ (void)jpushReceiveNotificationRequest:(UNNotificationRequest *)request with:(void (^)(void))completion
```
#### 参数说明

* request  UNNotificationRequest
* completion 消息送达上报回调，请在该回调中执行显示 APNs 等操作

### setLogOff

关闭日志    
默认为开启，建议发布时关闭以减少不必要的 IO

#### 接口定义

```
+ (void)setLogOff
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
      <td>AppKey 不存在</td>
      <td>请到官网检查 Appkey 对应的应用是否已被删除</td>
    </tr>
    <tr >
      <td>1008</td>
      <td>AppKey 非法</td>
      <td>请到官网检查此应用详情中的 Appkey，确认无误</td>
    </tr>
    <tr >
      <td>1009</td>
      <td>当前的 Appkey 下没有创建 iOS 应用；你所使用的 SDK 版本低于 2.1.0</td>
      <td>请到官网检查此应用的应用详情；更新应用中集成的极光 SDK 至最新。</td>
    </tr>
        <tr >
      <td>6001</td>
      <td>无效的设置，tag/alias 不应参数都为 null</td>
      <td></td>
    </tr>
    <tr >
      <td>6002</td>
      <td>设置超时</td>
      <td>建议重试，一般出现在网络不佳、初始化尚未完成时</td>
    </tr>
    <tr >
      <td>6003</td>
      <td>alias 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|</td>
    </tr>
    <tr >
      <td>6004</td>
      <td>alias 超长。最多 40 个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6005</td>
      <td>某一个 tag 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字、特殊字符（2.1.9 支持）@!#$&*+=.|</td>
    </tr>
    <tr >
      <td>6006</td>
      <td>某一个 tag 超长。一个 tag 最多 40 个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6007</td>
      <td>tags 数量超出限制。最多 1000 个</td>
      <td>这是一台设备的限制。一个应用全局的标签数量无限制。</td>
    </tr>
    <tr >
      <td>6008</td>
      <td>tag 超出总长度限制</td>
      <td>总长度最多 7 K 字节</td>
    </tr>
    <tr >
      <td>6009</td>
      <td>未知错误</td>
      <td>SDK 发生了意料之外的异常，客户端日志中将有详细的报错信息，可据此排查。</td>
    </tr>
    <tr >
      <td>6011</td>
      <td>短时间内操作过于频繁</td>
      <td>10s 内设置 tag 或 alias 大于 10 次，或 10s 内设置手机号码大于 3 次</td>
    </tr>
    <tr >
      <td>6012</td>
      <td>在 JPush 服务 stop 状态下设置了 tag 或 alias 或手机号码</td>
      <td>开发者可根据这个错误码的信息做相关处理或者提示</td>
    </tr>
    <tr >
      <td>6013</td>
      <td>用户设备时间轴异常</td>
      <td>设备本地时间轴异常变化影响了设置手机号码</td>
    </tr>
    <tr >
      <td>6014</td>
      <td>网络繁忙</td>
      <td>网络繁忙，本次请求失败，请重新发起请求</td>
    </tr>
    <tr >
      <td>6015</td>
      <td>黑名单</td>
      <td>用户被拉入黑名单，请联系 support 解除</td>
    </tr>
    <tr >
      <td>6016</td>
      <td>该用户无效</td>
      <td>失效用户请求失败</td>
    </tr>
    <tr >
      <td>6017</td>
      <td>该请求无效</td>
      <td>本次请求出现异常参数，请求无效</td>
    </tr>
	 <tr >
      <td>6018</td>
      <td>Tags 过多</td>
      <td>该用户 tags 已设置超过 1000 个，不能再设置</td>
    </tr>
    <tr >
      <td>6019</td>
      <td>获取 Tags 失败</td>
      <td>在获取全部 tags 时发生异常</td>
    </tr>
	  <tr >
      <td>6020</td>
      <td>请求失败</td>
      <td>发生了特殊问题导致请求失败</td>
    </tr>
    <tr >
      <td>6021</td>
      <td>上一次的 tags 请求还在等待响应，暂时不能执行下一次请求</td>
      <td>多次调用 tag 相关的 API，请在获取到上一次调用回调后再做下一次操作；在未取到回调的情况下，等待 20 秒后可做下一次操作。</td>
    </tr>
	 <tr >
      <td>6022</td>
      <td>上一次的 alias 请求还在等待响应，暂时不能执行下一次请求。</td>
      <td>多次调用 alias 相关的 API，请在获取到上一次调用回调后再做下一次操作；在未取到回调的情况下，等待 20 秒后可做下一次操作。</td>
    </tr>
    <tr >
      <td>6023</td>
      <td>手机号码不合法</td>
      <td>只能以 “+” 或者数字开头，后面的内容只能包含 “-” 和数字</td>
    </tr>
    <tr >
      <td>6024</td>
      <td>服务器内部错误</td>
      <td>服务器内部错误，过一段时间再重试</td>
    </tr>
    <tr >
      <td>6025</td>
      <td>手机号码太长</td>
      <td>手机号码过长，目前极光检测手机号码的最大长度为 20</td>
    </tr>
    <tr >
      <td>7000</td>
      <td>地理围栏过期</td>
      <td>当前时间超过设置的过期时间</td>
    </tr>
    <tr >
      <td>7001</td>
      <td>地理围栏不存在</td>
      <td>逻辑是触发地理围栏的时候，本地缓存列表没有查找到对应的geofenceid</td>
    </tr>

  </table>
</div>

[0]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194-CH3-SW1
[1]: https://github.com/ylechelle/OpenUDID







