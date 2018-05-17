## Description of SDK API

+ SMSSDK class: External class. This class is a singleton. The methods that call this class need to obtain the unique instance of the class. The method is SMSSDK.getInstance().
+ SmscodeListener: Get the callback interface for verification code. You need to pass in the interface instance when calling the SMSSDK's getSmsCode.
+ SmscheckListener: Check the callback interface of the verification code. An instance of the interface needs to be passed in when calling the SMSSDK's checkSmsCode.

### SMSSDK.initSdk(Context context)

#### Interface Description

This interface is an initialization interface. It is mainly to detect some configuration information. If the configuration is incorrect, the initialization will fail and an error log will be printed. The interface must be called before calling other interfaces. It is called only once and it is recommended to call it in the Application or initial activity.

#### Call Example
```
SMSSDK.getInstance().initSdk(this);
```

###SMSSDK.getSmsCode(String phone, String tempId, SmscodeListener listener)

#### Interface Description

Get the verification code.

>The interface is a callback in a non-UI thread that needs to call back in the UI thread SMSSDK.getSmsCodeAsyn().

#### Parameter Description

+ phone：Phone number
+ tempId：SMS template
+ listener：Callback interface

#### Call Example
```
SMSSDK.getInstance().getSmsCodeAsyn("159xxxxxxxx", "1", new SmscodeListener() {
    @Override
    public void getCodeSuccess(final String uuid) {
        // 获取验证码成功，uuid 为此次获取的唯一标识码。
    }

    @Override
    public void getCodeFail(int errCode, final String errMsg) {
        // 获取验证码失败 errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
    }
});
```

### SMSSDK.checkSmsCode(String phone, String code, SmscheckListener listener)

#### Interface Description

Verification interface of verification code
>The interface is a callback in a non-UI thread that needs to call back in the UI thread SMSSDK.checkSmsCodeAsyn().

#### Parameter Description

+ phone：Phone number
+ code：SMS verification code
+ listener：Callback interface

#### Call Example
```
SMSSDK.getInstance().checkSmsCodeAsyn("159xxxxxxxx", "123456", new SmscheckListener() {
    @Override
    public void checkCodeSuccess(final String code) {
        // 验证码验证成功，code 为验证码信息。
    }

    @Override
    public void checkCodeFail(int errCode, final String errMsg) {
        // 验证码验证失败, errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
    }
});
```

### SMSSDK.getVoiceCode(String phone, SmscodeListener listener)

#### Interface Description

Get voice verification code. The speech language is Chinese.

>The interface is a callback in a non-UI thread that needs to call back in the UI thread SMSSDK.getVoiceCodeAsyn().


#### Parameter Description

+ phone：Phone number
+ listener：Callback interface

#### Call Example
```
SMSSDK.getInstance().getVoiceCodeAsyn("159xxxxxxxx", new SmscodeListener() {
    @Override
    public void getCodeSuccess(final String uuid) {
        //获取验证码成功，uuid 为此次获取的唯一标识码。
    }
    @Override
    public void getCodeFail(int errCode, final String errMsg) {
        //获取验证码失败，errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
    }
});
```

### SMSSDK.getVoiceCode(String phone,int language,SmscodeListener listener)

#### Interface Description

Get voice verification code. This interface can specify the language.

>The interface is a callback in a non-UI thread that needs to call back in the UI thread SMSSDK.getVoiceCodeAsyn()

#### Parameter Description

+ phone：Phone number
+ language：0 for Chinese, 1 for English, and 2 for Chinese and English. If unsupported languages passed in, it will report 50040.
+ listener：Callback interface
#### Call Example
```
SMSSDK.getInstance().getVoiceCodeAsyn("159xxxxxxxx",2,new SmscodeListener() {
    @Override
    public void getCodeSuccess(final String uuid) {
        //获取验证码成功，uuid 为此次获取的唯一标识码。
    }
    @Override
    public void getCodeFail(int errCode, final String errMsg) {
        //获取验证码失败，errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
    }
});
```

### SMSSDK.setIntervalTime(long intervalTime)

#### Interface Description

Set the interval for getting the verification code twice. Default to 30 seconds.

#### Parameter Description

+ intervalTime：Interval, in milliseconds (ms).

#### Call Example
```
SMSSDK.getInstance().setIntervalTime(60000);    // 设置间隔时间为 60 秒
```

### SMSSDK.getIntervalTime()

#### Interface Description

Get the interval of current settings.

#### Return Value

+ long：The unit is milliseconds (ms). 

#### Call Example
```
SMSSDK.getInstance().getIntervalTime();
```

### SMSSDK.setDebugMode(boolean debugMode)

#### Interface Description

Set the debug mode. Setting true will output the logs printed by the SDK.

#### Parameter Description

+ debugMode：true is debug mode, false is non-debug mode.

#### Call Example
```
SMSSDK.getInstance().setDebugMode(true);
```

## Description of Error Code 

| Error code | Description of Error code | Remarks |
|--------|---------------------|--------------------------|
| 3001 | Request timed out |  |
| 3002 | Invalid phone number |  |
| 4001 | Body is empty |  |
| 4002 | Invalid AppKey |  |
| 4003 | Invalid source |  |
| 4004 | Decryption of body failed|  |
| 4005 | Decryption of aes key failed |  |
| 4006 | Timestamp conversion failed |  |
| 4007 | Format of body is incorrect |  |
| 4008 | Invalid timestamp |  |
| 4009 | No SMS verification permission |  |
| 4011 | Send overclocking | There is no limit for the same mobile phone number getting verification code every day. The notification verification code with same content is 3 pieces in 10 minutes, and there are no restrictions on different contents. The marketing category is also 3 in 10 minutes.|
| 4013 | Template does not exist |  |
| 4014 | Extra is empty |  |
| 4015 | Incorrect verification code |  |
| 4016 | No margin |  |
| 4017 | Verification code timeout |  |
| 4018 | Double verification |  |
| 2993 | Verification of verification code failed | SMS delivered but get uuid exception |
| 2994 | Local data is wrong |  |
| 2995 | Data parsing error |  |
| 2996 | Interval for two requests is no more than 1 minute | Local verification |
| 2997 | Failed to get verification code |  |
| 2998 | Network Error | No network, etc |
| 2999 | Other errors |  |
| 50040 | Pass in unsupported language | 0 for Chinese, 1 for English, 2 for English and Chinese |



