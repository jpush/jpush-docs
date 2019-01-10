# [iOS SDK Overview]
<style>
img[alt= jiguang] { width: 800px; }
</style>

## JAnalytics iOS

###  Modular Jiguang Developer SDK

The Jiguang Developer Service SDK adopts a modular usage model, namely a core (JCore)+N service (JPush,JAnalytics,...), which allows developers to use a single service or multiple services, which greatly optimizes the duplication of functional modules when multiple modules are used simultaneously. As shown below:

![jiguang](./image/sdk_model.png)


## Reporting Strategy

The JAnalytics iOS SDK adopts a strategy of separating data records from data reporting. The data is recorded in real time and reported in accordance with the reporting strategy.

-   Open application reporting

-   Close application reporting

Remarks: In the event of an extreme situation leading to unsuccessful data reporting, the data will not be cleared, but wait to be triggered by the next reporting strategy and then report.

## Package Description

-   janalytics-ios-x.x.x.a static library

-   jcore-ios-x.x.x.a static library

-   header file of statistics portal JANALYTICSService.h

-   header file of statistics event object file JANALYTICSEventObject.h

-   a complete iOS Demo project that demonstrates the basic usage of the JAnalytics SDK and can be used as a reference.


## Integration Approach

The current SDK only supports iOS 7 or later mobile phone systems. Reference: [Integration Guide of JAnalytics iOS SDK](ios_guide)

## Interface Description

Reference: [JAnalytics iOS API](ios_api)

## Technical Support

When a problem occurs:

-   Please read the documentation carefully to see if there are any omissions.

-   Send an email to our support: [support&#64;jpush.cn](mailto:support&#64;jpush.cn)

In order to solve the problem more quickly, please provide the following information when seeking help:

-   Provide appkey

-   If it is a SDK issue, please provide the corresponding SDK version and complete logging
