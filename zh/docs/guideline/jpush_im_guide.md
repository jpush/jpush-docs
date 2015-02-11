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



### 相关文档

+ [IM SDK](../../client/im_sdk/)
+ [IM REST API](../../server/rest_api_im/)

