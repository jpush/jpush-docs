# Rich Push Development Guide

### Overview

Rich Push, which refers to rich media push, allows developers to push Web pages, pictures, sounds, and more rich content other than plain text.

Application developers can use "rich text push" to push richer content such as news, coupons, and event information. They can also use "rich media file push" to extend existing IM communication capabilities.

From the perspective of end-user experience, JPush fully takes into the characteristics of the domestic network environment. The Rich Push feature has been specially designed: 1) When preparing resources on the Portal, all are saved on the JPush server; 2) JPush SDK display pre-loaded media files before pushing. This ensures that a rich text push page is always visible and complete.

### Function Description

It is divided into two parts: information flow template push and URL rich media link push. For details, please refer to the document [Rich Media Push](../guideline/intro/#rich_push)

#### Flow template push

* Push Web page (rich text)
* Push tool on Portal to quickly create rich text pages
* Rich text pushed to the client as a notification
* Client click notification to automatically display the rich text page

#### URL push

* Push the URL of the page, click the notification bar message, and jump to the page specified by the URL.

### Development Steps

#### Download JPush Android SDK which supports Rich Push 

Integrate into Android App based on related documents.

### SDK Support

Rich Push needs to respond to SDK version to support
* JPush Android SDK 1.8.0 and above
* JPush iOS SDK (not supported yet)
