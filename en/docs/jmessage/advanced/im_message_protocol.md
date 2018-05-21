# Message Agreement

## Overview

JMessage has a message protocol in JSON format for different message types. This service-level protocol is encoded by the sender, decoded and processed by the receiver.

The sending message interface provided for the developer interface also needs to follow this document definition to assemble the message for sending to the client.

## Protocol Definition

+ version Number
	+ Required
	+ Version number of protocol. The first version: 1, and so on.
+ target_type String
	+ Required
	+ Type of recipient
	+ Options: single, group
+ target_id String
	+ Required
	+ Receiver ID.
	+ Possible values: ${username}, ${gid}
	+ The recipient can use this field to check whether the message was sent to himself.
+ target_name String
	+ Optional.
	+ Display name of recipient.
+ from_type String
	+ Required
	+ Source of sender
	+ Options: user, robot, admin, .... can be used to extend specific news sources.
	+ Users are only allowed to send messages like from_type = user.
+ from_id String
	+ Required
	+ Username of sender
+ from_name String
	+ Optional
	+ Display name of sender
+ from_platform String
	+ Required
	+ Platform of sender
	+ Options: a - Android, i - iOS, w - WinPhone, web - Web
+ create_time Number
	+ Required
	+ The time message was sent.
	+ Accurate to second.
+ msg_type String
	+ Required
	+ Options: text, voice, image, custom
+ msg_body JsonObject
	+ Required
	+ Message entity.

## Message Body Definition

According to the different msg_type, msg_body will have the following field information.

+ extras
	+ Optional.
	+ JsonObject
	+ For additional parameters. All message types can have this field.

msg_type = text

+ text String
	+ Required
	+ Message content of text type.

msg_type = voice

+ media_id String
	+ Required
	+ The media file is uploaded to the obtained KEY for generating a download URL.
+ media_crc32 Number
	+ Required
	+ The file's CRC32 checksum.
+ duration Number
	+ Required
	+ Voice duration (unit: seconds)
+ format String
	+ Required
	+ Voice type.
+ fsize Number
	+ Required
	+ File size (bytes)

msg_type = image

+ media_id String
	+ Required
	+ The media file is uploaded to the obtained KEY for generating a download URL.
+ media_crc32 Number
	+ Required
	+ The file's CRC32 checksum.
+ width Number
	+ Required
	+ Original image width.
+ height Number
	+ Required
	+ Original image scheduling.
+ format String
	+ Optional.
	+ Image format.
+ fsize Number
	+ Required
	+ File size (bytes)
+ img_link String
	+ Optional.
	+ Picture links

msg_type = custom

Developer custom fields. JsonObject.

## Message Example

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

## Related documentation

+ [JMessage Product Brief](../guideline/jmessage_guide/)
+ [IM REST API](https://docs.jiguang.cn/jmessage/server/rest_api_im/)
+ [Download](https://docs.jiguang.cn/jmessage/resources/)



