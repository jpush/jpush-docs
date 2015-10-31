#示例与代码 

##Android Example 项目

这里说的 Example 示例项目，是个标准的 Android 应用项目。
把这个应用，导入到你的 Eclipse 开发环境，就可以 demo 起来 JPush Android SDK 的基本功能。

### Portal 上下载 Example

极光推送开发者在管理平台（Portal）上登录后，创建一个新的应用，填写上你自己应用的包名，应用创建成功后，其详情界面有个按钮 "下载 Android Example"。

这里下载到的 Android Example 项目，是个 appKey 与 Android应用包名都已经被填写好的应用项目。

开发者把这个应用导入 Eclipse 里边，理论上就可以马上编译成功（不需要动一行代码与配置），运行安装到手机（或者模拟器）里去。

这个 Android Example 也就是 [3 分钟快速 Demo](../guideline/android_3m) 快速教程提及到的示例项目。



### Android SDK 下载包里的 Example

这个 Example 里的 AndroidManifest.xml 配置文件，包名、AppKey 等配置位置，都是留空的，需要你根据你本身应用的情况去填写。

##服务器端 API 开发包与示例

极光推送官方维护 Java Library，以及使用本开发包的示例代码：[Java开发包与使用示例。](https://github.com/jpush/jpush-api-java-client/releases)

并且其源代码也是开源放在 github 上的，请参考上述页面。

##完整的项目 
### 推聊（PushTalk）
+ 这是开发者 Good-Life 贡献的开源项目，已经有其他开发者在共同参与
+ 该项目包含有 Android 客户端（嵌入JPush Android SDK），iOS 客户端（嵌入 JPush iOS SDK），与聊天服务器（调用 JPush Remote API）
+ 发布网站：[http://androidpush.cn/](http://androidpush.cn/)
+ 开源项目：[https://github.com/good-life/PushTalk/](https://github.com/good-life/PushTalk/)
	+ 打包下载最新代码：[https://github.com/good-life/PushTalk/archive/master.zip](https://github.com/good-life/PushTalk/archive/master.zip)
	+ 下载打包好可运行的文件：[https://github.com/good-life/PushTalk/tree/master/dist](https://github.com/good-life/PushTalk/tree/master/dist)
+ 首发介绍文章：[http://www.androidpush.cn/post/2012-11-27/40043266501](http://www.androidpush.cn/post/2012-11-27/40043266501)
+ 定制指南文章：[http://www.androidpush.cn/post/2012-12-01/pushtalk_customization_guide](http://www.androidpush.cn/post/2012-12-01/pushtalk_customization_guide)
![](image/pushtalk_architecture_2.png)