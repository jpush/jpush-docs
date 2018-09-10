# Device API <small>v3</small>

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p> Device API 用于在服务器端查询、设置、更新、删除设备的 tag，alias 信息，使用时需要注意不要让服务端设置的标签又被客户端给覆盖了。</p>
<ul style="margin-bottom: 0;">
   <li>如果不是熟悉 tag，alias 的逻辑建议只使用客户端或服务端二者中的一种。</li>
   <li>如果是两边同时使用，请确认自己应用可以处理好标签和别名的同步。</li>
 </ul>
</div>

<br>

* 需要了解 tag，alias 的详细信息，请参考对应客户端平台的 API 说明。

    * [Android - tag,alias](../../client/Android/android_api/#api_3)
    * [iOS - tag,alias](../../client/iOS/ios_api/#api-ios)
    * [WinPhone - tag,alias](../../client/WindowsPhone/winphone_api/#api_1)

## API 概述

Device API 用于在服务器端查询、设置、更新、删除设备的 tag, alias 信息。

包含了 device, tag, alias 三组 API。其中：

+ device 用于查询/设置设备的各种属性，包含 tags, alias；
+ tag 用于查询/设置/删除设备的标签；
+ alias 用于查询/设置/删除设备的别名。

需要用到的关键信息还有 registration ID：    

+ 设备的 registration_id 在客户端集成后获取，详情查看 [Android](https://docs.jiguang.cn/jpush/client/Android/android_api/#registrationid-api)、 [iOS](https://docs.jiguang.cn/jpush/client/iOS/ios_api/#registrationid) 和 [WinPhone](https://docs.jiguang.cn/jpush/client/WindowsPhone/winphone_api/#registrationid) 的 API 文档；
+ 服务端未提供 API 去获取设备的 registrationID 值，需要开发者在客户端获取到 registration ID 后上传给开发者服务器保存。

### 调用地址
https://device.jpush.cn

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">

<p>如果创建的极光应用分配的北京机房，并且 API 调用方的服务器也位于北京，则比较适合调用极光北京机房的 API，可以提升一定的响应速度。</p>
<p>通过极光 Web 控制台 “应用设置” -> "应用信息" 中可以看到应用所在机房。如果应用所在地为北京机房，同时会给出各 API 的调用地址。</p>

<p>北京机房 Push API 调用地址： https://bjapi.push.jiguang.cn/v3/device </p>
<p>详细对应关系见 “应用信息” 中 “服务器所在地” 后的信息。</p>

</div>


## 查询设备的别名与标签

```
GET /v3/devices/{registration_id}
获取当前设备的所有属性，包含 tags, alias，手机号码 mobile。
```

### Example Request

**Request Header**

```
GET /v3/devices/{registration_id}
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

+ N/A

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

+ 找不到统计项就是 null，否则为统计项的值

## 设置设备的别名与标签

使用短信业务，请结合服务端[ SMS_MESSAGE ](rest_api_v3_push/#sms_message)字段

```
POST /v3/devices/{registration_id}
更新当前设备的指定属性，当前支持 tags, alias，手机号码 mobile。
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

+ tags：支持 add, remove 或者空字符串。当 tags 参数为空字符串的时候，表示清空所有的 tags；add/remove 下是增加或删除指定的 tag；
    + 一次 add/remove tag 的上限均为 100 个，且总长度均不能超过 1000 字节。
    + 可以多次调用 API 设置，一个设备（registrationID）能设置的 tag 上限为 1000 个，应用 tag 总数没有限制 。
+ alias：更新设备的别名属性；当别名为空串时，删除指定设备的别名；
+ mobile：设备关联的手机号码

### Example Response
**Response Header**

```
HTTP/1.1 200 OK
  Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

## 查询别名
获取指定 alias 下的设备，最多输出 10 个；

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

+ platform 可选参数，不填则默认为所有平台。

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

+ 找不到统计项就是 null，否则为统计项的值。

## 删除别名
删除一个别名，以及该别名与设备的绑定关系。

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

+ platform 可选参数，不填则默认为所有平台。

### Example Response
**Response**

+ N/A

## 查询标签列表

```
GET /v3/tags/
```

获取当前应用的所有标签列表，每个平台最多返回 100 个。


### Example Request
**Request Header**

```
GET /v3/tags/
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

+ None

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

+ 找不到统计项就是 null，否则为统计项的值。

## 判断设备与标签绑定关系

```
GET /v3/tags/{tag_value}/registration_ids/{registration_id}
查询某个设备是否在 tag 下。
```

### Example Request
**Request Header**

```
GET /v3/tags/{tag_value}/registration_ids/090c1f59f89
  Authorization: Basic (base64 auth string)
  Accept: application/json
```

**Request Params**

+ registration_id  必须，设备的 registration_id

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

## 更新标签

为一个标签添加或者删除设备。


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

+ action 操作类型，有两个可选："add"，"remove"，标识本次请求是"添加"还是"删除"。
+ registration_ids 需要添加/删除的设备 registration_id。
+ add/remove 最多各支持 1000 个；

### Example Response
**Response Header**

```
HTTP/1.1 200 OK
 Content-Type: application/json; charset=utf-8
```
**Response Data**

+ N/A

## 删除标签
删除一个标签，以及标签与设备之间的关联关系。

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

+ platform 可选参数，不填则默认为所有平台。

### Example Response
+ N/A



## 获取用户在线状态（VIP 专属接口）

如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

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

+ registration_ids  需要在线状态的用户 registration_id， 最多支持查询 1000 个 registration_id；
+ 需要申请开通了这个业务的 Appkey 才可以调用此 API。


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
    + true: 10 分钟之内在线；
    + false: 10 分钟之内不在线；

+ last_online_time
    + 当 online 为 true 时，该字段不返回;
    + 当 online 为 false，且该字段不返回时，则表示最后一次在线时间是两天之前；

+ 对于无效的 regid 或者不属于该 appkey 的 regid，该 registration id 返回的结果为空;



## 调用返回


### 业务返回码

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >描述</th>
      <th style="t;" >详细解释</th>
      <th >HTTP Status Code</th>
    </tr>
    <tr >
      <td>7000</td>
      <td>内部错误</td>
      <td>系统内部错误</a></td>
      <td>500</td>
    </tr>
    <tr >
      <td>7001</td>
      <td>校验信息为空</td>
      <td><a href="https://docs.jiguang.cn/jpush/server/push/server_overview/#_1">调用验证</a>中的 Appkey 与 MasterSecret 为空</td>
      <td>401</td>
    </tr>
    <tr >
      <td>7002</td>
      <td>请求参数非法</td>
      <td>需严格遵守文档参数类型与值说明</td>
      <td>400</td>
    </tr>
    <tr >
      <td>7004</td>
      <td>校验失败</td>
      <td>检查<a href="https://docs.jiguang.cn/jpush/server/push/server_overview/#_1">调用验证</a>中的 Appkey 与 MasterSecret 是否正确</td>
      <td>401</td>
    </tr>
    <tr >
      <td>7008</td>
      <td>appkey 不存在</td>
      <td>检查工程填写的 Appkey 是否与官网应用一致</td>
      <td>400</td>
    </tr>
    <tr >
      <td>7030</td>
      <td>系统繁忙，稍后重试</td>
      <td>系统繁忙，稍后重试</td>
      <td>503</td>
    </tr>
  </table>
</div>

### 参考
参考文档：[Http-Status-Code](../pus/http_status_code)

