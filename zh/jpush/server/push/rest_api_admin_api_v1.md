# Admin API V1
JPush Admin API 提供给开发者操创建/删除 app，上传证书等功能。  
这类 API 地址统一为： https://admin.jpush.cn/v1/

**注：Admin API 目前尚未完全开放，如需体验该功能，请**[联系我们](https://www.jiguang.cn/contact) 。


<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>请求头定义：</p>
<ul style="margin-bottom: 0;">
<li>HTTP Header Authorization 的值：Basic base64_auth_string;</li>
<li>base64_auth_string 生成规则是：base64(dev_key:dev_secret), dev_key 及 dev_secret 请登录官网在开发者帐号页面获取;</li>
<li>留意 dev_key 与 dev_secret 中间使用 ":" 冒号隔开。</li>
</ul>
</div>
请参考相关规范文档：[HTTP基本认证](http://zh.wikipedia.org/zh/HTTP基本认证)。

## 创建极光 app

### 功能说明  
在开发者账号下创建一个 app

### 调用地址

POST https://admin.jpush.cn/v1/app

### 请求示例

```
	curl  -X POST -v https://admin.jpush.cn/v1/app
		  -H 'Content-type: application/json'
		  -u 'd61988533983cbc7a2eceb0a:fb3ea2a1830d9731ef202a8f'
		  -d '{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}'

	> POST /v1/app HTTP/1.1
	> Authorization: Basic ZDYxOTg4NTMzOTgzY2JjN2EyZWNlYjBhOmZiM2VhMmExODMwZDk3MzFlZjIwMmE4Zg==
```



**请求参数**

请求参数为一个 App 对象，以 JSON 格式表达，包含的字段信息如下：


参数名称           | 类型          |是否必需  |描述
---------------- | ------------  | -------- | ------------
app_name         |string 	      | 是       |应用名称
android_package  |string 	      | 是       |应用包名（Android）
group_name       |string 	      | 否       |应用分组名称

```
	{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}
```

### 响应示例

```
	< HTTP/1.1 200 OK
	< Content-Type: application/json
	{"app_key":"dc51b6829206b2736e7e6d63","is_new_created":true,"android_package":"cn.jpush.app"}
```

**响应参数**

参数名称          | 描述         |描述
---------------- | ----------- | ------------
app_key          |string 	    | 应用标识
android_package  |string 	    | 应用包名（Android）
is_new_created   |boolean 	    |

## app删除

### 功能说明

删除开发者账号下的指定 app

### 调用地址

POST https://admin.jpush.cn/v1/app/{appKey}/delete

### 请求示例

```
    curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/delete
         -X POST
         -u devKey:devSecret
```

### 响应示例

```
    错误:{"error":{"code":1015,"message":"app delete fail"}}
    正确:{"success":"Synchronized success"}
```


## 证书上传

### 功能说明

使用该 API 开发者可上传证书到对应的极光 app 

### 调用地址

POST https://admin.jpush.cn/v1/app/{appKey}/certificate

### 请求示例

```
    curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/certificate
         -F "devCertificatePassword=your dev certificate passowrd"
         -F "proCertificatePassword=your pro certificate passowrd"
         -F "devCertificateFile=@your dev certificate file"
         -F "proCertificateFile=@your pro certificate file"
         -u '{devKey}:{devSecret}'
```

   如果没有dev证书或pro证书,则不需要相应的-F参数及相应password，比如: 只有dev证书。

```
    curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/certificate
         -F "devCertificatePassword=your dev certificate passowrd"
         -F "devCertificateFile=@your dev certificate file"
         -u 'devKey:devSecret'
```

**请求参数**

参数名称                 | 类型           |描述
----------------------  | ------------  | ----------
devCertificatePassword  |string 	    |dev 证书密码
proCertificatePassword  |string 	    |pro 证书密码
devCertificateFile      |文件 	        |dev 证书文件
proCertificateFile      |文件 	        |pro 证书文件

### 响应示例

```
    错误:{"error":{"code":1012,"message":"certificate invalid"}}
    正确:{"success":"Synchronized success"}
```

**响应参数**

参数名称          | 描述         |描述
---------------- | ----------- | ------------
code             |int 	       | 返回码
message          |string 	   | 响应信息


## 错误码及错误信息

HTTP Status Code| Error Code|描述|
----- | ----- | ----- |
200| |Success!|
200|1010|证书已存在|
200|1012|证书不合法|
200|1013|appkey 不合法|
200|1014|参数中没有证书文件|
200|1015|app删除失败|
405|4001|只支持 HTTP Post 方法|
400|4002|请求参数为空|
400|4003|请求参数非法|
401|4004|权限校验错误: dev_key 不存在|
401|4005|权限校验错误: dev_secret 不正确|
401|4007|未开通权限|
500|10|系统错误|

参考文档：[HTTP-Status-Code](http_status_code)