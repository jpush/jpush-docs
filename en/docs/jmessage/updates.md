# Recent Updates

### PC SDK V1.2.1

#### Update Time

+ 2018-04-12

#### ChangeLog

##### NewFeature:

+ New PC-side SDK supports Windows and macOS
+ Synchronize all features of Windows v1.2.0

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Download SDK package from the official website and simply replace it all
+ If using NuGet package, you can use NuGet package manager to update directly

### iOS SDK v3.5.0

#### Update Time

+ 2018-03-01

#### ChangeLog


##### BugFix:

+ Fix some bugs in user feedback

##### NewFeature

+ Set group administrator
+ Dissolve group
+ Transfer owner privileges
+ Transparent transmission of messages between devices
+ Login interface returns records of login device

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore of the JMessage.framework in the new version to the project. For details, see the official Integration Document.
Interface Change
+ -(void)onReceiveNotificationEvent: The interface is subdivided into -(void)onReceiveUserLoginStatusChangeEvent: and -(void)onReceiveFriendNotificationEvent:

### Android SDK v2.5.0

#### Update Time

+ 2018-03-01

##### Change Log


##### BugFix:

+ Fix an issue where the banned list in the old version was not available
+ Fix some bugs reported by other users

##### NewFeature:

+ Adaptation to Android O system
+ Add group managers
+ Support for dissolving groups
+ Support for obtaining device landing records
+ Support to transfer owner privileges
+ Support transparent transmission of messages between devices

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.9.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.5.0.jar and delete the original Jiguang jar file. Replace the original libjcoreXXX.so file in the project with the libjcore119.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file.
Note that JCore has added the provider component from version 1.1.7. If the JCore used in the project is earlier than 1.1.7, you need to pay attention to the configuration of the new provider component in the manifest when intergrating.
+ If JMessage is integrated by jcenter, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### Windows SDK V1.2.0

#### Update Time

+ 2018-02-02

#### ChangeLog


##### NewFeature:

+ Login device history
+ Dissove group
+ Set up group administrators
+ Get a list of public groups
+ Transfer owner
+ Transparent transmission of messages between devices

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Download SDK package on the official website and simply replace it all
+ If using NuGet package, you can use NuGet package manager to update directly

### Web SDK v2.6.0

#### Update Time

+ 2018-01-26

##### Change Log


##### NewFeature:

+ Add administrator role
+ Add the functions to dissolve groups and transfer owner
+ Add access to transparent transmission of messages between devices and device records
+ Add access to all public groups under appkey

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.6.0.min.js

### iOS SDK v3.4.1

#### Update Time

+ 2018-01-03

#### ChangeLog


##### BugFix:

+ Fix some bugs in user feedback

##### NewFeature

+ Add access to all public group interfaces under AppKey

#### Upgrade Guide

+ Replace old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the integration document on the official website.

### Android SDK v2.4.1

#### Update Time

+ 2018-01-02

##### Change Log


##### BugFix:

+ Fix the problem where the banned list was not updated when dealing with offline group member deletion and exit
+ Improve sdk stability

##### NewFeature:

+ Add interface to get all public groups under a specified application
+ Extras of custom messages and messages support to get data of value as Object

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.8.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.4.1.jar and delete the original Jiguang jar file. Replace the original libjcoreXXX.so file in the project with the libjcore118.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of the SDK download package to update the configuration of AndroidManifest.xml file.
Note that JCore has added the provider component from version 1.1.7. If the JCore used in the project is earlier than 1.1.7, you need to pay attention to the configuration of the new provider component in the manifest when integrating.
+ If integrating JMessage by jcenter, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### iOS SDK v3.4.0

#### Update Time

+ 2017-12-11

#### ChangeLog


##### BugFix:

+ Fix some bugs in user feedback

##### NewFeature

+ Add chat room features
+ Add bans to group member
+ Add public group function which supports application for admission
+ Add supporting for setting file types when sending file messages

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the integration document on the official website.

### Android SDK v2.4.0

#### Update Time

+ 2017-12-11

##### Change Log


##### BugFix:

+ Fix the incorrect title and avatar resulted by absence of targetAppkey settings when reading conversation from database
+ Improve sdk stability

##### NewFeature:

+ Add chat room features
+ Add public group types to support application for admission
+ Add bans to group member

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.8.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.4.0.jar and delete the original Jiguang jar file. Replace the existing libjcoreXXX.so file in the project with the libjcore118.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file.
Note that JCore has added the provider component from version 1.1.7. If the JCore used in the project is earlier than 1.1.7, you need to pay attention to configuration of the new provider component in the manifest when integrating.
+ If you use jcenter to integrate JMessage, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### Windows SDK v1.1.0

#### Update Time

+ 2017-12-04

##### Change Log


##### NewFeature:

+ Chat room features
+ Public group in which users can apply for admission
+ Support group bans
+ Transparent transmission of message
+ Provide NuGet package
+ Add GroupId type to replace int64_t, and use GroupId::get to get value

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Check the latest SDK documentation

### Web SDK v2.5.0

#### Update Time

+ 2017-11-29

##### Change Log


##### NewFeature:

+ Add chat room features
+ Add public group types in which users can apply for admission
+ Support group bans

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.5.0.min.js

### Web SDK v2.4.1

#### Update Time

+ 2017-11-02

##### Change Log


##### BugFix:

+ Logic optimization of the unread

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.4.1.min.js

### iOS SDK v3.3.0

#### Update Time

+ 2017-10-27

#### ChangeLog


##### BugFix:

+ Fix some bugs in user feedback

##### NewFeature

+ Support multi-end simultaneously online
+ Support group avatar
+ Support message transparent transmission
+ Add message read receipt function
+ Add message forwarding interface
+ Extras extension fields is added to JMSGConversation class
+ Extras extension field is added to the JMSGUser class
+ User registration interface supports other attribute value settings

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the integration document on the official website

### Android SDK v2.3.0

#### Update Time

+ 2017-10-20

##### Change Log


##### BugFix:

+ Fix delete failures that may occur on the deleteSingleConversation interface
+ Improve sdk stability

##### NewFeature:

+ Support multi-end simultaneously online
+ Add message read receipt function
+ Add message forwarding interface
+ Support command transparent transmission
+ Extra extension fields is added to Conversation class
+ Support group avatar
+ UserInfo supports extension field extras
+ User registration interface supports other attribute settings

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.7.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.3.0.jar and delete the original Jiguang jar file. Replace the existing libjcoreXXX.so file in the project with the libjcore117.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the lastest demo version of SDK download package to update the configuration of AndroidManifest.xml.
Note that the JCore 1.1.7 version adds a provider component. When integrating, you need to pay attention to the configuration of the new provider component in the manifest.
+ If you use jcenter to integrate JMessage, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### Web SDK v2.4.0

#### Update Time

+ 2017-10-16

##### Change Log


##### NewFeature:

+ Support message transparent transmission
+ Support group avatar
+ Support multi-end simultaneously online
+ Message read receipt
+ Session and user information support extension fields
+ Registration supports extension fields
+ Support acquiring number of unread sessions and resetting number of unreading sessions

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.4.0.min.js

### Windows SDK v1.0.0

#### Update Time

+ 2017-10-13

##### Change Log

    ### • SDK The first release of the JMessage Windows C++ SDK covers all features of the current Web SDK v2.3.1, which used a number of new features for convenient development based on the latest C++17 language standard (requires VS2017). Based on the task/then asynchronous interface of cpprestsdk (More about task), the upper layer can use the SDK with callbacks or co_await methods.


##### NewFeature:

+ Support multi-end simultaneously online
+ Message read receipt
+ Group avatar

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Download the SDK. For detailed integration instructions, please refer to the official Integration Guide

### iOS SDK v3.2.1

#### Update Time

+ 2017-08-29

#### ChangeLog


##### BugFix:

+ Fix some bugs in user feedback

##### NewFeature

+ Offline event processing is upgraded to an event synchronization mechanism, which greatly improves the performance of handling a large number of events. The upper layer does not need to be modified or adapted.
+ Specify the suffix name when creating imageContent
+ Specify the suffix name when uploading an avatar
+ Add interfaces：
    + JMSGUser
        + +(void)updateMyAvatarWithData:avatarFormat:completionHandler;// specifies suffix name of the avatar
    + JMSGImageContent
        + @property(nonatomic, strong) NSString *format;//specifies extension name of the picture
    + JMSGFileContent
        + -(void)fileDataWithProgress:completionHandler: ;// file download interface with download progress

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the integration document on official website.

### Android SDK v2.2.1

#### Update Time

+ 2017-08-15

##### Change Log


##### BugFix:

+ Fix the problem that custom notification bar text does not work when sending custom type messages
+ Improve sdk stability

##### NewFeature:

+ Offline event processing is upgraded to an event synchronization mechanism, which greatly improves the performance of handling a large number of events. The upper layer does not need to be modified or adapted.
+ A new type group_info_updated is added to the group event EventNotificationContent to indicate that the group information is updated. See the "Receiving Message Events" section in the Event Handling section for code examples
+ Add interfaces of extention name when creating ImageContent and specifying storage

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.6.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.2.1.jar and delete the original Jiguang jar file. Use the libjcore116.so file in the corresponding CPU folder to replace the original libjcoreXXX.so file in the project and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file.
+ If JMessage is integrated by jcenter, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### Web SDK v2.3.1

#### Update Time

+ 2017-08-11

##### Change Log


##### NewFeature:

+ Event synchronization
+ Custom notification bar
+ Message forwarding
+ Group block list

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.3.1.min.js

### iOS SDK v3.2.0

#### Update Time

+ 2017-06-30

#### ChangeLog


##### BugFix:

+ Fix the automatic update of user information

##### NewFeature

+ Add the message recall feature
+ Add storage and controlling function of offline messages
+ Add displaying and controlling function of notification bar messages
+ Add custom notification bar
+ Add the interface for unified uploading user information
+ Add classes：
    + JMSGPromptContent
        + @property(nonatomic, readonly, copy) NSString *promptText;// propmts message
    + JMSGOptionalContent
        + @property(nonatomic, assign) BOOL noSaveOffline;// does not save offline messages
        + @property(nonatomic, assign) BOOL noSaveNotification;// does not save notification message
        + @property(nonatomic, strong) JMSGCustomNotification * customNotification; // custom notification bar
    + JMSGUserInfo
        + This class is only used to modify user information
+ Add interfaces：
    + JMSGEventDelegate
        + -(void)onReceiveMessageRetractEvent:;// monitors message revocation events
    + JMSGConversation
        + -(void)retractMessage: completionHandler: ;// retracts messages
        + -(void)sendMessage: optionalContent:;// customizes contents of notification bar and controls storage of offline messages
        + -(NSString *)avatarLocalPath;// gets the local path of the session avatar
    + JMSGMessage
        + +(void)retractMessage: completionHandler: ;// retracts messages
        + +(void)sendMessage: optionalContent:;// customizes contents of notification bar and controls storage of offline messages
    + JMSGUser
        + +(void)updateMyInfoWithUserInfo: completionHandler:;// updates user information (support for unified uploading of fields)
        + -(NSString *)thumbAvatarLocalPath;// gets the local path of thumbnail file of user avatar
        + -(NSString *)largeAvatarLocalPath;// gets the local path of big picture file of user avatar
    + JMSGMediaAbstractContent
        + @property(nonatomic, strong, readonly) NSString * originMediaLocalPath; // gets the local path of original file
    + JMSGImageContent
        + @property(nonatomic, strong, readonly) NSString *thumbImageLocalPath;// gets  the local path of thumbnail

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the official integration document.

### Android SDK v2.2.0

#### Update Time

+ 2017-6-15

##### Change Log


##### BugFix:

+ Improve sdk stability

##### NewFeature:

+ Support message recall
+ Support various controls when sending messages, including：
    + Storage control of offline messages
    + Display control of message notification bar
    + Text of custom message notification bar
See Message Management section in development guidance
+ Add an interface to uniformly update all information of users
+ Support @everyone in group chats
+ Support automatic update of user information
+ Support notification bar to light up breathing light

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.3.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.2.0.jar and delete the original Jiguang jar file. Replace the original libjcoreXXX.so file in the project with the libjcore113.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file.
+ If JMessage is integrated by jcenter, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide

### Web SDK v2.3.0

#### Update Time

+ 2017-6-15

##### Change Log


##### NewFeature:

+ Storage control of offline message and display control of message notification bar
+ Message recall
+ Monitor updata of user information
+ Get status of SDK connection, initialization, and login
+ Optimize event listener field

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.3.0.min.js

### Web SDK v2.2.1

#### Update Time

+ 2017-05-09

##### Change Log


##### BugFix:

+ Fix the bug immediately reported by initialization after page loading
+ Fix the problem where some scenes cannot get historical news in roaming mode

##### NewFeature:

+ Nickname and avatar field are added to get group member interface.
+ Get session list interface: Nickname and avatar field are added in the single chats and group name field is added in group chats

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.2.1.min.js

### iOS SDK v3.1.1

#### Update Time

+ 2017-05-05

#### ChangeLog


##### BugFix:

+ Fix the logic problem when sorting allConversations interface
+ Fix the problem of download progress with callback error when downloading multimedia files

##### NewFeature

+ Conversation adds latestMsgTime attribute for session ordering
    + @property(nonatomic, strong, readonly) NSNumber *latestMsgTime;

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the official integration document.

### Android SDK v2.1.2

#### Update Time

+ 2017-4-28

##### Change Log


##### BugFix:

+ Improve sdk stability

##### NewFeature:

+ Add the interface JMessageClient.getAllUnReadMsgCount() to get global unread number
+ Support jcenter to automatically integrate

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.2.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.1.2.jar and delete the original Jiguang jar file. Replace the existing libjcoreXXX.so file in the project with the libjcore112.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file
+ If JMessage is integrated by jcenter, you do not need to add related components and resources. For detailed integration instructions, please refer to the official Integration Guide.

### iOS SDK v3.1.0

#### Update Time

+ 2017-04-05

#### ChangeLog


##### BugFix:

+ Fix the occasional failures of message sending due to repetition of mediaID.
+ Fix the problem that the group member list is not returned sequentially according to the time of entering the group.

##### NewFeature

+ New message synchronization mechanism
+ Support message roaming
+ Group@feature
+ Block group message
+ Support automatic update of user information
+ Add a parity mode for media messages: hash check, which is used to be compatible with media messages sent by web sdk
+ Add interfaces：
    + Message synchronization agent
        + Offline messages - (void)onSyncOfflineMessageConversation:offlineMessages:
        + Roaming messages - (void)onSyncRoamingMessageConversation:
        + Set up message roaming + (void)setupJMessage:appKey:channel:apsForProduction:category:messageRoaming:
    + Group@function related
        + Create a group message with atList：+ (JMSGMessage *)createGroupMessageWithContent:groupId:at_list:
        + Send atList message：- (void)sendMessage: at_list:
        + Create @ all group message：+ (JMSGMessage *)createGroupAtAllMessageWithContent:groupId:
        + Send @ all message：- (void)sendAtAllMessage:
        + Determine if yourself is @ in the message：- (BOOL)isAtMe
        + Determine if all are @ in the message：- (BOOL)isAtAll
        + Get the list of members of @：- (void)getAt_List:
    + Block group message related
        + Set up group message block：- (void)setIsShield:handler:
        + Determine if the group is blocked：group.isShieldMessage
        + Get the current user's group block list：+ (void)shieldList:
+ Interface changes：
    + To adapt the use of Swift, interface name of allConversationsByDefault is changed to allUnsortedConversations. Only the interface name is modified, and the function of the interface remains unchanged

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

#### Upgrade Prompt

+ After upgrading the version, the upper layer needs to add the monitoring agent method of message synchronization, otherwise the upper layer cannot sense
+ Developers who need to set message record roaming, call a new initialization method to set whether message roaming is enabled

### Android SDK v2.1.1

#### Update Time

+ 2017-03-22

##### Change Log


##### BugFix:

+ Fix the issue of getting no user avatar in some cases
+ Fix other bugs reported by users

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.0.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.1.1.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore110.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file
+ For detailed integration instructions, please refer to the official Integration Guide.

### Web SDK v2.2.0

#### Update Time

+ 2017-03-17

##### Change Log

+ Add group chat @ features
+ Add group blocking feature
+ Add path interface access to resource
+ Add synchronization listening interface of offline messages (optimized performance)
+ Add abnormal disconnection monitoring

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old version of sdk with the latest jmessage-sdk-web.2.2.0.min.js

### Android SDK v2.1.0

#### Update Time

+ 2017-03-10

##### Change Log


##### BugFix:

+ Fix the probability of getgroupowner() is empty after successfully get the group information
+ Fix the occasional failure of picture sending when sending a large number of pictures
+ Fix the problem that related group member change events will not be thrown when the session does not exist.
+ Fix the occasional failure of message sending due to duplication of mediaID
+ Fix other bugs reported by users

##### NewFeature

+ New message synchronization mechanism
+ Support message roaming
+ Group@feature
+ Block group messages
+ Support Dev-api buddy updateeEvent
+ Add a user offline reason: Login status is abnormal
+ Support Dev-api user information update event
Add interfaces
+ Group@function related interfaces
    + Create a group message containing atList ：conversation.createSendMessage(content,atlist,string)、JMessageClient. createAtGroupMembersMessage(long,atlist,content)
    + Determine if the message has @ yourself：message.isAtMe()
    + Get the list of group members @ in the message：message.getAtUserList(callback)
+ Group block related interfaces
    + Set group message blocking：groupInfo.setBlockGroupMessage(int,callback)
    + Determine if the group is blocked：groupInfo.isGroupBlocked()
    + Get the current user's group blocking list：JMessageClient.getBlockedGroupsList(callback)
+ Set whether message roaming is required：JMessageClient.init(context,boolean)
+ Add offline message event：OfflineMessageEvent
+ Add synchronization completion event of roaming message：ConversationRefreshEvent
+ Add user information updated event：MyInfoUpdatedEvent

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.0.jar. Replace the original Jiguang jar file in the project with jmessage-android_v2.1.0.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore110.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file
+ For detailed integration instructions, please refer to the official Integration Guide.

### iOS SDK v3.0.1

#### Update Time

+ 2017-02-15

#### ChangeLog


##### BugFix:

+ Fix the occasional crashes occurred when the SDK starts.
+ Fix the problem that you need to log in again to receive the message when integrating JPush after a pre-separation version upgrading to a post-separation version.
+ Fix the problem that there is sometimes no callback when calling the login interface

##### NewFeature

+ JMessage provides the method of designing the markers (originally set by JPush)
+ Add interfaces
+ Set the marker: + (BOOL)setBadge:(NSInteger)value;
+ Reset the marker: + (void)resetBadge;

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the official integration document.

#### Upgrade Prompt

+ After the upgrade, because JCore is updated to v1.1.1, it needs to be manually introduced into the project.

### iOS SDK v3.0.0

#### Update Time

+ 2017-01-10

#### ChangeLog

+  Modularly separate to the integration of JCore and JMessage, and separate from the dependency with JPush
The Jiguang Developer Service SDK adopts a modular usage model, namely a core (JCore)+N service (JMessage, JPush...) usage, which facilitates developers to use a single service or multiple services and greatly optimize the problem of duplication of function modules when multiple modules are used.
+ Add interfaces：
    + Register remote push: + (void)registerForRemoteNotificationTypes:(NSUInteger)types categories:(NSSet *)categories;
    + Register DeviceToken: + (void)registerDeviceToken: (NSData *)deviceToken

#### Upgrade Guide

+ Note that the processor for i386 is no longer supported in 3.0.0 and above
+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file
+ Link the JCore in the new version of JMessage.framework to the project. For details, see the official integration document.

### Android SDK v2.0.0

#### Update Time

+ 2017-01-09

##### Change Log

+ Add the modular separation to JCore.  And JMessage. The original jar package used is divided into two jar packages, jcore and jmessage, and get rid of the dependency with JPush.
+ Fix some bugs reported by users.

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ First unzip the zip archive you got
+ Update library files
    + Open the libs folder and add jcore-android_v1.1.0.jar. Replace the original Jiguang jar file in the project with jmessage-android_2.0.0.jar and delete the original Jiguang jar file. Replace the original libjpushXXX.so file in the project with the libjcore110.so file in the corresponding CPU folder, and delete the original Jiguang so file. Each type of so file can be found in the SDK download package.
+ Update AndroidManifest.xml
    + Please refer to the latest demo version of SDK download package to update the configuration of AndroidManifest.xml file
+ For detailed integration instructions, please refer to the official Integration Guide.

### iOS SDK v2.2.4

#### Update Time

+ 2016-12-19

##### Change Log


##### BugFix

+ Fix the problem with fixed download size of thumbnails
+ Modify the failures of sending pictures and voices in some regions

##### NewFeature

+ Add notification event of current user information change kJMSGEventNotificationCurrentUserInfoChange
+ Add extra field interface for modifying message -(void)updateMessageExtra:extraValue:extraKey:
+ Add the interface used to get the total number of unread messages for all current sessions + (NSNumber *)getAllUnreadCount

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Web SDK v2.1.0

#### Update Time

+ 2016-12-14

##### Change Log

+ Add friend modules (adding friends, delete friends, modify friend notes, friends list)
+ Add logout interface
+ Optimize callback function of successful message sending with a added parameter to get content already sent
+ Optimize forced offline (sdk level enables automatically offline)

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the jmessage-sdk-web.js file

### Web SDK v1.2.1

#### Update Time

+ 2016-12-05

##### Change Log

    ### • Fix the image uploading problem of Web SDK v1.2.0

Download Link
    ### • Click to download Web SDK v1.2.1

 Special Note
+ The v1.x version will no longer provide new features and only maintains problems caused by bugs. It is recommended to switch to the 2.x version as soon as possible.

### iOS SDK v2.2.3

#### Update Time

+ 2016-11-30

##### Change Log

+ Optimize HTTPS in SDK to HTTP
+ Fix the problem with group event unable to create session
+ Fix the crash cause by sending messages in a loop

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Web SDK v2.0.0

#### Update Time

+ 2016-11-23

##### Change Log

+ Comprehensively upgrade APIs to support Promise style APIs
+ Add the function for modifying user information
+ Add the function for updating avatar
+ Add the function for updating user password
+ Add the function for receiving location
+ Add the function for file uploading and downloading
+ Add support for sending and receiving emoij expressions
+ Add cross-application message Do-Not-Disturb functionality
+ Add message auto-retry logic

#### Upgrade Guide

+ Introduce the latest jmessage-sdk-web.min.js on the page.

#### Upgrade Prompt

+ Because the API call mode has changed, all access codes need to be modified to upgrade.
Special Note
+ The v1.x version will no longer provide new features and will only maintain bug-related issues. It is recommended to update to v2.0.

### iOS SDK v2.2.1

#### Update Time

+ 2016-11-04

##### Change Log

+ Optimize to adapt to JPush SDK 2.2.0 to increase SDK stability
+ Fix the incorrect display named of message
+ Add events
    + kJMSGEventNotificationReceiveServerFriendUpdate; // event type: Non-client modifies friend relationship and receives friend update event

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

#### Upgrade Prompt

+ Note: The libresolv.tbd library is added to the project. Otherwise, the compiler will report an error (2.2.1 and above).

### iOS SDK v2.2.0

#### Update Time

+ 2016-10-18

##### Change Log

##### New Feature

+ Add friend function
+ Add friend note name and comment information settings
+ Add file message sending
+ Add location message sending
+ Add adaptation to iOS 10
+ Add events
    + kJMSGEventNotificationServerAlterPassword = 2, // event type: Non-client alters password for forced logout event
    + kJMSGEventNotificationUserLoginStatusUnexpected = 70,// event type: User login status exception event (requires login again)
    + kJMSGEventNotificationReceiveFriendInvitation = 51,// event type: receives a friend invitation
    + kJMSGEventNotificationAcceptedFriendInvitation = 52,// event type: The other party accepts your friend invitation
    + kJMSGEventNotificationDeclinedFriendInvitation = 53,// event type: The other party rejects your friend invitation
    + kJMSGEventNotificationDeletedFriend = 6, // event type: The other party removes you from his friends
Add interfaces：
+ JMSGEventDelegate
    + -(void)onReceiveNotificationEvent:(JMSGNotificationEvent *)event;// monitors event notifications. For example, buddy events, kicked events, etc. can all be listened to with this parameter.
+ JMSGFriendManager
    + +(void)getFriendList:;// gets friend list
    + +(void)sendInvitationRequestWithUsername: appKey: reason: completionHandler: ;// sends a request for adding friends
    + +(void)acceptInvitationWithUsername: appKey: completionHandler: ;// accepts friend invitations
    + +(void)rejectInvitationWithUsername: appKey: reason: completionHandler: ;// rejects friend invitations
    + +(void)removeFriendWithUsername: appKey: completionHandler: ;// deletes friends
+ JMSGUser
    + @property(nonatomic, assign, readonly) BOOL isFriend;// friends status
    + @property(nonatomic, copy, readonly) NSString *noteName;//note name
    + @property(nonatomic, copy, readonly) NSString *noteText;// remarks
    + -(void)updateNoteName: completionHandler: ;// modifies user comment name
    + -(void)updateNoteText: completionHandler: ;// modifies user comment information
+ JMSGFriendNotificationEvent
    + @property(nonatomic, assign, readonly) JMSGEventNotificationType eventType;// friend notification event type
    + - (NSString *JMSG_NULLABLE) getReason;// gets the reason for the event
    + - (NSString *JMSG_NULLABLE) getFromUsername;// username of the event sender
    + -(JMSGUser *JMSG_NULLABLE)getFromUser;// gets user of event sender
+ JMSGConversation
    + -(void)sendFileMessage: fileName: ;// sends file message
    + -(void)sendLocationMessage: longitude: scale: address: ;  sends location message
+ JMSGMessage
    + +(void)sendSingleFileMessage: fileName: toUser: ;// sends file message of single chats
    + +(void)sendSingleFileMessage: fileName: toUser: appKey: ;// sends cross-application file message of single chats
    + +(void)sendGroupFileMessage: fileName:toGroup: ;// sends file message of group chats
    + +(void)sendSingleLocationMessage: longitude: scale: address: toUser: ; // sends location message of single chats
    + +(void)sendSingleLocationMessage: longitude: scale: address: toUser: appKey: ;// sends cross-application location message of single chats
    + +(void)sendGroupLocationMessage: longitude: scale: address: toGroup: ; sends location message of group chats
+ JMSGFileContent
    + @property(nonatomic, copy, readonly) NSString *fileName;// filename
    + - (instancetype) initWithFileData: fileName: ;/ / initializates file content
    + -(void)fileData:(JMSGAsyncDataHandler)handler; gets data of file contents
+ JMSGLocationContent
    + @property(nonatomic, strong, readonly) NSNumber *latitude;// latitude
    + @property(nonatomic, strong, readonly) NSNumber *longitude;/ /longitude
    + @property(nonatomic, strong, readonly) NSNumber *scale;// zoom
    + @property(nonatomic, copy, readonly) NSString *address;// detailed address information
    + -(instancetype)initWithLatitude: longitude: scale: address: ;// initializes the file contents
Obsolete interface
+ JMSGUserDelegate
    + -(void)onLoginUserKicked;// Use the onReceiveNotificationEvent method in the JMSGEventDelegate class to monitor events such as kicking, user information expiration, and friends.

##### Bug Fix

+ Fix the problem that avatar can not obtained after the version upgraded
+ Fix the problem that group information and error information are returned meantime when the group is successfully created and the initialization of group members fails.

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Web SDK v1.2.0

#### Update Time

+ 2016-10-10

##### Change Log

##### New Feature

+ Increase the interface for sending pictures
+ Increase the interface for user registration
+ Increase cross-application interface for blacklist
+ Increase cross-application support between groups
+ Optimize Demo

#### Upgrade Prompt

+ Suggest an upgrade!

### iOS SDK v2.1.8

#### Update Time

+ 2016-09-22

##### Change Log


##### Bug Fix

+ Fix the crashes of application when switching back and forth at the same time of receiving a large number of messages
+ Fix occasional crashes when logging in
+ Fix the issue of duplicate events caused by problems on the network or in the background

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.4.2

#### Update Time

+ 2016-09-21

##### SDK Change Log


##### Bug Fix

+ Fix the problems on sending media messages

#### Upgrade Guide

+ Old jar package needs to be removed when jar package is updated to jmessage-sdk-1.4.2.jar.
+ Update the so library to libjpush220.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to the display requirements of rich media, a res folder is added to the SDK to store resource files. Users need to put the resource file in the corresponding folder into the project directory
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of SDK download package.

### Android SDK v1.4.1

#### Update Time

+ 2016-09-14

##### SDK Change Log


##### Bug Fix

+ Fixed the issue where the authorization box of location permission pops up when some models of mobile apps launch

#### Upgrade Guide

+ Old jar package needs to be deleted when updating to jmessage-sdk-1.4.1.jar.
+ Update the so library to libjpush220.so and delete the old version so. Pay attention to the structure of different cpu models.
+ Due to the display requirements of rich media, a res folder is added to the SDK to store resource files. Users need to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of SDK download package.

### iOS SDK v2.1.7

#### Update Time

+ 2016-09-09

##### Change Log


##### Bug Fix

+ Fixed the problem with incorrect timestamp of message in 32-bit system

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.4.0

#### Update Time

+ 2016-09-09

##### SDK Change Log


##### Bug Fix

+ Fix the problem that you may add yourself to blacklist when adding users into the blacklist across applicaions
+ Fix the problem that you may set DND to yourself when setting DND across applications.
+ Fix thet timeout of im request caused by crashes and restarts of the upper application process
+ Fix the problem that there is a chance that the message object is empty when clicking notification bar
+ Fix related internal logic error under special user name
+ Fix the problem with database access when there are too many local sessions.
##### New Feature

+ Add friend module
+ Added user note name and comment information settings
+ Add sending interface for file information
+ Add sending interface for location information
+ Add an instance interface to get the application appkey of the group owner in GroupInfo
+ getConversationList is sorted in descending order by default.
+ Optimize execution efficiency of interfaces
Add interfaces
+ ContactManager: Buddy management interface class
    + See api doc: ContactManager for specific definition
+ New instance interface in UserInfo class
    + Set note name：updateNotename
    + Set note text：updateNoteText
    + Remove the user from buddy list：removeFromFriendList
+ ContactNotifyEvent: Buddy related notification event class
    + See api doc: ContactNotifyEvent for specific definition
+ Add two types of message content:
    + File message：FileContent
    + Location Message：LocationContent
+ Add instance interface in the GroupInfo class：getOwnerAppkey
Note
Starting from this version, JChat source code will no longer be released as part of sdk zip with sdk. Instead, it is a simple JMessage Demo that shows only the interface usage.
See GitHub for previous JChat source code.

#### Upgrade Guide

+ When the jar package is updated to the jmessage-sdk-1.4.0.jar update, the old version jar package needs to be removed.
+ Update the so library to libjpush219.so and delete the old version so. Pay attention to the structure of different cpu models.
+ Due to the display requirements of rich media, a res folder is added to the SDK to store resource files. Users need to put the resource file in the corresponding folder into the project directory
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of SDK download package

### iOS SDK v2.1.6

#### Update Time

+ 2016-09-01

##### Change Log


##### Bug Fix

+ Fix the duplicate messages due to problems on the network or in the background

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Web SDK v1.1.2

#### Update Time

+ 2016-08-31

##### Change Log

+ Add type conversion and iOS receiving message

#### Upgrade Prompt

+ Suggest an upgrade!

### Web SDK v1.1.1

#### Update Time

+ 2016-08-30

##### Change Log

+ Fix the issue of sending group messages

#### Upgrade Prompt

+ Suggest an upgrade!

### Web SDK v1.1.0

#### Update Time

+ 2016-08-26

##### Change Log

##### New Feature

+ Add Do-Not-Disturb function
+ Support the reception of pictures and audio messages

#### Upgrade Prompt

+ Suggest an upgrade!

### Web SDK v1.0.1

#### Update Time

+ 2016-08-19

##### Change Log

##### New Feature

+ Add cross-application interface for obtaining user information
+ Add cross-application interface for sending single chat message

#### Upgrade Prompt

+ Optional upgrade!

### iOS SDK v2.1.5

#### Update Time

+ 2016-08-13

##### SDK Change Log


##### BugFix:

+ Fix the inconsistent message sequence caused by inconsistent local time and background time

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.3.1

#### Update Time

+ 2016-08-13

##### SDK Change Log


##### Bug Fix

+ Fix the inconsistent message sequence caused by inconsistent local time and background time

##### JChat Change Log

+ Adaptation to JMessage SDK 1.3.1

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.3.1.jar
+ Update the so library to libjpush216.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v2.1.3

#### Update Time

+ 2016-07-15

##### SDK Change Log

##### New Feature

+ Add Do-Not-Disturb function of this application and cross-application
+ Add cross-application group chat feature
+ Add blacklist feature of this application and cross-application
+ Add username(s) that exposes the event msg object and event msg; customed by developer
+ Added JMGGroup adds an attribute max_member_count, indicating the maximum number of members in the current group;
+ Added JMGGroup adds an attribute ownerAppKey, which indicates the appKey of the current group owner.
+ Add interfaces：
    + JMessage
        + +(void)noDisturbList:(JMSGCompletionHandler)handler;//User Do-Not-Disturb List Sets the global Do-Not-Disturb indicator
        + +(BOOL)isSetGlobalNoDisturb;//Get global Do-Not-Disturb status
        + +(void)setIsGlobalNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//Set whether global Do-Not-Disturb
        + +(void)balckList:(JMSGCompletionHandler)handler;//Get blacklist
    + JMSGUser
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//Get Do-Not-Disturb Status
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//Set user Do-Not-Disturb (support cross-application settings)
        + @property(nonatomic, assign, readonly) BOOL isInBlacklist;//get status of blacklist
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray completionHandler:(JMSGCompletionHandler)handler;//Add blacklist
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray completionHandler:(JMSGCompletionHandler)handler; //Delete blacklist
        + +(void)addUsersToBlacklist:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//Add a blacklist across applications
        + +(void)delUsersFromBlacklist:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler)handler;//Remove blacklist across applications
    + JMSGGroup
        + @property(nonatomic, copy, readonly) NSString *ownerAppKey;//appkey of owner
        + @property(nonatomic, strong, readonly) NSString *maxMemberCount;//Get the maximum number of groups
        + @property(nonatomic, assign, readonly) BOOL isNoDisturb;//Get Do-Not-Disturb status
        + -(void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;//Set group message Do-Not-Disturb (support cross-application settings)
    + JMSGEventContent
        + -(NSString *JMSG_NULLABLE)getEventFromUsername;//Get the username of initiator of the event
        + -(NSArray *JMSG_NULLABLE)getEventToUsernameList;// Get the username list of object acted by events
    + JMSGMessage
        + +(void)sendSingleTextMessage:(NSString)text toUser:(NSString)username appKey:(NSString *)userAppKey; //Send cross-application text message of a single chat
        +  (void)sendSingleImageMessage:(NSData) imageData toUser:(NSString)username appKey:(NSString *)userAppKey; //send cross-application picture message of a single chat
        +  (void)sendSingleVoiceMessage:(NSData)voiceData voiceDuration:(NSNumber) duration toUser:(NSString) username appKey:(NSString)userAppKey; //send cross-application voice message of a single chat
    + Cross-application group chat
        + -(void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//Add cross-application group members
        + -(void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString))usernameArray appKey:(NSString *)userAppKey completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;//Delete cross-application group members

##### Bug Fix

+ Fix the problem that group event msg event cannot be customized;

#### Upgrade Guide

+ Replace the old file with the same name in the original project with the new version of the JMessage.framework file!

### Web SDK v1.0.0

#### Update Time

+ 2016-07-13

##### Change Log

+ First release of the JMessage Web SDK
+ Chat supports: single chat, group chat
+ Chat content: text
+ Provide user management, group management and acquisition of session list

#### Upgrade Prompt

+ Optional upgrade!

### Android SDK v1.3.0

#### Update Time

+ 2016-07-12

##### SDK Change Log

##### New Feature

+ Increase cross-application capabilities for group, blacklist and DND
+ Add Global Do-Not-Disturb interface
+ Add interfaces
    + JMessageClient
        + setNoDisturbGlobal Set global Do-Not-Disturb identifier
        + getNoDisturbGlobal Get Global Do-Not-Disturb identifier
        + addGroupMembers Add group members (cross-application)
        + removeGroupMembers remove group members (cross-application)
        + addUsersToBlacklist Add users to the blacklist (cross-application)
        + delUsersFromBlacklist remove users from the blacklist (cross-application)
    + GroupInfo
        + getGroupMemberInfo Get information of group members(cross-application)

##### Bug Fix

+ Fix the problem with low probability of receiving messages
+ Fix the occasional crashes of native layer

##### JChat Change Log

+ Adaptation to JMessage SDK 1.3.0
##### New Feature

+ Adaptation to the cross-application function of group chat, blacklist and Do-Not-Disturb
+ Add global Do-Not-Disturb function

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.3.0.jar
+ Update the so library to libjpush216.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v2.1.1

#### Update Time

+ 2016-06-15
Version Number
+ JMessage SDK 2.1.1
+ JChat 1.1.0b1893

##### Change Log

+ Add supports for IPv6 networks.

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.2.5

#### Update Time

+ 2016-06-12

##### SDK Change Log

##### New Feature

+ Conversation object adds an interface to set the number of local unread messages
+ Add interface：
    + conversation.setUnReadMessageCnt

##### Bug Fix

+ Fix the problem that prompt text displayed at other members is incorrect when the group member quits the group
+ Fix the problem that the local owner information is not updated after the owner quits the group.
+ Fix the problem that printing of targetName in the received message is empty when the user received message for the first time
+ Fix the occasional crash of application when sending group chat message
+ Fix the abnormal operation of database when quickly loging in to account B after logined to an account A
+ Fix the problem that sdk is not updated after dev api removes DND of group chat
+ Fix the problem that messageid field value is 0 after the SDK receives the group event
+ Optimize the efficiency of data processing in groups with a large number of group members

##### JChat Change Log

+ Adaptation to JMessage SDK 1.2.5

##### Bug Fix

+ Fix the bug when 1.2.9 pulldowns the refresh
+ Fix the bug that 1.2.9 may have session lost after receiving message
+ Optimize the stuck UI after receiving a large number of offline messages

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.2.5.jar
+ Update the so library to libjpush211.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v2.1.0

#### Update Time

+ 2016-05-10
Version Number
+ JMessage SDK 2.1.0
+ JChat 1.1.0b1870

##### Change Log

+ Implement cross-application single chat
+ Support the upper limit of VIP user groups exceeding 200

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.2.3

#### Update Time

+ 2016-04-07

##### SDK Change Log


##### Bug Fix

+ Fix the crash caused by upgrading from old version to 1.2.1

##### JChat Change Log

+ Update JMessage jar to 1.2.3

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.2.3.jar
+ Update the so library to libjpush213.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### Android SDK v1.2.1

#### Update Time

+ 2016-03-31

##### SDK Change Log

##### New Feature

+ Add Do-Not-Disturb Function
+ Support the upper limit of VIP user groups exceeding 200
    + The max_member_count attribute is added to groupInfo to indicate the maximum number of members in the current group.
+ If you want to pass List as the parameter in the external interface, limit the list size.
+ Add interfaces：
    + JMessageClient
        + JMessageClient.getNoDisturbList(GetNoDisturbListCallback callback) Get Do-Not-Disturb list of the user
    + UserInfo
        + userinfo.setNoDisturb(int noDisturb,Callback callback) Set Do-Not-Disturb status of the user
        + userinfo.getNoDisturb() Get Do-Not-Disturb status of the user
    + GroupInfo：
        + groupinfo.setNoDisturb(int noDisturb, Callback callback) Set Do-Not-Disturb status of the group
        + groupinfo.getNoDisturb() Get Do-Not-Disturb status of the group
        + groupinfo.getMaxMemberCount() Get maximum limit of group members

##### Bug Fix

+ Fix the problem that return code is 0 when the api calls GetGroupInfo to get a group that has been destroyed
+ Fix the problem that database reports an error when invoking when the message is being sent

##### JChat Change Log

+ Adaptation to JMessage SDK 1.2.1
##### New Feature

+ Add Do-Not-Disturb function.

##### Bug Fix

+ Fix the problem that the project reports an error after compileSdkVersion is changed to 23 (android 6.0).
+ Fix the problem that interface is unchanged after adding group members
+ Optimize the search of group member

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.2.1.jar
+ Update the so library to libjpush211.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v2.0.1

#### Update Time

+ 2016-03-22
Version Number
+ JMessage SDK 2.0.1
+ JChat 1.1.0b1611

##### Change Log

+ Fix the failure of message sending due to group information is not synchronized when switching devices and changing group members.

#### Upgrade Prompt

+ Suggest an upgrade!
    ### • JMessage iOS SDK。 Due to a wide range of changes at the API and Model level, it is recommended to refer to the JChat project to adapt the new JMessage iOS SDK.


#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.2.0

#### Update Time

+ 2016-03-07

##### SDK Change Log

##### New Feature

+ Implement cross-application chat
+ getServerMessageId interface is added in message
+ Add setDebugMode interface
+ Add event processing for server to modifying the user password
+ Add interfaces
    + Conversation
        + conversation.getTargetAppkey gets the appkey of the session object (single chat only)
        + Conversation.createSingleConversation(username,appkey) creates a cross-application session for the specified appkey
        + JMessageClient.getSingleConversation(username,appkey) gets the session with the user under the specified appkey.
        + JMessageClient.enterSingleConversation(username,appkey) enters the session with the user under the specified appkey.
        + JMessageClient.deleteSingleConversation(username,appkey) deletes the session with the user named appkey
    + Message
        + message.getTargetAppKey gets the appkey of the message object. (Single chat message only)
        + message.getFromAppKey gets the appkey of the message sent.
        + message.getServerMessageId gets the messageId of corresponding message to the server.
    + UserInfo
        + userinfo.getAppKey gets the appkey to which the user belongs.
        + JMessageClient.getUserInfo(username,appkey,callback) gets the user information under the specified appkey.
    + JMessageClient
        + setDebugMode opens debug mode of JMessage, which is equivalent to JPush's setDebugMode.
    + Obsolete interface
        + The interface name of JMessageClient.enterSingleConversaion is misspelled, and use JMessageClient.enterSingleConversation instead.
        + The interface name of JMessageClient.exitConversaion is misspelled, and use JMessageClient.exitConversation instead.
        + Use LoginStateChangeEvent to replace UserDeletedEvent and UserLogoutEvent.

##### Bug Fix

+ Fix the problem of getting groupMembers to return null directly after getting gid via getGroupList
+ Fix the problem of without deleting notification bar message when deleting a session
+ Fix spelling error of conversation interface name
+ Fix the title error of creation session when received the message for the first time.
+ Fix the problem of createConversation interface not doing login verification.
+ Fix a bug where looping for userinfo occurs across applications
+ Fix the problem that cache information of login user is not flushed when calling login for multiple times without adjusting logout

##### JChat Change Log

+ Adaptation to JMessage SDK 1.2.0
##### New Feature

+ Conversation list provides disconnected prompts
+ Drafts can be displayed in the conversation list

##### Bug Fix

+ Fix the bug that some models failed to upload pictures
+ Fix the bug that throwing WindowWarning when App starts
+ Fix the bug with black shading after the dialog box was cropped
+ Fix the problem that the corresponding notification bar is not cleared after deleting the local cross-application session
+ Fix the problem that  username of the group member does not display in the group chat details after clicking to delete the member and entering to the chat members
+ Fix the problem that the interface stays in the state of the circle in group chat details interface, after clicking on the group member interface to add non-existent users
+ Fix the problem that group desktop is overwritten when the user exits the group.

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.2.0.jar
+ Update the so library to libjpush207.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v2.0.0

#### Update Time

+ 2016-02-22
Version Number
+ JMessage SDK 2.0.0
+ JChat 1.1.0b1460

##### Change Log

+ Adjustment of message structure: A message is now composed of a JMSGMessage class plus multiple types of Content, such as JMSGTextContent;
+ Objectivization: There are target objects in the session (JMSGUser or JMSGGroup), and there are target JMSGUser objects and fromUser objects in the message.
+ Notification adjustment: The method of changing from the previous NSNotification to Delegate is more simple and intuitive.
+ Performance optimization: For commonly used information, the SDK internally caches to reduce file and network access.
+ Complete documentation comments are added on the external API headers, including recommendations for use.

#### Upgrade Prompt

+ Suggest an upgrade!
    ### • Due to a wide range of changes at the API and Model level, it is recommended to refer to the JChat project to adapt the new JMessage iOS SDK


#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.1.5

#### Update Time

+ 2015-12-11

##### SDK Change Log

##### New Feature

+ Group member changes event all throw sdk without filtering.
+ Small user avatar for caching in sdk internally
+ Internal concurrent threads control, to prevent too many concurrent threads from causing problems
+ Optimize execution efficiency of network task
+ Storage of local media file is categorized by session for easy cleanup
+ Add interfaces
    + ImageContent adds an interface for constructing instances by passing Bitmaps
    + Conversation.CreateMessage adds a custom FromName interface. Developers can customize the FromName of the message
    + UserInfo adds the asynchronous interface getAvatarBitmap and getBigAvatarBitmap of the avatar bitmap, and sdk internally caches the bitmap of the avatar.
+ Obsolete interfaces:
    + EventNotificationContent.containsGroupOwner
    + UserInfo.getAvatarFileAsync

##### Bug Fix

+ The request will report an error when using a custom class to inherit BasicCallback
+ Some external interfaces do not have a login check and there will be a problem with invoking an interface when not logged in
+ Fix the bug where the other party will fail to download after sending large voice files
+ Fix the group ID that displayed when receiving the group message for the first time
+ Fix the problem of returning a null when calling both big avatars and small avatars at the same time

##### JChat Change Log

+ Adaptation to JMessage1.1.5
##### New Feature

+ Send one by one when sending multiple pictures,
+ Albums are sorted by modification time
+ Crop when uploading an avatar
+ Optimization: Could send 9 pictures at a time successfully, but with a low efficiency
+ Optimization: Suggesting that it is loading after clicking jchat user to view his avatar in [I], which means the experience is needed to be optimized.

##### Bug Fix

+ Fix the issue of multiple updates if there is no previous message when loading a previous message
+ Fix the exception when clearing the history messages in single chats
+ Fix the occasional NPE exception when sending multiple pictures
+ Fix the problem that when sending 9 pictures, it may get stuck on the prompt screen that is being sent, but the picture is not sent successfully.
+ Fix the problem that the avatar can not be updated by selecting picture from file management when Xiaomi 4 phone updates the avatar.

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.1.5.jar
+ Update the so library to libjpush205.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### Android SDK v1.1.4

#### Update Time

+ 2015-09-28

##### SDK Change Log

##### New Feature

+ Add blacklist function
+ Add user delete event
+ When a group chat message is received, tickerText in the notification bar displays the sender's displayName instead of the group name
+ New interfaces: createGroupConversation(long), createSingleConversation(String), getTargetInfo(), getLatestMessage()
+ Obsolete interfaces: createConversation(ConversationType, long), createConversation(ConversationType, String), getTargetID(), getLatestMsgDate() getLatestType(), getLatestText()
+ Add interfaces: getTargetInfo(), getFromUser()
+ Obsolete interfaces: getTargetID(), getTargetName(), getFromID(), getFromName(), getFromType()
+ Add interfaces: new createImageContentAsync in ImageContent class to create ImageContent interface asynchronously

##### Bug Fix

+ Fix the problem that group chat details UI is not updated after dev api adding the deletion of group users.
+ Fix the problem that the method documentation of customContent.setContentType does not explain its role
+ Fix the problem that nickname settings will only cause an anomaly if only in the expressions and return an error on the server
+ Fix the problem that IM cannot log in after invoking stopPush.
+ Fix the problem that the Demo APP can still register successfully even though package name of JMessage configuration file does not match the appkey.
+ Fix the direct crash when createSendMessage interface is called when the user is not logged in.
+ Fix the problem that status of the previously sent message was always "sending" after the user was kicked offline while sending media information
+ Fix the problem that corresponding event is not thrown to the upper layer when dev api adding/deleting group users
+ Fix an issue where the notification bar did not jump after clicking when receiving a rich media push

##### JChat Change Log

##### New Feature

+ Chat messages support paging loading
+ Add "About" page
+ Optimize the performance of chat, chat details interface loading
+ When blacked out, use a custom message "message has been sent but rejected by the other party" to prompt the user

##### Bug Fix

+ Fix the problem that UI interface shows 100% after the picture was successfully sent
+ Fix the problem that minus sign sometimes loaded 5/6s to show after the group owner clicking to enter the group [chat details],
+ Fix the problem of no response loading after clicking on the session if there are too many messages in a session window.
+ Fix the bug that the interface will not be closed after the soft keyboard pops up and shut-off button of soft keyboard is clicked.
+ Fix the bug where WindowLeak was thrown abnormally by clicking the OK button after being kicked off the line
+ Fix possible exceptions after starting APP: RuntimeException: Performing stop activity that is not resume
+ Fix the bug when clicking the recording after some phones setting recordings as inquiry or forbidden
+ Fix the bug that chat titles with emoji display abnormally
+ Fix the inconsistency in the order of previewing large picture and chat interface picture messages in the chat interface
+ Fix the bug of not displaying the username when entering the chat interface without the nickname filled in through the interface
+ Fix the bug of APP when clicking on the original image and sending the image after selecting the image
+ Fix the bug that picture progress is not updated when reentering the chat interface via chat details
+ Delete the generated picture after the picture is sent successfully
+ Fix the bug of APP when receiving offline messages

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Need to delete the old version jar package when the jar package is updated to the jmessage-sdk-1.1.4.jar
+ Update the so library to libjpush205.so and delete the old version so. Pay attention to the structure of different cpu models
+ Due to display requirements of rich media, a res folder is added to the SDK to store resource files. The user needs to put the resource file in the corresponding folder into the project directory.
+ If you are upgrading from an earlier version, it is recommended to update the configuration of AndroidManifest.xml file by referring to the latest demo version of the SDK download package.

### iOS SDK v1.0.6

#### Update Time

+ 2015-09-14
Version Number
+ JMessage 1.0.6b283
+ JChat 1.0.2b11

##### Change Log

+ Bugs caused by sending and receiving too many messages
+ Resolve conflicts when referring to third-party library
+ Qiniu Token failed and cannot be restored.
+ Crashes occur when sending voice or uploading pictures to Qiniu
+ Width pictures received are long pictures.
+ Downloaded original image is actually a thumbnail
+ Solve the crash of receiving and sendig custom type message
+ Playing voice and recording voice cannot be performed at the same time
+ Fix the problem that big picture cannot be downloaded when iOS side sent to the Android side
+ Fix the problem that voice cannot be downloaded properly
+ Fix the problem of APNS user not displaying nickname but username
+ Fix error messages when converting json
+ Add login verification to API
+ Solve the bug reported by badge

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Replace the old file with the same name under the original project with a new version of the JMessage.framework file

### Android SDK v1.1.3

#### Update Time

+ 2015-08-17

##### Change Log

+ Fix the problem that button to enter the [chat details] will disappear in the chat interface of the group chat when network is disconnected
+ Fix the issue thar jchat receiver notification bar will show when sending custom message
+ Fix the problem that return code is unreasonable when interface getAvatarFileAsync, which is used to get the user avatar asynchronously, gets information of user without avatar
+ Fix the problem that owner's username is not displayed in invitee's notification when an owner without a nickname invites someone to enter the group
+ Fix the problem that events are rarely lost due to network instability when receiving invitation to entering the group
+ JChat fixes the problem that the first picture received will not be download automatically
+ JChat fixes the crashes of application when selecting the group members from the group details to send the message

#### Upgrade Prompt

+ Suggest an upgrade!

#### Upgrade Guide

+ Update jar package to jmessage-android-1.1.3.jar, and delete the old version of jar
+ Update so library, /libs/armeabi/libjpush205.so . Also delete the old version of so

### Android SDK v1.0.18

#### Update Time

+ 2015-04-01

##### Change Log

+ First release of JMesssage Android SDK
+ Chat supports: single chat, group chat
+ Chat content: text, pictures, voice intercom
+ Provides user management and group management

#### Upgrade Prompt

Optional upgrade!

#### Upgrade Guide

+ After opening, replace your package name and APPKey according to the prompt of AndroidManifest.
+ Replace "import cn.jpush.im.android.demo.R;" with "import your package name. R;"
+ If you are a Android Studio user, check that the applicationId in build.gradle is consistent with your package name