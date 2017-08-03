# App-Create-API
## 创建App
### 功能说明

方便开发者创建App

### 调用地址

POST https://admin.jpush.cn/v1/app

### 请求示例

	curl  -X POST -v https://admin.jpush.cn/v1/app
		  -H 'Content-type: application/json'
		  -u 'd61988533983cbc7a2eceb0a:fb3ea2a1830d9731ef202a8f'
		  -d '{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}'
		  
	> POST /v1/app HTTP/1.1
	> Authorization: Basic ZDYxOTg4NTMzOTgzY2JjN2EyZWNlYjBhOmZiM2VhMmExODMwZDk3MzFlZjIwMmE4Zg==
	
	
### 响应示例

	< HTTP/1.1 200 OK
	< Content-Type: application/json
	{"app_key":"dc51b6829206b2736e7e6d63","is_new_created":true,"android_package":"cn.jpush.app"}
	
	
## 请求参数

### 请求头

HTTP Header Authorization 的值：Basic base64_auth_string

+ base64_auth_string 生成规则是：base64(dev_key:dev_secret),dev_key及dev_secret请登录官  网的帐号页面获取。
+ 留意 dev_key与 dev_secret中间使用 ":" 冒号隔开
+ 请参考相关规范文档：[HTTP基本认证](http://zh.wikipedia.org/zh/HTTP基本认证)。

### 请求体

请求参数为一个App对象，以 JSON 格式表达，包含的字段信息如下：


参数名称           | 类型          |是否必需  |描述
---------------- | ------------  | -------- | ------------
app_name         |string 	      | 是       |应用名称
android_package  |string 	      | 是       |应用包名(Android)
group_name       |string 	      | 否       |应用分组名称

	{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}

## 响应参数

参数名称          | 描述         |描述
---------------- | ----------- | ------------
app_key          |string 	    | 应用标识
android_package  |string 	    | 应用包名(Android)
is_new_created   |boolean 	    | 


## HTTP状态码及业务错误码

###HTTP 状态码

参考文档：[HTTP-Status-Code]()

HTTP Status Code| Code|描述|详细解释|提示信息
----- | ----- | ----- | ----- |------
200||OK|Success!|
405|4001|只支持 HTTP Post 方法|不支持 Get 方法。|Get HTTP method is not allowed
400|4002|请求参数非法|必须改正。|Request parameter {param} is null or empty
400|4003|请求参数非法|必须改正，目前仅校验 android_package。|Request parameter {param} is null or empty
401|4004|权限校验错误: dev_key 不存在|必须改正，请输入正确的dev_key。|Authentication failed: dev_key does not exist
401|4005|权限校验错误: dev_secret 不正确|必须改正，请输入正确的dev_secret。|Authentication failed: dev_key and dev_secret are not matched
401|4006|验证参数非法|不是一个合法的 HTTP Basic 验证串|Authentication failed: it is not a valid authorization string
500|10|系统错误||System error





