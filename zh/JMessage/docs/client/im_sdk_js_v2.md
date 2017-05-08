<h1>Web SDK 开发指南 V2</h1>

## 概述

极光 IM Web SDK 为 Web 应用提供一个 IM 系统开发框架, 屏蔽掉 IM 系统的复杂的细节, 对外提供较为简洁的 API 接口, 方便第三方应用快速集成 IM 功能。

## 版本说明

JMessage Web SDK V2版本对SDK通讯协议进行重新封装与优化:

* 提供更方便的API调用方式: 使用Promise风格的API，简化了接口调用方式，开发者可以更简单方便的集成SDK。
* 更可靠的消息重试方案: 新的SDK优化了消息重试技术方案，当弱网络环境下，出现消息发送失败，SDK会自动重试5次，并保证每次API调用都是幂等的，开发者无需担心因为消息重试导致重复发送的情况。
* 支持单页面多聊天实例: 新的SDK修改了实例化方式，开发者可以不需要在页面初始化的时候就初始化JMessage。在需要聊天功能的时候再进行初始化即可，并且一个页面可以初始化多个通道，实现多账号登录。

因为V2 API全面改造了API，为了提供更好的用户体验，V2 API不向下兼容，开发者需要根据JMessage Web SDK文档重新接入SDK。

## 鉴权

开发者在执行初始化的时候，需要传入auth_payload。 该数据结构由开发者服务端生成并传回浏览器，用于开发者授权此浏览器运行的JMessage初始化。开发者需确保能调用获取到此数据的皆为合法用户。

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
* timestamp : 当前时间戳，用于防止重放攻击，精确到毫秒
* signature : 签名，10分钟后失效

签名生成算法如下:

```
signature = md5(appkey=appkey&timestamp=timestamp&random_str=random_str&key=secret)
```

其中secret为开发者在极光平台注册的IM应用masterSecret。

## 快速开始

访问极光官网获取最新的 Web SDK。 然后在页面中引入：

```
<script src='./jmessage-sdk-web.min.js'></script>
```
引入该JS后，就可以使用Window上的全局对象JMessage。你可以通过以下方式创建JMessage示例:

```
var JIM = new JMessage();
```
如果你想开启Debug模式，则可以在实例化JMessage的时候传入参数：

```
var JIM = new JMessage({debug:true});
```



## API

API使用Promise风格，无特殊说明所有的API请求都是异步的，并支持以下4种回调处理。

- 请求成功回调 onSuccess()
- 请求失败回调 onFail()
- 请求超时回调 onTimeout()
- 请求应答回调 onAck()

比如你发送一条消息，你可以通过以下方式按需监听你感兴趣的事件回调:

```
JIM.sendSingleMsg({
    'target_username' : 'xiezefan',
    'content' : 'Hi, JiGuang '
}).onSuccess(function(data) {
    // do something
}).onFail(function(data) {
    // do something
}).onTimeout(function(data) {
    if (data.response_timeout) {
        // do something when response timeout
    } else {
        // do something when request timeout
    }
}).onAck(function(data) {
    // do something
});
```


### 初始化

JMessage#init()

**漫游参数**

Since SDK v2.2.0  新增漫游参数，初始化时，可设置是否启用消息记录漫游。
打开消息漫游之后，用户多个设备之间登录时，sdk会自动同步当前登录用户的历史消息。

**请求参数:**

| KEY        | REQUIRE | DESCRIPTION           |
| ---------- | ------- | --------------------- |
| appkey     | TRUE    | 开发者在极光平台注册的IM应用appkey |
| random_str | TRUE    | 随机字符串                 |
| timestamp  | TRUE    | 当初时间戳                 |
| signature  | TRUE    | 签名                    |
| flag       | FALSE   | 是否启用消息记录漫游，默认0否，1是    |

**请求示例**

```
  JIM.init({
               "appkey" : "<appkey>",
           "random_str" : "<random_str>",
            "signature" : "<signature>",
            "timestamp" : "<timestamp>",
            "flag" : "0"
        }).onSuccess(function(data) {
           //data.code 返回码
           //data.message 描述
          }).onFail(function(data) {
            // 同上
        });
```

### 断线监听

JMessage#onDisconnect(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 断线处理函数      |

**请求示例**

```
  JIM.onDisconnect(function(){
  });
```

### 注册与登录

#### 注册

JMessage#register()

**请求参数:**

| KEY      | REQUIRE | DESCRIPTION    |
| -------- | ------- | -------------- |
| username | TRUE    | 用户名            |
| password | TRUE    | 密码             |
| is_md5   | FALSE   | 密码是否是MD5密码，默认否 |

**请求示例**

```
  JIM.register({
            'username' : '<register name>',
			'password' : '<register password>',
			'is_md5' : '<is_md5>'
        }).onSuccess(function(data) {
            //data.code 返回码
            //data.message 描述
          }).onFail(function(data) {
            // 同上
        });
```

#### 登录

JMessage#login()

**请求参数:**

| KEY      | REQUIRE | DESCRIPTION    |
| -------- | ------- | -------------- |
| username | TRUE    | 用户名            |
| password | TRUE    | 密码             |
| is_md5   | FALSE   | 密码是否是MD5密码，默认否 |

**请求示例**

```
JIM.login({
    'username' : '<login username>',
    'password' : '<login password>'
}).onSuccess(function(data) {
     //data.code 返回码
     //data.message 描述
}.onFail(function(data){
  //同上
});
```

#### 登出

JMessage#loginOut()

**请求参数:**

无

**请求示例**

```
JIM.loginOut();//无回调函数，调用则成功
```

### 用户管理

#### 获取用户信息

JMessage#getUserInfo()

**请求参数:**

| KEY      | REQUIRE | DESCRIPTION          |
| -------- | ------- | -------------------- |
| username | TRUE    | 用户名                  |
| appkey   | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
  JIM.getUserInfo({
            'username' : '<search username>',
			'appkey' : '<search appkey>'
        }).onSuccess(function(data) {
            //data.code 返回码
            //data.message 描述
            //data.user_info.username
            //data.user_info.appkey
            //data.user_info.nickname
            //data.user_info.avatar 头像
            //data.user_info.birthday 生日，默认空
            //data.user_info.gender 性别 0 - 未知， 1 - 男 ，2 - 女
            //data.user_info.signature 用户签名
            //data.user_info.region 用户所属地区
            //data.user_info.address 用户地址
            //data.user_info.mtime 用户信息最后修改时间
          }).onFail(function(data) {
            //data.code 返回码
            //data.message 描述
        });
```

#### 更新个人信息

JMessage#updateSelfInfo()

**请求参数:**

| KEY       | REQUIRE | DESCRIPTION   |
| --------- | ------- | ------------- |
| nickname  | FALSE   | 昵称            |
| birthday  | FALSE   | 生日            |
| signature | FALSE   | 签名            |
| gender    | FALSE   | 性别，0未知, 1男，2女 |
| region    | FALSE   | 地区            |
| address   | FALSE   | 地址            |

**请求示例**

```
   JIM.updateSelfInfo({
                'nickname' : '<your_nickname>',
                 'birthday' : '<your_address>',
                'signature' : '<your_address>',
                'gender' : '<your_address>',
                'region' : '<your_address>',
                'address' : '<your_address>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //同上
               });
```

#### 更新个人头像

JMessage#updateSelfAvatar()

**请求参数:**

| KEY    | REQUIRE | DESCRIPTION |
| ------ | ------- | ----------- |
| avatar | FALSE   | 头像图片文件      |

**请求示例**

```
   JIM.updateSelfAvatar({
                'avatar' : '<formData with image>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //同上
               });
```

#### 更新个人密码

JMessage#updateSelfPwd()

**请求参数:**

| KEY     | REQUIRE | DESCRIPTION |
| ------- | ------- | ----------- |
| old_pwd | TRUE    | 旧的密码        |
| new_pwd | TRUE    | 新的密码        |
| is_md5  | FALSE   | 密码是否经过MD5   |

**请求示例**

```
   JIM.updateSelfPwd({
                'old_pwd' : '<oldPwd>',
                 'new_pwd' : '<newPwd>',
                  'is_md5' : '<idMd5>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                  //同上
               });
```


### 消息管理

#### 获取会话列表

JMessage#getConversation()

**请求参数：**

无

**请求示例**

```
   JIM.getConversation().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.conversations[] 会话列表，属性如下示例
                   //data.conversations[0].name  会话名称
                   //data.conversations[0].type  会话类型(3代表单聊会话类型，4代表群聊会话类型)
                   //data.conversations[0].key会话对象唯一标识(单聊用户唯一标识，群聊群组gid)
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 发送单聊文本

JMessage#sendSingleMsg()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| content         | TRUE    | 消息文本                 |
| extras          | FALSE   | 附加字段,字典类型            |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.sendSingleMsg({
                 'target_username' : '<targetName>',
			     'target_nickname' : '<targetNickname>',
                 'content' : '<textContent>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //msg.content 发送成功消息体,见下面消息体详情
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```
**消息体**

[消息体详情](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/): 

#### 发送单聊图片

JMessage#sendSinglePic()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| image           | TRUE    | 图片的DataForm对象        |
| extras          | FALSE   | 附加字段,字典类型            |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.sendSinglePic({
                 'target_username' : '<targetName>',
			     'target_nickname' : '<targetNickname>',
                 'image' : '<formData with image>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //同发送单聊文本
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送单聊文件

JMessage#sendSingleFile()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| file            | TRUE    | 文件的DataForm对象        |
| extras          | FALSE   | 附加字段,字典类型            |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.sendSingleFile({
                 'target_username' : '<targetName>',
			     'target_nickname' : '<targetNickname>',
                 'file' : '<formData with file>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送单聊位置

JMessage#sendSingleLocation()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| latitude        | TRUE    | 维度                   |
| longitude       | TRUE    | 精度                   |
| scale           | TRUE    | 地图缩放级别               |
| label           | TRUE    | 地址                   |
| extras          | FALSE   | 附加字段,字典类型            |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.sendSingleLocation({
                 'target_username' : '<targetName>',
			     'target_nickname' : '<targetNickname>',
			     'latitude' : '<latitude>',
                 'longitude' : '<longitude>',
                 'scale' : '<scale>',
                 'label' : '<address label>'
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送单聊自定义消息

JMessage#sendSingleCustom()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| custom          | TRUE    | 自定义json object消息     |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.sendSingleCustom({
                 'target_username' : '<targetName>',
			     'target_nickname' : '<targetNickname>',
                 'custome' : '<json object>'
                 'appkey' : '<targetAppkey>'
               }).onSuccess(function(data , msg) {
                  //同发送单聊文本
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送群聊文本

JMessage#sendGroupMsg()

**请求参数：**

| KEY          | REQUIRE | DESCRIPTION                              |
| ------------ | ------- | ---------------------------------------- |
| target_gid   | TRUE    | 群组id                                     |
| target_gname | TRUE    | 群组消息name                                 |
| content      | TRUE    | 消息文本                                     |
| extras       | FALSE   | 附加字段,字典类型                                |
| at_list      | FALSE   | @用户列表：[{'username': 'name1', 'appkey': '跨应用必填，默认不填表示本应用'}],@ALL 直接空数组：[] |

**请求示例**

```
   JIM.sendGroupMsg({
                 'target_gid' : '<targetGid>',
			     'target_gname' : '<targetGName>',
                 'content' : '<textContent>',
                 'extras' : '<json object>',
                 'at_list' : [] //at all
               }).onSuccess(function(data , msg) {
                  //同发送单聊文本
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 获取资源访问路径

JMessage#getResource ()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION   |
| -------- | ------- | ------------- |
| media_id | TRUE    | media_id 资源id |

**请求示例**

```
   JIM.getResource({
                 'media_id ' : '<media_id >',
               }).onSuccess(function(data , msg) {
                   //data.code 返回码
                   //data.message 描述
                   //data.url 资源临时访问路径
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 发送群聊图片

JMessage#sendGroupPic()

**请求参数：**

| KEY          | REQUIRE | DESCRIPTION   |
| ------------ | ------- | ------------- |
| target_gid   | TRUE    | 群组id          |
| target_gname | TRUE    | 群组消息name      |
| image        | TRUE    | 图片的DataForm对象 |
| extras       | FALSE   | 附加字段,字典类型     |

**请求示例**

```
   JIM.sendGroupPic({
                 'target_gid' : '<targetGid>',
			     'target_gname' : '<targetGName>',
                 'image' : '<formData with image>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送群聊文件

JMessage#sendGroupFile()

**请求参数：**

| KEY          | REQUIRE | DESCRIPTION   |
| ------------ | ------- | ------------- |
| target_gid   | TRUE    | 群组id          |
| target_gname | TRUE    | 群组消息name      |
| file         | TRUE    | 文件的DataForm对象 |
| extras       | FALSE   | 附加字段,字典类型     |

**请求示例**

```
   JIM.sendGroupFile({
                 'target_gid' : '<targetGid>',
			     'target_gname' : '<targetGName>',
                 'file' : '<formData with file>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送群聊位置

JMessage#sendGroupLocation()

**请求参数：**

| KEY          | REQUIRE | DESCRIPTION |
| ------------ | ------- | ----------- |
| target_gid   | TRUE    | 群组id        |
| target_gname | TRUE    | 群组消息name    |
| latitude     | TRUE    | 维度          |
| longitude    | TRUE    | 精度          |
| scale        | TRUE    | 地图缩放级别      |
| label        | TRUE    | 地址          |
| extras       | FALSE   | 附加字段,字典类型   |

**请求示例**

```
   JIM.sendGroupLocation({
                  'target_gid' : '<targetGid>',
			     'target_gname' : '<targetGName>',
			     'latitude' : '<latitude>',
                 'longitude' : '<longitude>',
                 'scale' : '<scale>',
                 'label' : '<address label>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送群聊自定义消息

JMessage#sendGroupMsg()

**请求参数：**

| KEY          | REQUIRE | DESCRIPTION      |
| ------------ | ------- | ---------------- |
| target_gid   | TRUE    | 群组id             |
| target_gname | TRUE    | 群组消息name         |
| custom       | TRUE    | 自定义json object消息 |

**请求示例**

```
   JIM.sendGroupMsg({
                  'target_gid' : '<targetGid>',
			     'target_gname' : '<targetGName>',
			     'custom' : '<json object>'
               }).onSuccess(function(data , msg) {
                   //同发送单聊文本
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

### 群组管理

#### 创建群组

JMessage#createGroup()

**请求参数：**

| KEY               | REQUIRE | DESCRIPTION |
| ----------------- | ------- | ----------- |
| group_name        | TRUE    | 群组名         |
| group_description | TRUE    | 群组描述        |

**请求示例**

```
   JIM.createGroup({
                 'group_name' : '<groupName>',
			     'group_description' : '<groupDescription>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.gid 群组id
                  //data.group_name 群名
                  //data.group_descriptin 群描述
               }).onFail(function(data) {
                    //data.code 返回码
                    //data.message 描述
               });
```

#### 退出群组

JMessage#exitGroup()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.exitGroup({
                  'gid' : '<exit gid>'
               }).onSuccess(function(data) {
                    //data.code 返回码
                    //data.message 描述
                    //data.gid 群组id
                    //data.group_name 群名
               }).onFail(function(data) {
                    //data.code 返回码
                    //data.message 描述
               });
```

#### 增加群组成员

JMessage#addGroupMembers()

**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| gid              | TRUE    | 群组id                                     |
| member_usernames | TRUE    | 增加用户名列表,示例：[{'username':'name1', 'appkey': '跨应用必填，默认不填表示本应用'},...] |

**请求示例**

```
   JIM.addGroupMembers({
                  'gid' : '<gid>',
          'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                  //同上
               });
```

#### 删除群组成员

JMessage#delGroupMembers()

**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| gid              | TRUE    | 群组id                                     |
| member_usernames | TRUE    | 增加用户名列表,示例：[{'username':'name1', 'appkey': '跨应用必填，默认不填表示本应用'},...] |

**请求示例**

```
   JIM.delGroupMembers({
                  'gid' : '<gid>',
          'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                  // 同上
               });
```

#### 获取群组列表

JMessage#getGroups()


**请求参数：**

无

**请求示例**

```
   JIM.getGroups().onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.group_list[] 群组列表，如下示例
                  //data.group_list[0].gid 群id
                  //data.group_list[0].name 群名
                  //data.group_list[0].desc 群描述
                  //data.group_list[0].appkey 群所属appkey
                  //data.group_list[0].ctime 群创建时间
                  //data.group_list[0].mtime 最近一次群信息修改时间
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```

#### 获取群信息

JMessage#getGroupInfo()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.getGroupInfo({
                  'gid' : '<gid>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.group_info.gid 群id
                  //data.group_info.name 群名
                  //data.group_info.desc 群描述
                  //data.group_info.appkey 群所属appkey
                  //data.group_info.ctime 群创建时间
                  //data.group_info.mtime 最近一次群信息修改时间
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 更新群信息

JMessage#updateGroupInfo()

**请求参数：**

| KEY               | REQUIRE | DESCRIPTION |
| ----------------- | ------- | ----------- |
| gid               | TRUE    | 群id         |
| group_name        | TRUE    | 群组名         |
| group_description | TRUE    | 群组描述        |

**请求示例**

```
   JIM.updateGroupInfo({
                  'gid' : '<gid>',
                  'group_name' : '<new group name>',
                  'group_description' : '<new group description>' 
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 获取群成员

JMessage#getGroupMembers()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群id         |

**请求示例**

```
   JIM.getGroupMembers({
                  'gid' : '<gid>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.member_list[] 成员列表，如下示例
                  //data.member_list[0].username 用户名
                  //data.member_list[0].appkey 用户所属appkey
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

### 免打扰管理

#### 获取免打扰

JMessage#getNoDisturb()

**请求参数：**

无

**请求示例**

```
   JIM.getNoDisturb().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.no_disturb.global 全局免打扰设置：0 关闭 1打开
                   //data.no_disturb.users[] 免打扰用户列表，比如示例
                   //data.no_disturb.users[0].username 用户名
                   //data.no_disturb.users[0].nickname 用户昵称
                   //data.no_disturb.users[0].appkey 用户所属appkey
                   //data.no_disturb.groups[] 免打扰群组列表，比如示例
                   //data.no_disturb.groups[0].gid 群组id
                   //data.no_disturb.groups[0].name 群名字
                   //data.no_disturb.groups[0].appkey 群所属appkey
                   //data.no_disturb.groups[0].desc 群描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 添加用户免打扰

JMessage#addSingleNoDisturb()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION     |
| ----------- | ------- | --------------- |
| target_name | TRUE    | username        |
| appkey      | FALSE   | 跨应用必填，默认不填表示本应用 |

**请求示例**

```
   JIM.addSingleNoDisturb({
          'target_name' : '<targetUserName>',
          'appkey' : '<targetAppkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 关闭用户免打扰

JMessage#delSingleNoDisturb()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION     |
| ----------- | ------- | --------------- |
| target_name | TRUE    | username        |
| appkey      | FALSE   | 跨应用必填，默认不填表示本应用 |

**请求示例**

```
   JIM.delSingleNoDisturb({
          'target_name' : '<targetUserName>',
          'appkey' : '<targetAppkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 添加群组免打扰

JMessage#addGroupNoDisturb()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.addGroupNoDisturb({
                     'gid' : '<targetGid>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 关闭群组免打扰

JMessage#delGroupNoDisturb()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.delGroupNoDisturb({
                     'gid' : '<targetGid>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 添加群屏蔽

JMessage#addGroupShield()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.addGroupShield({
                     'gid' : '<targetGid>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 关闭群屏蔽

JMessage#delGroupShield()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组id        |

**请求示例**

```
   JIM.delGroupShield({
                     'gid' : '<targetGid>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //同上
               });
```

#### 添加全局免打扰

JMessage#addGlobalNoDisturb()

**请求参数：**

无

**请求示例**

```
   JIM.addGlobalNoDisturb().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 关闭全局免打扰

JMessage#delGlobalNoDisturb()

**请求参数：**

无

**请求示例**

```
   JIM.delGlobalNoDisturb().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

### 黑名单管理

#### 获取黑名单

JMessage#getBlacks()

**请求参数：**

无

**请求示例**

```
   JIM.getBlacks().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.black_list[] 黑名单列表，比如示例
                   //data.black_list[0].username
                   //data.black_list[0].appkey
                   //data.black_list[0].nickname
                   //data.black_list[0].avatar 头像
                   //data.black_list[0].birthday 生日，默认空
                   //data.black_list[0].gender 性别 0 未知， 1 男 ，2 女
                   //data.black_list[0].signature 用户签名
                   //data.black_list[0].region 用户所属地区
                   //data.black_list[0].address 用户地址
                   //data.black_list[0].mtime 用户信息最后修改时间
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 添加黑名单

JMessage#addSingleBlacks()

**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| member_usernames | TRUE    | 用户列表示例：[{'username': 'name1', 'appkey': '跨应用必填，默认不填表示本应用'}] |

**请求示例**

```
   JIM.addSingleBlacks({
          'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 删除黑名单

JMessage#delSingleBlacks()

**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| member_usernames | TRUE    | 用户列表示例：[{'username': 'name1', 'appkey': '跨应用必填，默认不填表示本应用'}] |

**请求示例**

```
   JIM.delSingleBlacks({
          'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

### 好友相关

#### 好友列表

JMessage#getFriendList()

**请求参数：**

无

**请求示例**

```
   JIM.getFriendList().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.friend_list[] 好友列表，示例如下
                   //data.friend_list[0].username
                   //data.friend_list[0].appkey
                   //data.friend_list[0].nickname
                   //data.friend_list[0].avatar 头像
                   //data.friend_list[0].memo_nam 好友备注
                   //data.friend_list[0].memo_others 其他备注
                   //data.friend_list[0].birthday 生日，默认空
                   //data.friend_list[0].gender 性别 0 未知， 1 男 ，2 女
                   //data.friend_list[0].signature 用户签名
                   //data.friend_list[0].region 用户所属地区
                   //data.friend_list[0].address 用户地址
                   //data.friend_list[0].mtime 用户信息最后修改时间
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 添加好友&好友请求应答

JMessage#addFriend()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION               |
| ----------- | ------- | ------------------------- |
| target_name | TRUE    | 目标username                |
| from_type   | TRUE    | 1-邀请方，2-被邀请方（应答）          |
| why         | TRUE    | 1:邀请说明;2:空，同意添加好友，非空，拒绝原因 |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的appkey      |

**添加好友请求示例**

```
   JIM.addFriend({
             'target_name' : '< username >' ,
               'from_type' : '1',
                     'why' : '< why >',
                  'appkey' : '<appkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

**应答示例**

```
   JIM.addFriend({
             'target_name' : '< username >' ,
               'from_type' : '2',
                     'why' : '< 空表示同意，非空表示拒绝 >',
                  'appkey' : '<appkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 删除好友

JMessage#delFriend()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION          |
| ----------- | ------- | -------------------- |
| target_name | TRUE    | 目标username           |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.delFriend({
              'target_name' : '< username >' ,
              'appkey' : '< appkey >'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 更新好友备注

JMessage#updateFriendMemo()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION          |
| ----------- | ------- | -------------------- |
| target_name | TRUE    | 目标username           |
| memo_name   | TRUE    | 名称备注                 |
| memo_others | FALSE   | 其他备注                 |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的appkey |

**请求示例**

```
   JIM.updateFriendMemo({
          'target_name' : '< username >' ,
            'memo_name' : '< memo_name >',
          'memo_others' : '< memo_others >',
               'appkey' : '< appkey >'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

### 聊天消息实时监听

JMessage#onMsgReceive(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 消息接收处理函数    |

**返回参数**

| KEY       | DESCRIPTION                              |
| --------- | ---------------------------------------- |
| ctime_ms  | 消息发送时间                                   |
| from_gid  | 群组GID，群聊下有效                              |
| msg_type  | 消息类型   3-single, 4-group                 |
| msg_id    | 消息ID                                     |
| msg_level |                                          |
| content   | [消息体](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/) |

**使用示例**

```
JIM.onMsgReceive(function(data) {
    console.log('receive msg: ' + JSON.stringify(data));
});
```

<<<<<<< HEAD
### 离线消息同步
=======
### 离线消息同步监听
>>>>>>> renew

JMessage#onSyncConversation(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 消息接收处理函数    |

**返回参数**

| KEY      | DESCRIPTION                              |
| -------- | ---------------------------------------- |
| messages | [{'key':'会话标识','msgs':[{'msg_id':'消息id','content':[消息体](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/)}]},...] |



**使用示例**

```
JIM.onSyncConversation(function(data) {
    console.log('receive msg: ' + JSON.stringify(data));
});
```

### 业务事件监听

JMessage#onEventNotification(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**

| KEY           | DESCRIPTION |
| ------------- | ----------- |
| event_id      | 事件id        |
| event_type    | 事件类型        |
| gid           | 关系类型        |
| from_username | 事件发起者       |
| to_usernames  | 事件当事人       |
| ctime         | 事件生成时间      |

**使用示例**

```
JIM.onMsgReceive(function(data) {
    console.log('receive msg: ' + JSON.stringify(data));
});
```
**事件类型对照表**

|                  | 事件接收者                                   | event_type | from_username         | gid     | to_usernames       | return_code                     | extra    |
| ---------------- | --------------------------------------- | ---------- | --------------------- | ------- | ------------------ | ------------------------------- | -------- |
| 账号在其他地方登录，强制踢人事件 | 被踢者                                     | 1          |                       |         | none               |                                 |          |
| 修改密码强制登出事件       | 当前login在线的被踢者                           | 2          |                       | 0       |                    |                                 |          |
| 创建群组业务事件         | 群里所有人接收，即创建者                            | 8          | 创建者                   | groupID | 创建者                |                                 |          |
| 退出群组业务事件         | 群里所有人接收，即除退群者外的其他人，群主退群则群主和群里其他成员均会收到事件 | 9          | 退群者，0表示dev_api删除群组    | groupID | 退群者                |                                 |          |
| 添加群组成员业务事件       | 群里所有人接收，包括被添加的成员和原来的成员                  | 10         | 添加者，0表示dev_api管理员方式添加 | groupId | 被添加的成员             |                                 |          |
| 删除群组成员业务事件       | 群里所有人接收，包括被删除的成员和剩下的成员                  | 11         | 删除者                   | groupID | 被删除的成员             |                                 |          |
| 修改群组信息业务事件       | 群里所有成员                                  | 12         | 修改者                   | groupId | 修改者                |                                 |          |
| 免打扰变更事件          | 变更方                                     | 37         | none                  | 2       | none               |                                 |          |
| 黑名单变更事件          | 变更方                                     | 38         | none                  | 3       | none               |                                 |          |
| 好友邀请事件           | 被邀请方                                    | 5          | 邀请方                   | 1       |                    |                                 | 1，来自邀请方  |
| 好友邀请应答事件         | 邀请方                                     | 5          | 被邀请方                  | 1       | 同意则为空,拒绝则非空，表示拒绝原因 | 好友邀请返回码:0，添加好友成功,其他为添加好友备拒绝的返回码 | 2，来自被邀请方 |
| 删除好友事件           | 被删除好友                                   | 6          | 删除方                   | 1       |                    |                                 |          |
| 好友更新事件           | 好友双方都会                                  | 7          | "",api管理员操作           | 1       |                    |                                 |          |


## 高级应用

### 发送跨应用消息

跨应用是指相同账号下不同appkey之间的用户进行操作，默认在没指定目标appkey的情况下目标appkey就是当前登录用户所使用的appkey，如果需要跨应用操作则在接口参数上指定具体的目标appkey。

以2.1发送单聊为例：

JMessage#sendSingleMsg()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION          |
| --------------- | ------- | -------------------- |
| target_username | TRUE    | 接收消息者username        |
| target_nickname | TRUE    | 接收消息者nickname        |
| content         | TRUE    | 消息文本                 |
| extras          | FALSE   | 附加字段,字典类型            |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的appkey |
其中appkey为目标appkey，其他接口类似

### 发送图片或文件

SDK支持单图片,单文件发送。发送文件和图片接口需要接收一个类型为FormData参数值，该参数值包含了用户需要发送的文件信息。

构造FormData示例：

```
var fd = new FormData();

fd.append(fileName, file);
```

完成构造FormData后 将其作为参数传入对用的接口，以发送单聊图片为例子：

```
sendSinglePic({
            'target_username' : across_user,
			'appkey' : across_appkey,
            'image' : fd //构造好的 FormData
            }).onSuccess(function(data) {
                console.log('success:' + JSON.stringify(data))
            }).onFail(function(data) {
                 console.log('error:' + JSON.stringify(data))
           });
```

其他发送文件,图片接口类似

### 发送和接收Emoij表情

Emoji表情就是一种在Unicode位于`\u1F601`-`\u1F64F`区段的字符。 JMessage的消息内容都是使用[utf8mb4](https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html)编码，向下兼容UTF8。
只要正确输入Emoij字符都可以使用JMessage文本消息API进行发送。如果用户需要转存聊天消息，请先确保数据库支持utf8mb4编码。
开发者可以使用第三方开源的Web Emoij解决方案，如[coocy/emoji](https://github.com/coocy/emoji),[iamcal/js-emoji](https://github.com/iamcal/js-emoji)来在网页上显示Emoij表情。


## 错误码定义

参考文档：[IM Web SDK 错误码列表](./im_errorcode_js)

