#最近更新

###iOS SDK v1.3.0

####更新时间
+ 2017-10-10


####Change Log
+ 增加 Facebook 平台分享功能
+ 增加 Facebook 平台授权和获取个人信息功能

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件


###Android SDK v1.3.0

####更新时间
+ 2017-10-10

####Change Log
+ 增加 Facebook 平台分享功能
+ 增加 Facebook 平台授权和获取个人信息功能
+ 修复bug

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的 zip 压缩包。
+ 更新库文件。
	- 打开 libs 文件夹。删除原有极光 jar 文件, 并将 jcore-android-1.x.y.jar 、 jshare-android-1.3.0.jar、jshare-qq-android-1.3.0.jar、jshare-sina-android-1.3.0.jar、jshare-wechat-android-1.3.0.jar 以及 jshare-facebook-android-1.3.0.jar 复制入 libs 文件夹。
用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的极光 so 文件。
+ 更新 AndroidManifest.xml。
	- 压缩包根目录下有示例 AndroidManifest 文件。请对照示例更新跟 JShare 相关的组件属性，permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
+ 更新 JGShareSDK.xml。
	- 压缩包根目录下有示例 JGShareSDK 文件。请对照示例更新各个平台配置。
+ 如果使用 jcenter 的方式集成 JShare，不需要添加相关组件和资源，详细说明请参考官方集成指南。





###iOS SDK v1.2.1

####更新时间
+ 2017-9-1


####Change Log
+ 修复取消获取微信用户信息崩溃的 Bug。

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件



###Android SDK v1.2.1

####更新时间
+ 2017-7-21

####Change Log
+ 修复bug

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的 zip 压缩包。
+ 更新库文件。
	- 打开 libs 文件夹。删除原有极光jar文件, 并将 jcore-android-1.x.y.jar 、 jshare-android-1.2.0.jar、jshare-qq-android-1.2.0.jar、jshare-sina-android-1.2.0.jar以及jshare-wechat-android-1.2.0.jar 复制入libs 文件夹。
用对应CPU文件夹下的 libjcorexxx.so文件，替换项目中原有的极光so文件。
+ 更新 AndroidManifest.xml。
	- 压缩包根目录下有示例 AndroidManifest 文件。请对照示例更新跟 JShare 相关的组件属性，permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
+ 更新 JGShareSDK.xml。
	- 压缩包根目录下有示例 JGShareSDK 文件。请对照示例更新各个平台配置。
+ 如果使用 jcenter 的方式集成 JShare，不需要添加相关组件和资源，详细说明请参考官方集成指南。




###Android SDK v1.2.0

####更新时间
+ 2017-7-17

####Change Log
+ 增加微信、微博、QQ授权、获取第三方个人信息功能。
+ 修复QQ未登陆时没有回调问题。

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的 zip 压缩包。
+ 更新库文件。
	- 打开 libs 文件夹。删除原有极光jar文件, 并将 jcore-android-1.x.y.jar 、 jshare-android-1.2.0.jar、jshare-qq-android-1.2.0.jar、jshare-sina-android-1.2.0.jar以及jshare-wechat-android-1.2.0.jar 复制入libs 文件夹。
用对应CPU文件夹下的 libjcorexxx.so文件，替换项目中原有的极光so文件。
+ 更新 AndroidManifest.xml。
	- 压缩包根目录下有示例 AndroidManifest 文件。请对照示例更新跟 JShare 相关的组件属性，permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
+ 更新 JGShareSDK.xml。
	- 压缩包根目录下有示例 JGShareSDK 文件。请对照示例更新各个平台配置。
+ 如果使用 jcenter 的方式集成 JShare，不需要添加相关组件和资源，详细说明请参考官方集成指南。



###iOS SDK v1.2.0

####更新时间
+ 2017-7-17


####Change Log
+ 增加获取微信、QQ、新浪微博社交平台用户信息功能。
+ 修复 Bug。

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件


###Android SDK v1.1.0

####更新时间
+ 2017-5-25

####Change Log
+ 支持不存在新浪客户端情况下的网页分享。
+ 支持分享内容至新浪微博私信。

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的 zip 压缩包。
+ 更新库文件。
	- 打开 libs 文件夹。删除原有极光 jar 文件, 并将 jcore-android-v1.x.y.jar 、 jshare-android-v1.1.0.jar、jshare-qq-android-v1.1.0.jar、jshare-sina-android-v1.1.0.jar 以及 jshare-wechat-android-v1.1.0.jar 复制入 libs 文件夹。
用对应 CPU 文件夹下的 libjcorexxx.so 文件，替换项目中原有的极光 so 文件。
+ 更新 AndroidManifest.xml。
	- 压缩包根目录下有示例 AndroidManifest 文件。请对照示例更新跟 JShare 相关的组件属性，permission，Action 等配置。并在中文提示的位置替换你的包名 和 appkey。
+ 更新 JGShareSDK.xml。
	- 压缩包根目录下有示例 JGShareSDK 文件。请对照示例更新各个平台配置。
+ 如果使用 jcenter 的方式集成 JShare，不需要添加相关组件和资源，详细说明请参考官方集成指南。

###iOS SDK v1.1.0

####更新时间
+ 2017-5-25


####Change Log
+ 支持不存在新浪客户端情况下的网页分享。
+ 支持分享内容至新浪微博私信。
+ 修复部分 Log 错误。
+ 支持 CocoaPods。

####升级提升
+ 建议升级

####升级指南
+ 首先解压您获取到的zip压缩包
+ 更新库文件


###Android SDK v1.0.0

####更新时间
+ 2017-4-18

####Change Log
+ 支持基本内容分享到微信好友，微信朋友圈、QQ好友、QQ空间、新浪微博。


###iOS SDK v1.0.0

####更新时间
+ 2017-4-18


####Change Log
+ 支持基本内容分享到微信好友，微信朋友圈、QQ好友、QQ空间、新浪微博。
