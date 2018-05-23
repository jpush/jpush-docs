# Real-time Message Routing

## Usage scenarios

Jiguang can help developers achieve the following scenarios:

    1. Save chat history in real time on APP's own server
    2. Developers can automatically respond to the content of customer messages

If developers need to activate this feature, please contact: [Business customer service](https://www.jiguang.cn/accounts/business/form); if developers do not have real-time requirements, it is recommended to use the free IM REST Report to pull history messages.

## Current service supports https and http callbacks

Regarding developer authentication, in order to prevent developer services from being called at will, the verification of developer service uses HTTP Basic mechanism, that is, adding a field (Key/Value pair) to the HTTP Header:

Authorization: Basic base64_auth_string

The generation algorithm of base64_auth_string is：base64(appKey:masterSecret)

That is, adding a colon to the appKey, plus the string assembled by masterSecret, and do a base64 conversion then.

Msg callback brings Authorization: Basic base64_auth_string to verify developer service when requested

### The https interface uses the post method

**Request header**

```
Content-Type: application/json; charset=utf-8
```

**Request Body**
```
 {
 "total":1,
 "messages":[
 {
  "target_type":"single",
  "msg_type":"text",
  "target_name":"JMessage",
  "target_id":"10000002",
  "from_id":"10000001",
  "from_name":"JPush",
  "from_type":"user",
  "from_platform":"a",
  "msg_body":{
   "text":"text",
   "extras":{
   }
  },
 "create_time":1446016259,
 "version":1,
 "msgid":12345678,
 "msg_level": 0,
 "msg_ctime" : 1466866468352 // 服务器接收到消息的时间，单位毫秒
 }
 ]
}
```

Same format as the REST Report history message

### Successful response required by msg callback

Response

```
  HTTP/1.1 200
  Content-Type: application/json; charset=utf-8
```
