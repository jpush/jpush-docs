#iOS SDK FAQ




##分享不成功？


在iOS9/10下就需要增加一个应用可跳转的白名单，如果没配置白名单，则分享不成功。

在项目中的 info.plist 应用白名单看：<a href="https://docs.jiguang.cn/jshare/client/iOS/ios_sdk/#xcode">ApplicationQueriesSchemes</a>


##分享成功后，回不到应用

URL Types 没有配置或者 URL Schemes 格式不对；查看：<a href="https://docs.jiguang.cn/jshare/client/iOS/ios_sdk/#xcode">URL Types 设置</a>


##分享成功，但是统计不到数据
需要在AppDelegate类的 - （BOOL）应用程序中：（UIApplication* ）application handleOpenURL：（NSURL* ）url函数中，调用此函数+（BOOL）handleOpenUrl：（NSURL*）url;否则获取不到分享成功后的数据。


##新浪微博登录授权时报错，error：sso package or sign error
在[新浪微博开放平台](http://open.weibo.com/)的基本信息中查看 Bundle ID；

![](../image/bundle_id.png)

将项目的 Bundle ID 设置为开放平台的 Bundle ID 即可。