#iOS SDK API

##SDK接口说明

1. JVERIFICATIONService，包含SDK所有接口
2. JVAuthConfig类，应用配置信息类
3. VAuthEntity类，认证实体类
4. JVUIConfig类，登录界面UI配置基类
5. JVMobileUIConfig类，JVUIConfig的子类，移动登录界面UI配置类
6. JVUnicomUIConfig类，JVUIConfig的子类，联通登录界面UI配置类
7. JVTelecomUIConfig类，JVUIConfig的子类，电信登录界面UI配置类

##SDK初始化

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+  setupWithConfig:(JVAuthConfig * )config;***

    + 接口说明:
        + 初始化接口
    + 参数说明
        + config 配置类
    + 调用示例:

~~~
    // 如需使用 IDFA 功能请添加此代码并在初始化配置类中设置 advertisingId
    NSString *idfaStr = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
    
    JVAuthConfig *config = [[JVAuthConfig alloc] init];
    config.appKey = @"a0e6ace8d5b3e0247e3f58db";
    config.advertisingId = idfaStr;
    [JVERIFICATIONService setupWithConfig:config];
~~~

##SDK设置debug模式

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+  (void)setDebug:(BOOL)enable;***
    + 接口说明:
        + 开启debug模式
    +  参数说明
        + enable 是否开启debug模式

##SDK判断网络环境是否支持

###支持的版本
开始支持的版本 1.1.2

###接口定义

+ ***+ (BOOL)checkVerifyEnable;***
    + 接口说明:
        + 判断当前网络环境是否可以发起认证
    +  返回值说明
        + YES 可以认证
        + NO 不可以认证
        
    + 调用示例:

~~~
    if(![JVERIFICATIONService checkVerifyEnable]) {
        NSLog(@"当前网络环境不支持认证！");
        return;
    }
    //继续获取token操作
    ...
~~~

##SDK获取号码认证token

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+ (void)getToken:(void (^)(NSDictionary * result))completion;***

    + 接口说明:
        + 获取号码认证token
    + 参数说明
        + completion  参数是字典 返回token 、错误码等相关信息，token有效期1分钟, 一次认证后失效
        + result 字典 获取到token时key有code、token两个字段，获取不到token时key为code和content字段

    + 调用示例:
~~~
    [JVERIFICATIONService getToken:^(NSDictionary *result) {
        NSLog(@"getToken result:%@", result)
        //TODO:获取token后相关操作
    }];
~~~

***说明***：开发者可以通过SDK获取token接口的回调信息来选择验证方式，若成功获取到token则可以继续使用极光认证进行号码验证；若获取token失败，需要换用短信验证码等方式继续完成验证。

##SDK发起号码认证

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+ (void)verifyNumber:(JVAuthEntity * )entity result:(void (^)(NSDictionary * result))completion;***

    + 接口说明:
        + 发起号码认证，验证手机号码和本机SIM卡号码是否一致
    + 参数说明:
        + completion 认证结果
        + result 字典 key为code和content两个字段
        + entity 认证实体类

    + 调用示例:

~~~
    JVAuthEntity *entity = [[JVAuthEntity alloc] init];
    entity.number = @"phone number";
    entity.token = @"your token";
    [JVERIFICATIONService verifyNumber:entity result:^(NSDictionary *result) {
        NSLog(@"verify result:%@", result);
    }];
~~~

***说明***：开发者调用该接口，需要在管理控制台找到该应用，并在［认证设置］-［其他设置］中开启［SDK发起认证］。

##SDK请求授权一键登录

###支持的版本
开始支持的版本 2.0.0

###接口定义

+ ***+ (void)getAuthorizationWithController:(UIViewController *)vc completion:(void (^)(NSDictionary *result))completion***

    + 接口说明:
        + 授权一键登录
    + 参数说明:
        + completion 登录结果
        + result 字典 获取到token时key有operator、code、loginToken字段，获取不到token是key为code和content字段
        + vc 当前控制器

    + 调用示例:

~~~
    [JVERIFICATIONService getAuthorizationWithController:self completion:^(NSDictionary *result) {
        NSLog(@"一键登录 result:%@", result);
    }];
~~~

***说明***：如果您需要使用极光认证的一键登录功能，请在工作日9:00—18:00联系商务申请开通，TEL：400-612-5955

##SDK自定义授权页面UI样式

###支持的版本
开始支持的版本 2.0.0

###接口定义

+ ***+ (void)customUIWithConfig:(JVUIConfig *)UIConfig;***

    + 接口说明:
        + 自定义授权页面UI样式
    + 参数说明:
        + UIConfig JVUIConfig的子类

    + 调用示例:

~~~
    /*移动*/
    JVMobileUIConfig *mobileUIConfig = [[JVMobileUIConfig alloc] init];
    mobileUIConfig.logoImg = [UIImage imageNamed:@"logo"];
    [JVERIFICATIONService customUIWithConfig:mobileUIConfig];
    
    /*联通*/
    JVUnicomUIConfig *unicomUIConfig = [[JVUnicomUIConfig alloc] init];
    unicomUIConfig.logoImg = [UIImage imageNamed:@"logo"];
    [JVERIFICATIONService customUIWithConfig:unicomUIConfig];
    
    /*电信*/
    JVTelecomUIConfig *telecomUIConfig = [[JVTelecomUIConfig alloc] init];
    telecomUIConfig.logoImg = [UIImage imageNamed:@"logo"];
    [JVERIFICATIONService customUIWithConfig:telecomUIConfig];
~~~


##JVAuthConfig类

应用配置信息类。以下是属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|AppKey |NSString|极光系统应用唯一标识，必填|
|channel|NSString|应用发布渠道，可选|
|advertisingId|NSString|广告标识符，可选|
|isProduction|BOOL|是否生产环境。如果为开发状态，设置为NO；如果为生产状态，应改为YES。可选，默认为NO|

##JVAuthEntity类

认证实体类。包含认证的手机号和token。以下是属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|number|NSString|认证手机号，必填|
|token|NSString|认证手机号码的授权码。可选，若为空，则sdk自动获取后再认证。|


##JVUIConfig类

登录界面UI配置基类。以下是属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|logoImg|UIImage|LOGO图片|

##JVMobileUIConfig类

移动登录界面UI配置类，JVUIConfig的子类。

##JVUnicomUIConfig类

联通登录界面UI配置类，JVUIConfig的子类。

##JVTelecomUIConfig类

电信登录界面UI配置类，JVUIConfig的子类。


##错误码列表

|code|描述|备注|
|:-----:|:----:|:-----:|
|1000 | verify consistent|手机号验证一致|
|1001 | verify not consistent|手机号验证不一致|
|1002 | unknown result|未知结果|
|1003 | token expired|token失效|
|1004 | sdk verify has been closed|SDK发起认证未开启|
|1005|AppKey 不存在|请到官网检查 Appkey 对应的应用是否已被删除|
|1006|frequency of verifying single number is beyond the maximum limit|同一号码自然日内认证消耗超过限制|
|1007|beyond daily frequency limit|appKey自然日认证消耗超过限制|
|1008|AppKey 非法|请到官网检查此应用详情中的 Appkey，确认无误|
|1009|当前的 Appkey 下没有创建 iOS 应用；你所使用的 JCore 版本过低|请到官网检查此应用的应用详情；更新应用中集成的 JCore 至最新。|
|1010|verify interval is less than the minimum limit|同一号码连续两次提交认证间隔过短|
|2000 | token request success |获取token 成功|
|2001 | fetch token error |获取token失败|
|2002 | sdk init failed |sdk初始化失败|
|2003 | netwrok not reachable |网络连接不通 |
|2004 | get uid failed |极光服务注册失败 |
|2005 | request timeout|请求超时|
|2006 | fetch config failed |获取配置失败|
|2008 | Token requesting, please wait|正在获取token中，稍后再试|
|2009 | verifying, please try again later|正在认证中，稍后再试 |
|2014 | internal error while requesting token|请求token时发生内部错误 |
|2015 | rsa encode failed|rsa加密失败 |
|2016|network type not supported|当前网络环境不支持认证|
|4001 ||参数错误。请检查参数，比如是否手机号格式不对|
|4009 ||解密rsa失败|
|4018 ||没有足够的余额|
|4031 ||不是认证用户|
|4032 ||获取不到用户配置|
|4033|appkey is not support login|不是一键登录用户|
|5000|bad server|服务器未知错误|
|6000|loginToken request success|获取loginToken成功|
|6001|fetch loginToken failed|获取loginToken失败|
|6002|login cancel|用户取消登录|
|6003|UI load error|UI加载异常|
|6004|authorization requesting, please try again later|正在登录中，稍候再试|
