# iOS SDK 常见问题

<style>
img[alt=jpush_ios] { width: 800px; }
img[alt=jpush_ios_5] { width: 500px; }## 
</style>


## iOS 如何推送自定义声音

客户端需要将声音文件导入工程里，选中工程Target -> Build Phrases -> Copy Bundle Resources
![jpush_ios_v](../image/ios_voice.png)

服务端推送时，需要指定iOS 平台下的sound参数，具体传入的值是声音文件名＋后缀。


<br />

## 为什么iOS收不到推送消息？

如果你确认 appKey 在 SDK 客户端与 Portal 上设置是一致，其他环节也按照文档正确地操作。但还是收不到推送消息。那么，有一定的可能性，是你在 Portal 上上传的证书，不是 APNs (Push) 证书。推送时指定的iOS推送环境和应用证书是同一个环境。

请参考[iOS 证书设置指南](ios_faq)再次检查证书选择是否正确。

请注意：iOS能接受消息的必要条件是：应用程序的证书要和你上传到jpush portal上的证书对应，如果你的程序是直接在xcode上运行的，你的应用部署环境必须是开发状态才能收到APNS消息。

温馨提示：目前api推送的时候可以通过参数apns_production可以指定推送环境，false为开发环境，true为生产环境。V3 api不带此参数则默认为生产环境，V3 api封装的sdk 默认为开发环境。如果api有传apns_production则以此值为准，否则以应用详情的部署环境为准。

<br />

## 为什么启动的时候出现 Did Fail To Register For Remote Notifications With Error的错误

程序运行的时候出现下面的错误信息：

	did Fail To Register For Remote Notifications With Error: Error Domain=NSCocoaErrorDomain Code=3000 "未找到应用程序的“aps-environment”的权利字符串" UserInfo=0x1c55e000 {NSLocalizedDescription=未找到应用程序的“aps-environment”的权利字符串}
	
这个是由于你的Provisioning Profile文件，不具备APNS功能导致的。请登陆Apple Developer 网站设置好证书，更新Provisioning Profile，重新导入Xcode。

或参考：[http://blog.csdn.net/stefzeus/article/details/7418552](http://blog.csdn.net/stefzeus/article/details/7418552)

<br />

## 如何在接收到 APN 的时候获取 APN 消息内容并进行跳转或做出响应处理？

[获取 APNs 推送内容](ios_api)

<br />

## 如何关闭 APN  推送？

关闭推送有以下两种方式关闭：

+ 在iOS系统设置的通知设置中更改对应app的推送设置（推荐）；
+ 在代码中调用 [[UIApplication sharedApplication] unregisterForRemoteNotifications]；

对应以上关闭方式的重新打开推送方法：

+ 在iOS系统设置的通知设置中修改对应app的推送设置；
+ 在代码中重新调用 [JPUSHService registerForRemoteNotificationTypes:]；

<br />

## App badge number（角标）如何更改与清空？

JPush 网站上推送 iOS 通知时，可在［可选设置］里面指定 badge 参数的值，如：1或"+1"。

api上指定badge的参数请看：[Push-API-v3#API-v3-ios](/ios_api/#badge)

客户端上报badge到JPush服务器的接口请看:[设置badge](ios_api/#badge)

关于badge ＋1的介绍，请看[APNs Notification badge](http://blog.jiguang.cn/ios_apns_badge_plus/)

<br />
## Icon Badge number 的清空方法：

+ APN 推送内容指定 badge number 为 0；
+ 在代码中使用如下代码清空 badge number：  [[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];

**注意**：

badge累加只能通过v3 api推送，且只有1.7.4版本以上才能支持。

<br />

## 为何推送一条 APN 后，点击通知中心的 APN 通知打开 App，可是 APN 通知在通知中心依然存在而未被删除？

如果推送 APN 时，Badge number 被指定为0 ，则可能出现 APN 消息在通知中心被点击后，尽管调用了   [[UIApplication sharedApplication] setApplicationIconBadgeNumber:0]; 但 APN 消息在通知中心不会被删除的情况。 这种情况可以按如下代码调用以清除通知中心的 APN 通知。

	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:1];
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];

如果仍有其他消息，则考虑清除 local notification 通知。（ [[UIApplication sharedApplication] cancelAllLocalNotifications] ）

<br />

## 出现Not get deviceToken yet. Maybe: your certificate not configured APNs?...错误日志时如何排除问题?

如果出现上述日志，则说明一段时间内都无法获取device token，那么：

+ 确认你的app配置了apns权限，如果未配置apns权限，则应该会出现此错误提示。
+ 确认你的app运行在ios真机而非模拟器上，且通知中心中对应app的通知权限没有完全关闭（alert/sound/badge至少有一个权限是打开的）。
+ 确认你的网络状况，与apple的服务器的连接是通过tcp的 5223端口连接，确认你网络的对应端口是否可用，可通过下列命令来确认这点：

		telnet 1-courier.push.apple.com 5223

+ 在代码中可在以下两个函数中断点以确认device token的获取状态。

		- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken;
		- (void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(NSError *)error;


	如果app运行进入	didFailToRegisterForRemoteNotificationsWithError 则说明app的APNS权限问题或者app运行在模拟器，参考 证书设置文档。

	如果app运行进入didRegisterForRemoteNotificationsWithDeviceToken 则说明运行正常，请确认你在此函数中的代码中有将token传递给jpush的调用：

		[JPUSHService registerDeviceToken:deviceToken];

+ 如果以上两个registerRemoteNotification的函数都未进入， 请确认你的代码中有注册申请apns的函数调用：

		[JPUSHService registerForRemoteNotificationTypes:];
		
+ 如果上述情况都已确认且未进入第4步的任意回调函数，则可以判断无法获取token的原因在于设备与apple的网络连通性问题（注：一个设备只有在未申请过token的情况下才会需要与apple的网络交互来获取token，已经获取过某一环境token的设备在无网络的情况下也能获取到对应环境的token（环境分为 开发/生产）），这种情况下切换网络能够在大部分情况下解决此问题。

+ 如果仍然有问题，请将上述步骤的结果以邮件附件的形式发送到JPush支持邮箱，我们将协助你解决此问题。

<br />

## 上传到appStore的版本为什么收不到推送？

+ 请确认xcode选择的生产证书和上传的证书的bundleid一致；
+ 如果是在jpush网站上推送，请确认新建通知时推送对象是否选择了生产环境；
+ 如果是v3 api推送，请确认是否使用了apns_production参数，值是否为：true；如果没有使用apns_production参数请确认jpush网站上该应用的部署环境是否已经切换到生产环境。

<br />

## iOS 平台上传证书一直为未通过状态

证书上传未通过的原因一般有：

+ 密码错误；
+ 上传的apns证书环境不一致；
+ 上传到控制台必须是apns证书，非apns证书会带来错误，还有其他的原因可能是开发者证书也可能是apns证书那里导出来的私钥

具体请看上传后显示的错误输出内容。

<br />

## 为什么日志里面会打印：You've implemented -[ <UIApplicationDelegate\> application:didReceiveRemoteNotification:fetchCompletionHandler:], but you still need to add "remote-notification" to the list of your supported UIBackgroundModes in your Info.plist.

这个主要是提示开发者如果要支持UIBackgroundModes，需要开启Remote notifications，具体操作可以看：[iOS 7 Background Remote Notification](ios_faq/#ios-7-background-remote-notification)


<br />
