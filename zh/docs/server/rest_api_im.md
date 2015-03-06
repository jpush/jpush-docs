<h1>IM REST API</h1>

JPush IM API 为开发者提供 IM 相关功能。

这类 API 地址统一为（注意与 Push API 不同）：https://im.api.jpush.cn

### API 访问鉴权

参考统一文档。

###  用户注册与登录

#### 注册用户

批量注册用户到 JPush IM 服务器。

	POST /v1/users/

##### Example Request

```
[{"username": "dev_fang", "password": "password"}, 
 {"username": "dev_fang", "password": "password"}, 
] 
```

##### Request Params

JSON Array.

+ username 用户名
+ password 密码

##### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
< 
[{"username": "dev_fang",  }, 
 {"username": "dev_javen",  "error":{"code":8001,"message":"user exit"}}, 
] 
```
##### Response Params

JSON Array.

+ username
+ error 某个用户注册出错时，该对象里会有 error 对象，说明错误原因。

### 消息相关

#### 发送消息

	POST /messages
	
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
	"create_time": "2015-02-12 15:49 09",
	
	"msg_type": "text",
	"msg_body": {
		"content": "Hello, JPush IM!"		}}
```
##### Request Params

遵循协议文档：[IM 消息协议](../../client/im_message_protocol/)

##### Response Code

+ 200 发送消息成功
+ 400 消息体异常


### 用户维护

#### 获取用户信息

	GET /users/{username}
		
##### Request Params

+ username 用户名。填充到请求路径上。##### Example Response

```
{
	"user_name" : "test", 
	"nickname" : "hello", 
	"star" : 2, 
	"avatar" = "/avatar", 
	"birthday" : "1990-01-24 00:00:00", 
	"gender" : 0, 
	"signature" : "orz", 
	"region" : "shenzhen", 
	"address" : "shenzhen", 
	"mtime" : "2015-01-01 00:00:00", 
	"ctime" : "2015-01-01 00:00:00"}
```

#### 更新用户信息

	PUT /users/{username}
		
##### Example Request

##### Response Code

+ 200 OK

#### 删除用户

	DELETE /users/

#### 获取用户列表（分页）

	GET /users/?start={number}&count={number}


		

### 群组维护

#### 创建群组

	POST /groups/

#### 获取群组详情

	GET /groups/{gid}	
#### 添加群组成员

	POST /groups/{gid}/members

#### 删除群组成员

	DELETE /groups/{gid}/members

#### 删除群组

	DELETE /groups/{gid}
	

### HTTP 返回

HTTP 返回码参考文档：[HTTP-Status-Code](../http_status_code)

#### Example Error Response

```
< HTTP/1.1 401 Unauthorized
< Content-Type: application/json
<
{ 
  "error": {
        "code": 3001, 
        "message": "Basic authentication failed"
     }
}
```

#### 业务错误码定义

| Code | 描述	| 详细解释 |
| ---- | ---- | ---- |
|10|系统内部错误||


### 相关文档

+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [JPush IM 指南](../../guideline/jpush_im_guide/)
+ [IM 消息协议](../../client/im_message_protocol/)
