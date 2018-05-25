# iOS SDK FAQ

## What to do if the share failed?

In iOS 9/10, you need to add a whitelist that the application can jump to. If no whitelist is configured, the sharing is unsuccessful

Info.plist whitelist in the project can be viewed in: [ApplicationQueriesSchemes](https://docs.jiguang.cn/jshare/client/iOS/ios_sdk/#xcode)

## Why cannot return to the application after sharing successfully?

URL Types is not configured or the format of URL Schemes is incorrect; see: [URL Types Settings](https://docs.jiguang.cn/jshare/client/iOS/ios_sdk/#xcode)


## Why there is no statistics after sharing successfully?

Need to call + (BOOL) handleOpenUrl: (NSURL \*) url in the - (BOOL) application of the AppDelegate class: (UIApplication) application handleOpenURL: (NSURL) url, otherwise the data after successful sharing cannot be obtained.

## Report an error when Weibo logins to authorize：sso package or sign error

View the Bundle ID in the basic information of the [Sina Weibo open platform](http://open.weibo.com/)；

![](../image/bundle_id.png)

Set Bundle ID of the project as Bundle ID of the open platform.
