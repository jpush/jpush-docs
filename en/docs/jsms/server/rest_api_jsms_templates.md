# SMS Template API

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>Support for creating, modifying, querying, and deleting SMS signatures</li>
</ul>
</div>
</br>

## HTTP Authentication

> Use HTTP Basic Authentication to do access authorization. In this way, the entire API request can be completed by common HTTP tools such as curl, browser plugins, etc.

A field (Key/Value pair) is added in the HTTP Header：

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret), that is: appKey plus a colon, plus string assembled by masterSecret, and then do a base64 conversion. appKey, masterSecret can be viewed in the application settings of console.

## Create Template API

### Function Description

+ Create SMS template

### Call Address

+ POST https://api.sms.jpush.cn/v1/templates

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/templates -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "template": "您好，您的验证码是{{code}}，2分钟内有效！",
    "type": 1,
    "ttl": 120,
    "remark": "此模板用于用户注册"
}'
```

### Parameters

|KEY|REQUIRE|DESCRIPTION
|----|----|----
|template|TRUE|Template content. Note: The contents of SMS, according to operator’s regulations, cannot exceed 350 characters
|type|TRUE|Template type, 1 for verification code, 2 for notification, 3 for marketing
|ttl|FALSE|Validity period of verification code, in seconds (must be transmitted when the template type is 1)
|remark|FALSE|Remarks, length is limited to 500 characters

### Return Example

#### Successful Request

```json
{"temp_id": 37582}
```

#### Failed Request

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Modify Template API

### Function Description

+ Modify the template that failed the audit and submit the audit again

### Call Address

+ PUT https://api.sms.jpush.cn/v1/templates/{temp_id}

### Request Example

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "temp_id": 37582,
    "template": "您好，您的验证码是{{code}}，5分钟内有效！",
    "type": 1,
    "ttl": 300,
    "remark": "此模板用于用户注册"
}'
```

### Parameters

|KEY|REQUIRE|DESCRIPTION
|----|----|----
| temp_id | TRUE | Template ID
| template | TRUE | Template content. Note: The contents of SMS, according to operator’s regulations, cannot exceed 350 characters
| type | TRUE | Template type, 1 for verification code, 2 for notification, 3 for marketing
| ttl | FALSE | Validity period of verification code, in seconds (must be transmitted when the template type is 1)
| remark | FALSE | Remarks, length is limited to 500 characters

### Return Example

#### Successful Request

```json
{"temp_id": 37582}
```

#### Failed Request

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Query Template API

### Function Description

+ Query SMS template

### Call Address

+ GET https://api.sms.jpush.cn/v1/templates/{temp_id}

### Request Example

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```json
{
    "temp_id": 37582,
    "template": "您好，您的验证码是{{code}}，5分钟内有效！",
    "type": 1,
    "ttl": 300,
    "remark": "此模板用于用户注册",
    "status": 1     // 状态，0为审核中，1为审核通过，2为审核不通过
}
```

#### Failed Request

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Delete Template API

### Function Description

+ Delete SMS template

### Call Address

+ DELETE https://api.sms.jpush.cn/v1/templates/{temp_id}

### Request Example

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/templates/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```
HTTP/1.0 200
  Content-Type: application/json
  Content-Length: 0
```

#### Failed Request

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Return Code

|HTTP CODE| CODE| MESSAGE  | DESC|
|:--- |:--- |:--- |:----
| 200 | 50000 | success | Successful Request
| 400 | 50001 | missing auth | auth is empty
| 401 | 50002 | auth failed | Authentication of Auth failed
| 400 | 50003 | missing body | body is empty
| 403 | 50007 | invalid body | body is invalid
| 403 | 50008 | no sms code auth | Not open SMS service
| 403 | 50013 | invalid temp_id | Template ID is empty
| 404 | 50016 | api not found | API does not exist
| 415 | 50017 | media not supported | Media type is not supported
| 405 | 50018 | request method not support | Request method is not supported
| 500 | 50019 | server error | Server exception
| 403 | 50025 | wrong template type | Wrong template type
| 403 | 50037 | has black word | Template content contains sensitive words
| 403 | 50041 | invalid ttl value | Ttl is invalid and must be greater than 0 and no more than 86400 seconds (24 hours)
| 403 | 50042 | template is empty | Template content is empty
| 403 | 50043 | template too long | Content of the template is too long and the length of the signature is limited to 350 characters
| 403 | 50044 | template parameter invalid | Template Parameters is invalid
| 403 | 50045 | remark too long | The comment is too long and the length is limited to 500 characters
| 403 | 50046 | signature not set | The application does not have a signature, please set the signature first
| 403 | 50047 | modify template not allow | Only the template that failed the audit is allowed to modify
