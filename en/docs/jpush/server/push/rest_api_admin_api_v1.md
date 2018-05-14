## Admin API V1

The JPush Admin API provides the developers with the ability to create/delete an app, upload a certificate, and more.

The unified API address is: https://admin.jpush.cn/v1/

**Note: The Admin API is not yet fully open. To experience this feature, please** [contact us](https://www.jiguang.cn/contact).

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Definition of request header：</p>
<ul style="margin-bottom: 0;">
    <li>The value of HTTP Header Authorization: Basic base64_auth_string</li>
    <li>The generation rule of base64_auth_string is: base64(dev_key:dev_secret), dev_key, and dev_secret. Please visit the developer account page of official website to obtain</li>
    <li>Note that the dev_key is separated from the dev_secret by a ":" colon</li>
</ul>
</div>

Please refer to the relevant specification document: [Basic Authentication of HTTP](https://en.wikipedia.org/wiki/Basic_access_authentication).

## Create a Jiguang app

### Function Description

Create an app under the developer account.

### Call Address

POST https://admin.jpush.cn/v1/app

### Request Example

```
curl  -X POST -v https://admin.jpush.cn/v1/app
      -H 'Content-type: application/json'
      -u 'd61988533983cbc7a2eceb0a:fb3ea2a1830d9731ef202a8f'
      -d '{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}'

> POST /v1/app HTTP/1.1
> Authorization: Basic ZDYxOTg4NTMzOTgzY2JjN2EyZWNlYjBhOmZiM2VhMmExODMwZDk3MzFlZjIwMmE4Zg==
```

**Request Parameters**

The request parameter is an App object, expressed in JSON format, and containing the field information as follows：

Parameter name  | Type  | Is it necessary   | Description
---             | ---   | ---               | ---
app_name        | string | Yes              | Application Name
android_package | string | Yes              | Name of Application package (Android)
group_name      | string | No               | Name of Application group

```
{"app_name":"myapp","android_package":"cn.jpush.app","group_name":"groupOne"}
```

### Response Example

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"app_key":"dc51b6829206b2736e7e6d63","is_new_created":true,"android_package":"cn.jpush.app"}
```

**Response Parameters**

Parameter Name  | Description | Description
---------------- | ----------- | ------------
app_key          |string        | Application ID
android_package  |string        |Name of Application package (Android)
is_new_created   |boolean       |

## Delete an app

### Function Description

Delete the specified app under the developer account

### Call Address

POST https://admin.jpush.cn/v1/app/{appKey}/delete

### Request Example

```
curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/delete
     -X POST
     -u devKey:devSecret
```

### Response Example

```
错误:{"error":{"code":1015,"message":"app delete fail"}}
正确:{"success":"Synchronized success"}
```

## Upload Certificates

### Function Description

Developers can upload certificates to the corresponding Jiguang app by using this API

### Call Address

POST https://admin.jpush.cn/v1/app/{appKey}/certificate

### Request Example

```
curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/certificate
     -F "devCertificatePassword=your dev certificate passowrd"
     -F "proCertificatePassword=your pro certificate passowrd"
     -F "devCertificateFile=@your dev certificate file"
     -F "proCertificateFile=@your pro certificate file"
     -u '{devKey}:{devSecret}'
```

If there is no dev certificate or pro certificate, the corresponding -F parameter and corresponding password are not required. For example: dev certificate only.

```
curl https://admin.jpush.cn/v1/app/ffbb0932c267d938941e470b/certificate
     -F "devCertificatePassword=your dev certificate passowrd"
     -F "devCertificateFile=@your dev certificate file"
     -u 'devKey:devSecret'
```

**Request Parameters**

Parameter name          | Types         | Description
----------------------  | ------------  | ----------
devCertificatePassword  |string         |Dev certificate password
proCertificatePassword  |string         |Pro certificate password
devCertificateFile      |file           |Dev certificate file
proCertificateFile      |file           |Pro certificate file

### Response Example

```
错误:{"error":{"code":1012,"message":"certificate invalid"}}
正确:{"success":"Synchronized success"}
```

**Response Parameters**

Parameter name  | Description| Description
---------------- | ----------- | ------------
code             |int          | Return code
message          |string       | Response information

## Error Code and Error Message

HTTP Status Code | Error Code | Description
---------------- | ----------- | ------------
200 | | Success!
200 | 1010 | Certificate already exists
200 | 1012 | Certificate is illegal
200 | 1013 | Appkey is illegal
200 | 1014 | There is no certificate file in the parameters
200 | 1015 | App deleting failed
405 | 4001 | Only HTTP Post methods are supported
400 | 4002 | Request parameter is empty
400 | 4003 | Illegal request parameters
401 | 4004 | Permission verification error: dev_key does not exist
401 | 4005 | Permission verification error: dev_secret is incorrect
401 | 4007 | Permission are not opened
500 | 10 | System error

Reference Document: [HTTP-Status-Code](http_status_code)
