# Report API

The Received API takes msg_id as a parameter to obtain delivery statistics for this msg_id.

If there are many objects of an API call push(such as broadcast push), the statistics returned by this API will continue to increase because of persistent client delivery.

Delivery statistics for each push message last up to 10 days. That is, the delivery statistics will be cleared after a message is sent for 10 days.

### API Endpoint

https://report.jpush.cn

```
(message) explanation: only https access is supported, not support direct http access
```

### Resource

GET /v2/received

### Example Request

```
curl -v https://report.jpush.cn/v2/received?msg_ids=1613113584,1229760629,1174658841,1174658641 -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
 
< GET /v2/received?msg_ids=1613113584,1229760629,1174658841,1174658641 HTTP/1.1
< Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

### Request Params

* A list of msg_ids returned by push API. Multiple msg_ids are separated by commas, and up to 100 msg_ids are supported.
* Value of HTTP Header Authorization: Basic base64_auth_string
    * Generation rule of base64_auth_string is: base64(appKey:masterSecret)
    * Note that the appKey is separated from the masterSecret by a ":" colon
    * Please refer to the relevant specification document: [Basic Authentication of HTTP](https://en.wikipedia.org/wiki/Basic_access_authentication).

### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
[  {"android_received":62,
    "ios_apns_sent":11,
    "msg_id":1613113584},
   {"android_received":56,
     "ios_apns_sent":33,
     "msg_id":1229760629},
   {"android_received":null,
    "ios_apns_sent":14,
    "msg_id":1174658841},
   {"android_received":32,
    "ios_apns_sent":null,
    "msg_id":1174658641}
]
```

### Response Params

JSON Array.

* android_received:  Android delivery. Null if there is no such data.
* ios_apns_sent: iOS push succeed. Null if there is no such data.

### Example Error Response

```
< HTTP/1.1 401 Unauthorized
< Content-Type: application/json
<
{
  "error": {
        "code": 3001,
        "message": "Basic authentication failed"
     }
}
```

### HTTP Return Code

Reference Document：[HTTP-Status-Code](https://en.wikipedia.org/wiki/Basic_access_authentication)

### Definition of Error Code

Code | Description | Detailed Explanation
--- |--- | ---
10 | Internal system error| |
3001 | HTTP Basic authorization fails. |Please refer to instructions for API documentation
3002 |  The msg_ids parameter does not exist
