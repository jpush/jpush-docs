# Definition of JShare SDK ErrorCode 

The ErrorCode in the following list may appear during the calling of SDK. Below is for your reference to understand its meaning.

| **Code** | **Error Message**                    | **Remarks**                                                  |
|----------|--------------------------------------|--------------------------------------------------------------|
| 40001    | appid missing                        | Missing appid parameter                                      |
| 40002    | appkey missing                       | Missing appkey parameter                                     |
| 40003    | secret missing                       | Missing secret parameter                                     |
| 40004    | mediaType missing                    | Missing mediaType parameter                                  |
| 40005    | invalid mediaType                    | Invalid mediaType                                            |
| 40006    | platform missing                     | Missing platform parameter                                   |
| 40007    | invalid platform                     | Invalid platform                                             |
| 40008    | SinaRedirectUri missing              | Missing SinaRedirectUri parameter                            |
| 40009    | not install app                      | Not install the application                                  |
| 40010    | unfinished initialization            | Not initialize                                               |
| 40011    | shareParams missing                  | Missing shareParams                                          |
| 41001    | text size out of limit               | Length of text parameter exceeds the limit                   |
| 41002    | image url size out of limit          | Length of image link field exceeds the limit                 |
| 41003    | image size out of limit              | Image size exceeds the limit                                 |
| 41004    | url size out of limit                | Url length exceeds the limit                                 |
| 41005    | audio url size out of limit          | Length of audio url exceeds the limit                        |
| 41006    | video url size out of limit          | Length of video url exceeds the limit                        |
| 41007    | app url size out of limit            | Length of app url exceeds the limit                          |
| 41008    | app size out of limit                | App size exceeds the limit                                   |
| 41009    | file size out of limit               | File size exceeds the limit                                  |
| 41010    | emotion size out of limit            | Emotion size exceeds the limit                               |
| 41011    | title size out of limit              | Title parameter exceeds the limit                            |
| 41012    | description size out of limit        | Description parameter exceeds the limit                      |
| 41013    | thumb size out of limit              | Thumbnail parameter exceeds the limit                        |
| 41014    | image is empty                       | Picture parameter is empty                                   |
| 41015    | audio url is empty                   | Audio url parameter is empty                                 |
| 41016    | video url is empty                   | Video url parameter is empty                                 |
| 41017    | app url is empty                     | App url parameter is empty                                   |
| 41018    | emotion is empty                     | Emotion parameter is empty                                   |
| 41019    | file is empty                        | File parameter is empty                                      |
| 41020    | image count out of limit             | Number of pictures exceeds the limit                         |
| 41021    | url is empty                         | Url parameter is empty                                       |
| 41022    | text is empty                        | Text parameter is empty                                      |
| 41023    | fileExt size out of limit            | FileExt exceeds the limit                                    |
| 41024    | sinaObjectId size out of limit       | SinaObjectId exceeds the limit                               |
| 41025    | title is empty                       | Title is empty                                               |
| 41026    | invalid url                          | Url is invalid                                               |
| 41027    | file not exist                       | File does not exist                                          |
| 41028    | text and url size out of limit       | Length of text and url exceeds limit                         |
| 41029    | can't share image and video together | Can't share pictures and videos at the same time             |
| 42001    | invalid credential                   | Invalid credentials                                          |
| 50001    | get access token error               | Get access token error                                       |
| 50002    | share failed                         | Failed to share                                              |
| 50003    | get userinfo failed                  | Failed to get user information                               |
| 50004    | auth failed                          | Authorization failed                                         |
| 50005    | this platform unsupported authorize  | Platform does not support authorization                      |
| 50006    | Invalid or expired token             | Invalid or expired token                                     |
| 50007    | Unable to verify your credentials    | Unable to verify your credentials                            |
| 50008    | Internal error                       | Unknown internal error occurred                              |
| 50009    | Status is a duplicate                | Content of this status has been released by verified account |
