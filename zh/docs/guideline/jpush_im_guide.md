# JPush IM 指南

### 认识 JPush IM

JPush IM 为开发者提供快速集成 IM 功能到 App 里的功能。开发者只需要很少的工作，集成 IM SDK 到 App 里，做简单的接口集成，就可以使得 App 具有了全流程的 IM 功能。

JPush IM 的致力于帮 App 解决 IM 聊天问题。其核心能力在于 IM 聊天本身。其他的附属功能是可选的：用户信息提交、群组维护、好友维护。 

开发者可选择只是单纯注册用户，然后让这些用户之间互发消息，而不使用其他附加功能。

鉴于好友关系的敏感性，我们暂未实现开放这部分功能。


### JPush IM 与 JPush 的关系

JPush IM 是以 JPush 作为基础的，共享 JPush 的网络长连接。

SDK 侧，IM SDK 包含了 JPush 的完整功能，以 JPush SDK 的基础之上再附加上 IM 功能。

REST API 部分，原有 Push 相关的 REST API 可继续使用，可向集成了 IM SDK 的客户端做 Push 相关操作。

Web 控制台上，还是原来的基础流程，只是增加了 IM 功能。

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


### JPush IM 功能集

#### IM SDK

+ 注册用户（可选不在客户端注册）
+ 登录用户
+ 更新用户信息
+ 单聊
+ 创建群组
+ 添加、删除群组成员
+ 群聊

好友关系维护相关功能，稍后的版本提供。

#### REST API

+ 注册用户
+ 发送消息
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

