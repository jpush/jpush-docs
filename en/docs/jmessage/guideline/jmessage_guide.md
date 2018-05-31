# Product Introduction of JMessage

## Know JMessage

JMessage is dedicated to helping apps solve issues of in-app chats and cross-application chats, so that developers can integrate SDKs to quickly achieve stable and reliable chat features. The iOS, Android, web, and Windows SDKs, as well as the Rest API and background management system are currently available to meet the needs of developers in different scenarios, greatly reducing development costs and improving efficiency.

### Modular Jiguang Developer SDK

The Jiguang Developer Service SDK adopts a modular usage model, namely a core module (JCore) + N kinds of services (IM, JPush, JAnalytics) to facilitate developers to integrate multiple Jiguang developer services at the same time and optimize the problem of duplicate function modules when multiple modules are used simultaneously. As shown below:
![jiguang](../image/sdk_model.png)

### The difference between JMessage and JPush

JMessage starts from the IM usage scenario and sends messages to the user based on the login account. However, JPush meets the push scenario, faces the mobile device, and pushes according to the device's tag and usage attributes.

<div class="table-d" align="center" >
  <table border="1" width="100%">
    <thead>
      <tr  bgcolor="#D3D3D3" >
        <th></th>
        <th>JPush</th>
        <th>JMessage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Usage scenarios</td>
        <td>Application push</td>
        <td>IM chat, social</td>
      </tr>
      <tr>
        <td>Object-oriented</td>
        <td>Equipment</td>
        <td>User, account</td>
      </tr>
      <tr>
        <td>Message object</td>
        <td>App operators or App Server pushes to user</td>
        <td>Users communicate with each other</td>
      </tr>
      <tr>
        <td>Sending method  </td>
        <td>Supports broadcast, tag, or single device</td>
        <td>Single chat, group chat</td>
      </tr>
    </tbody>
  </table>
</div>

### How to choose JPush and JMessage services

Developers can choose the applicable business according to their own business scenarios.

* If your application needs instant messaging capabilities to meet the interactive needs of users, then JMessage is for you.
* If your application is primarily based on sending feature announcements, campaign promotions, subscriptions and broadcast content, you should choose a more concise push service. If subsequent services need to be extended, JMessage can be integrated again without any impact on the original Push function.

## The Basic Concept of JMessage

### username

This is the username of the App. It is used to uniquely identify the user in the app and must be unique.

What the App actually uses when calling the IM SDK can be its user ID, user account name, or Email. Any one of them can uniquely identify its user.

### groupId

The group ID will be obtained when the app creates a group by using the grouping function provided by JMessage. This group ID is required for sending group messages, adding people, and kicking people.

###AppKey

AppKey is used to uniquely identify an app and needs to be created in the management console. When the SDK is integrated, this key needs to be configured so that the system can identify that which application owns the current user .

#### Note: The username must be unique in the same AppKey, and the username can be the same between different AppKeys.

### Architecture of IM and JPush

![jpush_im_architecture](../image/jmessage_architecture.png)

The above figure shows the overall architecture of JPush and IM services. It can be understood that:

* Push supported in the IM SDK uses the same long network connection as JPush.
* Server-side access servers are shared between two services.
* Above the access server, the two services are relatively independent and separate.

### The Advantages of JMessage

* Technically based on large-scale, highly concurring and stable push services provided by JPush as well as inherit these characteristics.
* The IM SDK shares a network connection with the JPush SDK and supports both IM and Push services.
* IM is perfectly compatible with Push. Users who have already used the Push service can integrate IM and upgrade smoothly.
* The JPush team had previously developed the IM App and have a deeper understanding of the IM business to continuously improve and revolutionize IM services.

## Functions and Features of JMessage

### Overall characteristics

* Message type: text, voice, picture, geographic location, file, custom message, etc.
* Chat methods: single chat, group chat.
* Platform support: multi-platform interoperability across Android, iOS, Web.
* User maintenance: registration, login, avatar, and other information.
* Group maintenance: create groups, join groups, leave groups.
* Offline messages: choose whether you want to save offline messages
* Relationship mode: friend mode and no friend mode
* Cross-application chat: users in different applications can communicate with each other

### REST API

Provides HTTP APIs that meet the REST specification to use commonly used features.
There are several categories:

* registered users (support batch)
* Send a message
* User information maintenance
* User relationship maintenance
* Group maintenance

### Management console

Integrated with the JPush console for basic maintenance of users and groups.

* Create an application
* Registered user
* Manage users
* Maintain group
* Send a message

## Integration Process

1. Create an app on the web console and get the AppKey. If you have used JPush before, you can directly use the old AppKey.

2. Integrate the client SDK.

* Integrate IM SDK into App
* Android developers please refer to the document: [JMessage Android SDK Integration Guide](/jmessage/client/jmessage_android_guide/)
* iOS developers please refer to the documentation: [JMessage iOS SDK Integration Guide](/jmessage/client/jmessage_ios_guide/)

3. Send a message by using the management console, or by calling the REST API to manage users.

### Related Documents

* [JMessage Android SDK Development Guide](../client/im_sdk_android/)
* [JMessage iOS SDK Development Guide](../client/im_sdk_ios/)
* [JMessage WEB SDK Development Guide](https://docs.jiguang.cn/jmessage/client/im_sdk_js/)
* [JMessage Windows SDK Integration Guide](https://docs.jiguang.cn/jmessage/client/im_sdk_win/)

