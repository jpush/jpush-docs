<h1>IM REST API</h1>

极光IM API 为开发者提供 IM 相关功能的 HTTP API。

这类 API 地址统一为（注意与 Push API 不同）：https://api.im.jpush.cn

**HTTP 验证**

验证采用 HTTP Basic 机制，即 HTTP Header（头）里加一个字段（Key/Value对）：

Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

### User对象字段总览

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >含义</th>
			<th >字符长度限制</th>
		</tr>
		<tr >
			<td>username</td>
			<td>用户登陆名</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>password</td>
			<td>登陆密码</td>
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
	</table>
</div>


###  用户注册



#### 注册用户

批量注册用户到极光IM 服务器，一次批量注册最多支持500个用户。

	POST /v1/users/




##### Example Request

```
[{"username": "dev_fang", "password": "password"}, 
 {"username": "dev_fang_", "password": "password"}
] 
```

##### Request Params

JSON Array.

+ username（必填）用户名
	+ 开头：字母或者数字
	+ 字母、数字、下划线
	+ 英文点、减号、@
+ password（必填）用户密码。极光IM服务器会MD5加密保存。

##### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 
[{"username": "dev_fang"  }, 
 {"username": "dev_javen",  "error":{"code":899001,"message":"The user  already exists"}}
] 
```

##### Response Params

JSON Array.

+ username
+ error 某个用户注册出错时，该对象里会有 error 对象，说明错误原因。
	+ 899003   参数错误，Request Body参数不符合要求
	+ 899001   用户已存在


#### Admin

##### **Admin Register 管理员注册**

```
POST /v1/admins/
```
##### Example Request

```
{"username": "dev_fang", "password": "password"}
```

##### Request Params

+ username Byte(4-128) 支持字符
	 + 开头：字母或者数字
	 + 字母、数字、下划线
	 + 英文点、减号, @

+ password Byte(4-128) 字符不限

##### Example Response

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8 
```

##### **GetAdminsListByAppkey  获取应用管理员列表** 

```
GET /v1/admins?start=:start&count=:count
```
##### Example Request

###### Request Header 

```
GET /admins?start=1&count=30
Accept: application/json
```
###### Request Body

```
N/A
```

##### request params
+ start    起始记录位置 从0开始
+ count  查询条数 最多支持500条

##### Example Response

###### Response Header

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```
###### Response Data 

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

### 用户维护

#### 获取用户信息

	GET /v1/users/:username
		
##### Request Params

+ username 用户名。填充到请求路径上。

##### Example Response

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

除了username mtime ctime这三个子段之外，其余字段如果没存json中就有没有相应的key

#### 更新用户信息

	PUT /v1/users/:username

##### Example Request

```
{
	"nickname": "Hello JMessage"
}
```

##### Request Params

+ nickname  （选填）用户昵称
	+ 不支持的字符：英文字符： \n \r\n 
+ birthday    （选填）生日 example: 1990-01-24
	+ yyyy-MM-dd 
+ signature  （选填）签名
	+ 支持的字符：全部，包括 Emoji
+ gender    （选填） 性别
	+ 0 - 未知， 1 - 男 ，2 - 女 
+ region      （选填）地区
	+ 支持的字符：全部，包括 Emoji。
+ address   （选填）地址
	+ 支持的字符：全部，包括 Emoji	


##### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json; charset=utf-8
```

#### 修改密码

```
PUT /v1/users/:username/password
```

##### Request Header 

```
PUT /v1/users/javen/password
```

##### Example Request

```
{
	 "new_password": "654321" 
}
```
##### Request Params

+ new_password （必填）新密码

##### Example Response

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```
##### Response Data
+ N/A

#### 删除用户

	DELETE /v1/users/:username
	
Request Params

+ username 用户名。

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json; charset=utf-8   
```

#### 添加黑名单

```
Put /users/:username/blacklist
```

Example Request

Request Header 

```
Put /users/:username/blacklist
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


#### 移除黑名单

```
Delete /users/:username/blacklist
```

Example Request

Request Header 

```
Delete /users/:username/blacklist
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

#### 黑名单列表

```
Get /users/:username/blacklist
```

Example Request

Request Header 

```
Put /users/:username/blacklist
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


#### 获取用户列表

	GET /v1/users/?start=:start&count=:count

Request Params

+ start 开始的记录数
+ count 要获取的记录个数

Example Response

```
< HTTP/1.1 204 NO CONTENT
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

### 消息相关

#### 发送消息

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
			<td>版本号</td>
		</tr>
		<tr >
			<td>target_type</td>
			<td>发送目标类型 single - 个人，group - 群组</td>
		</tr>
		<tr >
			<td>from_type</td>
			<td>发消息着身份 当前只限admin</td>
		</tr>
		<tr >
			<td>msg_type</td>
			<td>发消息类型 当前只限text</td>
		</tr>
		<tr >
			<td>target_id</td>
			<td>目标id single填username group 填gid</td>
		</tr>
		<tr >
			<td>from_id</td>
			<td>发送者的username</td>
		</tr>
		<tr >
			<td>msg_body</td>
			<td>消息体</td>
		</tr>
		<tr >
			<td>msg_body -> text</td>
			<td>消息内容</td>
		</tr>
		<tr >
			<td>msg_body-> extras</td>
			<td>选填的json对象 开发者可以自定义extras里面的key value	</td>
		</tr>
	</table>
</div>




##### Example Request

```
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
```

##### Request Params

+ JSON Object.

+ 遵循协议文档：[IM 消息协议](../../advanced/im_message_protocol/)

+ 此api只能用admin用户发送

##### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json
< 
{"msg_id": 43143728109  }
```

Error Code

+ 899003    参数错误，Request Body参数不符合要求
+ 899002   用户不存在，target_id或者from_id不存在
+ 899016   from_id 没有权限发送message


### Group对象字段总览

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
			<td>level</td>
			<td>群组的等级 1 - 最大人数40，2 - 最大人数100，3 - 最大人数 200， 4 最大人数 500</td>
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
	</table>
</div>

<br>

### 群组维护

#### 创建群组

	POST /v1/groups/
	
群组Level（人数限制）定义

+ 	Level_1 40人
+ 	Level_2 100人
+  	Level_3 200人

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
	+ 支持的字符：全部，包括 Emoji。
+ members_username 成员 username
+ desc               （必填） 群描述 
	+ 支持的字符：全部，包括 Emoji。

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
    "level" = 3, 
    "mtime" = "2014-07-01 00:00:00", 
    "ctime"="2014-06-05 00:00:00"
}
```

####  获取群组详情

	GET /v1/groups/:gid

Request Params

+ gid 群组ID。由创建群组时分配。

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
      "level" : 3,  
      "mtime" : "2014-07-01 00:00:00", 
      "ctime" : "2014-06-05 00:00:00"
}
```

####  更新群组信息
```
PUT /v1/groups/{gid}
```
Request Params

+ name 群名称
+ desc 群描述

```
PUT /v1/groups/{gid}
```
Request Body

```
{ "the key you want to update" : "the value you want to update" }
```
Example Response

```
HTTP/1.1 204 NO Content
```


#### 删除群组

删除某 gid 的群组。

该群组的所有成员都会收到群组被解散通知。

	DELETE /v1/groups/:gid

Request Params

+ gid 群组ID。

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

#### 更新群组成员

批量增加与删除某 gid 群组的成员。

群组成员将收到增加与删除成员的通知。

	POST /v1/groups/{gid}/members

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

####  获取群组成员列表

    GET /v1/groups/{gid}/members/

Request Params

+ gid 群组ID。

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
	+ 0 - 普通群成员
	+ 1 - 群主


####  获取某用户的群组列表

    GET /v1/users/:username/groups/

Request Params

+ username 用户名。

Example Response

+ ctime  群组创建时间
+ mtime 群组最后修改时间 

```
< HTTP/1.1 200 OK
< Content-Type: application/json

[ { "gid": 12345, "name" : "jpush", "desc" : "push", "appkey" : "dcf71ef5082057832bd44fbd", "level" : 3, "mtime" : "2014-07-01 00:00:00", "ctime" : "2014-06-05 00:00:00"}]
```


#### 获取当前应用的群组列表

    GET /v1/groups/?start=:start&count=:count

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
 [ { "gid": 12345, "name" : "jpush", "desc" : "push", "appkey" : "dcf71ef5082057832bd44fbd", "level" : 3, "mtime" : "2014-07-01 00:00:00", "ctime" : "2014-06-05 00:00:00"}] } 

```


### HTTP 返回

HTTP 返回码参考文档：[HTTP-Status-Code](../server/http_status_code)

#### Example Error Response

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

#### 业务错误码定义

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th style="text-align:center;" >Code</th>
			<th >HTTP</th>
			<th >Error Message</th>
			<th >说明</th>
		</tr>
		<tr >
			<td style="text-align:center;">899000</td>
			<td>500</td>
			<td>Server internal error</td>
			<td>系统内部错误</td>
		</tr>
		<tr >
			<td style="text-align:center;">899001</td>
			<td>403</td>
			<td>User exists</td>
			<td>用户已存在</td>
		</tr>
		<tr >
			<td style="text-align:center;">899002</td>
			<td>403</td>
			<td>No sush user</td>
			<td>用户不存在</td>
		</tr>
		<tr >
			<td style="text-align:center;">899003</td>
			<td>400</td>
			<td>Parameter invalid!</td>
			<td>请求参数不合法 </td>
		</tr>
		<tr >
			<td style="text-align:center;">899004</td>
			<td>403</td>
			<td>Password error</a></td>
			<td>密码错误</td>
		</tr>
		<tr >
			<td style="text-align:center;">899005</td>
			<td>403</td>
			<td>Invalid uid </td>
			<td>uid 不存在</td>
		</tr>
		<tr >
			<td style="text-align:center;">899006</td>
			<td>403</td>
			<td>gid invalid</td>
			<td>gid 不存在</td>
		</tr>
		<tr >
			<td style="text-align:center;">899007</td>
			<td>401</td>
			<td>Missing authen info.</td>
			<td>校验信息为空</td>
		</tr>
		<tr >
			<td style="text-align:center;">899008</td>
			<td>401</td>
			<td>Basic authentication failed.</td>
			<td>校验失败</td>
		</tr>
		<tr >
			<td style="text-align:center;">899009</td>
			<td>400</td>
			<td>appkey not exists</td>
			<td>appkey不存在</td>
		</tr>
		<tr >
			<td style="text-align:center;">899010</td>
			<td>400</td>
			<td>Delete fail</td>
			<td>删除失败</td>
		</tr>
		<tr >
			<td style="text-align:center;">899011</td>
			<td>400</td>
			<td>Repeat to add the members</td>
			<td>重复添加</td>
		</tr>
		<tr >
			<td style="text-align:center;">899012</td>
			<td>403</td>
			<td>no enough space for members</td>
			<td>群组剩余位置不够</td>
		</tr>
		<tr >
			<td style="text-align:center;">899013</td>
			<td>403</td>
			<td>user list is bigger than 500 </td>
			<td>注册列表过长</td>
		</tr>
		<tr >
			<td style="text-align:center;">899014</td>
			<td>403</td>
			<td>add success remove fail but there are user not exit in this group</td>
			<td>移除成员失败</td>
		</tr>
		<tr >
			<td style="text-align:center;">899015</td>
			<td>403</td>
			<td>user 's group are 100 can not continue</td>
			<td>用户加入讨论组达到上限</td>
		</tr>
		<tr >
			<td style="text-align:center;">899016</td>
			<td>403</td>
			<td>No authority to send message</td>
			<td>用户没有权限</td>
		</tr>
		<tr >
			<td style="text-align:center;">899017</td>
			<td>403</td>
			<td>there are usernames exist in blacklist</td>
			<td>用户已经被添加进黑名单</td>
		</tr>
		<tr >
			<td style="text-align:center;">899018</td>
			<td>403</td>
			<td>admin can not be added into blacklist</td>
			<td>管理员不能被添加进黑名单</td>
		</tr>
		<tr >
			<td style="text-align:center;">899019</td>
			<td>403</td>
			<td>here are usernames not exist in blacklist</td>
			<td>用户不存在黑名单中</td>
		</tr>
		<tr >
			<td style="text-align:center;">899030</td>
			<td>503</td>
			<td>Server response time out, please try again later</td>
			<td>系统繁忙，稍后重试</td>
		</tr>
	</table>
</div>



### 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)

