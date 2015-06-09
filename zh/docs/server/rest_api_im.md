<h1>IM REST API</h1>

极光IM API 为开发者提供 IM 相关功能的 HTTP API。

这类 API 地址统一为（注意与 Push API 不同）：https://api.im.jpush.cn


###  用户注册与登录

#### 注册用户

批量注册用户到极光IM 服务器，一次批量注册最多支持500个用户。

	POST /v1/users/

##### Example Request

```
[{"username": "dev_fang", "password": "password"}, 
 {"username": "dev_fang", "password": "password"}
] 
```

##### Request Params

JSON Array.

+ username 用户名
+ password 用户密码。极光IM服务器会MD5加密保存。

##### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 
[{"username": "dev_fang",  }, 
 {"username": "dev_javen",  "error":{"code":8001,"message":"The user  already exists"}}
] 
```

##### Response Params

JSON Array.

+ username
+ error 某个用户注册出错时，该对象里会有 error 对象，说明错误原因。


### 消息相关

#### 发送消息

暂未开放。

	POST /v1/messages

##### Example Request

```
{
	"version": 1, 
	"target_type": "single",
	"target_id": "javen",
	"target_name": "Javen Fang",
	"from_type": "user",
	"from_id": "fang", 
	"from_name": "Fang Javen", 
	"create_time": 135431243278,
	"msg_type": "text",
	"msg_body": {
	    "extras": {},
		"text": "Hello, JMessage!"	
	}
}
```

##### Request Params

JSON Object.

遵循协议文档：[IM 消息协议](../../client/im_message_protocol/)

##### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json
< 
{"msg_id": 43143728109  }
```

### 用户维护

#### 获取用户信息

	GET /v1/users/:username
		
##### Request Params

+ username 用户名。填充到请求路径上。

##### Example Response

```
{
	"username" : "test", 
	"nickname" : "hello", 
	"star" : 2, 
	"avatar" = "/avatar/path", 
	"birthday" : "1990-01-24 00:00:00", 
	"gender" : 0, 
	"signature" : "orz", 
	"region" : "shenzhen", 
	"address" : "shenzhen", 
	"mtime" : "2015-01-01 00:00:00", 
	"ctime" : "2015-01-01 00:00:00"}
```

#### 更新用户信息

	PUT /v1/users/:username

##### Example Request

```
{
	"nickname": "Hello JMessage", 
	"avatar" = "/avatar/path/new"
}
```

##### Request Params

+ username 用户名。
+ BODY JSON Object。根据相应 KEY 更新用户信息。

##### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

#### 删除用户

	DELETE /v1/users/:username
	
Request Params

+ username 用户名。

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
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
    "users":["tom", "eddie", "annie"]
}
```


### 群组维护

#### 创建群组

	POST /v1/groups/

Example Request

```
{
    “owner_username”: "tom", 
    "group_name": "泡否", 
    "members_username": ["eddie", "annie"], 
    "group_desc": "你懂的。。。"
}
```

Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 

{
    "gid": 13579,
    "group_name": "泡否", 
    "group_desc": "你懂的。。。",
    "appkey": "dcf71ef5082057832bd44fbd",
    "level": 3,
    "mtime": "2014-07-01 00:00:00",
    "ctime": "2014-07-01 00:00:00"
}
```

#### 获取群组详情

	GET /v1/groups/:gid

Request Params

+ gid 群组ID。由创建群组时分配。

Example Response
```
< HTTP/1.1 200 OK
< Content-Type: application/json
< 

{
    "gid": 13579,
    "group_name": "泡否", 
    "group_desc": "你懂的。。。",
    "appkey": "dcf71ef5082057832bd44fbd",
    "level": 3,
    "mtime": "2014-07-01 00:00:00",
    "ctime": "2014-07-01 00:00:00"
}
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

	POST /v1/groups/:gid/members

Request Params

+ gid 群组ID。

Example Request 

```
{    
    "add":[
        "test1", "test2"
    ]
    "remove":[
        "test3", "test4"
    ]
```

Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

#### 获取群组成员列表

    GET /v1/groups/:gid/members/

Request Params

+ gid 群组ID。

Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json

[
    {"username":"tom", "flag":0, "ctime":"2015-03-20 22:00:13"}, 
    {"username":"annie", "flag":1, "ctime":"2015-03-11 01:12:00"}
]
```

#### 获取某用户的群组列表

    GET /v1/users/:username/groups/

Request Params

+ username 用户名。

Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json

[111, 222, 333]
```

#### 获取当前应用的群组列表

    GET /v1/groups/?start=:start&count=:count

Request Params

+ start 开始的记录数。
+ count 本次读取的记录数量。

Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json

{
    "total": 1322,
    "start": 1100,
    "count": 100,
    "groups":[111, 222, 333]
}

```


### HTTP 返回

HTTP 返回码参考文档：[HTTP-Status-Code](../http_status_code)

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
			<th style="padding: 0 5px;text-align:center;" >Code</th>
			<th style="padding: 0 5px;" >HTTP</th>
			<th style="padding: 0 5px;" >Error Message</th>
			<th style="padding: 0 5px;" >说明</th>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899000</td>
			<td style="padding: 0 5px;">500</td>
			<td style="padding: 0 5px;">Server internal error</td>
			<td style="padding: 0 5px;">系统内部错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899001</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">User exists</td>
			<td style="padding: 0 5px;">用户已存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899002</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">No sush user</td>
			<td style="padding: 0 5px;">用户不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899003</td>
			<td style="padding: 0 5px;">400</td>
			<td style="padding: 0 5px;">Parameter invalid!</td>
			<td style="padding: 0 5px;">请求参数不合法 </td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899004</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">Password error</a></td>
			<td style="padding: 0 5px;">密码错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899005</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">Invalid uid </td>
			<td style="padding: 0 5px;">uid 不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899006</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">gid invalid</td>
			<td style="padding: 0 5px;">gid 不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899007</td>
			<td style="padding: 0 5px;">401</td>
			<td style="padding: 0 5px;">Missing authen info.</td>
			<td style="padding: 0 5px;">校验信息为空</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899008</td>
			<td style="padding: 0 5px;">401</td>
			<td style="padding: 0 5px;">Basic authentication failed.</td>
			<td style="padding: 0 5px;">校验失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899009</td>
			<td style="padding: 0 5px;">400</td>
			<td style="padding: 0 5px;">appkey not exists</td>
			<td style="padding: 0 5px;">appkey不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899010</td>
			<td style="padding: 0 5px;">400</td>
			<td style="padding: 0 5px;">Delete fail</td>
			<td style="padding: 0 5px;">删除失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800011</td>
			<td style="padding: 0 5px;">400</td>
			<td style="padding: 0 5px;">Repeat to add the members</td>
			<td style="padding: 0 5px;">重复添加</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800012</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">no enough space for members</td>
			<td style="padding: 0 5px;">群组剩余位置不够</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899013</td>
			<td style="padding: 0 5px;">403</td>
			<td style="padding: 0 5px;">user list is bigger than 500 </td>
			<td style="padding: 0 5px;">注册列表过长</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">899030</td>
			<td style="padding: 0 5px;">503</td>
			<td style="padding: 0 5px;">Server response time out, please try again later</td>
			<td style="padding: 0 5px;">系统繁忙，稍后重试</td>
		</tr>
	</table>
</div>



### 相关文档

+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM 消息协议](../../advanced/im_message_protocol/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)

