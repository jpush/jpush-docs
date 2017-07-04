# JSMS iOS SDK集成指南
##SDK 说明

+ 目前SDK支持iOS7.0及以上版本.

### SDK 压缩包内包括

+ lib文件夹：包含头文件 JSMSSDK.h、JSMSConstant.h，静态库文件libsms-lib.a ，支持的iOS版本为 7.0 及以上版本。
+ pdf文件：集成指南
+ demo文件夹：示例

## 集成步骤

### 创建应用

注册成为JPush开发者。在极光的web portal 上创建应用得到APPkey，如果您已经是是极光其他产品的用户并且创建过应用，那么无需重复创建。

### 导入开发包

将SDK包解压，将解压后的JsmsSDK文件夹（包含头文件 include，静态库文件libsms-lib.a 。头文件目录包含JSMSSDK.h、JSMSConstant.h两个对外接口文件）添加到工程目录中。 

### Build Settings

+ 在项目配置，Build Settings，Other Linker Flags 里增加  -ObjC ;
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>1.2.0版本之后，sdk完全支持https传输，不需要再进行AppTransportSecurity相关设置。
</div>

### Capabilities
由于SDK内部加密协议涉及KeyChain，如使用Xcode8及以上环境开发，在模拟器运行调试时请开启Application Target的Capabilities->KeyChain Sharing选项，如图：  
![jsms_ios][1]

### 添加代码
```
 + (void)registerWithAppKey:(NSString * _Nonnull)appkey; 
```
**接口说明**

注册SDK接口：在官网创建应用,创建成功后自动生成 AppKey 用以标识该应用

**调用示例：**

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      // Override point for customization after application launch.
  
      //从官网注册获取
      //注册短信验证的appKey
      [JSMSSDK registerWithAppKey:kAppKey];

      return YES;
 }
```

```
+ (void)getVerificationCodeWithPhoneNumber:(NSString * _Nonnull)number 
                             andTemplateID:(NSString * _Nonnull)templateID
                         completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```



**接口说明**

获取短信验证码接口：创建获取短信验证码的按钮，或者是在自己已有的界面的按钮事件里调用获取短信验证码的方法

**参数说明：**

+ number :手机号码
+ templateID:短信模板ID
+ handler:请求成功或者失败的回调

**调用示例：**

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
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>1.2.0版本新增--获取语音验证码接口。
</div>

```
+ (void)getVoiceVerificationCodeWithPhoneNumber:(NSString * _Nonnull)number
                              completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```

**接口说明**

获取语音验证码接口：创建获取语音验证码的按钮，或者是在自己已有的界面的按钮事件里调用获取语音验证码的方法

**参数说明：**

+ number :手机号码
+ handler:请求成功或者失败的回调

**调用示例：**

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

```
+ (void)commitWithPhoneNumber:(NSString * _Nonnull)number
             verificationCode:(NSString * _Nonnull)vCode
            completionHandler:(JSMSCompletionHandler _Nonnull)handler;
```

**接口说明**

验证验证码：创建提交验证码的按钮，或者是在自己已有的界面的按钮事件里调用提交验证码的方法

**参数说明：**

+ number:手机号码
+ vCode:短信验证码
+ handler:请求成功或者失败的回调

**调用示例：**

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

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">	<p>1.2.0版本新增--设置获取验证码请求时间间隔的接口。
</div>

```
+ (void)setMinimumTimeInterval:(NSTimeInterval)seconds;
```
**接口说明**

设置获取验证码请求时间间隔的接口：在设置时间间隔内只能发送一次获取验证码的请求。如果不调用此接口，sdk默认间隔是30s

**参数说明：**

+ seconds:时间间隔

**调用示例：**

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  
      [JSMSSDK setMinimumTimeInterval:60];
      return YES;
 }
```
## 错误码描述

| 错误码 | 错误码描述               | 备注 |
|--------|--------------------------|------|
| 2993   | uuid错误，验证码验证失败 |      |
| 2994   | 参数错误               |      |
| 2996   | 两次请求在最小时间间隔内  |      |
| 2997   | 号码改变，请首先获取验证码 |      |
| 2998   | 网络错误                 |      |
| 2999   | 其他错误                 |      |
| 3001   | 请求超时                 |      |
| 4204   | 无效的手机号码           |      |
| 4001   | body为空                 |      |
| 4002   | 无效的appkey             |      |
| 4003   | 无效的来源               |      |
| 4004   | body解密失败             |      |
| 4005   | aes key解密失败          |      |
| 4006   | 时间戳转化失败           |      |
| 4007   | body格式不正确           |      |
| 4008   | 无效时间戳               |      |
| 4009   | 没有短信验证权限         |      |
| 4011   | 发送超频                 | 同一手机号每天获取验证码无限制，通知类相同内容10分钟3条，不同内容无限制，营销类10分钟3条。|
| 4012   | api不存在                |      |
| 4013   | 模板不存在               |      |
| 4014   | extra为空                |      |
| 4015   | 验证码不正确             |      |
| 4016   | 没有余额                 |      |
| 4017   | 验证码超时               |      |
| 4018   | 验证码已经验证过              |      |
| 5000   | 服务端错误               |      |


[1]: ./image/Jsms-ios-1.png