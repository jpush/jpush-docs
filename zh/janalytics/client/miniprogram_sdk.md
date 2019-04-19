# MiniProgram SDK 概述


## JAnalytics MiniProgram

针对微信小程序开发的统计SDK，集成快速且简易，有效降低开发者的接⼊成本。

SDK的配置流程：

![jiguang](./image/miniprogram_flow.png)

其中，开发者需登录「微信公众平台」，在「开发-开发设置-服务器域名」的「request合法域名」中添加合法域名。


## 上报策略

JAnalytics MiniProgram SDK 所有上报均为即时上报。即触发立马进行上报。

缓存上报策略：

+ 每次初始化时判断注册状态，已注册获取缓存上报，未注册触发注册
+ 注册成功前产生的事件都会先进行缓存,注册成功后获取缓存进行上报。


## 压缩包说明
供下载的 JAnalytics MiniProgram SDK 压缩包，一般包含以下几个部分：

+ libs/janalytics-m-1.x.x.js
	+ SDK analysis 开发包
+ libs/janalytics-conf.js
	+ SDK analysis 配置文件
+ example
	+ 是一个完整的小程序项目，通过这个演示了 JAnalysis SDK 的基本用法，可以用来做参考。

## 集成方式
参考：[MiniProgram SDK 集成指南](miniprogram_guide)

## 接口说明
参考：[MiniProgram SDK API](miniprogram_api)

## 技术支持

当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。
+ 给我们的 support 发邮件：[support&#64;jiguang.cn](mailto:support&#64;jiguang.cn)

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 提供 appkey
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录

