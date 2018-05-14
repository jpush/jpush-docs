# Product Introduction of JPush

JPush is a tried-and-tested large-scale APP push platform, pushing more than 500 million messages per day. Developers could push messages by calling the API after they integrated the SDK. At the same time, JPush provides a visual web console to send notifications and statistically analyzes push results. JPush fully supports Android, iOS and Winphone.

## Message Form

JPush offers four types of messages: notifications, custom messages, rich media, and local notifications.

### Notification

Or say Push Notification, which means a notification message displayed on the notification bar (status bar) of the mobile phone. The notification is mainly used to prompt the user and often used in news content, promotional activities, product information, version update alerts, order status reminders and other scenarios.

Developer Reference Document：[Push API v3 notification](../server/push/rest_api_v3_push/#notification)

### Custom Message

Custom messages are not notifications and will not be displayed on the notification bar by the SDK. Its content is completely defined by the developer himself. Custom messages are mainly used for the application's internal business logic. When a custom message is pushed over, there may not be any interface display.

Developer Reference Document：[Push API v3 message](../server/push/rest_api_v3_push/#message)

<a name="rich_push"></a>
### Rich Media

JPush allows developers to send images and notifications to better communicate information and bring more user interaction. JPush provides five kinds of templates. Developers can send rich media notifications in the form of landing pages, pop-up windows, and information streams by filling template content. Developers can also send pre-edited pages directly through URLs. Rich media currently supports the Android platform. To better use the features of rich media, it is recommended to update the current SDK version to v2.1.8 and above. However, it can only be sent via JPush console. API format is not supported yet.

Android Developer Reference Document：[Rich Push Developer Guide](../advanced/rich_push/)

### Local Notification

The local notification API does not depend on the network and can be triggered under non-network conditions. The time of local notification is calculated from the time of sending, and is not affected by operations such as intermediate shutdown.
The notifications of local notifications and network pushes are independent of each other, and are not limited by the number of recent notifications.
Local notifications apply to notifications sent at specific times, such as Todo and alarm clock applications, reminding users to return to the application and view tasks at weekly or monthly fixed times. 

Android Developer Reference Document：[Android Local Notification]((../client/Android/android_api/#api_8))

iOS Developer Reference Document：[iOS Local Notification](../client/iOS/ios_api/#_47)

## Push Target

By using labels, aliases, Registration IDs, and user groups, developers can push messages to one or more specific users.

### Label

The purpose of tagging the user who installs the application is mainly to facilitate the developer to deliver push messages in batches according to the tags. Multiple tags can be played for each user. Example: game, old_page, women.

### Alias

Each user can only specify one alias.
Within the same application, different aliases are recommended for different users. In this way, developers could uniquely identify the user based on the alias. 

Android Developer Reference Document: [Android Labels and Alias](../client/Android/android_api/#api_1)
iOS Developer Reference Document: [iOS Labels and Alias](../client/iOS/ios_api/#api-ios) 
Use Aliases and Labels for Pushing, Please refer to the document：[Push API v3 Audience](../server/push/rest_api_v3_push/#audience)

### Registration ID

After the client initiates JPush, the JPush server will assign a Registration ID as the ID of this device (different APP registration IDs for the same mobile phone). Developers can push a single device by specifying a specific Registration ID.

### User Group

The filter of user group includes: label, geographic location, system version, registration time, active user, and online user. For example, developers can set up such user group: users in Beijing, Shanghai, Guangzhou, and Shenzhen who have been online for the last 7 days.
Developers can specify the group's name when the console pushes it, or use the API to call the group's id after the user is grouped on the console.

User Cluster Console User Guide：[User Group](../console/Instructions/#_14)

## Statistical Analysis

JPush supports the statistics of data such as push quantity, user opening time, user usage time, new users, and active users.
Android developers need to implement related statistical APIs before user-related statistics can be performed.
iOS developers do not need to implement the statistics API, and can directly view the relevant data in the [console] - [statistics] page.

Android Developer Reference Document：[Statistical Analysis API](../client/Android/android_api/#api_2)

## Quick Start

+ [Register the developer account](https://www.jiguang.cn/accounts/register) with the JPush official website;
+ [Login](https://www.jiguang.cn/accounts/login/form) to the management console to create an application and get Appkey (the SDK and the server identify each other via Appkey)；
+ [Download SDK](../resources/) and integrate it into App

## Technical Support

When a problem occurs:

+ Please read the document carefully to see if anything is missing [Android FAQ](../client/Android/android_faq/)  [iOS FAQ](../client/iOS/ios_faq/)
+ You can search for similar issues in the Jiguang community；
+ Email us at support@jpush.cn

To solve the problem more quickly, please provide the following information when seeking help:

+ What API interface to use, for example: https://api.jpush.cn/v3/push
+ Provide information of appkey and message id
+ Provides time when there is a problem with the calling API
+ If it is a SDK issue, please provide the corresponding SDK version and complete log record
