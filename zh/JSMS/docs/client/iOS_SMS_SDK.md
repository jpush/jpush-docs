# JSMS iOS SDK集成指南
##SDK 说明

+ 目前SDK支持iOS7.0及以上版本.

### SDK 压缩包内包括

+ lib文件夹：包含头文件 JSMSSDK.h、JSMSContant.h，静态库文件libsms-lib.a ，支持的iOS版本为 7.0 及以上版本。
+ pdf文件：集成指南
+ demo文件夹：示例

## 集成步骤

### 创建应用

注册成为JPush开发者。在极光的web portal 上创建应用得到APPkey，如果您已经是是极光其他产品的用户并且创建过应用，那么无需重复创建。

### 导入开发包

将SDK包解压，将解压后的JsmsSDK文件夹（包含头文件 include，静态库文件libsms-lib.a 。头文件目录包含JSMSSDK.h、JSMSContant.h两个对外接口文件）添加到工程目录中。 

### Build Settings

+ 在项目配置，Build Settings，Other Linker Flags 里增加  -ObjC ;
+ 如果使用的是Xcode7编译时，需要在App项目的plist手动加入以下Source Code 以支持iOS 9 的 http传输:

`
<key>NSAppTransportSecurity</key>
    <dict>
   <key>NSAllowsArbitraryLoads</key>
   <true/> 
 </dict>
`

### 添加代码

#### + (void)registerWithAppKey:(NSString * __nullable)appkey; 

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
+ (void)getVerificationCodeWithPhoneNumber:(NSString * __nullable)number 
                          andTemplateID:(NSString * __nullable)templateID
                          completionHandler:(JSMSCompletionHandler __nullable)handler;
```



**接口说明**

获取验证码接口：创建获取验证码的按钮，或者是在自己已有的界面的按钮事件里调用获取验证码的方法

**参数说明：**

+ number :手机号码
+ tempID：短信模板ID，目前服务器只提供+ tempID：@“1”
+ handler：请求成功或者失败的回调

**调用示例：**

```

//点击获取验证码
 - (IBAction)sendAuthCode:(id)sender {
  
     [self.view endEditing: YES];
     [JSMSSDK getVerificationCodeWithPhoneNumber:@"15220000000" andTemplateID:@"1" completionHandler:^(id resultObject, NSError *error) {
     if (!error) {
         NSLog(@"Get Verification Code success!");
     }else{
         NSLog(@"Get Verification Code failure!");
     }];
 }
```

```
+ (void)commitWithPhoneNumber:(NSString * __nullable)number
                     verificationCode:(NSString * __nullable)vCode
                  completionHandler:(JSMSCompletionHandler __nullable)handler;
```

**接口说明**

验证验证码：创建提交验证码的按钮，或者是在自己已有的界面的按钮事件里调用提交验证码的方法

**参数说明：**

+ number  手机号码
+ vCode:短信验证码
+ handler:请求成功或者失败的回调

**调用示例：**

```
//验证验证码 
 [JSMSSDK commitWithPhoneNumber:@"15220000000" verificationCode:@"123456" completionHandler:^(id resultObject, NSError *error) {
      if (!error) {
           NSLog(@"Commit Verification Code success!");
      }else{
           NSLog(@"%@",error);
           NSLog(@"Commit Verification Code failure!");
      }
 }];
```

## 错误码描述

| 错误码 | 错误码描述               | 备注 |
|--------|--------------------------|------|
| 2993   | uuid错误，验证码验证失败 |      |
| 2996   | 两次请求在一分钟内       |      |
| 2997   | 请首先获取验证码         |      |
| 2998   | 网络错误                 |      |
| 2999   | 其他错误                 |      |
| 3001   | 请求超时                 |      |
| 3002   | 无效的手机号码           |      |
| 4001   | body为空                 |      |
| 4002   | 无效的appkey             |      |
| 4003   | 无效的来源               |      |
| 4004   | body解密失败             |      |
| 4005   | aes key解密失败          |      |
| 4006   | 时间戳转化失败           |      |
| 4007   | body格式不正确           |      |
| 4008   | 无效时间戳               |      |
| 4009   | 没有短信验证权限         |      |
| 4011   | 发送超频                 | 单个设备或同一手机号每天获取验证码默认10次|
| 4012   | api不存在                |      |
| 4013   | 模板不存在               |      |
| 4014   | extra为空                |      |
| 4015   | 验证码不正确             |      |
| 4016   | 没有余额                 |      |
| 4017   | 验证码超时               |      |
| 5000   | 服务端错误               |      |

