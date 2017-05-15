#JShare产品介绍

极光Share致力于帮助应用快速具备国内主流社交平台分享功能，提供接入新浪微博，QQ，微信等第三方社会化分享服务；SDK包体积小，集成成本低，提供iOS和Android的SDK，并且还提供了统计功能，方便开发者了解应用的分享效果，提高产品推广效率，助力产品获得更多用户。


##JShare技术原理

目前市面上依赖平台原生SDK的分享SDK皆为这种形式：
![](image/yilaiban.png)但是，极光Share技术上不依赖原生SDK的方式，分享的原理实际上就是两个APP之间的相互跳转和通信，使用极光Share代替平台SDK实现分享，其原理如下图：![](image/feiyilaiban.png)JShare SDK分享遵循以下步骤：

1.注册Appkey。<br>
2.配置分享参数。<br>
3.发起分享。<br>
4.等待回调<br>

##功能与特性

1.集成简单<br>
&emsp;&emsp;只需几分钟即可集成JShare组件，让您的应用轻松拥有强大的社会化功能。<br>
2.稳定，安装包小<br>
&emsp;&emsp;不依赖第三方平台的库包，极大的减少SDK的体积。<br>
3.社会化统计分析<br>
&emsp;&emsp;完整的统计和分析后台，帮助开发者了解各项统计指标。<br>
4.一键分享<br>
&emsp;&emsp;通过组件对新浪微博，QQ，微信等社会化平台一键分享；分享内容包括文字、图片、链接、音视频、文件、表情等。<br>


##集成流程

在Web控制台上创建应用，得到Appkey。如果之前已经使用了JPush，可以直接延用老的Appkey。

集成客户端SDK。<br>
Android开发者请参考文档:[JShare Android SDK 集成指南](../client/Android/android_sdk.md)<br>
IOS开发者请参考文档：[JShare iOS SDK 集成指南](../client/iOS/ios_sdk.md)<br>

###相关文档
[JShare Android SDK 接口文档](../client/Android/android_api.md)<br>
[JShare iOS SDK 接口文档](../client/iOS/ios_api.md)