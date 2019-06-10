# iOS SDK API

## SDK 接口说明
JSHAREService 类，包含分享 SDK 的所有接口。  
JSHARELaunchConfig 类，分享 SDK 启动配置模型。  
JSHAREMessage 类，分享参数说明。  
JSHARESocial 类，社交平台授权信息模型。  
JSHARESocialUserInfo 类，社交平台用户信息模型，继承于 JSHARESocial。    

## SDK 初始化

### Method - setupWithConfig

#### 接口说明
初始化接口,建议在 application:didFinishLaunchingWithOptions 中调用。
#### 接口定义
```
+(void)setupWithConfig:(JSHARELaunchConfig *)config
```

#### 参数说明
config：JSHARELaunchConfig 类。
    
#### 调用示例

```
    JSHARELaunchConfig *config = [[JSHARELaunchConfig alloc] init];
    config.appKey = @"AppKey copied from JiGuang Portal application";
    config.SinaWeiboAppKey = @"374535501";
    config.SinaWeiboAppSecret = @"baccd12c166f1df96736b51ffbf600a2";
    config.SinaRedirectUri = @"https://www.jiguang.cn";
    config.QQAppId = @"1105864531";
    config.QQAppKey = @"glFYjkHQGSOCJHMC";
    config.WeChatAppId = @"wxa2ea563906227379";
    config.WeChatAppSecret = @"bb63c0a06bf0ee7f633a5bc44304d110";
    config.FacebookAppID = @"1847959632183996";
    config.FacebookDisplayName = @"JShareDemo";
    config.TwitterConsumerKey = @"4hCeIip1cpTk9oPYeCbYKhVWi";
    config.TwitterConsumerSecret = @"DuIontT8KPSmO2Y1oAvby7tpbWHJimuakpbiAUHEKncbffekmC";
    config.JChatProAuth = @"a7e2ce002d1a071a6ca9f37d";
    [JSHAREService setupWithConfig:config];
```

	
	
## 处理平台回调
### Method - handleOpenUrl
#### 接口说明
处理平台回调，必要；
#### 接口定义
```
+(BOOL)handleOpenUrl:(NSURL *)url;
```
#### 参数说明
url：在 Appdelegate 的 application:handleOpenURL: 中调用。不调用此接口 JSHARE 将无法提供分享回调。
#### 调用示例

```
    - (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [JSHAREService handleOpenUrl:url];
    return YES;
    }
```

## 发起分享
### Method - share
#### 接口说明
调用此接口发起分享
#### 接口定义
```
 +(void)share:(JSHAREMessage *)message
      handler:(JSHAREStateHandler)handler
```
#### 参数说明
message：JSHAREMessage 类    
handler：分享结果的回调。
        
#### 调用示例
    
    
```
    JSHAREMessage *message = [JSHAREMessage message];
    message.text = @"欢迎使用极光社会化组件 JShare，SDK 包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = JSHAREPlatformWechatSession;
    message.mediaType = JSHAREText;
    [JSHARESdk share:message handler:^(JSHAREState state, NSError *error) {
          NSLog(@"分享回调");
    }];
```
    

    
##发起分享 - 仅支持JChatPro
### Method - share
####接口说明
调用此接口发起分享
####接口定义
```
 + (void)share:(JSHAREMessage *)message
      completionHandler:(JSHARECompletionHandler)handler ;
```
####参数说明
message：JSHAREMessage 类<br>
handler：分享结果的回调。
        
####调用示例：
    
    
```
    JSHAREMessage *message = [JSHAREMessage message];
    message.mediaType = JSHAREText;
    message.url = @"http://tech.qq.com/zt2012/tmtdecode/252.htm";
    message.text = @"欢迎使用极光社会化组件 JShare，SDK 包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能";
    message.title = @"极光社会化组件";
    message.platform = JSHAREPlatformJChatPro;
    message.thumbUrl = @"http://img2.imgtn.bdimg.com/it/u=3721213387,3527941751&fm=27&gp=0.jpg";
    message.extInfo = @"extramessage";
    message.callbackUrl = @"https://www.jiguang.cn/";
    message.pkgName = @"android_pkg";
    message.className = @"android_class_name";
    message.appName = @"我是MT";
    message.fromScheme = @"jchatproa7e2ce002d1a071a6ca9f37d";

    [JSHAREService share:message completionHandler:^(JSHAREState state, NSError *error, id responseObject) {
        NSLog(@"responseObject :%@", responseObject);
        if (!error) {
            NSLog(@"分享图文成功");
        }else{
            NSLog(@"分享图文失败, error : %@", error);
        }
    }];
```
        
       


## 各平台分享参数说明

### 微信(包括微信好友、朋友圈、微信收藏)
#### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|分享文本|不超过10KB

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```
#### 2）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
title| 否 | NSString|标题|长度不能超过 512
image| 是 | NSData|图片|大小不能超过 10M，
```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```
#### 3）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREAudio
title| 否 | NSString|音乐标题|长度不能超过 512
text| 否 | NSString|音乐描述|长度不能超过 1K
mediaDataUrl| 否 | NSString |音乐资源 Url |点击播放按钮可直接播放 url ,长度不能超过 10K
Url| 是 | String|跳转Url|点击跳转页面 url,长度不能超过 10K
thumbnail | 否 | NSData|缩略图|大小不能超过 32K,
```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```
#### 4）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
title| 否 | NSString|音乐标题|长度不能超过 512
text| 否 | NSString|音乐描述|长度不能超过 1K
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 10K
thumbnail | 否 | NSDate|缩略图|大小不能超过 32K,
```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```
#### 5）分享网页
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
title| 否 | NSString|标题|长度不能超过 512
text| 否 | NSString|描述|长度不能超过 1K
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 10K
thumbnail| 否 | NSDate|缩略图|不超过32K，当分享JSHARELink类型时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.image = imageData;

```
#### 6）分享Emoji表情（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREEmoticon
emoticonData | 是 | NSData|表情|大小不能超过 10M，
```
    message.mediaType = JSHAREEmoticon;
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"res6" ofType:@"gif"];
    NSData *emoticonData = [NSData dataWithContentsOfFile:filePath];
    message.emoticonData = emoticonData;

```
#### 7）分享文件（朋友圈不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREFile
fileData| 是 | NSData|文件的数据|大小不能超过10M
fileExt| 否 | NSString|文件后缀名|最大 64 字符
```
    message.mediaType = JSHAREFile;
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"jiguang" ofType:@"mp4"];
    NSData *fileData = [NSData dataWithContentsOfFile:filePath];
    message.fileData = fileData;
    message.fileExt = @"mp4";
    message.platform = platform;
    message.title = @"jiguang.mp4";
```
#### 8）分享app（微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREApp
title| 否 | NSString|标题|长度不能超过 512
text| 否 | NSString|描述|长度不能超过 1K
Url| 否 | NSString|跳转Url|点击跳转页面 url,长度不能超过 10K
extInfo| 否 | NSString|  |第三方程序自定义的简单数据。
fileData | 否 | NSData|对应APP的数据| 大小不能超过10M
```
    message.mediaType = JSHAREApp;
    message.url =@"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.extInfo = @"<xml>extend info</xml>";
    message.fileData = data;
    message.platform = platform;
```

#### 9）分享小程序（仅支持分享到微信会话）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREMiniProgram
title| 是 | NSString|小程序title|长度不能超过 512
text| 否 | NSString|小程序描述|长度不能超过 1K
Url| 是 | NSString|兼容微信低版本网页地址|长度不能超过10k
userName| 是 | NSString|小程序username |小程序原始ID获取方法：登录小程序管理后台-设置-基本设置-帐号信息
path | 是 | NSString|小程序页面的路径| 小程序被用户点击后所打开的页面路径
miniProgramType | 否 | NSString|小程序版本类型| 0正式版，1开发版，2体验版。默认0，正式版。
withShareTicket | 否| Bool|是否使用带 shareTicket 的转发| 默认false,不使用带 shareTicket 的转发。
image | 是 | NSData|小程序新版本的预览图| 最大128k
```
    message.mediaType = JSHAREMiniProgram;
    message.title = @"小程序title";
    message.text = @"小程序描述";
    message.url = @"www.jiguang.cn";
    message.userName = @"gh_d43f693ca31f";
    message.path = @"pages/page";
    message.miniProgramType = 0;
    message.withShareTicket = YES;
    message.image = imageData;
    message.platform = JSHAREPlatformWechatSession;
```


### QQ
#### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|分享文本|最大1536字符

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
image| 是 | NSData|图片|大小不能超过 5 M，
text | 否 | NSString|分享内容的描述|最大 512 字符
```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```


#### 3）分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 1024
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
	 message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.image = imageData;

```

#### 4）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREAudio
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 1024
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。
mediaDataUrl| 否 | NSString |音乐资源 Url |点击播放按钮可直接播放 url


```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```
#### 5）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 1024
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

### QQ空间
#### 1)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|分享文本|最大128字符

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
image| 是 | NSData|图片|大小不能超过 5 M，
images| 否 | NSArray|图片|分享到 QQ 空间支持多张图片，图片数组的元素需要为 NSData 类型，图片数量限制为20张。若只分享单张图片至 QQ 空间使用 image 字段即可。，

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```
#### 3）分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 512
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
	 message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.image = imageData;

```

#### 4）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREAudio
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 512
mediaDataUrl| 否 | NSString|音乐数据url地址|长度不能超过 512
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```
#### 5）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
Url| 是 | NSString|跳转Url|点击跳转页面 url,长度不能超过 512
thumbnail| 否 | NSDate|缩略图|不超过1M，当分享时没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。

```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```
#### 6）分享本地视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
title| 否 | NSString|标题|长度不能超过 128
text| 否 | NSString|描述|长度不能超过 512
videoAssetURL | 是 | NSString| 本地视频AssetURL |分享本地视频到 QQ 空间的必填参数，可传ALAsset的ALAssetPropertyAssetURL，或者PHAsset的localIdentifier。


```
    message.mediaType = JSHAREVideo;
    message.text = @"欢迎使用极光社会化组件JShare，SDK包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.videoAssetURL = assetURL.absoluteString;
    message.platform = JSHAREPlatformQzone;
```


### 新浪微博
#### 1)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|分享文本|不超过140个中文字符

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
image| 是 | NSData|图片|大小不能超过 10 M，
text | 否 | NSString|分享内容的描述|不超过140个中文字符
```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```
#### 3)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
title| 否 | NSString|标题|长度不能超过 1 K
text| 否 | NSString|描述|长度不能超过 140个中文字符
Url| 是 | NSString|跳转Url|最大 255 字符。
thumbnail| 否 | NSData|缩略图|小于32k，当分享没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。当最终未获得缩略图时，可能导致链接在客户端上无法正常跳转。建议填写。

```
	 message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.image = imageData;

```

### 新浪微博私信
#### 1)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
title| 否 | NSString|标题|长度不能超过 1 K，且不为空
text| 否 | NSString|描述|长度不能超过 140个中文字符
Url| 是 | NSString|跳转Url|最大 255 字符。
thumbnail| 否 | NSDate|缩略图|大小小于32k，当分享没有提供缩略图时，若image参数不为空，JSHARE将会裁剪此参数提供的图片去适配缩略图。
```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.platform = JSHAREPlatformSinaWeiboContact;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.image = imageData;
```


### Facebook, Facebook Messenger

#### 1)分享图片

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
images| 是 | NSArray|图片| 图片数量限制为6张。如果分享单张图片，图片大小建议不要超过12M；如果分享多张图片，每张图片大小建议不要超过700K，
text | 否 | NSString|文本| 
```
    message.text = [NSString stringWithFormat:@"时间:%@ JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！",[self localizedStringTime]];
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.images = @[imageData,imageData];
    message.mediaType = JSHAREImage;
    message.platform = platform;
```

#### 2）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
text| 否 | NSString|文本| 
videoAssetURL | 是 | NSString | 视频参数 |分享到视频类型至 facebook 、facebookMessenger 只能识别 ALAsset 的ALAssetPropertyAssetURL。
```
    message.mediaType = JSHAREVideo;
    message.text = @"欢迎使用极光社会化组件JShare，SDK包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.videoAssetURL = assetURL.absoluteString;
    message.platform = platform;
```
  
#### 3)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
text| 否 | NSString|描述|
Url| 是 | NSString|跳转Url|分享点击跳转的 url 
```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
```



### Twitter
#### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|分享文本| 不超过140个中文字符

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```


#### 2)分享图片

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
image| 是 | NSData|图片|单张图片大小不能超过 5 M，
images| 否 | NSArray|图片|分享多张图片用images ，图片数组的元素需要为 NSData 类型，图片数量限制为4张。
text | 否 | NSString|文本| 最大 140 个汉字
```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.image = imageData;
    message.mediaType = JSHAREImage;
    message.platform = platform;
```

#### 3）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREVideo
text| 否 | NSString|文本| 最大 140 个汉字
videoData | 是 | NSData | 视频参数 |分享到 twitter 的视频，大小不应超过15 mb , 时间应该在0.5秒到30秒之间,尺寸应该在32x32和1280x1024之间 , 长宽比应在1：3和3：1之间

```    
    message.mediaType = JSHAREVideo;
    message.text = [NSString stringWithFormat:@"时间:%@ JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！",
    NSString *path = [[NSBundle mainBundle] pathForResource:@"jiguangVideoForTwitter" ofType:@"mp4"];
    NSData *data = [NSData dataWithContentsOfFile:path];
    message.videoData = data;
    message.platform = JSHAREPlatformTwitter;
```

#### 4)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHARELink
text| 否 | NSString|描述|url 和 text 的总长度不能超过280个字节。
Url| 是 | NSString|跳转Url|url 和 text 的总长度不能超过280个字节，可以带有图片或视频，但是不能同时带图片和视频。
videoData | 否 | NSData | 视频参数 |分享到 twitter 的视频，大小不应超过15 mb。
image| 否 | NSData|图片|单张图片大小不能超过 5 M，
images| 否 | NSArray|图片|分享多张图片用images ，图片数组的元素需要为 NSData 类型，图片数量限制为4张。

```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.image = imageData;
```



### JChatPro
#### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM| 分享类型| JSHAREText
text | 是 | NSString|消息内容|不超过4k字节
title | 否 | NSString|消息标题|
extInfo | 否 | NSString|点击消息跳转到第三方应用时带的extra信息|
callbackUrl | 否 | NSString|当应用内的分享消息被点击时，如果启动的客户端不存在时，回调的url。开发者可以通过这个配置实现本地应用不存在时跳转到他们的官网之类的操作|
pkgName | 否 | NSString|点击消息时跳转第三方android客户端的包名|
className | 否 | NSString|点击消息时跳转第三方android客户端的类名|
appName | 否 | NSString|第三方客户端应用名称|

```
    message.mediaType = JSHAREText;
    message.text = @"JChatPro 分享文本TEST";
    message.title = @"极光社会化组件";
    message.appName = @"我是MT";
    message.platform = JSHAREPlatformJChatPro;
```


#### 2)分享图片

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREImage
thumbUrl| 否 | NSString|图片|网络缩略图地址
image| images且imageURL为空时必填 | NSData|图片|分享单张图片，暂无限制。
images| image且imageURL为空时必填 | NSArray|图片|分享多张图片用images ，图片数组的元素需要为 NSData 类型，图片数量限制为9张。
imageURL| image且images为空时必填 | NSString |图片|图片网络地址。
text | 否 | NSString|消息内容|不超过4k字节
title | 否 | NSString|消息标题|
extInfo | 否 | NSString|点击消息跳转到第三方应用时带的extra信息|
callbackUrl | 否 | NSString|当应用内的分享消息被点击时，如果启动的客户端不存在时，回调的url。开发者可以通过这个配置实现本地应用不存在时跳转到他们的官网之类的操作|
pkgName | 否 | NSString|点击消息时跳转第三方android客户端的包名|
className | 否 | NSString|点击消息时跳转第三方android客户端的类名|
appName | 否 | NSString|第三方客户端应用名称|
```
    message.mediaType = JSHAREImage;
    message.platform = JSHAREPlatformJChatPro;
    message.imageURL = @"http://pic.58pic.com/58pic/13/76/61/33N58PICRdp_1024.jpg";
    message.image = imageData;
    message.images = @[imageData,imageData,imageData];
```

#### 3）分享图文
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
mediaType | 是| NS_ENUM | 分享类型| JSHAREGraphic
thumbUrl| 否 | NSString|图片|网络缩略图地址
image| 否 | NSData|图片|分享单张图片，暂无限制。
images| 否| NSArray|图片|分享多张图片用images ，图片数组的元素需要为 NSData 类型，图片数量限制为9张。
imageURL| 否 | NSString |图片网络地址|
text | 否 | NSString|消息内容|不超过4k字节
title | 否 | NSString|消息标题|
extInfo | 否 | NSString|点击消息跳转到第三方应用时带的extra信息|
callbackUrl | 否 | NSString|当应用内的分享消息被点击时，如果启动的客户端不存在时，回调的url。开发者可以通过这个配置实现本地应用不存在时跳转到他们的官网之类的操作|
pkgName | 否 | NSString|点击消息时跳转第三方android客户端的包名|
className | 否 | NSString|点击消息时跳转第三方android客户端的类名|
appName | 否 | NSString|第三方客户端应用名称|

```    
    message.mediaType = JSHAREGraphic;
    message.platform = JSHAREPlatformJChatPro;
    message.text = @"欢迎使用极光社会化组件 JShare，SDK 包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能";
    message.title = @"极光社会化组件";

    message.thumbUrl = @"http://d.lanrentuku.com/down/png/0905/pngicon-12/png-1102.png";
    message.extInfo = @"extramessage";
    message.callbackUrl = @"https://www.jiguang.cn/";
    message.pkgName = @"android_pkg";
    message.className = @"android_class_name";
    message.appName = @"我是MT";
```

参数的具体使用可参考Demo。




        
    
## 检查不存在新浪客户端情况的网页端是否登陆

 +(BOOL)isSinaWeiboWebLogined

## 登出新浪网页端最新帐号

 +(BOOL)sinaWeiboWebLogOut
 
## 检查是否存在微信客户端
    
 +(BOOL)isWeChatInstalled
    
## 检查是否存在 QQ 客户端
    
 +(BOOL)isQQInstalled

## 检查是否存在新浪微博客户端
    
 +(BOOL)isSinaWeiBoInstalled

## 检查是否存在 Facebook 客户端
    
 +(BOOL)isFacebookInstalled
 
## 检查是否存在 Messenger 客户端
    
 +(BOOL)isFacebookMessengerInstalled
 
## 检查是否存在 Twitter 客户端
  +(BOOL)isTwitterInstalled
 
## 检查是否存在JChatPro客户端
  +(BOOL)isJChatProInstalled
 
## 获取社交平台用户信息
### method - getSocialUserInfo
#### 接口定义
+(void)getSocialUserInfo:(JSHAREPlatform)platform
                  handler:(JSHARESocialHandler)handler
                  
#### 接口说明
通过调用获取用户信息接口，获取用户在第三方平台的用户 ID、头像等资料完成账号体系的构建。

#### 参数说明

* platform : JSHAREPlatform 枚举类型
* handler : JSHARESocialHandler 获取用户信息的回调

#### 调用实例

```
[JSHAREService getSocialUserInfo:platfrom handler:^(JSHARESocialUserInfo *userInfo, NSError *error) {
        NSString *alertMessage;
        NSString *title;
        if (error) {
            title = @"失败";
            alertMessage = @"无法获取到用户信息";
        }else{
            title = userInfo.name;
            alertMessage = [NSString stringWithFormat:@"昵称: %@\n 头像链接: %@\n 性别: %@\n",userInfo.name,userInfo.iconurl,userInfo.gender == 1? @"男" : @"女"];
        }
        UIAlertView *Alert = [[UIAlertView alloc] initWithTitle:title message:alertMessage delegate:nil cancelButtonTitle:@"OK" otherButtonTitles:nil];
        dispatch_async(dispatch_get_main_queue(), ^{
            [Alert show];
        });
        
        
    }];
```

### method - isPlatformAuth
#### 接口定义
+(BOOL)isPlatformAuth:(JSHAREPlatform)platform
#### 接口说明
检查用户授权之后信息是否过期。注意：仅仅检验本地 token 是否在有效期内，假如对应的社交平台用户在社交平台手动取消了授权，即使本地 token 还在有效期内，但是还是失效的。

#### 参数说明
* platform: 社交平台枚举 

#### 调用实例
```
BOOL isOauth = [JSHAREService isPlatformAuth:JSHAREPlatformQQ];
```
### method - cancelAuthWithPlatform
#### 接口定义
+(BOOL)cancelAuthWithPlatform:(JSHAREPlatform)platfrom

#### 接口说明
删除用户授权之后的储存在本地的授权信息。

#### 参数说明
* platform: 社交平台枚举 

#### 调用实例
```
BOOL cancelOauth = [JSHAREService cancelAuthWithPlatform:JSHAREPlatformQQ];
;
```


## 日志等级设置
### Method - setDebug
#### 接口说明
设置是否打印 sdk 产生的 Debug 级 log 信息, 默认为 NO (不打印 Debug 级 log)
#### 接口定义
```    
+(void)setDebug:(BOOL)enable
```
#### 参数说明
enable：设置为 YES 开启，设置为 NO 关闭

#### 调用示例 
        
```
[JSHAREService setDebug:YES];
```
      
      
      


