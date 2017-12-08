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

### 添加初始化代码
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
更多接口，参考[iOS SDK API](ios_api)文档说明

[1]: ../image/Jsms-ios-1.png

