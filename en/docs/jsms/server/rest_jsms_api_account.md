# SMS Margin Querying API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>Support query the margin of developer accounts</li>
<li>Support query the margin of applications</li>
</ul>
</div>
</br>

## Account Margin Querying API

### Function Description

+ Check the account margin. The account margin refers to the amount of SMS margin that is not assigned to a specific application and belongs to the shared account.

### Call Address

+ GET https://api.sms.jpush.cn/v1/accounts/dev

### HTTP Authentication

> Use HTTP Basic Authentication to do access authorization. In this way, the entire API request can be completed by common HTTP tools such as curl, browser plugins, etc.

A field (Key/Value pair) is added in the HTTP Header：

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret), that is: appKey plus a colon, plus string assembled by masterSecret, and then do a base64 conversion. appKey, masterSecret can be viewed in the application settings of console.

### Request Example

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/accounts/dev -H "Content-Type: application/json" -u "7e503edcb0cb725e331b0311:7289516381dcdf1113730f2b"
```

### Return Example

#### Sent Successfully

```json
{ "dev_balance": 9,  "dev_voice": 702, "dev_industry": 121981, "dev_market": 11683 }
```

#### Response Params

+ dev_balance; Margin of full-size SMS
+ dev_voice; Margin of voice SMS
+ dev_industry; Margin of industry SMS
+ dev_market; Margin of marketing SMS
+ Field value returns null means that margin is not allocated.


#### Failed to Send

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

## Application Margin Querying API

### Function Description

+ Query application margin. Application margin refers to the SMS amount allocated to an application solely.

### Call Address

+ GET https://api.sms.jpush.cn/v1/accounts/app

### HTTP Authentication

> Use HTTP Basic Authentication to do access authorization. In this way, the entire API request can be completed by common HTTP tools such as curl, browser plugins, etc.

A field (Key/Value pair) is added in the HTTP Header：

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret), that is: appKey plus a colon, plus string assembled by masterSecret, and then do a base64 conversion. appKey, masterSecret can be viewed in the application settings of console.

### Request Example

```
curl --insecure -X GET -v https://api.sms.jpush.cn/v1/accounts/app -H "Content-Type: application/json" -u "4c6921c9b20b2fd9bcd8ca3d:5b3e2979c8a48b84cebeaaf4"
```

### Return Example

#### Sent Successfully

```json
{ "app_balance": 1, "app_voice": 22, "app_industry": 44, "app_market": 14 }
```

#### Response Params

+ app_balance: Margin of full-size SMS
+ app_voice: Margin of voice SMS
+ app_industry: Margin of industry SMS
+ app_market: Margin of marketing SMS
+ Field value returns null means that margin is not allocated.

#### Failed to Send

```json
{
  "error": {
    "code": *****,
    "message": "*****"
  }
}
```

## Return Code

|HTTP CODE| CODE| CONTENT  | DESC|
|:---- |:---- |:---- |:----
| 200 | 50000 | success | Request successfully
| 400 | 50001 | missing auth | Auth is empty
| 401 | 50002 | auth failed | Auth authentication failed
| 403 | 50008 | no sms code auth | SMS service is not opened
| 403 | 50009 | out of freq | Send overclocking
| 404 | 50016 | api not found | API does not exist
| 415 | 50017 | media not supported | Media type is not supported
| 405 | 50018 | request method not support | Request method is not supported
| 500 | 50019 | server error | Server exception
| 403 | 50033 | app quota not assigned | The app does not allocate margin
