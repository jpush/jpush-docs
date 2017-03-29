# JSHARE 对外集成文档
##使用提示
本文是 JSHARE iOS SDK 的标准集成指南文档。
匹配的 SDK 版本为：V1.0.0及以后版本。

* 如果你想要快速测试、请参考本文在几分钟内跑通 Demo。
* 极光文档官网上有相关的所有指南、API、教程等全部的文档。包括本文档的更新版本，都会及时地发布到该网站上。
* [极光社区](https://community.jiguang.cn/)网站：大家对文档有疑惑，以及产品出现问题，可以到极光社区来提问题，可以即时得到回应。

##产品功能说明
JSHARE SDK 可以让用户不用额外集成第三方平台的 SDK 实现平台间的分享功能，可以有效的降低包体积。

###主要场景：

* 将分享内容分享到 QQ、微信、新浪微博三个主要的社交平台。

###集成压缩包内容

* JSHARE-ios-1.0.0.a静态库
* jcore-ios-x.x.x.a静态库
* JSHARE SDK 入口 JSHARESdk.h 头文件
* 一个完整的 iOS Demo 项目工程，这个工程演示了 JSHARE SDK 的基本用法，配置 SDK 时建议参考这个 Demo。

###iOS SDK 支持版本
目前 JSHARE 只支持 iOS 7 以上 iOS 版本。

##JSHARE SDK 集成步骤

* 解压压缩包，将 Lib 下的所有文件复制到工程中，即可开始使用 SDK。
* 增加相关的 framework 依赖：
UIKit,SystemConfiguration,CoreTelephony,CoreGraphics,Security,Foundation,CoreLocation,CoreFoundation,CFNetwork,libz.tbd,libresolv.tbd

* 添加以下代码到 AppDelegate.m 引用头文件的位置


```
// 引入JSHARE功能所需头文件
#import "JSHARESdk.h"
// 如果需要使用idfa功能所需要引入的头文件（可选）
#import <AdSupport/AdSupport.h>
```

##SDK 主要接口说明
JSHARELaunchConfig类，JSHARE SDK 启动配置模型。
JSHARESdk类，包含 JSHARE SDK 的所有接口。

 
**1.+ (void)setupWithConfig:(JSHARELaunchConfig *)config**
接口说明：初始化接口。建议在 application:didFinishLaunchingWithOptions: 中调用。
参数说明：

* config：JSHARELaunchConfig类的实例。
调用示例：

```
    JSHARELaunchConfig *config = [[JSHARELaunchConfig alloc] init];
    config.appKey = @"Your Jiguang Appkey";
    config.SinaWeiboAppKey = @"727232518";
    config.SinaWeiboAppSecret = @"9b63b2c95a200e4fc671ca97a6b01ba9";
    config.SinaRedirectUri = @"https://www.jiguang.cn/";
    config.QQAppId = @"1105864531";
    config.WeChatAppId = @"wxa2ea563906227379";
    [JSHARESdk setupWithConfig:config];

```

**2.+ (void)share:(JSHAREMessage *)message
     platform:(JSHAREPlatform)platform
      handler:(JSHAREStateHandler)handler**
参数说明：

* message：JSHAREMessage 类的实例
* platform：JSHAREPlatform 枚举类型
* handler：JSHAREStateHandler 分享后的回调      

调用示例：

```
JSHAREMessage *message = [JSHAREMessage message];
    message.detail = @"来自JShare的分享";
    message.platform = JSHAREPlatformQQ;
    message.mediaType = JSHAREText;
    [JSHARESdk share:message platform:JSHAREPlatformQQ handler:^(JSHAREState state, NSError *error) {
        if (!error) {
          NSLog(@"分享ok");
        }
    }];
```

**3.+ (BOOL)handleOpenUrl:(NSURL *)url**
接口说明：回调接口，必要！在application:handleOpenURL:中调用。

参数说明：

* url：回调的 url

调用示例：

```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [JSHARESdk handleOpenUrl:url];
    return YES;
}

```
其他接口作用详见 JSHARESdk.h 文件中的接口注释。


##Xcode 中的设置
###HTTPS 设置
 > Apple将从2017年开始执行ATS(App Transport Security)，所有进行审核的应用中网络请求全部支持HTTPS，届时以下配置将会失效，请提前做好准备。
 
 目前 JSHARE 支持不存在新浪微博客户端情况下的网页分享，但是由于新浪的 api 尚未针对 https 做优化所以需要针对新浪的做对应的 https 设置。在 JSHARE 中是默认关闭新浪微博的网页端分享的，如需使用这个功能则需要在JSHARELaunchConfig类的实例中将 **isSupportWebSina** 属性设置为 YES。
 
 以iOS10 SDK编译的工程会默认以SSL安全协议进行网络传输，即HTTPS，如果依然使用HTTP协议请求网络会报系统异常并中断请求。目前可用如下这种方式保持用HTTP进行网络连接：   
 
在info.plist中加入安全域名白名单(右键info.plist用source code打开)

```
<key>NSAppTransportSecurity</key>
<dict>
    <!-- 配置允许 http的任意网络End-->
   <key>NSExceptionDomains</key>
   <dict>
       <!-- 集成新浪微博对应的HTTP白名单-->
       <key>sina.com.cn</key>
       <dict>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionAllowsInsecureHTTPLoads</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <key>sinaimg.cn</key>
       <dict>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionAllowsInsecureHTTPLoads</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <key>sinajs.cn</key>
       <dict>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionAllowsInsecureHTTPLoads</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <key>sina.cn</key>
       <dict>
           <!-- 适配iOS10 -->
           <key>NSExceptionMinimumTLSVersion</key>
           <string>TLSv1.0</string>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <key>weibo.cn</key>
       <dict>
           <!-- 适配iOS10 -->
           <key>NSExceptionMinimumTLSVersion</key>
           <string>TLSv1.0</string>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <key>weibo.com</key>
       <dict>
           <!-- 适配iOS10 -->
           <key>NSExceptionMinimumTLSVersion</key>
           <string>TLSv1.0</string>
           <key>NSIncludesSubdomains</key>
           <true/>
           <key>NSThirdPartyExceptionAllowsInsecureHTTPLoads</key>
           <true/>
           <key>NSThirdPartyExceptionRequiresForwardSecrecy</key>
           <false/>
       </dict>
       <!-- 新浪微博-->  
   </dict>
</dict>
```

### 配置ApplicationQueriesSchemes
在iOS9/10下就需要增加一个应用可跳转的白名单，即LSApplicationQueriesSchemes，否则将在SDK判断是否跳转时用到的canOpenURL时返回NO，进而只进行webview分享/分享失败。 在项目中的info.plist中加入应用白名单，右键info.plist选择source code打开(具体设置在Build Setting -> Packaging -> Info.plist File可获取plist路径)

```
<key>LSApplicationQueriesSchemes</key>
<array>
    <!-- 微信 URL Scheme 白名单-->
    <string>wechat</string>
    <string>weixin</string>

    <!-- 新浪微博 URL Scheme 白名单-->
    <string>sinaweibohd</string>
    <string>sinaweibo</string>
    <string>sinaweibosso</string>
    <string>weibosdk</string>
    <string>weibosdk2.5</string>

    <!-- QQ、Qzone URL Scheme 白名单-->
    <string>mqqapi</string>
    <string>mqq</string>
    <string>mqqOpensdkSSoLogin</string>
    <string>mqqconnect</string>
    <string>mqqopensdkdataline</string>
    <string>mqqopensdkgrouptribeshare</string>
    <string>mqqopensdkfriend</string>
    <string>mqqopensdkapi</string>
    <string>mqqopensdkapiV2</string>
    <string>mqqopensdkapiV3</string>
    <string>mqqopensdkapiV4</string>
    <string>mqzoneopensdk</string>
    <string>wtloginmqq</string>
    <string>wtloginmqq2</string>
    <string>mqqwpa</string>
    <string>mqzone</string>
    <string>mqzonev2</string>
    <string>mqzoneshare</string>
    <string>wtloginqzone</string>
    <string>mqzonewx</string>
    <string>mqzoneopensdkapiV2</string>
    <string>mqzoneopensdkapi19</string>
    <string>mqzoneopensdkapi</string>
    <string>mqqbrowser</string>
    <string>mttbrowser</string>
</array>
```

###添加 URL Types
参考 JSHARE 的对外 demo 工程设置：
<img src="../image/url_types.jpeg">

下图是各个平台的URL Schemes 格式：

| 平台 | 格式 | 举例 |
| ------| ------ | ------ |
| QQ | "tencent"+appID | tencent1105864531 |
| 微信 | 微信的AppID | wx8c923fa84d6a555d |
| 新浪 | "wb"+sina的appkey | wb568898243 |

##各个平台的分享规则
###新浪微博分享规则
新浪微博分享支持文本内容、图片，注意需要分享链接应将链接的 URL 拼接在分享文本后面。

参数说明：

* detail：不能超过140个汉字
* image：图片最大不超过5M，仅支持JPEG、GIF、PNG格式

###QQ分享规则
QQ 好友分享支持文字、单图、图文和音频分享

参数说明：

* detail：最多40个字符
* title：最多30个字符
* url ：URL 地址，最长 512 个字符
* thumbImage：预览图数据，最大1M字节
* image：最大5M字节

###微信（好友、朋友圈、收藏）分享规则：
微信三个平台中，好友的功能最完整，朋友圈不能分享表情、文件，收藏不能分享表情和应用。

参数说明：

* title：512Bytes以内
* url：不能为空且长度不能超过10K
* ThumbImage：内存大小不能超过32K的png图
* image:大小不能超过10M 

#end

