# IM REST API

极光 IM API 为开发者提供 IM 相关功能的 HTTP API。

这类 API 地址统一为（注意与 Push API 不同）：https://api.im.jpush.cn  

**HTTP 验证**

验证采用 HTTP Basic 机制，即 HTTP Header（头）里加一个字段（Key/Value对）：

Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

## User对象字段总览

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >含义</th>
			<th >字符长度限制</th>
		</tr>
		<tr >
			<td>username</td>
			<td>用户登录名</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>password</td>
			<td>登录密码</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>appkey</td>
			<td>用户所属于的应用的appkey</td>
			<td></td>
		</tr>
		<tr >
			<td>nickname</td>
			<td>用户昵称</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>birthday</td>
			<td>生日</td>
			<td>yyyy-MM-dd HH:mm:ss</td>
		</tr>
		<tr >
			<td>gender</td>
			<td>性别 0 - 未知， 1 - 男 ，2 - 女 </td>
			<td></td>
		</tr>
		<tr >
			<td>signature</td>
			<td>用户签名</td>
			<td>Byte(0~250)</td>
		</tr>
		<tr >
			<td>region</td>
			<td>用户所属地区</td>
			<td>Byte(0~250)</td>
		</tr>
		<tr >
			<td>address</td>
			<td>用户详细地址</td>
			<td>Byte(0~250)</td>
		</tr>
		<tr >
			<td>ctime</td>
			<td>用户创建时间</td>
			<td></td>
		</tr>
		<tr >
			<td>mtime</td>
			<td>用户最后修改时间</td>
			<td></td>
		</tr>
		<tr >
			<td>extras</td>
			<td>用户自定义json对象</td>
			<td>Byte(0~512)</td>
		</tr>
	</table>
</div>


##  用户注册


### 注册用户

批量注册用户到极光IM 服务器，一次批量注册最多支持500个用户。

	POST /v1/users/


#### Example Request

```
[{"username": "dev_fang", "password": "password"}] 
```

#### Request Params

JSON Array.

+ username（必填）用户名
    - 开头：字母或者数字
    - 字母、数字、下划线
    - 英文点、减号、@
+ password（必填）用户密码。极光IM服务器会MD5加密保存。
+ nickname  （选填）用户昵称
    - 不支持的字符：英文字符： \n \r\n 
+ avatar  （选填）头像
    - 需要填上从文件上传接口获得的media_id	
+ birthday    （选填）生日 example: 1990-01-24
    - yyyy-MM-dd 
+ signature  （选填）签名
    - 支持的字符：全部，包括 Emoji
+ gender    （选填） 性别
    - 0 - 未知， 1 - 男 ，2 - 女 
+ region      （选填）地区
    - 支持的字符：全部，包括 Emoji
+ address   （选填）地址
    - 支持的字符：全部，包括 Emoji
+ extras     (选填) 用户自定义json对象

#### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 
[{"username": "dev_fang"  }] 
```

#### Response Params

JSON Array.

+ username
+ error 某个用户注册出错时，该对象里会有 error 对象，说明错误原因。
    - 899003   参数错误，Request Body参数不符合要求
    - 899001   用户已存在


## Admin 注册

### Admin Register 管理员注册 (管理员api发送消息接口的权限)

```
POST /v1/admins/
```
#### Example Request

```
{"username": "dev_fang", "password": "password"}
```

#### Request Params

+ username Byte(4-128) 支持字符
    - 开头：字母或者数字
    - 字母、数字、下划线
    - 英文点、减号、@

+ password Byte(4-128) 字符不限
+ nickname  （选填）用户昵称
    - 不支持的字符：英文字符： \n \r\n 
+ avatar  （选填）头像
    - 需要填上从文件上传接口获得的media_id	
+ birthday    （选填）生日 example: 1990-01-24
    - yyyy-MM-dd 
+ signature  （选填）签名
    - 支持的字符：全部，包括 Emoji
+ gender    （选填） 性别
    - 0 - 未知， 1 - 男 ，2 - 女 
+ region      （选填）地区
    - 支持的字符：全部，包括 Emoji
+ address   （选填）地址
    - 支持的字符：全部，包括 Emoji
+ extras     (选填) 用户自定义json对象

#### Example Response

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8 
```

### GetAdminsListByAppkey  获取应用管理员列表

```
GET /v1/admins?start={start}&count={count}
```
#### Example Request

#### Request Header 

```
GET /admins?start=1&count=30
Accept: application/json
```
#### Request Body

```
N/A
```

#### request params
+ start    起始记录位置 从0开始
+ count  查询条数 最多支持500条

#### Example Response

#### Response Header

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```
#### Response Data 

```
{
  "total":1233, 
  "start":1100,
  "count":3,
  "users":
    [{"username" : "cai", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"},
      {"username" : "yi", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"},
      {"username" : "huang", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"} ]
}
```

## 用户维护

### 获取用户信息

	GET /v1/users/{username}

#### Request Params

+ username 用户名。填充到请求路径上。

#### Example Response

```
{
	"username" : "javen", 
 	"nickname" : "hello", 
 	"avatar" : "/avatar", 
 	"birthday" : "1990-01-24 00:00:00", 
 	"gender" : 0, 
 	"signature" : "orz", 
 	"region" : "shenzhen", 
 	"address" : "shenzhen", 
 	"mtime" : "2015-01-01 00:00:00", 
 	"ctime" : "2015-01-01 00:00:00"}
```
说明

除了username mtime ctime这三个子段之外，其余字段如果没存json中就没有相应的key

### 更新用户信息

	PUT /v1/users/{username}

#### Example Request

```
{
	"nickname": "Hello JMessage"
}
```

#### Request Params

+ nickname  （选填）用户昵称
    - 不支持的字符：英文字符： \n \r\n 
+ avatar  （选填）头像
    - 需要填上从文件上传接口获得的media_id	
+ birthday    （选填）生日 example: 1990-01-24
    - yyyy-MM-dd 
+ signature  （选填）签名
    - 支持的字符：全部，包括 Emoji
+ gender    （选填） 性别
    - 0 - 未知， 1 - 男 ，2 - 女 
+ region      （选填）地区
    - 支持的字符：全部，包括 Emoji
+ address   （选填）地址
    - 支持的字符：全部，包括 Emoji
+ extras     (选填) 用户自定义json对象



#### Example Response

```
< HTTP/1.1 204 
< Content-Type: application/json; charset=utf-8

```

### 用户在线状态查询 

```
Get /v1/users/{username}/userstat
```
#### Example Request

Request Header 

```
Get /v1/users/caiyh/userstat
Content-Type: application/json; charset=utf-8 
```
Request Params

+ username 用户名 

Request Body

N/A

#### Example Response
Response Header

```
HTTP/1.1 200 NO Content
Content-Type: application/json; charset=utf-8
```

Response Data

```
{"login":true, "online": false}
```
该接口不适用于多端在线，多端在线请用批量状态接口

#### Error Code

错误码

+ 899003 username不合法
+ 899002 用户不存在


### 批量用户在线状态查询

```
Post /v1/users/userstat
```
#### Example Request

Request Header 

```
Post /v1/users/userstat
Content-Type: application/json; charset=utf-8 
```
Request Params

N/A

Request Body

["USER1","USER2"]

#### Example Response
Response Header

```
HTTP/1.1 200 
Content-Type: application/json; charset=utf-8
```

Response Data

```
[{"devices": [],"username": "caiyh01"},{"devices": [{"login": false,"online": false,"platform": "a"}],"username": "Rauly"}]
```
+ devices  设备登陆状态数组，没有登陆过数组为空
+ platform SDK各平台：a-Android，i-iOS，j-JS，w-Windows

#### Error Code

错误码

+ 899003 username不合法
+ 899002 用户不存在


### 修改密码

```
PUT /v1/users/{username}/password
```

#### Request Header 

```
PUT /v1/users/javen/password
```

#### Example Request

```
{
	 "new_password": "654321" 
}
```
#### Request Params

+ new_password （必填）新密码

#### Example Response

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```
#### Response Data
+ N/A

### 删除用户

	DELETE /v1/users/{username}

Request Params

+ username 用户名。

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json; charset=utf-8   
```


### 添加黑名单

```
Put /v1/users/{username}/blacklist
```

Example Request

Request Header 

```
Put /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8  
```

Request Params 

+ JsonArray
  + username的JsonArray

Request Body

```
[
 "test1",
 "test2"
 ]
```

Example Response 

Response Header 

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8 
```

Response Data

N/A


### 移除黑名单

```
Delete /v1/users/{username}/blacklist
```

Example Request

Request Header 

```
Delete /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8  
```

Request Params

+ JsonArray
  + username的JsonArray

Request Body

```
[
 "test1",
 "test2"
 ]
```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

### 黑名单列表

```
Get /v1/users/{username}/blacklist
```

Example Request

Request Header 

```
Put /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8 
```

Request Params

+ username 用户名

Request Body

N/A

Example Response

Response Header 

```
HTTP/1.1 200 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

```
[{"username" : "javen", "nickname" : "hello", "avatar" = "/avatar", "birthday" : "1990-01-24 00:00:00", "gender" : 0, "signature" : "orz", "region" : "shenzhen", "address" : "shenzhen", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"}]
```


### 获取用户列表

	GET /v1/users/?start={start}&count={count}

Request Params

+ start 开始的记录数
+ count 要获取的记录个数

Example Response

```
< HTTP/1.1 200 
< Content-Type: application/json

{
    "total": 12580,
    "start": 1100,
    "count": 100,
    "users":
    [{"username" : "cai", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"},
      {"username" : "yi", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"},
      {"username" : "huang", "nickname" : "hello", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00"} ]
}
```

### 免打扰
#### 免打扰设置

```
POST  /v1/users/{username}/nodisturb
```

Example Request

Request Header 

```
POST  /v1/users/{username}/nodisturb
Content-Type: application/json; charset=utf-8  
```

Request Params

+ single  单聊免打扰，支持add remove数组 （可选）
+ group   群聊免打扰，支持add remove数组（可选）
+ global  全局免打扰，0或1 0表示关闭，1表示打开 （可选）


Request Body

```
{   
   "single":{   
      "add":[   
         "username1",
         "username2"
      ]
   },
   "group":{   
      "add":[   
         110000101
      ],
      "remove":[   
         1000001111
      ]
   },
   "global":0
}
```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

Error Code

+ 899003 username不合法；
+ 899002 用户不存在；
+ 899051  群组不存在；
+ 899052 设置群组消息屏蔽，设置的群组屏蔽已经打开
+ 99053 设置群组消息屏蔽，设置的群组屏蔽已经关闭


### 禁用用户

	PUT /v1/users/{username}/forbidden?disable={disable}

Request Params

+ disable  boolean,true代表禁用用户，false代表激活用户

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```


## 消息相关

### 发送消息

```
POST /v1/messages
```

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >含义</th>
		</tr>
		<tr >
			<td>version</td>
			<td>版本号 目前是1 （必填）</td>
		</tr>
		<tr >
			<td>target_type</td>
			<td>发送目标类型 single - 个人，group - 群组 （必填）</td>
		</tr>
		<tr >
			<td>from_type</td>
			<td>发送消息者身份 当前只限admin用户，必须先注册admin用户 （必填）</td>
		</tr>
		<tr >
			<td>msg_type</td>
			<td>发消息类型 text - 文本，image - 图片, custom - 自定义消息（msg_body为json对象即可，服务端不做校验）voice - 语音 （必填）</td>
		</tr>
		<tr >
			<td>target_id</td>
			<td>目标id single填username group 填Group id （必填）</td>
		</tr>
		<tr >
			<td>target_appkey</td>
			<td>跨应用目标appkey（选填）</td>
		</tr>
		<tr >
			<td>from_id</td>
			<td>发送者的username （必填</td>
		</tr>
		<tr >
			<td>from_name</td>
			<td>发送者展示名（选填）</td>
		</tr>
		<tr >
			<td>target_name</td>
			<td>接受者展示名（选填）</td>
		</tr>
		<tr >
			<td>no_offline</td>
			<td>消息是否离线存储 true或者false，默认为false，表示需要离线存储（选填）</td>
		</tr>
		<tr >
			<td>no_notification</td>
			<td>消息是否在通知栏展示 true或者false，默认为false，表示在通知栏展示（选填）
</td>
		</tr>
		<tr >
			<td>notification</td>
			<td>自定义通知栏展示（选填）</td>
		</tr>
		<tr >
			<td>notification->title</td>
			<td>通知的标题（选填）</td>
		</tr>
		<tr >
			<td>notification->alert</td>
			<td> 通知的内容（选填）</td>
		</tr>
		<tr bgcolor="#D3D3D3">
			<td>msg_body</td>
			<td>Json对象的消息体 限制为4096byte</td>
		</tr>
				<tr>
		<td colspan="2" ><font  color="red">msg_type为text时，msg_body的格式如下 </font></td>
		</tr>
		<tr >
			<td>msg_body -> text</td>
			<td>消息内容 （必填）</td>
		</tr>
		<tr >
			<td>msg_body-> extras</td>
			<td>选填的json对象 开发者可以自定义extras里面的key value（选填）	</td>
		</tr>

		<tr>
		<td colspan="2" ><font  color="red">msg_type为image时,msg_body为上传图片返回的json，格式如下 </td>
		</tr>
		<tr>
		<td>msg_body->media_id</td>
		<td>String 文件上传之后服务器端所返回的key，用于之后生成下载的url（必填）</td>
		</tr>
		<tr>
		<td>msg_body->media_crc32</td>
		<td>long 文件的crc32校验码，用于下载大图的校验 （必填）</td>
		</tr>
		<tr>
		<td>msg_body->width</td>
		<td>int 图片原始宽度（必填）</td>
		</tr>
		<tr>
		<td>msg_body->height</td>
		<td>int 图片原始高度（必填）</td>
		</tr>
		<tr>
		<td>msg_body->format </td>
		<td>String 图片格式（必填）</td>
		</tr>
		<tr>
		<td>msg_body->hash </td>
		<td>String 图片hash值（可选）</td>
		</tr>
		<tr>
		<td>msg_body->fsize</td>
		<td>int 文件大小（字节数）（必填）</td>
		</tr>
	
	<td colspan="2" ><font  color="red">msg_type为voice时,msg_body为上传语音返回的json，格式如下 </td>
		</tr>
		<tr>
		<td>msg_body->media_id</td>
		<td>String 文件上传之后服务器端所返回的key，用于之后生成下载的url（必填）</td>
		</tr>
		<tr>
		<td>msg_body->media_crc32</td>
		<td>long 文件的crc32校验码，用于下载大图的校验 （必填）</td>
		</tr>
		<tr>
		<td>msg_body->duration</td>
		<td>int 音频时长（必填）</td>
		</tr>
		
		<tr>
		<td>msg_body->hash </td>
		<td>String 音频hash值（可选）</td>
		</tr>
		<tr>
		<td>msg_body->fsize</td>
		<td>int 文件大小（字节数）（必填）</td>
		</tr>
	</table>
</div>




#### Example Request

```
msg_type:text
{
	"version": 1, 
	"target_type": "single",
	"target_id": "javen",
	"from_type": "admin",
	"from_id": "fang", 
	"msg_type": "text",
	"msg_body": {
	    "extras": {},
		"text": "Hello, JMessage!"	
	}
}

msg_type:image
{
	"version": 1, 
	"target_type": "single",
	"target_id": "javen",
	"from_type": "admin",
	"from_id": "fang", 
	"msg_type": "image",
	"msg_body": {
	"media_id": "qiniu/image/CE0ACD035CBF71F8",
	"media_crc32":2778919613,
	"width":3840,
	"height":2160,
	"fsize":3328738,
	"format":"jpg"
	}
}

msg_type:voice

{
    "version": 1, 
    "target_type": "single",
    "target_id": "ppppp",
    "from_type": "admin",
     "from_id": "admin_caiyh", 
    "msg_type": "voice",
    "msg_body": {
    "media_id": "qiniu/voice/j/A96B61EB3AF0E5CDE66D377DEA4F76B8",
    "media_crc32":1882116055,
    "hash":"FoYn15bAGRUM9gZCAkvf9dolVH7h",
	"fsize" :12344;
	 "duration": 6
    }
}
```
```
msg_type:custom

{
    "version": 1, 
    "target_type": "single",
    "target_id": "ppppp",
    "from_type": "admin",
     "from_id": "admin_caiyh", 
    "msg_type": "voice",
    "msg_body": {
   		json define yourself
       }
}
```

#### Request Params

+ JSON Object.

+ 遵循协议文档：[IM 消息协议](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/)

+ 此api只能用admin用户发送

#### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 
{"msg_id": 43143728109, "msg_ctime":1493794522950}
```
msg_ctime:  消息创建的时间戳

Error Code

+ 899003    参数错误，Request Body参数不符合要求
+ 899002   用户不存在，target_id或者from_id不存在
+ 899016   from_id 没有权限发送message



### 消息撤回

```
POST /v1/messages/{username}/{msgid}/retract
```
#### Example Request

Request Header 

```
POST /v1/messages/{username}/{msgid}/retract
```
Request Body

N/A

Request Params


| 参数      | 含义                       | 备注   |
| ------- | ------------------------ | ---- |
| msgid | 消息msgid  |      |
| username | 发送此msg的用户名 |      |


#### Example Response 
Response Header

```
HTTP/1.1 204 No Content
Content-Type: application/json; charset=utf-8 
```

Error Code 
	•	855001 超出撤回消息时间 有效撤回时间为消息发出后3分钟之内
	•	855003 撤回消息不存在
	•	855004 消息已经撤回

## 媒体文件下载与上传

#### 文件下载

```
GET /v1/resource?mediaId={mediaId}
```
#### Example Request

Request Header 

```
GET /v1/resource?mediaId={mediaId}
```
Request Body

N/A

Request Params


| 参数      | 含义                       | 备注   |
| ------- | ------------------------ | ---- |
| mediaId | 资源的mediaId，包括用户的avatar字段 |      |


#### Example Response 
Response Header

```
HTTP/1.1 200 no content
Content-Type: application/json; charset=utf-8 
```

Response Data

```
{"url":"http://........."}
```

### 文件上传

```
POST /v1/resource?type=image
```
#### Example Request
文件上传采用form表单上传
curl示例:
图片上传 curl   -F "filename=@/home/test.jpg" https://api.im.jpush.cn/v1/resource?type=image -u "appkey:secret"

文件上传 curl   -F "filename=@/home/test.mp3" https://api.im.jpush.cn/v1/resource?type=file -u "appkey:secret"

语音上传 curl   -F "filename=@/home/test.mp3" https://api.im.jpush.cn/v1/resource?type=voice -u "appkey:secret"

注：文件大小限制8m，暂时只支持图片格式 jpg bmp gif png等


| 参数       | 含义                     | 备注   |
| -------- | ---------------------- | ---- |
| filename | 磁盘本地文件路径               |      |
| type     | 文件类型 支持是"image", "file", "voice" |      |


Response Header  

#### Example Response 

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8 
```
Response Data
图片 Response

```
{"media_id":"qiniu/image/F39AA12204DAB6A2","media_crc32":1338734977,"width":720,"height":1280,"format":"jpg","fsize":52468}
```

+ media_id String  文件上传之后服务器端所返回的key
+ media_crc32 long 文件的crc32校验码
+ width int  图片原始宽度
+ height  int  图片原始高度
+ format String 图片格式
+ fsize int 文件大小 （字节数）
+ hash String 可选，用于crc校验码不存在时的替代的验证

文件 Response 

```
{"media_id":"qiniu/file/j/1BB3B833AEABFF62E883C5CE421867A9","media_crc32":1415584260,"fname":"0839d1c0-48e9-4032-9333-f3691a7d9e48.dmp","fsize":176512,"hash":"FtH0kPT0YI89HAw1K9wv_vVKiNab"}
```

+  media_id String 文件上传之后服务器端所返回的key，用于之后生成下载的url
+  media_crc32 long 文件的crc32校验码
+  hash String 可选，用于crc校验码不存在时的替代的验证
+  fsize int 文件大小（字节数）
+  fname String 发送与接收到的文件名

语音 Response

```
{"media_id":"qiniu/voice/j/9C4312B1EA0FB28337566D1A29A244B5","media_crc32":1882116055,"hash":"FoYn15bAGRUM9gZCAkvf9dolVH7h","format":"m4a","fsize":238105}
```

+  media_id String 文件上传之后服务器端所返回的key，用于之后生成下载的url
+  media_crc32 long 文件的crc32校验码
+  hash String 可选，用于crc校验码不存在时的替代的验证
+  fsize int 文件大小（字节数）
+  format String 源文件格式


## Group对象字段总览

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >含义</th>
			<th >字符长度限制</th>
		</tr>
		<tr >
			<td>name</td>
			<td>群组名称</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>desc</td>
			<td>群组描述</td>
			<td>Byte(0~250)</td>
		</tr>
		<tr >
			<td>owner_username</td>
			<td>群主的username</td>
			<td>Byte(4-128)</td>
		</tr>
		<tr >
			<td>MaxMemberCount</td>
			<td>群组默认500人</td>
			<td></td>
		</tr>
		<tr >
			<td>ctime</td>
			<td>创建时间</td>
			<td></td>
		</tr>
		<tr >
			<td>mtime</td>
			<td>最后修改时间</td>
			<td></td>
		</tr>
		<tr >
			<td>avatar</td>
			<td>群组头像</td>
			<td></td>
		</tr>
	</table>
</div>

<br>

## 群组维护

### 创建群组

	POST /v1/groups/

群组MaxMemberCount（人数限制）定义


Example Request

```
{
    "owner_username": "tom", 
    "name": "群聊天室", 
    "members_username": ["eddie", "annie"], 
    "desc": "运动"
}
```

Request Params

+ owner_username     （必填）群主username
+ name               （必填）群组名字
    - 支持的字符：全部，包括 Emoji。
+ members_username 成员 username
+ avatar           （选填）群组头像，上传接口所获得的media_id 
+ desc               （选填） 群描述 
    - 支持的字符：全部，包括 Emoji。

Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 

{
    "gid":12345, 
    "owner_username": 123456, 
    "name": "display_name", 
    "members_username": [], 
    "desc":"doubi",
    "MaxMemberCount" = 500
}
```

###  获取群组详情

	GET /v1/groups/{Group id}

Request Params

+ Group id 群组ID。由创建群组时分配。

Example Response
```
< HTTP/1.1 200 OK
< Content-Type: application/json
< 

{
      "gid": 12345, 
      "name" : "jpush", 
      "desc" : "push", 
      "appkey" : "dcf71ef5082057832bd44fbd", 
      "MaxMemberCount" : 500,  
      "mtime" : "2014-07-01 00:00:00", 
      "ctime" : "2014-06-05 00:00:00"
}
```

###  更新群组信息
```
PUT /v1/groups/{Group id}
```
Request Params

+ name 群名称
+ desc 群描述
+ avatar 群组头像media_id

```
PUT /v1/groups/{Group id}
```
Request Body

```
{ "the key you want to update" : "the value you want to update" }
```
Example Response

```
HTTP/1.1 204 NO Content
```


### 删除群组

删除某个群组。

该群组的所有成员都会收到群组被解散通知。

	DELETE /v1/groups/{Group id}

Request Params

+ Group id 群组ID。

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

### 更新群组成员

批量增加与删除某 gid 群组的成员。

群组成员将收到增加与删除成员的通知。

	POST /v1/groups/{Group id}/members

Request Params

+ gid 群组ID
+ add        json数组 表示要添加到群组的用户(可选)
+ remove   json数组 表示要从群组删除的用户（可选）
+ 两者至少要有一个

Example Request 

```
{    
    "add":[
        "test1", "test2"
    ],
    "remove":[
        "test3", "test4"
    ]
}
```

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

###  获取群组成员列表

    GET /v1/groups/{Group id}/members/

Request Params

+ Group id 群组ID。

Example Response

+ JsonObject UID数组

```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[ 
	{"username" : "javen", "nickname" : "hello", "avatar" = "/avatar", "birthday" : "1990-01-24 00:00:00", "gender" : 0, "signature" : "orz", "region" : "shenzhen", "address" : "shenzhen", "flag":0} 
]
```
+ flag
    - 0 - 普通群成员
    - 1 - 群主


###  获取某用户的群组列表

    POST /v1/users/{username}/groups/

Request Params

+ username 用户名。

Example Response

+ ctime  群组创建时间
+ mtime 群组最后修改时间 

```
< HTTP/1.1 200 OK
< Content-Type: application/json

[ { "gid": 12345, "name" : "jpush", "desc" : "push", "appkey" : "dcf71ef5082057832bd44fbd", "MaxMemberCount" : 500, "mtime" : "2014-07-01 00:00:00", "ctime" : "2014-06-05 00:00:00"}]
```


### 获取当前应用的群组列表

    GET /v1/groups/?start={start}&count={count}

Request Params

+ start 开始的记录数。
+ count 本次读取的记录数量。最大值为500

Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json

{ "total":1233, 
  "start":1100, 
  "count":1, 
  "groups": 
 [ { "gid": 12345, "name" : "jpush", "desc" : "push", "appkey" : "dcf71ef5082057832bd44fbd", "MaxMemberCount" : 500, "mtime" : "2014-07-01 00:00:00", "ctime" : "2014-06-05 00:00:00"}] } 

```

### 群消息屏蔽

    POST /v1/users/{username}/groupsShield


Request Params

N/A

Example Request Body
```
{   
      "add":[   
         110000101
      ],
      "remove":[   
         1000001111
      ]

}
```
| 参数 | 含义 | 
| -------- | -----: | 
| add |添加群消息屏蔽的gid数组  （可选）| 
|remove | 移除群消息屏蔽的gid数组 （可选）| 



Example Response
```
< HTTP/1.1 204 OK
< Content-Type: application/json
```




## 好友

### 添加好友
	POST  /v1/users/{username}/friends

Request Params

+ json数组 表示要添加的用户名列表 最大限制500个



Example Request 

```
["user01","user02"] 

```
Example Response

```
< HTTP/1.1 201 
< Content-Type: application/json; charset=utf-8 
```

Response Data
N/A

Error Code

+ 899003  Request Body json格式不符合要求，json参数不符合要求；
+ 899002  用户不存在；
+ 899070  已经添加了好友；


### 删除好友
	DELETE  /v1/users/{username}/friends

Request Params

+ json数组 表示要删除的用户名列表 最大限制500个

Example Request 

```
["user01","user02"] 

```
Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8 
```

Response Data
N/A

Error Code

+ 899003  Request Body json格式不符合要求，json参数不符合要求；
+ 899002  用户不存在；

### 更新好友备注
      PUT  /v1/users/{username}/friends

Request Params

+ note_name 表示要添加的好友列表， 格式：Byte(64)
  支持的字符：不包括 "\n" "\r"。
+ others 其他备注信息，格式：Byte(250)
  支持的字符：全部，包括 Emoji。
+ username 用户username；
+ 支持批量修改 最大限制500个



Example Request 

```
[{ "note_name": "new note name", "others": “好友备注文档" ,"username":"user01"}]

```
Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8 
```

Response Data
N/A

Error Code

+ 899003  Request Body json格式不符合要求，json参数不符合要求；
+ 899002  用户不存在；

### 获取好友列表
     GET  /v1/users/{username}/friends

Request Params

N/A 


Example Request 


Example Response

```
< HTTP/1.1 200 NO Content
< Content-Type: application/json; charset=utf-8 
```

Response Data

```
[{"username" : "javen", "nickname" : "hello", "avatar" = "/avatar", "birthday" : "1990-01-24 00:00:00", "gender" : 0, "signature" : "orz", "region" : "shenzhen", "address" : "shenzhen", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00","note_name":"= =","others":"test", "appkey":"pojkasouduioadk"}]
```

Error Code

+ 899003  Request Body json格式不符合要求，json参数不符合要求；
+ 899002  用户不存在；

## 跨应用

### 跨应用管理群组成员
	POST  /v1/cross/groups/{gid}/members
Request Params

+ add  json数组 表示要添加到群组的用户(可选)
+ remove  json数组 表示要从群组删除的用户（可选）
+ appkey 管理用户所属的appkey 必填

add remove两者至少要有一个

Example Request 

```
[{ 
 "appkey":" 4f7aef34fb361292c566a1cd",
 "add": [
 "test1",
 "test2"
 ],
 "remove": [
 "name3",
 "name4"
 ]
}]
```
Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8 
```

Response Data
N/A

备注：当群组没有成员的时候 群会被删除 
Error Code

+ 899003  Request Body json格式不符合要求，json参数不符合要求；
+ 899002  用户不存在；
+ 899012  没有足够的位置添加群成员；
+ 899014  用户不存在于群组；
+ 899011  用户已经存在于群组；

### 跨应用获取群组成员列表

    GET /v1/cross/groups/{Group id}/members/

Request Params

+ Group id 群组ID。

Example Response

+ JsonObject UID数组

```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[ 
	{"username" : "javen", "nickname" : "hello", "avatar" = "/avatar", "birthday" : "1990-01-24 00:00:00", "gender" : 0, "signature" : "orz", "region" : "shenzhen", "address" : "shenzhen", "flag":0, "appkey":"appkey"} 
]
```

+ flag
    - 0 - 普通群成员
    - 1 - 群主

    
### 跨应用获取用户群组
GET /v1/cross/users/{username}/groups

Request Params

+ username 用户名

Example Response


```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[ { "gid": 12345, "name" : "jpush", "desc" : "push", "appkey" : "dcf71ef5082057832bd44fbd","max_member_count" : 200, "mtime" : "2014-07-01 00:00:00", "ctime" : "2014-06-05 00:00:00","appkey":"appkey"}]

```



### 跨应用添加黑名单

```
Put /v1/cross/users/{username}/blacklist
```

Example Request

Request Header 

```
Put /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8  
```

Request Params 

+ username 添加的用户的数组
+ appkey   用户所属的appkey

Request Body

```
 [{
 "appkey":"appkey",
 "usernames":[ "test1", "test2"]
 
 } ] 
```

Example Response 

Response Header 

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8 
```

Response Data

N/A

### 跨应用移除黑名单

```
Delete /v1/cross/users/{username}/blacklist
```

Example Request

Request Header 

```
Delete /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8  
```

Request Params 

+ username 移除的用户的数组
+ appkey   用户所属的appkey

Request Body

```
 [{
 "appkey":"appkey",
 "usernames":[ "test1", "test2"]
 
 } ] 
```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A



### 跨应用黑名单列表

```
Get /v1/cross/users/{username}/blacklist
```

Example Request

Request Header 

```
Get /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8 
```

Request Params

+ username 用户名

Request Body

N/A

Example Response

Response Header 

```
HTTP/1.1 200 
Content-Type: application/json; charset=utf-8   
```

Response Data

```
[{"username" : "javen", "nickname" : "hello", "avatar" = "/avatar", "birthday" : "1990-01-24 00:00:00", "gender" : 0, "signature" : "orz", "region" : "shenzhen", "address" : "shenzhen", "mtime" : "2015-01-01 00:00:00", "ctime" : "2015-01-01 00:00:00", "appkey":"appkey"}]
```

### 跨应用免打扰设置

```
POST  /v1/cross/users/{username}/nodisturb
```

Example Request

Request Header 

```
POST  /v1/cross/users/{username}/nodisturb
Content-Type: application/json; charset=utf-8  
```

Request Params

+ single  单聊免打扰，支持add remove数组 （可选）
+ group   群聊免打扰，支持add remove数组（可选）
+ appkey  目标的appkey


Request Body

```
[ {
   "appkey":"appkey1",    "single":{          "add":[             "username1",          "username2"       ]    },    "group":{          "add":[             110000101       ],       "remove":[             1000001111       ]    } }
]

```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

Error Code

+ 899003 username不合法；
+ 899002 用户不存在；
+ 899051  群组不存在；
+ 899052 设置群组消息屏蔽，设置的群组屏蔽已经打开
+ 899053 设置群组消息屏蔽，设置的群组屏蔽已经关闭

### 跨应用添加好友 

```
POST  /v1/cross/users/{username}/friends
```

Example Request

Request Header 

```
POST  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8  
```

Request Params

+ appkey  用户所属的appkey （必填）
+ users   username的json数组 最多500个（必填）


Request Body

```
 {
   "appkey":"appkey1",    "users":         [            "username1",         "username2"       ]     }


```

Example Response

Response Header

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

### 跨应用删除好友 

```
DELETE  /v1/cross/users/{username}/friends
```

Example Request

Request Header 

```
DELETE  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8  
```

Request Params

+ appkey  用户所属的appkey （必填）
+ users   username的json数组 最多500个（必填）


Request Body

```
 {
   "appkey":"appkey1",    "users":         [            "username1",         "username2"       ]     }


```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

### 跨应用更新好友备注 

```
PUT  /v1/cross/users/{username}/friends
```

Example Request

Request Header 

```
PUT  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8  
```

Request Params

+ appkey  用户所属的appkey （必填）
+ note_name 表示要添加的好友列表， 格式：Byte(64)
  支持的字符：不包括 "\n" "\r"。
+ others 其他备注信息，格式：Byte(250)
  支持的字符：全部，包括 Emoji。  


Request Body

```
[{ "note_name": "new note name", "others": “好友备注文档" ,"username":"user01", "appkey":"appkey"}]


```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

## 敏感词

### 添加敏感词

```
POST  /v1/sensitiveword
```

Example Request

Request Header 

```
POST  /v1/sensitiveword
Content-Type: application/json; charset=utf-8  
```

Request Params
  N/A

Request Body
+ 敏感词数组 一个词长度最多为10，默认支持100个敏感词，[有更高需求可联系商务](https://www.jiguang.cn/accounts/business/form?from=im)

```
["FUCK"] 


```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A


### 修改敏感词

```
PUT  /v1/sensitiveword
```

Example Request

Request Header 

```
PUT  /v1/sensitiveword
Content-Type: application/json; charset=utf-8  
```

Request Params

  N/A

Request Body
+ old_word  旧敏感词
+ new_word  新敏感词

```
{"new_word":"fuck", "old_word":"FUCK"}


```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A


### 删除敏感词

```
DELETE /v1/sensitiveword
```

Example Request

Request Header 

```
DELETE  /v1/sensitiveword
Content-Type: application/json; charset=utf-8  
```

Request Params

   N/A

Request Body
+ word  被删除的敏感词

```
{"word":"fuck"}


```

Example Response

Response Header

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A


### 获取敏感词列表

```
GET /v1/sensitiveword
```

Example Request

Request Header 

```
GET  /v1/sensitiveword?stat={start}&count={count}
Content-Type: application/json; charset=utf-8  
```

Request Params

+ start：起始序号 从0开始
+ count: 查询条数，最多2000

Request Body

N/A

Example Response

Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8   
```

Response Data

```
{
"start": 2,
"count": 1,
"words": [
{
"name": "fuck",
"itime": "itime": "1970-01-17 16:49:11"
}
],
"total": 3
}
```

### 更新敏感词功能状态

```
PUT /v1/sensitiveword/status
```

Example Request

Request Header 

```
PUT  /v1/sensitiveword/status?status=0
Content-Type: application/json; charset=utf-8  
```

Request Params

+ status : 敏感词开关状态， 1表示开启过滤， 0表示关闭敏感词过滤

Request Body

N/A

Example Response

Response Header

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8   
```

Response Data

N/A

### 获取敏感词功能状态

```
GET /v1/sensitiveword/status
```

Example Request

Request Header 

```
GET  /v1/sensitiveword/status
Content-Type: application/json; charset=utf-8  
```

Request Params

N/A

Request Body

N/A

Example Response

Response Header

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8   
```

Response Data

```
 {"status": 1} 
```

## HTTP 返回

HTTP 返回码参考文档：[HTTP-Status-Code](https://docs.jiguang.cn/jpush/server/push/http_status_code/)

### Example Error Response

```
< HTTP/1.1 401 Unauthorized
< Content-Type: application/json
<
{ 
  "error": {
        "code": 899008, 
        "message": "Basic authentication failed"
     }
}
```

## 业务错误码定义

[IM Server ErrorCode](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)


