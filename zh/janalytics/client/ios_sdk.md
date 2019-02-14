# iOS SDK 概述
<style>
img[alt= jiguang] { width: 800px; }
</style>
## JAnalytics iOS
### 模块化的极光开发者SDK
极光开发者服务SDK采用了模块化的使用模式，即一个核心（JCore）+N种服务（JPush，JAnalytics，...）的使用方式，方便开发者使用某一项服务或多项服务，极大的优化了多模块同时使用时功能模块重复的问题。如下图：
![jiguang](./image/sdk_model.png)

## 上报策略
JAnalytics iOS SDK采用了数据记录与数据上报分离的策略，数据实时记录，按照上报策略上报数据。

+ 打开应用上报
+ 关闭应用上报

备注：如遇到极端情况导致数据上报不成功，数据不会被清除，等待下一次上报策略触发再上报。

## 动态圈选及自动统计策略
v2.0.0及以上版本支持。

按最新的集成指南关于动态圈选的描述集成，可加入动态圈选及自动统计功能，不需要额外加入统计埋点代码。

在极光管理控制台扫二维码开启圈选功能，跳转到应用出现圈选按钮，移动圈选红圈点，可圈选定义需要统计的视图，圈选确定后被圈选的视图自动加入统计功能，按钮类的视图可自动统计点击浏览事件，非按钮类的视图可自动统计浏览事件，按上述上报策略上报。

###关于UITableViewCell及UICollectionViewCell动态圈选及自动统计需要注意下

* 自动统计UITableViewCell的点击事件，需要实现UITableView的delegate中tableView:didSelectRowAtIndexPath:方法
* 自动统计UITableViewCell的滑动浏览事件，需要实现UITableView的delegate中tableView:didEndDisplayingCell:forRowAtIndexPath:方法
* 自动统计UICollectionViewCell的点击事件，需要实现UICollectionView的delegate中collectionView:didSelectItemAtIndexPath:方法
* 自动统计UICollectionViewCell的滑动浏览事件，需要实现UICollectionView的delegate中collectionView:didEndDisplayingCell:forItemAtIndexPath:方法

## 压缩包说明
+ janalytics-ios-x.x.x.a静态库
+ jcore-ios-x.x.x.a静态库
+ 统计入口JANALYTICSService.h头文件
+ 统计事件对象文件JANALYTICSEventObject.h头文件
+ 一个完整的 iOS  Demo项目，通过这个演示了 JAnalytics SDK 的基本用法，可以用来做参考。

## 集成方式
目前SDK只支持iOS 7以上版本的手机系统。

参考：[JAnalytics iOS SDK 集成指南](ios_guide)

## 接口说明
参考：[JAnalytics iOS API](ios_api)

## 技术支持

当出现问题时：

+ 请仔细阅读文档，查看是否有遗漏。
+ 给我们的support发邮件：[support&#64;jiguang.cn](mailto:support&#64;jiguang.cn)

为了更快速的解决问题，在寻求帮助时，请提供下列信息：

+ 提供appkey
+ 如果是 SDK 问题请提供对应的 SDK 版本和完整的日志记录


