# Integration Guide of JSMS iOS SDK

## SDK Instructions

-   Currently SDK supports iOS 7.0 and above.

### SDK package includes

-   The lib folder: Contains the header files JSMSSDK.h, JSMSConstant.h, and the static library file libsms-lib.a. The supported iOS versions are 7.0 and above.

-   pdf file: Integration Guide

-   demo folder: Example

## Integration Steps

### Create an Application

Register as a JPush developer. Create an app on the Jiguang web portal to get APPkey. If you are already a user of Jiguang 's other products and have created an app, you don't need to create it again.

### Import Development Package

Extract the SDK package and add the extracted JsmsSDK folder (including the header include, the static library libsms-lib.a, and JSMSSDK.h, JSMSConstant.h, two external interface files in the header directory) to the project directory.

### Build Settings

-   Increase -ObjC in Project Configuration, Build Settings, Other Linker Flags.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>After the 1.2.0 release, sdk fully supports https transport and does not require any additional AppTransportSecurity settings.
</div>

### Capabilities

Since SDK internal encryption protocol involves KeyChain, if you use Xcode8 and above environment to develop, please open the Capabilities-\>KeyChain Sharing option of Application Target when the simulator is running and debugging.

![jsms_ios][1]

### Add Initialization Code

```
 + (void)registerWithAppKey:(NSString * _Nonnull)appkey; 
```

**Interface Description**

Register the SDK interface: Create an application on the official website, and automatically generate an AppKey to identify the application.

**Call Example**

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      // Override point for customization after application launch.
  
      //从官网注册获取
      //注册短信验证的appKey
      [JSMSSDK registerWithAppKey:kAppKey];

      return YES;
 }
```

For more interfaces, refer to [iOS SDK API](ios_api) documentation.

[1]: ../image/Jsms-ios-1.png
