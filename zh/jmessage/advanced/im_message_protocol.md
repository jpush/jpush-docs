# 消息协议

## 概述

JMessage 对于不同的消息类型，有一个 JSON 格式的消息协议。这个业务级别的协议，由发送者编码，由接收者解码，并处理接收到的消息。

面向开发者接口提供的发送消息接口，也需要遵循此文档定义来组装消息，以发往客户端。


## 协议定义

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
+ create_time Number 
	+ 必须。
	+ 消息发送时间。
	+ 精确到秒。
+ msg_type String 
	+ 必须。
	+ 选项：text, voice, image, file, video, location, custom
+ msg_body JsonObject 
	+ 必须。
	+ 消息实体。
+ from_appkey String
	+ 可选
	+ 发送者所属应用appkey

## 消息体定义

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

msg_type = file

+ media_id String
	+ 必须。
	+ 媒体文件上传到得到的KEY，用于生成下载URL。
+ media_crc32 Number
	+ 必须。
	+ 文件的 CRC32 校验码。
+ fsize  Number
	+ 必须
	+ 文件大小（字节数）
+ fname String
	+ 必须
	+ 文件名

msg_type = location

+ latitude Number
	+ 必须。
	+ 纬度
+ longitude Number
	+ 必须。
	+ 经度
+ scale  Number
	+ 必须
	+ 缩放比例
+ lable String
	+ 必须
	+ 位置信息

msg_type = video

+ video JsonObject 
	+ 必须
	+ 视频文件信息， 使用<FileObject>消息体子类型,类型定义见下文
+ duration Number 
	+ 必须
	+ 视频时长
thumb JsonObject 
	+ 可选
	+ 缩略图文件信息， 使用<ImageObject>消息体子类型,类型定义见下文

msg_type = custom

开发者自定义字段。JsonObject。


### 消息体子类型定义

FileObject

+ media_id String 
	+ 必须
	+ 媒体文件上传之后得到的key，用于生成下载的URL
+ media_crc32 Number 
	+ 必须
	+ 文件的 CRC32 校验码。
+ fsize Number 
	+ 必须
	+ 文件大小
+ fname String 
	+ 必须
	+ 发送与接收到的文件名

ImageObject

+ media_id String  
	+ 必须
	+ 媒体文件上传之后得到的key，用于生成下载的URL
+ media_crc32 Number 
	+ 必须
	+ 文件的 CRC32 校验码。
+ format String 
	+ 必须
	+ 图片格式
+ width Number 
	+ 必须
	+ 图宽度
+ height Number 
	+ 必须
	+ 图高度
+ fsize Number 
	+ 必须
	+ 文件大小

## 消息示例

```
文字消息
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

图片消息
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

语音消息
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
    	"fsize" :12344,
     	"duration": 6
    }
}

位置信息
{
	"version":1,
	"target_type":"single",	
	"target_id":"oooo",	
	"target_appkey":"4f7aef34fb361292c566a1cd",
	"from_type":"admin",
	"from_id":"oooo",
	"msg_type":"location",
	"msg_body":{
		"latitude":111.2,
		"longitude":22.3,
		"scale":500,
		"label":"xx省xx市xx区xx街道"
	}
}

视频信息
{
	"version":1,
	"target_type":"single",	
	"target_id":"oooo",	
	"target_appkey":"4f7aef34fb361292c566a1cd",
	"from_type":"admin",
	"from_id":"oooo",
	"msg_type":"video",
	"msg_body":{
		"duration":10,
		"thumb":{
			"fsize":20736,
			"width":72,
			"format":"png",
			"media_crc32":2565087609,
			"media_id":"qiniu/image/a/707F13B42CEDB275702938DD13ED76E8.png",
			"height":72
		},
		"video":{
			"fname":"testvideo",
			"fsize":2900883,
			"media_crc32":428957395,
			"media_id":"qiniu/file/a/2745EACC984972A4F914C7614CEC1572"
		}
	}
}

自定义消息
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

## 相关文档

+ [JMessage 产品简介](../guideline/jmessage_guide/)
+ [IM REST API](https://docs.jiguang.cn/jmessage/server/rest_api_im/)
+ [资源下载](https://docs.jiguang.cn/jmessage/resources/)



