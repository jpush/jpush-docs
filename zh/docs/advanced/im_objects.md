# IM 业务对象

IM 在各类对外暴露的接口里，有一些公共的业务对象。本文档集中定义这些业务对象。

这些业务对象都以 JSON 格式定义。在 Android SDK, iOS SDK 里的 API 暴露是相应语言的对象，不适用本文档。

### UserInfo 用户信息

```
{
    "username": "chicken",
    "nickname": "Tom Chick",
    "star": 2,
    "avatar": "qiniu/image/uipreqfdsakl",     // 用户头像。存储的路径
    "gender": 0,                              // 用户性别
    "signature": "I am a ...",                // 签名
    "region": "深圳",                          // 区域
    “address”: "某街某号",                     // 详细地址
    "mtime": "2015-03-03 11:00:00",           // 修改时间
    "ctime": "2015-03-03 11:00:00",           // 创建时间
}
```

### GroupInfo 群组信息

```
{
    "gid": 13579,                            // 群组ID。由服务器端生成。长整型
    "owner_username": "tom",                 // 群主用户名
    "group_name": "群名称",                   // 群名称。可任意指定
    "group_desc": "群描述",                   // 群描述
    "members_username": ["eddie","annie"]    // 成员用户名
```

### EventNotification 事件通知

```
{
    "event_type: "create_group",            // 事件类型
    "from_username": "",                    // 发起事件的用户
    “gid”: 13579,                           // 触发事件所在的群组（群组相关事件需要填写）
    "to_username_list": ["eddie", "annie"], // 事件目标用户
    "description": "the event is due to..." 
}
```

事件类型：

- create_group
- exit_group
- add_members
- remove_members

### See Also 相关文档

+ [IM 消息协议](../im_message_protocol/)
+ [极光IM 指南](../../guideline/jmessage_guide/)
+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [IM REST API](../../server/rest_api_im/)

