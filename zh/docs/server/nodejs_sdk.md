<h1>JPush API client library for Node.js</h1>

###概述

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>详细API介绍文档地址   <a href="https://github.com/jpush/jpush-api-nodejs-client/blob/master/doc/api.md">NodeJS API DOC</a></p>
</div>

<br>

本SDK提供JPush服务端接口的Node封装，与 JPush Rest API 组件通信。使用时引用该模块即可，可参考附带Demo学习使用方法。

[REST API 文档](../server/rest_api_v3_push/)


版本更新：[Release页面](../../resources/#sdk_1)。下载更新请到这里。

###Install

```
npm install jpush-sdk
#or
{
    "dependencies": {
        "jpush-sdk": "*"
    }
}
```

### Example

#### Quick start

此Demo展示如何使用Node lib向所有用户推送通知。

```
var JPush = require("../lib/JPush/JPush.js");
var client = JPush.buildClient('your appKey', 'your masterSecret');

//easy push
client.push().setPlatform(JPush.ALL)
    .setAudience(JPush.ALL)
    .setNotification('Hi, JPush', JPush.ios('ios alert', 'happy.caf', 5))
    .send(function(err, res) {
        if (err) {
            console.log(err.message);
        } else {
            console.log('Sendno: ' + res.sendno);
            console.log('Msg_id: ' + res.msg_id);
        }
    });
```

#### Expert mode(高级版)

```
client.push().setPlatform('ios', 'android')
    .setAudience(JPush.tag('555', '666'), JPush.alias('666,777'))
    .setNotification('Hi, JPush', JPush.ios('ios alert'), JPush.android('android alert', null, 1))
    .setMessage('msg content')
    .setOptions(null, 60)
    .send(function(err, res) {
        if (err) {
            console.log(err.message);
        } else {
            console.log('Sendno: ' + res.sendno);
            console.log('Msg_id: ' + res.msg_id);
        }
    });
```


 关于Payload对象的方法，参考 [详细API文档](https://github.com/jpush/jpush-api-nodejs-client/blob/master/doc/api.md)

#### 获取统计信息

本Node lib简易封装获取统计信息的接口，传入推送API返回的 msg_id 列表，多个 msg_id 用逗号隔开，最多支持100个msg_id。
更多详细要求，请参考 [Report API 文档](../server/rest_api_v3_report/)

```
var JPush = require("../lib/JPush/JPush.js");
var client = JPush.buildClient('your appKey', 'your masterSecret');

client.getReportReceiveds('746522674,344076897', function(err, res) {
    if (err) {
        console.log(err.message);
    } else {
        for (var i=0; i<res.length; i++) {
            console.log(res[i].android_received);
            console.log(res[i].ios_apns_sent);
            console.log(res[i].msg_id);
            console.log('------------');
        }
    }
});
```

####单元测试

在程序根目录下执行

```
mocha test
``` 