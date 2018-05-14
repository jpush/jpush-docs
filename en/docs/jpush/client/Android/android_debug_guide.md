# Android SDK Debugging Guide

## SDK Startup Process
+ Check whether the AppKey is configured in AndroidManifest.xml. If not, the startup fails
+ Check the correctness of the Androidmanifest.xml file configuration. You must ensure that all the annotations in the "Android SDK Integration Guide" are marked "
+ The "Required" section is correctly configured. Otherwise, the startup fails.
+ Check the validity of the JPush SDK library file. If the library file is invalid, the startup fails.
+ Check whether the network is available. If the network is available, connect to the server to log in. Otherwise, the startup fails.
+ After the login is successful, you can see the following log from the log

![](../image/jpush.jpg)

## Test confirmation
+ Make sure that all required “Required” items in Androidmanifest.xml have been added. If there is a "Required" item not added, the log will indicate an error.
+ Make sure that the AppKey (generated on the Portal) has been correctly written in Androidmanifest.xml. If you do not write it, there will be a log error.
+ Make sure to call the init(context) interface when the program starts
+ Make sure that the network of test cell phone (or emulator) is available. If the network is available, the client should have a login succeed message soon after the init called, as shown in the SDK startup process
+ Start the application, log in to the Portal system, and send a custom message or notification bar to the application. Within a few seconds, the client should be able to receive the delivery announcement or defined message.

## Exception Handling of Aliases and Tags Settings

Due to the unstable network connection, there is a certain probability that the JPush SDK will fail to set aliases and tags. 

If App developers properly handle the setup failures, the impact of occasional failures to normal use of the application is limited.


The followings use the Android SDK as an example.

The basic idea：

+ When the setting is successful, write the status to the SharePreference and do not need to set later
+ If encounters a 6002 timeout, please retry a little later.

    
        // 这是来自 JPush Example 的设置别名的 Activity 里的代码。一般 App 的设置的调用入口，在任何方便的地方调用都可以。
        private void setAlias() {
            EditText aliasEdit = (EditText) findViewById(R.id.et_alias);
            String alias = aliasEdit.getText().toString().trim();
            if (TextUtils.isEmpty(alias)) {
                Toast.makeText(PushSetActivity.this,R.string.error_alias_empty, Toast.LENGTH_SHORT).show();
                return;
            }
            if (!ExampleUtil.isValidTagAndAlias(alias)) {
                Toast.makeText(PushSetActivity.this,R.string.error_tag_gs_empty, Toast.LENGTH_SHORT).show();
                return;
            }
        
            // 调用 Handler 来异步设置别名
            mHandler.sendMessage(mHandler.obtainMessage(MSG_SET_ALIAS, alias));
        }
        
        private final TagAliasCallback mAliasCallback = new TagAliasCallback() {
            @Override
            public void gotResult(int code, String alias, Set<String> tags) {
                String logs ;
                switch (code) {
                case 0:
                    logs = "Set tag and alias success";
                    Log.i(TAG, logs);
                    // 建议这里往 SharePreference 里写一个成功设置的状态。成功设置一次后，以后不必再次设置了。
                    break;
                case 6002:
                    logs = "Failed to set alias and tags due to timeout. Try again after 60s.";
                    Log.i(TAG, logs);
                    // 延迟 60 秒来调用 Handler 设置别名
                    mHandler.sendMessageDelayed(mHandler.obtainMessage(MSG_SET_ALIAS, alias), 1000 * 60);
                    break;
                default:
                    logs = "Failed with errorCode = " + code;
                    Log.e(TAG, logs);
                }
                ExampleUtil.showToast(logs, getApplicationContext());
            }
        };
        private static final int MSG_SET_ALIAS = 1001;
        private final Handler mHandler = new Handler() {
        @Override
            public void handleMessage(android.os.Message msg) {
                super.handleMessage(msg);
                switch (msg.what) {
                    case MSG_SET_ALIAS:
                        Log.d(TAG, "Set alias in handler.");
                        // 调用 JPush 接口来设置别名。
                        JPushInterface.setAliasAndTags(getApplicationContext(),
                                                        (String) msg.obj,
                                                         null,
                                                         mAliasCallback);
                    break;
                default:
                    Log.i(TAG, "Unhandled msg - " + msg.what);
                }
            }                                       
        };
        

## Network Problem Analysis of Android SDK

Unstable Android client network will sometimes cause a delay for the App to receive push messages. 

Many developers think this is due to JPush’s instability and delay, and sometimes they even think that the backend push system of JPush has a problem. 

The purpose of this article is to analyze the problem of JPush caused by the Android network from all aspects.

## Necessary Conditions for Normal Work of JPush

At first, we need to know that the JPush SDK will not always work after it is integrated into the App.

The necessary condition for its normal operation is that the JPush SDK maintains a connection with the network of JPush Server. Please refer to this article for further understanding: JPush Technology Principle: [Long Connection of Mobile Wireless Network.](http://blog.jiguang.cn/jpush_wireless_push_principle/)

The complexity and instability of the Android device's network is one of the most complicated aspects of Android device development.

In addition, the network capabilities of each mobile phone are also very different. Many domestic brands of mobile phones may even have serious problems in the network. However, big brand manufacturers have much better mobile phones.

As long as JPush's network connection is normal, then:

+ The news received by JPush must be timely. The delay is in seconds, typically within 1 second. If it exceeds 10 seconds, there must be a problem with the client network.
+ When the phone goes to sleep, it can also receive push messages in a timely manner.

## Special Handling of Particular System Causes Problems

### MIUI V5 System

+ Self-initiated Management: By default, after the phone is turned on, only the system default service can be started. Unless in the self-initiated management interface, settings allow third-party programs to start automatically.
+ Network Assistant: You can manually disable installed third-party programs from accessing 2G/3G and WIFI networks and set whether new installation programs will allow access to 2G/3G and WIFI networks.

### Over 4.0 Android System

+ After Setting ->Application, the program can't restart automatically after forcibly stopping the application. Even if it is restarted, it must be manually opened.

### Let us sort out the debugging ideas from the current feedback

**Cannot receive the JPush message when the phone is sleeping. Messages can be successfully received after unlocking or the light of the screen.**

This phenomenon indicates that the JPush SDK was "forced" to lose connection with the server's network when the phone was dormant.

The working principle of the JPush SDK is to ensure that the mobile phone can work normally even when the mobile phone is dormant, that is, it can receive Push messages in time when it is dormant. In fact, JPush can achieve this effect on most mobile phones.

This "forced" is caused by the environment of Android device. The reasons involved are as follows:

+ The network settings of the phone itself. The standard version of Android ROM does not have this setting, but some special ROMs may have this setting.
+ Additional things to do with security and power saving software on mobile phones

The above special mechanism will shut down the network. Once the network is connected, JPush will also connect to the server so that Push messages will be received.

**Sometimes receiving a JPush message is very timely, while sometimes it will need to wait a few minutes**

JPush will monitor network switching broadcasts. When the network is closed, the original JPush connection is closed. Create a JPush connection when there is a new network.

In addition, the RTC sends heartbeats periodically. If the previous network has been broken, it will be reconnected.

It should be said that the current network connection strategy is still relatively simple. The purpose of doing so is to save electricity and traffic.

The bad news is: When the network is not switched, the JPush connection will be interrupted because the network is too bad at the time. In this case, you can only wait for the RTC heartbeat to trigger the connection. This is also the reason why JPush cannot receive Push messages in time. According to the different network conditions, the probability of this situation will be different. However, according to our own test, 90% of the time can receive Push messages in a timely manner.

JPush currently does not have a positive online chat strategy like Wechat. If this is done, the power and flow consumption will inevitably increase exponentially.

**Failed to receive JPush messages completely**

If you don't receive a Push message completely after the integration, it is most likely a configuration error somewhere. Please double check according to the documentation: 
[Android SDK Integration Guide](https://docs.jiguang.cn/jpush/client/Android/android_guide/),
[iOS SDK Integration Guide](https://docs.jiguang.cn/jpush/client/iOS/ios_guide_new/),
or Reference Tutorial: 
[Android SDK Debugging Guide](https://docs.jiguang.cn/jpush/client/iOS/ios_guide_new/),
[iOS SDK Debugging Guide](https://docs.jiguang.cn/jpush/client/iOS/ios_guide_new/).
