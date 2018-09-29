#iOS SDK 概述

##JVerification iOS

###模块化的极光开发者SDK

极光开发者服务SDK采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JVerification，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。如下图：

![JVerification](../image/sdk_model.png)

##压缩包说明

供下载的JVerification iOS SDK压缩包，一般包含以下几部分：
* jverification-iOS-x.x.x.a静态库
* jcore-ios-x.x.x.a静态库
* 认证入口JVERIFICATIONService.h头文件
* 一个完整的iOS Demo项目，通过这个演示了JVerification SDK的基本用法，可以用来做参考

##集成方式

目前SDK只支持iOS 7以上版本的手机系统。参考：[iOS SDK 集成指南](../ios_guide)

##接口说明

参考：[iOS SDK API](../ios_api)

##技术支持

当出现问题时：

* 请仔细阅读文档，查看是否有遗漏
* 给我们的support发邮件：[support&#64;jpush.cn](mailto:support&#64;jpush.cn)

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

* 提供appKey
* 如果是SDK问题请提供对应的SDK版本和完整的日志记录
