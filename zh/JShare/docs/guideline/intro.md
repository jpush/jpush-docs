#JSHARE产品介绍

极光SHARE致力于帮助应用快速具备国内主流社交平台分享功能，提供了接入新浪微博，QQ，微信等第三方社会化分享服务；SDK包体积最小，集成成本低，提供IOS和ANDROID的SDK，并且还提供了统计功能，方便开发者了解应用的分享效果，提高产品推广效率，助力产品获得更多用户。


##JSHARE技术原理
目前市面上的依赖平台原生SDK的分享SDK皆为这种形式
<DIV>
![](IMAGE/YILAIBAN.PNG)但是，极光SHARE技术上不依赖原生SDK的方式，分享的原理实际上就是两个APP之间的相互跳转及通信，使用极光SHARE代替平台SDK实现分享，其原理如下图：
<DIV>
![](IMAGE/FEIYILAIBAN.PNG)JSHARE SDK分享遵循以下步骤。

1.注册APPKEY。<BR>
2.配置分享参数。<BR>
3.发起分享。<BR>
4.等待回调。<BR>

##功能与特性

1.集成简单<BR>
	&EMSP;&EMSP;只需几分钟即可集成JSHARE组件，让您的应用轻松拥有强大的社会化功能。<BR>
2.稳定，安装包小<BR>
	&EMSP;&EMSP;不依赖第三方平台的库包，极大的减少SDK的体积，让分享更稳定。<BR>
3.社会化统计分析<BR>
	&EMSP;&EMSP;完整的统计和分析后台，帮助开发者了解各项统计指标。<BR>
4.一键分享<BR>
	&EMSP;&EMSP;通过组件对新浪微博、QQ、微信等社会化平台一键分享；分享内容包括文字、图片、链接、音视频、文件表情等。<BR>
	
##集成流程

在 WEB 控制台上创建应用，得到 APPKEY。如果之前已经使用了 JPUSH，可以直接延用老的 APPKEY。

集成客户端 SDK。<BR>
集成 JSHARE SDK 到 APP 里.<BR>
ANDROID 开发者请参考文档：[JSHARE ANDROID SDK 集成指南](../CLIENT/ANDROID/ANDROID_SDK.MD)<BR>
IOS 开发者请参考文档：[JSHARE IOS SDK 集成指南](../CLIENT/IOS/IOS_SDK.MD)<BR>

###相关文档

[JSHARE ANDROID SDK 接口文档](../CLIENT/ANDROID/ANDROID_API.MD)<BR>
[JSHARE IOS SDK 接口文档](../CLIENT/IOS/IOS_API.MD)