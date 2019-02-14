# QuickApp SDK 概述
<style>
img[alt= jiguang] { width: 800px; }
</style>
## JAnalytics QuickApp
针对小米与主流⼚商联合制定统⼀标准而产生的快应用SDK，集成快速且简易，有效降低开发者的接⼊成本。


## 上报策略
JAnalytics QuickApp SDK 所有上报均为即时上报。即触发立马进行上报。

缓存上报策略：

+ 每次初始化时获取进行上报
+ 注册成功后获取缓存进行上报。

备注:注册成功前产生的事件都会先进行缓存，然后等待注册成功，注册成功后会立即获取缓存进行上报。


## 压缩包说明
供下载的 JAnalytics QuickApp SDK 压缩包，一般包含以下几个部分：

+ libs/janalytics-quickapp-sdk_1.x.x.jar
	+ SDK analysis 开发包
+ example
	+ 是一个完整的 Quick App 项目，通过这个演示了 JAnalysis SDK 的基本用法，可以用来做参考。

## 集成方式
目前SDK只支持1000或以上版本的手机系统。
参考：[QuickApp SDK 集成指南](quickapp_guide)

## 接口说明
参考：[QuickApp SDK API](quickapp_api)

## 技术支持

当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。
+ 给我们的support发邮件：[support&#64;jiguang.cn](mailto:support&#64;jiguang.cn)

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 提供appkey
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录

