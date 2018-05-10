Push API v3

This is the most recent version of the Push API.
Compared to the API v2 version, improvements of the v3 version are:：
    • Based solely on https, no longer provides http access；
    • Use HTTP Basic Authentication for access authorization. This way, the entire API request can be completed by using common HTTP tools such as curl, browser plugins, etc；
    • Push content is completely in JSON format;；
    • Supported features have been improved: Support for multiple tags and operations; can send notifications or custom messages alone as well as at the same time; windows phone currently only supports notifications.

Push Overview
Function Description
Push a notification or message to a single device or a list of devices.
Pushed content can only be a push object represented by JSON
Call Address
https://api.jpush.cn/v3/push
If the created Jiguang application is allocated to the Beijing computer room and the API caller's server is also located in Beijing, it is more suitable to call the API of the Jiguang Beijing computer room, which can improve the response speed.
The room where the application is located can be seen through Application Settings -> Application Info of the Jiguang Web Console. If the application is located in the Beijing computer room, the calling address of each API will be given at the same time.
Call address of Push API in Beijing computer room： https://bjapi.push.jiguang.cn/v3/push
For the detailed mapping relationship, see the "Server Location" information in "Application Information".
Request Example
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush !","android":{"extras":{"android-key1":"android-value1"}},"ios":{"sound":"sound.caf","badge":"+1","extras":{"ios-key1":"ios-value1"}}}}'

> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
Return Example
< HTTP/1.1 200 OK
< Content-Type: application/json
{"sendno":"18","msg_id":"1828256757"}

Call Verification
Add a field (Key/Value pair) in the HTTP Header
Authorization: Basic base64_auth_string
The generation algorithm of base64_auth_string is: base64(appKey:masterSecret)
That is, add a colon to the appKey, plus the string assembled by masterSecret, and do a base64 conversion.

Pushing Objects
A push object expressed in JSON format, represents a push-related piece of information
Keyword
Option 
Meaning
platform
Required
Settings of push platform
audience
Required
Designation of push device
notification
Optional
Notification content body is the content that is pushed to the client. At least one between it and message must exist and they can coexist.
message
Optional
Message content body is the content that is pushed to the client. At least one between it and message must exist and they can coexist
sms_message
Optional
SMS channels supplements the delivery of content body
options
Optional
Push parameters
cid
Optional
An identifier defined to prevent the duplicate pushes from the server caused by the retrying of api caller

Examples and Descriptions
{
    "cid": "8103a4c628a0b98974ec1949-711261d4-5f17-4d2f-a855-5e5a8909b26e",
    "platform": "all",
    "audience": {
        "tag": [
            "深圳",
            "北京"
        ]
    },
    "notification": {
        "android": {
            "alert": "Hi, JPush!",
            "title": "Send to Android",
            "builder_id": 1,
            "extras": {
                "newsid": 321
            }
        },
        "ios": {
            "alert": "Hi, JPush!",
            "sound": "default",
            "badge": "+1",
            "extras": {
                "newsid": 321
            }
        }
    },
    "message": {
        "msg_content": "Hi,JPush",
        "content_type": "text",
        "title": "msg",
        "extras": {
            "key": "value"
        }
    },
    "sms_message":{
        "content":"sms msg content",
        "delay_time":3600
    },
    "options": {
        "time_to_live": 60,
        "apns_production": false,
        "apns_collapse_id":"jiguang_test_201706011100"
    }
}

platform：Push Platform
JPush currently supports the push of Android, iOS, and Windows Phone. The keywords are: "android", "ios", "winphone".
If the target platform is the iOS platform, the push environment needs to be set in the options via the apns_production field. True indicates to push the production environment, False indicates to push the development environment, and if not specified, it means to push the production environment.

Push to all platforms:：
{ "platform" : "all" }
Specify a specific push platform:：
{ "platform" : ["android", "ios"] }

audience：Push Target
Object of push device represents a list of devices to which a push can be pushed. To confirm the object of push device, JPush provides a variety of methods, such as aliases, tags, registration IDs, groupings, and broadcasts.
all
If you want to send a broadcast (all devices), fill in "all" directly.
Push Target
There are several ways to select devices outside the broadcast:：

Keyword
Type
Meaning
Instruction
Remark
tag
JSON Array
Label OR
Arrays. There is an OR relationship between multiple tags, which is a union.
Use tags for the grouping of device attributes and user attributes in a large scale. Push up to 20 at a time.
    • Components of valid tags: letters (case-sensitive), numbers, underscore, kanji, special characters @!#$&*+=.|$.
    • Restrictions: The length of each tag is limited to 40 bytes. (UTF-8 encoded is required to determine the length)
tag_and
JSON Array
Label AND
Arrays. There is an AND relationship between multiple tags, which is the intersection.
Note the difference with tag. Push up to 20 at a time.
tag_not
JSON Array
Tag NOT
Arrays. Between multiple tags, take the union of multiple tags first, then take the complement of results
Push up to 20 at a time.
alias
JSON Array
Alias
Arrays. There is an OR relationship between multiple aliases, which is a union.
Use aliases to identify a user. A device can only bind one alias, but multiple devices can be bound to the same alias. Push up to 1000 at a time.
    • Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters @!#$&*+=.|$.
    • Limitations: The length of each alias is limited to 40 bytes. (UTF-8 encoded is required to determine the length)
registration_id
JSON Array
Registration ID
Arrays. There is an OR relationship between multiple registration IDs, which is a union.
Equipment Identity. Push up to 1000 at once
segment
JSON Array
User group ID
The ID of the user group created on the page. Defined as an array, but currently can only push one at a time.
The current limit is that only one can be pushed at a time
abtest
JSON Array
A/B Test ID
The ID of the A/B test created on the page. Defined as an array, but currently only one can be pushed at a time.
The current limit is that only one can be pushed at a time

There must be at least one of the above types. If the length of the value array is 0, the type does not exist.
These types can coexist, and the implicit relationship of multiple items is AND, which is to take the intersection of several types of results.
Example：
"audience" : { "tag" : [ "tag1", "tag2" ], "tag_and" : [ "tag3", "tag4"], "tag_not" : [ "tag5", "tag6"] }
First calculate the result of "tag" field tag1 or tag2=A;
Then calculate the result of the "tag_and" field tag3 and tag4=B
Then calculate the result of the "tag_not" field Non (tag5 or tag6)=C
The final results of "audience" are A and B and C

Example
    • Push to all (broadcast)：
{
   "platform": "all",
   "audience" : "all",
   "notification" : {
      "alert" : "Hi, JPush!",
      "android" : {}, 
      "ios" : {
         "extras" : { "newsid" : 321}
      }
   }
}
    • Push to multiple tags (as long as they are within any tag range): in Shenzhen, Guangzhou, or Beijing
{
    "audience" : {
        "tag" : [ "深圳", "广州", "北京" ]
    }
}
    • Push to multiple tags (requiring in multiple tags at the same time): In Shenzhen and "Female"
{
    "audience" : {
        "tag_and" : [ "深圳", "女" ]
    }
}
    • Push to multiple aliases：
{
    "audience" : {
        "alias" : [ "4314", "892", "4531" ]
    }
}
    • Push to multiple registration IDs：
{
    "audience" : {
        "registration_id" : [ "4312kjklfds2", "8914afd2", "45fdsa31" ]
    }
}
    • Multiple push targets can be pushed at the same time: in Shenzhen or Guangzhou, and “female” “member”
{
    "audience" : {
        "tag" : [ "深圳", "广州" ],
        "tag_and" : [ "女", "会员"]
    }
}

notification：Notification
The "notification" object, which is one of the physical content objects (the other is the "message") of push, is pushed as a "notification" to the client.
Its subordinate attribute contains 4 kinds, 3 platform attributes, and an "alert" attribute
alert
The content of the notification may have only the most basic attribute "alert" on each platform.
The "alert" attribute of this position (directly under the notification object) is a shortcut definition. If the alert information of each platform is the same, it may not be defined. If there is a definition for each platform, the definition here will be overwritten.
{
    "notification" : {
        "alert" : "Hello, JPush!"
    }
}
The notification object defined above will be pushed to multiple platforms specified by "platform" and its information for notification alert will be the same.
android
Notifications on the Android platform will be displayed in a certain notification bar style by the JPush SDK.
Supported fields are：
Keyword
Type
Option
Meaning
Instruction
alert
string
Required
Notification content
If specified here, it will override the alert information specified by the superior; the content can be an empty string, indicating that it does not display in the notification bar.
title
string
Optional
Notification title
If specified, the place where the App name originally appeared in the notification will be displayed as this field.
builder_id
int
Optional
Style ID of notification bar 
The Android SDK can set the style of notification bar. Specifying which style to use bases on the style ID.
priority
int
Optional
Display priority of notification bar 
The default is 0, the range is -2 to 2, and other values ​​will be ignored and defaulted.
category
string
Optional
Filtering or sorting of Notification bar entry 
Rely on rom vendor's strategy for category
style
int
Optional
Type of notification bar style 
The default is 0, and there are 1,2,3 as optional. They are used to specify which style of notification bar to choose, and other values ​​are invalid. There are three options for bigText=1, Inbox=2, bigPicture=3.
alert_type
int
Optional
Alerting method of Notification
The selectable range is -1 to 7, corresponding to any combination of "Not" for Notification.DEFAULT_ALL = -1 or Notification.DEFAULT_SOUND = 1, Notification.DEFAULT_VIBRATE = 2, Notification.DEFAULT_LIGHTS = 4. The default is -1.
big_text
string
Optional
Notification bar style of large text
Available when style = 1. The content will be displayed in large text of the notification bar. Supports roms above api 16.
inbox
JSONObject
Optional
Notification bar style of text entry
Available when style = 2. The value of each key of json will be displayed one by one as a text entry. Supports roms above api 16.
big_pic_path
string
Optional
Notification bar style of large picture
Available when style = 3, can be a network image url, or a path to a local image. Currently supports images with .jpg and .png suffixes. The picture content will be displayed in the notification bar in the form of a large picture. If it is url of http/https url, it could be downloaded automatically; if you want to specify the local picture prepared by the developer, fill in the relative path of sdcard. Supports roms above api 16.
extras
JSON Object
Optional
Extend Field
Customize the Key/Value information in JSON format for business use.

{
    "notification" : {
        "android" : {
             "alert" : "hello, JPush!", 
             "title" : "JPush test", 
             "builder_id" : 3, 
             "style":1  // 1,2,3
             "alert_type":1 // -1 ~ 7
             "big_text":"big text content",
             "inbox":JSONObject,
             "big_pic_path":"picture url",
             "priority":0, // -2~2
             "category":"category str",
             "extras" : {
                  "news_id" : 134, 
                  "my_key" : "a value"
             }
        }
    }
}

iOS
APNs notification structure on the iOS platform.
The content of this notification will be sent by the JPush agent to the Apple APNs server and presented on the iOS device in the form of a system notification.
The content of this notice meets the specifications of the APNs. The supported fields are as follows：
Keyword
Type
Option
Meaning
Instruction
alert
String or JSON Object
Required
Notification content
The content specified here will override the alert information specified by the upper level; it will not be displayed in the notification bar if the content is empty. Supports string formats and also officially defined alert payload structures
sound
string
Optional
Notification sound
If there is no such field, there is no audible prompt for this message; if there is this field, the specified sound will be played after found; otherwise, the default sound will be played. If this field is an empty string, iOS 7 will play default sound, and it will be soundless for iOS 8 and above. (message) Description: The JPush official API Library (SDK) fills sound fields by default. Provide additional ways to turn off the sound.
badge
int
Optional
Application mark
If not, it means that the number of the marker is not changed; otherwise change the marker number to the specified number; 0 means clear. The JPush official API Library (SDK) will populate the badge with the value "+1" by default. For details, see: badge +1
content-available
boolean
Optional
Push wake
Carried "content-available": true when pushing, indicates it is Background Remote Notification. However, it is a normal Remote Notification without carrying this field. For more details: Background Remote Notification
mutable-content
boolean
Optional
Notification extension
Carried with "mutable-content": true when pushing, indicates it is UNNotificationServiceExtension which can support iOS10. It is a normal Remote Notification without carrying the field. For details, refer to: UNNotificationServiceExtension
category
string
Optional

Only IOS8 supports. Set the "category" field value in APNs payload
extras
JSON Object
Optional
Additional fields
Customize Key/value information for business use.

The iOS informs JPush to forward to the APNs server. The APNs protocol defines a notification length of 2048 bytes.
Since JPush needs to be repackaged and considering a bit of security redundancy, it requires the total length of "iOS": {} and in braces does not exceed 2000 bytes. JPush uses utf-8 encoding, so a Chinese character occupies 3 bytes in length.

Server Sends Message String
{
    "notification" : {
         "ios" : {
                 "alert" : "hello, JPush!", 
                 "sound" : "sound.caf", 
                 "badge" : 1, 
                 "extras" : {
                      "news_id" : 134, 
                      "my_key" : "a value"
                 }
            }
       }
}                
Client Receives apns
{
    "_j_msgid" = 813843507;
    aps =     {
        alert = "hello,JPush!";
        badge = 1;
        sound = "sound.caf";
    };
    "my_key" = "a value";
    "news_id" = 134;
}

winphone
Notifications on the Windows Phone platform.
This notification is sent by the JPush server agent to Microsoft's MPNs server and displayed on the system notification bar of the Windows Phone client.
This notice satisfies the relevant specifications of the MPNs. Currently JPush only supports toast type：
Keyword
Type
Option
Meaning
Instruction
alert
string
Required
Notification content
It will be populated to the toast type text2 field. If specified here, it will override the alert information specified by the superior; if the content is empty, it will not be displayed in the notification bar.
title
string
Optional
Notification title
It will be padded to the toast type text1 field.
_open_page
string
Optional
Click on the opened page name
Click on the open page. It will be populated to the param field of the push message, indicating which App page opened the notification. You could not fill it, then it will open by the default home page.
extras
JSON Object
Optional
Extend Field 
Attach as a parameter to the open page above.

    {
        "notification" : {
            "winphone" : {
                 "alert" : "hello, JPush!", 
                 "title" : "Push Test", 
                 "_open_page" : "/friends.xaml", 
                 "extras" : {
                      "news_id" : 134, 
                      "my_key" : "a value"
                 }
            }
        }
    }

message：Custom Message
In-app messages. Or called: custom message, transparent message.
This part of the content will not be displayed on the notification bar. The JPush SDK will transparently pass message content to the App after receiving it and then App needs to handle it.
On the iOS platform, this part of the content is captured in the channel (non-APNS) of in-app message push. Windows Phone temporarily does not support in-app messages.
The message contains the following fields：
Keyword
Type
Option
Meaning
msg_content
string
Required
The content of the message itself
title
string
Optional
Message header
content_type
string
Optional
Message content type
extras
JSON Object
Optional
Optional parameters in JSON format

Android 1.6.2 and lower versions receive offline push with the coexistence of notifications and messages (that is, the api calls push notifications and messages at the same time). Only the notification section can be received, message section is not transparently passed to the App.
Android version 1.6.3 and above SDKs have been adjusted accordingly to receive offline notifications for simultaneous push of notifications and messages.
iOS 1.7.3 and above can parse v3 messages correctly, but cannot parse in-app messages that are delivered simultaneously with v2 push notifications.

Sms_message: SMS Supplement
Tips:：
The use of SMS services will generate additional operator fees. For details, please contact the business team. Tel: 400-612-5955 Business QQ: 800024881

Used to set SMS push content and the delay of sending SMS. If receive the number by mobile phone, the developer needs to match the user's mobile phone number with the device's registration id. Binding method: Server - Device - Update Device
Matched the original JSON service agreement, the message has the following field information:
Keyword
Type
Option
Example
content
string
Required
Cannot exceed 480 characters. "Hello, JPush" is 8 characters. 70 characters counted as a text message fee. If there are more than 70 characters, then divide it according to 67 characters as one and billed one by one. A single Chinese character, punctuation, and English are all counted as one word.
delay_time
int
Required
The unit is seconds and cannot exceed 24 hours. Set to 0 to send an SMS immediately. This parameter is only valid for android platform, and text messages will be sent immediately on iOS and Winphone platform.

options：Optional Parameters
Push options.
Currently contains the following options：
Keyword
Type
Option
Meaning
Instruction
sendno
int
Optional
Push number
Purely used as an API call identifier. The API is returned as is, to facilitate API caller to match requests and returns. A value of 0 indicates that the messageid has no sendno, so the field takes a range of non-zero ints.
time_to_live
int
Optional
Retention time of offline message (seconds)
When the current user is offline, the offline message is reserved for the user so that they can be pushed again when they go online. The default is 86400 (1 day) up to 10 days. A setting of 0 means that offline messages are not retained and only users who are currently online can receive them.
override_msg_id
long
Optional
Message ID to be overwritten
If the current push is to overwrite the previous push, filling in the previous push msg_id will result in the overlay effect, that is: 1) the message received by the msg_id offline is the overwritten content; 2) even if the msg_id Android user has already received, if the notification bar has not been cleared, the new message content will overwrite the previous one; the time limit for the overriding function is: 1 day. If the msg_id does not exist within the specified time limit, a 1003 error is returned, and prompt that it is not a valid operation for message overwriting. The current message will not be pushed.
apns_production
boolean
Optional
Whether APNs is production environment
True means push the production environment, False means push the development environment, and it defaults to push production environment if not specify. Note, however, that the JPush server SDK is set to push the "development environment" by default.
apns_collapse_id
string
Optional
Update identifiers for iOS notifications
If the APNs’ new notification matches the notification that with the same apns-collapse-id field in the current notification center, it will update it with the new notification content and place it at the top of the notification center. The collapse id cannot exceed 64 bytes in length.
big_push_duration
int
Optional
Time of fixed speed push (minutes)
Also known as slow push, which means slow dwon the original push speed as fast as possible within a given n minutes, and evenly push to the target user of this push. The maximum value is 1400. Not setting is not fixed speed push.

Cid: Push the Unique Identifier
Call Address
GET https://api.jpush.cn/v3/push/cid[?count=n[&type=xx]]
Function Description
Cid is a push parameter defined to prevent the api caller from retrying to cause repeated pushes on the server side.
After the user pushes via a cid, and then pushed via the same cid again, the result of the first successful push will be returned directly, and will not be pushed again.
The CID is valid for 1 day. The format of the CID is: {appkey}-{uuid}
Before using the cid, you must obtain your cid pool through the interface. Get type=push or do not pass type value.
Call Example
Request Header
curl --insecure -X GET -v https://api.jpush.cn/v3/push/cid?count=3 -H "Content-Type: application/json" -u "2743204aad6fe2572aa2d8de:e674a3d0fd42a53b9a58121c"
GET /v3/push/cid?count=3
Authorization: Basic (base64 auth string)
Content-Type: text/plain
Accept: application/json
Request Params
count
    可选参数。数值类型，不传则默认为1。范围为[1, 1000] Optional parameters. Numeric type, defaults to 1 if not passed. The range is [1, 1000]
type
    可选参数。CID类型。取值：push(默认), schedule   Optional parameters. CID type. Value: push (default), schedule
Response Header
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

 Response Data  

{
 "cidlist":[
 "8103a4c628a0b98994ec1949-128eeb45-471c-49f3-b442-a05c20c9ed56",
 "8103a4c628a0b98994ec1949-6e44d7f1-89f5-48a8-bec4-e359c15b13e5",
 "8103a4c628a0b98994ec1949-47e0a960-ce67-4e71-94ce-b4b9e8813af0"
 ]
}
Response Params
cidlist
    cid列表

Group Push API: Application Group Push
Call Address
POST https://api.jpush.cn/v3/grouppush
Function Description
This API is used to create pushes for application groups created by developers on the portal. The groupkey can be obtained from the created grouping information, and is similar to the appkey, but it needs to be prefixed with the “group-” prefix.
Note: The override_msg_id attribute of option is not supported at this time.
Call Example
curl --insecure -X POST -v https://api.jpush.cn/v3/grouppush -H "Content-Type: application/json" -u "group-e4c938578ee598be517a2243:71d1dc4dae126674ed386b7b" -d '{"platform":["android"],"audience":"all","notification":{"android":{"alert":"notification content","title":"notification title"}},"message":{"msg_content":"message content"}}'

Push Check API
Call Address
POST https://api.jpush.cn/v3/push/validate
Function Description
The API is only used to verify that if the push call succeeds. The difference with the push API is that no message is sent to the user. Descriptions of other fields: Same as push API.

Call Return
Code
Description
Detailed Explanation
HTTP Status Code
1000
Internal System Error
Internal logic error of Server. Please try again later.
500
1001
Only HTTP Post methods are supported
The Get method is not supported.
405
1002
Necessary parameters are missed.
Must correct
400
1003
The parameter value is illegal
Must correct. Examples of illegal parameters: the tag, alias, registration_id in the Audience parameter has a null value, and the single registration_id specified is illegal or in the wrong format.
400
1004
Verification failed
Must correct. For details, see: Call Verification
401
1005
Message body is too large
Must correct. The limited length of Android platform Notification + Message is 4000 bytes; the total length of "iOS": {} and braces in iOS Notification does not exceed: 2000 bytes (including custom parameters and symbols), the length of iOS Message is no more than 4000 bytes; the length of notification in Winphone platform is limited to 1000 bytes
400
1008
Illegal app_key parameter
Must correct
400
1009
Unsupported key in push object
Must correct
400
1011
There are no push targets that meet the conditions
Please check audience
400
1020
Only supports HTTPS requests
Must correct
404
1030
Internal service timeout
Try again later
503
2002
Call frequency of API exceeds the limit of the application
Contact Jiguang Business team or Technical Support to open a higher frequency of API calls
429
2003
The appkey has been restricted from calling the API
Contact technical support to find out the reasons for restriction and seek help
403
2004
No permission to perform the current operation
Must correct. The source ip address of the current calling API is not in the app's ip whitelist.
403
2005
The amount of information sent exceeds a reasonable range.
It is detected that the cumulative amount of messages sent by the target user is too large and exceeds a reasonable range of use. It is necessary to check the business logic or contact technical support.
403

Reference
    • HTTP return code: HTTP-Status-Code
    • Get push delivery API: Report-API
    • Old Push API: Push API v2
    • Reference for HTTP specification: Basic Authentication of HTTP
    • Apple APNs specification: Apple Push Notification Service
    • Microsoft MPNs specification: Push notifications for Windows Phone 8
