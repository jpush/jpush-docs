# Business Objects

There are some common business objects in various types of externally exposed interfaces. This document defines these business objects.

These business objects are defined in JSON format. In the Android SDK, the API exposure in the iOS SDK is an object of the corresponding language, which is not applied in this document.

## User Information

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

## Group information

```
{
    "gid": 13579,                            // 群ID，则服务器端创建
    "owner_username": "tom",                 // 群主用户名
    "group_name": "群名称",                   // 群名称。可任意指定
    "group_desc": "群描述",                   // 群描述
    "appkey": "dcf71ef5082057832bd44fbd",    // 应用Appkey
    "level": 3,                              // 群组级别
    "mtime": "2014-07-01 00:00:00",          // 更新时间
    "ctime": "2014-07-01 00:00:00"           // 创建时间
}
```

## Event Notification

```
{
    "event_type: "create_group",            // 事件类型
    "from_username": "",                    // 发起事件的用户
    “gid”: 13579,                           // 触发事件所在的群组（群组相关事件需要填写）
    "to_username_list": ["eddie", "annie"], // 事件目标用户
    "description": "the event is due to...",// 事件描述信息
    "ctime": "2014-07-01 00:00:00"          // 事件创建时间
}
```

Event type

+ create_group
+ exit_group
+ add_members
+ remove_members

## Chat Message

Defined in a separate document: [IM Message Protocol](../advanced/im_message_protocol/)

## Related Documents

+ [JMessage  Product Brief](../guideline/jmessage_guide/)
+ [Android SDK Development Guide](../client/im_sdk_android/)
+ [iOS SDK Development Guide](../client/im_sdk_ios/)
+ [Download](https://docs.jiguang.cn/jmessage/resources/)

