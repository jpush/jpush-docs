# 已知的BUG
## Portal & API
+ 基于别名或者标签推送时，如果指定只推送某一个平台（Android/iOS），则会二个平台都推送
	+ FIXED: 2013.0719
+ Portal 上推送时有时候 extra 信息下去是空的
	+ 具体步骤是：推送完成后，提示“推送成功，是否去查看推送记录？”时，你选择“留下来继续发送”这个选项时，再次推送填写的扩展字段信息会被丢失掉。
	+ FIXED: 2013.04.27
+ 历史推送记录那里，复制一条记录重发时，没有复制附加信息
	+ FIXED: 2013.03.06 发布上线的 v2 版本 Portal 已经解决此问题。
## Android SDK
+ r1.3.5 resumePush恢复Push开关滞后，会导致紧跟着 resumePush 后的其他API调用失效。
	+ FIXED: r1.3.6 已经发布，修改了这个问题。
## iOS SDK
+ r1.2.8 以及之前的版本：部分设备的 device token 上报不正常，导致不能够收到推送消息。
	+ FIXED: r1.3.0 已经发布。
+ r1.2.6 以及之前的版本：JPush iOS SDK 内部使用 OpenUdid 方式来唯一地标识设备。但是，发挥发现 iOS 6 上 OpenUdid 值会改变，不能唯一地标识一台设备了。这会导致，同一台设备，JPush SDK 会注册为多个用户。群发推送时，同一条消息可能会收到多个。
	+ FIXED: r1.2.7 提供 UDID 版本下载，JPush iOS SDK 内部使用原生的 UDID 来唯一地标识设备。[https://www.jpush.cn/home/download-ios.jsp](https://www.jpush.cn/home/download-ios.jsp)