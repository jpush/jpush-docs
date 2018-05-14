
# iOS SDK FAQ

## iOS 9 Integration

### Changes of iOS 9 affect the SDK section:

-   Added bitCode encoding format. When the SDK does not support bitCode, the bitCode option cannot be enabled as the user is integrating.

    -   Phenomenon: It cannot compile after the user integrates the SDK. The error log contains bitCode related error information.

-   By default, the https connection is used. If the request is http, the plist needs to be manually configured to support the http service. Currently, all requests of our server go through HTTP services.

    -   Phenomenon: All JPush-related http services will prompt connection errors or connection timeouts after the user integrates the SDK. This may be the problem.

### bitCode Solution

JPush iOS SDK v1.8.7 or later SDK has added support for iOS9's new feature bitCode. The JMessage iOS SDK v2.0.0 and above supports bitCode.

### Https Solution

SDK does not provide https address version

-   Requires users to actively add an NSAppTransportSecurity type Dictionary to the Info.plist of the current project.

-   Add NSAllowsArbitraryLoads type Boolean under NSAppTransportSecurity with the value set to YES

## How to push custom sounds for iOS？

The client needs to import the sound file into the project, select the project Target -\> Build Phrases -\> Copy Bundle Resources

![jpush_ios_v](../image/ios_voice.png)

When the server pushes, you need to specify the sound parameter of the iOS platform. The specific value is the sound file name + suffix.

## Why doesn't iOS receive push messages?**

If you confirm that the appKey is set on the SDK client and Portal, and the other sections follow the documentation correctly, but still can not receive push messages, there is a certain possibility that the certificate you uploaded on Portal is not an APNs (Push) certificate. The iOS push environment and application certificate specified during push need to the same environment.

Please refer to the [iOS Certificate Setup Guide](ios_cer_guide) again to check if the certificate selection is correct.

Please note that the necessary condition for iOS to accept messages is that the application's certificate should correspond to the certificate you uploaded to the jpush portal. If your program is run directly on xcode, your application deployment environment must be developed to receive APNS message.

Reminder: When the api is pushed, the push environment can be specified through the parameter apns\_production. False is the development environment, true is the production environment. V3 api without this parameter defaults to the production environment. The sdk packaged by V3 api defaults to the development environment. If apis\_apns\_production is passed, then this value prevails; otherwise, the application deployment environment prevails.

## Why does“Did Fail To Register For Remote Notifications With Error”appear when starting?

The following error message appears when the program is running：

did Fail To Register For Remote Notifications With Error: Error Domain=NSCocoaErrorDomain Code=3000 "未找到应用程序的“aps-environment”的权利字符串" UserInfo=0x1c55e000 {NSLocalizedDescription=未找到应用程序的“aps-environment”的权利字符串}

This is because your Provisioning Profile file does not have APNS functionality. Please visit the Apple Developer website to set up a certificate, update the Provisioning Profile, and re-import Xcode.

Or refer to: [http://blog.csdn.net/stefzeus/article/details/7418552](http://blog.csdn.net/stefzeus/article/details/7418552)

## How to obtain the APN message content and jump or respond to it when receiving the APN?

[Get Push Content of APNs](ios_api/#apns)

## How to turn off APN push?

By calling the code
```
// iOS 8 以上可用此方法
[[UIApplication sharedApplication] openURL:[NSURL URLWithString:UIApplicationOpenSettingsURLString]] 
```

Go to your application's settings page and click "Notification Settings", The user can change the status of "Allow Notification".

## How to change and clear the app badge number?

When pushing iOS notifications on the JPush website, you can specify the value of the badge parameter in \[Optional Settings\], such as: 1 or "+1".  
For the parameters of specifying badge on api, please look at: [Push API](../../server/push/rest_api_v3_push/#notification)

About the interface for the client reporting the badge to the JPush server, please look at: [Setting the badge](ios_api/#badge)

For an introduction to badge +1, see [APNs Notification badge](http://blog.jiguang.cn/ios_apns_badge_plus/)

## Clear method of Icon Badge number：

-   APN push content specifies badge number as 0；

-   Use the following code to clear the badge number: \[\[UIApplication sharedApplication\] setApplicationIconBadgeNumber:0\]

**Note:**：

The accumulation of the badge can only be pushed by the v3 api, and can only be supported by versions 1.7.4 and above.

## Why the APN notification remained in the notification center and was not deleted after pushing a APN and clicking the APN notification center to open the App?

If the Badge number is specified as 0 when the APN is pushed, it may happen that the APN message is not deleted in the notification center after clicking in the notification center and calling 

\[\[UIApplication sharedApplication\] setApplicationIconBadgeNumber:0\]. The following code can be used to clear the notification center's APN notification.

```
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:1];
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];
```

If there are still other messages, consider clearing the local notification. (\[\[UIApplication sharedApplication\] cancelAllLocalNotifications\])

## How to troubleshoot the problem if Not get deviceToken yet. Maybe: your certificate not configured APNs?... error log occurs?

If the above log appears, it means that the device token cannot be obtained within a period of time. Then:：

-   Verify that your app is configured with apns privilege. If apns privilege is not configured, this error message should appear.。

-   Make sure that your app is running on the ios real machine instead of the emulator, and the notification permission of the corresponding app in the notification center is not completely closed (at least one permission for the alert/sound/badge is open).

-   Confirm your network status. The connection to the apple server is through the tcp port 5223. Make sure the corresponding port of your network is available. You can confirm this by the following command：

-   telnet 1-courier.push.apple.com 5223

-   The following two function breakpoints can be used in the code to confirm the acquisition status of device token

-   \- (void)application:(UIApplication \*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData \*)deviceToken;

-   \- (void)application:(UIApplication \*)application didFailToRegisterForRemoteNotificationsWithError:(NSError \*)error;

> If the app runs into didFailToRegisterForRemoteNotificationsWithError, it indicated that the app's APNS permissions issue or the app is running on the emulator. Refer to the Certificate Setup Documentation.
>
> If the app runs into didRegisterForRemoteNotificationsWithDeviceToken then it works fine. Please make sure that you pass the token to jpush in the code of this function.：
>
> \[JPUSHService registerDeviceToken:deviceToken\];

-   If none of the above two registerRemoteNotification functions enter, make sure your code has a function call to register for apns：

-   \[JPUSHService registerForRemoteNotificationTypes:\];

-   If the above conditions have been confirmed and no callback function of step 4 has been entered, then the reason why the token cannot be obtained is due to the network connectivity problem between the device and the apple (Note: A device only needs to interact with the apple network to obtain tokens when it never applied for token. Devices that have already obtained an environment token can also obtain tokens of corresponding environment even there is no network(environment is divided into development/production). In this case, switching the network can solve this problem under most circumstances.

-   If you still have problems, please send the results of the above steps to the JPush support e-mail by attachment. We will assist you to resolve this issue.

**Why the version uploaded to the AppStore cannot receive push?**

-   Please confirm that the bundled id of the production certificate selected by xcode is the same as the bundled certificate uploaded.

-   If you are pushing on the jpush website, please confirm whether the push object has selected the production environment when you create a new notification.

-   If you are pushing by the v3 API, check whether the aps production\_parameter is used and whether the value of parameter is true. If the apns\_production parameter is not used, check whether deployment environment of the application on the jpush website has been switched to the production environment.

**Uploading certificates on the iOS platform has failed**

Reasons for failing to upload a certificate are generally：

-   Wrong password；

-   The environment of uploaded apns certificate is inconsistent；

-   It must be apns certificate to upload to the console, otherwise non-apns certificate will bring errors. Other reasons may be the developer certificate, and may also be private key exported from the apns certificate

For details, see the error output displayed after uploading.

## Why does the log print: You've implemented -\[ \<UIApplicationDelegate\>** application:didReceiveRemoteNotification:fetchCompletionHandler:\], but you still need to add "remote-notification" to the list of your supported UIBackgroundModes in your Info.plist.

This is mainly to prompt developers that supporting UIBackgroundModes needs to open Remote notifications. The specific operation can be seen in: [iOS 7 Background Remote Notification](ios_new_fetures/#ios-7-background-remote-notification)
