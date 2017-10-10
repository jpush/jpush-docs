# iOS SDK API

##SDK 接口说明：
JSHAREService 类，包含分享 SDK 的所有接口。  
JSHARELaunchConfig 类，分享 SDK 启动配置模型。  
JSHAREMessage 类，分享参数模型。  
JSHARESocial 类，社交平台授权信息模型。  
JSHARESocialUserInfo 类，社交平台用户信息模型，继承于 JSHARESocial。    

##SDK 初始化：

### Method - setupWithConfig

####接口说明：
初始化接口,建议在 application:didFinishLaunchingWithOptions 中调用。
####接口定义：
```
+(void)setupWithConfig:(JSHARELaunchConfig *)config
```

####参数说明：
config：JSHARELaunchConfig 类。
    
####调用示例：

   
   

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
    [JSHAREService setupWithConfig:config];
```

	
	
##处理平台回调
### Method - handleOpenUrl
####接口说明
处理平台回调，必要；
####接口定义
```
+(BOOL)handleOpenUrl:(NSURL *)url;
```
####参数说明
url：在 Appdelegate 的 application:handleOpenURL: 中调用。不调用此接口 JSHARE 将无法提供分享回调。
####调用示例

```
    - (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [JSHAREService handleOpenUrl:url];
    return YES;
    }
```

	
	
##分享参数模型
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-yw4l">参数</th>
    <th class="tg-yw4l">类型</th>
    <th class="tg-yw4l">参数说明</th>
  </tr>
  <tr>
    <td class="tg-yw4l">title</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">标题：长度每个平台的限制而不同。<br>微信好友：最大 512 字符。<br>微信朋友圈：最大 512 字符。<br>微信收藏：最大 512 字符。<br>QQ：最大 128 字符。<br>QQ空间：最大 128 字符。<br>新浪微博：分享链接类型，最大 1 K 字符。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">text</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">文本：文本内容，长度每个平台的限制而不同。<br>在分享非文本类型时，此字段作为分享内容的描述使用。<br>
微信好友：分享文本类型时，最大 10 K 字符。分享非文本类型，最大 1 K 字符。<br>微信朋友圈：分享文本类型时，最大 10 K 字符。分享非文本类型，最大 1 K 字符。<br>微信收藏：分享文本类型时，最大 10 K字符。分享非文本类型，最大 1 K 字符。<br>QQ：分享文本类型时，最大 1536 字符。分享非文本类型，最大 512 字符。<br>QQ空间：分享文本类型时，最大 128 字符。分享非文本类型，最大 512 字符。<br>新浪微博：最大 140 汉字。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">url</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">链接：根据媒体类型填入链接，长度每个平台的限制不同。分享非文本及非图片类型时，必要；<br>微信好友：最大 10 K 字符。<br>微信朋友圈：最大 10 K 字符。<br>微信收藏：最大 10 K 字符。<br>QQ：最大 512 字符。<br>QQ空间：最大 512 字符。<br>新浪微博：最大 512 字符。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">videoAssetURL</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">本地视频AssetURL:分享本地视频到 QQ 空间的必填参数，可传ALAsset的ALAssetPropertyAssetURL，或者PHAsset的localIdentifier。分享到视频类型至 facebook 、facebookMessenger 只能识别 ALAsset 的ALAssetPropertyAssetURL。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">thumbnail</td>
    <td class="tg-yw4l">NSData</td>
    <td class="tg-yw4l">缩略图：大小限制根据平台不同而不同。<br>微信好友：最大 32 K。<br>微信朋友圈：最大 32 K。<br>微信收藏：最大 32 K。<br>QQ：最大 1 M。<br>QQ空间：最大 1 M。<br>新浪微博：最大 32 K。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">image</td>
    <td class="tg-yw4l">NSData</td>
    <td class="tg-yw4l">图片：分享 JSHAREImage 类型，大小限制根据平台不同而不同，当分享 JSHARELink 类型时没有提供缩略图时，若此参数不为空，JSHARE 将会裁剪此参数提供的图片去适配缩略图。<br>微信好友：最大 10 M。<br>微信朋友圈：最大 10 M。<br>微信收藏：最大 10 M。<br>QQ：最大 5 M。<br>QQ空间：最大 5 M。<br>新浪微博：最大 10 M。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">images</td>
    <td class="tg-yw4l">NSArray</td>
    <td class="tg-yw4l">图片数组：分享到 QQ 空间 或 Facebook/Messenger 支持多张图片，图片数组的元素需要为 NSData 类型。<br>1.QQ 空间图片数量限制为20张。若只分享单张图片使用 image 字段即可。<br> 2.Facebook/Messenger 图片数量限制为6张。如果分享单张图片，图片大小建议不要超过12M；如果分享多张图片，图片大小建议不要超过700K，否则可能出现重启手机或者不能分享。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">mediaType</td>
    <td class="tg-yw4l">JSHAREMediaType</td>
    <td class="tg-yw4l">分享的媒体类型。必要参数</td>
  </tr>
  <tr>
    <td class="tg-yw4l">platform</td>
    <td class="tg-yw4l">JSHAREPlatform</td>
    <td class="tg-yw4l">分享的目标平台。必要参数</td>
  </tr>
  <tr>
    <td class="tg-yw4l">mediaDataUrl</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">分享 JSHAREAudio 类型至微信平台或 QQ 平台时，音乐数据 url 地址。<br>微信好友：最大 10 K 字符。<br>微信朋友圈：最大 10 K 字符。<br>微信收藏：最大 10 K 字符。<br>QQ：最大 512 字符。<br>QQ空间：最大 512 字符。<br>新浪微博：最大 512 字符。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">extInfo</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">分享 JSHAREApp 类型至微信平台时，第三方程序自定义的简单数据。</td>
  </tr>
  <tr>
    <td class="tg-yw4l">fileData</td>
    <td class="tg-yw4l">NSData</td>
    <td class="tg-yw4l">分享 JSHAREFile 类型或者 JSHAREApp 类型至微信平台时，对应的 File 数据以及 App 数据，最大 10 M</td>
  </tr>
  <tr>
    <td class="tg-yw4l">fileExt</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">分享 JSHAREFile 类型至微信平台时，对应的文件后缀名，分享文件必填，否则会导致分享到微信平台出现不一致的文件类型,最大 64 字符</td>
  </tr>
  <tr>
    <td class="tg-yw4l">emoticonData</td>
    <td class="tg-yw4l">NSData</td>
    <td class="tg-yw4l">分享 JSHAREEmoticon 类型至微信平台时，对应的表情数据，最大 10 M</td>
  </tr>
  <tr>
    <td class="tg-yw4l">sinaObjectID</td>
    <td class="tg-yw4l">NSString</td>
    <td class="tg-yw4l">分享至新浪微博平台时，分享参数的一个标识符，默认为 “objectId”。最大 255 字符</td>
  </tr>
</table>


##发起分享
### Method - share
####接口说明
调用此接口发起分享
####接口定义
```
 +(void)share:(JSHAREMessage *)message
      handler:(JSHAREStateHandler)handler
```
####参数说明
message：JSHAREMessage 类<br>
handler：分享结果的回调。
        
####调用示例：
    
    
```
    JSHAREMessage *message = [JSHAREMessage message];
    message.text = @"欢迎使用极光社会化组件 JShare，SDK 包体积小，集成简单，支持主流社交平台、帮助开发者轻松实现社会化功能！";
    message.platform = JSHAREPlatformWechatSession;
    message.mediaType = JSHAREText;
    [JSHARESdk share:message handler:^(JSHAREState state, NSError *error) {
          NSLog(@"分享回调");
    }];
```
    
        
    
##检查不存在新浪客户端情况的网页端是否登陆

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
 
## 获取社交平台用户信息
###method - getSocialUserInfo
#### 接口定义：
+(void)getSocialUserInfo:(JSHAREPlatform)platform
                  handler:(JSHARESocialHandler)handler
                  
#### 接口说明：
通过调用获取用户信息接口，获取用户在第三方平台的用户 ID、头像等资料完成账号体系的构建。

#### 参数说明：

* platform : JSHAREPlatform 枚举类型
* handler : JSHARESocialHandler 获取用户信息的回调

####调用实例：

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
#### 接口定义：
+(BOOL)isPlatformAuth:(JSHAREPlatform)platform
#### 接口说明：
检查用户授权之后信息是否过期。注意：仅仅检验本地 token 是否在有效期内，假如对应的社交平台用户在社交平台手动取消了授权，即使本地 token 还在有效期内，但是还是失效的。

#### 参数说明：
* platform: 社交平台枚举 

#### 调用实例：
```
BOOL isOauth = [JSHAREService isPlatformAuth:JSHAREPlatformQQ];
```
### method - cancelAuthWithPlatform
#### 接口定义：
+(BOOL)cancelAuthWithPlatform:(JSHAREPlatform)platfrom

#### 接口说明：
删除用户授权之后的储存在本地的授权信息。

#### 参数说明：
* platform: 社交平台枚举 

#### 调用实例：
```
BOOL cancelOauth = [JSHAREService cancelAuthWithPlatform:JSHAREPlatformQQ];
;
```


## 日志等级设置
### Method - setDebug
#### 接口说明：
设置是否打印 sdk 产生的 Debug 级 log 信息, 默认为 NO (不打印 Debug 级 log)
#### 接口定义：
```    
+(void)setDebug:(BOOL)enable
```
#### 参数说明：
enable：设置为 YES 开启，设置为 NO 关闭

#### 调用示例： 
        
```
[JSHAREService setDebug:YES];
```
      
      
      


