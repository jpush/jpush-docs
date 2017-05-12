# JMessage API client library for CSharp

## 概述
JMessage's officially supported CSharp client library for accessing JMessage APIs. 极光IM官方支持的 CSharp 版本服务器端 SDK。

## 安装
###  本地安装
*   安装第三方依赖 Json.NET
*   项目引用添加 jmessage.dll

### nuget 安装
*   nuget 搜索并安装 Json.NET
*   nuget 搜索并安装 jmessage

## 使用

###  以用户注册为例

>以下代码节选自项目目录  example/UserExamples/RegistUserExample.cs

```
UserPayload user = new UserPayload("username", "password");
List<UserPayload> users = new List<UserPayload> { user };
ResponseWrapper content = client.registUser(users);
```
###  以文本消息发送为例
>以下代码节选自项目目录  example\MessageExamples\SendTextMessageExample.cs

```
TextMessageBody msg_body = new TextMessageBody();
msg_body.text= "text";
msg_body.extras = null;
TextMessagePayload payload = new TextMessagePayload("1", "single", "admin", "text", "xiaohuihui", "admin",msg_body);
ResponseWrapper content = client.sendMessage(payload);          
```
###  以创建群组为例
>以下代码节选自项目目录  example\GroupExamples\CreateGroupExample.cs

```
List<string> members_username = new List<string> { "xiaohuihui", "jintian" };
GroupPayload payload = new GroupPayload("toms", "xiaohuihui", members_username, "jmessage");
ResponseWrapper content = client.createGroup(payload);
```

###  以添加好友为例
>以下代码节选自项目目录  example\FriendExamples\AddFriendsExample.cs

```
List<string> members_username = new List<string> {"jintian" };       
ResponseWrapper content = client.addFriends("xiaohuihui", members_username);
```

###  以跨应用管理群组成员为例
>以下代码节选自项目目录  example\CrossExamples\GroupExample.cs

```
String appkey = "6be9204c30b9473e87bad4dc";
List<string> add = new List<string> { "jmessage123" };
CrossMemberPayload payload = new CrossMemberPayload(appkey, add, null);
List<CrossMemberPayload> payloads = new List<CrossMemberPayload> { };
payloads.Add(payload);    
ResponseWrapper content = client.crossAddRemoveMembers("19749893", payloads);
```

## REST 文档
> 文档地址：https://docs.jiguang.cn/jmessage/server/rest_api_im/

## ErrorCode
> 文档地址：https://docs.jiguang.cn/jmessage/client/im_errorcode_server/
