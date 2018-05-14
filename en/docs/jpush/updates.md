# Recent Updates

### JPush iOS SDK v3.0.8

#### Update Time

+ 2018-01-11

Change Log

+ Add api with the mobile phone number on the SDK side, using for SMS supplement function;
+ Add log switch in Service Extension
+ Fix several known issues;

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ The 3.0.8 version of JPush only supports JCore version 1.1.7 and above. Please upgrade JCore together when upgrading the SDK.
+ Notification Service Extension SDK is added in Lib of package from Version 3.0.8 , which can be used for the delivery of statistical notification. Developers should pay attention to adding it to Libs. Please refer to the integration guide for usage.
+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386 .
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v3.1.1

#### Update Time

+ 2018-01-09

Change Log

+ The api added with the mobile phone number on the SDK side is used for the SMS supplement function
+ Move the DaemonService component from the JPush module into the JCore module
+ Optimize JPush access service;
+ Fix several known bugs;

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-3.1.1.jar and jcore-android-1.1.9.jar, and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore119.so file in the corresponding CPU folder and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+  Update AndroidManifest.xml
    + Please update the JPush related component properties, Permission, Action, etc. against the example AndroidManifest. Replace your package name and appkey in the location of the Chinese prompt.
    + When the old user is upgrading, please note that the ContentProvider component has been added since the 3.0.9.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
    + For version after Android 5.0, using the application icon as notification icon may display exception, then please refer to res/drawable-xxxx/jpush_notification_icon as a dedicated notification icon. For details, see the instructions in the Android SDK Integration Guide, or the example.
+ If jsun is used to integrate JPush, there is no need to add JPush related components and resources. For details, refer to the official integration guide.

JPush Android SDK v3.1.0

#### Update Time

+ 2017-11-17

Change Log

+ Optimize the inter-process communication mechanism;
+ Optimize the heartbeat mechanism for maintaining long connections;
+ Adjust code structure to reduce the size of dynamic library files
+ Fix the problems reported by developers

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-3.1.0.jar and jcore-android-1.1.8.jar, and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore118.so file in the corresponding CPU folder and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please update the JPush related component properties, Permission, Action, etc. against the example AndroidManifest. Replace your package name and appkey in the location of the Chinese prompt.
    + When the old user is upgrading, please note that the ContentProvider component has been added since the 3.0.9.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file
    + For version after Android 5.0, using the application icon as notification icon may display exception, then please refer to res/drawable-xxxx/jpush_notification_icon as a dedicated notification icon. For details, see the instructions in the Android SDK Integration Guide, or the example.
+ If jsun is used to integrate JPush, there is no need to add JPush related components and resources. For details, refer to the official integration guide.

### JPush iOS SDK v3.0.7

#### Update Time

+ 2017-10-12

Change Log

+ Add iOS Extension sdk to measure the delivery of notifications
+ Optimize sdk internal code

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ JPush in the 3.0.7 version only supports JCore version of 1.1.6 and above. When upgrading the SDK, please upgrade JCore together.
+ Notification Service Extension SDK is added in Lib of package from Version 3.0.7 , which can be used for the delivery of statistical notification. Developers should pay attention to adding it to Libs. Please refer to the integration guide for usage.
+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v3.0.9

#### Update Time

+ 2017-09-25

Change Log

+ Add ContentProvider component for data synchronization.
+ Optimize SDK compatibility on Android 8.0.
+ Fix the problems reported by developers

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-3.0.9.jar and jcore-android-1.1.7.jar and delete the original Jiguang jar file. Replace the existing libjpushXXX.so file in the project with the libjcore117.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please update the JPush related component properties, Permission, Action, etc. against the example AndroidManifest. Replace your package name and appkey in the location of the Chinese prompt.
    + When the old user is upgrading,, please note that the ContentProvider component has been added in version 3.0.9.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
    + For version after Android 5.0, using the application icon as notification icon may display exception, then please refer to res/drawable-xxxx/jpush_notification_icon as a dedicated notification icon. For details, see the instructions in the Android SDK Integration Guide, or the example.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

JPush Android SDK v3.0.8

#### Update Time

+ 2017-07-26

Change Log

+ Fix: Bugs reported by several developers

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android-1.1.6.jar. Replace the original Jiguang jar file in the project with jpush-android-3.0.8.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore116.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+  Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

JPush Android SDK v3.0.7

#### Update Time

+ 2017-07-10

Change Log

+ Add a set of tag/alias operation interfaces
+ Optimize the problems with timeouts in tag/alias settings
+ Fix bugs reported by several developers

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.1.5.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.7.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore115.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

### JPush iOS SDK v3.0.6

#### Update Time

+ 2017-07-03

Change Log

+ Tag interface changes. It is recommended to use the new CRUD interface
+ Optimize connection protocols to improve connection speed and stability

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ The 3.0.6 version of JPush only supports JCore version of 1.1.5 and above. When upgrading the SDK, please upgrade JCore together.
+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v3.0.6

#### Update Time

+ 2017-05-08

Change Log

    1. Optimization: Data storage performance
    2. Optimization: Improve security of sdk
    3. Addtion: Set tag/alias to increase error code 6013 (error of time axis)

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.1.3.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.6.jar and delete the original Jiguang jar file. Use the libjcore113.so file in the corresponding CPU folder to replace the original libjpushXXX.so file in the project and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

JPush Android SDK v3.0.5

#### Update Time

+ 2017-04-14

Change Log

+ Optimize storage performance
+ Improve sdk stability

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.1.2.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.5.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore112.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

### JPush iOS SDK v3.0.5

#### Update Time

+ 2017-04-14

Change Log

+ Modify bugs to improve compatibility with other SDKs

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

### JPush iOS SDK v3.0.3

#### Update Time

+ 2017-04-01

Change Log

+ Optimization: Socket connect mechanism
+ Fix: Occasional crashes reported by SDK HTTP and enhances robustness

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+  If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC
    •
JPush Android SDK v3.0.3

#### Update Time

+ 2017-03-13

Change Log

+ Add: Supports for breathing lights of notification
+ Modification: Fix some compatibility issues reported by developers

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.1.1.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.3.jar and delete the original Jiguang jar file. Use the libjcore111.so file in the corresponding CPU folder to replace the original libjpushXXX.so file in the project and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

### JPush iOS SDK v3.0.2

#### Update Time

+ 2017-02-13

Change Log

+ Fix crash caused by DNS resolution failure, improving stability

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

### JPush iOS SDK v3.0.1

#### Update Time

+ 2017-01-09

Change Log

+ Fix: Known bugs.
+ Optimization: Operational performance.

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v3.0.1

#### Update Time

+ 2017-01-05

Change Log

+ Fix: Some known issues.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.1.0.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.1.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore110.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
+ If you use jcenter to integrate JPush, you do not need to add related components and resources. For details, refer to the official integration guide.

JPush Android SDK v3.0.0

#### Update Time

+ 2016-12-02

Change Log

+ Addition: Modular separation to integration of JCore and JPush. The original jar package is divided into two jar packages.
+ Addition: Encryption of message channel.
+ Addition: Supports for big text, big picture, inbox of native Android .
+ Addition: Support for the notification attributes priority and category.
+ Addtion: Support for adding Actions to the notification bar.
+ Fix: Some bugs reported by users.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Add jcore-android_v1.0.0.jar. Replace the original Jiguang jar file in the project with jpush-android_v3.0.0.jar and delete the original Jiguang jar file. Use the libjcore100.so file in the corresponding CPU folder to replace the original libjpushXXX.so file in the project and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the example AndroidManifest to update the JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the sample AndroidManifest.
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
(Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample of AndroidManifest configuration component)

### JPush iOS SDK v3.0.0

#### Update Time

+ 2016-12-02

Change Log

+ Addition: Modular separation to JCore, JPush, and support the integration with the Jiguang Statistic SDK.

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Opening of Bitcode is not supported by Xcode 8.0 or lower version.
+ The Jiguang Developer Service SDK adopts a modular usage model, which means the use of a core (JCore) + N services (JPush, JAnalytics, ...) to facilitate developers to use a single service or multiple services, at the same time, greatly optimize the problem of function modules duplication when multiple modules are used simultaneously.

Upgrade Guide

+ Note that JPush SDK for 3.0.0 and above will no longer support simulator with the processor as i386.
+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+  If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC
    •
### JPush iOS SDK v2.2.0

#### Update Time

+ 2016-10-20

Change Log

+ Fix known bugs to run more stably.
+ Encrypte the transmission messages to keep the information more secure.
+ Optimize version information reporting, log printing, etc to make the design more reasonable.
+ Optimize network processing such as IPv6 to make connections more reliable.

Upgrade Prompt

+ Recommend to upgrade!
+ Note: Add libresolv.tbd library, otherwise it will generate an error (required by 2.2.0 and above version)

Upgrade Guide

+ Add libresolv.tbd library, otherwise the compiler will report an error (required by 2.2.0 and above)
+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v2.2.0

#### Update Time

+ 2016-10-12

Change Log

+ Optimization and improvements: sdk internal https access to increase certificate authentication.
+ Optimizationand improvements: rich text pages to support two-finger zoom.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip package you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.2.0.jar and delete the original Jiguang jar file. Use the libjpush220.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+  Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
 (Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample of AndroidManifest configuration component)

### JPush iOS SDK v2.1.9

#### Update Time

+ 2016-09-07

Change Log

+ Addition: Thoroughly support new features of iOS 10.
+ Fix bug: Increase the stability of the SDK.
+ Optimization and improvements: Add interface to get registrationID, TagAlias ​​supports setting special characters.
+ Optimization and improvements: All SDK use HTTPS links.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v2.1.9

#### Update Time

+ 2016-08-26

Change Log

+ Improve the stability of access services

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.9.jar and delete the original Jiguang jar file. Use the libjpush219.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
(Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample AndroidManifest configuration component)

JPush Android SDK v2.1.8

#### Update Time

+ 2016-08-24

Change Log

+ Add support for jcenter integration.
+ Increase the ability to report crash logs in a timely manner
+ Optimize the code structure to significantly reduce the size of the jar package.
+ Optimize rich media push capabilities.
+ Fix negativeArraySizeException exceptions on several models.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.8.jar and delete the original Jiguang jar file. Use the libjpush218.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
 (Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample AndroidManifest configuration component)

JPush Android SDK v2.1.7

#### Update Time

+ 2016-06-28

Change Log

+ Optimization: Fix a null pointer problem.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.7.jar and delete the original Jiguang jar file. Use the libjpush217.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
(Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample AndroidManifest configuration component)

JPush Android SDK v2.1.6

#### Update Time

+ 2016-06-22

Change Log

+ Addition: Add special characters for tag, alias settings, including: @!#$&*+=.|$
+ Fix: Issue on setting silent time.
+ Optimization: Notification icon inside the SDK in debug mode.
+ Optimization: Deal with some possible crashes.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.6.jar and delete the original Jiguang jar file. Use the libjpush216.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
(Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample AndroidManifest configuration component)

### JPush iOS SDK v2.1.8

#### Update Time

+ 2016-06-21

Change Log

+ Optimize the communication mechanism under IPv6 network.
+ The number of tags is up to 1000, but the total length cannot exceed 7000 bytes.
+ The statistics report upgrades to https report.
+ Optimize to increase SDK stability.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

### JPush iOS SDK v2.1.7

#### Update Time

+ 2016-05-26

Change Log

+ Addtion: Support for IPv6 networks.
+ Optimization and improvements: Improve the user's backup app and revert to the new device with RegistrationID unchangeed.
+ Fix: Occasional crash problems with the SDK.
+ Optimization and improvements: Statistics of page length.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v2.1.5

#### Update Time

+ 2016-05-06

Change Log

+ Fix: The problem that only notifications are received on version 2.1.3 when push message with message and custom message together by API
+ Fix: The problems for unseccuessful setting after clearing Tag/alias in the extreme cases

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.5.jar and delete the original Jiguang jar file. Use the libjpush215.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+  Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.
(Note: To use Rich Media Push, place the resource in the package res into the project's corresponding folder and follow the sample AndroidManifest configuration component)

### JPush iOS SDK v2.1.6

#### Update Time

+ 2016-04-13

Change Log

+ Fix: Problem with version 2.1.5 reporting errors during simulator debugging.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC
    •
### JPush iOS SDK v2.1.5

#### Update Time

+ 2016-04-07

Change Log

+ Added Features: Increase IDFA (advertiser identifier) ​​settings interface. Developers can increase statistical accuracy by uploading IDFA values. The Jiguang SDK does not contain code that could actively calls for IDFA.
+ Optimization and improvements: Fix the accidental crash problem of the SDK and enhance robustness.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v2.1.3

#### Update Time

+ 2016-04-07

Change Log

+ Added: Templates of rich media popwin and landingPage.
+ Optimization: The introduction of aorg.apache.http already abandoned in android 6.0, and modify the http-related code to the google recommendation mode of httpUrlconnection.
+ Optimization: Reporting of crash log
+ Fix：The problem that the notification bar icon does not display in Android 5.0 and above version. The custom icon needs to replace the file drawable-hdpi/jpush_notification_icon, or use the custom notification bar interface.
+ Fix: The issue of scan error in the red umbrella.
+ Fix: Some anomalies that may cause a crash.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.3.jar and delete the original Jiguang jar file. Use the libjpush213.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.

JPush Android SDK v2.1.0

#### Update Time

+ 2016-03-04

Change Log

+ Addition: Support for Android 6.0 (Note: If compiling on compileSdkVersion 23, please add useLibrary 'org.apache.http.legacy' in build.gradle's android to support apache's http class);
+ Addition：Android 6.0 request permission interface: JPushInterface.requestPermission (Activity context), developers can call this interface in their own Activity page, request permission includes:
{"android.permission.READ_PHONE_STATE", "android.permission.WRITE_EXTERNAL_STORAGE", "android.permission.READ_EXTERNAL_STORAGE", "android.permission.ACCESS_FINE_LOCATION"}.
+ Fix: Bugs of setPushTime interface.
+ Fix: Bug of setLatestNotificationNumber interface.
+ Fix: Read/write exception of partial data caused by the detached process.
+ Fix: Crash reported by some test platforms.
+ Fix: The exception caused by the .so library not to crashing the application, and leverage the log to prompt the developer.
+ Optimization: Judgment strategy for device uniqueness.
+ Optimization: Adaptation of network state.
+ Optimization: Log output.

Upgrade Prompt

+ Strongly recommended to upgrade to fit Android 6.0

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.1.0.jar and delete the original Jiguang jar file. Use the libjpush210.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original aurora so file. Each type of so file can be found in the SDK download package.
+  Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.

JPush Android SDK v2.0.6

#### Update Time

+ 2016-01-15

Change Log

+ New features: Support templates of new rich media
+ Fix bug : Set alias/tag related bugs
+ Fix bug: Bug of building a notification on 2.3.x system.
+ Optimization: Optimize process log of init, sis, log and access
+ Optimization: Optimize the prompting log in the silence time, and push prohibiting time .

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original Jiguang jar file in the project with jpush-android-2.0.6.jar and delete the original Jiguang jar file. Replace the original aurora so file in the project with the libjpush206.so file in the corresponding CPU folder and delete the original Jiguang so file. The official website default compression package only provides the .so file of the arm architecture. To support the x86 and the mips architecture, please download the corresponding version from the “Resource Download” page of the official website.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file

### JPush iOS SDK v2.1.0

#### Update Time

+ 2016-01-12

Change Log

Mainly support for iOS 9 adapter.
+ Added Features: Add support for bitcode
+ Optimization and improvements: Demo adds support for iPhone 6 and 6plus
+ Optimization and improvements:APService changed to JPUSHService
+ Added Features: Increase appKey and channel and initialize API via code
+ Optimizations and Improvements: Optimize the poor network environment and long DNS resolution timeout
+ Optimization and improvements: Fix the bug where RegistrationID was not obtained when registering
+ Optimization and improvements: The static library file name changed from "libPushSDK-x.x.x.a" to "jpush-ios-x.x.x.a"

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder: first delete the old .a and .h files from the project and re-import the new .a and .h files (note that the new version replaces APService.h with JPUSHService.h)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v2.0.5

#### Update Time

+ 2015-11-06

Change Log

+ New features: Support for configuring PushService as a separate process
+ FixBug: Reolve the problem that the rich media push interface actionBar of some devices can't be fully covered horizontally
+ FixBug: Resolve crash issues caused by clicks on rich media pages
+ Optimization: Refactor the related code for rich media push
+ The demo project in the zip package supports Android Studio and Eclipse, which has its own corresponding AndroidManifest configuration

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder. Replace the original aurora jar file in the project with jpush-android-2.0.5.jar and delete the original Jiguang jar file. Use the libjpush205.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original Jiguang so file. The official website default compression package only provides the .so file of the arm architecture. To support the x86 and the mips architecture, please download the corresponding version from the “Resource Download” page of the official website.
+ Update AndroidManifest.xml
    + There are two AndroidManifest files prepared for the two development platforms Eclipse and AndroidStudio under the root directory of the package. Please refer to the examples to update JPush-related component properties, permissions, and actions. To use rich media push, place the resource in the tarball res into the corresponding folder of the project and configure the PushActivity component as per the example AndroidManifest
+ Add resource files
    + Add the resource file under the res folder to the corresponding folder under your project res/. Depending on the style of your application interface, you can modify the layout file's color, font, and other attributes, or modify icon under the the drawable folder. But be careful not to operate the file name and the component id in the layout file.

### JPush iOS SDK v1.8.8

#### Update Time

+ 2015-10-27

Change Log

+ Feature Modification: Fix the issue where archive compiling fails when starting bitcode in 1.8.7

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Delete the old .a file in the project and re-import the new .a file (special attention)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

### JPush iOS SDK v1.8.7

#### Update Time

2015-10-20

Change Log

+ Feature improvements: Add support for new feature bitcode of iOS9

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Delete the old .a file in the project and re-import the new .a file (special attention)
+ In the Xcode7 environment, replace the previously imported libz.dylib framework with libz.tbd (special attention)
+ Need to remove the old libPushSDK-Simulator.a (if it exists)
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v1.8.2

#### Update Time

+ 2015-09-30

Change Log

+ Fix Bug: Fix the problem that it may fail to connect JPush after upgrading from lower versions of 171 to later versions.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package at the same time
+ Newly add the .so package: libs/armeabi/libjpush182.so , and delete the original so-called old packages at the same time
+ As a result of rich media display requirements, add a res in SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package.
+ If you are using the old version of the API activityStarted/activityStopped, please replace it by the latest API onResume/onPause. You could refer to the Documentation Statistics API
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip and copy libs/x86/libjpush182.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip and copy libs/mips/libjpush182.so to your project's libs/mips/ directory.

JPush Android SDK v1.8.1

#### Update Time

+ 2015-09-07

Change Log

+ Optimization and improvements: Prevent open rich media pages from crashing due to layout files without rich media pages added.

Upgrade Prompt

+ Recommend to upgrade!
+ It is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package
+ As a result of rich media display requirements, a res folder is added to the SDK to store resource files. Users need to put the resource file in the corresponding folder into the project directory

Upgrade Guide

+ Newly add .jar package and delete the old jar package at the same time
+ Newly add .so package: libs/armeabi/libjpush181.so and delete the original so package of the old version at the same time
+ As a result of rich media display requirements, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip and copy libs/x86/libjpush181.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip and copy libs/mips/libjpush181.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.8.5

#### Update Time

2015-07-30

Change Log

+ Fix Bug: Resolve compilation error caused by conflicts with third-party libraries.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version;
+ Replace the .h file in the lib folder with the new version;
+ The project adds two libraries, libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.8.0

#### Update Time

+ 2015-07-27

Change Log

+ New features: Support for inter-application process pulls that integrates with the new version of the JPush SDK
+ Optimization and improvements: Optimize the preparation of rich media template impressions. (More features can be used after updating web background)

Upgrade Prompt

+ Recommend to upgrade!
+ It is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package
+ As a result of rich media display requirements, a res folder is added to the SDK to store resource files. Users need to put the resource file in the corresponding folder into the project directory

Upgrade Guide

+ Newly add .jar package and delete the old jar package at the same time
+ Newly add the .so package: libs/armeabi/libjpush180.so and delete the original so-called old packages at the same time
+ As a result of rich media display requirements, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush180.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush180.so to your project's libs/mips/ directory

### JPush iOS SDK v1.8.4

#### Update Time

2015-07-17

Change Log

+ Optimization and improvements: Improve the unable login to the server due to hijacking of domain name

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version;
+ Replace the .h file in the lib folder with the new version
+ The project adds two libraries, libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.7.5

#### Update Time

+ 2015-06-16

Change Log

+ Optimization and improvements: Optimize registration logic to prevent duplicate registrations for dual-card phones.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package at the same time
+ Newly add to the .so package: libs/armeabi/libjpush175.so and delete the original so-called old packages at the same time
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush175.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush175.so to your project's libs/mips/ directory.

JPush Android SDK v1.7.4

#### Update Time

+ 2015-05-11

Change Log

+ New features: Support 64-bit CPUs, and provide .so files for 64-bit CPUs on arm, x86, and mips platforms.
+ Optimization and improvements: Optimize code to prevent TransactionTooLargeException.
+ Optimization and improvements: Optimize the operation code for the local database.
+ Optimization and  improvements: catch AssertionError to avoid network interface errors at the framework level.
+ Optimization and improvements: Client-side printing with the API setLatestNotificationNum added
+ Optimization and improvements: Prompt corresponding information when the appKey in the Manifest is filled in as the appKey of the non-Android platform
+ Fix bug: Fix repeated attempt to register when create an app setting only with an iOS version.
+ Fix bug: Fix the issue that registration initiates when the appKey fills in.
+ Fix bug: Special operations cause the setting of number of retention notifications expire.
+ Fix bug that local notifications pop up repeatedly.
+ Fix bug: Fix crashes caused by external applications starting JPush internal components abnormally
+ Fix bug: Fix reported code to prevent ConcurrentModificationException.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add the .so package: libs/armeabi/libjpush174.so , and delete the original so package.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush174.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush174.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.8.3

#### Update Time

2015-03-25

Change Log

+ Fix bug: Fix the problem of cpu rising to 100% in a few cases
+ Fix bug: Low probability to write to file Crash
+ Optimization and improvements: Officially deprecated OpenUDID Interface

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version;
+ Replace the .h file in the lib folder with the new version;
+ The project adds two libraries, libz.dylib and Security.framework
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.7.3

#### Update Time

+ 2015-02-09

Change Log

+ Fix vulnerabilities: Fix the possible security issues when using webview in your code
+ Fix bug: Fix the problem that registration id may change when upgrading previous version to 172

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add the .so package: libs/armeabi/libjpush173.so , and also delete the old so versions of the old package.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip and copy libs/x86/libjpush173.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip and copy libs/mips/libjpush173.so to your project's libs/mips/ directory.

JPush Android SDK v1.7.2

#### Update Time

+ 2015-01-16

Change Log

+ Optimization and improvements: Android optimizes SIS multi-address retry strategy
+ Optimization and improvements: Android SDK supports more alternative access IP
+ Optimization and improvements: Optimize the Socket Connection Strategy
+ Optimization and improvements: Optimize the resolution od DNS domain name
+ Fix bug: Modify the conditions that Android SDK initiates to check for registration

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add  the .so package: libs/armeabi/libjpush172.so , and delete the original so package of the old version.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package
+ If you want to support x86 CPU models, download the separate x86 JPush SDK package, unzip and copy libs/x86/libjpush172.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip and copy libs/mips/libjpush172.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.8.2

#### Update Time

2014-12-11

Change Log

+ Optimization and improvements: Fix some issues that may cause crashes
+ Optimization and improvements: Fix the problem where the RegistrationID could not be obtained in some cases

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version
+ Replace the .h file in the lib folder with the new version;
+ The project adds two libraries, libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.7.1

#### Update Time

2014-12-03

Change Log

+ Optimization and improvements: Update internal protocol from 32-bit to 64-bit
+ Optimization and improvements: Optimize log print content of demo
+ Fix bug: The problem that there are always prompt for intergration failure regardless of whether the statistics are integrated when using TabActivity.
+ Fix bug: Fix null pointer exception due to absence of MainActivity or LAUNCHER in configuration file
+ Fix bug to support push custom message content as empty
+ Fix bug: Modify the name of the interface that provides the maximum number of notifications
+ Fix bug: Add @JavascriptInterface annotation for Java code called by JS

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add the .so package: libs/armeabi/libjpush171.so , and delete the original so package of the old version.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip and copy libs/x86/libjpush171.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip and copy libs/mips/libjpush171.so to your project's libs/mips/ directory.

JPush Android SDK v1.7.0

#### Update Time

2014-09-25

Change Log

+ Optimization and improvements: Optimize statistical accuracy of time based on server time
+ Fix bug: The problem that passing in getApplicationContext() will cause crash when integrating statistics analysis by calling onPause or onResume
+ Fix bug: The problem that 6008 will be reported when the length of tags is greater than 998

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package
+ Newly add .so package: libs/armeabi/libjpush170.so , and delete the original so package of the old version.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush170.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush170.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.8.1

#### Update Time

2014-09-23

Change Log

+ Optimization and improvements: Modify conflicts with some third-party SDK variables
+ Optimization and improvements: Fix Demo button exception of iOS5 version

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version
+ Replace the .h file in the lib folder with the new version
+ The project adds two libraries, libz.dylib and Security.framework
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

### JPush iOS SDK v1.8.0

#### Update Time

2014-09-19

Change Log

+ New features: Add support for iOS8
+ New features: Add Local Push API
+ New features: Add reporting of geographic information
+ New features: Add reporting of crash log
+ New features: Add modification of log level
+ Optimization and improvements: Modify escalation retry mechanism
+ Optimization and improvements: Fix the bug crashed when the callback class is released when setTagAlias
+ Optimization and improvements: New reference Demo

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version;
+ Replace the .h file in the lib folder with the new version
+ The project adds two libraries, libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.6.4

#### Update Time

2014-08-27

Change Log

+ New features: support Push v3 API to push notifications and custom messages at the same time, and broadcast them to App after receiving them;
+ New features: local notification API. A local notification can be customized through the API, and trigger the client notification at the point.
+ Fix bug: fix the problem that statistics are not reported when clicking on rich media notifications
+ Fix bug: fix heartbeat problem in r1.6.3 release

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add .so package: libs/armeabi/libjpush164.so , and delete the original so package of each old version.
+ If you are using the old version of the API activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API
+ Increase permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush164.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush164.so to your project's libs/mips/ directory.

JPush WinPhone SDK v1.0.2

#### Update Time

2014-08-14

Change Log

+ Optimization and improvements: The delegate of the Setup interface to obtain RegistrationID is not called
+ Optimization and improvements: excessive SDK cpu usage, resulting in caton of cocos2d-x for wp
+ Optimization and improvements: The SDK uses a more reasonable strategy to further reduce the impact on the UI thread
+ Optimization and improvements: The SDK works when the network type is NetworkUnkown
+ Optimization and improvements: Optimize statistics code

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add library: JPushSDK-v1.0.2.dll while deleting old dlls

### JPush iOS SDK v1.7.4

#### Update Time

2014-08-06

Change Log

New features: Add the settings of updating the badge value to the JPush server. This version of the SDK is used with the server-side push notification badge +1, so as to achieve different values ​​for the badge value when pushing iOS notification in batch.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version.
+ Replace the .h file in the lib folder with the new version.
+ The project adds two libraries: libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a.
+ If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.6.3

#### Update Time

2014-07-01

Change Log

+ Optimization and improvements: Improve startup speed of JPush service.
+ Optimization and improvements: Provide an interface to check JPush connection status.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package and delete the old jar package.
+ Newly add .so package: libs/armeabi/libjpush163.so , and delete the original so package of the old version.
+ If you are using the old version of the API for activityStarted/activityStopped, replace it by the latest API onResume/onPause and please refer to the Documentation Statistics API for adding permissions in AndroidManifest.xml.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration by referring to the latest version of the SDK download package.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.7.3

#### Update Time

2014-07-24

Change Log

+ Optimization and improvements: With API V3, better support for custom message parsing.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version
+ Replace the .h file in the lib folder with the new version
+ The project adds two libraries, libz.dylib and Security.framework.
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

### JPush iOS SDK v1.7.2

#### Update Time

2014-11-07

Change Log

+ New features: Add support for arm64 architecture
+ Optimization and improvements: Fully optimize the SDK architecture and maintain short-lived network connections while running in the back-end.
+ Optimization and improvements: Specifically consolidate x86 schema libraries of simulators into one file for easy management.

Upgrade Prompt

+ This SDK supports iOS 5.0 and above version
+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Need to remove the old libPushSDK-Simulator.a
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification

### JPush iOS SDK v1.7.1

#### Update Time

2014-07-24

Change Log

+ Fix Bug: Fix the problem that the empty version of the target->general page can cause crash;
+ Fix Bug: Fix the problem of compilation error occurred when  developers’ package static library contains the JPush iOS SDK and the XCode is version 5.0.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version
+ The project adds two libraries, libz.dylib and Security.framework
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush WinPhone SDK v1.0.0

#### Update Time

2014-07-24
JPush support for Windows Phone push is similar to the support for iOS push. The main functions are:：
+ Agent push notification to official push channel MPNs
+ Uniformly push interface;
+ Push statistics, etc.
A slight difference from JPush's push to the iOS platform is that Windows Phone push does not currently support in-app push, but only the notification toast.
The online features include
+ JPush WinPhone SDK version 1.0.0 for App integration
+ Set application to support for Windows Phone on the console;
+ Push notifications for Windows Phone devices on the console;
+ Push notifications for Windows Phone devices by calling API

### JPush iOS SDK v1.7.0

#### Update Time

2014-09-17

Change Log

+ New features: support for RegistrationID push
+ New features: increase page statistics reporting
+ Fix bug: Fix the bug crashed in a specific situation of the previous version

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Replace the .a file in the lib folder with the new version;
+ The project adds two libraries, libz.dylib and Security.framework
+ The new version no longer requires libPushSDK-Simulator.a. If your old version of the SDK contains this file, remove it.

JPush Android SDK v1.6.1

#### Update Time

2014-03-09

Change Log

+ Optimization and improvements: stopPush completely stops the Push Service and no longer responds to Receiver;
+ Optimization and improvements: Prompt in the notification bar only if the statistics tag is not added in Main Activity.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

    1. Newly add .jar package: libs/jpush-sdk-release1.6.1.jar and delete the old jar package.
    2. Newly add .so package: libs/armeabi/libjpush.so , and also delete the original so-called old packages.
    3. If you are using the old version of the API for activityStarted/activityStopped, use the latest API onResume/onPause instead, and please refer to the Andorid API
    4. Increase permissions <uses-permission android:name="android.permission.WRITE_SETTINGS" /> in AndroidManifest.xml
    5. If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package
    6. If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush.so to your project's libs/x86/ directory.
    7. If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush.so to your project's libs/mips/ directory.

JPush Android SDK v1.6.0

#### Update Time

2014-02-25

Change Log

    1. New features: Add statistical analysis API.
    2. New features: Add method to get RegistrationID. The server-side Push API can precisely push site-to-site based on this RegistrationID.

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

    1. Add the new .jar package: libs/jpush-sdk-release1.6.0.jar and delete the old jar packages.
    2. Newly add .so package: libs/armeabi/libjpush.so , and also delete the original so-called old packages.
    3. If you are using the old version of the API for activityStarted/activityStopped, use the latest API onResume/onPause instead, and refer to the documentation Andorid API
    4. Increase permissions  <uses-permission android:name="android.permission.WRITE_SETTINGS" />  in AndroidManifest.xml
    5. If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package.
    6. If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush.so to your project's libs/x86/ directory.
    7. If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush.so to your project's libs/mips/ directory.

### JPush iOS SDK v1.6.3

#### Update Time

2014-07-01

Change Log

+ Optimization and improvements: bug fix

Upgrade Prompt

+ This SDK supports iOS 5.0 and above version
+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Need to remove the old libPushSDK-Simulator.a
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

JPush Android SDK v1.5.6

#### Update Time

2014-01-03

Change Log

+ Optimization and improvements: Adjust SDK network policies to adapt to unstable environment of network interworking

Upgrade Prompt

+ Recommend to upgrade!

Upgrade Guide

+ Newly add .jar package: libs/jpush-sdk-release1.5.6.jar and delete old jar packages.
+ Newly add .so package: libs/armeabi/libjpush.so , and delete the original so package of the old version.
+ If you want to support x86 CPU models, download the separate x86 JPush SDK archive, unzip it and copy libs/x86/libjpush.so to your project's libs/x86/ directory.
+ If you want to support mips CPU models, download the separate mips JPush SDK archive, unzip it and copy libs/mips/libjpush.so to your project's libs/mips/ directory.
+ If you are upgrading from an earlier version, it is recommended to update the AndroidManifest.xml file configuration with reference to the latest version of the SDK download package.

### JPush iOS SDK v1.6.2

#### Update Time

2014-01-15

Change Log

+ Optimization and improvements: Adjust SDK network policies to adapt to unstable environment of network interworking

Upgrade Prompt

+ This SDK supports iOS 5.0 and above version
+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Need to remove the old libPushSDK-Simulator.a
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC

### JPush iOS SDK v1.6.0

#### Update Time

2014-02-25

Change Log

+ New features: Add support for arm64 architecture.
+ Optimization and improvements : Fully optimize the SDK architecture and maintain short-lived network connections while running in the back-end.
+ Optimization and improvements: Specifically consolidate x86 schema libraries of simulators into one file for easy management.

Upgrade Prompt

+ This SDK supports iOS 5.0 and above version
+ Recommend to upgrade!

Upgrade Guide

+ Replace the files in the lib folder
+ Need to remove the old libPushSDK-Simulator.a
+ If you are upgrading from version 1.2.7 or earlier version, please find Other Linker Flags in Build Settings and remove -all_load, -ObjC
+ About iOS 7 Background Push, JPush provides a tutorial document: iOS 7 Background Remote Notification
