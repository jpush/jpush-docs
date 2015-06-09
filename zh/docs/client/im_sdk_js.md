<h1>极光IM SDK - JavaScript</h1>

### 概述

极光IM（英文名JMessage）JS SDK 方便用户开发 Web IM 类应用程序。

要了解极光IM的概述信息，请参考文档：[极光IM指南](../../guideline/jmessage_guide)

### 功能

#### Demo Web IM

我们基于极光 IM JS SDK 提供一个完整的 Web IM Demo，它就是一个 Web IM App。或者说，如果你需要做一个 Web IM 应用，你可以从 GitHub 上下载该源码，然后做以下两个变更将它变成你自己的 Web IM 应用：
 
+ 在 JPush Web 控制台上注册应用，获取到的 Appkey 配置到 Web IM 中；
+ 根据我们提供的特定算法，在自己的服务器端生成签名，获取后配置到 Web IM 即可。

#### 消息

极光IM 最核心的功能是 IM 即时消息的功能。

- 保证消息及时下发；
- 单聊，群聊；
- 消息类型：文本、语音、图片；
- 用户未在线时保存离线消息；
- 基于 JPush 原有的大容量稳定的长连接、大容量消息并发能力；

#### 用户

开发者的用户，基于 username / password 注册到 JMessage。
目前 JS SDK 侧不提供注册用户功能，你可以通过 Android 端、 IOS 端或者服务器端批量发起注册。
用户登录 Web IM 后，就可以向其它 username 发聊天消息，也可以收到来自其它 username 的消息，或者群组消息了。
用户 A 是否有权限向用户 B 发消息，由 App 逻辑自己控制。（由 JMessage 提供好友关系时，JMessage 会做控制）

#### 群组

可以把多个 username 加入到同一个群组里，之后各成员可以在群组中发群聊消息。

- 创建群组、退出群组；
- 添加群组成员、移除群组成员；


#### 好友（还未提供）



### SDK 权限签名

为保证开发者应用的安全性，在使用JMessage JS SDK 之前需要在开发者自己的服务器端实现签名的逻辑，然后将相关信息返回，调用 JS SDK 相关接口填入相关信息来完成开发者有效性认证。
#### 签名算法
签名生成规则如下：参与签名的字段包括 appKey, masterSecrect, timestamp（时间戳）, randomStr（随机字符串）。对所有待签名参数按照 appKey、timestamp、randomStr、masterSecrect的顺序，使用URL键值对的格式（即key1=value1&key2=value2…）拼接成字符串string1。对 string1 作 MD5 加密，字段名和字段值都采用原始值，不进行 URL 转义，然后将 MD5 串转成大写，完成签名。
#### 算法示例（Java）
	// 生成时间戳
	public String getTimestamp() {
        	return Long.toString(System.currentTimeMillis() / 1000);
	}
	
	// 生成随即字符串
	public String getRandomStr() {
        	return UUID.randomUUID().toString();
   	}
	
	// 生成签名
	public String getSignature(String appKey, String timestamp, String randomStr, String masterSecrect){
    		String str = "appKey=" + appKey + "&timestamp=" + timestamp +
             	"&randomStr=" + randomStr + "&masterSecrect=" + masterSecrect;
    		MessageDigest md = MessageDigest.getInstance("MD5");
    		String result = byteArrayToHexString(md.digest(str.getBytes()));
    		return result.toUpperCase();
	}


### 集成指南

#### 集成概述
在开发者自己页面中按照以下顺序引入相关脚本文件：
#  
```<script type="text/javascript" src="http://web.file.jpush.cn/jquery.min.js"></script>```
```<script type="text/javascript" src="http://web.file.jpush.cn/ajaxfileupload.min.js"></script>```
```
<!-- 该脚本用于上传图片文件 -->
```
```<script type="text/javascript" src="http://web.file.jpush.cn/socket.io.min.js"></script>```
```
<!-- 该脚本用于维护客户端到服务端的网络连接 -->
```
```<script type="text/javascript" src="http://web.file.jpush.cn/jmessage-1.0.0.min.js"></script>```
```
<!-- 该脚本为 JMessage JS SDK -->
```
#  
以上脚本文件为集成 JMessage JS SDK 时所必须引入的文件，由于这些脚本存在相互依赖的关系，所以集成时请按照以上顺序引入。

引入成功后，在调用 JMessage JS SDK 的部分 API 前，你需要先完成签名认证，这个过程大致为：在客户端与服务端建立连接后，从你自己的服务端获取签名相关参数，之后调用 API JMessage.config 发起配置验证请求，之后可以在 JMessage.ready 和 JMessage.error 的回调中得到相应的反馈，如果 ready 那么你可以成功调用其它的 API，否则你需要对照我们文档中的签名部分检查下自己的签名逻辑，然后重新发起验证。

#### 集成示例
```
JMessage.onConnected(function(){ // 在网络连接成功的回调中完成获取签名的逻辑
	$.ajax({  // 如果您需要跨域获取，则采用下面方式；否则采用普通ajax方式即可。
		url: '获取签名的服务端地址',
		method: 'GET',
		dataType : 'jsonp',
		jsonp: 'jsoncallback',
		jsonpCallback: 'jsonpCallback',
	});
});

var jsonpCallback = function(data){  // 在成功返回签名数据后，调用 API 完成验证。
     	JMessage.config({
		debug: true,
		appKey: '开发者注册应用的AppKey',
		timestamp: data.timeStamp,
		randomStr: data.randomStr,
		signature: data.signature
	});
};

JMessage.ready(function(){ // 签名验证成功后触发回调，你可以在此完成部分业务逻辑

});

JMessage.error(function(code, message){ // 签名失败时触发回调，会返回异常状态码和相应的异常信息

});

在签名验证成功后，你可以根据自身的业务需求，调用 JMessage JS SDK API 来完成自己的业务逻辑。
```


### API 列表

#### 验证类

##### 配置与验证
在使用 JMessage JS SDK 的其它 API 之前，必须从开发者自己的服务端获取 appKey、timestamp、randomStr、signature 参数，然后调用API config 来完成验证。
```
JMessage.config({
	appKey: "",
	timestamp: "",
	randomStr: "",
	signature: ""
});
```
参数说明

+ String appKey 开发者创建应用时的appKey
+ String timestamp 开发者 Server 端返回的时间戳
+ String randomStr 开发者 Server 端返回的随即字符串
+ String signature 开发者 Server 端返回的签名


##### 验证成功
```
JMessage.ready(function() {

});
```
参数说明

+ 无


##### 验证失败
```
JMessage.error(function(code, message) {

});
```
返回

+ Number code 验证错误相应的错误码
+ String message 错误码对应的错误信息

#### 网络连接类

##### 网络连接成功
```
JMessage.onConnected(function() {

});
```

参数说明

+ 无

##### 网络连接中断
```
JMessage.onDisconnected(function() {

});
```
参数说明

+ 无


#### 用户类

##### 用户登陆
```
JMessage.login({
	username: "",
  	password: "", 
  	success: function() {
           
  	},
	fail: function(code, message){

	}
});
```
参数说明

+ String username 用户名
+ String password 用户密码
+ Function success 登陆成功的回调函数
+ Function fail 登陆失败的回调函数

	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息

##### 用户退出
```
JMessage.logout();
```
参数说明

+ 无

##### 获取用户信息
```
JMessage.getUserInfo({
  	username: "",
  	success: function(response) {
               
  	},
	fail: function(code, message){

	}
});
```
参数说明

+ String username 用户名
+ Function success 获取用户信息成功后的回调函数 

	+ 参数说明
		+ String response 对应用户的信息

```
{
	"username": "chicken",
	"nickname": "Tom Chick",
	"star": 2,
	"avatar": "qiniu/image/uipreqfdsakl",     // 用户头像。存储的路径
	"gender": 0,                              // 用户性别
	"signature": "I am a ...",                // 签名
	"region": "深圳",                         // 区域
	"address": "南山区",                      // 详细地址
	"mtime": "2015-03-03 11:00:00",          // 修改时间
	"ctime": "2015-03-03 11:00:00",          // 创建时间
}
```

+ Function fail 获取用户信息失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息


#### 消息类

##### 发送文本消息
```
JMessage.sendTextMessage({
	targetId: "",
	targetType: "",
	text: "",
	idGenerated: function(rid){
	
	},
	success: function(rid) {

	},
	fail: function(code, message, rid) {	

	}
});
```
参数说明

+ String targetId 单聊时为 username，群聊时为 groupId
+ String targetType 单聊时为"single"，群聊时为"group"
+ String text 发送消息的文本内容
+ Function idGenerated 发送消息后的回调
	+ 参数说明
		+ Number rid 此消息对应的 rid

+ Function success 消息发送成功的回调函数
	+ 参数说明
		+ Number rid 此消息对应的 rid

+ Function fail 消息发送失败的回调函数
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息
		+ Number rid 此消息对应的 rid


##### 发送图片消息
```
JMessage.sendImageMessage({
	targetId: "",
	targetType: "",
	fileId: "",
	idGenerated: function(rid){
	
	},
	success: function(rid) {

	},
	fail: function(code, message, rid) {	

	}
});
```
参数说明

+ String targetId 单聊时为 username，群聊时为 groupId
+ String targetType 单聊时为"single"，群聊时为"group"
+ String fileId 上传文件域（```<input type='file' id='' name='' />```）的 id，此项开发者需注意id 和 name 保持一致
+ Function idGenerated 发送消息后的回调
	+ 参数说明
		+ Number rid 此消息对应的 rid

+ Function success 消息发送成功的回调函数
	+ 参数说明
		+ Number rid 此消息对应的 rid

+ Function fail 消息发送失败的回调函数
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息
		+ Number rid 此消息对应的 rid

##### 重发消息
```
JMessage.resendMessage({
	rid: 12345,
	success: function(rid) {

	},
	fail: function(code, message, rid) {

	}
});
```
参数说明

+ Number rid 发送失败的消息对应的 rid
+ Function success 消息发送成功的回调函数
	+ 参数说明
		+ Number rid 此消息对应的 rid

+ Function fail 消息发送失败的回调函数
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息
		+ Number rid 此消息对应的 rid


##### 收到下发消息
```
JMessage.onMessageReceived(function(jMessage) {
	
});
```
参数说明

+ String jMessage 消息内容，详情参照 [消息协议](http://docs.jpush.io/advanced/im_message_protocol/#im)
```
{
    "version": 1,
    "target_type": "single",
    "target_id": "javen",
    "target_name": "Javen Fang",
    "from_type": "user",
    "from_id": "fang", 
    "from_name": "Fang Javen", 
    "create_time": 135432432187,
    "msg_type": "text",
    "msg_body": {
        "text": "Hello, JPush IM!"  
    }
}

```
	

##### 收到下发事件
```
JMessage.onEventReceived(function(jEvent) {
	
});
```
参数说明

+ String jEvent 事件内容，详情参照 [事件通知](http://docs.jpush.io/advanced/im_objects/#eventnotification)
```
{
    "event_type: "create_group",
    "from_username": "",
    "gid": 13579,
    "to_username_list": ["eddie", "annie"],
    "description": "the event is due to...",
    "ctime": "2014-07-01 00:00:00"
}
```

#### 群组类

##### 创建群组
```
JMessage.createGroup({
	groupName: "",
	groupDescription: "",
	success: function(response) {
        
	},
	fail: function(code, message){
	
	}
});
```
参数说明

+ String groupName 群组名称
+ String groupDescription 群组描述
+ Function success 创建群组成功后的回调函数
	+ 参数说明
	 	+ String resposne 新建群组的信息
```
{
	"groupName": "tGroup",
	"groupDescription": "测试建群",
	"groupLevel": 200,	
	"flag": 0,
	"gid": 10005307
}
```

+ Function fail 创建群组失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息


##### 获取群组信息
```
JMessage.getGroupInfo({
	groupId: 12345
	success: function(response) {
	
	},
	fail: function(code, message) {

	}
});
```
参数说明

+ Number groupId 群组ID
+ Function success 获取群组信息成功后的回调函数
	+ 参数说明
	 	+ String resposne 群组的详细信息
```
{
	"gid":10003195,
	"ownerUsername":"群组名称",
	"groupName":"群名称",
	"groupDesc":"群描述",
	"members":[
			{	
				"username":"p001",
				"nickname":"nick",
				"star":0,
				"avatar":"qiniu/image/DDAF7129753ADDB3",
				"gender":0,
				"signature":"个性签名位在这里那哦",
				"region":"深圳",
				"address": "南山区"
				"mtime":"2015-05-22 14:00:51",
				"ctime":"2015-03-30 15:50:13"
			  },{}...
			]
}
```

+ Function fail 获取群组信息失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息

##### 更新群组信息
```
JMessage.updateGroupInfo({
	groupId: "",
	groupName: "",
	groupDescription: "",
	success: function(response){
	
	},
	fail: function(code, message){

	}
});
```
参数说明

+ String groupName 群组名称
+ String groupDescription 群组描述
+ Function success 修改群组信息成功后的回调函数
	+ 参数说明
	 	+ String resposne 新建群组的信息
```
{
	"groupName": "tGroup",
	"groupDescription": "测试建群",
	"groupLevel": 200,	
	"flag": 0,
	"gid": 10005307
}
```

+ Function fail 修改群组信息失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息

##### 添加群组成员
```
JMessage.addGroupMembers({
	groupId: 12345,
	memberUsernames:['u001', 'u002'],
	success: function(){
		
	},
	fail: function(code, message){
	
	}
});
```
参数说明

+ String groupID 群组ID
+ Array memberUsernames 添加群成员的用户名的列表
+ Function success 添加群成员成功后的回调函数
+ Function fail 添加群成员失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息

##### 删除群组成员
```
JMessage.removeGroupMembers({
	groupId: 12345,
	memberUsernames:['u001', 'u002'],
	success: function(){
		
	},
	fail: function(code, message){
	
	}
});
```
参数说明

+ String groupID 群组ID
+ Array memberUsernames 移除群成员的用户名的列表
+ Function success 移除群成员成功后的回调函数
+ Function fail 移除群成员失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息


##### 退出群组
```
JMessage.exitGroup({
	groupId: 12345,
	success: function(){
	
	},
	fail: function(code, message){

	}
});
```
参数说明

+ String groupID 群组ID
+ Function success 退出群组成功后的回调函数
+ Function fail 退出群组失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息

##### 获取我的群组列表
```
JMessage.getGroupList({
	success: function(response) {
	
	}, 
	fail: function(code, message){

	}
});
```
参数说明

+ Function success 获取我的群组列表成功后的回调函数
	+ 参数说明
	 	+ String resposne 我的群组的信息
```
[
	{
		"gid":10003195,
		"ownerUsername":"p001",
		"groupName":"m_name",
		"groupDesc":"m_g_desc",
		"membersUsername":["p001","p002","p003","p005","p004"]
	},{
		"gid":10003055,
		"ownerUsername":"p001",
		"groupName":"test15",
		"groupDesc":"",
		"membersUsername":["p001","p002","p003","p004"]
	},{}...
]
```
+ Function fail 获取我的群组列表失败后的回调函数 
	
	+ 参数说明
		+ Number code 错误码
		+ String message 错误码对应的错误信息



### 错误码定义

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th style="padding: 0 5px; " width="10px">Code</th>
      <th style="padding: 0 5px; " width="468px">说明</th>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872000</td>
      <td style="padding: 0 5px; " >服务端错误</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872001</td>
      <td style="padding: 0 5px; " >用户未登陆</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872002</td>
      <td style="padding: 0 5px; " >传入参数异常</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872003</td>
      <td style="padding: 0 5px; " >登陆异常</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872004</td>
      <td style="padding: 0 5px; " >配置校验异常</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872005</td>
      <td style="padding: 0 5px; " >签名失效</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872006</td>
      <td style="padding: 0 5px; " >请求超时</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872007</td>
      <td style="padding: 0 5px; " >与服务端断开</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >872008</td>
      <td style="padding: 0 5px; " >在其它地方登陆</td>
    </tr>
  </table>
</div>


### 相关文档
+ [极光IM指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM 业务对象](../../advanced/im_objects/)
+ [JPush Android SDK 集成指南](../../guideline/android_guide/)
+ [JPush Android SDK 概述](../../client/android_sdk/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [IM REST API](../../server/rest_api_im/)

