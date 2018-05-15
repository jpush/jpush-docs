# Advanced Application Scenario

## Each Message Needs to be Received

### Business Scenario

In some scenarios, such as corporate office class and order status notifications, the pushed messages need to ensure that users must receive them; if they are not received in time, further measures need to be taken.

### Problem Analysis

Pushing notifications/messages through the network has a possibility that the notifications cannot reach the users in a timely manner (because of the mobile phone and the network). Therefore, you need to check in a timely manner to confirm whether the client has received.

### Solutions

* The JPush Report API provides delivery statistics for a message. This statistic is real-time, and be checked immediately by calling this Report API after push. It allows continuous checks for multiple times at a certain interval;
* The developer app feedbacks the confirmation of push message received to their application server.

### Implement Chat Based on JPush
To meet the developer's IM functional requirements, Jiguang provided JMessage. JMessage is based on the long connection technology of JPush and adds the IM feature to meet the typical IM App usage scenario.
The App that integrates the JMessage SDK and JPush share the same connection and have full JPush functionality.
Detailed Reference: [JMessage Guide](../../jmessage/guideline/jmessage_guide/)

## Offline Messages with Multiple Account Logins

### Business Scene

The client app is a QQ-like (chat) client application that supports multiple account logins.

The chat account UID is set to a JPush alias so that chat users can push messages to each other through aliases.

After the A account is logged in (binding A uid to an alias), you can push messages to A through JPush.

After A quits, log in to B (update bound B uid to alias). At this time, you can push messages to B through JPush. However, if you continue to push a message to A, you will get an error and cannot find the target user by alias A uid.

### Problem Analysis

The JPush alias is set for the device. Only one alias can be bound on one device. The new alias will be overwritten, and the alias that is overwritten will no longer correspond to the device.

This is the mechanism of JPush.

In this scenario, if the A user does not log out, you can still push a message to him and let JPush save the offline message so that A can continue to receive the message when he logs in again.

This business scenario requirement is overly dependent on JPush.

JPush just does the "push" this only function. JPush provides offline messages for a limited period of time. It is part of the push mechanism, not to save the history message.

If the developer application wants to do recording of history message, it should be done by its own application server.

### Solutions

After the user A logs off, when there are other users who want to send messages to user A, the developer application server should save the message history and not push it to user A. Only user A can log in again, you can push messages to them.

## Alias ​​Setting for Multiple Account Login

### Business Scene

Client App supports multiple account logins.

When each user logs in, the UID of the account is set as an alias so that the user's push message is received.

However, there is a problem: After A logs out, the push message sent to A before B updating its alias will be received by B.

### Problem Analysis

The alias is bound to this device (this application). Before B succeeds in setting up an alias, the information pushed to A is always received.

### Solutions

Before A user logs out, make an alias setting: Set the alias to blank.

Then the push to A will not be pushed to this setting.