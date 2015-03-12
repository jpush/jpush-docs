# JPush IM 指南

### 认识 JPush IM

开发者可以通过 JPush IM 服务快速集成 IM 功能到 App 里。只需要很少的工作，集成 IM SDK，做简单的接口集成，就可以使得自己的 App 具备了用户间聊天的功能。

JPush IM 致力于帮助 App 解决 IM 聊天问题。其核心能力在于 IM 聊天本身。其他的附属功能是可选的。 开发者可选择只是单纯注册用户，然后让这些用户之间互发消息，而不使用其他附加功能。

鉴于好友关系的敏感性，我们暂未实现开放这部分功能。

#### JPush IM 与 JPush 的关系

JPush IM 以 JPush 技术作为基础，共享 JPush 的网络长连接。在保留了 JPush 推送全部功能的基础上增加了附加的 IM 功能。 

集成 JPush IM 服务的应用，从客户端 SDK，到服务端 REST API，Web 控制台，都具备并且兼容 JPush 的全部功能。

![im_sdk_and_jpush](../image/jpush_im_sdk.png)

	对于同一个应用 JPush IM 与 JPush 使用同样的 AppKey。

#### JPush IM 与 JPush 的区别

|                  | JPush        | JPush IM       |
| ------------ | ------------- | ------------------ |
| 使用场景 | 应用推送 | IM聊天、社交 |
| 面向对象 | 设备          | 用户、帐号     |
| 消息对象 | App 运营人员或者 App Server 向用户推送 | 用户之间互相交流 |
| 发送方式 | 支持广播、Tag，或者单设备 | 单聊、群群 |
 
JPush IM 以 IM 使用场景出发，面向用户根据登录帐号来收发消息；而 JPush 则满足推送场景，面向移动设备，根据设备的标签以及使用属性进行推送。

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

#### JPush 更新后的架构

![jpush_im_architecture](../image/jpush_im_architecture.png)

上图是 JPush 新增了 IM 服务后的整体架构图。通过此图可以理解：

+ IM SDK 里支持的推送部分，与 IM 部分使用同一个网络长连接。
+ 服务器端接入服务器在两个服务之间是共享的。
+ 接入服务器之上，二套服务整体相对独立、分离。

#### JPush IM 的相对优势

+ 基于 JPush 的大规模、高并发、稳定的推送服务的技术基础，JPush IM 服务从刚开始就是相对稳定、可靠、大容量的即时消息服务。
+ IM SDK 与 JPush SDK 合并在一起，一个网络连接同时支持 IM 与 Push 业务。
+ IM 业务与 Push 业务完美集成，先使用 Push 服务时可平滑升级。
+ JPush 团队之前就是开发 IM App 的，对 IM 业务具有更深刻的理解，能够持续地改进与革新 IM 服务。


### JPush IM 功能与特性

#### IM SDK

+ 聊天类型：文本、语音、图片。
+ 聊天对象：单聊、群聊。
+ 平台支持：Android, iOS, Web，三平台互通。
+ 用户维护：注册、登录、头像、用户其他信息。
+ 群组维护：创建群组、加群、退群。

好友关系维护相关功能，稍后的版本提供。

#### REST API

+ 发送消息
+ 用户信息维护
+ 群组维护

#### Web Portal

+ 创建应用
+ 发送消息
+ 注册用户
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

