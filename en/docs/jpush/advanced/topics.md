# Advanced Topics

This document describes some of the advanced, behind-the-scenes logic of JPush.

## Message Life Cycle

When a message is pushed by JPush from the developer's AppServer (called via the API) or the Portal, it does not mean that the message was successfully pushed to the user's device immediately. In fact, this simply means that this message was received by the JPush server and entered the ready-to-push state. What will happen after this message is received depends on several factors.

Ideally, when the user device and the server are still connected and there are no other factors that cause this message to be dropped, the user will immediately receive this message.

Next, depend on the specification of the time_to_live field. If 0, the message is not saved offline, that is, if the user is not currently online, the user will never receive the message. When time_to_live is greater than 0, the offline message time of the specified duration is retained.

After that see if override_msg_id is specified. If a new message whose override_msg_id is the same as the existing one in the offline message, this new message will overwrite the old message.

### Offline Messages

JPush currently supports 5 offline messages by default. If there are special needs, please contact the business team.

On the Android platform, when users go online, offline message will be pushed.

In app push in iOS is the same as Android.

iOS notifications are determined by the APNs offline message strategy (last one) because they are directly based on the push channel APNs of the Apple platform itself.

API 2.0 provides a time_to_live field that allows you to set the retention time in seconds when calling push messages. 0 means that offline messages are not retained, that is, messages are only pushed to online users. Up to 10 days.

### Message Coverage

JPush defines message override logic based on override_msg_id.

That is, for the same application, if a new message whose override_msg_id exists and is the same as the old one, it is considered to overwrite the old message.

This situation is different for saving offline messages:：

* If the client has already received, and the user has opened notification: the new message (override_msg_id exists) is still displayed in the notification bar, and the user sees a new message.
* If the client has received but it is still in the notification bar: New messages will overwrite old messages in the notification bar. The user sees the new message content.
* If the client has not yet received and the message is still in the offline message, then: the new message will overwrite the old message and the user will not receive the old message.

### Message Deletion

In general, after a message is pushed out, if a user is online, he will receive it immediately, so there is no chance of repenting (deleting).

JPush provides a message coverage mechanism that allows you to have the opportunity to update messages that are received by users who are temporarily offline.

JPush has not yet opened the mechanism and interface for deleting "offline messages". If there is a need for special reasons, please send an e-mail to support@jpush.cn, and have support personnel JPush to operate.

### Push Order

JPush does not guarantee the order of push messages, so the client will receive message in the same order.

But most of the time message received by the user is pushed in order, even if the offline message is saved in order.