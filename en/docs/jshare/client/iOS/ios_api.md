# iOS SDK API

## SDK Interface Description
JSHAREService class, contains all interfaces of share SDK.
JSHARELaunchConfig class, boot configuration model of share SDK  
JSHAREMessage class，instructions of share parameters  
JSHARESocial class, authorization information model of social platforms
JSHARESocialUserInfo class, user information model of social platforms, inherited from JSHARESocial.

## SDK Initialization

### Method - setupWithConfig

#### Interface Description

Initialize the interface. It is recommended to call in application:didFinishLaunchingWithOptions.

#### Interface Definition

```
+(void)setupWithConfig:(JSHARELaunchConfig *)config
```

#### Parameter Description
config：JSHARELaunchConfig class.

#### Call Example

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
    [JSHAREService setupWithConfig:config];
```

## Processing Platform Callbacks

### Method - handleOpenUrl

#### Interface Description

Processing platform callback, required;

#### Interface Definition

```
+(BOOL)handleOpenUrl:(NSURL *)url;
```

#### Parameter Description

url：Called in application:handleOpenURL: of Appdelegate. JShare will not be able to provide share callbacks without calling this interface.

#### Call Example

```
    - (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [JSHAREService handleOpenUrl:url];
    return YES;
    }
```

## Initiate Sharing

### Method - share

#### Interface Description

Call this interface to initiate sharing

#### Interface Definition

```
 +(void)share:(JSHAREMessage *)message
      handler:(JSHAREStateHandler)handler
```

#### Parameter Description

message：JSHAREMessage class  
handler：Callback for sharing results

#### Call Example

```
    JSHAREMessage *message = [JSHAREMessage message];
    message.text = @"欢迎使用极光社会化组件 JShare，SDK 包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = JSHAREPlatformWechatSession;
    message.mediaType = JSHAREText;
    [JSHARESdk share:message handler:^(JSHAREState state, NSError *error) {
          NSLog(@"分享回调");
    }];
```

## Instructions of Share Parameters on Each Platform

### WeChat (Including WeChat Friends, Moments Collection) 

#### 1）Share Texts

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**       |
|---------------|----------------------|--------------------|---------------------------|-------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText        |
| text          | Yes                  | NSString           | Share text                | No more than 10KB |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 

#### 2）Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**            |
|---------------|----------------------|--------------------|---------------------------|------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREImage            |
| image         | No                   | NSData             | Image                     | Size cannot exceed 10M |

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```

#### 3）Share Music

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                              |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREAudio                                                              |
| title         | No                   | NSString           | Music title               | Length cannot exceed 512                                                 |
| text          | No                   | NSString           | Music description         | Length cannot exceed 1K                                                  |
| mediaDataUrl  | No                   | NSString           | Music resource Url        | Click play button to play url directly, and the length cannot exceed 10K |
| Url           | Yes                  | String             | Jump Url                  | Click the url for jump page, and the length cannot exceed 10K            |
| thumbnail     | No                   | NSDate             | Thumbnail                 | Size cannot exceed 32K                                                   |

```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

#### 4）Share Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                   |
|---------------|----------------------|--------------------|---------------------------|---------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                   |
| title         | No                   | NSString           | Music title               | Length cannot exceed 512                                      |
| text          | No                   | NSString           | Music description         | Length cannot exceed 1K                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 10K |
| thumbnail     | No                   | NSDate             | Thumbnail                 | Size cannot exceed 32K                                        |

```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

#### 5）Share Webpages

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                     |
|---------------|----------------------|--------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                                                      |
| title         | No                   | NSString           | Title                     | Length cannot exceed 512                                                                                                                                                        |
| text          | No                   | NSString           | Description               | Length cannot exceed 1K                                                                                                                                                         |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 10K                                                                                                                   |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 32K. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

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

#### 6）Share Emoji Expressions（Not support by WeChat Moments and WeChat Collection）

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**            |
|---------------|----------------------|--------------------|---------------------------|------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREEmoticon         |
| emoticonData  | No                   | NSData             | Expression                | Size cannot exceed 10M |

```
    message.mediaType = JSHAREEmoticon;
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"res6" ofType:@"gif"];
    NSData *emoticonData = [NSData dataWithContentsOfFile:filePath];
    message.emoticonData = emoticonData;

```

#### 7）Share Files（Not support by WeChat Moments）

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                |
|---------------|----------------------|--------------------|---------------------------|----------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREFile                 |
| fileData      | Yes                  | NSData             | File data                 | Size cannot exceed 10M     |
| fileExt       | Yes                  | NSString           | File suffix               | No more than 64 characters |

```
    message.mediaType = JSHAREFile;
    NSString *filePath = [[NSBundle mainBundle] pathForResource:@"jiguang" ofType:@"mp4"];
    NSData *fileData = [NSData dataWithContentsOfFile:filePath];
    message.fileData = fileData;
    message.fileExt = @"mp4";
    message.platform = platform;
    message.title = @"jiguang.mp4";
```

#### 8）Share apps（Not support by WeChat Collection）

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description**    | **Remarks**                                                   |
|---------------|----------------------|--------------------|------------------------------|---------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                   | JSHAREApp                                                     |
| title         | No                   | NSString           | Title                        | Length cannot exceed 512                                      |
| text          | No                   | NSString           | Description                  | Length cannot exceed 1K                                       |
| Url           | No                   | NSString           | Jump Url                     | Click the url for jump page, and the length cannot exceed 10K |
| extInfo       | No                   | NSString           |                              | Custom simple data of third-party programs                    |
| fileData      | No                   | NSData             | Data of Corresponding to APP | Size cannot exceed 10M                                        |

```
    message.mediaType = JSHAREApp;
    message.url =@"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.extInfo = @"<xml>extend info</xml>";
    message.fileData = data;
    message.platform = platform;
```

### QQ

#### 1）Share Texts

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                  |
|---------------|----------------------|--------------------|---------------------------|------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText                   |
| text          | Yes                  | NSString           | Share text                | No more than 1536 characters |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 

#### 2）Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description**     | **Remarks**                 |
|---------------|----------------------|--------------------|-------------------------------|-----------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                    | JSHAREImage                 |
| image         | Yes                  | NSData             | Image                         | Size cannot exceed 15M      |
| text          | No                   | NSString           | Description of shared content | No more than 512 characters |

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```

#### 3）Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                                                     |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

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

#### 4）Share Music

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREAudio                                                                                                                                                                    |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |
| mediaDataUrl  | No                   | NSString           | Music resource Url        | Click play button to play url directly                                                                                                                                         |

```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

#### 5）Share Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                                                                                                                                    |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

### QQ Space 

#### 1)Share Texts

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                  |
|---------------|----------------------|--------------------|---------------------------|------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText                   |
| text          | Yes                  | NSString           | Share text                | No more than 1536 characters |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                                                                      |
|---------------|----------------------|--------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREImage                                                                                                                                                                                                                      |
| image         | Yes                  | NSData             | Image                     | Size cannot exceed 5M                                                                                                                                                                                                            |
| images        | No                   | NSArray            | Image                     | Sharing to QQ space supports multiple pictures. The elements of picture array need to be NSData type, and the number of pictures is limited to 20 pieces. If you only share a single image to the QQ space, use the image field. |

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
``` 

#### 3）Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                                                     |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

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

#### 4）Share Music

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREAudio                                                                                                                                                                    |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| mediaDataUrl  | No                   | NSString           | Url address of music data | Length cannot exceed 512                                                                                                                                                       |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

```
    message.mediaType = JSHAREAudio;
    message.url =  @"https://y.qq.com/n/yqq/song/003RCA7t0y6du5.html";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

#### 5）Share Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                    |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                                                                                                                                    |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                                                       |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                                                       |
| Url           | Yes                  | NSString           | Jump Url                  | Click the url for jump page, and the length cannot exceed 512                                                                                                                  |
| thumbnail     | No                   | NSDate             | Thumbnail                 | No more than 1M. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

```
    message.mediaType = JSHAREVideo;
    message.url =@"http://v.youku.com/v_show/id_XOTQwMDE1ODAw.html?from=s1.8-1-1.2&spm=a2h0k.8191407.0.0";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
```

#### 6）Share Local Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                  |
|---------------|----------------------|--------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                                                                                                  |
| title         | No                   | NSString           | Title                     | Length cannot exceed 128                                                                                                                     |
| text          | No                   | NSString           | Description               | Length cannot exceed 512                                                                                                                     |
| videoAssetURL | Yes                  | NSString           | Local video AssetURL      | The required parameters for sharing local video to QQ space, can be passed ALAssetPropertyAssetURL of ALAsset, or localIdentifier of PHAsset |

```
    message.mediaType = JSHAREVideo;
    message.text = @"欢迎使用极光社会化组件JShare，SDK包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.title = @"欢迎使用极光社会化组件JShare";
    message.videoAssetURL = assetURL.absoluteString;
    message.platform = JSHAREPlatformQzone;
```

### Sina Weibo

#### 1)Share Texts

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**      |
|---------------|----------------------|--------------------|---------------------------|------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText       |
| text          | Yes                  | NSString           | Share text                | No more than 140 |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description**     | **Remarks**                 |
|---------------|----------------------|--------------------|-------------------------------|-----------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                    | JSHAREImage                 |
| image         | Yes                  | NSData             | Image                         | The size cannot exceed 10 M |
| text          | No                   | NSString           | Description of shared content | No more than 140            |

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    
    message.mediaType = JSHAREImage;
    message.platform = platform;
    message.image = imageData;
```

#### 3)Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                              |
|---------------|----------------------|--------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                                                               |
| title         | No                   | NSString           | Title                     | Length cannot exceed 1K                                                                                                                                                                  |
| text          | No                   | NSString           | Description               | Length cannot exceed 140                                                                                                                                                                 |
| Url           | Yes                  | NSString           | Jump Url                  | No more than 512 characters                                                                                                                                                              |
| thumbnail     | No                   | NSDate             | Thumbnail                 | The size is less than 32k. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

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

### Direct Message on Sina Weibo

#### 1)Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                              |
|---------------|----------------------|--------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                                                               |
| title         | No                   | NSString           | Title                     | Length cannot exceed 1K and is not empty                                                                                                                                                 |
| text          | No                   | NSString           | Description               | Length cannot exceed 1K                                                                                                                                                                  |
| Url           | Yes                  | NSString           | Jump Url                  | No more than 512 characters                                                                                                                                                              |
| thumbnail     | No                   | NSDate             | Thumbnail                 | The size is less than 32k. When sharing does not provide a thumbnail, if the image parameter is not empty, JShare will crop the picture provided by this parameter to fit the thumbnail. |

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

#### 1）Share Texts (Not support by Messenger)

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks** |
|---------------|----------------------|--------------------|---------------------------|-------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText  |
| text          | Yes                  | NSString           | Share text                |             |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                                                  |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREImage                                                                                                                                                                                                  |
| images        | Yes                  | NSArray            | Image                     | The number of pictures is limited to six. If you share a single picture, the size of the picture should not exceed 12M. If you share more than one picture, the size of each picture should not exceed 700K. |
| text          | No                   | NSString           | Text                      |                                                                                                                                                                                                              |

```
    message.text = [NSString stringWithFormat:@"时间:%@ JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！",[self localizedStringTime]];
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.images = @[imageData,imageData];
    message.mediaType = JSHAREImage;
    message.platform = platform;
```

#### 3）Share Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                |
|---------------|----------------------|--------------------|---------------------------|------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                                                                |
| text          | No                   | NSString           | Text                      |                                                                                                            |
| videoAssetURL | Yes                  | NSString           | Video parameter           | Sharing the video type to facebook, facebookMessenger can only recognize ALAsset's ALAssetPropertyAssetURL |

```
    message.mediaType = JSHAREVideo;
    message.text = @"欢迎使用极光社会化组件JShare，SDK包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.videoAssetURL = assetURL.absoluteString;
    message.platform = platform;
```

#### 4)Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**            |
|---------------|----------------------|--------------------|---------------------------|------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink             |
| text          | No                   | NSString           | Description               |                        |
| Url           | Yes                  | NSString           | Jump Url                  | Share clicked jump url |

```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
```

### Twitter

#### 1）Share Texts

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks** |
|---------------|----------------------|--------------------|---------------------------|-------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREText  |
| text          | Yes                  | NSString           | Share text                |             |

```
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    message.mediaType = JSHAREText;
```

#### 2)Share Images

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                |
|---------------|----------------------|--------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREImage                                                                                                                                |
| image         | Yes                  | NSData             | Image                     | The size of a single image cannot exceed 5M.                                                                                               |
| images        | No                   | NSArray            | Image                     | Share multiple images with images, and the elements of the image array need to be of type NSData. The number of images is limited to four. |
| text          | No                   | NSString           | Text                      | No more than 140 characters                                                                                                                |

```
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.image = imageData;
    message.mediaType = JSHAREImage;
    message.platform = platform;
```

#### 3）Share Videos

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                                                                                      |
|---------------|----------------------|--------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHAREVideo                                                                                                                                                                                                      |
| text          | No                   | NSString           | Text                      | No more than 140 characters                                                                                                                                                                                      |
| videoData     | Yes                  | NSData             | Video parameter           | Videos shared to twitter, the size should not exceed 15mb, the time should be between 0.5 seconds and 30 seconds, the size should be between 32x32 and 1280x1024, the aspect ratio should be between 1:3 and 3:1 |

```    
    message.mediaType = JSHAREVideo;
    message.text = [NSString stringWithFormat:@"时间:%@ JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！",
    NSString *path = [[NSBundle mainBundle] pathForResource:@"jiguangVideoForTwitter" ofType:@"mp4"];
    NSData *data = [NSData dataWithContentsOfFile:path];
    message.videoData = data;
    message.platform = JSHAREPlatformTwitter;
```

#### 4)Share Links

| **Parameter** | **Whether Required** | **Parameter Type** | **Parameter Description** | **Remarks**                                                                                                                                       |
|---------------|----------------------|--------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| mediaType     | Yes                  | NS\_ENUM           | Share type                | JSHARELink                                                                                                                                        |
| text          | No                   | NSString           | Description               | The total length of url and text cannot exceed 280 bytes                                                                                          |
| Url           | Yes                  | NSString           | Jump Url                  | The total length of url and text can't exceed 280 bytes. It can have pictures or videos, but it can't bring pictures and videos at the same time. |
| videoData     | No                   | NSData             | Video parameter           | Videos shared to twitter should not exceed 15mb in size.                                                                                          |
| image         | No                   | NSData             | Image                     | The size of a single image cannot exceed 5M.                                                                                                      |
| images        | No                   | NSArray            | Image                     | Share multiple images with images, and the elements of the image array need to be of type NSData. The number of images is limited to four.        |

```
    message.mediaType = JSHARELink;
    message.url = @"https://www.jiguang.cn/";
    message.text = @"JShare SDK支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = platform;
    NSString *imageURL = @"http://img2.3lian.com/2014/f5/63/d/23.jpg";
    NSData *imageData = [NSData dataWithContentsOfURL:[NSURL URLWithString:imageURL]];
    message.image = imageData;
```

The specific use of parameters can refer to Demo.

## Check whether the webpage logs in with no Sina client

+(BOOL)isSinaWeiboWebLogined

## Log out the latest account on Sina.com

+(BOOL)sinaWeiboWebLogOut

## Check if there is a WeChat Client

+(BOOL)isWeChatInstalled

## Check if there is a QQ client

+(BOOL)isQQInstalled

## Check if there is a Sina Weibo client

+(BOOL)isSinaWeiBoInstalled

## Check if there is a Facebook client

+(BOOL)isFacebookInstalled

## Check if there is a Messenger client

+(BOOL)isFacebookMessengerInstalled

## Check if there is a Twitter client

+(BOOL)isTwitterInstalled

## Get user information on social platforms

### method - getSocialUserInfo

#### Interface Definition

+(void)getSocialUserInfo:(JSHAREPlatform)platform handler:(JSHARESocialHandler)handler

#### Interface Description

By calling the interface for user information acquiring, obtain user's ID, avatar, and other data on the third-party platform to construct the account system.

#### Parameter Description

-   platform: JSHAREPlatform enumeration type

-   handler: JSHARESocialHandler gets callbacks for user information

#### Call Example

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

#### Interface Definition

+(BOOL)isPlatformAuth:(JSHAREPlatform)platform

#### Interface Description

Check if the information expires after the user is authorized. Note: Just check whether the local token is within the validity period. If the corresponding social platform user manually cancels the authorization on the social platform, even if the local token is still in the validity period, it still fails.

#### Parameter Description

-   platform: Social platform enumeration

#### Call Example
```
BOOL isOauth = [JSHAREService isPlatformAuth:JSHAREPlatformQQ];
```

### method - cancelAuthWithPlatform

#### Interface Definition

+(BOOL)cancelAuthWithPlatform:(JSHAREPlatform)platfrom

#### Interface Description

Delete authorization information stored locally after the user is authorized.

#### Parameter Description

-   platform: Social platform enumeration

#### Call Example

```
BOOL cancelOauth = [JSHAREService cancelAuthWithPlatform:JSHAREPlatformQQ];
```

## Log Level Settings

### Method - setDebug

#### Interface Description

Set whether to print Debug level log information generated by sdk, and the default is NO (do not print Debug level log)

#### Interface Definition
```
+(void)setDebug:(BOOL)enable
```

#### Parameter Description
enable：Set YES to enable, set NO to turn off

#### Call Example

```
[JSHAREService setDebug:YES];
```