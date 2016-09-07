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

| KEY     | TYPE | REQUIRE | DESCIPTION                                               |      |
| ------- | ---- | ------- | ---------------------------------                        | ---- |
| debug   | boolean | FALSE   | 是否开启DEBUG模式，DEBUG模式会有更多日志打印，默认不开窍 |      |
| address | string | FALSE   | JMessage服务器地址，一般不需要指定，默认即可             |      |
| timeout | string | FALSE   | 请求超时时间，默认为30秒                                 |      |

**Example:**  

```javascript
JIM.init({
  debug: true //是否开启debug模式
})
```

#### 登陆 JIM.login()

PS: 此API是IM业务方法的前置动作，需要登录后，才能进行后续的接口调用
PS: sdk中集成了MD5处理，用户可以自由选择传入的密码是否做过MD5处理。

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                                                                                                     |
| ---------------- | ---- | ------- | ----------------------------------------                                                                                       |
| username         | string | TRUE    | 用户名                                                                                                                         |
| password         | string | TRUE    | 明文密码或进行MD5处理后的用户密码                                                                                              |
| auth_payload     | json | TRUE    | 签名，具体创建方法见签名算法                                                                                                   |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null                                                                                   |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null                                                                                       |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null                                                                                       |
| is_md5           | boolean | FALSE   | 传入的密码是否已经做了MD5处理：不传或者值为false，则sdk会对传入的密码做md5处理；传入的值为true，则sdk不会对传入的密码做md5处理 |

**Example:**  

```javascript
JIM.login(username, password, auth_payload, function(data) {
    // 登录结果返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
}, is_md5);
```

#### 获取用户信息 JIM.getUserInfo()

**Params:**
| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| username         | string | TRUE    | 用户名                                       |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE  | REQUIRE | DESCIPTION                                   |
| ---------------- | ----- | ------- | ------------------------                     |
| target_username  | string | TRUE    | 消息接受者username                           |
| target_nickname  | string | TRUE    | 消息接受者nickname                           |
| content          | json | TRUE    | 消息文本                                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| target_gid       | string | TRUE    | 消息接受群组gid                              |
| group_name       | string | TRUE    | 群组消息name                                 |
| content          | json | TRUE    | 消息文本                                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

#### 获取消息构建器MsgBuilder JIM.createMsgBuilder()

**MsgBuilder**

MsgBuilder提供链式调用风格的API帮助开发者构建符合[JMessage消息协议](http://docs.jiguang.cn/advanced/im_message_protocol/)的聊天消息对象。

主要提供一下方法:  

* setType(type) 设置消息类型
    * type : 消息类型，必填，取值single或group
* setTarget(target, target_name) 设置消息接受对象
    * target : 消息接收对象，必填，单聊消息为username，群聊消息为group_id
    * target_name : 消息接受者名称，非必须，单聊消息为用户昵称，群聊消息为群组名称，如果不填，JMessage Server会自动填充
* setFromName(from_name) 设置发送者名称
    * from_name : 发送者名称，非必填，如不填，JMessage Server会自动填充
* setText(content, extras) 设置文本消息
    * content : 文本消息内容，必填
    * extras : 附加参数, 任意格式的JSON对象，非必填
* setCustom(custom) 设置自定义消息
    * custom : 自定义消息对象，必填 
* send($resp, $ack, $timeout) 发送消息
    * $resp : 返回数据处理回调函数，不处理则忽略或传入null
    * $ack : 请求送达回调函数，不处理则忽略或传入null
    * $timeout : 请求超时回调函数，不处理则忽略或传入null

**Example:**

```javascript
JIM.createMsgBuilder()
        .setType('single')
        .setTarget(friend_name, 'friend_nickname')
        .setFromName('from_name')
        .setImage('media_id', 'media_crc32', 600, 400, 'format', 'fsize', 'img_link', {'key1':'value1', 'key2':'value2'})
        .send(function(data) {
            // 返回处理
        }, function(ack) {
            // 请求送达JMessage服务器事件处理
        }, function(timeout) {
            // 请求发送超时事件处理
        });  
        
```


#### 创建群组 JIM.createGroup()

**Params:**

| KEY               | TYPE | REQUIRE | DESCIPTION                                   |
| ----------------- | ---- | ------- | ------------------------                     |
| group_name        | string | TRUE    | 群组名称                                     |
| group_description | string | TRUE    | 群组描述                                     |
| resp_callback     | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback      | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback  | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```javascript
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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | TRUE    | 群组gid                                      |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```javascript
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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | TRUE    | 群组gid                                      |
| username_list    | array | TRUE    | 增加进群组的用户名列表                       |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | TRUE    | 群组gid                                      |
| username_list    | array | TRUE    | 增加进群组的用户名列表                       |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | TRUE    | 群组gid                                      |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY               | TYPE | REQUIRE | DESCIPTION                                   |
| ----------------- | ---- | ------- | ------------------------                     |
| gid               | string | TRUE    | 群组gid                                      |
| group_name        | string | TRUE    | 群组名称                                     |
| group_description | string | TRUE    | 群组描述                                     |
| resp_callback     | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback      | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback  | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | TRUE    | 群组gid                                      |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

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

#### 获取免打扰 JIM.getNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.getNoDisturb(function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 添加单聊免打扰 JIM.addSingleNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| target_name      | string | true    | 需要设置为免打扰的单聊用户target_name        |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.addSingleNoDisturb(target_name, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 删除单聊免打扰 JIM.deleteSingleNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| target_name      | string | true    | 需要取消为免打扰的单聊用户target_name        |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.deleteSingleNoDisturb(target_name, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 添加群聊免打扰 JIM.addGroupNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | true    | 需要设置为免打扰的群组gid                    |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.addGroupNoDisturb(gid, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 删除群聊免打扰 JIM.deleteGroupNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| gid              | string | true    | 需要删除为免打扰的群组gid                    |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.deleteGroupNoDisturb(gid, function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 添加全局免打扰 JIM.addGlobalNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.addGlobalNoDisturb(function(data) {
    // 返回处理
}, function(ack) {
    // 请求送达JMessage服务器事件处理
}, function(timeout) {
    // 请求发送超时事件处理
});
```

#### 删除全局免打扰 JIM.deleteGlobalNoDisturb()

**Params:**

| KEY              | TYPE | REQUIRE | DESCIPTION                                   |
| ---------------- | ---- | ------- | ------------------------                     |
| resp_callback    | function | FALSE   | 返回数据处理回调函数，不处理则忽略或传入null |
| ack_callback     | function | FALSE   | 请求送达回调函数，不处理则忽略或传入null     |
| timeout_callback | function | FALSE   | 请求超时回调函数，不处理则忽略或传入null     |

**Example:**

```
JIM.deleteGlobalNoDisturb(function(data) {
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

**Msg Payload Example**

```
{
  "target_type": "single", //"single"为单聊，"group"为群聊
  "target_name": "user1", //接收用户的昵称，当target_type为single时，target_name对应的是单聊用户的昵称，当target_type为group时，target_name对应的是群组的名称
  "target_id": "userid1", //接收用户的id，当target_type为single时，target_name对应的是单聊用户的id，当target_type为group时，target_name对应的是群组的gid
  "from_name": "user2", //发送用户的昵称，当target_type为single时，from_name对应的是单聊用户的昵称，当target_type为group时，from_name对应的是群组的名称
  "from_id": "userid2", //发送用户的id，当target_type为single时，from_id对应的是单聊用户的id，当target_type为group时，from_id对应的是群组的gid
  "from_platform": "web", //发送消息的平台
  "create_time": 1472128104291, //消息创建时间戳
  "msg_type": "text", //消息类型，有文本-"text", 图片-"image", 语音-"voice", 文件-"file"
  "msg_body": {
    "text": "HI, Jpush", //文本信息
    "media_id": "id", //MEDIA 文件上传之后服务器端所返回的key，用于之后生成下载的url
    "media_crc32": "stirng", // 文件的crc32校验码
    "format": "type", //文件格式
    "duration": 200, //语音消息的时长，单位秒
    "fsize": 300, //文件大小（字节数）
    "media_url": "url" //文件，图片，语音类消息的资源下载地址
  }, //消息体, 消息的内容都在消息体中,ps:不同的消息类型，返回值有所区别，这里只是字段示例
  "msg_level": "normal" //"normal"-普通，"across"-跨应用
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
