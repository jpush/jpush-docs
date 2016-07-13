## JMessage WEB SDK 开发文档

### SDK概述

极光WebIM SDK 为 Web 应用提供一个 IM 系统开发框架, 屏蔽掉 IM 系统的复杂的细节, 对外提供较为简洁的 API 接口, 方便第三方应用快速集成 IM 功能。


### 签名算法

开发者在执行登录的时候，需要传入auth_payload。 该数据结构由开发者服务端生成并传回浏览器，用于开发者授权此浏览器运行的JMessage登录。开发者需确保能调用获取到此数据的皆为合法用户。
  
auth_payload的数据结构如下:  
  
```
{
    "appkey": "7e42e869baa2fbca8ccb823c",
    "random_str": "022cd9fd995849b58b3ef0e943421ed9",
    "signature": "E422A978DE37196588531CD0C42010B5",
    "timestamp": "1467967210887"
}
```

参数说明:
  
* appkey : 开发者在极光平台注册的IM应用appkey
* random_str : 20-36长度的随机字符串, 作为签名加salt使用
* timestamp : 当初时间戳，用于防止重放攻击
* signature : 签名

签名生成算法如下:  
  
```
signature = md5(appkey=appkey&timestamp=timestamp&random_str=random_str&key=secret)
```  

其中secret为开发者在极光平台注册的IM应用masterSecret。


### 开发准备

#### 1  引入sockit.io.js
JiGuang WebIM是基于[sockit.io](http://socket.io/)开发，开发者在使用之前需引入`sockit.io.js`。

CDN源:

```
// 官网CDN源
<script src="//cdn.socket.io/socket.io-1.4.5.js"></script>

// bootcdn源
<script src="//cdn.bootcss.com/socket.io/1.4.5/socket.io.min.js"></script>
```

以上CDN源引入任一一个即可，开发者也可以将socket.io.js下载到自己的项目目录并手动引入，建议引入最新版本的socket.io。

#### 2  引入jmessage-web-sdk.min.js

```
<script src='./jmessage-sdk-web-1.0.0.min.js'></script>
```
引入该js后便可使用window上的全局变量`JIM`。

#### 3  调用JIM.init()进行初始化。
```
JIM.init({debug:true});
```

### API

#### 初始化 JIM.init()

PS: 此API是进行`JIM.login()`的前置动作，需要调用此接口才能进行登录操作。

**Params:**  
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|debug|FALSE|是否开启DEBUG模式，DEBUG模式会有更多日志打印，默认不开窍|
|address|FALSE|JMessage服务器地址，一般不需要指定，默认即可|
|timeout|FALSE|请求超时时间，默认为30秒|

**Example:**  
  
```javascript
Jim.init({
  debug: true //是否开启debug模式
})
```

#### 登陆 JIM.login()

PS: 此API是IM业务方法的前置动作，需要登录后，才能进行后续的接口调用

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|username|TRUE|用户名|
|password_md5|TRUE|进行MD5处理后的用户密码|
|auth_payload|TRUE|签名，具体创建方法见签名算法|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**  
  
```javascript
JIM.login(username, password, auth_payload, function(data) {
    // 登录结果返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 获取用户信息 JIM.getUserInfo()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|username|TRUE|用户名|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.getUserInfo('xiezefan', 'username', function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 发送单聊消息 JIM.sendSingleMsg()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|target_username|TRUE|消息接受者username|
|content|TRUE|消息文本|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.sendSingleMsg(friend_id, 'Hi, JPush', function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 发送群组消息 JIM.sendGroupMsg()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|target_gid|TRUE|消息接受群组gid|
|content|TRUE|消息文本|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.sendGroupMsg(group_id, 'Hi, JPush', function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 创建群组 JIM.createGroup()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|group_name|TRUE|群组名称|
|group_description|TRUE|群组描述|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.createGroup('Group Name', 'Group Description', function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 获取群组列表 JIM.getGroupList()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.getGroupList(function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 获取群组信息 JIM.getGroupInfo()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.getGroupInfo(group_id, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 增加群组成员 JIM.addGroupMember()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|username_list|TRUE|增加进群组的用户名列表|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.addGroupMember(group_id, ['xiezefan01', 'xiezefan02', 'xiezefan03'], function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 删除群组成员 JIM.delGroupMember()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|username_list|TRUE|增加进群组的用户名列表|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.delGroupMember(group_id, ['xiezefan01', 'xiezefan02', 'xiezefan03'], function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 获取群组成员列表 JIM.getGroupMembers()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.getGroupMembers(group_id, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 更新群组信息 JIM.updateGroupInfo()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|group_name|TRUE|群组名称|
|group_description|TRUE|群组描述|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.updateGroupInfo(group_id, 'New Group Name', 'New Group Description', function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 退出群组 JIM.exitGroup()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|gid|TRUE|群组gid|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.exitGroup(group_id, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```


#### 获取会话列表 JIM.getConversations()

**Params:**
  
|KEY|REQUIRE|DESCIPTION|
|----|----|----|
|resp_callback|FALSE|返回数据处理回调函数，不处理则忽略或传入null|
|ack_callback|FALSE|请求送达回调函数，不处理则忽略或传入null|
|timeout_callback|FALSE|请求超时回调函数，不处理则忽略或传入null|  
  
**Example:**

```
JIM.getConversations(function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 登出 JIM.loginOut()

#### 聊天消息监听

**Example:**

```
JIM.onMsgReceive(function(data) {
    // 聊天消息处理
});
```  

**Event Payload Example**

```
{
  "uid": 16836751, // 消息接受者ID
  "messages": [
    {
      "from_gid": 0, // 消息发送群组ID 
      "msg_type": 3, // 消息类型，3单聊， 4群聊
      "ctime": 1468152712, // msgid 生成时间，单位秒
      "msg_id": 79206290, // 消息ID
      "msg_level": 0, //0-普通消息 1-跨应用消息 2-系统提示 ...
      "from_uid": 16887920, // 消息发送者ID
      "content": "Hi, JPush" // 消息正文
    }
  ],
  "rid": 79206290, // 流水ID
  "event": "msg_sync" // 业务事件名，忽略
}
```
#### 业务事件监听

**Example:**  
  
```
JIM.onEvent(function(data) {
    // 业务事件处理
});
```


**Event Payload Example**

```
{
  "uid": 16836751, 
  "event_id": 59826578, // 事件ID
  "event_type": 12, // 事件类型
  "gid": 10210335,
  "to_uidlist": [], // 事件当事人
  "extra": 0, // 用于好友邀请事件：1-来自邀请方的事件，2－来自被邀请方，即好友邀请的应答事件
  "description": {
    "validUtf8": true,
    "empty": true
  },
  "ctime": 1468152292, // event_id 生成时间，单位秒
  "rid": 59826578, // 流水ID
  "event": "event_notification",
  "return_code": 0, // 用于好友邀请应答事件：0－添加好友成功，其他为添加好友被拒绝的返回码
  "from_uid": 16836751 // 事件发起者
}
```


