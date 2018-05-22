# Recent Updates

### JAnalytics iOS SDK v1.2.1

#### Update Time

+ 2018-03-12

#### Change Log

+ Add real-time reporting function. If the default is to report in a timely manner, the API can be used to disable the function or adjust the reporting frequency.
+ When calling identifying_account and detach_account, the SDK automatically triggers the initialization method if it is not successfully initialized and then continues to execute the corresponding API function.

#### Upgrade Prompt

+ Recommend to upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics iOS SDK v1.2.0

#### Update Time

+ 2018-01-15

#### Change Log

+ Add user dimension binding/unbinding functions
+ Increase timed reporting function.
+ Optimize internal logic.

#### Upgrade Prompt

+ Recommend to upgrade!

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics Android SDK v1.2.0

#### Update Time

+ 2018-01-15

#### Change Log

+ Add statistical dimension-account, through which users can register account information and disassociate information.
+ Add statistical frequency setting, through which users can set the automatic reporting period of statistical data.
+ Fix some known issues.

#### Upgrade Prompt

+ Recommend to upgrade!

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update the library file and open the libs folder. Replace the original JAnalytics sdk jar files in the project with janalytics-android-v1.x.x.jar, and delete the original JAnalytics sdk jar files. Replace the original Jiguang jcore jar file in the project with jcoe-android-v1.x.x.jar and delete the original Jiguang jcore jar file. Use the libjcore1xx.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original Jiguang so file.
+ Update AndroidManifest.xml. There is an AndroidManifest file in the root directory of the compressed package, which is equipped with permissions required for sdk statistics. Please update JAnlytics-related component properties, permissions, etc. according to the examples. Note: All of the Jiguang Android sdk use the same key and channel. For details, see the instructions in the JAnalytics Android SDK Integration Guide, or the examples in the example.
+ If integrate JAnalytics by jcenter, you do not need to add related components and resources. For details, refer to the official integration guide.

### JAnalytics Android SDK v1.1.2

#### Update Time

+ 2017-07-26

#### Change Log

+ Fix some bugs reported by users
+ Fix some known issues.
+ The .pdf document of integration guide is no longer provided, and use README.txt instead

#### Upgrade Prompt

+ Recommend to upgrade!

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update the library file and open the libs folder. Replace the original JAnalytics sdk jar files in the project with janalytics-android-v1.x.x.jar, and delete the original JAnalytics sdk jar files. Replace the original Jiguang jcore jar file in the project with jcoe-android-v1.x.x.jar and delete the original Jiguang jcore jar file. Use the libjcore1xx.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original Jiguang so file.
+ Update AndroidManifest.xml. There is an AndroidManifest file in the root directory of the compressed package, which is equipped with permissions required for sdk statistics. Please update JAnlytics-related component properties, permissions, etc. according to the examples. Note: All of the Jiguang Android sdk use the same key and channel. For details, see the instructions in the JAnalytics Android SDK Integration Guide, or the examples in the example.
+ If integrate JAnalytics by jcenter, you do not need to add related components and resources. For details, refer to the official integration guide.

### JAnalytics iOS SDK v1.1.3

#### Update Time

+ 2017-07-05

#### Change Log

+ Fix several bugs that affected data collection in statistics
+ Replace original pdf document with README
+ Optimize structure of sdk

#### Upgrade Prompt

+ Recommend to upgrade!
+ Note: Xcode 8.0 or lower version is not supported to enable bitcode.

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics Android SDK v1.1.1

#### Update Time

+ 2017-04-21

#### Change Log

+ Fix some bugs reported by users
+ Fix some known issues.
+ Add the switch interface for CrashLog reporting: initCrashHandler (open the reporting) and stopCrashHandler (stop the reporting)

#### Upgrade Prompt

+ Recommend to upgrade!

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update the library file and open the libs folder. Replace the original JAnalytics sdk jar files in the project with janalytics-android-v1.x.x.jar, and delete the original JAnalytics sdk jar files. Replace the original Jiguang jcore jar file in the project with jcoe-android-v1.x.x.jar and delete the original Jiguang jcore jar file. Use the libjcore1xx.so file in the corresponding CPU folder to replace the original Jiguang so file in the project and delete the original Jiguang so file.
+ Update AndroidManifest.xml. There is an AndroidManifest file in the root directory of the compressed package, which is equipped with permissions required for sdk statistics. Please update JAnlytics-related component properties, permissions, etc. according to the examples. Note: All of the Jiguang Android sdk use the same key and channel. For details, see the instructions in the JAnalytics Android SDK Integration Guide, or the examples in the example.
+ If integrate JAnalytics by jcenter, you do not need to add related components and resources. For details, refer to the official integration guide.

### JAnalytics iOS SDK v1.1.2

#### Update Time

+ 2017-04-14

#### Change Log

+ Add pdf documentation
+ Fix some log records
+ BUG Fix BUG
+ Increase statistical reporting data.

#### Upgrade Prompt

+ Recommend to upgrade!
+ Note: Xcode 8.0 or lower version is not supported to enable bitcode.

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics iOS SDK v1.1.1

#### Update Time

+ 2017-02-13

#### Change Log

+ Fix the rrash caused by failure of JCore DNS resolution.

#### Upgrade Prompt

+ Recommend to upgrade!
+ Note: Xcode 8.0 or lower version is not supported to enable bitcode.

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics Android SDK v1.1.0

#### Update Time

+ 2017-02-08

#### Change Log

+ Fix bugs reported by users
+ Fix some known issues

#### Upgrade Prompt

+ Recommend to upgrade!

####  Upgrade Guide

+ First unzip the zip archive you got
+ Import SDK Development Kit
        ◦ Replace the original JAnalytics sdk jar file with janalytics-android-v1.1.0.jar, and delete the original JAnalytics sdk jar file.
        ◦ Replace the original Jiguang jcore jar file in the project with jcoe-android-v1.1.0.jar and delete the original Jiguang jcore jar file.
        ◦ Replace the original Jiguang so file in the project with the libjcore110.so file in the corresponding CPU folder, and delete the original Jiguang so file.
+ Configure AndroidManifest.xml
        ◦ There is an AndroidManifest file in the root directory of the compressed package, which is equipped with permissions required for sdk statistics.
        ◦ Please update JAnlytics-related component properties, permissions, etc. according to the examples.
        ◦ Note: All of the Jiguang Android sdk use the same key and channel.
+ If integrate JAnalytics by jcenter, you do not need to add related components and resources. For details, refer to the official integration guide.

### JAnalytics iOS SDK v1.1.0

#### Update Time

+ 2017-01-09

#### Change Log

+ Fix the error of isProduction property in JANALYTICSLaunchConfig object
+ Fix some internal bugs
+ Optimize the running performance

#### Upgrade Prompt

+ Recommend to upgrade!
+ Note: Xcode 8.0 or lower version is not supported to enable bitcode.

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics iOS SDK v1.0.0

#### Update Time

+ 2016-12-02

#### Change Log

+ Support active users, new users and other basic statistics.
+ Support crash information statistics of the application
+ Support for purchasing, content browsing, login, registration and other template events.
+ Support custom calculation events and custom count events.
+ Support page flow statistics.

#### Upgrade Prompt

+ Recommend to upgrade!
+ Note: Xcode 8.0 or lower version is not supported to enable bitcode.

####  Upgrade Guide

+ First unzip the zip archive you got
+ Update library files

### JAnalytics Android SDK v1.0.0

#### Update Time

+ 2016-12-02

#### Change Log

+ Support active users, new users and other basic statistics.
+ Support crash information statistics of the application
+ Support for purchasing, content browsing, login, registration and other template events.
+ Support custom calculation events and custom count events.
+ Support page flow statistics.

#### Upgrade Prompt

+ Recommend to upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Import SDK Development Kit
+ Configure AndroidManifest.xml