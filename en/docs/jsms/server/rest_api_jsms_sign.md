# SMS Signing API

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

## Create Signature API

### Function Description

+ Create SMS Signature

### Call Address

+ POST https://api.sms.jpush.cn/v1/sign

### Request Example

Please note that the content-type is multipart/form-data.

```
curl -X POST \
  https://api.sms.jpush.cn/v1/sign \
  -u '7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1' \
  -H 'content-type: multipart/form-data;' \
  -F 'sign=申请的签名'
```

### Parameter

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|sign|TRUE|Signature content|
|image0|FALSE|Signature review with picture|
|image1|FALSE|Signature review with picture|
|image2|FALSE|Signature review with picture|
|image3|FALSE|Signature review with picture|

### Return Example

#### Successful Request

```
{"sign_id": 37582}
```

#### Failed Request

```
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Modify Signature API

### Function Description

+ Modify the signature that failed the audit and submit the audit again

### Call Address

+ PUT https://api.sms.jpush.cn/v1/sign/{sign_id}

### Request Example

```
curl -X POST \
  https://api.sms.jpush.cn/v1/sign/37582 \
  -u '7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1' \
  -H 'content-type: multipart/form-data;' \
  -F 'sign=修改的签名'
```

### Parameter

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|sign|TRUE|Signature content|
|image0|FALSE|Signature review with picture|
|image1|FALSE|Signature review with picture|
|image2|FALSE|Signature review with picture|
|image3|FALSE|Signature review with picture|

### Return Example

#### Successful Request

```
{"sign_id": 37582}
```

#### Failed Request

```
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Query Signature API

### Function Description

+ Query SMS signature

### Call Address

+ GET https://api.sms.jpush.cn/v1/sign/{sign_id}

### Request Example

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/sign/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```
{
    "sign_id": 37582,
    "sign": "极光推送",
    "status": 1, //签名审核状态,1为通过，2为未通过
    "use_status": 1 //签名使用状态，1为使用中，0为未使用
}
```

#### Failed Request

```
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

## Delete Signature API

### Function Description

+ Delete SMS signature

### Call Address

+ DELETE https://api.sms.jpush.cn/v1/sign/{sign_id}

### Request Example

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/sign/37582 -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```
HTTP/1.0 200
  Content-Type: application/json
  Content-Length: 0
```

#### Failed Request

```
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
| 403 | 50101 | invalid image | Illegal picture
| 403 | 50102 | invalid sign id | Illegal signature id
| 403 | 50103 | other signatures in the audit | Other pending signatures exists and cannot be submitted
| 403 | 50104 | invalid signature | Illegal signature content
| 403 | 50105 | the signature in use cannot be deleted | The signature in use cannot be deleted
