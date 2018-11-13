#iOS SDK API

##SDK接口说明

1. JVERIFICATIONService，包含SDK所有接口
2. JVAuthConfig类，应用配置信息类
3. VAuthEntity类，认证实体类

##SDK初始化

+ ***+ setupWithConfig:(JVAuthConfig * )config;***

    + 接口说明:
        + 初始化接口
    + 参数说明
        + config 配置类
    + 调用示例:

~~~
    JVAuthConfig *config = [[JVAuthConfig alloc] init];
    config.appKey = @"your appkey";
    [JVERIFICATIONService setupWithConfig:config];
~~~

##SDK获取token

+ ***+ (void)getToken:(void (^)(NSDictionary * result))completion;***

    + 接口说明:
        + 获取手机号校验token
    + 参数说明
        + completion  参数是字典 返回token 、错误码等相关信息，token有效期1分钟, 一次认证后失效
        + result 字典 获取到token时key有code、token两个字段，获取不到token是key为code和content字段

    + 调用示例:
~~~
    [JVERIFICATIONService getToken:^(NSDictionary *result) {
        NSLog(@"getToken result:%@", result)
        //TODO:获取token后相关操作
    }];
~~~

***说明***：开发者可以通过SDK获取token接口的回调信息来选择验证方式，若成功获取到token则可以继续使用极光认证进行号码验证；若获取token失败，需要换用短信验证码等方式继续完成验证。

##SDK发起认证

+ ***+ (void)verifyNumber:(JVAuthEntity * )entity result:(void (^)(NSDictionary * result))completion;***

    + 接口说明:
        + 手机号认证
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

##SDK设置debug模式

+ ***+  (void)setDebug:(BOOL)enable;***
    + 接口说明:
        + 开启debug模式
    +  参数说明
        + enable 是否开启debug模式

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

##错误码列表

|code|描述|备注|
|:-----:|:----:|:-----:|
|1000 | verify consistent|手机号验证一致|
|1001 | verify not consistent|手机号验证不一致|
|1002 | unknown result|未知结果|
|1003 | token expired|token失效|
|2000 | token request success |获取token 成功|
|2001 | fetch token error |获取token失败|
|2002 | sdk init failed |sdk初始化失败|
|2003 | netwrok not reachable |网络连接不通 |
|2004 | get uid failed |极光服务注册失败 |
|2005 | request timeout|请求超时|
|2006 | fetch config failed |获取配置失败|
|2008 | Token requesting, please wait|正在获取token中，稍后再试|
|2009 | verifying, please try again later|正在认证中，稍后再试 |
|4001 ||参数错误。请检查参数，比如是否手机号格式不对|
|4009 ||解密rsa失败|
|4018 ||没有足够的余额|
|4031 ||不是认证用户|
|4032 ||获取不到用户配置|
|5000|bad server|服务器未知错误|
|1005|AppKey 不存在|请到官网检查 Appkey 对应的应用是否已被删除|
|1008|AppKey 非法|请到官网检查此应用详情中的 Appkey，确认无误|
|1009|当前的 Appkey 下没有创建 iOS 应用；你所使用的 Jcore 版本过低|请到官网检查此应用的应用详情；更新应用中集成的 JCore 至最新。|
