# Push API <small>v3</small>

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>This is the most recent version of the Push API.</p>
<p>Compared to the API v2 version, improvements of the v3 version are:</p>
<ul style="margin-bottom: 0;">
    <li>Based solely on https, no longer provides http access；</li>
    <li>Use HTTP Basic Authentication for access authorization. This way, the entire API request can be completed by using common HTTP tools such as curl, browser plugins, etc；</li>
    <li>Push content is completely in JSON format;</li>
    <li>Supported features have been improved: Support for multiple tags and operations; can send notifications or custom messages alone as well as at the same time; windows phone currently only supports notifications.</li>
</ul>
</div>

## Push Overview

### Function Description

Push a notification or message to a single device or a list of devices.
Pushed content can only be a push object represented by JSON

### Call Address

https://api.jpush.cn/v3/push

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
    <p>If the created Jiguang application is allocated to the Beijing computer room and the API caller's server is also located in Beijing, it is more suitable to call the API of the Jiguang Beijing computer room, which can improve the response speed.</p>
    <p>The room where the application is located can be seen through Application Settings -> Application Info of the Jiguang Web Console. If the application is located in the Beijing computer room, the calling address of each API will be given at the same time.</p>
    <p>Call address of Push API in Beijing computer room： https://bjapi.push.jiguang.cn/v3/push</p>
    <p>For the detailed mapping relationship, see the "Server Location" information in "Application Information".</p>
</div>

### Request Example

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush !","android":{"extras":{"android-key1":"android-value1"}},"ios":{"sound":"sound.caf","badge":"+1","extras":{"ios-key1":"ios-value1"}}}}'

> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

### Return Example

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"sendno":"18","msg_id":"1828256757"}
```

## Call Verification

Add a field (Key/Value pair) in the HTTP Header

```
Authorization: Basic base64_auth_string
```

The generation algorithm of base64_auth_string is: base64(appKey:masterSecret)
That is, add a colon to the appKey, plus the string assembled by masterSecret, and do a base64 conversion.

## Pushing Objects
A push object expressed in JSON format, represents a push-related piece of information

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Keyword</th>
            <th>Option</th>
            <th>Meaning</th>
        </tr>
        <tr>
            <td>platform</td>
            <td>Required</td>
            <td>Settings of push platform</td>
        </tr>
        <tr>
            <td>audience</td>
            <td>Required</td>
            <td>Designation of push device</td>
        </tr>
        <tr>
            <td>notification</td>
            <td>Optional</td>
            <td>Notification content body is the content that is pushed to the client. At least one between it and message must exist and they can coexist.</td>
        </tr>
        <tr>
            <td>message</td>
            <td>Optional</td>
            <td>Message content body is the content that is pushed to the client. At least one between it and message must exist and they can coexist</td>
        </tr>
        <tr>
            <td>sms_message</td>
            <td>Optional</td>
            <td>SMS channels supplements the delivery of content body</td>
        </tr>
        <tr>
            <td>options</td>
            <td>Optional</td>
            <td>Push parameters</td>
        </tr>
        <tr>
            <td>cid</td>
            <td>Optional</td>
            <td>An identifier defined to prevent the duplicate pushes from the server caused by the retrying of api caller</td>
        </tr>
    </table>
</div>

### Examples and Descriptions

```
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
```

## platform：Push Platform

JPush currently supports the push of Android, iOS, and Windows Phone. The keywords are: "android", "ios", "winphone".

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>If the target platform is the iOS platform, the push environment needs to be set in the options via the apns_production field. True indicates to push the production environment, False indicates to push the development environment, and if not specified, it means to push the production environment.</p>
</div>

Push to all platforms:：

```
{ "platform" : "all" }
```

Specify a specific push platform:：

```
{ "platform" : ["android", "ios"] }
```

## audience：Push Target

Object of push device represents a list of devices to which a push can be pushed. To confirm the object of push device, JPush provides a variety of methods, such as aliases, tags, registration IDs, groupings, and broadcasts.

###all

If you want to send a broadcast (all devices), fill in "all" directly.

### Push Target

There are several ways to select devices outside the broadcast:：

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr bgcolor="#D3D3D3">
            <th>Keyword</th>
            <th>Type</th>
            <th>Meaning</th>
            <th>Instruction</th>
            <th>Remark</th>
        </tr>
        <tr>
            <td>tag</td>
            <td>JSON Array</td>
            <td>Label OR</td>
            <td>Arrays. There is an OR relationship between multiple tags, which is a union.</td>
            <td>Use tags for the grouping of device attributes and user attributes in a large scale. Push up to 20 at a time.
                <ul style="margin-bottom: 0;">
                    <li>Components of valid tags: letters (case-sensitive), numbers, underscore, kanji, special characters @!#$&*+=.|$.</li>
                    <li>Restrictions: The length of each tag is limited to 40 bytes. (UTF-8 encoded is required to determine the length)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>tag_and</td>
            <td>JSON Array</td>
            <td>Label AND</td>
            <td>Arrays. There is an AND relationship between multiple tags, which is the intersection.</td>
            <td>Note the difference with tag. Push up to 20 at a time.</td>
        </tr>
        <tr>
            <td>tag_not</td>
            <td>JSON Array</td>
            <td>Tag NOT</td>
            <td>Arrays. Between multiple tags, take the union of multiple tags first, then take the complement of results</td>
            <td>Push up to 20 at a time.</td>
        </tr>
        <tr>
            <td>alias</td>
            <td>JSON Array</td>
            <td>Alias</td>
            <td>Arrays. There is an OR relationship between multiple aliases, which is a union.</td>
            <td>Use aliases to identify a user. A device can only bind one alias, but multiple devices can be bound to the same alias. Push up to 1000 at a time.
                <ul style="margin-bottom: 0;">
                    <li>Valid aliases consist of letters (case-sensitive), numbers, underscores, kanji, special characters @!#$&*+=.|$.</li>
                    <li>Limitations: The length of each alias is limited to 40 bytes. (UTF-8 encoded is required to determine the length)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>registration_id</td>
            <td>JSON Array</td>
            <td>Registration ID</td>
            <td>Arrays. There is an OR relationship between multiple registration IDs, which is a union.</td>
            <td>Equipment Identity. Push up to 1000 at once</td>
        </tr>
        <tr>
            <td>segment</td>
            <td>JSON Array</td>
            <td>User group ID</td>
            <td>The ID of the user group created on the page. Defined as an array, but currently can only push one at a time.</td>
            <td>The current limit is that only one can be pushed at a time</td>
        </tr>
        <tr>
            <td>abtest</td>
            <td>JSON Array</td>
            <td>A/B Test ID</td>
            <td>The ID of the A/B test created on the page. Defined as an array, but currently only one can be pushed at a time.</td>
            <td>The current limit is that only one can be pushed at a time</td>
        </tr>
    </table>
</div>
<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
    <p>There must be at least one of the above types. If the length of the value array is 0, the type does not exist.</p>
    <p>These types can coexist, and the implicit relationship of multiple items is AND, which is to take the intersection of several types of results.</p>
    <p>Example：

"audience" : {
    "tag" : [ "tag1", "tag2" ],
    "tag\_and" : [ "tag3", "tag4"],
    "tag\_not" : [ "tag5", "tag6"]
}

First calculate the result of "tag" field **`tag1 or tag2=A`**;

Then calculate the result of the "tag_and" field **`tag3 and tag4=B`**

Then calculate the result of the "tag_not" field **`Not (tag5 or tag6)=C`**

The final results of "audience" are **`A and B and C`**</p>
</div>
<br>

### Example

* Push to all (broadcast)：

```
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
```

* Push to multiple tags (as long as they are within any tag range): in Shenzhen, Guangzhou, or Beijing

```
{
    "audience" : {
        "tag" : [ "深圳", "广州", "北京" ]
    }
}
```

* Push to multiple tags (requiring in multiple tags at the same time): In Shenzhen and "Female"

```
{
    "audience" : {
        "tag_and" : [ "深圳", "女" ]
    }
}
```

* Push to multiple aliases：

```
{
    "audience" : {
        "alias" : [ "4314", "892", "4531" ]
    }
}
```

* Push to multiple registration IDs：

```
{
    "audience" : {
        "registration_id" : [ "4312kjklfds2", "8914afd2", "45fdsa31" ]
    }
}
```

* Multiple push targets can be pushed at the same time: in Shenzhen or Guangzhou, and “female” “member”

```
{
    "audience" : {
        "tag" : [ "深圳", "广州" ],
        "tag_and" : [ "女", "会员"]
    }
}
```

## notification：Notification

The "notification" object, which is one of the physical content objects (the other is the "message") of push, is pushed as a "notification" to the client.
Its subordinate attribute contains 4 kinds, 3 platform attributes, and an "alert" attribute

###alert

The content of the notification may have only the most basic attribute "alert" on each platform.
The "alert" attribute of this position (directly under the notification object) is a shortcut definition. If the alert information of each platform is the same, it may not be defined. If there is a definition for each platform, the definition here will be overwritten.

```
{
    "notification" : {
        "alert" : "Hello, JPush!"
    }
}
```

The notification object defined above will be pushed to multiple platforms specified by "platform" and its information for notification alert will be the same.

### android

Notifications on the Android platform will be displayed in a certain notification bar style by the JPush SDK.
Supported fields are：

<br>
<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Keyword</th>
            <th>Type</th>
            <th width="6%">Option</th>
            <th>Meaning</th>
            <th>Instruction</th>
        </tr><tr>
            <td>alert</td>
            <td>string</td>
            <td>Required</td>
            <td>Notification content</td>
            <td>If specified here, it will override the alert information specified by the superior; the content can be an empty string, indicating that it does not display in the notification bar.</td>
        </tr><tr>
            <td>title</td>
            <td>string</td>
            <td>Optional</td>
            <td>Notification title</td>
            <td>If specified, the place where the App name originally appeared in the notification will be displayed as this field.</td>
        </tr><tr>
            <td>builder_id</td>
            <td>int</td>
            <td>Optional</td>
            <td>Style ID of notification bar</td>
            <td>The Android SDK can set the style of notification bar. Specifying which style to use bases on the style ID.</td>
        </tr><tr>
            <td>priority</td>
            <td>int</td>
            <td>Optional</td>
            <td>Display priority of notification bar</td>
            <td>The default is 0, the range is -2 to 2, and other values ​​will be ignored and defaulted.</td>
        </tr><tr>
            <td>category</td>
            <td>string</td>
            <td>Optional</td>
            <td>Filtering or sorting of Notification bar entry</td>
            <td>Rely on rom vendor's strategy for category</td>
        </tr><tr>
            <td>style</td>
            <td>int</td>
            <td>Optional</td>
            <td>Type of notification bar style</td>
            <td>The default is 0, and there are 1,2,3 as optional. They are used to specify which style of notification bar to choose, and other values ​​are invalid. There are three options for bigText=1, Inbox=2, bigPicture=3.</td>
        </tr><tr>
            <td>alert_type</td>
            <td>int</td>
            <td>Optional</td>
            <td>Alerting method of Notification</td>
            <td>The selectable range is -1 to 7, corresponding to any combination of "Not" for Notification.DEFAULT_ALL = -1 or Notification.DEFAULT_SOUND = 1, Notification.DEFAULT_VIBRATE = 2, Notification.DEFAULT_LIGHTS = 4. The default is -1.</td>
        </tr><tr>
            <td>big_text</td>
            <td>string</td>
            <td>Optional</td>
            <td>Notification bar style of large text</td>
            <td>Available when style = 1. The content will be displayed in large text of the notification bar. Supports roms above api 16.</td>
        </tr><tr>
            <td>inbox</td>
            <td>JSONObject</td>
            <td>Optional</td>
            <td>Notification bar style of text entry</td>
            <td>Available when style = 2. The value of each key of json will be displayed one by one as a text entry. Supports roms above api 16.</td>
        </tr><tr>
            <td>big_pic_path</td>
            <td>string</td>
            <td>Optional</td>
            <td>Notification bar style of large picture</td>
            <td>Available when style = 3, can be a network image url, or a path to a local image. Currently supports images with .jpg and .png suffixes. The picture content will be displayed in the notification bar in the form of a large picture. If it is url of http/https url, it could be downloaded automatically; if you want to specify the local picture prepared by the developer, fill in the relative path of sdcard. Supports roms above api 16.</td>
        </tr><tr>
            <td>extras</td>
            <td>JSON Object</td>
            <td>Optional</td>
            <td>Extend Field</td>
            <td>Customize the Key/Value information in JSON format for business use.</td>
</tr></table></div>
<br>

```
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
```

### iOS

APNs notification structure on the iOS platform.
The content of this notification will be sent by the JPush agent to the Apple APNs server and presented on the iOS device in the form of a system notification.
The content of this notice meets the specifications of the APNs. The supported fields are as follows：

<br>
<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Keyword</th>
            <th>Type</th>
            <th width="6%">Option</th>
            <th width="20%">Meaning</th>
            <th>Instruction</th>
        </tr><tr>
            <td>alert</td>
            <td>String or JSON Object</td>
            <td>Required</td>
            <td>Notification content</td>
            <td>The content specified here will override the alert information specified by the upper level; it will not be displayed in the notification bar if the content is empty. Supports string formats and also officially defined alert payload structures</td>
        </tr><tr>
            <td>sound</td>
            <td>string</td>
            <td>Optional</td>
            <td>Notification sound</td>
            <td>If there is no such field, there is no audible prompt for this message; if there is this field, the specified sound will be played after found; otherwise, the default sound will be played. If this field is an empty string, iOS 7 will play default sound, and it will be soundless for iOS 8 and above. (message) Description: The JPush official API Library (SDK) fills sound fields by default. Provide additional ways to turn off the sound.</td>
        </tr><tr>
            <td>badge</td>
            <td>int</td>
            <td>Optional</td>
            <td>Application mark</td>
            <td>If not, it means that the number of the marker is not changed; otherwise change the marker number to the specified number; 0 means clear. The JPush official API Library (SDK) will populate the badge with the value "+1" by default. For details, see: badge +1</td>
        </tr><tr>
            <td>content-available</td>
            <td>boolean</td>
            <td>Optional</td>
            <td>Push wake</td>
            <td>Carried "content-available": true when pushing, indicates it is Background Remote Notification. However, it is a normal Remote Notification without carrying this field. For more details: Background Remote Notification</td>
        </tr><tr>
            <td>mutable-content</td>
            <td>boolean</td>
            <td>Optional</td>
            <td>Notification extension</td>
            <td>Carried with "mutable-content": true when pushing, indicates it is UNNotificationServiceExtension which can support iOS10. It is a normal Remote Notification without carrying the field. For details, refer to: UNNotificationServiceExtension</td>
        </tr><tr>
            <td>category</td>
            <td>string</td>
            <td>Optional</td>
            <td></td>
            <td>Only IOS8 supports. Set the "category" field value in APNs payload</td>
        </tr><tr>
            <td>extras</td>
            <td>JSON Object</td>
            <td>Optional</td>
            <td>Additional fields</td>
            <td>Customize Key/value information for business use.</td>
</tr></table></div>
<br>

<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>The iOS informs JPush to forward to the APNs server. The APNs protocol defines a notification length of 2048 bytes.</p>
<p>Since JPush needs to be repackaged and considering a bit of security redundancy, it requires the total length of "iOS": {} and in braces does not exceed 2000 bytes. JPush uses utf-8 encoding, so a Chinese character occupies 3 bytes in length.</p>
</div>
<br>

**Server Sends Message String**

```
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
```

**Client Receives apns**

```
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
```

### winphone

Notifications on the Windows Phone platform.
This notification is sent by the JPush server agent to Microsoft's MPNs server and displayed on the system notification bar of the Windows Phone client.
This notice satisfies the relevant specifications of the MPNs. Currently JPush only supports toast type：

<br>
<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Keyword</th>
            <th>Type</th>
            <th width="6%">Option</th>
            <th>Meaning</th>
            <th>Instruction</th>
        </tr><tr>
            <td>alert</td>
            <td>string</td>
            <td>Required</td>
            <td>Notification content</td>
            <td>It will be populated to the toast type text2 field. If specified here, it will override the alert information specified by the superior; if the content is empty, it will not be displayed in the notification bar.</td>
        </tr><tr>
            <td>title</td>
            <td>string</td>
            <td>Optional</td>
            <td>Notification title</td>
            <td>It will be padded to the toast type text1 field.</td>
        </tr><tr>
            <td>_open_page</td>
            <td>string</td>
            <td>Optional</td>
            <td>Click on the opened page name</td>
            <td>Click on the open page. It will be populated to the param field of the push message, indicating which App page opened the notification. You could not fill it, then it will open by the default home page.</td>
        </tr><tr>
            <td>extras</td>
            <td>JSON Object</td>
            <td>Optional</td>
            <td>Extend Field</td>
            <td>Attach as a parameter to the open page above.</td>
</tr></table></div>
<br>

```
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
```

## message：Custom Message

In-app messages. Or called: custom message, transparent message.
This part of the content will not be displayed on the notification bar. The JPush SDK will transparently pass message content to the App after receiving it and then App needs to handle it.
On the iOS platform, this part of the content is captured in the channel (non-APNS) of in-app message push. Windows Phone temporarily does not support in-app messages.

The message contains the following fields：

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th width="10%">Keyword</th>
            <th width="8%">Type</th>
            <th width="6%">Option</th>
            <th>Meaning</th>
        </tr><tr>
            <td>msg_content</td>
            <td>string</td>
            <td>Required</td>
            <td>The content of the message itself</td>
        </tr><tr>
            <td>title</td>
            <td>string</td>
            <td>Optional</td>
            <td>Message header</td>
        </tr><tr>
            <td>content_type</td>
            <td>string</td>
            <td>Optional</td>
            <td>Message content type</td>
        </tr><tr>
            <td>extras</td>
            <td>JSON Object</td>
            <td>Optional</td>
            <td>Optional parameters in JSON format</td>
        </tr>
    </table>
</div>

```
Android 1.6.2 and lower versions receive offline push with the coexistence of notifications and messages (that is, the api calls push notifications and messages at the same time). Only the notification section can be received, message section is not transparently passed to the App.
Android version 1.6.3 and above SDKs have been adjusted accordingly to receive offline notifications for simultaneous push of notifications and messages.
iOS 1.7.3 and above can parse v3 messages correctly, but cannot parse in-app messages that are delivered simultaneously with v2 push notifications.
```

## Sms_message: SMS Supplement
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>Tips:</p>
<p>The use of SMS services will generate additional operator fees. For details, please contact the business team. Tel: 400-612-5955 Business QQ: 800024881</p>
</div>

Used to set SMS push content and the delay of sending SMS. If receive the number by mobile phone, the developer needs to match the user's mobile phone number with the device's registration id. Binding method: [Server - Device - Update Device](rest_api_v3_device/#device)

Matched the original JSON service agreement, the message has the following field information:

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th width="10%">Keyword</th>
            <th width="8%">Type</th>
            <th width="6%">Option</th>
            <th>Example</th>
        </tr><tr>
            <td>content</td>
            <td>string</td>
            <td>Required</td>
            <td>Cannot exceed 480 characters. "Hello, JPush" is 8 characters. 70 characters counted as a text message fee. If there are more than 70 characters, then divide it according to 67 characters as one and billed one by one. A single Chinese character, punctuation, and English are all counted as one word.</td>
        </tr><tr>
            <td>delay_time</td>
            <td>int</td>
            <td>Required</td>
            <td>The unit is seconds and cannot exceed 24 hours. Set to 0 to send an SMS immediately. This parameter is only valid for android platform, and text messages will be sent immediately on iOS and Winphone platform.
            </td>
        </tr>
    </table>
</div>

## options：Optional Parameters

Push options.

Currently contains the following options：

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th >Keyword</th>
            <th >Type</th>
            <th width="6%">Optional</th>
            <th>Meaning</th>
            <th>Instruction</th>
        </tr><tr>
            <td>sendno</td>
            <td>int</td>
            <td>Optional</td>
            <td>Push number</td>
            <td>Purely used as an API call identifier. The API is returned as is, to facilitate API caller to match requests and returns. A value of 0 indicates that the messageid has no sendno, so the field takes a range of non-zero ints.</td>
        </tr><tr>
            <td>time_to_live</td>
            <td>int</td>
            <td>Optional</td>
            <td>Retention time of offline message (seconds)</td>
            <td>When the current user is offline, the offline message is reserved for the user so that they can be pushed again when they go online. The default is 86400 (1 day) up to 10 days. A setting of 0 means that offline messages are not retained and only users who are currently online can receive them.</td>
        </tr><tr>
            <td>override_msg_id</td>
            <td>long</td>
            <td>Optional</td>
            <td>Message ID to be overwritten</td>
            <td>If the current push is to overwrite the previous push, filling in the previous push msg_id will result in the overlay effect, that is: 1) the message received by the msg_id offline is the overwritten content; 2) even if the msg_id Android user has already received, if the notification bar has not been cleared, the new message content will overwrite the previous one; the time limit for the overriding function is: 1 day. If the msg_id does not exist within the specified time limit, a 1003 error is returned, and prompt that it is not a valid operation for message overwriting. The current message will not be pushed.</td>
        </tr><tr>
            <td>apns_production</td>
            <td>boolean</td>
            <td>Optional</td>
            <td>Whether APNs is production environment</td>
            <td>True means push the production environment, False means push the development environment, and it defaults to push production environment if not specify. Note, however, that the JPush server SDK is set to push the "development environment" by default.</td>
        </tr><tr>
            <td>apns_collapse_id</td>
            <td>string</td>
            <td>Optional</td>
            <td>Update identifiers for iOS notifications</td>
            <td>If the APNs’ new notification matches the notification that with the same apns-collapse-id field in the current notification center, it will update it with the new notification content and place it at the top of the notification center. The collapse id cannot exceed 64 bytes in length.</td>
        </tr><tr>
            <td>big_push_duration</td>
            <td>int</td>
            <td>Optional</td>
            <td>Time of fixed speed push (minutes)</td>
            <td>Also known as slow push, which means slow dwon the original push speed as fast as possible within a given n minutes, and evenly push to the target user of this push. The maximum value is 1400. Not setting is not fixed speed push.</td>
        </tr>
    </table>
</div>

## Cid: Push the Unique Identifier

### Call Address

GET https://api.jpush.cn/v3/push/cid[?count=n[&type=xx]]

### Function Description

Cid is a push parameter defined to prevent the api caller from retrying to cause repeated pushes on the server side.
After the user pushes via a cid, and then pushed via the same cid again, the result of the first successful push will be returned directly, and will not be pushed again.
The CID is valid for 1 day. The format of the CID is: {appkey}-{uuid}
Before using the cid, you must obtain your cid pool through the interface. Get type=push or do not pass type value.

###Call Example

**Request Header**

```
curl --insecure -X GET -v https://api.jpush.cn/v3/push/cid?count=3 -H "Content-Type: application/json" -u "2743204aad6fe2572aa2d8de:e674a3d0fd42a53b9a58121c"
```
```
GET /v3/push/cid?count=3
Authorization: Basic (base64 auth string)
Content-Type: text/plain
Accept: application/json
```

**Request Params**

```
count
    可选参数。数值类型，不传则默认为1。范围为[1, 1000] Optional parameters. Numeric type, defaults to 1 if not passed. The range is [1, 1000]
type
    可选参数。CID类型。取值：push(默认), schedule   Optional parameters. CID type. Value: push (default), schedule
```

**Response Header**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
```

**Response Data**

```
{
 "cidlist":[
 "8103a4c628a0b98994ec1949-128eeb45-471c-49f3-b442-a05c20c9ed56",
 "8103a4c628a0b98994ec1949-6e44d7f1-89f5-48a8-bec4-e359c15b13e5",
 "8103a4c628a0b98994ec1949-47e0a960-ce67-4e71-94ce-b4b9e8813af0"
 ]
}
```

**Response Params**

```
cidlist
    cid列表
```

## Group Push API: Application Group Push

### Call Address

POST https://api.jpush.cn/v3/grouppush

### Function Description

This API is used to create pushes for application groups created by developers on the portal. The groupkey can be obtained from the created grouping information, and is similar to the appkey, but it needs to be prefixed with the “group-” prefix.

**Note**: The override_msg_id attribute of option is not supported at this time.

### Call Example

```
curl --insecure -X POST -v https://api.jpush.cn/v3/grouppush -H "Content-Type: application/json" -u "group-e4c938578ee598be517a2243:71d1dc4dae126674ed386b7b" -d '{"platform":["android"],"audience":"all","notification":{"android":{"alert":"notification content","title":"notification title"}},"message":{"msg_content":"message content"}}'
```

## Push Check API

### Call Address

POST https://api.jpush.cn/v3/push/validate

### Function Description

The API is only used to verify that if the push call succeeds. The difference with the push API is that no message is sent to the user. Descriptions of other fields: Same as push API.

## Call Return

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th>Code</th>
            <th>Description</th>
            <th>Detailed Explanation</th>
            <th>HTTP Status Code</th>
        </tr><tr>
            <td>1000</td>
            <td>Internal System Error</td>
            <td>Internal logic error of Server. Please try again later.</td>
            <td>500</td>
        </tr><tr>
            <td>1001</td>
            <td>Only HTTP Post methods are supported</td>
            <td>The Get method is not supported.</td>
            <td>405</td>
        </tr><tr>
            <td>1002</td>
            <td>Necessary parameters are missed.</td>
            <td>Must correct</td>
            <td>400</td>
        </tr><tr>
            <td>1003</td>
            <td>The parameter value is illegal</td>
            <td>Must correct. Examples of illegal parameters: the tag, alias, registration_id in the Audience parameter has a null value, and the single registration_id specified is illegal or in the wrong format.</td>
            <td>400</td>
        </tr><tr>
            <td>1004</td>
            <td>Verification failed</td>
            <td>Must correct. For details, see: Call Verification</td>
            <td>401</td>
        </tr><tr>
            <td>1005</td>
            <td>Message body is too large</td>
            <td>Must correct. The limited length of Android platform Notification + Message is 4000 bytes; the total length of "iOS": {} and braces in iOS Notification does not exceed: 2000 bytes (including custom parameters and symbols), the length of iOS Message is no more than 4000 bytes; the length of notification in Winphone platform is limited to 1000 bytes</td>
            <td>400</td>
        </tr><tr>
            <td>1008</td>
            <td>Illegal app_key parameter</td>
            <td>Must correct</td>
            <td>400</td>
        </tr><tr>
            <td>1009</td>
            <td>Unsupported key in push object</td>
            <td>Must correct</td>
            <td>400</td>
        </tr><tr>
            <td>1011</td>
            <td>There are no push targets that meet the conditions</td>
            <td>Please check audience</td>
            <td>400</td>
        </tr><tr>
            <td>1020</td>
            <td>Only supports HTTPS requests</td>
            <td>Must correct</td>
            <td>404</td>
        </tr><tr>
            <td>1030</td>
            <td>Internal service timeout</td>
            <td>Try again later</td>
            <td>503</td>
        </tr><tr>
            <td>2002</td>
            <td>Call frequency of API exceeds the limit of the application</td>
            <td>Contact Jiguang Business team or Technical Support to open a higher frequency of API calls</td>
            <td>429</td>
        </tr><tr>
            <td>2003</td>
            <td>The appkey has been restricted from calling the API</td>
            <td>Contact technical support to find out the reasons for restriction and seek help</td>
            <td>403</td>
        </tr><tr>
            <td>2004</td>
            <td>No permission to perform the current operation</td>
            <td>Must correct. The source ip address of the current calling API is not in the app's ip whitelist.</td>
            <td>403</td>
        </tr><tr>
            <td>2005</td>
            <td>The amount of information sent exceeds a reasonable range.</td>
            <td>It is detected that the cumulative amount of messages sent by the target user is too large and exceeds a reasonable range of use. It is necessary to check the business logic or contact technical support.</td>
            <td>403</td>
        </tr>
    </table>
</div>

## Reference

* HTTP return code: HTTP-Status-Code
* Get push delivery API: Report-API
* Old Push API: Push API v2
* Reference for HTTP specification: Basic Authentication of HTTP
* Apple APNs specification: Apple Push Notification Service
* Microsoft MPNs specification: Push notifications for Windows Phone 8
