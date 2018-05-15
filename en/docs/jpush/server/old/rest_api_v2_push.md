# REST API v2

<div style="font-size:13px;background: #F0E68C;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>Special tip: It is recommended not to call this API directly in the client. Since the Android apk is easy to crack, it is easy for someone to find out the secret information needed to invoke the JPush Remote API from the client code, so that he could simulate your identity and initiate a malicious push.</p>
<p>The recommended method is: Place the code that calls the JPush Remote API on your own application server, and push message by the interface provided by your own application server to the client. For details, please refer to the push chat method: examples and codes.</p>
<p>Upgrade to v3 Push API: Developers are advised to upgrade to v3. This version will be supported until 2015.</p>
</div>

### Push Full-featured Interface

#### Function Description

Developers call this remote interface to push notification messages or custom messages to specified users.

This API can be used for scenarios where developers want to flexibly send messages to specific user or users on their own business servers.

#### Call Address

http://api.jpush.cn:8800/v2/push

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>Please access the JPush API via the domain name, rather than IP directly.</p>
<p>This interface only supports HTTP Post requests.</p>
<p>Unless specified instructions, utf-8 encoding is used uniformly in the interface.</p>
<p>Content-Type of HTTP Post requires application/x-www-form-urlencoded</p>
<p>Considering that there may be some special characters in the content, it is necessary to perform URL Encode on the content before calling the interface. For more details, please refer to: Special Character Issues.</p>
<p>If you attach great importance to the security of the interface, please use the SSL interface. By default, the 443ssl encryption protocol port is used. That is, the interface URL is changed to [> https://+api.jpush.cn/v2/push][0]> .</p>
<p>Whether your application on the JPush Portal is a production environment or test environment, use this API address to push messages.</p>
</div>

#### Call Parameters

##### sendno

int: required

Send the number (up to 32 positive integers (4294967295)). It is maintained by the developer himself and used by the developer to identify the sending request once.

##### app_key

int: required

Only one application can be sent (appKey).

##### receiver_type

int: required

Receiver type.

2- The specified tag.
3 - The specified alias.
4 - Broadcast: Push messages to all users under app_key.
5 - Push based on RegistrationID. Support Android SDK r1.6.0 and above.

##### receiver_value

string: optional

Send range value, corresponding to receiver_type.


2 - The app invokes the tag (tag) set by the SDK API. Supports up to 10 and separated by "," intervals. When multiple tags are filled in, the last push object is the union of the user set of these multiple tags without duplicate users.
3 - The app calls the alias (alias) of the SDK API settings. Supports up to 1000 and separated by "," intervals.
4 - Do not need to fill.
5 - RegistrationID of the target device. Supports up to 1000 and separated by "," (comma) intervals.

##### verification_code

string: required

The verification string is used to verify the validity of the transmission.

After concatenating the four values ​​of sendno, receiver_type, receiver_value, and master_secret (strings are directly concatenated), generate once MD5 (32-bit uppercase).

Reference: concatenate example of verification code

Since the component of the verification string has a String content, and JPush uses UTF-8 encoding, therefore, if your API call does not use UTF-8 encoding, you will first encounter an error return that verification_code incorrect and validation fails, causing the call failure.

##### msg_type

int: required

The type of message sent out

1 - Notification

2 - Custom Message (Only Android Support)

##### msg_content

int: required

Describe the send call.

Will not be sent to the user.

##### platform

string: required

The platform type of the terminal phone of target user, such as: please use comma to separate android, ios, winphone.

##### apns_production

int: optional

Specify delivery environment of APNS notification: 0: Development environment, 1: Production environment.

If the parameter is not carried, the push environment is the same as the APNS environment setting on the JPush Web.

##### time_to_live

int: optional

Save offline time in seconds since the message was pushed. Supports up to 10 days (864000 seconds).

0 means the message is not saved offline. That is, sent immediately if the user is online, and the current offline user will not receive this message.

Not setting this parameter indicates the default, which will save offline messages for 1 day (86400 seconds).

##### override_msg_id

string: optional

The ID of the previous message to be overwritten.

When this parameter is specified, the current message will overwrite the message with the specified ID. The specific behavior of coverage is

1）If the covered message user has not received it yet, it will not be received in the future;

2）If the overwritten message has been received by the Android user but the notification bar has not been cleared, the new one on the Android notification bar will overwrite the previous one.

The time limit for the coverage function to work is 1 day. If the msg_id does not exist within the specified time limit, a 1003 error will be returned, prompting it is not a valid message overwritten operation, and the current message will not be pushed.

#### Call Return

When calling the interface, Jiguang Push Server performs a simple validation check and returns the result immediately.

Under normal circumstances, the return code is 200, the type of return content is a string, and the form is JSON

| Name of Key | Value Description |
|:---|:---|
| errcode |Error code. Reference: Definition ofError Code |
| errmsg |Error description |
| msg_id| ID of the message |

### Format of Message Content

There are specific requirements for the msg_content format in the call parameters of the message sending interface. This section gives specific instructions.

First of all, its requirements are JSON format. The specific content varies according to the type.

#### Notification Type

When call parameter msg_type = 1, msg_content JSON requires:

| Name of Key | Is it necessary | Value Description |
| :--- | :--- | :--- |
| n_builder_id | Optional | The value of 1-1000. If not filled, it defaults to 0 and uses the default notification style of Jiguang Push SDK. Only Android supports this parameter. For further information, please refer to the document: Customization API of Notification Bar Style |
| n_title | Optional | Notification title. If not, the application name is used by default. Only Android supports this parameter. |
| n_content | Required | Notification content. |
| n_extras | Optional | Additional parameters of notifications. JSON format. The client can get all the content.|

```
 For length restrictions, please refer to: Notice for Limitations on Length of Notifications.
 In addition, for iOS notifications, there are special places to explain. Please refer to: Special Instructions for iOS APNs.
```

#### Special Instructions for iOS APNs

When pushing the iOS APNs message simultaneously through the JPush API, there are some contents that need to be adapted to the APNs.

For specific definitions on APNs, please refer to the official document:Apple Push Notification Service

| JPush field | APNs field |
| :--- | :--- |
| n_content | alert |
| n_extras -> ios -> badge | badge |
| n_extras -> ios -> sound | sound |
| n_extras -> ios >content-available | content-available |

The n_content field must exist, but it can be an empty string. At this time, if there is a badge field in extras, the notification received will show the number in the upper right corner of the application icon without the notification bar content.

Overall N_extras can be empty.

Example for complete notification msg_content JSON string with iOS specific parameters specified

```
{
 "n_content":"通知内容",
 "n_extras":{
    "ios":{
        "badge":88,
        "sound":"default",
        "content-available":1
        },
 "user_param_1":"value1",
 "user_param_2":"value2"}
}
```

#### Description of Notification Length Limit

The JPush API supports notification push from Andorid and the iOS platform simultaneously.

Since the APNs limit is 255 bytes, JPush push notifications are also uniformly limited based on APNs.

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
<p>The design of notification length limit, on the one hand, is really due to APNs.</p>
<p>On the other hand, we also believe that for "notices", information displayed in the notification bar, such length is sufficient. </p>
<p>Also note that the length here is byte. Due to UTF-8 encoding, one Chinese character occupies 3 bytes</p>
</div>

Since the assembly APNs have several JSON fields, the JPush API notification limits the size to 220 bytes.

The specific limit algorithm is: the contents of n_content, plus the contents of n_extras,is its total length.

#### Types of Custom Message

```
Only Android supports custom messages
```

When the call parameter msg_type = 2 is called, msg_content JSON requires:

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
        <th>Name of Key</th>
        <th>Options</th>
        <th>Value Descri~~ption</th>
    </tr><tr>
        <td>message</td>
        <td>Required</td>
        <td>The content of the custom message.</td>
    </tr><tr>
        <td>content_type</td>
        <td>Optional</td>
        <td>The content type in the message field. Used for content parsing of specific message</td>
    </tr><tr>
        <td>title</td>
        <td>Optional</td>
        <td>Message header</td>
    </tr><tr>
        <td>extras</td>
        <td>Optional</td>
        <td>Returned intact. More affiliated information in JSON format</td>
    </tr>
    </table>
</div>

The total length of all field information of a custom message must not exceed 1000 bytes.

```
It is worth noting that JPush SDK itself will not parse this information .
Instead, the client provides the API to the developer's own application for processing. Please refer to related documents for receiving push messages.
```

#### verification_code: Splicing Example

```
int sendno = 3321;
int receiverType = 2;
String receiverValue = "game, oldman, student";
String masterSecret = "71638202938228382811FCB1CB308ADC"; //极光推送portal
上分配的 appKey 的验证串(masterSecret)

String input = String.valueOf(sendno) + receiverType + receiverValue + masterSecret;
String verificationCode = StringUtils.toMD5(input);
```

### Special Character Problem

If use the official Java Library - Java v2 directly when calling the API, you can send any special characters in the content.

However, if you want to call this API directly, there are special character issues to consider.

In principle, there are two parts with special character problems:

* Push content msg_content is a JSON string, so JSON-related special characters need to be escaped.
* Calling interfaces in the way of HTTP API is essentially transferring all the issues with URL encode based on URLs.

Therefore, before the official call interface issues the content, your code needs to handle two parts of the content: JSON encode, URL encode.

For JSON encode, if you use some JSON library directly to process JSON, then these packages will automatically handle special character escapes for you.

If you completely assemble a JSON string manually, it is necessary for you to write JSON special string escapes yourself. Please refer to the JSON official documentation: [http://www.json.org/][1]

URL encode In general, each development language platform provides this tooling method to operate URL encode.

## Definition of Error Code

When the HTTP return code is 200, it is a service-related error.

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
        <th>Error Code</th>
        <th>Description</th>
    </tr><tr>
        <td>0</td>
        <td>Call success</td>
    </tr><tr>
        <td>10</td>
        <td>Internal system error</td>
    </tr><tr>
        <td>1001</td>
        <td>Only HTTP Post methods are supported, and Get methods are not supported</td>
    </tr><tr>
        <td>1002</td>
        <td>Miss necessary parameters</td>
    </tr><tr>
        <td>1003</td>
        <td>The parameter value is illegal</td>
    </tr><tr>
        <td>1004</td>
        <td>Verification_code verification failed</td>
    </tr><tr>
        <td>1005</td>
        <td>Message body is too large</td>
    </tr><tr>
        <td>1007</td>
        <td>Receiver_value parameter is illegal</td>
    </tr><tr>
        <td>1008</td>
        <td>Illegal appkey parameter</td>
    </tr><tr>
        <td>1010</td>
        <td>Msg_content is illegal</td>
    </tr><tr>
        <td>1011</td>
        <td>There are no push targets that meet the conditions</td>
    </tr><tr>
        <td>1012</td>
        <td>iOS does not support pushing custom messages. Only Android supports pushing custom messages.</td>
    </tr><tr>
        <td>1013</td>
        <td>Content-type only supports application/x-www-form-urlencoded</td>
    </tr><tr>
        <td>1014</td>
        <td>The message contains sensitive words.</td>
    </tr><tr>
        <td>1030</td>
        <td>Internal service timed out. Try again later.</td>
    </tr>
</table>
</div>

```
When returning 1011：

If it is a mass sending: This application does not yet have a user registered on the client. Please check whether the SDK integration is normal.

If it is pushed to an alias or tag: This alias or tag has not yet been submitted successfully on any client SDK.
```

### Reference

For the query of delivery messages, please refer to: [Report-API][2]
To understand limitation of API frequency: [Limitation of API Frequency][3]

[1]: http://www.json.org/
[2]: ../push/rest_api_v3_report
[3]: ../push/server_overview/#api-rating