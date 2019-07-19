<h1>Web SDK 开发指南 V2</h1>

## 概述

极光 IM Web SDK 为 Web 应用提供一个 IM 系统开发框架, 屏蔽掉 IM 系统的复杂的细节, 对外提供较为简洁的 API 接口, 方便第三方应用快速集成 IM 功能。SDK 支持 IE10及以上版本，Edge、Chrome、 Safari 、Firefox 、UC等主流浏览器

## 版本说明

JMessage Web SDK V2 版本对 SDK 通讯协议进行重新封装与优化:

* 提供更方便的 API 调用方式: 使用 Promise 风格的 API，简化了接口调用方式，开发者可以更简单方便的集成  SDK。
* 更可靠的消息重试方案: 新的 SDK 优化了消息重试技术方案，当弱网络环境下，出现消息发送失败，SDK 会自动重试 5 次，并保证每次 API 调用都是幂等的，开发者无需担心因为消息重试导致重复发送的情况。
* 支持单页面多聊天实例: 新的 SDK 修改了实例化方式，开发者可以不需要在页面初始化的时候就初始化 JMessage。在需要聊天功能的时候再进行初始化即可，并且一个页面可以初始化多个通道，实现多账号登录。

因为 V2  API 全面改造了 API，为了提供更好的用户体验，V2  API 不向下兼容，开发者需要根据 JMessage Web SDK 文档重新接入 SDK。

## 鉴权

开发者在执行初始化的时候，需要传入 auth_payload。 该数据结构由开发者服务端生成并传回浏览器，用于开发者授权此浏览器运行的 JMessage 初始化。开发者需确保能调用获取到此数据的皆为合法用户。

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

* appkey : 开发者在极光平台注册的 IM 应用 appkey
* random_str :  20-36 长度的随机字符串, 作为签名加 salt 使用
* timestamp : 当前时间戳，用于防止重放攻击，精确到毫秒
* signature : 签名，10 分钟后失效（只针对初始化操作，初始化成功则之后的操作跟签名无关）

签名生成算法如下:

```
signature = md5(appkey={appkey}&timestamp={timestamp}&random_str={random_str}&key={secret})
```
其中 secret 为开发者在极光平台注册的 IM 应用 masterSecret。
签名生成示例:
```
signature = md5("appkey=25b693b31d2c2ad5f072ef0c&timestamp=1507791639926&random_str=022cd9fd995849b&key=bc2efab258f2019727a4f36l")
```
***生产环境签名的生成需要在开发者服务端生成，不然存在 masterSecret 暴露的风险**


## 快速开始

访问极光官网获取最新的 Web SDK。 然后在页面中引入：

```
<script src='./jmessage-sdk-web.<version>.min.js'></script>
```
引入该 JS 后，就可以使用 Window 上的全局对象 JMessage。你可以通过以下方式创建 JMessage 示例:

```
var JIM = new JMessage();
```
如果你想开启 Debug 模式，则可以在实例化 JMessage 的时候传入参数：

```
var JIM = new JMessage({debug:true});
```



## API

API 使用 Promise 风格，无特殊说明所有的 API 请求都是异步的，并支持以下 4 种回调处理。

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

***Since 2.2.0***  新增漫游参数，初始化时，可设置是否启用消息记录漫游。
打开消息漫游之后，用户多个设备之间登录时，sdk 会自动同步当前登录用户的历史消息。

**请求参数:**

| KEY        | REQUIRE | DESCRIPTION            |
| ---------- | ------- | ---------------------- |
| appkey     | TRUE    | 开发者在极光平台注册的IM应用 appkey |
| random_str | TRUE    | 随机字符串                  |
| timestamp  | TRUE    | 当初时间戳                  |
| signature  | TRUE    | 签名                     |
| flag       | FALSE   | 是否启用消息记录漫游，默认 0 否，1 是  |

**请求示例**

```
  JIM.init({
               "appkey" : "<appkey>",
           "random_str" : "<random_str>",
            "signature" : "<signature>",
            "timestamp" : "<timestamp>",
            "flag" : 0
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

### 多端同时在线

SDK从2.4.0版本开始支持多端同时在线，具体规则见[多端在线说明](../guideline/faq/#_5)


### 注册登录相关

#### 注册

***Since 2.4.0*** 注册支持其他字段

JMessage#register()

**请求参数:**

| KEY       | REQUIRE | DESCRIPTION      |
| --------- | ------- | ---------------- |
| username  | TRUE    | 用户名              |
| password  | TRUE    | 密码               |
| is_md5    | FALSE   | 密码是否是 MD5 密码，true/false。默认false |
| nickname  | FALSE   | 昵称               |
| birthday  | FALSE   | 生日               |
| signature | FALSE   | 签名               |
| gender    | FALSE   | 性别，0 未知, 1 男，2 女 |
| region    | FALSE   | 地区               |
| address   | FALSE   | 地址               |
| extras    | FALSE   | 自定义 json 格式字段    |
| media_id  | FALSE   | 头像 id            |

**请求示例**

```
  JIM.register({
        'username' : '<register name>',
	    'password' : '<register password>',
	      'is_md5' : <is_md5>,
	      'extras' : {'key1':'val1','key2':'val2'},
	     'address' : '深圳'
        }).onSuccess(function(data) {
            //data.code 返回码
            //data.message 描述
          }).onFail(function(data) {
            // 同上
        });
```

#### 连接状态

JMessage#isConnect()

**请求参数:**

无

**请求示例**

```
JIM.isConnect();// 无回调函数，调用则成功
```

#### 初始化状态

JMessage#isInit()

**请求参数:**

无

**请求示例**

```
JIM.isInit();// 无回调函数，调用则成功
```

#### 登录状态

JMessage#isLogin()

**请求参数:**

无

**请求示例**

```
JIM.isLogin();// 无回调函数，调用则成功
```

#### 登录

***Since 2.6.0*** 支持online_list

JMessage#login()

**请求参数:**

| KEY      | REQUIRE | DESCRIPTION      |
| -------- | ------- | ---------------- |
| username | TRUE    | 用户名              |
| password | TRUE    | 密码               |
| is_md5   | FALSE   | 密码是否是 MD5 密码，true/false。默认false |

**请求示例**

```
JIM.login({
    'username' : '<login username>',
    'password' : '<login password>'
}).onSuccess(function(data) {
     //data.code 返回码
     //data.message 描述
     //data.online_list[] 在线设备列表
     //data.online_list[].platform  Android,ios,pc,web
     //data.online_list[].mtime 最近一次登录时间
     //data.online_list[].isOnline 是否在线 true or false
     //data.online_list[].isLogin 是否登录 true or false
     //data.online_list[].flag 该设备是否被当前登录设备踢出 true or false
}).onFail(function(data){
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

***Since 2.4.0*** 支持 extras 字段

JMessage#getUserInfo()

**请求参数:**

| KEY      | REQUIRE | DESCRIPTION           |
| -------- | ------- | --------------------- |
| username | TRUE    | 用户名                   |
| appkey   | FALSE   | 跨应用查询时必填，目标应用的 appkey |

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
            //data.extras 自定义json字段
          }).onFail(function(data) {
            //data.code 返回码
            //data.message 描述
        });
```

#### 更新个人信息

***Since 2.4.0*** 支持 extras 字段

JMessage#updateSelfInfo()

**请求参数:**

| KEY       | REQUIRE | DESCRIPTION      |
| --------- | ------- | ---------------- |
| nickname  | FALSE   | 昵称               |
| birthday  | FALSE   | 生日               |
| signature | FALSE   | 签名               |
| gender    | FALSE   | 性别，0 未知, 1 男，2 女 |
| region    | FALSE   | 地区               |
| address   | FALSE   | 地址               |
| extras    | FALSE   | 自定义 json 格式字段    |

**请求示例**

```
   JIM.updateSelfInfo({
                 'nickname' : '<your_nickname>',
                 'birthday' : '<your_address>',
                'signature' : '<your_address>',
                   'gender' : '<your_address>',
                   'region' : '<your_address>',
                  'address' : '<your_address>'
                   'extras' : {'key1':'val1','key2':'val2'}
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

| KEY    | REQUIRE | DESCRIPTION         |
| ------ | ------- | ------------------- |
| avatar | TRUE    | 头像头像图片的 DataForm 对象 |

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
| is_md5  | FALSE   | 密码是否经过 MD5，true/false。 默认false  |

**请求示例**

```
   JIM.updateSelfPwd({
                 'old_pwd' : '<oldPwd>',
                 'new_pwd' : '<newPwd>',
                  'is_md5' : <idMd5>
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                  //同上
               });
```


### 消息管理

#### 获取会话列表

***Since 2.4.0*** 支持会话 extras 字段

JMessage#getConversation()

**请求参数：**

无

**请求示例**

```
   JIM.getConversation().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.conversations[] 会话列表，属性如下示例
                   //data.conversations[0].extras 附加字段
                   //data.conversations[0].unread_msg_count 消息未读数
                   //data.conversations[0].name  会话名称
                   //data.conversations[0].appkey  appkey(单聊)
                   //data.conversations[0].username  用户名(单聊)
                   //data.conversations[0].nickname  用户昵称(单聊)
                   //data.conversations[0].avatar  头像 media_id 
                   //data.conversations[0].mtime 会话最后的消息时间戳
                   //data.conversations[0].gid 群 id(群聊)
                   //data.conversations[0].type  会话类型(3 代表单聊会话类型，4 代表群聊会话类型)
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 更新会话信息

***Since 2.4.0***

JMessage#updateConversation()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION           |
| -------- | ------- | --------------------- |
| gid      | FALSE   | 群 id,群聊有效             |
| username | FALSE   | 用户username,单聊有效       |
| appkey   | FALSE   | 用户appkey,单聊有效         |
| extras   | TRUE    | json object, 老的数据会被覆盖 |

**请求示例**

```
   // 群会话,调用则成功，无回调函数
   JIM.updateConversation({
                            'gid' : 'gid',
                            'extras' : {'key':'val','key2':'val2'}
                           });
                           
   // 单聊会话, 调用则成功，无回调函数
   JIM.updateConversation({
                            'appkey' : 'appkey',
                            'username' : 'username',
                            'extras' : {'key':'val','key2':'val2'}
                           });
```

#### 获取会话未读数

***Since 2.4.0***

JMessage#getUnreadMsgCnt()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION       |
| -------- | ------- | ----------------- |
| gid      | FALSE   | 群 id,群聊会话有效       |
| username | FALSE   | 用户username,单聊会话有效 |
| appkey   | FALSE   | 用户appkey,单聊会话有效   |


**请求示例**

```
   // 单聊，未读数，调用则成功，无回调函数
   var count = JIM.getUnreadMsgCnt({
                            'username' : '<username>'
                           });
   // 群聊，未读数，调用则成功，无回调函数
   var count = JIM.getUnreadMsgCnt({
                            'gid' : '<gid>'
                           });
```

#### 重置会话未读数

***Since 2.4.0***

JMessage#resetUnreadCount()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION       |
| -------- | ------- | ----------------- |
| gid      | FALSE   | 群 id,群聊会话有效       |
| username | FALSE   | 用户username,单聊会话有效 |
| appkey   | FALSE   | 用户appkey,单聊会话有效   |


**请求示例**

```
   // 重置单聊会话，调用则成功，无回调函数
   JIM.resetUnreadCount({
                            'username' : '<username>'
                           });
   // 重置群聊会话，调用则成功，无回调函数
   JIM.resetUnreadCount({
                            'gid' : '<gid>'
                           });
```

#### 消息未读用户列表

***Since 2.4.0***

JMessage#msgUnreadList()

**请求参数：**

| KEY    | REQUIRE | DESCRIPTION |
| ------ | ------- | ----------- |
| msg_id | TRUE    | 消息 id       |

**请求示例**

```
   // 消息发送设置了需要回执的时候,可以查看消息的已读未读用户列表
   // 消息接收方收到需要回执的消息的时候,阅读后需要通过消息已读回执接口通知后台消息已读
   JIM.msgUnreadList({
                        'msg_id' : '<msg_id>'
                     }).onSuccess(function(data) {
                        //data.code 返回码
                        //data.message 描述
                        // 未读用户列表
                        //data.msg_unread_list.unread_list[].appkey
                        //data.msg_unread_list.unread_list[].username
                        //data.msg_unread_list.read_list[].nickname
                        // 已读用户列表
                        //data.msg_unread_list.read_list[].appkey
                        //data.msg_unread_list.read_list[].username
                        //data.msg_unread_list.read_list[].nickname
                    }).onFail(function(data) {
                        //data.code 返回码
                        //data.message 描述
                     });
```

#### 单聊消息已读回执

***Since 2.4.0***

JMessage#addSingleReceiptReport()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION          |
| -------- | ------- | -------------------- |
| username | TRUE    | 用户 name              |
| msg_ids  | TRUE    | 已经阅读过的消息的 id 列表,数组类型 |
| appkey   | FALSE   | 默认本应用 appkey         |

**请求示例**

```
   // 接收方收到需要消息回执的消息，阅读后进行消息回执操作
   JIM.addSingleReceiptReport({
                      'username' : '<用户 name>',
                      'msg_ids' : '<[msg_ids]>'
                     }).onSuccess(function(data,msg_ids){
                       // data.code 返回码
                       // data.appkey 目标 appkey
                       // data.username 目标 username
                       // msg_ids 消息数组
                     }).onFail(function(data.msg_ids){
                       
                     })
```

#### 群聊消息已读回执

***Since 2.4.0***

JMessage#addGroupReceiptReport()

**请求参数：**

| KEY     | REQUIRE | DESCRIPTION          |
| ------- | ------- | -------------------- |
| gid     | TRUE    | 群 ID                 |
| msg_ids | TRUE    | 已经阅读过的消息的 id 列表,数组类型 |

**请求示例**

```
   // 接收方收到需要消息回执的消息，阅读后进行消息回执操作
   JIM.addGroupReceiptReport({
                      'gid' : '<gid>',
                      'msg_id' : '<[msg_ids]>'
                     }).onSuccess(function(data,msg_ids){
                       // data.code 返回码
                       // gid 目标 群
                       // msg_ids 消息数组
                     }).onFail(function(data.msg_ids){
                       
                     });
```

#### 获取资源访问路径

JMessage#getResource ()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION    |
| -------- | ------- | -------------- |
| media_id | TRUE    | media_id 资源 id |

**请求示例**

```
   JIM.getResource({
                 'media_id' : '<media_id >',
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.url 资源临时访问路径，具体超时时间expire time会包含在url中
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```


#### 消息撤回

JMessage#msgRetract  ()

**请求参数：**

| KEY    | REQUIRE | DESCRIPTION |
| ------ | ------- | ----------- |
| msg_id | TRUE    | 消息id        |

**请求示例**

```
   JIM.msgRetract({
                 'msg_id' : '<msg_id >',
               }).onSuccess(function(data , msg) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```


#### 发送单聊文本

JMessage#sendSingleMsg()

**请求参数：**

| KEY                 | REQUIRE           | DESCRIPTION                              |
| ------------------- | ----------------- | ---------------------------------------- |
| target_username     | TRUE              | 接收消息者 username                           |
| content             | 与 msg_body  参数二选一 | 消息文本                                     |
| msg_body            | 与 content 参数二选一   | 消息的 msg_body，用来实现消息转发功能                  |
| target_nickname     | FALSE             | 接收者的展示名                                  |
| extras              | FALSE             | 附加字段,字典类型                                |
| appkey              | FALSE             | 跨应用查询时必填，目标应用的 appkey                    |
| no_offline          | FALSE             | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE             | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE             | 通知栏参数，见下表                                |
| need_receipt        | FALSE             | 是否需要已读回执，需要:true 不需要:false               |



**custom_notification：**

| KEY     | REQUIRE | DESCRIPTION           |
| ------- | ------- | --------------------- |
| enabled | TRUE    | 是否启用自定义消息通知栏 默认 FALSE |
| title   | FALSE   | 通知栏标题                 |
| alert   | FALSE   | 通知栏内容                 |

**请求示例**

```
   // 发送消息
   JIM.sendSingleMsg({
                 'target_username' : '<targetName>',
	         'target_nickname' : '<targetNickname>',
                 'content' : '<textContent>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体,见下面消息体详情
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```
```
   // 转发消息
   JIM.sendSingleMsg({
                 'target_username' : '<targetName>',
	         'target_nickname' : '<targetNickname>',
                 'msg_body' : {
                              'text' : '',
                            'extras' : 'json object'
                              }, // 可以直接从已有消息体里面获取msg_body
                 'appkey' : '<targetAppkey>',
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
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

| KEY                 | REQUIRE          | DESCRIPTION                              |
| ------------------- | ---------------- | ---------------------------------------- |
| target_username     | TRUE             | 接收消息者 username                           |
| image               | 与 msg_body 参数二选一 | 图片的 DataForm 对象                          |
| msg_body            | 与 image 参数二选一    | 消息的 msg_body，用来实现消息转发功能                  |
| target_nickname     | FALSE            | 接收者的展示名                                  |
| extras              | FALSE            | 附加字段,字典类型                                |
| appkey              | FALSE            | 跨应用查询时必填，目标应用的 appkey                    |
| no_offline          | FALSE            | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE            | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE            | 通知栏参数，见下表                                |
| need_receipt        | FALSE            | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY     | REQUIRE | DESCRIPTION           |
| ------- | ------- | --------------------- |
| enabled | TRUE    | 是否启用自定义消息通知栏 默认 FALSE |
| title   | FALSE   | 通知栏标题                 |
| alert   | FALSE   | 通知栏内容                 |

**请求示例**

```
 // 发送消息
 JIM.sendSinglePic({
                 'target_username' : '<targetName>',
	         'target_nickname' : '<targetNickname>',
                 'image' : '<formData with image>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendSinglePic({
                 'target_username' : '<targetName>',
	         'target_nickname' : '<targetNickname>',
                 'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                'width':'',
                               'height':'',
                               'format':'',
                                'fsize':'',
                              'extras' : 'json object'
                                }, // 可以直接从已有消息体里面获取msg_body
                 'appkey' : '<targetAppkey>',
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送单聊文件

JMessage#sendSingleFile()

**请求参数：**

| KEY                 | REQUIRE          | DESCRIPTION                              |
| ------------------- | ---------------- | ---------------------------------------- |
| target_username     | TRUE             | 接收消息者 username                           |
| file                | 与 msg_body 参数二选一 | 文件的 DataForm 对象                          |
| msg_body            | 与 file 参数二选一     | 消息的 msg_body，用来实现消息转发                    |
| target_nickname     | FALSE            | 接收者的展示名                                  |
| extras              | FALSE            | 附加字段,字典类型                                |
| appkey              | FALSE            | 跨应用查询时必填，目标应用的 appkey                    |
| no_offline          | FALSE            | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE            | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE            | 通知栏参数，见下表                                |
| need_receipt        | FALSE            | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY     | REQUIRE | DESCRIPTION           |
| ------- | ------- | --------------------- |
| enabled | TRUE    | 是否启用自定义消息通知栏 默认 FALSE |
| title   | FALSE   | 通知栏标题                 |
| alert   | FALSE   | 通知栏内容                 |

**请求示例**

```
  // 发送消息
  JIM.sendSingleFile({
                 'target_username' : '<targetName>',
		 'target_nickname' : '<targetNickname>',
                 'file' : '<formData with file>',
                 'appkey' : '<targetAppkey>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendSingleFile({
                 'target_username' : '<targetName>',
	         'target_nickname' : '<targetNickname>',
                 'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                 'hash':'',
                                'fname':'',
                                'fsize':'',
                              'extras' : 'json object'
                                }, // 可以直接从已有消息体里面获取msg_body
                 'appkey' : '<targetAppkey>',
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送单聊位置

JMessage#sendSingleLocation()

**请求参数：**

| KEY                 | REQUIRE        | DESCRIPTION                              |
| ------------------- | -------------- | ---------------------------------------- |
| target_username     | TRUE           | 接收消息者 username                           |
| latitude            | 与 msg_body 二选一 | 纬度                                       |
| longitude           | 与 msg_body 二选一 | 经度                                       |
| scale               | 与 msg_body 二选一 | 地图缩放级别                                   |
| label               | 与 msg_body 二选一 | 地址                                       |
| msg_body            | 与位置相关参数二选一     | 消息的 msg_body，用来实现消息转发功能                  |
| target_nickname     | FALSE          | 接收者的展示名                                  |
| extras              | FALSE          | 附加字段,字典类型                                |
| appkey              | FALSE          | 跨应用查询时必填，目标应用的 appkey                    |
| no_offline          | FALSE          | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE          | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE          | 通知栏参数，见下表                                |
| need_receipt        | FALSE          | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY     | REQUIRE | DESCRIPTION           |
| ------- | ------- | --------------------- |
| enabled | TRUE    | 是否启用自定义消息通知栏 默认 FALSE |
| title   | FALSE   | 通知栏标题                 |
| alert   | FALSE   | 通知栏内容                 |

**请求示例**

```
  // 发送消息
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
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendSingleLocation({
                 'target_username' : '<targetName>',
		 'target_nickname' : '<targetNickname>',
		        'msg_body' : {
                               'latitude' : '<latitude>',
                              'longitude' : '<longitude>',
                                  'scale' : '<scale>',
                                  'label' : '<address label>',
                                 'extras' : 'json object'
		                      } // 可以直接从已有消息体里面获取msg_body
                 'appkey' : '<targetAppkey>',
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送单聊自定义消息

JMessage#sendSingleCustom()

**请求参数：**

| KEY                 | REQUIRE      | DESCRIPTION                              |
| ------------------- | ------------ | ---------------------------------------- |
| target_username     | TRUE         | 接收消息者 username                           |
| custom              | TRUE         | 自定义 json object 消息                       |
| msg_body            | 与 custom 二选一 | 消息的 msg_body，用来实现消息转发功能                  |
| target_nickname     | FALSE        | 接收者的展示名                                  |
| appkey              | FALSE        | 跨应用查询时必填，目标应用的 appkey                    |
| no_offline          | FALSE        | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE        | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE        | 通知栏参数，见下表                                |
| need_receipt        | FALSE        | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY     | REQUIRE | DESCRIPTION           |
| ------- | ------- | --------------------- |
| enabled | TRUE    | 是否启用自定义消息通知栏 默认 FALSE |
| title   | FALSE   | 通知栏标题                 |
| alert   | FALSE   | 通知栏内容                 |

**请求示例**

```
   // 发送消息
   JIM.sendSingleCustom({
                 'target_username' : '<targetName>',
		 'target_nickname' : '<targetNickname>',
                 'custom' : '<json object>'
                 'appkey' : '<targetAppkey>'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendSingleCustom({
                 'target_username' : '<targetName>',
		 'target_nickname' : '<targetNickname>',
                 'msg_body' : '<json object>', // 可以直接从已有消息体里面获取msg_body
                 'appkey' : '<targetAppkey>'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.appkey 用户所属 appkey
                  //data.target_username 用户名
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送群聊文本

JMessage#sendGroupMsg()

**请求参数：**

| KEY                 | REQUIRE          | DESCRIPTION                              |
| ------------------- | ---------------- | ---------------------------------------- |
| target_gid          | TRUE             | 群组 id                                    |
| content             | 与 msg_body 参数二选一 | 消息文本                                     |
| msg_body            | 与 content 参数二选一  | 消息的 msg_body，用来实现消息转发                    |
| target_gname        | FALSE            | 接收者的展示名                                  |
| extras              | FALSE            | 附加字段,字典类型                                |
| at_list             | FALSE            | @用户列表：[{'username': 'name1', 'appkey': '跨应用必填，默认不填表示本应用'}],@ALL  直接空数组：[] |
| no_offline          | FALSE            | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification     | FALSE            | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| custom_notification | FALSE            | 通知栏参数，见下表                                |
| need_receipt        | FALSE            | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY       | REQUIRE | DESCRIPTION          |
| --------- | ------- | -------------------- |
| enabled   | TRUE    | 是否启用自定义消息通知栏 默认FALSE |
| title     | FALSE   | 通知栏标题                |
| alert     | FALSE   | 通知栏内容                |
| at_prefix | FALSE   | 被@目标的通知内容前缀          |

**请求示例**

```
   // 发送消息
   JIM.sendGroupMsg({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
                 'content' : '<textContent>',
                 'extras' : '<json object>',
                 'at_list' : [] //at all
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
   // 转发消息
   JIM.sendGroupMsg({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
                 'msg_body' : {
                              'text' : '',
                            'extras' : ''
                               }, // 可以直接从已有消息体里面获取msg_body
                 'at_list' : [] //at all
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```


#### 发送群聊图片

JMessage#sendGroupPic()

**请求参数：**

| KEY             | REQUIRE          | DESCRIPTION                              |
| --------------- | ---------------- | ---------------------------------------- |
| target_gid      | TRUE             | 群组 id                                    |
| image           | 与 msg_body 参数二选一 | 图片的 DataForm 对象                          |
| msg_body        | 与 image 参数二选一    | 消息的 msg_body，用来实现消息转发                    |
| target_gname    | FALSE            | 接收者的展示名                                  |
| extras          | FALSE            | 附加字段,字典类型                                |
| no_offline      | FALSE            | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification | FALSE            | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| need_receipt    | FALSE            | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY       | REQUIRE | DESCRIPTION          |
| --------- | ------- | -------------------- |
| enabled   | TRUE    | 是否启用自定义消息通知栏 默认FALSE |
| title     | FALSE   | 通知栏标题                |
| alert     | FALSE   | 通知栏内容                |
| at_prefix | FALSE   | 被@目标的通知内容前缀          |

**请求示例**

```
   // 发送消息
   JIM.sendGroupPic({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
                 'image' : '<formData with image>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendGroupPic({
                 'target_gid' : '<targetGid>',
	       'target_gname' : '<targetGName>',
                  'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                'width':'',
                               'height':'',
                               'format':'',
                                'fsize':'',
                              'extras' : 'json object'
                                }, // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 发送群聊文件

JMessage#sendGroupFile()

**请求参数：**

| KEY             | REQUIRE          | DESCRIPTION                              |
| --------------- | ---------------- | ---------------------------------------- |
| target_gid      | TRUE             | 群组 id                                    |
| file            | 与 msg_body 参数二选一 | 文件的 DataForm 对象                          |
| msg_body        | 与 file 参数二选一     | 消息的 msg_body，用来实现消息转发                    |
| target_gname    | FALSE            | 接收者的展示名                                  |
| extras          | FALSE            | 附加字段,字典类型                                |
| no_offline      | FALSE            | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification | FALSE            | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| need_receipt    | FALSE            | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY       | REQUIRE | DESCRIPTION          |
| --------- | ------- | -------------------- |
| enabled   | TRUE    | 是否启用自定义消息通知栏 默认FALSE |
| title     | FALSE   | 通知栏标题                |
| alert     | FALSE   | 通知栏内容                |
| at_prefix | FALSE   | 被@目标的通知内容前缀          |

**请求示例**

```
   // 发送消息
   JIM.sendGroupFile({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
                 'file' : '<formData with file>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
   // 转发消息
   JIM.sendGroupFile({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
                 'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                 'hash':'',
                                'fname':'',
                                'fsize':'',
                                'extras' : 'json object'
                                } // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送群聊位置

JMessage#sendGroupLocation()

**请求参数：**

| KEY             | REQUIRE        | DESCRIPTION                              |
| --------------- | -------------- | ---------------------------------------- |
| target_gid      | TRUE           | 群组 id                                    |
| latitude        | 与 msg_body 二选一 | 纬度                                       |
| longitude       | 与 msg_body 二选一 | 经度                                       |
| scale           | 与 msg_body 二选一 | 地图缩放级别                                   |
| label           | 与 msg_body 二选一 | 地址                                       |
| msg_body        | 与位置相关参数二选一     | 消息的 msg_body，用来实现消息转发                    |
| target_gname    | FALSE          | 接收者的展示名                                  |
| extras          | FALSE          | 附加字段,字典类型                                |
| no_offline      | FALSE          | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification | FALSE          | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| need_receipt    | FALSE          | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY       | REQUIRE | DESCRIPTION          |
| --------- | ------- | -------------------- |
| enabled   | TRUE    | 是否启用自定义消息通知栏 默认FALSE |
| title     | FALSE   | 通知栏标题                |
| alert     | FALSE   | 通知栏内容                |
| at_prefix | FALSE   | 被@目标的通知内容前缀          |

**请求示例**

```
   // 发送消息
   JIM.sendGroupLocation({
                 'target_gid' : '<targetGid>',
		 'target_gname' : '<targetGName>',
		 'latitude' : '<latitude>',
                 'longitude' : '<longitude>',
                 'scale' : '<scale>',
                 'label' : '<address label>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
   // 转发消息
   JIM.sendGroupLocation({
                 'target_gid' : '<targetGid>',
               'target_gname' : '<targetGName>',
		   'msg_body' : {
                              'latitude' : '<latitude>',
                             'longitude' : '<longitude>',
                                 'scale' : '<scale>',
                                 'label' : '<address label>',
                                 'extras' : 'json object'
		                      } // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 发送群聊自定义消息

JMessage#sendGroupCustom()

**请求参数：**

| KEY             | REQUIRE      | DESCRIPTION                              |
| --------------- | ------------ | ---------------------------------------- |
| target_gid      | TRUE         | 群组 id                                    |
| custom          | TRUE         | 自定义 json object 消息                       |
| msg_body        | 与 custom 二选一 | 消息的 msg_body，用来实现消息转发                    |
| target_gname    | FALSE        | 接收者的展示名                                  |
| no_offline      | FALSE        | 消息离线控制标志，false，默认值，保存离线消息；true，不保存离线消息   |
| no_notification | FALSE        | 状态栏显示消息标志，false，默认值，状态栏显示消息；true，状态栏不显示消息 |
| need_receipt    | FALSE        | 是否需要已读回执，需要:true 不需要:false               |

**custom_notification：**

| KEY       | REQUIRE | DESCRIPTION          |
| --------- | ------- | -------------------- |
| enabled   | TRUE    | 是否启用自定义消息通知栏 默认FALSE |
| title     | FALSE   | 通知栏标题                |
| alert     | FALSE   | 通知栏内容                |
| at_prefix | FALSE   | 被@目标的通知内容前缀          |

**请求示例**

```
   // 发送消息
   JIM.sendGroupCustom({
                  'target_gid' : '<targetGid>',
		'target_gname' : '<targetGName>',
		      'custom' : '<json object>'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
   // 转发消息
   JIM.sendGroupCustom({
                  'target_gid' : '<targetGid>',
		'target_gname' : '<targetGName>',
		    'msg_body' : '<json object>'// 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.msg_id 发送成功后的消息id
                  //data.ctime_ms 消息生成时间,毫秒
                  //data.target_gid 群 id
                  //data.unread_count 消息需要已读回执的时候,默认未读数
                  //msg.content 发送成功消息体
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
#### 单聊消息透传
***Since 2.4.0***

JMessage#transSingleMsg()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION    |
| --------------- | ------- | -------------- |
| target_username | TRUE    | 目标用户           |
| cmd             | TRUE    | 透传信息 string 类型 |
| target_appkey   | FALSE   | 目标用户所属 appkey  |

**请求示例**

```
   JIM.transSingleMsg({
                 'target_username' : '<username>',
                             'cmd' : '<cmd>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                    //data.code 返回码
                    //data.message 描述
               });
```

#### 群聊消息透传
***Since 2.4.0***

JMessage#transGroupMsg()

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION    |
| ---- | ------- | -------------- |
| gid  | TRUE    | 目标群 id         |
| cmd  | TRUE    | 透传信息 string 类型 |

**请求示例**

```
   JIM.transGroupMsg({
                 'gid' : '<gid>',
                 'cmd' : '<cmd>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                    //data.code 返回码
                    //data.message 描述
               });
```

#### 多端在线消息透传
***Since 2.6.0***

JMessage#transPlatMsg()

**请求参数：**

| KEY      | REQUIRE | DESCRIPTION    |
| -------- | ------- | -------------- |
| platform | TRUE    | 多端在线目标平台：[all,android,ios,pc] |
| cmd      | TRUE    | 透传信息 string 类型 |

**请求示例**

```
   JIM.transPlatMsg({
                 'platform' : 'android',
                 'cmd' : '<cmd>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                    //data.code 返回码
                    //data.message 描述
               });
```

### 群组管理

#### 创建群组

***Since 2.4.0*** 支持群头像

***Since 2.5.0*** 支持公开群

JMessage#createGroup()

**请求参数：**

| KEY               | REQUIRE | DESCRIPTION        |
| ----------------- | ------- | ------------------ |
| group_name        | TRUE    | 群组名                |
| group_description | FALSE   | 群组描述               |
| avatar            | FALSE   | 群头像图片的 DataForm 对象 |
| is_limit          | FALSE   | 是否是公开群,默认 false    |

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

***Since 2.5.0*** 支持 flag 标记


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
                  //data.group_list[0].avatar 群头像
                  //data.group_list[0].group_type 公开群:2,私有群:0或者1
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```

#### 获取群信息

JMessage#getGroupInfo()

***Since 2.5.0*** 支持公开群

**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群组 id       |

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
                  //data.group_list[0].avatar 群头像
                  //data.group_list[0].group_type 公开群:2,私有群:0或者1
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 更新群信息

***Since 2.4.0*** 支持群头像

JMessage#updateGroupInfo()

**请求参数：**

| KEY               | REQUIRE | DESCRIPTION                 |
| ----------------- | ------- | --------------------------- |
| gid               | TRUE    | 群 id                        |
| group_name        | FALSE   | 群组名,最少一个属性必填,非空             |
| group_description | FALSE   | 群组描述,最少一个属性必填,非空            |
| avatar            | FALSE   | 群头像图片的 DataForm 对象,最少一个属性必填 |

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
                  //data.member_list[0].appkey 用户所属 appkey
                  //data.member_list[0].nickname 用户昵称
                  //data.member_list[0].avatar 用户头像 id
                  //data.member_list[0].flag  0：普通成员 1：群主 2：管理员
                  //data.member_list[0].keep_silence 是否被禁言true|false
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 主动加群（公开群）

***Since 2.5.0*** 

JMessage#joinGroup()

**请求参数：**

| KEY    | REQUIRE | DESCRIPTION |
| ------ | ------- | ----------- |
| gid    | TRUE    | 群id         |
| reason | FALSE   | 申请理由        |

**请求示例**

```
JIM.joinGroup({
                  'gid' : '<gid>',
                  'reason' : '<reason>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 审批入群请求

***Since 2.5.0*** 

JMessage#addGroupMemberResp()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION                |
| --------------- | ------- | -------------------------- |
| gid             | TRUE    | 群id                        |
| event_id        | TRUE    | 入群申请事件的 id                 |
| from_username   | TRUE    | 邀请方 username               |
| target_username | TRUE    | 被邀请方 username              |
| result          | TRUE    | 审批结果，0:同意 1:拒绝             |
| reason          | FALSE   | 拒绝原因                       |
| from_appkey     | FALSE   | 邀请方所属 appkey,默认本应用 appkey  |
| target_appkey   | FALSE   | 被邀请方所属 appkey,默认本应用 appkey |


**请求示例**

```

JIM.addGroupMemberResp({
                  'gid' : '<gid>',
                  'event_id' : '<event_id>'
                  'target_appkey' : '<target_appkey>',
                  'target_username' : '<target_username>',
                  'result' : 2,
                  'from_appkey' : '<from_appkey>',
                  'from_username' : '<from_username>'
                  'resaon' : '<reason>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 添加群用户禁言

***Since 2.5.0*** 

JMessage#addGroupMemSilence()


**请求参数：**

| KEY             | REQUIRE | DESCRIPTION |
| --------------- | ------- | ----------- |
| gid             | TRUE    | 群id         |
| target_username | TRUE    | 目标 username |
| target_appkey   | FALSE   | 目标 appkey   |


**请求示例**

```

JIM.addGroupMemSilence({
                  'gid' : '<gid>',
                  'target_appkey' : '<target_appkey>',
                  'target_username' : '<target_username>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 取消群用户禁言

***Since 2.5.0*** 

JMessage#delGroupMemSilence()


**请求参数：**

| KEY             | REQUIRE | DESCRIPTION |
| --------------- | ------- | ----------- |
| gid             | TRUE    | 群id         |
| target_username | TRUE    | 目标 username |
| target_appkey   | FALSE   | 目标 appkey   |


**请求示例**

```

JIM.delGroupMemSilence({
                  'gid' : '<gid>',
                  'target_appkey' : '<target_appkey>',
                  'target_username' : '<target_username>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 添加管理员

***Since 2.6.0*** 

JMessage#addGroupKeeper()


**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| gid              | TRUE    | 群id                                      |
| member_usernames | TRUE    | 增加管理员列表,示例：[{'username':'name1', 'appkey': '跨应用必填，默认不填表示本应用'},...] |



**请求示例**

```

JIM.addGroupKeeper({
                  'gid' : '<gid>',
                   'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 删除管理员

***Since 2.6.0*** 

JMessage#delGroupKeeper()


**请求参数：**

| KEY              | REQUIRE | DESCRIPTION                              |
| ---------------- | ------- | ---------------------------------------- |
| gid              | TRUE    | 群id                                      |
| member_usernames | TRUE    | 增加管理员列表,示例：[{'username':'name1', 'appkey': '跨应用必填，默认不填表示本应用'},...] |



**请求示例**

```

JIM.delGroupKeeper({
                  'gid' : '<gid>',
                   'member_usernames' : [{'username':'name1'},{'username':'name2','appkey':'appkey2'}...]
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 移交群主权限

***Since 2.6.0*** 

JMessage#changeGroupAdmin()


**请求参数：**

| KEY             | REQUIRE | DESCRIPTION            |
| --------------- | ------- | ---------------------- |
| gid             | TRUE    | 群id                    |
| target_username | TRUE    | 目标用户名                  |
| target_appkey   | FALSE   | 跨应用 appkey,默认本应用appkey |



**请求示例**

```

JIM.changeGroupAdmin({
                  'gid' : '<gid>',
                   'target_username' : '<username>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 解散群

***Since 2.6.0*** 

JMessage#dissolveGroup()


**请求参数：**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| gid  | TRUE    | 群id         |

**请求示例**

```

JIM.dissolveGroup({
                  'gid' : '<gid>'
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 获取公开群

***Since 2.6.0*** 

JMessage#getAppkeyPublicGroups()


**请求参数：**

| KEY    | REQUIRE | DESCRIPTION      |
| ------ | ------- | ---------------- |
| start  | TRUE    | 分页下标,首页获取为0      |
| appkey | FALSE   | 群所属 appkey,默认本应用 |

**请求示例**

```

JIM.getAppkeyPublicGroups({
                   'start' : 0
               }).onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.result.total 群总数量
                  //data.result.start 本次查询 index 下标值
                  //data.result.groups[] 群列表
                  //data.result.groups[0].gid 群id
                  //data.result.groups[0].name 群名
                  //data.result.groups[0].desc 群描述
                  //data.result.groups[0].appkey 群所属appkey
                  //data.result.groups[0].ctime 群创建时间
                  //data.result.groups[0].mtime 最近一次群信息修改时间
                  //data.result.groups[0].avatar 群头像
                  //data.result.groups[0].group_type 公开群:2,私有群:0或者1
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```


### 聊天室

***Since 2.5.0*** 加入聊天室相关功能

#### 获取appkey下聊天室分页列表

JMessage#getAppkeyChatrooms()

**请求参数：**


| KEY    | REQUIRE | DESCRIPTION        |
| ------ | ------- | ------------------ |
| start  | TRUE    | 分页下标,首页获取为0        |
| appkey | FALSE   | 聊天室所属 appkey,默认本应用 |


**请求示例**

```
   JIM.getAppkeyChatrooms({
                   'start' : 0
                 }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.result.total 聊天室总数量
                   //data.result.start 本次查询 index 下标值
                   //data.result.count 本次查询返回列表大小
                   //data.result.rooms[].id 聊天室 id
                   //data.result.rooms[].name 聊天室名字
                   //data.result.rooms[].description 聊天室描述
                   //data.result.rooms[].appkey 聊天室所属 appkey
                   //data.result.rooms[].total_member_count 当前聊天室人数
                   //data.result.rooms[].max_member_count 聊天室最大容量
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 获取已加入的聊天室

JMessage#getSelfChatrooms()

**请求参数：**

无

**请求示例**

```
   JIM.getSelfChatrooms().onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.chat_rooms[].id 聊天室 id
                   //data.chat_rooms[].name 聊天室名字
                   //data.chat_rooms[].description 聊天室描述
                   //data.chat_rooms[].appkey 聊天室所属 appkey
                   //data.chat_rooms[].total_member_count 当前聊天室人数
                   //data.chat_rooms[].max_member_count 聊天室最大容量
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 获取聊天室详情

JMessage#getChatroomInfo()

**请求参数：**


| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| id   | TRUE    | 聊天室 id      |


**请求示例**

```
   JIM.getChatroomInfo({
                   'id' : '<id>'
                 }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.info.id 聊天室 id
                   //data.info.name 聊天室名字
                   //data.info.description 聊天室描述
                   //data.info.appkey 聊天室所属 appkey
                   //data.info.total_member_count 当前聊天室人数
                   //data.info.max_member_count 聊天室最大容量
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 进入聊天室

JMessage#enterChatroom ()

**请求参数：**


| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| id   | TRUE    | 聊天室id       |


**请求示例**

```
   JIM.enterChatroom({
                   'id' : '<id>'
                 }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.id 聊天室 id
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 退出聊天室

JMessage#exitChatroom ()

**请求参数：**


| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| id   | TRUE    | 聊天室id       |


**请求示例**

```
   JIM.exitChatroom({
                   'id' : '<id>'
                 }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
                   //data.id 聊天室 id
               }).onFail(function(data) {
                   //data.code 返回码
                   //data.message 描述
               });
```

#### 聊天室发送文本消息

JMessage#sendChatroomMsg()

**请求参数：**

| KEY          | REQUIRE           | DESCRIPTION             |
| ------------ | ----------------- | ----------------------- |
| target_rid   | TRUE              | 目标 id                   |
| content      | 与 msg_body  参数二选一 | 消息文本                    |
| msg_body     | 与 content 参数二选一   | 消息的 msg_body，用来实现消息转发功能 |
| target_rname | FALSE             | 接收者的展示名                 |
| extras       | FALSE             | 附加字段,字典类型               |

**请求示例**

```
   // 发送文本消息
   JIM.sendChatroomMsg({
                 'target_rid' : '<targetRid>',
                 'content' : '<textContent>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```
```
   // 转发文本消息
   JIM.sendChatroomMsg({
                 'target_rid' : '<targetRid>',
                 'msg_body' : {
                              'text' : '',
                            'extras' : 'json object'
                              }, // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //data.code 返回码
                  //data.message 描述
               });
```
**消息体**

[消息体详情](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/): 

#### 聊天室发送图片消息

JMessage#sendChatroomPic()

**请求参数：**

| KEY          | REQUIRE          | DESCRIPTION             |
| ------------ | ---------------- | ----------------------- |
| target_rid   | TRUE             | 目标 id                   |
| image        | 与 msg_body 参数二选一 | 图片的 DataForm 对象         |
| msg_body     | 与 image 参数二选一    | 消息的 msg_body，用来实现消息转发功能 |
| target_rname | FALSE            | 接收者的展示名                 |
| extras       | FALSE            | 附加字段,字典类型               |


**请求示例**

```
 // 发送消息
 JIM.sendChatroomPic({
            'target_rid' : '<targetRid>',
                 'image' : '<formData with image>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendChatroomPic({
               'target_rid' : '<targetRid>',
                 'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                'width':'',
                               'height':'',
                               'format':'',
                                'fsize':'',
                              'extras' : 'json object'
                                } // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 聊天室发送文件消息

JMessage#sendChatroomFile()

**请求参数：**

| KEY          | REQUIRE          | DESCRIPTION           |
| ------------ | ---------------- | --------------------- |
| target_rid   | TRUE             | 目标 id                 |
| file         | 与 msg_body 参数二选一 | 文件的 DataForm 对象       |
| msg_body     | 与 file 参数二选一     | 消息的 msg_body，用来实现消息转发 |
| target_rname | FALSE            | 接收者的展示名               |
| extras       | FALSE            | 附加字段,字典类型             |


**请求示例**

```
  // 发送消息
  JIM.sendChatroomFile({
                 'target_rid' : '<targetRid>',
                 'file' : '<formData with file>',
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendChatroomFile({
                 'target_rid' : '<targetRid>',
                 'msg_body' : {
                             'media_id':'',
                          'media_crc32':'',
                                 'hash':'',
                                'fname':'',
                                'fsize':'',
                              'extras' : 'json object'
                                } // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg<可选>) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```

#### 聊天室发送位置消息

JMessage#sendChatroomLocation()

**请求参数：**

| KEY          | REQUIRE        | DESCRIPTION             |
| ------------ | -------------- | ----------------------- |
| target_rid   | TRUE           | 接收消息者 username          |
| latitude     | 与 msg_body 二选一 | 纬度                      |
| longitude    | 与 msg_body 二选一 | 经度                      |
| scale        | 与 msg_body 二选一 | 地图缩放级别                  |
| label        | 与 msg_body 二选一 | 地址                      |
| msg_body     | 与位置相关参数二选一     | 消息的 msg_body，用来实现消息转发功能 |
| target_rname | FALSE          | 接收者的展示名                 |
| extras       | FALSE          | 附加字段,字典类型               |


**请求示例**

```
  // 发送消息
  JIM.sendChatroomLocation({
                'target_rid' : '<targetRid>',
		          'latitude' : '<latitude>',
                 'longitude' : '<longitude>',
                 'scale' : '<scale>',
                 'label' : '<address label>'
                 'extras' : 'json object'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendChatroomLocation({
              'target_rid' : '<targetRid>',
		        'msg_body' : {
                               'latitude' : '<latitude>',
                              'longitude' : '<longitude>',
                                  'scale' : '<scale>',
                                  'label' : '<address label>',
                                 'extras' : 'json object'
		                      } // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                   //同发送单聊文本
               });
```

#### 聊天室发送自定义消息

JMessage#sendChatroomCustom()

**请求参数：**

| KEY          | REQUIRE      | DESCRIPTION             |
| ------------ | ------------ | ----------------------- |
| target_rid   | TRUE         | 接收消息者 username          |
| custom       | TRUE         | 自定义 json object 消息      |
| msg_body     | 与 custom 二选一 | 消息的 msg_body，用来实现消息转发功能 |
| target_rname | FALSE        | 接收者的展示名                 |
| extras       | FALSE        | 附加字段,字典类型               |

**请求示例**

```
   // 发送消息
   JIM.sendChatroomCustom({
              'target_rid' : '<targetRid>',
                 'custom' : '<json object>'
                 'appkey' : '<targetAppkey>'
               }).onSuccess(function(data , msg) {
                  //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //同发送单聊文本
               });
```
```
  // 转发消息
  JIM.sendChatroomCustom({
           'target_rid' : '<targetRid>',
           'msg_body' : '<json object>' // 可以直接从已有消息体里面获取msg_body
               }).onSuccess(function(data , msg) {
                 //data.code 返回码
                  //data.message 描述
                  //data.room_id 目标聊天室 id
                  //data.msg_id 发送成功后的消息 id
                  //data.ctime_ms 消息生成时间,毫秒
               }).onFail(function(data) {
                  //同发送单聊文本
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
                   //data.no_disturb.global 全局免打扰设置：0 关闭 1 打开
                   //data.no_disturb.users[] 免打扰用户列表，比如示例
                   //data.no_disturb.users[0].username 用户名
                   //data.no_disturb.users[0].nickname 用户昵称
                   //data.no_disturb.users[0].appkey 用户所属 appkey                 
                   //data.no_disturb.groups[0].gid 群id
                   //data.no_disturb.groups[0].name 群名
                   //data.no_disturb.groups[0].desc 群描述
                   //data.no_disturb.groups[0].appkey 群所属appkey
                   //data.no_disturb.groups[0].ctime 群创建时间
                   //data.no_disturb.groups[0].mtime 最近一次群信息修改时间
                   //data.no_disturb.groups[0].avatar 群头像
                   //data.no_disturb.groups[0].group_type 公开群:2,私有群:0或者1
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

#### 群屏蔽列表

JMessage#groupShieldList()

**请求参数：**

无

**请求示例**

```
   JIM.groupShieldList().onSuccess(function(data) {
                  //data.code 返回码
                  //data.message 描述
                  //data.group_list[] 群组列表，如下示例
                  //data.group_list[0].gid 群id
                  //data.group_list[0].name 群名
                  //data.group_list[0].desc 群描述
                  //data.group_list[0].appkey 群所属appkey
                  //data.group_list[0].ctime 群创建时间
                  //data.group_list[0].mtime 最近一次群信息修改时间
                  //data.group_list[0].avatar 群头像
                  //data.group_list[0].group_type 公开群:2,私有群:0或者1 
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

#### 添加好友

JMessage#addFriend()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION           |
| ----------- | ------- | --------------------- |
| target_name | TRUE    | 目标 username           |
| why         | TRUE    | 邀请说明                  |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的 appkey |

**添加好友请求示例**

```
   JIM.addFriend({
             'target_name' : '< username >' ,
                     'why' : '< why >',
                  'appkey' : '<appkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 同意好友请求

***Since 2.4.0***

JMessage#acceptFriend()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION           |
| ----------- | ------- | --------------------- |
| target_name | TRUE    | 目标 username           |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的 appkey |

**添加好友请求示例**

```
   JIM.acceptFriend({
             'target_name' : '< username >' ,
                  'appkey' : '<appkey>'
               }).onSuccess(function(data) {
                   //data.code 返回码
                   //data.message 描述
               }).onFail(function(data) {
                   // 同上
               });
```

#### 拒绝好友请求

***Since 2.4.0***

JMessage#declineFriend()

**请求参数：**

| KEY         | REQUIRE | DESCRIPTION           |
| ----------- | ------- | --------------------- |
| target_name | TRUE    | 目标 username           |
| why         | FALSE   | 拒绝理由                  |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的 appkey |

**添加好友请求示例**

```
   JIM.declineFriend({
             'target_name' : '< username >' ,
                     'why' : '< why >',
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

| KEY         | REQUIRE | DESCRIPTION           |
| ----------- | ------- | --------------------- |
| target_name | TRUE    | 目标 username           |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的 appkey |

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

| KEY         | REQUIRE | DESCRIPTION           |
| ----------- | ------- | --------------------- |
| target_name | TRUE    | 目标 username           |
| memo_name   | TRUE    | 名称备注                  |
| memo_others | FALSE   | 其他备注                  |
| appkey      | FALSE   | 跨应用查询时必填，目标应用的 appkey |

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

**返回消息数组**

| KEY                           | DESCRIPTION                              |
| ----------------------------- | ---------------------------------------- |
| ctime_ms                      | 消息生成时间,毫秒                                |
| msg_type                      | 消息类型   3-single, 4-group                 |
| from_appkey                   | 消息来源 appkey 单聊有效                         |
| from_username                 | 消息来源 username 单聊有效                       |
| from_gid                      | 消息来源群id 群聊有效                             |
| msg_id                        | 消息 ID                                    |
| need_receipt                  | 是否需要回执                                   |
| custom_notification.enabled   | 是否启用自定义消息通知栏                             |
| custom_notification.title     | 通知栏标题                                    |
| custom_notification.alert     | 通知栏内容                                    |
| custom_notification.at_prefix | 被@目标的通知内容前缀                              |
| content                       | [消息体](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/) |

**使用示例**

```
JIM.onMsgReceive(function(data) {
   // data.messages[]
   // data.messages[].ctime_ms
   // data.messages[].msg_type 会话类型
   // data.messages[].msg_id
   // data.messages[].from_appey 单聊有效
   // data.messages[].from_username 单聊有效
   // data.messages[].from_gid 群聊有效
   // data.messages[].need_receipt
   // data.messages[].content
   // data.messages[].custom_notification.enabled
   // data.messages[].custom_notification.title
   // data.messages[].custom_notification.alert
   // data.messages[].custom_notification.at_prefix
});
```

### 离线消息同步监听

JMessage#onSyncConversation(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 消息接收处理函数    |

**返回参数**

| KEY      | DESCRIPTION                              |
| -------- | ---------------------------------------- |
| messages | [{'msg_type':'会话类型','from_appkey':'目标所属appkey','from_username':'目标username','from_gid':'目标群id','unread_msg_count':'消息未读数','receipt_msgs':[{'msg_id':'消息 id','unread_count':'未读数','mtime':'更新时时间,毫秒'},...],'msgs':[{参考聊天消息实时监听},...]},...] |

**使用示例**

```
JIM.onSyncConversation(function(data) {
   // data[]
   // data[].msg_type 会话类型
   // data[].from_appey 单聊有效
   // data[].from_username 单聊有效
   // data[].from_gid 群聊有效
   // data[].unread_msg_count 消息未读数
   // 消息已读回执状态，针对自己发的消息
   // data[].receipt_msgs[]
   // data[].receipt_msgs[].msg_id
   // data[].receipt_msgs[].unread_count
   // data[].receipt_msgs[].mtime
   // 消息列表
   // data[].msgs[]
   // data[].msgs[].msg_id
   // data[].msgs[].content
   // data[].msgs[].msg_type
   // data[].msgs[].ctime_ms
   // data[].msgs[].need_receipt
   // data[].msgs[].custom_notification.enabled
   // data[].msgs[].custom_notification.title
   // data[].msgs[].custom_notification.alert
   // data[].msgs[].custom_notification.at_prefix
});
```

### 用户信息变更监听

JMessage#onUserInfUpdate(fn)

**监听对象**

监听对象包括好友、群组成员、会话列表中的单聊

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 处理函数        |

**返回参数**

| KEY      | DESCRIPTION |
| -------- | ----------- |
| appkey   | 变更方的appkey  |
| username | 变更方username |
| mtime    | 变更时间（秒）     |

**使用示例**

```
JIM.onUserInfUpdate(function(data) {
    console.log('user info update event: ' + JSON.stringify(data));
});
```

### 业务事件监听

JMessage#onEventNotification(fn)

**请求参数(根据具体事件取值):**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**

| KEY           | DESCRIPTION                              |
| ------------- | ---------------------------------------- |
| event_id      | 事件 id                                    |
| event_type    | 事件类型，开发者根据对应的事件类型取相关字段，见下面示例             |
| gid           | 关系类型                                     |
| from_username | 事件发起者 username                           |
| from_appkey   | 事件发起者 appkey                             |
| to_usernames  | 事件当事人 [{"username":"","appkey":"","nickname":""},...] |
| ctime_ms      | 事件生成时间,精确到毫秒                             |
| extra         | 标识制字段                                    |
| return_code   | 用于好友邀请应答事件                               |
| description   | 描述                                       |
| msg_ids       | 消息 id 列表                                 |
| from_gid      | 群 gid                                    |
| to_groups     | 目标群组，格式 [{'gid':' ','name':' '},...]     |
| new_owner     | 新群主，格式  {'appkey':' ','username':' '}    |
| group_name    | 群名                                       |
| type          | 0:单聊，1:群聊                                |
| group_name    | 群名                                       |


**同时登录或者被禁用，被迫下线示例：event_type = 1**

```
//被踢者收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.extra =0同时登录，=1用户被禁用，=2用户被删除
});
```

**密码被修改，被迫下线示例：event_type = 2**

```
//当前在线者收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
});
```

**好友邀请事件示例：event_type = 5**

```
//被邀请方收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 邀请方 username
    //data.from_appkey 邀请方 appkey
    //data.media_id 邀请方头像
    //data.extra 1-来自邀请方的事件，2－来自被邀请方，即好友邀请的应答事件
    
});
```

**好友应答事件示例：event_type = 5**

```
//邀请方收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 被邀请方 username
    //data.from_appkey 被邀请方 appkey
    //data.extra 1-来自邀请方的事件，2－来自被邀请方，即好友邀请的应答事件
    //data.return_code 0－添加好友成功，其他为添加好友被拒绝的返回码
    //data.media_id 被邀请方头像
    //data.description 原因
});
```

**删除好友事件示例：event_type = 6**

```
//被删除好友收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 删除请求方 username
    //data.from_appkey 删除请求方 appkey
});
```

**好友更新事件示例：event_type = 7**

```
//好友双方都会收到该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.description API 好友管理
});
```

**创建群组事件示例：event_type = 8**

```
//群里所有人接收，即创建者接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 创建者 username
    //data.from_appkey 创建者 appkey
    //data.to_usernames 创建者
    //data.group_name 群名
    //data.media_id 群头像
    //data.gid 群 id
});
```

**退出群组事件示例：event_type = 9**

```
//群里所有人接收，包括退群者
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.extra=69 表示群主解散群，所有成员退出
    //data.from_username 退群者 username，extra=69 为空
    //data.from_appkey 退群者 appkey，extra=69 为空
    //data.to_usernames 退群者
    //data.gid 群 id
    //data.media_id 群头像
    //data.group_name 群名
    //data.new_owner 如果是群主退出，这个表示新群主
});
```

**添加群组成员事件示例：event_type = 10**

```
//群里所有人接收，包括被添加的成员和原来的成员
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 添加者 username
    //data.from_appkey 添加者 appkey
    //data.to_usernames 被添加的成员
    //data.media_id 群头像
    //data.group_name 群名
    //data.gid 群id
});
```

**删除群组成员事件示例：event_type = 11**

```
//群里所有人接收，包括被删除的成员和剩下的成员
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 删除者 username
    //data.from_appkey 删除者 appkey
    //data.to_usernames 被删除的成员
    //data.media_id 群头像
    //data.group_name 群名
    //data.gid 群 id
    //data.new_owner 如果是群主被删除，这个表示新群主
});
```

**修改群信息事件示例：event_type = 12**

```
//群里所有人接收该事件，包括修改者
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 修改者 username
    //data.from_appkey 修改者 appkey
    //data.to_usernames 修改者
    //data.gid 群 id
});
```

**免打扰变更事件示例：event_type = 37**

```
//变更方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
});
```

**黑名单变更事件示例：event_type = 38**

```
//变更方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
});
```

**群屏蔽变更事件示例：event_type =39**

```
//变更方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
});
```

**用户信息变更事件示例：event_type = 40**

```
//变更方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
});
```

**消息被撤回事件示例：event_type = 55**

```
//变更方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_username 消息发送方 username
    //data.from_appkey 消息发送方 appkey
    //data.msgid_list 被撤回的消息列表
    //data.type 0 单聊 ，1 群聊
    //data.to_usernames 撤回消息目标用户，单聊有效
    //data.from_gid 群id 群聊有效
});
```
**入群申请事件示例：event_type = 56**

***Since 2.5.0*** 

```
//群主接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.by_self 是否主动申请入群，true 是，false 被动邀请
    //data.from_appkey 邀请方或申请方 appkey
    //data.from_username 邀请方或申请方 username
    //data.target_appkey 被邀请方所属 appkey
    //data.to_usernames 被邀请方数组，by_self=false 有效，当by_self=true的时候邀请的目标用户就是from_user
    //data.description 申请理由，by_self=true 有效
});
```

**入群申请被拒绝事件示例：event_type = 57**

***Since 2.5.0*** 

```
//邀请方或者申请方接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_appkey 群主所属 appkey
    //data.from_username 群主 username
    //data.to_usernames 被邀请方或申请方   
    //data.description 拒绝理由
});
```
**管理员审批拒绝事件示例：event_type = 58**

***Since 2.6.0*** 

```
//群里所有管理员和群主
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_appkey 群主所属 appkey
    //data.from_username 群主 username
    //data.to_usernames 被拒绝成员   
    //data.from_eventid 操作事件 id
});
```

**群用户禁言事件：event_type = 65**

***Since 2.5.0*** 

```
//群所有用户接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_appkey 群主所属 appkey
    //data.from_username 群主 username
    //data.to_usernames 目标用户列表   
    //data.extra 1:禁言 2:取消禁言
});
```

**群组管理员变更事件：event_type = 80**

***Since 2.6.0*** 

```
//群所有用户接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_appkey 群主所属 appkey
    //data.from_username 群主 username
    //data.to_usernames 目标用户列表   
    //data.extra =1 添加管理员 2=取消管理员
});
```

**群主移交事件：event_type = 82**

***Since 2.6.0*** 

```
//群所有用户接收该事件
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.from_gid 群 id
    //data.group_name 群名
    //data.media_id 群头像
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.from_appkey 老群主 appkey
    //data.from_username 老群主 username
    //data.to_usernames 新群主   
});
```


**多端在线好友变更事件示例：event_type =100**

```
//自己触发
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.extra 5 添加好友 6 删除好友 7 修改好友备注
    //data.to_usernames 目标用户
    /data.media_id 目标头像
    //data.description extra=7有效，格式{'memo_name':','memo_others':''}
});
```

**多端在线黑名单变更事件示例：event_type =101**

```
//自己触发
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.to_usernames 目标用户
    //data.extra 1 添加黑名单 2 删除黑名单
});
```

**多端在线免打扰变更事件示例：event_type =102**

```
//自己触发
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.extra 31 添加单聊免打扰 32 删除单聊免打扰
    //           33 添加群组免打扰 34 删除群组免打扰
    //           35 添加全局免打扰 36 删除全局免打扰
    //data.to_usernames 目标用户, extra = 31,32 有效
    //data.to_groups 目标群组, extra = 33,34 有效
});
```

**多端在线群屏蔽变更事件示例：event_type =103**

```
//自己触发
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 事件生成时间
    //data.extra 1 添加群屏蔽 2 删除群屏蔽
    //data.to_groups 目标群组
});
```

**多端在线消息已读回执变更事件示例：event_type =201**

```
//自己触发
JIM.onEventNotification(function(data) {
    //data.event_id 事件 id
    //data.event_type 事件类型
    //data.ctime_ms 
    //data.description.type 3:单聊 4:群聊
    //data.description.gid 群 id, 群聊有效
    //data.description.appkey 用户所属 appkey, 单聊有效
    //data.description.username 用户 name
    //data.msgids 表示其他端对消息列表里面的消息已经已读了
});
```

### 业务事件同步监听

JMessage#onSyncEvent(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**
 同业务事件监听

 **使用示例**

```
JIM.onSyncEvent(function(data) {
    // data 为事件数组 [event1,event2,...]
});
```

### 消息已读数变更事件实时监听

***Since 2.4.0***

JMessage#onMsgReceiptChange(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**

| KEY          | DESCRIPTION    |
| ------------ | -------------- |
| gid          | 群 ID,群聊有效      |
| appkey       | 所属 appkey,单聊有效 |
| username     | 用户 name,单聊有效   |
| type         | 会话类型 3:单聊 4:群聊 |
| receipt_msgs | 消息未读状态列表,如下:   |

**消息未读状态参数**

| KEY          | DESCRIPTION               |
| ------------ | ------------------------- |
| msg_id       | 消息 id                     |
| unread_count | 消息未读数，跟之前的对比，取小的作为最新消息未读数 |

 **使用示例**

```
JIM.onMsgReceiptChange(function(data) {
    // data.type
    // data.gid
    // data.appkey
    // data.username
    // data.receipt_msgs[].msg_id
    // data.receipt_msgs[].unread_count
});
```


### 消息已读数变更事件同步监听

***Since 2.4.0***

JMessage#onSyncMsgReceipt(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**

同已读数变更事件实时监听

 **使用示例**

```
JIM.onSyncMsgReceipt(function(data) {
    // data 为已读数变更事件数组 [receiptChange1,...]
});
```

### 会话未读数变更监听（多端在线）

***Since 2.4.0***

JMessage#onMutiUnreadMsgUpdate(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 事件接收处理函数    |

**返回参数**

| KEY      | DESCRIPTION             |
| -------- | ----------------------- |
| type     | 3 单聊 ，4 群聊              |
| gid      | 群 id ，type=4 有效         |
| appkey   | 目标用户 appkey，type=3 有效   |
| username | 目标用户 username，type=3 有效 |

 **使用示例**

```
JIM.onMutiUnreadMsgUpdate(function(data) {
    // data.type 会话类型
    // data.gid 群 id
    // data.appkey 所属 appkey
    // data.username 会话 username
});
```
### 消息透传监听
***Since 2.4.0***

JMessage#onTransMsgRec(fn)

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 监听处理函数      |

**返回参数**

| KEY           | DESCRIPTION                              |
| ------------- | ---------------------------------------- |
| type          | 3 单聊消息透传 ，4 群聊消息透传, 5 在线设备消息透传           |
| gid           | 群 id ，type=4 有效                          |
| from_appkey   | 用户 appkey，type=3 有效                      |
| from_username | 用户 username，type=3 有效                    |
| platform      | 目标平台 all \| android \| ios \| pc，type=5 有效 |
| cmd           | 透传信息                                     |

 **使用示例**

```
JIM.onTransMsgRec(function(data) {
    // data.type 会话类型
    // data.gid 群 id
    // data.from_appkey 用户所属 appkey
    // data.from_username 用户 username
    // data.platform 目标平台
    // data.cmd 透传信息
});
```

###聊天室消息监听

JMessage#onRoomMsg(fn)

***Since 2.5.0***

**请求参数:**

| KEY  | REQUIRE | DESCRIPTION |
| ---- | ------- | ----------- |
| fn   | TRUE    | 消息接收处理函数    |

**返回消息数组**

| KEY      | DESCRIPTION                              |
| -------- | ---------------------------------------- |
| room_id  | 聊天室 id                                   |
| msg_id   | 消息 ID                                    |
| ctime_ms | 消息生成时间,毫秒                                |
| content  | [消息体](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/) |

**使用示例**

```
JIM.onRoomMsg(function(data) {
   // data.room_id 聊天室 id
   // data.msg_id 消息 id
   // data.ctime_ms 消息生成时间
   // data.content
});
```

## 高级应用

### 发送跨应用消息

跨应用是指相同账号下不同 appkey 之间的用户进行操作，默认在没指定目标 appkey 的情况下目标 appkey 就是当前登录用户所使用的 appkey，如果需要跨应用操作则在接口参数上指定具体的目标 appkey。

以2.1发送单聊为例：

JMessage#sendSingleMsg()

**请求参数：**

| KEY             | REQUIRE | DESCRIPTION           |
| --------------- | ------- | --------------------- |
| target_username | TRUE    | 接收消息者 username        |
| target_nickname | TRUE    | 接收消息者 nickname        |
| content         | TRUE    | 消息文本                  |
| extras          | FALSE   | 附加字段,字典类型             |
| appkey          | FALSE   | 跨应用查询时必填，目标应用的 appkey |
其中 appkey 为目标 appkey，其他接口类似

### 发送、接收图片或文件

SDK 支持单图片,单文件发送。发送文件和图片接口需要接收一个类型为 FormData 参数值，该参数值包含了用户需要发送的文件信息。

构造FormData示例：

```
var fd = new FormData();

fd.append(fileName, file);
```

完成构造 FormData 后 将其作为参数传入对用的接口，以发送单聊图片为例子：

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

图片、文件的接收需要通过 JMessage#getResource 接口传入资源 media_id 获取访问路径

### 发送和接收 Emoji 表情

Emoji 表情就是一种在 Unicode 位于`\u1F601`-`\u1F64F`区段的字符。 JMessage的消息内容都是使用[utf8mb4](https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html)编码，向下兼容 UTF8。
只要正确输入 Emoji 字符都可以使用 JMessage 文本消息 API 进行发送。如果用户需要转存聊天消息，请先确保数据库支持 utf8mb4 编码。
开发者可以使用第三方开源的 Web Emoji 解决方案，如[coocy/emoji](https://github.com/coocy/emoji),[iamcal/js-emoji](https://github.com/iamcal/js-emoji)来在网页上显示Emoij表情。


## 错误码定义

参考文档：[IM Web SDK 错误码列表](./im_errorcode_js)



