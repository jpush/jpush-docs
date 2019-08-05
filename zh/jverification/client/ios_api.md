#iOS SDK API

##SDK接口说明

1. JVERIFICATIONService，包含SDK所有接口
2. JVAuthConfig类，应用配置信息类
3. VAuthEntity类，认证实体类
4. JVUIConfig类，登录界面UI配置基类
5. JVMobileUIConfig类，JVUIConfig的子类，移动登录界面UI配置类
6. JVUnicomUIConfig类，JVUIConfig的子类，联通登录界面UI配置类
7. JVTelecomUIConfig类，JVUIConfig的子类，电信登录界面UI配置类
8. JVLayoutConstraint类，认证界面控件布局类
9. JVLayoutItem，布局参照枚举

##SDK初始化(新增回调参数)

###支持的版本
开始支持的版本 2.3.6

###接口定义

+ ***+ setupWithConfig:(JVAuthConfig \* )config;***

    + 接口说明:
        + 初始化接口
    + 参数说明
        + config 配置类
    + 调用示例:

~~~
    // 如需使用 IDFA 功能请添加此代码并在初始化配置类中设置 advertisingId
    NSString *idfaStr = [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
    
    JVAuthConfig *config = [[JVAuthConfig alloc] init];
    config.appKey = @"AppKey copied from JiGuang Portal application";
    config.advertisingId = idfaStr;
    config.authBlock = ^(NSDictionary *result) {
        NSLog(@"初始化结果 result:%@", result);
    };
    [JVERIFICATIONService setupWithConfig:config];
~~~

##SDK初始化

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+  setupWithConfig:(JVAuthConfig \* )config;***

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

##SDK获取初始化状态

###支持的版本
开始支持的版本 2.3.2

+ ***+ (BOOL)isSetupClient***

	+ 接口说明:
		+ 初始化是否完成
	+  返回值说明
		+ YES 初始化完成
		+ NO 初始化未完成
	+ 调用示例:

~~~
BOOL isSetupClient = [JVERIFICATIONService isSetupClient];
if (isSetupClient) {
//初始化完成，可以进行后续操作
}
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

##SDK获取号码认证token（新）

###支持的版本
开始支持的版本 2.2.0

+ ***+ (void)getToken:(NSTimeInterval)timeout completion:(void (^)(NSDictionary \* result))completion;***

    + 接口说明:
        + 获取手机号校验token
    + 参数说明
        + completion  参数是字典 返回token 、错误码等相关信息，token有效期1分钟, 一次认证后失效
        + result 字典 获取到token时key有operator、code、token字段，获取不到token是key为code和content字段
        + timeout 超时时间（毫秒）,有效取值范围(0,10000],若小于等于0则取默认值5000.大于10000则取10000.为保证获取token的成功率，建议设置为3000-5000ms.

    + 调用示例:
    + 
~~~
    [JVERIFICATIONService getToken:(NSTimeInterval)timeout completion:^(NSDictionary *result) {
        NSLog(@"getToken result:%@", result)
        //TODO:获取token后相关操作
    }];
~~~


##SDK获取号码认证token（旧）

###支持的版本
开始支持的版本 1.0.0

###接口定义

+ ***+ (void)getToken:(void (^)(NSDictionary \* result))completion;***

    + 接口说明:
        + 获取号码认证token，此接口已废弃，建议使用新接口
    + 参数说明
        + completion  参数是字典 返回token、错误码等相关信息，token一次认证后失效
        + result 字典 获取到token时key有operator、code、token字段，获取不到token时key为code和content字段

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

+ ***+ (void)verifyNumber:(JVAuthEntity * )entity result:(void (^)(NSDictionary \* result))completion;***

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

***说明***：开发者调用该接口，需要在管理控制台找到该应用，并在［认证设置］-［其他设置］中开启［SDK发起认证］，建议从开发者服务端发起号码认证。

##SDK登录预取号

###支持的版本
开始支持的版本 2.2.0

+ ***+ (void)preLogin:(NSTimeInterval)timeout completion:(void (^)(NSDictionary \*result))completion***

    + 接口说明:
        + 验证当前运营商网络是否可以进行一键登录操作，该方法会缓存取号信息，提高一键登录效率。建议发起一键登录前先调用此方法。
    + 参数说明:
        + completion 预取号结果
        + result 字典 key为code和message两个字段
        + timeout 超时时间（毫秒）,有效取值范围(0,10000],若小于等于0则取默认值5000.大于10000则取10000.为保证获取token的成功率，建议设置为3000-5000ms.

    + 调用示例:

~~~
    [JVERIFICATIONService preLogin:5000 completion:^(NSDictionary *result) {
        NSLog(@"登录预取号 result:%@", result);
    }];
~~~

##SDK请求授权一键登录（新）

###支持的版本
开始支持的版本 2.3.0

+ ***+ (void)getAuthorizationWithController:(UIViewController \*)vc hide:(BOOL)hide completion:(void (^)(NSDictionary \*result))completion***

    + 接口说明:
        + 授权一键登录
    + 参数说明:
        + completion 登录结果
        + result 字典 获取到token时key有operator、code、loginToken字段，获取不到token是key为code和content字段
        + vc 当前控制器
        + hide 完成后是否自动隐藏授权页，默认YES。若此字段设置为NO，请在收到一键登录回调后调用SDK提供的关闭授权页面方法。

    + 调用示例:

~~~
    [JVERIFICATIONService getAuthorizationWithController:self hide:YES completion:^(NSDictionary *result) {
        NSLog(@"一键登录 result:%@", result);
    }];
~~~

***说明***：获取到一键登录的loginToken后，将其返回给应用服务端，从服务端调用[REST API](https://docs.jiguang.cn/jverification/server/rest_api/loginTokenVerify_api/)来获取手机号码

##SDK请求授权一键登录（旧）

###支持的版本
开始支持的版本 2.0.0

###接口定义

+ ***+ (void)getAuthorizationWithController:(UIViewController \*)vc completion:(void (^)(NSDictionary \*result))completion***

    + 接口说明:
        + 授权一键登录
    + 参数说明:
        + completion 登录结果
        + result 字典 获取到loginToken时key有operator、code、loginToken字段，获取不到loginToken时key为code和content字段
        + vc 当前控制器

    + 调用示例:

~~~
    [JVERIFICATIONService getAuthorizationWithController:self completion:^(NSDictionary *result) {
        NSLog(@"一键登录 result:%@", result);
    }];
~~~

##SDK关闭授权页面

###支持的版本
开始支持的版本 2.3.0

+ ***+ (void)dismissLoginController;***

    + 接口说明:
        + 关闭授权页

    + 调用示例:

~~~
    [JVERIFICATIONService dismissLoginController];
~~~

##SDK自定义授权页面UI样式

**<font color=red size=4>开发者不得通过任何技术手段将授权页面的隐私协议栏、slogan隐藏或者覆盖，对于接入极光认证SDK并上线的应用，我方会对上线的应用授权页面做审查，如果发现未按要求设计授权页面，将关闭应用的一键登录服务。</font>**

###支持的版本
开始支持的版本 2.0.0

###接口定义

+ ***+ (void)customUIWithConfig:(JVUIConfig \*)UIConfig;***

    + 接口说明:
        + 自定义登录页UI样式
    + 参数说明:
        + UIConfig JVUIConfig对象

~~~
    JVUIConfig *config = [[JVUIConfig alloc] init];
    config.navCustom = NO;
    config.autoLayout = YES;
    
    //弹窗
    config.showWindow = YES;
    config.windowCornerRadius = 10;
    config.windowBackgroundAlpha = 1;
    config.windowBackgroundImage = [UIImage imageNamed:@"cuccLogo"];
    CGFloat windowW = 300;
    CGFloat windowH = 300;
    JVLayoutConstraint *windowConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterY multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:windowW];
    JVLayoutConstraint *windowConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:windowH];
    config.windowConstraints = @[windowConstraintX,windowConstraintY,windowConstraintW,windowConstraintH];
    
    
    //弹窗close按钮
    UIImage *window_close_nor_image = [self imageNamed:@"close"];
    UIImage *window_close_hig_image = [self imageNamed:@"close"];
    if (window_close_nor_image && window_close_hig_image) {
        config.windowCloseBtnImgs = @[window_close_nor_image, window_close_hig_image];
    }
    CGFloat windowCloseBtnWidth = window_close_nor_image.size.width?:15;
    CGFloat windowCloseBtnHeight = window_close_nor_image.size.height?:15;;
    JVLayoutConstraint *windowCloseBtnConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeRight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeRight multiplier:1 constant:-5];
    JVLayoutConstraint *windowCloseBtnConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:5];
    JVLayoutConstraint *windowCloseBtnConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeWidth multiplier:1 constant:windowCloseBtnWidth];
    JVLayoutConstraint *windowCloseBtnConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:windowCloseBtnHeight];
    config.windowCloseBtnConstraints = @[windowCloseBtnConstraintX,windowCloseBtnConstraintY,windowCloseBtnConstraintW,windowCloseBtnConstraintH];
    
    
    
    //logo
    config.logoImg = [UIImage imageNamed:@"cmccLogo"];
    CGFloat logoWidth = config.logoImg.size.width?:100;
    CGFloat logoHeight = logoWidth;
    JVLayoutConstraint *logoConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *logoConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:10];
    JVLayoutConstraint *logoConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:logoWidth];
    JVLayoutConstraint *logoConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:logoHeight];
    config.logoConstraints = @[logoConstraintX,logoConstraintY,logoConstraintW,logoConstraintH];
    
    
    //号码栏
    JVLayoutConstraint *numberConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *numberConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:130];
    config.numberConstraints = @[numberConstraintX,numberConstraintY];
    
    //slogan展示
    JVLayoutConstraint *sloganConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *sloganConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:160];
    config.sloganConstraints = @[sloganConstraintX,sloganConstraintY];
    
    
    //登录按钮
    UIImage *login_nor_image = [self imageNamed:@"loginBtn_Nor"];
    UIImage *login_dis_image = [self imageNamed:@"loginBtn_Dis"];
    UIImage *login_hig_image = [self imageNamed:@"loginBtn_Hig"];
    if (login_nor_image && login_dis_image && login_hig_image) {
        config.logBtnImgs = @[login_nor_image, login_dis_image, login_hig_image];
    }
    CGFloat loginButtonWidth = login_nor_image.size.width?:100;
    CGFloat loginButtonHeight = login_nor_image.size.height?:100;
    JVLayoutConstraint *loginConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *loginConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:180];
    JVLayoutConstraint *loginConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:loginButtonWidth];
    JVLayoutConstraint *loginConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:loginButtonHeight];
    config.logBtnConstraints = @[loginConstraintX,loginConstraintY,loginConstraintW,loginConstraintH];
    
    //勾选框
    UIImage * uncheckedImg = [self imageNamed:@"checkBox_unSelected"];
    UIImage * checkedImg = [self imageNamed:@"checkBox_selected"];
    CGFloat checkViewWidth = uncheckedImg.size.width;
    CGFloat checkViewHeight = uncheckedImg.size.height;
    config.uncheckedImg = uncheckedImg;
    config.checkedImg = checkedImg;
    JVLayoutConstraint *checkViewConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeLeft relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeLeft multiplier:1 constant:20];
    JVLayoutConstraint *checkViewConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeBottom relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeBottom multiplier:1 constant:-45];
    JVLayoutConstraint *checkViewConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:checkViewWidth];
    JVLayoutConstraint *checkViewConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:checkViewHeight];
    config.checkViewConstraints = @[checkViewConstraintX,checkViewConstraintY,checkViewConstraintW,checkViewConstraintH];
    
    
    
    //隐私
    CGFloat spacing = checkViewWidth + 20 + 5;
    config.privacyState = YES;
    config.appPrivacyOne = @[@"应用自定义服务条款1",@"https://www.jiguang.cn/about"];
    config.appPrivacyTwo = @[@"应用自定义服务条款2",@"https://www.jiguang.cn/about"];
    
    JVLayoutConstraint *privacyConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeLeft relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeLeft multiplier:1 constant:spacing];
    JVLayoutConstraint *privacyConstraintX2 = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeRight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeRight multiplier:1 constant:-spacing];
    JVLayoutConstraint *privacyConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeBottom relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeBottom multiplier:1 constant:-20];
    JVLayoutConstraint *privacyConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:50];
    config.privacyConstraints = @[privacyConstraintX,privacyConstraintX2,privacyConstraintY,privacyConstraintH];
    
    
    //loading
    JVLayoutConstraint *loadingConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *loadingConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterY multiplier:1 constant:0];
    JVLayoutConstraint *loadingConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:30];
    JVLayoutConstraint *loadingConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:30];
    config.loadingConstraints = @[loadingConstraintX,loadingConstraintY,loadingConstraintW,loadingConstraintH];
    
    
    
    
    /*
     config.authPageBackgroundImage = [UIImage imageNamed:@"背景图"];
     config.navColor = [UIColor redColor];
     config.barStyle = 0;
     config.navText = [[NSAttributedString alloc] initWithString:@"自定义标题"];
     config.navReturnImg = [UIImage imageNamed:@"自定义返回键"];
     UIButton *button = [UIButton buttonWithType:UIButtonTypeCustom];
     button.frame = CGRectMake(0, 0, 44, 44);
     button.backgroundColor = [UIColor greenColor];
     config.navControl = [[UIBarButtonItem alloc] initWithCustomView:button];
     config.logoHidden = NO;
     config.logBtnText = @"自定义登录按钮文字";
     config.logBtnTextColor = [UIColor redColor];
     config.numberColor = [UIColor blueColor];
     config.appPrivacyColor = @[[UIColor redColor], [UIColor blueColor]];
     config.sloganTextColor = [UIColor redColor];
     config.navCustom = NO;
     config.numberSize = 24;
     config.privacyState = YES;
     */
    [JVERIFICATIONService customUIWithConfig:config customViews:nil];
    
    
~~~


##SDK授权页面添加自定义控件

###支持的版本
开始支持的版本 2.1.0

###接口定义

+ ***+ (void)customUIWithConfig:(JVUIConfig \*)UIConfig customViews:(void(^)(UIView \*customAreaView))customViewsBlk;***

    + 接口说明:
        + 自定义授权页面UI样式，并添加自定义控件
    + 参数说明:
        + UIConfig JVUIConfig的子类
        + customViewsBlk 添加自定义视图的block

    + 调用示例:

~~~
          
    JVUIConfig *config = [[JVUIConfig alloc] init];
    config.navCustom = NO;
    config.autoLayout = YES;
    
    //弹窗
    config.showWindow = YES;
    config.windowCornerRadius = 10;
    config.windowBackgroundAlpha = 1;
    config.windowBackgroundImage = [UIImage imageNamed:@"cuccLogo"];
    CGFloat windowW = 300;
    CGFloat windowH = 300;
    JVLayoutConstraint *windowConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterY multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:windowW];
    JVLayoutConstraint *windowConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:windowH];
    config.windowConstraints = @[windowConstraintX,windowConstraintY,windowConstraintW,windowConstraintH];
    
    
    //弹窗close按钮
    UIImage *window_close_nor_image = [self imageNamed:@"close"];
    UIImage *window_close_hig_image = [self imageNamed:@"close"];
    if (window_close_nor_image && window_close_hig_image) {
        config.windowCloseBtnImgs = @[window_close_nor_image, window_close_hig_image];
    }
    CGFloat windowCloseBtnWidth = window_close_nor_image.size.width?:15;
    CGFloat windowCloseBtnHeight = window_close_nor_image.size.height?:15;;
    JVLayoutConstraint *windowCloseBtnConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeRight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeRight multiplier:1 constant:-5];
    JVLayoutConstraint *windowCloseBtnConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:5];
    JVLayoutConstraint *windowCloseBtnConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeWidth multiplier:1 constant:windowCloseBtnWidth];
    JVLayoutConstraint *windowCloseBtnConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:windowCloseBtnHeight];
    config.windowCloseBtnConstraints = @[windowCloseBtnConstraintX,windowCloseBtnConstraintY,windowCloseBtnConstraintW,windowCloseBtnConstraintH];
    
    
    
    //logo
    config.logoImg = [UIImage imageNamed:@"cmccLogo"];
    CGFloat logoWidth = config.logoImg.size.width?:100;
    CGFloat logoHeight = logoWidth;
    JVLayoutConstraint *logoConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *logoConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:10];
    JVLayoutConstraint *logoConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:logoWidth];
    JVLayoutConstraint *logoConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:logoHeight];
    config.logoConstraints = @[logoConstraintX,logoConstraintY,logoConstraintW,logoConstraintH];
    
    
    //号码栏
    JVLayoutConstraint *numberConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *numberConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:130];
    config.numberConstraints = @[numberConstraintX,numberConstraintY];
    
    //slogan展示
    JVLayoutConstraint *sloganConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *sloganConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:160];
    config.sloganConstraints = @[sloganConstraintX,sloganConstraintY];
    
    
    //登录按钮
    UIImage *login_nor_image = [self imageNamed:@"loginBtn_Nor"];
    UIImage *login_dis_image = [self imageNamed:@"loginBtn_Dis"];
    UIImage *login_hig_image = [self imageNamed:@"loginBtn_Hig"];
    if (login_nor_image && login_dis_image && login_hig_image) {
        config.logBtnImgs = @[login_nor_image, login_dis_image, login_hig_image];
    }
    CGFloat loginButtonWidth = login_nor_image.size.width?:100;
    CGFloat loginButtonHeight = login_nor_image.size.height?:100;
    JVLayoutConstraint *loginConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *loginConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeTop multiplier:1 constant:180];
    JVLayoutConstraint *loginConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:loginButtonWidth];
    JVLayoutConstraint *loginConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:loginButtonHeight];
    config.logBtnConstraints = @[loginConstraintX,loginConstraintY,loginConstraintW,loginConstraintH];
    
    //勾选框
    UIImage * uncheckedImg = [self imageNamed:@"checkBox_unSelected"];
    UIImage * checkedImg = [self imageNamed:@"checkBox_selected"];
    CGFloat checkViewWidth = uncheckedImg.size.width;
    CGFloat checkViewHeight = uncheckedImg.size.height;
    config.uncheckedImg = uncheckedImg;
    config.checkedImg = checkedImg;
    JVLayoutConstraint *checkViewConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeLeft relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeLeft multiplier:1 constant:20];
    JVLayoutConstraint *checkViewConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeBottom relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeBottom multiplier:1 constant:-45];
    JVLayoutConstraint *checkViewConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:checkViewWidth];
    JVLayoutConstraint *checkViewConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:checkViewHeight];
    config.checkViewConstraints = @[checkViewConstraintX,checkViewConstraintY,checkViewConstraintW,checkViewConstraintH];
    
    
    
    //隐私
    CGFloat spacing = checkViewWidth + 20 + 5;
    config.privacyState = YES;
    config.appPrivacyOne = @[@"应用自定义服务条款1",@"https://www.jiguang.cn/about"];
    config.appPrivacyTwo = @[@"应用自定义服务条款2",@"https://www.jiguang.cn/about"];
    
    JVLayoutConstraint *privacyConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeLeft relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeLeft multiplier:1 constant:spacing];
    JVLayoutConstraint *privacyConstraintX2 = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeRight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeRight multiplier:1 constant:-spacing];
    JVLayoutConstraint *privacyConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeBottom relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeBottom multiplier:1 constant:-20];
    JVLayoutConstraint *privacyConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:50];
    config.privacyConstraints = @[privacyConstraintX,privacyConstraintX2,privacyConstraintY,privacyConstraintH];
    
    
    //loading
    JVLayoutConstraint *loadingConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *loadingConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterY multiplier:1 constant:0];
    JVLayoutConstraint *loadingConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:30];
    JVLayoutConstraint *loadingConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:30];
    config.loadingConstraints = @[loadingConstraintX,loadingConstraintY,loadingConstraintW,loadingConstraintH];
    
    
    
    
    /*
     config.authPageBackgroundImage = [UIImage imageNamed:@"背景图"];
     config.navColor = [UIColor redColor];
     config.barStyle = 0;
     config.navText = [[NSAttributedString alloc] initWithString:@"自定义标题"];
     config.navReturnImg = [UIImage imageNamed:@"自定义返回键"];
     UIButton *button = [UIButton buttonWithType:UIButtonTypeCustom];
     button.frame = CGRectMake(0, 0, 44, 44);
     button.backgroundColor = [UIColor greenColor];
     config.navControl = [[UIBarButtonItem alloc] initWithCustomView:button];
     config.logoHidden = NO;
     config.logBtnText = @"自定义登录按钮文字";
     config.logBtnTextColor = [UIColor redColor];
     config.numberColor = [UIColor blueColor];
     config.appPrivacyColor = @[[UIColor redColor], [UIColor blueColor]];
     config.sloganTextColor = [UIColor redColor];
     config.navCustom = NO;
     config.numberSize = 24;
     config.privacyState = YES;
     */
    [JVERIFICATIONService customUIWithConfig:config customViews:^(UIView *customAreaView) {
        /*
         //添加一个自定义label
         UILabel *lable  = [[UILabel alloc] init];
         lable.text = @"这是一个自定义label";
         [lable sizeToFit];
         lable.center = customAreaView.center;
         [customAreaView addSubview:lable];
         */
        
    }];
~~~


##JVLayoutItem枚举

|枚举值|枚举说明|
|:-----:|:-----:|
|JVLayoutItemNone |不参照任何item。可用来直接设置width、height|
|JVLayoutItemLogo|参照logo视图|
|JVLayoutItemNumber|参照号码栏|
|JVLayoutItemSlogan|参照标语栏|
|JVLayoutItemLogin|参照登录按钮|
|JVLayoutItemCheck|参照隐私选择框|
|JVLayoutItemPrivacy| 参照隐私栏|
|JVLayoutItemSuper|参照父视图|

##JVLayoutConstraint类
属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|firstAttribute |NSLayoutAttribute|约束类型|
|relation|NSLayoutRelation|与参考视图之间的约束关系|
|item|JVLayoutItem|参照item|
|attr2|NSLayoutAttribute|参照item约束类型|
|multiplier|CGFloat|乘数|
|c|CGFloat|常量|

##创建JVLayoutConstraint布局对象

+ ***+ (instancetype)constraintWithAttribute:(NSLayoutAttribute)attr1<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;relatedBy:(NSLayoutRelation)relation<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;toItem:(JVLayoutItem)item<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;attribute:(NSLayoutAttribute)attr2<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;multiplier:(CGFloat)multiplier<br>
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;constant:(CGFloat)c;***

+ 接口说明:
   + 创建JVLayoutConstraint布局对象

+ 接口说明:
    + attr1 约束类型
    + relation 与参照视图之间的约束关系
    + item 参照item
    + attr2 参照item约束类型
    + multiplier 乘数
    + c 常量

+ 调用示例:

~~~
    CGFloat windowW = 300;
    CGFloat windowH = 300;
    JVLayoutConstraint *windowConstraintX = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterX multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintY = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemSuper attribute:NSLayoutAttributeCenterY multiplier:1 constant:0];
    JVLayoutConstraint *windowConstraintW = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeWidth relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeWidth multiplier:1 constant:windowW];
    JVLayoutConstraint *windowConstraintH = [JVLayoutConstraint constraintWithAttribute:NSLayoutAttributeHeight relatedBy:NSLayoutRelationEqual toItem:JVLayoutItemNone attribute:NSLayoutAttributeHeight multiplier:1 constant:windowH];
    config.windowConstraints = @[windowConstraintX,windowConstraintY,windowConstraintW,windowConstraintH];
~~~

##JVAuthConfig类

应用配置信息类。以下是属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|AppKey |NSString|极光系统应用唯一标识，必填|
|channel|NSString|应用发布渠道，可选|
|advertisingId|NSString|广告标识符，可选|
|isProduction|BOOL|是否生产环境。如果为开发状态，设置为NO；如果为生产状态，应改为YES。可选，默认为NO|
|authBlock|Block|初始化回调，包含code和content两个参数。10s未完成则返回超时|

##JVAuthEntity类

认证实体类。包含认证的手机号和token。以下是属性说明：

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|number|NSString|认证手机号，必填|
|token|NSString|认证手机号码的授权码。可选，若为空，则sdk自动获取后再认证。|


##JVUIConfig类

授权界面UI配置基类。以下是属性说明：

+ 授权页面设置

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|authPageBackgroundImage|UIImage|授权界面背景图片|
|autoLayout|BOOL|是否使用autoLayout，默认YES，|
|shouldAutorotate|BOOL|是否支持自动旋转 默认YES|
|orientation|UIInterfaceOrientation|设置进入授权页的屏幕方向，不支持UIInterfaceOrientationPortraitUpsideDown|

+ 导航栏

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|navCustom|BOOL|是否隐藏导航栏（适配全屏图片）|
|navColor|UIColor|导航栏颜色|
|barStyle|UIBarStyle|状态栏着色样式|
|navText|NSAttributedString|导航栏标题|
|navReturnImg|UIImage|导航返回图标|
|navControl|UIBarButtonItem|导航栏右侧自定义控件|

+ LOGO

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|logoImg|UIImage|LOGO图片|
|logoWidth|CGFloat|LOGO图片宽度|
|logoHeight|CGFloat|LOGO图片高度|
|logoOffsetY|CGFloat|LOGO图片偏移量|
|logoConstraints|NSArray|LOGO图片布局对象|
|logoHidden|BOOL|LOGO图片隐藏|

+ 登录按钮

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|logBtnText|NSString|登录按钮文本|
|logBtnOffsetY|CGFloat|登录按钮Y偏移量|
|logBtnConstraints|NSArray|登录按钮布局对象|
|logBtnTextColor|UIImage|登录按钮文本颜色|
|logBtnImgs|UIColor|登录按钮背景图片添加到数组(顺序如下) @[激活状态的图片,失效状态的图片,高亮状态的图片]|

+ 手机号码

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|numberColor|UIColor|手机号码字体颜色|
|numberSize|CGFloat|手机号码字体大小|
|numFieldOffsetY|CGFloat|号码栏Y偏移量|
|numberConstraints|NSArray|号码栏布局对象|

+ checkBox

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|uncheckedImg|UIImage|checkBox未选中时图片|
|checkedImg|UIImage|checkBox选中时图片|
|checkViewConstraints|NSArray|checkBox布局对象|
|privacyState|BOOL|checkBox默认选中状态 默认:NO|

+ 隐私协议栏

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|appPrivacyOne|NSArray|隐私条款一:数组（务必按顺序）@[条款名称,条款链接]|
|appPrivacyTwo|NSArray|隐私条款二:数组（务必按顺序）@[条款名称,条款链接]|
|appPrivacyColor|UIImage|隐私条款名称颜色 @[基础文字颜色,条款颜色]|
|privacyOffsetY |CGFloat|隐私条款Y偏移量(注:此属性为与屏幕底部的距离)|
|privacyComponents|NSArray|隐私条款拼接文本数组|
|privacyConstraints|NSArray|隐私条款布局对象|

+ slogan

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|sloganOffsetY|CGFloat|slogan偏移量Y|
|sloganConstraints|NSArray|slogan布局对象|
|sloganTextColor|UIColor|slogan文字颜色|

+ loading

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|loadingConstraints|NSArray|loading布局对象|

+ 弹窗

|参数名称|参数类型|参数说明|
|:-----:|:----:|:-----:|
|showWindow|BOOL|是否弹窗，默认no|
|windowBackgroundImage|UIImage|弹窗内部背景图片|
|windowBackgroundAlpha|CGFloat|弹窗外侧 透明度  0~1.0|
|windowCornerRadius|CGFloat|弹窗圆角数值|
|windowConstraints|NSArray|弹窗布局对象|
|windowCloseBtnImgs|NSArray|弹窗close按钮图片 @[普通状态图片，高亮状态图片]|
|windowCloseBtnConstraints|NSArray|弹窗close按钮布局|

![JVerification](../image/cutomeUI_description.png)

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
|7000|preLogin success|预取号成功|
|7001|preLogin failed|预取号失败|
|7002|preLogin requesting, please try again later|取号中|
|8000|init success|初始化成功|
|8005|init timeout|初始化超时|
