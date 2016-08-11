# IM 消息协议

### Summary 概述

JMessage 对于不同的消息类型，有一个 JSON 格式的消息协议。这个业务级别的协议，由发送者编码，由接收者解码，并处理接收到的消息。

面向开发者接口提供的发送消息接口，也需要遵循此文档定义来组装消息，以发往客户端。


### Protocol 协议定义

+ version Number 
	+ 必须。
	+ 协议版本号。第一版本：1，以此类推。
+ target_type String 
	+ 必须。
	+ 接收者类型。
	+ 选项：single, group
+ target_id  String
	+ 必须。
	+ 接收者ID。
	+ 可能值：${username}, ${gid} 
	+ 接收方可用此字段，校验消息是不是发给自己的。
+ target_name String 
	+ 可选。
	+ 接收者的展示名。
+ from_type String 
	+ 必须。
	+ 发送方来源。
	+ 选项：user, robot, admin, ...。可用于扩展特定消息来源。 
	+ 用户只允许发送 from_type = user 的消息。
+ from_id String 
	+ 必须。
	+ 发送者 username
+ from_name String 
	+ 可选。
	+ 发送方展示名。
+ from_platform String
	+ 必须。
	+ 发送方平台。
	+ 可选项： a - Android, i - iOS, w - WinPhone, web - Web
+ create_time Number 
	+ 必须。
	+ 消息发送时间。
	+ 精确到秒。
+ msg_type String 
	+ 必须。
	+ 选项：text, voice, image, custom
+ msg_body JsonObject 
	+ 必须。
	+ 消息实体。

### Message Body 消息体定义

根据 msg_type 的不同，msg_body 里会有以下字段信息。

+ extras
	+ 可选。
	+ JsonObject
	+ 用于附加参数。所有的消息类型都可以带此字段。

msg_type = text

+ text String
	+ 必须。
	+ 文本类型消息内容。

msg_type = voice

+ media_id String
	+ 必须。
	+ 媒体文件上传到得到的KEY，用于生成下载URL。
+ media_crc32 Number
	+ 必须。
	+ 文件的 CRC32 校验码。
+ duration Number
	+ 必须。
	+ 语音时长（单位：秒）
+ format String
	+ 必须。
	+ 语音类型。
+ fsize  Number
	+ 必须
	+ 文件大小（字节数）

msg_type = image

+ media_id String
	+ 必须。
	+ 媒体文件上传到得到的KEY，用于生成下载URL。
+ media_crc32 Number
	+ 必须。
	+ 文件的 CRC32 校验码。
+ width Number
	+ 必须。
	+ 原图片宽度。
+ height Number
	+ 必须。
	+ 原图片调度。
+ format String
	+ 可选。
	+ 图片格式。
+ fsize  Number
	+ 必须
	+ 文件大小（字节数）
+ img_link String
	+ 可选。
	+ 图片链接。

msg_type = custom

开发者自定义字段。JsonObject。


### Examples 消息示例

```
{
	"version": 1, 
	"target_type": "single",
	"target_id": "javen",
	"target_name": "Javen Fang",
	"from_type": "user",
	"from_id": "fang", 
	"from_name": "Fang Javen", 
	"create_time": 135432432187,
	"msg_type": "text",
	"msg_body": {
		"text": "Hello, JPush IM!"	
	}
}
```

### See Also 相关文档

+ [极光IM 指南](../guideline/jmessage_guide/)
+ [IM SDK for Android](../client/im_sdk_android/)
+ [IM SDK for iOS](../client/im_sdk_ios/)
+ [IM REST API](../server/rest_api_im/)
+ [IM 业务对象](im_objects/)


