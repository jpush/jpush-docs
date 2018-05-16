# 实时消息路由

## 使用场景

极光可以帮助开发者实现以下场景：

1. 在 APP 自己的服务端实时保存聊天历史
2. 开发者可以实现针对客户消息的内容进行自动回复

如需要开通此功能，请联系：[商务客服](https://www.jiguang.cn/accounts/business/form)；如果开发者没有实时性需求，建议使用免费的IM REST Report拉取历史消息。


## 目前服务支持https和http回调

关于开发者鉴权的问题，为了防止开发者服务被随意调用，开发者服务验证采用 HTTP Basic 机制，即 HTTP Header（头）里加一个字段（Key/Value对）：

Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

msg callback在请求的时候会带上Authorization: Basic base64_auth_string让开发者服务进行验证

### https 接口采用post方法 

Request header

```
  Content-Type: application/json; charset=utf-8
```


Request Body
 
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

与REST Report历史消息获取的消息格式相同

### msg callback 所需的成功响应

Response

```
  HTTP/1.1 200  
  Content-Type: application/json; charset=utf-8

```

