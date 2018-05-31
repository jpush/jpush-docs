# SMS Sending API
# 短信发送 API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
    <ul style="margin-bottom: 0;">
    <li>Support SMS with text and voice verification code</li>
    <li>Support verification of verification code</li>
    <li>Support sending template SMS as single one or in batch</li>
    </ul>
</div>

## HTTP Authentication

> Use HTTP Basic Authentication to do access authorization. In this way, the entire API request can be completed by common HTTP tools such as curl, browser plugins, etc.

A field (Key/Value pair) is added in the HTTP Header：

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret), that is: appKey plus a colon, plus string assembled by masterSecret, and then do a base64 conversion. appKey, masterSecret can be viewed in the application settings of console.

## Sending SMS with Text Verification Code API

### Function Description

+ Send SMS with text verification code

### Call Address

+ POST https://api.sms.jpush.cn/v1/codes

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"mobile":"xxxxxxxxxxx","temp_id":*}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|Phone number|
|temp_id|TRUE|Template ID|

### Return Example

#### Sent successfully

```
{"msg_id": "288193860302"}
```

#### Failed to send

```
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

## Sending SMS with Voice Verification Code API

### Function Description

+ Send SMS with voice verification code

### Call Address

+ POST https://api.sms.jpush.cn/v1/voice_codes

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/voice_codes -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"mobile":"xxxxxxxxxxxxxx", "ttl":60}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|Phone number|
|code|FALSE|The value of voice verification code, only supports 4-8 digits|
|voice_lang|Broadcast language selection of voice verification code, 0 for Chinese, 1 for English, 2 for Chinese and English|
|ttl|FALSE|Validity period of verification code, default is 60 seconds|

### Return Example

#### Sent successfully

```
{"msg_id": "288193860302"}
```

#### Failed to send

```
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

## Verification Code Verifying API

### Function Description

+ Verify whether the verification code is valid

### Call Address

+ POST https://api.sms.jpush.cn/v1/codes/{msg_id}/valid (Note: msg_id is the return value of the calling verification code API)

### Request Example
```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/codes/288193860302/valid -H "Content-Type: application/json" \
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"code":"123456"}'
```

### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|code|TRUE|Verification code|

### Return Example

#### Verification Passed

```
{
    "is_valid": true
}
```

#### Verification Failed

```
{
    "is_valid": false,
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

## Sending Single Template SMS API

### Function Description

+ Send single template SMS

### Call Address

+ POST https://api.sms.jpush.cn/v1/messages

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/messages -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" \
-d '{"mobile":"xxxxxxxxxxxxxx","temp_id":1,"temp_para":{"xxxx":"xxxx"}}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|mobile|TRUE|Phone number|
|temp_id|TRUE|Template ID|
|temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Sent Successfully

```
{"msg_id": 288193860302}
```

#### Failed to Send

```
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

## Sending Bulk Template SMS API

### Function Description

+ Send bulk template SMS

### Call Address

+ POST https://api.sms.jpush.cn/v1/messages/batch

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/messages/batch -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "temp_id": 1250,
    "recipients": [
        {
            "mobile": "13812345678",
            "temp_para": {
                "number": "741627"
            }
        },
        {
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|temp_id|TRUE|Template ID|
|recipients|TRUE|List of SMS recipients|
|recipients.mobile|TRUE|Phone number|
|recipients.temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Sent Successfully

```json
{
    "success_count": 1,
    "failure_count": 1,
    "recipients": [
        {
            "msg_id": "274887115920",
            "mobile": "13812345678"
        },
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "msg_id": "275421247364",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
}
```

#### Failed to Send

```json
{
    "error": {
        "code": *****,
        "message": "******"
    }
}
```

## Return Code

|HTTP CODE| CODE| MESSAGE  | DESC
|:--- |:--- |:--- |:----
| 200 | 50000 | success | Successful Request
| 400 | 50001 | missing auth | Auth is empty
| 401 | 50002 | auth failed | Auth authentication failed
| 400 | 50003 | missing body | Body is empty.
| 400 | 50004 | missing mobile | Phone number is empty.
| 400 | 50005 | missing temp_id | Template ID is empty.
| 403 | 50006 | invalid mobile | Phone number is invalid.
| 403 | 50007 | invalid body | body is invalid.
| 403 | 50008 | no sms code auth | SMS service is not opened
| 403 | 50009 | out of freq | Send overclocking
| 403 | 50010 | invalid code | Verification code is invalid
| 403 | 50011 | expired code | Verification code timeout
| 403 | 50012 | verified code | Verification code has been verified
| 403 | 50013 | invalid temp_id | Template ID is invalid.
| 403 | 50014 | no money | SMS margin is Insufficient.
| 400 | 50015 | missing code | Verification code is empty
| 404 | 50016 | api not found | Api does not exist
| 415 | 50017 | media not supported | Media type is not supported
| 405 | 50018 | request method not support | Request method is not supported
| 500 | 50019 | server error | Server exception
| 403 | 50020 | template auditing | The template is in auditing
| 403 | 50021 | template not pass | Template failed the auditing.
| 403 | 50022 | parameters not all replaced | Not all parameters in the template are replaced
| 403 | 50023 | parameters is empty | The parameter is empty
| 403 | 50024 | unsubscribed mobile | Phone number has been unsubscribed.
| 403 | 50025 | wrong template type | API does not support this template type
| 403 | 50026 | wrong msg_id | msg_id is invalid
| 403 | 50030 | recipients is empty | recipients are empty
| 403 | 50031 | too much recipients | Recipients of SMS exceeds 1000
| 403 | 50034 | repeat send | Send repeatedly
| 403 | 50035 | illegal IP | Illegal IP request
| 403 | 50036 | app in black | The application is listed as blacklist
| 403 | 50037 | has black word | SMS content contains sensitive vocabulary
| 403 | 50038 | invalid code length | Length of the voice verification code is wrong
| 403 | 50039 | invalid code type | The voice verification code is wrong. The verification code only supports digital
| 403 | 50040 | invalid voice language type | Broadcast language type of voice verification code is wrong
| 403 | 50041 | invalid ttl value | Validity of verification code is wrong.
