# Scheduled SMS API

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>Support for submitting, modifying, querying, and deleting of scheduled SMS templates</li>
</ul>
</div>

## HTTP Authentication

> Use HTTP Basic Authentication to do access authorization. In this way, the entire API request can be completed by common HTTP tools such as curl, browser plugins, etc.

A field (Key/Value pair) is added in the HTTP Header：

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret), that is: appKey plus a colon, plus string assembled by masterSecret, and then do a base64 conversion. appKey, masterSecret can be viewed in the application settings of console.

## Single Scheduled SMS Submitting API

### Function Description

+ Submit sending tasks of single scheduled SMS

### Call Address

+ POST https://api.sms.jpush.cn/v1/schedule

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/schedule -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "mobile": "13812345678",
    "temp_id": 1250,
    "temp_para": {
        "number": "741627"
    }
}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|Delivery time, in the format of yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|Phone number|
|temp_id|TRUE|Template ID|
|temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Successful Request

```json
{"schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e"}
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

## Scheduled SMS Bulk Submitting API

### Function Description

+ Submit sending tasks of bulk scheduled SMS

### Call Address

+ POST https://api.sms.jpush.cn/v1/schedule/batch

### Request Example

```
curl --insecure -X POST -v https://api.sms.jpush.cn/v1/schedule/batch -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
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
|send_time|TRUE|Delivery time, in the format of yyyy-MM-dd HH:mm:ss|
|temp_id|TRUE|Template ID|
|recipients|TRUE|List of SMS recipients|
|recipients.mobile|TRUE|Phone number|
|recipients.temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Successful Request

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "success_count": 1,
    "failure_count": 1,
    "failure_recipients": [
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
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

## Single Scheduled SMS Modifying API

### Function Description

+ Modify sending tasks of single scheduled SMS

### Call Address

+ PUT https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### Request Example

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
    "mobile": "13812345678",
    "temp_id": 1250,
    "temp_para": {
        "number": "741627"
    }
}'
```

#### Parameters

|KEY|REQUIRE|DESCRIPTION|
|----|----|----|
|send_time|TRUE|Delivery time, in the format of yyyy-MM-dd HH:mm:ss|
|mobile|TRUE|Phone number|
|temp_id|TRUE|Template ID|
|temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Successful Request

```json
{"schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e"}
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

## Scheduled SMS Bulk Modifying API

### Function Description

+ Modify sending tasks of bulk scheduled SMS

### Call Address

+ PUT https://api.sms.jpush.cn/v1/schedule/batch/{schedule_id}

### Request Example

```
curl --insecure -X PUT -v https://api.sms.jpush.cn/v1/schedule/batch/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d \
'{
    "send_time": "2017-07-01 09:00:00",
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
|send_time|TRUE|Delivery time, in the format of yyyy-MM-dd HH:mm:ss|
|temp_id|TRUE|Template ID|
|recipients|TRUE|List of SMS recipients|
|recipients.mobile|TRUE|Phone number|
|recipients.temp_para|FALSE|Template parameters, parameter names and key-value pairs of values that need to be replaced.|

### Return Example

#### Successful Request

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "success_count": 1,
    "failure_count": 1,
    "failure_recipients": [
        {
            "error_code": "50006",
            "error_message": "invalid mobile",
            "mobile": "18603050709",
            "temp_para": {
                "number": "147721"
            }
        }
    ]
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

## Scheduled SMS Querying API

### Function Description

+ Query sending tasks of scheduled SMS

### Call Address

+ GET https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### Request Example

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```json
{
    "schedule_id": "1a886e7c-a267-49e6-9970-0d396ca5bb1e",
    "send_time": "2017-07-01 09:00:00",
    "temp_id": 1250,
    "recipients": [
        {
            "msg_id": "274887115920",
            "mobile": "13812345678",
            "temp_para": {
                "number": "741627"
            }
        }
    ]
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

## Scheduled SMS Deleting API

### Function Description

+ Delete sending tasks of scheduled SMS

### Call Address

+ DELETE https://api.sms.jpush.cn/v1/schedule/{schedule_id}

### Request Example

```
curl --insecure -X DELETE -v https://api.sms.jpush.cn/v1/schedule/1a886e7c-a267-49e6-9970-0d396ca5bb1e -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
```

### Return Example

#### Successful Request

```json
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

| HTTP CODE | CODE | MESSAGE | DESC
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
| 403 | 50013 | invalid temp_id | Template ID is invalid.
| 403 | 50014 | no money | SMS margin is Insufficient.
| 404 | 50016 | api not found | API does not exist
| 415 | 50017 | media not supported | Media type is not supported
| 405 | 50018 | request method not support | Request method is not supported
| 500 | 50019 | server error | Server exception
| 403 | 50020 | template auditing | The template is in auditing.
| 403 | 50021 | template not pass | Auditing of template failed.
| 403 | 50022 | parameters not all replaced | Not all parameters in the template are replaced.
| 403 | 50023 | parameters is empty | The parameter is empty.
| 403 | 50024 | unsubscribed mobile | Phone number has been unsubscribed.
| 403 | 50025 | wrong template type | API does not support this template type
| 403 | 50026 | wrong msg_id | msg_id is invalid.
| 403 | 50027 | invalid send_time | send_time is empty or before the current time.
| 403 | 50028 | invalid schedule_id | schedule_id is invalid.
| 403 | 50029 | wrong schedule status | Scheduled SMS has been sent or deleted and cannot be modified
| 403 | 50030 | recipients is empty | Recipients are empty.
| 403 | 50031 | too much recipients | Number of SMS recipients exceeds 1000
| 403 | 50034 | repeat send | Repeatedly send
