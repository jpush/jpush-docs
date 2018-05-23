# Jmessage-wxapplet-sdk Integration Guide

This article shows how to integrate JMessage in an applet. Jmessage-wxapplet-sdk is developed by JMessage specifically for adapting applet applications. Its functionality basically covers all the features provided by the  Web SDK .

## SDK Download

#### jmessage-wxapplet-sdk v1.4.0

Update Time

- 2018-01-26

Change Log

##### NewFeature:

- Add group administrator roles
- Add the function to dissolve group and transfer group owner
- Add the function to obtain transparent transmission of messages between devices and logging devices history.
- Add the function to get all public groups under appkey

Upgrade Prompt

- Recommend to upgrade!

Upgrade Guide

- Replace the old version of sdk with the latest jmessage-wxapplet-sdk-1.4.0.min.js
Click to download：[ jmessage-wxapplet-sdk-1.4.0 ](https://www.jiguang.cn/downloads/server_sdk/im/wxapplet)



## Project Configuration

Legal domain name of socket：wss://ws.im.jiguang.cn

Legal domain name of uploadFile：https://sdk.im.jiguang.cn

Legal domain name of downloadFile：https://dl.im.jiguang.cn/

## Usage

1. Download jmessage-wxapplet-sdk-.js and move to the libs directory

2. Introduce in app.js:


```
var JMessage=require('./libs/jmessage-wxapplet-sdk-<version>.js')
```

Create JMessage object

```
var jim = new JMessage({
       // debug : true
    });
```

Initialize the connection

```
 jim.init({
            "appkey"    : "<appkey>",
            "random_str": "<random_str>",
            "signature" : "<signature>",
            "timestamp" : "<timestamp>"
        }).onSuccess(function(data) {
          //TODO
        }).onFail(function(data) {
          //TODO
        });  
```

All api operations are similar to the Web SDK and can directly refer to the [WEB SDK API](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/)

## Other Instructions

#### Applet SDK Interface for Video Sending 

```
//单聊发送视频示例,群聊、聊天室类似
//先通过小程序API获取视频资源
wx.chooseVideo({
         sourceType: ['album', 'camera'],
         camera: 'back',
         success: function (res) {
                       //sendGroupVedio(),sendChatroomVedio()类似
                       jim.sendSingleVedio({
                          'target_username' : '<target_username>',
   			              'target_nickname' : '<target_nickname>',
   		                           'appkey' : '<appkey>',
                                     'file' : res.tempFilePath
                              }).onSuccess(function(data,msg) {
                                 //TODO
                              }).onFail(function(data) {
                                 //TODO
                               });
                    }
             })
```

#### Interface for Picture Sending (single chats, group chats and chat rooms) is different from WEB SDK API

```
//先通过小程序API获取图片
wx.chooseImage({
          count: 1, //
          sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
        sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
          success: function (res) {
              var tempFilePaths = res.tempFilePaths[0]; //获取成功，读取文件路径
                jim.sendSinglePic({
                    'target_username' : '<target_username>',
            'target_nickname' : '<target_nickname>',
                      'appkey' : '<appkey>',
                              'image' : tempFilePaths //设置图片参数
                    }).onSuccess(function(data,msg) {
                        //TODO
                    }).onFail(function(data) {
                        //TODO
                      });
          }
    })
```



