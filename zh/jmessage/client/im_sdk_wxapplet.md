# jmessage-wxapplet-sdk 集成指南

本文说明如何在小程序中集成 JMessage。jmessage-wxapplet-sdk 是 JMessage 专门为适配小程序应用而开发的，其功能基本涵盖所有[ WEB SDK ](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/)所提供的功能

## SDK下载

#### jmessage-wxapplet-sdk v1.2.0

更新时间

+ 2017-10-19

Change Log

##### NewFeature:

+ 事件同步
+ 自定义通知栏
+ 消息转发
+ 支持消息透传
+ 支持群组头像
+ 支持多端同时在线
+ 消息已读回执
+ 会话、用户信息支持扩展字段
+ 注册支持扩展字段
+ 支持会话未读数获取、重置会话未读数

升级提示

+ 升级！

升级指南

+ 用最新的 jmessage-wxapplet-sdk-1.2.0.min.js 替换掉老版本的 sdk

点击下载：[ jmessage-wxapplet-sdk-1.2.0 ](https://sdkfiledl.jiguang.cn/src/jmessage-wxapplet-sdk-1.2.0.zip)



## 项目配置

socket 合法域名：wss://ws.im.jiguang.cn

uploadFile 合法域名：https://sdk.im.jiguang.cn

downloadFile 合法域名：https://dl.im.jiguang.cn/


## 使用

1.下载 jmessage-wxapplet-sdk-<version>.js,移动到 libs 目录下

2.在 app.js 中引入：

```
var JMessage=require('./libs/jmessage-wxapplet-sdk-<version>.js')
```

新建 JMessage 对象：

```
var jim = new JMessage({
       // debug : true
    });
```

初始化连接：

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

所有 api 操作跟 WEB SDK 类似，可以直接参考[ WEB SDK API](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/)

## 其他说明

1. 小程序不支持文件传输，所以单聊以及群聊文件发送相关 api 不可用

2. 发送图片(单聊和群聊)接口跟 WEB SDK API 有所差异

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
   ​

