# Integration Guide of JSMS Android SDK 

## SDK Instructions

### Support Versions

+ The current SDK only supports mobile phone systems in Android 2.3 and above.

### SDK Package Contains

+ AndroidManifest.xml: configuration file of client-embedded SDK;
+ libs/jpush-sdk-sms-v1.x.x.jar: SDK Java Development Kit;
+ example: A complete Android project that demonstrates the basic usage of the SMS SDK can be used as a reference.


## Integration Steps

### Create an Application

Register as an Jiguang developer and create an App on the Jiguang Web Portal. If you are already a user of Jiguang 's other products and have created applications, you do not need to create them again.

### Import SDK Development Kit

Unzip the package and copy libs/jpush-sdk-sms-v1.x.x.jar to the project's libs directory.

### Integrate the Confusion of JPush Android SDK
```
-keep class cn.jpush.sms.SMSSDK {*;}
-keep class cn.jpush.sms.listener.** {*;}
```

### Configure AndroidManifest.xml

+ Configure permissions:

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

+ Configure AppKey：
```
<meta-data android:name="JPUSH_APPKEY" android:value="Your AppKey"/>
```

### Add Code
Refer to the Demo and SDK API instructions for adding integration.
