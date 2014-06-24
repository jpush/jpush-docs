# Rich Push 开发指南
## 概述
Rich Push，即富媒体推送，允许开发者推送 Web页面、图片、声音等除普通文本之外更丰富的内容。

应用开发者可以利用“富文本推送”功能推送如新闻、优惠券、活动信息等更加丰富的内容，也可以使用“富媒体文件推送” 使已有的 IM 类沟通功能得到扩展。

JPush从终端用户使用体验的角度出发，充分考虑到国内的网络环境特点，Rich Push 功能上做了些特别的设计：1）Portal 上准备资源时，都保存到 JPush 的服务器上；2）JPush SDK 展示推送前预加载媒体文件。这样保证了一个富文本推送页面展示时是一定可见的、完整的。


## 功能说明
功能上分为富文本推送和富媒体文件推送二个部分。


### 富文本推送
+ 推送 Web 页面（富文本）
+ Portal 上提供推送工具，来快捷地创建富文本页面
+ 富文本作为通知推送到客户端
+ 客户端点击通知，自动展示该富文本页面

Portal 上的推送工具包括：在线HTMl编辑器，模板功能（保存、编辑）。

+ 推送图片、音频以及其他任何格式的文件 
+ 媒体文件作为“自定义消息”推送下去
+ 在客户端 JPush SDK 广播消息给 App 时，除了自定义消息内容本身外，还附带了富媒体文件在 SDCard 上保存的路径

Portal 上提供上传新的文件，或者指定一个媒体文件的URL 地址。


### 富媒体文件推送
## 开发步骤
### 下载支持 Rich Push 的 JPush Android SDK
下载地址：[http://www.jpush.cn/sdk/android](http://www.jpush.cn/sdk/android)

根据相关文档集成到 Android App 里。

### 推送富文本通知

JPush Portal （管理控制台）上，新建一个 Android 应用，或者对已经存在的 Android 应用，进行下图所示操作。

![](../image/Snip20130701_52.png)

之后根据提示信息，可以基于模板或者任意地自己创建 Web页面。

推送到客户端后，通知栏里点击通知，会自动展现出来这个页面。

客户端可不做更多的处理。如果需要处理，请参考相关 Android 客户端关于 Rich Push 的文档。

### 推送富媒体文件消息
JPush Portal （管理控制台）上，新建一个 Android 应用，或者对已经存在的 Android 应用，进行下图所示操作。
![](image/Snip20130701_52.png)

富媒体文件推送到客户端后，JPush SDK 不会自动展现。客户端 App 需要去收取广播消息，以取得该消息内容，包括媒体文件的 SDCard 路径。具体操作请参考 Android 客户端相关文档。


## SDK 支持

Rich Push 需要响应 SDK 版本配合支持

+ JPush Android SDK 1.4.0 及以上
+ JPush iOS SDK（后续支持）

## 限制条件

JPush为了保证最终的体验做如下限制：

### 富文本页面

+ 不允许包含 `<link>,<script>,<video>,<object>,<audio> ,<embed><iframe>`标签
+ 资源文件总大小不能超过 200K
+ HTML不能超过 20K
+ 不允许使用外部 CSS 和 JS 文件
 
### 富媒体文

文件大小不能超过 200K

## See Also
[富文本页面 Javascript 回调API](../android_api)
