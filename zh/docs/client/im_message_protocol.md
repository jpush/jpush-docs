# IM 消息协议

### Summary 概述

JPush IM 对于不同的消息类型，有一个 JSON 格式的消息协议。这个业务级别的协议，由发送者编码，由接收者解码，并处理接收到的消息。

面向开发者接口提供的发送消息接口，也需要遵循此文档定义来组装消息，以发往客户端。


### Protocol 协议定义

+ version Number 
	+ 必须。
	+ 协议版本号。第一版本：1，以此类推。
+ target_type String 
	+ 必须。
	+ 接收者类型。
	+ 选项：single单聊, group群聊
+ target_id  String
	+ 必须。
	+ 接收者ID。可能值：{username}, {gid} 
	+ 接收方可用此字段，校验消息是不是发给自己的。
+ target_name String 
	+ 可选。
	+ 接收者的展示名。
+ from_type String 
	+ 必须。
	+ 发送者类型。选项：user, robot, api, console...  
	+ 用户只允许发送from_type = user 的消息。
+ from_id Number 
	+ 必须。
	+ 发送者 username
+ from_name String 
	+ 可选。
	+ 发送者展示名。
+ create_time String 
	+ 必须。
	+ 消息发送时间。用于展示目的。
+ msg_type String 
	+ 必须。
	+ 选项：text, image, voice, location, custom 消息命令
+ msg_body JsonObject 
	+ 必须。
	+ 消息实体。

### Message Body 消息体定义

根据 msg_type 的不同，msg_body 里会有以下字段信息。

+ extras
	+ 可选。
	+ 用于附加参数。所有的消息类型都可以有。

msg_type = text

+ content String
	+ 必须。
	+ 文本类型消息内容。

msg_type = voice

+ media_id String
	+ 必须。
	+ 媒体文件上传到得到的KEY，用于生成下载URL。
+ media_crc Number
	+ 必须。
	+ 文件的 CRC 校验码。
+ duration Number
	+ 必须。
	+ 语音时长（单位：秒）
+ format String
	+ 必须。
	+ 语音类型。

msg_type = image

+ media_id String
	+ 必须。
	+ 媒体文件上传到得到的KEY，用于生成下载URL。
+ media_crc Number
	+ 必须。
	+ 文件的 CRC 校验码。
+ width Number
	+ 必须。
	+ 原图片宽度。
+ height Number
	+ 必须。
	+ 原图片调度。
+ format String
	+ 可选。
	+ 图片格式。
+ img_link String
	+ 可选。
	+ 图片链接。



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
	"create_time": "2015-02-12 15:49 09",
	
	"msg_type": "text",
	"msg_body": {
		"content": "Hello, JPush IM!"		}
}
```

### See Also 相关文档

+ [IM SDK for Android](../../client/im_sdk_android/)
+ [IM SDK for iOS](../../client/im_sdk_ios/)
+ [JPush IM 指南](../../guideline/jpush_im_guide/)
+ [JPush IM REST API](../../server/rest_api_im/)
