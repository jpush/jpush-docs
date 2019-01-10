# Device API <small>v3</small>

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>
The Device API is used to query, set, update, and delete the tag and alias information of the device on the server side. When using the device API, it is necessary to take care not to allow the client to overwrite the tag set by the server.
</p>
<ul style="margin-bottom: 0;">
   <li>If you are not familiar with the logic of tag and alias, it is recommended to use only one of the client or server。</li>
   <li>If both sides are used at the same time, make sure your app can handle the synchronization of tags and aliases.。</li>
 </ul>
</div>

* For details on tags and aliases, refer to the API description of the corresponding client platform.。

    * [Android - tag,alias](../../client/Android/android_api/#api_1)
    * [iOS - tag,alias](../../client/iOS/ios_api/#api-ios)
    * [WinPhone - tag,alias](../../client/WindowsPhone/winphone_api/#api_1)

## API Overview

The Device API is used to query, set, update, and delete device's tag and alias information on the server.

Contains three APIs as device, tag, and alias. Among them：

    * device is used to query/set various attributes of the device, including tags, alias；
    * tag is used to query/set/delete the device's tag
    * alias is used to query/set/delete device’s aliases

### Call Address

https://device.jpush.cn

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
  <p>If the created Jiguang application is allocated to the Beijing computer room and the API caller's server is also located in Beijing, it is more suitable to call the API of the Jiguang Beijing computer room, which can improve the response speed.</p>
  <p>The room where the application is located can be seen through Application Settings -> Application Info of the Jiguang Web Console. If the application is located in the Beijing computer room, the calling address of each API will be given at the same time.</p>
  <p>Call address of Push API in Beijing computer room: https://bjapi.push.jiguang.cn/v3/device</p>
  <p>For the detailed mapping relationship, see the "Server Location" information in "Application Information".</p>
</div>

## Query Device Aliases and Tags

```
GET /v3/devices/{registration_id}
Get all attributes of the current device, including tags, alias and mobile phone number.
```

### Example Request

**Request Header**

```
GET /v3/devices/{registration_id}
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

    * N/A


### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
     "tags": ["tag1", "tag2"],
     "alias": "alias1",
     "mobile": "13012345678"
}
```

* No statistics item is null, otherwise it is the value of the statistic item

## Set Device Aliases and Labels

Please combine server SMS_MESSAGE field when using SMS service[SMS_MESSAGE](rest_api_v3_push/#sms_message).

```
POST /v3/devices/{registration_id}
Update the specified attribute of the current device, and currently supports tags, alias and mobile number
```

### Example Request

**Request Header**

```
POST /v3/devices/{registration_id}
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Body**

```
{
        "tags":{
            "add": [
                "tag1",
                "tag2"
            ],
            "remove": [
                "tag3",
                "tag4"
            ]
        },
        "alias": "alias1",
        "mobile":"13012345678"
    }
```

**Request Params**

+ tags: Support add, remove, or an empty string. When the tags parameter is an empty string, it means to clear all tags; add/remove is to add or remove the specified tags.
    + The limit of one add/remove tag is 100 and the total length cannot exceed 1000 bytes.
    + API settings can be called multiple times, with a maximum of 1000 for registered id tags and no limit on the total number of tag applications。
+ alias: Update the device's alias attribute; when the alias is an empty string, delete the alias of the specified device
+ mobile: Mobile number associated with the device

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

* N/A

## Query Alias

Get the device under the specified alias, up to 10

```
GET /v3/aliases/{alias_value}
```

### Example Request

**Request Header**

```
GET /v3/aliases/{alias_value}?platform=android,ios
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

* platform: Optional parameters. If not, the default is all platforms

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
     "registration_ids": ["registration_id1", "registration_id2"]
}
```

* No statistics item is null, otherwise it is the value of the statistic item.。

## Delete an Alias

Delete an alias and binding relationship between the device and alias

```
DELETE /v3/aliases/{alias_value}
```

### Example Request

**Request Header**

```
DELETE /v3/aliases/{alias_value}?platform=android,ios
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

* platform: Optional parameters. If not filled in, the default is all platforms

### Example Response

**Response**

* N/A

## Query Tag List

```
GET /v3/tags/
```

Get a list of all currently applied tags. Each platform returns a maximum of 100.

### Example Request

**Request Header**

```
GET /v3/tags/
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

* None

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
     "tags": ["tag1", "tag2"]
}
```

* No statistics is null, otherwise it is the value of the statistics item

## Determine the Binding Relationship between Device and Tag

```
GET /v3/tags/{tag_value}/registration_ids/{registration_id}
Check if a device is under tag.
```

### Example Request

**Request Header**

```
GET /v3/tags/{tag_value}/registration_ids/090c1f59f89
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

* registration_id: Required, the device's registration_id

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
     "result": true/false
}
```

###Update Tags

Add or remove devices for a tag

```
POST /v3/tags/{tag_value}
```

### Example Request

**Request Header**

```
POST /v3/tags/{tag_value}
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Body**

```
{
  "registration_ids":{
    "add": [
      "registration_id1",
      "registration_id2"
    ],
    "remove": [
      "registration_id3",
      "registration_id4"
    ]
  }
}
```

**Request Params**

+ action: Action type, which has two options: "add", "remove", identifies whether the request is "add" or "delete."
+ registration_ids: The device registration_id that needs to be added/deleted.
+ add/remove: Support up to 1000 each;

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
 Content-Type: application/json; charset=utf-8
```

**Response Data**

* N/A

##Delete Labels

Delete a tag, and the relationship between tag and device

```
DELETE /v3/tags/{tag_value}
```

### Example Request

**Request Header**

```
DELETE /v3/tags/{tag_value}?platform=android,ios
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

* platform: Optional parameters. If not filled in, the default is all platforms

### Example Response

* N/A

## Get Online Status of User (VIP Exclusive Interface)

If you need to open this interface, please contact: [Business Service](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### Example Request

**Request Header**

```
POST /v3/devices/status/
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Data**

```
{
  "registration_ids":["010b81b3582", "0207870f1b8", "0207870f9b8"]
}
```

**Request Params**

* registration_id: Need the online registration_id of the user, up to a maximum of 1000
* Appkeys that opened this service can call this API

### Example Response

**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
     "010b81b3582": {
         "online": true
     },
     "0207870f1b8": {
          "online": false,
          "last_online_time": "2014-12-16 10:57:07"
     },
     "0207870f9b8": {
          "online": false
    }
}
```

**Response Params**

+ online
    + true: Online in 10 minutes;
    + false: Offline within 10 minutes;
+ last_online_time
    + When online is true, this field does not return
    + When online is false, and the field does not return, it means that the last online time was two days ago;
+ For an invalid regid or regid that does not belong to the appkey, the result returned by the registration id is null;;

## Call Return

### Return Code of Business

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th>Code</th>
      <th>Description</th>
      <th style="t;">Detailed Explanation</th>
      <th>HTTP Status Code</th>
    </tr>
    <tr>
      <td>7000</td>
      <td>Internal error</td>
      <td>Internal system error</td>
      <td>500</td>
    </tr>
    <tr>
      <td>7001</td>
      <td>Parity information is empty</td>
      <td>Must correct</td>
      <td>401</td>
    </tr>
    <tr>
      <td>7002</td>
      <td>Illegal request parameters</td>
      <td>Must correct</td>
      <td>400</td>
      </tr>
    <tr>
      <td>7004</td>
      <td>Failed to verify</td>
      <td>Must correct</td>
      <td>401</td>
      </tr>
    <tr>
      <td>7008</td>
      <td>Appkey does not exist</td>
      <td>Check whether the project appkey is consistent with the official website application</td>
      <td>400</td>
    </tr>
  </table>
</div>

### Reference

Reference documents：[Http-Status-Code](../pus/http_status_code)
