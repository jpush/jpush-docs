# jmessage-wxapplet-sdk 集成指南

本文说明如何在小程序中集成 JMessage。jmessage-wxapplet-sdk 是 JMessage 专门为适配小程序应用而开发的，其功能基本涵盖所有[ WEB SDK ](https://docs.jiguang.cn/jmessage/client/im_sdk_js_v2/)所提供的功能

## SDK下载

#### jmessage-wxapplet-sdk v1.1.1

更新时间

+ 2017-6-29

Change Log

##### BugFix:

+ 真机上报Blob对象undefined错误
+ 性能优化

升级提示

+ 升级！

升级指南

+ 用最新的 jmessage-wxapplet-sdk-1.1.1.min.js 替换掉老版本的 sdk

点击下载：[ jmessage-wxapplet-sdk-1.1.1 ](https://sdkfiledl.jiguang.cn/jmessage-wxapplet-sdk-1.1.1.zip)



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

