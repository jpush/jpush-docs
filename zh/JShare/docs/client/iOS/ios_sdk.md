# JSHARE 对外集成文档
##使用提示
本文匹配的JSHARE SDK 版本为：V1.0.0及以后版本。

<font color="#4590a3" size = "4px"> 产品说明</font>

JSHARE SDK 同时支持 微信、QQ、微博等社交平台的分享功能，集成、使用方便，可以有效的降低多平台分享的包体积。

<font color="#4590a3" size = "4px">压缩包内容</font> 

* JSHARE-ios-1.0.0.a静态库
* jcore-ios-x.x.x.a静态库
* JSHARE SDK 入口：JSHARESdk.h 头文件
* 一个完整的 iOS Demo 项目工程，这个工程演示了 JSHARE SDK 的基本用法，配置 SDK 时建议参考这个 Demo。

<font color="#4590a3" size = "4px">文档</font> 

正式编码前，请先去看JSHARE iOS SDK 相关文档或JSHARESdk.h文件。


[在线文档](https://docs.jiguang.cn)（本文档如有更新，会同时发布到此网站）

> 在编码时可参考Demo。

<font color="#4590a3" size = "4px">iOS系统</font> 


 * JSHARE 支持 iOS 7 及以上 iOS 版本；
 
 > 注：由于模拟器没有微博、微信等APP，所以无法用于JShare测试。

## 快速体验
* 双击压缩包里面的JShareDemo.xcodeproj 打开 Demo；
* 修改 AppDelegate.m 里面的appKey的值;
* 在项目的【General】页面 -> 【Identity】->【Bundle Identifier】 选项填写你在极光创建应用所上传的证书的Bundle id;
* 配置【General】页面 的【Siging】；
* 运行安装Demo到真机，即可。

##JSHARE SDK 集成步骤

<font color="#4590a3" size = "4px">添加JSHARE SDK</font> 

 解压sdk压缩包，将 Lib 下的所有文件复制到工程中。
	 
<font color="#4590a3" size = "4px">增加相关的 framework 依赖：</font> 

 - CFNetwork.framework
 - CoreFoundation.framework
 - CoreTelephony.framework
 - SystemConfiguration.framework
 - CoreGraphics.framework
 - Foundation.framework
 - UIKit.framework
 - Security.framework
 - libz.tbd (Xcode7以下版本是libz.dylib)
 - AdSupport.framework (获取IDFA需要；如果不使用IDFA，请不要添加)
 - libresolv.tbd (JPush 2.2.0及以上版本需要, Xcode7以下版本是libresolv.dylib)

<font color="#4590a3" size = "4px">在 AppDelegate.m 引用头文件</font> 

```
  //引用JSHARE SDK 头文件
  #import "JSHARESdk.h"
  //如需要使用idfa，请添加 AdSupport.framework 框架，并引用其头文件
  #import <AdSupport/AdSupport.h>
```


<font color="#4590a3" size = "4px">初始化JSHARE SDK</font> 



```
//请根据自己的需求配置分享平台信息
 JSHARELaunchConfig *config = [[JSHARELaunchConfig alloc] init];
    config.appKey = @"Your JiGuang AppKey";
    config.SinaWeiboAppKey = @"Your SinaWeibo Appkey";
    config.SinaWeiboAppSecret = @"Your SinaWeiboAppSecret";
    config.SinaRedirectUri = @"Your SinaRedirectUri";
    config.QQAppId = @"1105919571";
    config.WeChatAppId = @"Your config.WeChatAppId "; //wxa2ea563906227379
 [JSHARESdk setupWithConfig:config];
    
//如需更详细的JSHARE日志，请在这里调用以下接口：
 [JSHARESdk setDebug:YES];
    
    
```


<font color="#4590a3" size = "4px">添加回调接口</font> 

**接口说明**：回调接口，必要！在application:handleOpenURL:中调用。

**参数说明**：url：回调的 url

**调用示例**：

```
- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    [JSHARESdk handleOpenUrl:url];
    return YES;
}

```


<font color="#4590a3" size = "4px">配置 HTTPS 设置</font> 
 
  Apple将从2017年开始执行ATS(App Transport Security)，所有进行审核的应用中网络请求全部支持HTTPS，届时以下配置将会失效，请提前做好准备。
 
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

<font color="#4590a3" size = "4px">配置 ApplicationQueriesSchemes</font> 


需在iOS9/10就需要增加一个应用可跳转的白名单，即LSApplicationQueriesSchemes，否则将在SDK判断是否跳转时用到的canOpenURL时返回NO，无法得到分享回调。 

**在项目中的info.plist中加入应用白名单方法：**

* 右键 info.plist 选择 source code (具体设置在Build Setting -> Packaging -> Info.plist File可获取plist路径)
* 在打开的info.plist 的source code 里面添加以下内容：

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

<font color="#4590a3" size = "4px">添加 URL Types</font> 

* 进入【target】->【info】界面，添加以下几个URL Types:

这里是图片

各个平台的URL Schemes 格式说明：
这里是表格或者图片

##各个平台的分享规则
<font color="#4590a3" size = "4px">新浪微博分享规则</font> 

新浪微博分享支持文本内容、图片，注意需要分享链接应将链接的 URL 拼接在分享文本后面。

参数说明：

* detail：不能超过140个汉字
* image：图片最大不超过5M，仅支持JPEG、GIF、PNG格式

<font color="#4590a3" size = "4px">QQ分享规则</font> 

QQ 好友分享支持文字、单图、图文和音频分享

参数说明：

* detail：最多40个字符
* title：最多30个字符
* url ：URL 地址，最长 512 个字符
* thumbImage：预览图数据，最大1M字节
* image：最大5M字节

<font color="#4590a3" size = "4px">微信（好友、朋友圈、收藏）分享规则</font> 

微信三个平台中，好友的功能最完整，朋友圈不能分享表情、文件，收藏不能分享表情和应用。

参数说明：

* title：512Bytes以内
* url：不能为空且长度不能超过10K
* ThumbImage：内存大小不能超过32K的png图
* image:大小不能超过10M 





#end


