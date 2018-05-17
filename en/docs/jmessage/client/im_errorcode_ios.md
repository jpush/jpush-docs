# Definition of IM SDK ErrorCode

The ErrorCode in the following list may appear during the call of SDK. The list below is for your reference.

## JMessage iOS

Error codes that only appear in the iOS SDK

| **Code** | **Error Message**                            | **Instructions**                                                                                         |
|----------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 860015   | Network downloading media failed.            | Failed to download media file.                                                                           |
| 860018   | Network uploading media failed               | Failed tot upload media file.                                                                            |
| 860020   | Getting upload token failed                  | Failed to get media file upload token                                                                    |
| 860021   | Network result is invalid                    | Data returned from the server is not expected.                                                           |
| 861004   | DB Migrating failed                          | Failed to update SDK database                                                                            |
| 861100   | Appkey is invalid                            | Appkey is illegal                                                                                        |
| 861101   | Internal param check failure                 | Internal parameter verification goes wrong                                                               |
| 863001   | Username is invalid                          | Invalid username                                                                                         |
| 863002   | Password is invalid                          | Invalid password                                                                                         |
| 863004   | User is not at Login state                   | User is not logged in                                                                                    |
| 863005   | Request number over flow                     | The number of requesting users exceeds the limit (the maximum number of single request is 500 currently) |
| 863006   | User repeat Login fault                      | Repeated login error                                                                                     |
| 863007   | User is logouting                            | The user is exiting                                                                                      |
| 863008   | Add friend fault                             | Failed to add friends                                                                                    |
| 863009   | Delete friend fault                          | Failed to delete friend                                                                                  |
| 864001   | It is not a media message                    | Not a media message                                                                                      |
| 864002   | Media resource is missing                    | Miss media resources unexpectedly                                                                        |
| 864003   | Media crc32 code is invalid                  | Invalid media CRC code                                                                                   |
| 864004   | Media crc check failure                      | Failed to vertify media CRC                                                                              |
| 864005   | Uploading media file is empty                | Uploaded media file was accidentally lost                                                                |
| 864007   | Media Hash value verify failure              | Failed to text Media file Hash                                                                           |
| 865001   | Message content is invalid                   | Invalid message content                                                                                  |
| 865002   | Message is nil                               | Message is empty                                                                                         |
| 865003   | Message is not prepared for sending          | Message did not meet the conditions for sending                                                          |
| 865004   | You are not in the group for sending message | You are not a group member who sent a group chat message                                                 |
| 866001   | Unknown conversation type                    | Unknown session type                                                                                     |
| 866002   | Conversation username is invalid             | Invalid username of single chat session                                                                  |
| 866003   | Conversation groupId is invalid              | Invalid conversation ID of group chat                                                                    |
| 867001   | GroupId is invalid                           | Invalid group ID                                                                                         |
| 867002   | Group fields are invalid                     | Invalid group field                                                                                      |
| 868001   | ChatRoom not support                         | Chat room is not supported                                                                               |
| 868002   | ChatRoom not exist                           | Chat room does not exist                                                                                 |
| 869999   | Unknown SDK error                            | Unknown SDK error code                                                                                   |

If the corresponding error code is not found in the above list, check the [Server Error Code](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)

## Related Documents

-   [Android SDK Error Code](../client/im_errorcode_android/)

-   [Server Error Code](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)
