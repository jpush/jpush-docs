# Overview of Server REST API

JSMS provides REST-compliant HTTP APIs for developers to remotely invoke services provided by JSMS.

At the same time, in order to facilitate developers to use JSMS API easier, a variety of commonly used programming languages (SDKs) are also provided.

## Basic Constraints of REST API

* The API is designed to conform to the HTTP, REST specification. For example: Use the Get method when querying requests, and Use the Post method when submitting requests. If a request is not a corresponding HTTP method, an error will be returned.
* Unless otherwise specified, the value of called parameter should be transcoded to: UTF-8, URL encoded [^1].

[1]: [URL Encoding - WikiPedia Definition](http://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

## API Resource List

### SMS Sending API
<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th style="width: 185px;">Name</th>
            <th>Resource</th>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms/#api_1">Sending SMS with Text Verification Code API<a/></td>
            <td>POST https://api.sms.jpush.cn/v1/codes</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms/#api_2">Sending SMS with Voice Verification Code API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/voice_codes</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms/#api_3">Verification Code Verifying API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/codes/{msg_id}/valid</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms/#api_4">Sending Single Template SMS API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/messages</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms/#api_5">Sending Bulk Template SMS API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/messages/batch</td>
        </tr>
    </table>
</div>

### Scheduled SMS API

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th style="width: 185px;">Name</th>
            <th>Resource</th>
        </tr>
        <tr>
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_1">Single Scheduled SMS Submitting API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/schedule</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_2">Scheduled SMS Bulk Submitting API</a></td>
            <td>POST https://api.sms.jpush.cn/v1/schedule/batch</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_3">Single Scheduled SMS Modifying API</a></td>
            <td>PUT https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_4">Scheduled SMS Bulk Modifying API</a></td>
            <td>PUT https://api.sms.jpush.cn/v1/schedule/batch/{schedule_id}</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_5">Scheduled SMS Querying API</a></td>
            <td>GET https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_api_jsms_schedule/#api_6">Scheduled SMS Deleting API</a></td>
            <td>DELETE https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
        </tr>
        <tr>
</table>
</div>

### SMS Margin Querying API

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th style="width: 185px;">Name</th>
            <th>Resource</th>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_jsms_api_account/#api_1">Account Margin Querying API</a></td>
            <td>GET https://api.sms.jpush.cn/v1/accounts/dev</td>
        </tr>
        <tr >
            <td><a href="https://docs.jiguang.cn/en/jsms/server/rest_jsms_api_account/#api_2">Application Margin Querying API</a></td>
            <td>GET https://api.sms.jpush.cn/v1/accounts/app</td>
        </tr>
    </table>
</div>

## Return Code

If the request fails, the API will return the following return code and description in JSON format

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

### Summary of REST API Return Code

|HTTP CODE| CODE| MESSAGE  | DESC|
|:--- |:--- |:--- |:----
| HTTP CODE | CODE | MESSAGE | DESC
| 200 | 50000 | success | Request succeeded
| 400 | 50001 | missing auth | auth is empty
| 401 | 50002 | auth failed | Authentication of Auth failed
| 400 | 50003 | missing body | body is empty
| 400 | 50004 | missing mobile | Phone number is empty
| 400 | 50005 | missing temp_id | Template ID is empty
| 403 | 50006 | invalid mobile | Phone number is invalid
| 403 | 50007 | invalid body | body is invalid
| 403 | 50008 | no sms code auth | Not open SMS service
| 403 | 50009 | out of freq | Send overclocking
| 403 | 50010 | invalid code | Verification code is invalid
| 403 | 50011 | expired code | Verification code expired
| 403 | 50012 | verified code | Verification code has been verified
| 403 | 50013 | invalid temp_id | Template ID is invalid
| 403 | 50014 | no money | SMS to deliver is insufficient
| 400 | 50015 | missing code | Verification code is empty
| 404 | 50016 | api not found | API does not exist
| 415 | 50017 | media not supported | Media type is not supported
| 405 | 50018 | request method not support | Request method is not supported
| 500 | 50019 | server error | Server exception
| 403 | 50020 | template auditing | The template is in auditing
| 403 | 50021 | template not pass | Template failed the auditing.
| 403 | 50022 | parameters not all replaced | Not all parameters in the template are replaced
| 403 | 50023 | parameters is empty | The parameter is empty
| 403 | 50024 | unsubscribed mobile | Phone number has been unsubscribed
| 403 | 50025 | wrong template type | API does not support this template type
| 403 | 50026 | wrong msg_id | msg_id is invalid
| 403 | 50027 | invalid send_time | send_time is empty or before the current time
| 403 | 50028 | invalid schedule_id | schedule_id is invalid
| 403 | 50029 | wrong schedule status | Scheduled SMS has been sent or deleted and cannot be modified
| 403 | 50030 | recipients is empty | Recipients are empty
| 403 | 50031 | too much recipients | Recipients of SMS exceeds 1000
| 403 | 50034 | repeat send | Send repeatedly
| 403 | 50035 | illegal IP | Illegal IP request
| 403 | 50036 | app in black | The application is listed as blacklist
| 403 | 50037 | has black word | SMS content contains sensitive vocabulary
| 403 | 50038 | invalid code length | Length of the voice verification code is wrong
| 403 | 50039 | invalid code type | The voice verification code is wrong. The verification code only supports digital
| 403 | 50040 | invalid voice language type | Broadcast language type of voice verification code is wrong
| 403 | 50041 | invalid ttl value | Validity of verification code is wrong.
| 403 | 50042 | template is empty | Template content is empty
| 403 | 50043 | template too long | The content of template is too long and the length of the signature is limited to 350 characters
| 403 | 50044 | template parameter invalid | Template parameter is invalid
| 403 | 50045 | remark too long | The comment is too long and the length is limited to 500 characters
| 403 | 50046 | signature not set | The application does not set signature. Please set the signature first
| 403 | 50047 | modify template not allow | Only the template that fails the audit is allowed to modify
