# 短信验证码概述
## 功能
极光面向开发者提供短信验证码服务，主要包括：

+ SDK 短信验证功能，满足 App 短信验证需求。
+ REST API 短信验证，主要满足网站和其他终端访问需求。

## 主要场景
+ 用户注册；
+ 登录验证；
+ 关键信息修改；
+ 支付确认；
+ 人员身份有效性确认。

## 试用步骤
+ 注册成为极光开发者。
+ 通过极光后台创建 APP 得到 AppKey（如果之前创建过可以通用）。


## 充值和开通
目前没有自动充值的方式，如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business/form)。

## FAQ

**长度计算**

70个字记一条短信费，如果超过70个字则按照每条67个字拆分，逐条计费。单个汉字、标点、英文都算一个字。


## 集成指南
* [JSMS Android SDK 集成指南](../client/Android_SMS_SDK.md)。
* [JSMS iOS SDK 集成指南](../client/iOS_SMS_SDK.md)。
* [JSMS Rest API](../server/rest_api_jsms.md)。
