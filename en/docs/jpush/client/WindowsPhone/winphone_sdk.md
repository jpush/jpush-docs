# Windows Phone SDK 
- Download [WinPhone Client SDK](../../resources/#wp-sdk)
![jpush_wp](../image/jpush_wp.png)

JPush WP Push includes 1 section, MPNs push (proxy).
The red part is the MPNs push, which means the application of the JPush agent developer pushed to the Microsoft MPNs server. The application push to the WP device via the Microsoft MPNs Server.
The blue part is JPush in-app push, but currently not support in-app messages.

### Notifications on the Windows Phone Platform
This notification is sent by the JPush server agent to Microsoft's MPNs server and displayed on the notification bar of the Windows Phone client.
This notice meets the relevant specifications of the MPNs. Currently JPush only supports the toast type.

```
In-app messages are temporarily not supported on the Windows Phone platform.
```
### Windows Phone SDK Integration
Please refer to the following documents and tutorials to integrate the WinPhone SDK
- [3 Minutes Fast Demo (Winphone)](winphone_3m)
- [WinPhone Integration Guide](winphone_guide)
- [WinPhone API](winphone_api)