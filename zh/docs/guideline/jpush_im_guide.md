# JPush IM 指南

### 认识 JPush IM

开发者可以通过 JPush IM 服务快速集成 IM 功能到 App 里。只需要很少的工作，集成 IM SDK，做简单的接口集成，就可以使得自己的 App 具备了用户间聊天的功能。

JPush IM 致力于帮助 App 解决 IM 聊天问题。其核心能力在于 IM 聊天本身。其他的附属功能是可选的：用户信息提交、群组维护、好友维护。 

开发者可选择只是单纯注册用户，然后让这些用户之间互发消息，而不使用其他附加功能。

鉴于好友关系的敏感性，我们暂未实现开放这部分功能。

#### JPush IM 与 JPush 的关系
JPush IM 以 JPush 技术作为基础，共享 JPush 的网络长连接。在保留了 JPush 推送全部功能的基础上增加了额外的 IM 功能。 

集成 JPush IM 服务的应用，从SDK接口，服务端 REST API，Web 控制台都具备并且兼容 JPush 的推送功能。

![image](../image/jpush_im_sdk.png)

```
对于同一个应用 JPush IM 与 JPush 使用同样的 APPkey 和 master secret
```

#### JPush IM 与 JPush 的区别
JPush IM 以 IM 使用场景出发，面向用户根据登录帐号来收发消息，而 JPush 推送则是面向移动设备，根据设备的标签以及使用属性进行推送。

#### 推送与 IM 服务如何选择
开发者可以根据自身业务场景来选择适用的业务。


### JPush IM 基本概念

##### username（用户名）

这是 App 的用户名，App 里用来唯一地标识其用户。

username （用户名）必须唯一！

App 调用 IM SDK 时实际使用的，可以是其用户的 ID，用户帐号名，或者 Email，总之任何一个唯一地标识其用户的，都可以。

##### groupId（群组ID）

App 使用 JPush IM 提供的群组功能创建群组时，得到的群组标识。之后发群组消息、加人踢人等操作，都需要这个群组ID。

##### AppKey（应用Key）

这是 JPush 用来唯一地标识一个 App 的标识，需要在 JPush Web Portal 上去创建。SDK 集成时，需要配置此 Key，以便 JPush 识别当前用户属于某个应用。

同一个 AppKey 里用户名必须唯一！ 不同的 AppKey 之间用户名可以重名。


* 如果你的应用需要实现用户之间相互传递消息的 IM 功能，那么使用 JPush IM 则是为您准备的。
* 如果应用主要以发送功能通知，活动推广，订阅与广播内容为主，应该选择更为简洁的推送服务。如果后续业务上需要扩展，可以再集成 JPush IM，平滑添加，对原有的 Push 功能无任何影响。




### JPush IM 功能与特性

#### IM SDK

+ 注册用户（Webporal 可以控制是否允许客户端自由注册）
+ 用户登录
+ 更新用户信息
+ 单聊
+ 支持的消息类型：文本、语音、图片
+ 支持的平台：Android, iOS 并可互通
+ 创建群组
+ 添加、删除群组成员
+ 群聊

好友关系维护相关功能，稍后的版本提供。

#### REST API

+ 注册用户
+ 发送消息
+ 维护用户
+ 维护群组

#### Web Portal

+ 创建应用
+ 注册用户
+ 发送消息
+ 维护群组

#### Web IM

+ 登录用户
+ 单聊
+ 群聊

### 集成流程

...


### 相关文档

+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [IM REST API](../../server/rest_api_im/)

