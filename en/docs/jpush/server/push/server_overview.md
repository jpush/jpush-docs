# Overview of Server-side REST API
<br><br>

JPush provides REST-compliant HTTP APIs for developers to remotely call services provided by JPush.
At the same time, to facilitate the use of the JPush API, JPush also provides [SDKs for a variety of common programming languages](../../resources/#sdk_1).

## Basic Constraints of REST API

* The API is designed to conform to the specification of HTTP, REST. For example: the query request uses the Get method, and the submit request uses the Post method. If a request is not a corresponding HTTP method, an error will be returned.
* Unless otherwise special instructions, the called parameter value should be transcoded to: UTF-8, [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding)
* There is a [frequency limit for API requests](#api_1).
* The API request has a [blacklist mechanism](#blacklist)

## API Resource List

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Name</th>
            <th>Resource</th>
            <th>Base URL</th>
            <th>Description</th>
        </tr><tr>
            <td>[REST API v3 - Push](rest_api_v3_push)</td>
            <td>POST /v3/push</td>
            <td>https://api.jpush.cn</td>
            <td>Push message API</td>
        </tr><tr>
            <td>[REST API v3 - Report](rest_api_v3_report)</td>
            <td>GET /v3/received</td>
            <td>https://report.jpush.cn</td>
            <td>Get statistics</td>
        </tr><tr>
            <td>[REST API v3 - Devices](rest_api_v3_device)</td>
            <td>/v3/devices</td>
            <td>https://device.jpush.cn</td>
            <td>Operate tag,alias</td>
        </tr>
    </table>
</div>

## Authentication Method

Jiguang REST API uses [HTTP basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication).

The basic approach is adding Authorization to HTTP header：

```
Authorization: Basic ${base64_auth_string}
```

The Header name is "Authorization" and the value is "username:password" pair (with a colon in the middle) converted by base64. In the JPush API scenario, username is appKey and password is masterSecret. Both of these can be viewed in the application settings of JPush Web console. That is, the generation algorithm of base64_auth_string described above is: base64(appKey:masterSecret)

### Authentication Example
If your appKey is "7d431e42dfa6a6d693ac2d04" and masterSecret is "5e987ac6d2e04d95a9d8f0d1", then please write as below when you call Push API v3 and use the curl command：

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json"
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
-d  '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush!"}}'
```

The request made by the HTTP request is：

```
POST /v3/push HTTP/1.1
Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

## API Frequency Control

The JPush API has frequency control over the number of visits. That is, within a certain time window, the number of API calls is limited.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>Please note:<br> 
<p>The limited frequency of APIs does not mean that there is control over the number and speed of pushes by end users. In simple terms, an API call can be a broadcast pushing to all users of your app.</p>
</p>
</div>

### Frequency Definition

Within a time window, the current definition is: 1 minute. The number of API calls of per AppKey

API frequency of free version is shown in the following table：

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>API Type</th>
            <th>Frequency (times/minutes)</th>
        </tr><tr>
            <td>[Push API v3](rest_api_v3_push)</td>
            <td>600</td>
        </tr><tr>
            <td>[Report-API](rest_api_v3_report)</td>
            <td>2400</td>
        </tr><tr>
            <td>[Device-API](rest_api_v3_device)</td>
            <td>600</td>
        </tr>
    </table>
</div>

The paid version has different levels of frequency depending on the size of the end user. If necessary, please contact our [business team](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc).

### Get Frequency Information

Three frequency control messages are added to all HTTP API Response Headers:

* X-Rate-Limit-Quota：The number of calls within the time window of current AppKey
* X-Rate-Limit-Remaining：The remaining number of times the current time window is available
* X-Rate-Limit-Reset：The number of seconds remaining from the resetting of time window

### Out of Frequency Limit

When a request encounters a frequency limit, the HTTP return code returned by the JPush API is 429, which means: too many requests. In this case, the following information is returned：

```
{
  "error": {
       "code": 2002, 
       "message": "Rate limit exceeded"
   }
}
```

### Suggestions for Frequency Optimization

* Evenly distribute requests to various time windows
* Avoid invalid aliases when requesting a large number of aliases.
* If the request content of a large number of alias and registrationId is consistent, every call could be filled in multiple recipients. Please refer to description of the push API for details.

## BlackList

If an application is considered malicious, or if its API call is illegal, its AppKey will be blacklisted. API calls of blacklisted AppKey will be rejected directly with a return code of 403 (Request rejected). Format  of the returned content is：

```
{
  "error": {
       "code": 2003,
       "message": "The appKey is in black list."
   }
}
```

If your app is blacklisted, please send an e-mail to support@jpush.cn for further communication and coordination.。

## Reference

* [HTTP Error Code 429 - WikiPedia Definition](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error)
* [Definition of Twitter API Frequency Control](https://dev.twitter.com/docs/rate-limiting/1.1)