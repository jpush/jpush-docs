<h1>Device-API</h1>

```
   Device API 用于在服务器端查询、设置、更新、删除设备的 tag,alias 信息，
   使用时需要注意不要让服务端设置的标签又被客户端给覆盖了。
   *如果不是熟悉 tag，alias的逻辑建议只使用客户端或服务端二者中的一种。
   *如果是两边同时使用，请确认自己应用可以处理好标签和别名的同步。

```

* 需要了解tag,alias的详细信息，请参考对应客户端平台的API说明。

    * [Android - tag,alias](../../client/android_api/#api_1)
    * [iOS - tag,alias](../../client/ios_api/#api-ios)
    * [WinPhone - tag,alias](../../client/winphone_api/#api_1)

### API 概述

Device API 用于在服务器端查询、设置、更新、删除设备的 tag,alias 信息。

包含了device, tag, alias 三组API。其中：

+ device 用于查询/设置设备的各种属性，包含tags, alias；
+ tag 用于查询/设置/删除设备的标签；
+ alias 用于查询/设置/删除设备的别名。

API URL: https://device.jpush.cn

####调用验证

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)
即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

### Device
#### 查询设备(设备的别名与标签)

```
GET /v3/devices/{registration_id}
获取当前设备的所有属性，包含tags, alias。
```

##### Example Request

###### Request Header

```
GET /v3/devices/{registration_id}
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```

###### Request Params
+ N/A

##### Example Response

###### Response Header
```
HTTP/1.1 200 OK 
  Content-Type: application/json; charset=utf-8
```

###### Response Data
```
{
     "tags": ["tag1", "tag2"],
     "alias": "alias1"
}
```

+ 找不到统计项就是null,否则为统计项的值

#### 更新设备 （设置的别名与标签）

```
POST /v3/devices/{registration_id}
更新当前设备的指定属性，当前支持tags, alias。
```

##### Example Request
###### Request Header

```
POST /v3/devices/{registration_id}
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```

###### Request Body
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
        "alias": "alias1"
    } 

``` 
###### Request Params
+ tags:  支持add, remove 或者空字符串。当tags参数为空字符串的时候，表示清空所有的 tags；add/remove 下是增加或删除指定的 tag；
+ alias:  更新设备的别名属性；当别名为空串时，删除指定设备的别名；

##### Example Response
###### Response Header
```
HTTP/1.1 200 OK 
  Content-Type: application/json; charset=utf-8
```

###### Response Data
+ N/A

### Tag
#### 查询标签列表
```
GET /v3/tags/
获取当前应用的所有标签列表。
```

##### Example Request
###### Request Header
```
GET /v3/tags/
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```

###### Request Params
+ None

##### Example Request
###### Response Header
```
HTTP/1.1 200 OK 
  Content-Type: application/json; charset=utf-8
```

###### Response Data
```
{
     "tags": ["tag1", "tag2"]
}
```
+ 找不到统计项就是 null，否则为统计项的值。

#### 判断设备与标签的绑定
```
GET /v3/tags/{tag_value}/registration_ids/{registration_id}
查询某个设备是否在 tag 下。
```

##### Example Request
###### Request Header
```
GET /v3/tags/{tag_value}/registration_ids/090c1f59f89
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```

###### Request Params
+ registration_id  必须，设备的registration_id

##### Example Response
###### Response Header
```
HTTP/1.1 200 OK 
  Content-Type: application/json; charset=utf-8
```

###### Response Data
```
{
     "result": true/false
}
```

#### 更新标签 （与设备的绑定的关系）
```
POST /v3/tags/{tag_value}
为一个标签添加或者删除设备。
```
##### Example Request
###### Request Header
```
POST /v3/tags/{tag_value}
  Authorization: Basic (base64 auth string) 
  Accept: application/json 
```
###### Request Body
```
{  
        "registration_ids":{
            "add": [
                "registration_id1",
                "registration_id2"
            ],
            "remove": [
                "registration_id1",
                "registration_id2"
            ]
        }
}
```
###### Request Params
+ action操作类型，有两个可选："add"，"remove"，标识本次请求是"添加"还是"删除"。
+ registration_ids  需要添加/删除的设备registration_id。
+ add/remove最多各支持1000个；

##### Example Response
###### Response Header
```
HTTP/1.1 200 OK 
 Content-Type: application/json; charset=utf-8
```
###### Response Data
+ N/A

#### 删除标签 (与设备的绑定关系)
```
DELETE /v3/tags/{tag_value}
删除一个标签，以及标签与设备之间的关联关系。
```
##### Example Request
###### Request Header
```
DELETE /v3/tags/{tag_value}?platform=android,ios
  Authorization: Basic (base64 auth string) 
  Accept: application/json 
```

###### Request Params
+ platform 可选参数，不填则默认为所有平台。

##### Example Response
+ N/A


### Alias
#### 查询别名 （与设备的绑定关系）
```
GET /v3/aliases/{alias_value}
获取指定alias下的设备，最多输出10个；
```
##### Example Request
###### Request Header
```
GET /v3/aliases/{alias_value}?platform=android,ios
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```
###### Request Params
+ platform 可选参数，不填则默认为所有平台。

##### Example Response
###### Response Header
```
HTTP/1.1 200 OK 
  Content-Type: application/json; charset=utf-8
```
###### Response Data
```
{
     "registration_ids": ["registration_id1", "registration_id2"]
}
```
+ 找不到统计项就是 null，否则为统计项的值。

#### 删除别名 （与设备的绑定关系）
```
DELETE /v3/aliases/{alias_value}
删除一个别名，以及该别名与设备的绑定关系。
```
##### Example Request
###### Request Header
```
DELETE /v3/aliases/{alias_value}?platform=android,ios
  Authorization: Basic (base64 auth string) 
  Accept: application/json
```
###### Request Params
+ platform 可选参数，不填则默认为所有平台。

##### Example Response
###### Response
+ N/A

### 调用返回
#### HTTP 状态码
参考文档：[Http-Status-Code](../http_status_code)

#### 业务返回码
|Code | 描述 |详细解释|HTTP Status Code|
|-|-|-|-|
|7000|内部错误|系统内部错误|500|
|7001|校验信息为空|必须改正，详情请看：调用验证说明。|401|
|7002|请求参数非法|必须改正|400|
|7004|校验失败|必须修正，详情请看：调用验证说明。|401|

