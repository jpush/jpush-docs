# Android SDK Overview

<style>
img[alt= jiguang] { width: 800px; }
</style>

## JAnalytics Android

### Modular Jiguang Developer SDK

The Jiguang Developer Service SDK adopts a modular usage model, namely a core (JCore)+N service (JPush,JAnalytics,...), which allows developers to use a single service or multiple services, which greatly optimizes the duplication of functional modules when multiple modules are used simultaneously. As shown below:
![jiguang](./image/sdk_model.png)


## Reporting Strategy

The JAnalytics Android SDK adopts a strategy of separating data records from data reporting. The data is recorded in real time and reported in accordance with the reporting strategy.

+ Open application reporting
+ Close application reporting

Remarks: In the event of an extreme situation leading to unsuccessful data reporting, the data will not be cleared, but wait to be triggered by the next reporting strategy and then report.

##  Package Description

The JPush Android SDK archive for downloading contains the following sections

+ AndroidManifest.xml
	+ Configuration file of client embedded SDK 
+ libs/jcore-android_1.x.x.jar
	+ Sdk core package
+ libs/xxx/xx.so
	+ so file needed by sdk
+ libs/janalytics-android-sdk_1.x.x.jar
	+ SDK analysis development package
+ example
	+ It is a complete Android project that demonstrates the basic usage of the JAnalysis SDK and can be used as a reference.

## Integration Approach

At present, the SDK only supports Android 2.3 or later mobile phone systems. Reference: [Integration Guide of JAnalytics Android SDK.](android_guide)

## Interface Description
Reference: [JAnalytics Android API](android_api)

## Technical Support

When a problem occurs:

+ Please read the documentation carefully to see if there are any omissions.
+ Send an email to us: support@jpush.cn

In order to solve the problem more quickly, please provide the following information when seeking help:

+ Provide appkey
+ If it is a SDK issue, please provide the corresponding SDK version and complete logging

