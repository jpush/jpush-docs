# IM REST API

The JMessage API provides developers with an HTTP API for related IM functionality.

Addresses of these API are unified (note that unlike the Push API): https://api.im.jpush.cn

**HTTP Authentication**

Authentication uses the HTTP Basic mechanism, which adds a field (Key/Value pair) to the HTTP Header (header):

Authorization: Basic base64_auth_string

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret)

That is, add a colon to the appKey, plus the string assembled by masterSecret, and do a base64 conversion.

## Overview of User Object Fields

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Parameter</th>
            <th>Meaning</th>
            <th>Limits of character length</th>
        </tr><tr>
            <td>username</td>
            <td>User login name</td>
            <td>Byte(4~128)</td>
        </tr><tr>
            <td>password</td>
            <td>Login password</td>
            <td>Byte(4~128)</td>
        </tr><tr>
            <td>appkey</td>
            <td>Appkey to which the user belongs</td>
            <td></td>
        </tr><tr>
            <td>nickname</td>
            <td>User nickname</td>
            <td>Byte(0~64)</td>
        </tr><tr>
            <td>birthday</td>
            <td>Birthday</td>
            <td>yyyy-MM-dd HH:mm:ss</td>
        </tr><tr>
            <td>gender</td>
            <td>Gender 0 - Unknown, 1 - Male, 2 - Female</td>
            <td></td>
        </tr><tr>
            <td>signature</td>
            <td>User signature</td>
            <td>Byte(0~250)</td>
        </tr><tr>
            <td>region</td>
            <td>User area</td>
            <td>Byte(0~250)</td>
        </tr><tr>
            <td>address</td>
            <td>Detailed address</td>
            <td>Byte(0~250)</td>
        </tr><tr>
            <td>ctime</td>
            <td>User creation time</td>
            <td></td>
        </tr><tr>
            <td>mtime</td>
            <td>Last modified time</td>
            <td></td>
        </tr><tr>
            <td>extras</td>
            <td>User-defined json objects</td>
            <td>Byte(0~512)</td>
        </tr>
    </table>
</div>

## User Registration

### Register as user

Batch registration of users to JMessage server, up to 500 users in one batch registration

```
POST /v1/users/
```

#### Example Request

```
[{"username": "dev_fang", "password": "password"}]
```

**Request Params**

JSON Array.

+ username (required)
     - At the beginning: letters or numbers
     - letters, numbers, underscores
     - English, minus, @
+ password (required) JMessage server will be saved with MD5 encryption.
+ nickname (optional)
     - Unsupported characters: English characters: \n \r\n
+ avatar (optional)
     - Need to fill in the media_id obtained from the uploading interface of files
+ birthday (optional) example: 1990-01-24
     - yyyy-MM-dd
+ signature (optional)
     - Supported characters: All, including Emoji
+ gender (optional)
     - 0 - Unknown, 1 - Male, 2 - Female
+ region (optional)
     - Supported characters: All, including Emoji
+ address (optional)
     - Supported characters: All, including Emoji
+ extras (optional) user-defined json objects

#### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
<
[{"username": "dev_fang"  }]
```

**Response Params**

JSON Array.

+ username
+ Error: When an error occurs in the registration of a user, there is an error object in the object indicating the cause of the error.
     - 899003: parameter error, **Request Body** does not meet the requirements
     - 899001: user already exists

## Admin Registration

### Admin Register (Administrator api sends permissions of message interface)

```
POST /v1/admins/
```

#### Example Request

```
{"username": "dev_fang", "password": "password"}
```

**Request Params**

+ username Byte(4-128) supported character
     - At the beginning: letters or numbers
     - letters, numbers, underscores
     - English, minus, @
+ password Byte(4-128) Characters are not limited
+ nickname (optional)
     - Unsupported characters: English characters: \n \r\n
+ avatar (optional)
     - Need to fill in the media_id obtained from the uploading interface of files
+ birthday (optional) birthday example: 1990-01-24
     - yyyy-MM-dd
+ signature (optional)
     - Supported characters: All, including Emoji
+ gender (optional)
     - 0 - Unknown, 1 - Male, 2 - Female
+ region (optional)
     - Supported characters: All, including Emoji
+ address (optional)
     - Supported characters: All, including Emoji
+ extras (optional) user-defined json objects

#### Example Response

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8
```

### GetAdminsListByAppkey: Get admin list of app

```
GET /v1/admins?start={start}&count={count}
```

#### Example Request

**Request Header**

```
GET /admins?start=1&count=30
Acct: application/json
```

**Request Body**

+ N/A

**request params**

+ start: record position of starting, starts from 0
+ count: query number, supports up to 500

#### Example Response

**Response Header**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
  "total":1233,
  "start":1100,
  "count":3,
  "users":
    [{  "username": "cai",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    }, {"username": "yi",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    }, {"username": "huang",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    }]}
```

## User Maintenance

### Get user information

```
GET /v1/users/{username}
```

**Request Params**

+ username: Fill to the request path

#### Example Response

```
{
    "username": "javen",
    "nickname": "hello",
    "avatar": "/avatar",
    "birthday": "1990-01-24 00:00:00",
    "gender": 0,
    "signature": "orz",
    "region": "shenzhen",
    "address": "shenzhen",
    "mtime": "2015-01-01 00:00:00",
    "ctime": "2015-01-01 00:00:00"}
```

**Instructions**

In addition to the username mtime ctime, these three sub-sections, if there is no json for the the remaining fields, then there is no corresponding key.

### Update user information

```
PUT /v1/users/{username}
```

#### Example Request

```
{
    "nickname": "Hello JMessage"
}
```

**Request Params**

+ nickname (optional)
     - Unsupported characters: English characters: \n \r\n
+ avatar (optional)
     - Need to fill in the media_id obtained from the uploading interface of files
+ birthday (optional) birthday example: 1990-01-24
     - yyyy-MM-dd
+ signature (optional)
     - Supported characters: All, including Emoji
+ gender (optional)
     - 0 - Unknown, 1 - Male, 2 - Female
+ region (optional)
     - Supported characters: All, including Emoji
+ address (optional) address
     - Supported characters: All, including Emoji
+ extras (optional) user-defined json objects

#### Example Response

```
< HTTP/1.1 204
< Content-Type: application/json; charset=utf-8
```

### Query user online status

```
Get /v1/users/{username}/userstat
```

#### Example Request

**Request Header**

```
Get /v1/users/caiyh/userstat
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ username

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 200 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{"login":true, "online": false}
```

This interface is not applicable to multi-end online. Please use batch status interface for multi-end online.

#### Error Code

+ 899003: username is illegal
+ 899002: user does not exist

### Query bulk user online status

```
Post /v1/users/userstat
```

#### Example Request

**Request Header**

```
Post /v1/users/userstat
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ N/A

**Request Body**

```
["USER1","USER2"]
```

#### Example Response

**Response Header**

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
[
    {
        "devices": [],
        "username": "caiyh01"
    },
    {
        "devices": [{
            "login": false,
            "online": false,
            "platform": "a"
        }],
        "username": "Rauly"
    }
]

```

+ devices: Array of device login status. Array as empty if no login.
+ Platform SDK Platforms: a-Android, i-iOS, j-JS, w-Windows

#### Error Code

+ 899003: username is illegal
+ 899002: user does not exist

### Change password

```
PUT /v1/users/{username}/password
```

**Request Header**

```
PUT /v1/users/javen/password
```

#### Example Request

```
{
    "new_password": "654321"
}
```

**Request Params**

+ new_password （required）

#### Example Response

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Delete users

```
DELETE /v1/users/{username}
```

**Request Params**

+ username

#### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Ctent-Type: application/json; charset=utf-8
```

### Delete users in batches

```
DELETE /v1/users/
```

**Request Body**

```
["USER1","USER2"]
```

+ username: Array of usernames. (Maximum support for deleting 100 users at the same time)

#### Example Response

```
< HTTP/1.1 20 NO CONTENT
< Content-Type: application/json; charset=utf-8
```

### Add blacklist

```
Put /v1/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Put /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ JsonArray
+ username的JsonArray

**Request Body**

```
[
 "test1",
 "test2"
 ]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Remove blacklist

```
Delete /v1/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Delete /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ JsonArray
+ username的JsonArray

**Request Body**

```
[
    "test1",
    "test2"
 ]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### List of blacklist

```
Get /v1/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Put /v1/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ username

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 200 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
[{
    "username": "javen",
    "nickname": "hello",
    "avatar" = "/avatar",
    "birthday": "1990-01-24 00:00:00",
    "gender": 0,
    "signature": "orz",
    "region": "shenzhen",
    "address": "shenzhen",
    "mtime": "2015-01-01 00:00:00",
    "ctime": "2015-01-01 00:00:00"
}]
```

### Get user list

```
GET /v1/users/?start={start}&count={count}
```

**Request Params**

+ start: Number of records started
+ count: Number of records to retrieve

#### Example Response

```
< HTTP/1.1 200
< Content-Type: application/json

{
    "total": 12580,
    "start": 1100,
    "count": 100,
    "users":
    [{  "username": "cai",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    }, {"username": "yi",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    },{ "username": "huang",
        "nickname": "hello",
        "mtime": "2015-01-01 00:00:00",
        "ctime": "2015-01-01 00:00:00"
    }]
}
```

### Do-Not-Disturb

#### Do-Not-Disturb settings

```
POST  /v1/users/{username}/nodisturb
```

#### Example Request

**Request Header**

```
POST  /v1/users/{username}/nodisturb
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ single: single chat DND, supports add remove array (optional)
+ group: group chat DND, supports add remove array (optional)
+ global: global DND, 0 or 1 0 means closed, 1 means open (optional)

**Request Body**

```
{   
   "single":{   
      "add":[   
         "username1",
         "username2"
      ]
   },
   "group":{   
      "add":[   
         110000101
      ],
      "remove":[   
         1000001111
      ]
   },
   "global":0
}
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

#### Error Code

+ 899003: username is illegal;
+ 899002: user does not exist;
+ 899051: group does not exist
+ 899052: sets group
+ Blocked, group blocking is turned on
+ 99053: sets group message block and the group blocking is turned off

### Disable users

```
PUT /v1/users/{username}/forbidden?disable={disable}
```

**Request Params**

+ disable boolean, true for disabled users, false for activated users

#### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

## Message Related

### Send a message

```
POST /v1/messages
```

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Parameter</th>
            <th>Meaning</th>
        </tr><tr>
            <td>version</td>
            <td>Version number is currently 1 (required)</td>
        </tr><tr>
            <td>target_type</td>
            <td>Target type: single - person, group – group, chatroom - chat room (required)</td>
        </tr><tr>
            <td>from_type</td>
            <td>The sender's identity is currently restricted to the admin user and must be registered as an admin user (required)</td>
        </tr><tr>
            <td>msg_type</td>
            <td>Message type: text, image, custom message (msg_body is json object, server does not check) voice (required)</td>
        </tr><tr>
            <td>target_id</td>
            <td>Target id: single to fill username, group to fill group id, chatroom to fill chatroomid (required)</td>
        </tr><tr>
            <td>target_appkey</td>
            <td>Cross-app target appkey (optional)</td>
        </tr><tr>
            <td>from_id</td>
            <td>Sender's username (required)</td>
        </tr><tr>
            <td>from_name</td>
            <td>Sender’s display name (optional)</td>
        </tr><tr>
            <td>target_name</td>
            <td>Recipient’s display name (optional)</td>
        </tr><tr>
            <td>no_offline</td>
            <td>Whether the message is stored offline, true or false, defaults to false, indicating that it needs to be stored offline (optional)</td>
        </tr><tr>
            <td>no_notification</td>
            <td>Whether the message is displayed in the notification bar, true or false, the default is false, which means to display in the notification bar (optional)</td>
        </tr><tr>
            <td>notification</td>
            <td>Custom notification bar display (optional)</td>
        </tr><tr>
            <td>notification->title</td>
            <td>Title of the notification (optional)</td>
        </tr><tr>
            <td>notification->alert</td>
            <td>Content of notification (optional)</td>
        </tr><tr>
            <td bgcolor="#D3D3D3">msg_body</td>
            <td>The body of the Json object is limited to 4096 bytes</td>
        </tr><tr>
            <td colspan="2" ><font  color="red">When msg_type is text, the format of msg_body is as follows</td>
        </tr><tr>
            <td>msg_body -> text</td>
            <td>Message content (required)</td>
        </tr><tr>
            <td>msg_body-> extras</td>
            <td>Optional json objects. Developers can customize the extra key value (optional)</td>
        </tr><tr>
            <td colspan="2" ><font  color="red">When msg_type is an image, msg_body is the json returned by the uploaded image in the following format</td>
        </tr><tr>
            <td>msg_body->media_id</td>
            <td>String: The key returned by the server after the file is uploaded. It is used to generate the downloaded URL (required)</td>
        </tr><tr>
            <td>msg_body->media_crc32</td>
            <td>The crc32 checksum of a long file, used to download the checksum of the large image (required)</td>
        </tr><tr>
            <td>msg_body->width</td>
            <td>Int: Original width of image (required)</td>
        </tr><tr>
            <td>msg_body->height</td>
            <td>Int: Original height of image (required)</td>
        </tr><tr>
            <td>msg_body->format</td>
            <td>String: Image format (required)</td>
        </tr><tr>
            <td>msg_body->hash</td>
            <td>String: Image hash (optional)</td>
        </tr><tr>
            <td>msg_body->fsize</td>
            <td>Int: File size (bytes) (required)</td>
        </tr><tr>
            <td colspan="2" ><font  color="red">When msg_type is voice, msg_body is the json returned by uploading voice. The format is as follows:</td>
        </tr><tr>
            <td>msg_body->media_id</td>
            <td>String: The key returned by the server after the file is uploaded. It is used to generate the downloaded URL (required)</td>
        </tr><tr>
            <td>msg_body->media_crc32</td>
            <td>The crc32 checksum of a long file, used to download the checksum of the large image (required)</td>
        </tr><tr>
            <td>msg_body->duration</td>
            <td>Int: Audio duration (required)</td>
        </tr><tr>
            <td>msg_body->hash</td>
            <td>String: Audio hash (optional)</td>
        </tr><tr>
            <td>msg_body->fsize</td>
            <td>Int: File size (bytes) (required)</td>
        </tr>
    </table>
</div>

#### Example Request

```
msg_type:text
{
    "version": 1,
    "target_type": "single",
    "target_id": "javen",
    "from_type": "admin",
    "from_id": "fang",
    "msg_type": "text",
    "msg_body": {
        "extras": {},
        "text": "Hello, JMessage!"
    }
}

msg_type:image
{
    "version": 1,
    "target_type": "single",
    "target_id": "javen",
    "from_type": "admin",
    "from_id": "fang",
    "msg_type": "image",
    "msg_body": {
    "media_id": "qiniu/image/CE0ACD035CBF71F8",
    "media_crc32":2778919613,
    "width":3840,
    "height":2160,
    "fsize":3328738,
    "format":"jpg"
    }
}

msg_type:voice

{
    "version": 1,
    "target_type": "single",
    "target_id": "ppppp",
    "from_type": "admin",
     "from_id": "admin_caiyh",
    "msg_type": "voice",
    "msg_body": {
    "media_id": "qiniu/voice/j/A96B61EB3AF0E5CDE66D377DEA4F76B8",
    "media_crc32":1882116055,
    "hash":"FoYn15bAGRUM9gZCAkvf9dolVH7h",
    "fsize" :12344;
     "duration": 6
    }
}
```

```
msg_type:custom

{
    "version": 1,
    "target_type": "single",
    "target_id": "ppppp",
    "from_type": "admin",
     "from_id": "admin_caiyh",
    "msg_type": "voice",
    "msg_body": {
        json define yourself
       }
}
```

**Request Params**

+ JSON Object.
+ Follow the protocol document: [IM Message Protocol](https://docs.jiguang.cn/jmessage/advanced/im_message_protocol/)
+ This api can only be sent by admin user

#### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
<
{"msg_id": 43143728109, "msg_ctime":1493794522950}
```

msg_ctime: time stamp created  the message

#### Error Code

+ 899003: parameter error, Request Body parameter does not meet the requirements
+ 899002: user does not exist, and target_id or from_id does not exist
+ 899016: from_id does not have permission to send messages

### Retract message

```
POST /v1/messages/{username}/{msgid}/retract
```

#### Example Request

**Request Header**

```
POST /v1/messages/{username}/{msgid}/retract
```

**Request Body**

+ N/A

**Request Params**

Parameter | Meaning | Note
--- | --- | ---
msgid | Message msgid |
username | Username who send this msg |

#### Example Response

**Response Header**

```
HTTP/1.1 204 No Content
Content-Type: application/json; charset=utf-8 
```

#### Error Code 

+ 855001: Exceed the withdrawal time. The effective withdrawal time was within 3 minutes after the message was sent.
+ 855003: Revocation message does not exist
+ 855004: Message has been withdrawn

## Download and Upload Media Files

### Download Document

```
GET /v1/resource?mediaId={mediaId}
```

#### Example Request

**Request Header**

```
GET /v1/resource?mediaId={mediaId}
```

**Request Body**

+ N/A

**Request Params**

Parameter | Meaning | Note
--- | --- | ---
mediaId | The mediaId of the resource, including the user's avatar field |

#### Example Response

**Response Header**

```
HTTP/1.1 200 no content
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{"url":"http://........."}
```

### Upload File

```
POST /v1/resource?type=image
```

#### Example Request

File uploading uses form to upload curl examples:

image uploading curl -F "filename=@/home/test.jpg" https://api.im.jpush.cn/v1/resource?type=image -u "appkey:secret ""

File uploading curl -F "filename=@/home/test.mp3" https://api.im.jpush.cn/v1/resource?type=file -u "appkey:secret"

Voice uploading curl -F "filename=@/home/test.mp3" https://api.im.jpush.cn/v1/resource?type=voice -u "appkey:secret"

Note: The file size is limited to 8m. It only supports image formats currently, including jpg bmp gif png, etc.

Parameter | Meaning | Note
--- | --- | ---
filename | File path of local disk |
type | File type: Supports "image", "file", "voice" |

**Response Header**

#### Example Response

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

**Response Data**

Image Response

```
{
    "media_id":"qiniu/image/F39AA12204DAB6A2",
    "media_crc32":1338734977,
    "width":720,
    "height":1280,
    "format":"jpg",
    "fsize":52468
}
```

+ media_id String: The key returned by the server after the file is uploaded
+ Crc32 checksum of media_crc32 long file
+ width int: original width of picture
+ height int: original height of picture
+ format String: image format
+ fsize int: file size (bytes)
+ hash String: optional, for alternative verification when the crc checksum does not exist

File Response

```
{
    "media_id":"qiniu/file/j/1BB3B833AEABFF62E883C5CE421867A9",
    "media_crc32":1415584260,
    "fname":"0839d1c0-48e9-4032-9333-f3691a7d9e48.dmp",
    "fsize":176512,
    "hash":"FtH0kPT0YI89HAw1K9wv_vVKiNab"
}
```

+ media_id String: The key returned by the server after the file is uploaded. It is used to generate the downloaded URL.
+ Crc32 checksum of media_crc32 long file
+ hash String; optional, for alternative verification when the crc checksum does not exist
+ fsize int: file size (bytes)
+ fname String: file names of sending and receiving

Voice Response

```
{
    "media_id":"qiniu/voice/j/9C4312B1EA0FB28337566D1A29A244B5",
    "media_crc32":1882116055,
    "hash":"FoYn15bAGRUM9gZCAkvf9dolVH7h",
    "format":"m4a",
    "fsize":238105
}
```

+ media_id String: The key returned by the server after the file is uploaded. It is used to generate the downloaded URL
+ Crc32 checksum for media_crc32 long file
+ hash String: optional, for alternative verification when the crc checksum does not exist
+ fsize int: file size (bytes)
+ format String: format of source file

## Overview of Group Object Fields

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Parameter</th>
            <th>Meaning</th>
            <th>Limits of character length</th>
        </tr><tr>
            <td>name</td>
            <td>Group name</td>
            <td>Byte(0~64)</td>
        </tr><tr>
            <td>desc</td>
            <td>Group description</td>
            <td>Byte(0~250)</td>
        </tr><tr>
            <td>owner_username</td>
            <td>Owner's username</td>
            <td>Byte(4-128)</td>
        </tr><tr>
            <td>MaxMemberCount</td>
            <td>Group default to 500 people</td>
            <td></td>
        </tr><tr>
            <td>ctime</td>
            <td>Creation time</td>
            <td></td>
        </tr><tr>
            <td>mtime</td>
            <td>Last Modified Time</td>
            <td></td>
        </tr><tr>
            <td>avatar</td>
            <td>Group avatar</td>
            <td></td>
        </tr>
    </table>
</div>

## Group Maintenance

### Create a group

```
POST /v1/groups/
```

Group MaxMemberCount (number limit) definition

#### Example Request

```
{
    "owner_username": "tom",
    "name": "群聊天室",
    "members_username": ["eddie", "annie"],
    "flag": 1,
    "desc": "运动"
}
```

**Request Params**

+ owner_username (required)
+ name (required) group name
     - Supported characters: All, including Emoji.
+ members_username
+ avatar (optional) group avatar, media_id obtaine when uploading interfaces
+ desc (optional) group description
     - Supported characters: All, including Emoji.
+ flag (optional) type
     - 1 - private group (default)
     - 2 - public group
     - does not specify the flag, the default is 1

#### Example Response

```
< HTTP/1.1 201 Created
< Content-Type: application/json
<

{
    "gid":12345,
    "owner_username": 123456,
    "name": "display_name",
    "members_username": [],
    "desc":"doubi",
    "MaxMemberCount" = 500
}
```

### Get group details

```
GET /v1/groups/{Group id}
```

**Request Params**

+ Group id: assigned when creating a group

#### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<

{
      "gid": 12345,
      "name": "jpush",
      "desc": "push",
      "appkey": "dcf71ef5082057832bd44fbd",
      "MaxMemberCount": 500,
      "mtime": "2014-07-01 00:00:00",
      "ctime": "2014-06-05 00:00:00"
}
```

### Update group information

```
PUT /v1/groups/{Group id}
```

**Request Params**

+ name: group name
+ desc: group description
+ atar: group avatar, media_id

```
PUT /v1/groups/{Group id}
```

**Request Body**

```
{ "the key you want to update": "the value you want to update" }
```

#### Example Response

```
HTTP/1.1 204 NO Content
```

### Delete group

Delete a group.

All members of the group will receive notification that the group has been dissolved.

```
DELETE /v1/groups/{Group id}
```

**Request Params**

+ Group id

#### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

### Update group members

Batch adding and deleting members of a gid group.

Group members will receive notifications of adding and deleting members

```
POST /v1/groups/{Group id}/members
```

**Request Params**

+ gid: group ID
+ add json array: Indicates the user to add to the group (optional)
+ remove json array: Indicates the user to remove from the group (optional)
+ At least one of the two

#### Example Request

```
{
    "add":[
        "test1", "test2"
    ],
    "remove":[
        "test3", "test4"
    ]
}
```

#### Example Response

```
< HTTP/1.1 204 NO CONTENT
< Content-Type: application/json
```

### Get a list of group members

```
GET /v1/groups/{Group id}/members/
```

**Request Params**

+ Group id

#### Example Response

+ JsonObject UID array

```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[
    {
        "username": "javen",
        "nickname": "hello",
        "avatar" = "/avatar",
        "birthday": "1990-01-24 00:00:00",
        "gender": 0, "signature": "orz",
        "region": "shenzhen",
        "address": "shenzhen",
        "flag":0
    }
]
```

+ flag
     - 0 - common group members
     - 1 - Group owner

### Get the group list of some user

```
GET /v1/users/{username}/groups/
```

**Request Params**

+ username

#### Example Response

+ ctime: group
+ Creation time
+ Mtime: last modified time of group

```
< HTTP/1.1 200 OK
< Content-Type: application/json

[   {
        "gid": 12345,
        "name": "jpush",
        "desc": "push",
        "appkey": "dcf71ef5082057832bd44fbd",
        "MaxMemberCount": 500,
        "mtime": "2014-07-01 00:00:00",
        "ctime": "2014-06-05 00:00:00"
    }
]
```

### Get the group list of current application

```
GET /v1/groups/?start={start}&count={count}
```

**Request Params**

+ Start: number of records started
+ count: number of records read this time. The maximum is 500

#### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json

{
    "total":1233,
    "start":1100,
    "count":1,
    "groups":
    [{
        "gid": 12345,
        "name": "jpush",
        "desc": "push",
        "appkey": "dcf71ef5082057832bd44fbd",
        "MaxMemberCount": 500,
        "mtime": "2014-07-01 00:00:00",
        "ctime": "2014-06-05 00:00:00"
    }]
}
```

### Block group message

```
POST /v1/users/{username}/groupsShield
```

#### Request Param

+ N/A

**Request Body**

```
{   
    "add":[   
        110000101
     ],
     "remove":[   
        1000001111
     ]
}
```

Parameter | Meaning
--- | ---
add | Add the gid array of the group message blocking (optional)
remove | Remove the gid array of group message blocking(optional)

#### Example Response

```
< HTTP/1.1 204 OK
< Content-Type: application/json
```

### Ban group members

```
PUT  /groups/messages/{gid}/silence?status={status}
```

**Request body**

```
[ "username1", "username2"]
备注：username json数组
```

**Request Params**

```
status：开启或关闭禁言 true表示开启 flase表示关闭
```

#### Example Response

```
< HTTP/1.1 204 OK
< Content-Type: application/json
```

## Friends

### Add friend

```
POST  /v1/users/{username}/friends
```

**Request Params**

+ json array: Indicates the list of user names to be added. Maximum limit is 500.

#### Example Request

```
["user01","user02"] 
```

#### Example Response

```
< HTTP/1.1 201
< Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

#### Error Code

+ 899003: format of Request Body json does not meet the requirements, and json parameter does not meet the requirements;
+ 899002: user does not exist
+ 899070: has added friends

### Delete friend

```
DELETE  /v1/users/{username}/friends
```

**Request Params**

+ The json array represents the list of user names to be removed. The maximum limit is 500.

#### Example Request

```
["user01","user02"] 
```

#### Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

#### Error Code

+ 899003: format of Request Body json does not meet the requirements, and json parameter does not meet the requirements;
+ 899002: user does not exist;

### Update friend notes

```
PUT  /v1/users/{username}/friends
```

**Request Params**

+ note_name indicates the list of friends to add. Format: Supported characters of byte(64) excludes "\n" "\r".
+ others: Other note information, Format: byte(250) supports all characters, including Emoji.
+ Username;
+ Support batch modification with maximum limit as 500.

#### Example Request

```
[{
    "note_name": "new note name",
    "others": “好友备注文档",
    "username":"user01"
}]
```

#### Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

#### Error Code

+ 899003: format of Request Body json does not meet the requirements, and json parameter does not meet the requirements;
+ 899002: user does not exist;

### Get friend list

```
GET  /v1/users/{username}/friends
```

**Request Params**

+ N/A

#### Example Request

#### Example Response

```
< HTTP/1.1 200 NO Content
< Content-Type: application/json; charset=utf-8
```

**Response Data**

```
[{
    "username": "javen",
    "nickname": "hello",
    "avatar": "/avatar",
    "birthday": "1990-01-24 00:00:00",
    "gender": 0,
    "signature": "orz",
    "region": "shenzhen",
    "address": "shenzhen",
    "mtime": "2015-01-01 00:00:00",
    "ctime": "2015-01-01 00:00:00",
    "note_name":"= =",
    "others":"test",
    "appkey":"pojkasouduioadk"
}]
```

#### Error Code

+ 899003: format of Request Body json does not meet the requirements, and json parameter does not meet the requirements;
+ 899002: user does not exist;

## Cross-application

### Cross-application manage group members

```
POST  /v1/cross/groups/{gid}/members
```

**Request Params**

+ add json array: Indicates the user to add to the group (optional)
+ remove json array: Indicates the user to remove from the group (optional)
+ appkey: The appkey of user managed is required

at least one of the add and remove

#### Example Request

```
[{
    "appkey":" 4f7aef34fb361292c566a1cd",
    "add": [
        "test1",
        "test2"
    ],
    "remove": [
        "name3",
        "name4"
    ]
}]
```

#### Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

Remarks: The group wille deleted when the group has no members

#### Error Code

+ 899003: format of Request Body json does not meet the requirements, and json parameter does not meet the requirements;
+ 899002: user does not exist;
+ 899012: There are not enough places to add group members;
+ 899014: users do not exist in the group
+ 899011: users already exist in the group

### Get a group member list across applications

```
GET /v1/cross/groups/{Group id}/members/
```

**Request Params**

+ Group id

#### Example Response

+ JsonObject UID: array

```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[{
    "username": "javen",
    "nickname": "hello",
    "avatar": "/avatar",
    "birthday": "1990-01-24 00:00:00",
    "gender": 0,
    "signature": "orz",
    "region": "shenzhen",
    "address": "shenzhen",
    "flag":0,
    "appkey":"appkey"
}]
```

+ flag
     - 0 - common group members
     - 1 - Group owner

### Get user groups across applications

```
GET /v1/cross/users/{username}/groups
```

**Request Params**

+ username

#### Example Response

```
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8

[ {
    "gid": 12345,
    "name": "jpush",
    "desc": "push",
    "appkey": "dcf71ef5082057832bd44fbd",
    "max_member_count": 200,
    "mtime": "2014-07-01 00:00:00",
    "ctime": "2014-06-05 00:00:00",
    "appkey":"appkey"
}]
```

### Add a blacklist across applications

```
Put /v1/cross/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Put /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ username: An array of added users
+ appkey: appkey to which the user belongs

**Request Body**

```
 [{

    "appkey":"appkey",
    "usernames": [
        "test1", "test2"
    ]

}]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Cross-application remove blacklist

```
Delete /v1/cross/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Delete /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ username: An array of removed users
+ appkey: appkey to which the user belongs

**Request Body**

```
[{
    "appkey": "appkey",
    "usernames": [
        "test1", "test2"
    ]
}]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Cross-application list of blacklists

```
Get /v1/cross/users/{username}/blacklist
```

#### Example Request

**Request Header**

```
Get /v1/cross/users/{username}/blacklist
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ username

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
[{
    "username": "javen",
    "nickname": "hello",
    "avatar": "/avatar",
    "birthday": "1990-01-24 00:00:00",
    "gender": 0,
    "signature": "orz",
    "region": "shenzhen",
    "address": "shenzhen",
    "mtime": "2015-01-01 00:00:00",
    "ctime": "2015-01-01 00:00:00",
    "appkey":"appkey"
}]
```

### Cross-application Do-Not-Disturb Settings

```
POST  /v1/cross/users/{username}/nodisturb
```

#### Example Request

**Request Header**

```
POST  /v1/cross/users/{username}/nodisturb
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ single: single chat DND, supports adding or removing array (optional)
+ group: group chat DND, supports adding or removing array (optional)
+ appkey: appkey of targets

**Request Body**

```
[ {
    "appkey":"appkey1",    "single":{          "add":[             "username1",          "username2"       ]    },    "group":{          "add":[             110000101       ],       "remove":[             1000001111       ]    } 
}]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

#### Error Code

+ 899003: username is illegal;
+ 899002: user does not exist
+ 899051: group does not exist
+ 899052: Set the group message blocj and the setting of group block is already open
+ 899053: Set the group message blocj and the setting of group block is already turned off

### Add friends across applications

```
POST  /v1/cross/users/{username}/friends
```

#### Example Request

**Request Header**

```
POST  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ appkey: Appkey to which the user belongs (required)
+ json array of users username: up to 500 (required)

**Request Body**
```
{
   "appkey":"appkey1",    "users":         [            "username1",         "username2"       ]     
}
```

#### Example Response

**Response Header**

```
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Delete friends across applications

```
DELETE  /v1/cross/users/{username}/friends
```

#### Example Request

**Request Header**

```
DELETE  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ appkey: The appkey to which the user belongs (required)
+ json array of users username: up to 500 (required)

**Request Body**
```
 {
   "appkey":"appkey1",    "users":         [            "username1",         "username2"       ]     }
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Update friend notes across applications

```
PUT  /v1/cross/users/{username}/friends
```

#### Example Request

**Request Header**

```
PUT  /v1/cross/users/{username}/friends
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ appkey: The appkey to which the user belongs (required)
+ note_name: Indicates the list of friends to add. Format: Supported characters of byte(64) excludes "\n" "\r".
+ others: Other note information, Format: byte(250) supports all characters, including Emoji.

**Request Body**

```
[{
    "note_name": "new note name",
    "others": “好友备注文档" ,
    "username":"user01",
    "appkey":"appkey"
}]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Cross-application manage chat room members

```
POST  /cross/chatroom/{room_id}/members
```

**Request Params**

+ add json array: Representing the user to add to the chat room (optional)
+ remove json array: Indicates the user to delete from the chat room (optional)
+ appkey: appkey to which the managed user belongs (required)

add/remove:at least one of the two

#### Example Request

```
[{
    "appkey":" 4f7aef34fb361292c566a1cd",
    "add": [
        "test1",
        "test2"
    ],
    "remove": [
        "name3",
        "name4"
    ]
}]
```

#### Example Response

```
< HTTP/1.1 204 NO Content
< Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

## Sensitive Words

### Add sensitive words

```
POST  /v1/sensitiveword
```

#### Example Request

**Request Header**

```
POST  /v1/sensitiveword
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ N/A

**Request Body**

+ Array of Sensitive Words: A word with a length of up to 10, defaults to 100 sensitive words, and contact with [business team](https://www.jiguang.cn/accounts/business/form?from=im) for higher demands

```
["FUCK"]
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```
**Response Data**

+ N/A

### Modify sensitive words

```
PUT  /v1/sensitiveword
```

#### Example Request

**Request Header**

```
PUT  /v1/sensitiveword
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ N/A

**Request Body**

+ old_word: old sensitive word,
+ new_word: new sensitive word

```
{"new_word":"fuck", "old_word":"FUCK"}
```

#### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Delete sensitive words

```
DELETE /v1/sensitiveword
```

#### Example Request

**Request Header**

```
DELETE  /v1/sensitiveword
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ N/A

**Request Body**

+ word: sensitive words deleted

```
{"word":"fuck"}
```

### Example Response

**Response Header**

```
HTTP/1.1 204 NO Content
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Get a list of sensitive words

```
GET /v1/sensitiveword
```

#### Example Request

**Request Header**

```
GET  /v1/sensitiveword?start={start}&count={count}
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ start: start number, starting from 0
+ count: number of queries, up to 2000

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
    "start": 2,
    "count": 1,
    "words": [
{
    "name": "fuck",
    "itime": "1970-01-17 16:49:11"
}
],
    "total": 3
}
```

### Update the status of sensitive words

```
PUT /v1/sensitiveword/status
```

#### Example Request

**Request Header**

```
PUT  /v1/sensitiveword/status?status=0
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ status: switch status of sensitive words, 1 means turn on filtering, 0 means turn off sensitive word filtering

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8
```

**Response Data**

+ N/A

### Get the status of sensitive words

```
GET /v1/sensitiveword/status
```

#### Example Request

**Request Header**

```
GET  /v1/sensitiveword/status
Content-Type: application/json; charset=utf-8
```

**Request Params**

+ N/A

**Request Body**

+ N/A

#### Example Response

**Response Header**

```
HTTP/1.1 200
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
 {"status": 1}
```

## Overview of chat room fields

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Parameter</th>
            <th>Meaning</th>
            <th>Limits of character length</th>
        </tr><tr>
            <td>name</td>
            <td>Chat room name (required)</td>
            <td>Byte(0~64)</td>
        </tr><tr>
            <td>owner_username</td>
            <td>Creator of Chat room (required)</td>
            <td>Byte (4~128)</td>
        </tr><tr>
            <td>description</td>
            <td>Chat room description (optional)</td>
            <td>Byte(250)</td>
        </tr><tr>
            <td>members_username</td>
            <td>Member list of chat room (optional)</td>
            <td></td>
        </tr><tr>
            <td>ctime</td>
            <td>Creation time</td>
            <td></td>
        </tr><tr>
            <td>max_member_count</td>
            <td>Maximum number of members</td>
            <td></td>
        </tr><tr>
            <td>total_member_count</td>
            <td>Current total number</td>
            <td></td>
        </tr><tr>
            <td>flag</td>
            <td>Forbidden signs</td>
            <td>0 means not banned, 1 means open the ban</td>
        </tr>
    </table>
</div>

## Chat room maintenance

### Create a chat room

```
POST /v1/chatroom/
```

**Request Body**

```
{"owner_username":"liming", "name": "测试聊天室", "description":"测试", "members_username":[]}
```

**Request Params**

+ owner_username (required) owner the chat room
+ name (required) chat room name
+ members_username (optional) username of members
+ description (optional) Description

#### Example Response
```
 HTTP/1.1 201 Created
 Content-Type: application/json

{
"chatroom_id": 1000000
}
```

#### Get chat room details

```
POST /v1/chatroom/batch
```

**Request Params**

[10000001,10000002] roomid数组

#### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "id": 10000001,
        "owner_username": "xiaoming",
        "max_member_count": 10000,
        "appkey": "4f7aef34fb361292c566a1cd",
        "name": "test",
        "description": "test",
        "total_member_count": 2,
        "ctime": "2017-11-27 18:38:25"
    }，
 {
        "id": 10000002,
        "owner_username": "xiaoming",
        "max_member_count": 10000,
        "appkey": "4f7aef34fb361292c566a1cd",
        "name": "test",
        "description": "test",
        "total_member_count": 2,
        "ctime": "2017-11-27 18:38:25"
    }
]
```

### GET Get a list of user’s chat rooms

```
 GET /v1/users/{username}/chatroom
```

#### Example Request

```
GET /v1/users/xiaoming/chatroom
```

#### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "id": 100000,
        "owner_username": "xiaoming",
        "max_member_count": 10000,
        "appkey": "4f7aef34fb361292c566a1cd",
        "name": "test",
        "description": "test",
        "total_member_count": 2，
       "ctime": "2017-11-27 18:38:25"
    }，
 {
        "id": 10000001,
        "owner_username": "xiaoming",
        "max_member_count": 10000,
        "appkey": "4f7aef34fb361292c566a1cd",
        "name": "test",
        "description": "test",
        "total_member_count": 2，
        "ctime": "2017-11-27 18:38:25"
    }
]
```

### GET Get a list of chat rooms under the app

```
GET /v1/chatroom?start={start}&count={count}
```

#### Example Request

```
GET  /v1/chatroom?start=0&count=10
```

#### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
    "total": 1,
    "rooms": [
        {
            "id": 62,
            "owner_username": "xiaoming",
            "max_member_count": 10000,
            "appkey": "4f7aef34fb361292c566a1cd",
            "name": "test",
            "description": "test"，
             total_member_count": 11,
            "ctime": "2017-11-27 18:38:25"
        }
    ],
    "start": 0,
    "count": 1
}
```

#### Update chat room information

```
 PUT /v1/chatroom/{room_id}
```

#### Example Request

```
 PUT /v1/chatroom/111000001
```

**Request Body**

```
{"owner_username":"135380113231", "name": "中国人", "description":"说什么来这"}
```

#### Example Response

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8
```

### Delete chat room

```
DELETE /v1/chatroom/{room_id}
```

#### Example Request

```
DELETE  /v1/chatroom/100000
```

#### Example Response

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8
```

### Modify user banned state

```
 PUT /v1/chatroom/{room_id}/forbidden/{username}?status={status}
```

Status 0 means not banned, 1 means open the ban (required)

#### Example Request

```
PUT  /v1/chatroom/100000/forbidden/caiyh?status=1
```

#### Example Response

```
 HTTP/1.1 204 OK
 Content-Type: application/json; charset=utf-8
```

### Get a list of chat room members

```
GET /v1/chatroom/{room_id}/members?start={start}&count={count}
```

**Request Params**

+ room_id

#### Example Response

+ username
+ ctime
+ flag

```
 HTTP/1.1 200 OK
 Content-Type: application/json

{
    "total": 2,
    "users": [
        {
            "username": "13538013231",
            "flag": 0,
            "room_ctime": "2017-11-17 08:57:54",
            "mtime": "2017-10-30 17:24:17",
            "ctime": "2017-10-30 17:24:17"
        },
        {
            "username": "xia_12",
            "flag": 0,
            "room_ctime": "2017-11-16 19:13:07",
            "mtime": "2017-02-08 17:56:04",
            "ctime": "2017-02-08 17:56:04"
        }
    ],
    "count": 2,
    "start": 0
}
```

### Add chat room members

```
 PUT /v1/chatroom/{room_id}/members
```

**Request Params**

+ json array of username: supports up to 3000

#### Example Response

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8
```

### Remove chat room members

```
DELETE /v1/chatroom/{room_id}/members
```

**Request Params**

+ json array of username: supports up to 3000

### Example Response

```
HTTP/1.1 204
Content-Type: application/json; charset=utf-8
```

## Configuration

### Set SDK-API user registration switch

Open or close the SDK-API user registration.

```
PUT /sdkregister/status?status={status}
```

#### Example Request

```
PUT /sdkregister/status?status=0
```

**Request Params**

JSON Array.

+ status:0 is off, indicating SDK-API registration is not provided, 1 is on

#### Example Response

```
 HTTP/1.1 204 Created
 Content-Type: application/json

Response Data

N/A
```

### Get SDK-API user registration switch

```
get /sdkregister/status
```

#### Example Request

```
get /sdkregister/status
```

#### Example Response

```
 HTTP/1.1 200
 Content-Type: application/json

Response Data
{
"status": 0
}
status： 0为关闭，不提供SDK-API 注册功能，1为开启
```

## HTTP return

Reference documentation of HTTP return code: [HTTP-Status-Code](https://docs.jiguang.cn/jpush/server/push/http_status_code/)

### Example Error Response

```
 HTTP/1.1 401 Unauthorized
 Content-Type: application/json

{
  "error": {
        "code": 899008,
        "message": "Basic authentication failed"
     }
}
```

## Definition of business error code

[IM Server ErrorCode](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)
