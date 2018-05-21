
# Description of JSMS iOS SDK API

### Obtain SMS Verification Code

```
+ (void)getVerificationCodeWithPhoneNumber:(NSString * _Nonnull)number 
                             andTemplateID:(NSString * _Nonnull)templateID
                         completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```

**Interface Description**

Get interface of SMS verification code: Create a button to get the SMS verification code, or call the SMS verification code in the button event of the existing interface.

**Parameter Description**

-   number: Mobile number

-   templateID: SMS template ID

-   handler: The callback of request or request failure

**Call Example**

```

//点击获取短信验证码
 - (IBAction)sendSmsAuthCode:(id)sender {
  
     [JSMSSDK getVerificationCodeWithPhoneNumber:@"152xxxxxxxx" andTemplateID:@"1" completionHandler:^(id resultObject, NSError *error) {
     	if (!error) {
         	NSLog(@"Get verification code success!");
     	}else{
         	NSLog(@"Get verification code failure!");
         	NSLog(@"%@",error);
     	}
     }];
 }
```

### Get Voice Verification Code

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>Interface to get voice verification code is added in Version 1.2.0.
</div>

```
+ (void)getVoiceVerificationCodeWithPhoneNumber:(NSString * _Nonnull)number
                              completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```
**Interface Description**

Interface for obtaining voice verification code: Create button to get voice verification code, or call the method to get voice verification code in button event of existing interface

**Parameter Description**

-   number: Mobile number

-   handler: The callback of request or request failure

**Call Example**


```

//点击获取语音验证码
 - (IBAction)sendVoiceAuthCode:(id)sender {
  
     [JSMSSDK getVoiceVerificationCodeWithPhoneNumber:@"152xxxxxxxx" completionHandler:^(id resultObject, NSError *error) {
     	if (!error) {
         	NSLog(@"Get voice verification code success!");
     	}else{
         	NSLog(@"Get voice verification code failure!");
         	NSLog(@"%@",error);
     	}
     }];
 }
```

### Get Voice Verification Code (broadcast language can be set)

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>Interface to get voice verification code is added in Version 1.4.0, which can set type of broadcast language.
</div>

```
+ (void)getVoiceVerificationCodeWithPhoneNumber:(NSString * _Nonnull)number
                                languageOptions:(JSMSLanguageOptions)options
                              completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```

**Interface Description**

Interface for obtaining voice verification code: Create button to get voice verification code, or call the method to get voice verification code in button event of existing interface

**Parameter Description**

-   number: Mobile number

-   options: Broadcast language. When the parameter is invalid, default language is Chinese

-   handler: The callback of request or request failure

**Call Example**

```

//点击获取语音验证码
 - (IBAction)sendVoiceAuthCode:(id)sender {
  
     [JSMSSDK getVoiceVerificationCodeWithPhoneNumber:@"152xxxxxxxx"
                                         languageOptions:JSMSLanguage_zh_Hans
                                       completionHandler:^(id resultObject, NSError *error) {
     	if (!error) {
         	NSLog(@"Get voice verification code success!");
     	}else{
         	NSLog(@"Get voice verification code failure!");
         	NSLog(@"%@",error);
     	}
     }];
 }
```

### Verify Verification Code

```
+ (void)commitWithPhoneNumber:(NSString * _Nonnull)number
             verificationCode:(NSString * _Nonnull)vCode
            completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```

**Interface Description**

Verify verification code: Create a button to submit a verification code, or call a verification code in a button event of an existing interface.

**Parameter Description**

-   number: Mobile number

-   vCode: SMS verification code

-   handler: The callback of request or request failure

**Call Example**

```
//验证验证码 
 [JSMSSDK commitWithPhoneNumber:@"152xxxxxxxx" verificationCode:@"123456" completionHandler:^(id resultObject, NSError *error) {
      if (!error) {
           NSLog(@"Commit verification vode success!");
      }else{
           NSLog(@"%@",error);
           NSLog(@"Commit verification code failure!");
      }
 }];
```

**Set the Interval of Verification Code Request**

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>Set the interface for obtaining the interval of verification code request is added in Version 1.2.0.
</div>

```
+ (void)setMinimumTimeInterval:(NSTimeInterval)seconds;
```

**Interface Description**

Set the interface for obtaining the interval of verification code request: You can only send the request to obtain the verification code within the set interval once. If you do not call this interface, default interval of sdk is 30s

**Parameter Description**

-   seconds: Interval

**Call Example**

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  
      [JSMSSDK setMinimumTimeInterval:60];
      return YES;
 }
```

## Description of Error Code

| **Error Code** | **Description of Error Code**                              | **Remarks**                                                                                                                                                                                                                                                                  |
|----------------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2993           | Uuid error. Verification of verification code failed       |                                                                                                                                                                                                                                                                              |
| 2994           | Parameter error                                            |                                                                                                                                                                                                                                                                              |
| 2996           | Two requests within the minimum time interval              |                                                                                                                                                                                                                                                                              |
| 2997           | The number changed. Please get the verification code first |                                                                                                                                                                                                                                                                              |
| 2998           | Network Error                                              |                                                                                                                                                                                                                                                                              |
| 2999           | Other errors                                               |                                                                                                                                                                                                                                                                              |
| 3001           | Request timed out                                          |                                                                                                                                                                                                                                                                              |
| 4204           | Invalid mobile number                                      |                                                                                                                                                                                                                                                                              |
| 4001           | Body is empty                                              |                                                                                                                                                                                                                                                                              |
| 4002           | Invalid AppKey                                             |                                                                                                                                                                                                                                                                              |
| 4003           | Invalid source                                             |                                                                                                                                                                                                                                                                              |
| 4004           | Decryption of body failed                                  |                                                                                                                                                                                                                                                                              |
| 4005           | Decryption of aes key failed                               |                                                                                                                                                                                                                                                                              |
| 4006           | Timestamp conversion failed                                |                                                                                                                                                                                                                                                                              |
| 4007           | Format of body is incorrect                                |                                                                                                                                                                                                                                                                              |
| 4008           | Invalid timestamp                                          |                                                                                                                                                                                                                                                                              |
| 4009           | No SMS verification permission                             |                                                                                                                                                                                                                                                                              |
| 4011           | Send overclocking                                          | There is no limit for the same mobile phone number getting verification code every day. The notification verification code with same content is 3 pieces in 10 minutes, and there are no restrictions on different contents. The marketing category is also 3 in 10 minutes. |
| 4012           | Api does not exist                                         |                                                                                                                                                                                                                                                                              |
| 4013           | Template does not exist                                    |                                                                                                                                                                                                                                                                              |
| 4014           | Extra is empty                                             |                                                                                                                                                                                                                                                                              |
| 4015           | Incorrect verification code                                |                                                                                                                                                                                                                                                                              |
| 4016           | No margin                                                  |                                                                                                                                                                                                                                                                              |
| 4017           | Verification code timeout                                  |                                                                                                                                                                                                                                                                              |
| 4018           | Verification code has been verified                        |                                                                                                                                                                                                                                                                              |
| 5000           | Server error                                               |                                                                                                                                                                                                                                                                              |
