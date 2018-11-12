<h1>跨应用通信</h1>


## 概述

<font color= SteelBlue>说明：跨应用通信是指允许同一开发者账号下的不同应用能互相通信，以满足开发者对于不同appKey下应用通信的需求。</font>
</br>JMessage Android SDK在v1.2.0版本中实现了单聊跨应用，v1.3.0版本中实现了群聊以及其他一些功能的跨应用，
具体对应关系见下表：

<table>
	<tr>
		<th>Since</th>
		<th>实现功能</th>
		<th>说明</th>
	</tr>
	<tr>
		<td>v1.2.0</td>
		<td>1.跨应用获取用户信息<br>2.跨应用单聊</td>
		<td>1.实现跨应用获取用户信息<br>2.实现跨应用给用户发送单聊消息</td>
	</tr>
	<tr>
		<td>v1.3.0</td>
		<td>1.跨应用群聊<br>2.跨应用黑名单设置<br>3.跨应用免打扰设置</td>
		<td>1.群组中允许加入来自不同应用下的用户，使跨应用群聊成为可能*<br>2.允许跨应用加用户至黑名单，以屏蔽来自不同应用下用户的消息<br>3. 实现跨应用添加和移除免打扰</td>
	</tr>	
</table>


**：实现跨应用群聊的关键在于群组中加入跨应用的群成员，而创建会话和发送消息的流程和普通的群聊实现方式一致。*

## 跨应用相关接口摘要

跨应用接口与非跨应用接口区别主要在于：跨应用接口增加了appkey作为参数。只要接口中需要传appkey作为参数的，均可以支持跨应用通信，详细接口说明请前往极光IM [Android API Java docs](../im_android_api_docs/)。这里仅列举一些常用的跨应用接口和实现。


### Conversation跨应用接口摘要

创建单聊跨应用会话

```
createSingleConversation(String userName, String appKey)
```  

### JMessageClient跨应用接口摘要

跨应用获取用户信息

```
getUserInfo(String username,String appKey,GetUserInfoCallback callback)  
```
    
跨应用添加群成员

```
addGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback)            
``` 

跨应用踢出群成员

```
removeGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback)
```
    
跨应用添加user进黑名单

```
addUsersToBlacklist(List<String> usernames,String appKey,BasicCallback callback)  
```    


跨应用将user移出黑名单

```
delUsersFromBlacklist(List<String> usernames,String appKey,BasicCallback callback)  
```    

### GroupInfo跨应用接口摘要

获取群成员信息

```
getGroupMemberInfo(String username, String appKey)  
```    


## 跨应用相关具体实现

### 跨应用获取用户信息

通过指定appKey可以实现获取跨应用用户信息。

```
JMessageClient.getUserInfo(java.lang.String username,java.lang.String appKey,GetUserInfoCallback callback)
```

参数定义:

* username - 开发者注册的用户名
* appKey - 指定的appKey,如果为空则在本应用appKey下查找用户
* callback - 获取用户信息的回调接口

代码示例：

```
JMessageClient.getUserInfo("username", "appKey", new GetUserInfoCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage, UserInfo info) {
         // 获取到跨应用的用户信息
         ...
    }
});
```

### 跨应用单聊实现

创建单聊会话时指定对方用户所属appKey，即可建立起一个和跨应用用户的单聊会话。

```
Conversation.createSingleConversation(String targetUsername, String appKey)
```

参数定义：

* targetUsername - 用户的username
* appKey - 指定的appKey,如果为空则默认填本应用appKey

创建跨应用会话后，创建消息发送即可。下面以创建一条单聊文本消息为例

代码示例：

```
//创建跨应用会话
Conversation con = Conversation.createSingleConversation("username", "appKey");
MessageContent content = new TextContent("hello");
//创建一条消息 
Message message = con.createSendMessage(content);
//发送消息 
JMessageClient.sendMessage(message);
```

### 跨应用群聊实现

实现跨应用群聊的关键在于群组中加入跨应用的群成员，而创建会话和发送消息的流程和普通的群聊实现方式一致。

下面列出了和跨应用操作群成员相关的接口

1.跨应用添加群成员  

```
JMessageClient.addGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback);
```
参数:

* groupID - 群组的groupID
* appKey - usernameList中user所属的appKey,如果为空则在本应用appKey下查找用户
* userNameList - 添加进群组的成员username集合
* callback - 回调接口
 
2.跨应用踢出群成员

```
JMessageClient.removeGroupMembers(long groupID,String appKey,List<String> userNameList,BasicCallback callback);
```
参数:

* groupID - 群组的groupID
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* userNameList - 踢出群组成员的username集合
* callback - 回调接口

3.获取群成员信息 

```
//此接口是实例对象上的接口
groupInfo.getGroupMemberInfo(String username, String appKey)
```
参数:

* username - 指定群成员的username 
* appKey - 群成员所属的appKey


下面以向已有群组中添加跨应用群成员，然后创建会话发送消息为例:

代码示例：

```
//添加跨应用用户到群组
JMessageClient.addGroupMembers(testGid, "appKey", userNameList, new BasicCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage) {
         //添加跨应用群成员成功之后，创建会话，发送消息。 
         if(0 == responseCode){
             Conversation conversation = Conversation.createGroupConversation(testGid);
             Message msg = conversation.createSendTextMessage("hello");
             JMessageClient.sendMessage(msg);
         }
     }
});
```

### 跨应用添加黑名单实现

通过以下接口在操作黑名单列表时指定appKey，即可实现将跨应用的用户加入黑名单。

1.添加user进黑名单

```
JMessageClient.addUsersToBlacklist(List<String> usernames,String appKey,BasicCallback callback);
```
参数:

* usernames -添加进黑名单的username集合
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* callback - 回调接口

2.将user移出黑名单

```
JMessageClient.delUsersFromBlacklist(List<String> usernames,String appKey,BasicCallback callback)
```
参数:

* usernames - 移出黑名单的username集合
* appKey - usernameList中user所属的appKey,如果appKey为空则在本应用appKey下查找用户
* callback - 回调接口


代码示例：

```
//跨应用添加用户至黑名单
JMessageClient.addUsersToBlacklist(usernames, "appKey",new BasicCallback() {
     @Override
     public void gotResult(int responseCode, String responseMessage) {
         if (0 == responseCode）{
             //成功跨应用添加用户至黑名单
             ... 
         } 
     }
}); 
```


### 跨应用免打扰实现

原有接口无需变动。免打扰相关接口是在userinfo对象上的实例接口，也就是说只要获取到的user是跨应用的用户，直接调用该userinfo对象的免打扰接口就可实现跨应用

```
userinfo.setNoDisturb(int noDisturb,BasicCallback callback)
```
参数:

  * noDisturb - 1 -- 免打扰，其他 -- 非免打扰（设置免打扰时将参数设置为1，取消免打扰时将参数设置为0）
  * callback - 回调接口

代码示例：

```
//跨应用获取用户信息
JMessageClient.getUserInfo("username", "appKey", new GetUserInfoCallback() {
    @Override
    public void gotResult(int responseCode, String responseMessage, UserInfo info) {
        //跨应用获取用户信息成功，设置用户的免打扰属性 
        if(0 == responseCode){
            info.setNoDisturb(1,null);
        }
    }
});
```


