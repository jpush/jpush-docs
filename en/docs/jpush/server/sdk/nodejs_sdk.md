# JPush API client library for Node.js

[Github Source Code](https://github.com/jpush/jpush-api-nodejs-client)


This SDK provides the Node encapsulation of the JPush server interface and communicates with the JPush Rest API component. Cite the module when it is used, and refer to Demo usage.

[REST API Documentation](http://docs.jiguang.cn/jpush/server/push/server_overview/)

[NodeJS API Documentation](https://github.com/jpush/jpush-api-nodejs-client/blob/master/doc/api.md)

## Install

```js
npm install jpush-sdk

#or
{
    "dependencies": {
        "jpush-sdk": "*"
    }
}
```

## Example

### Quick Start

This Demo shows how to use the Node lib to push notifications to all users.

```js
var JPush = require("../lib/JPush/JPush.js")
var client = JPush.buildClient('your appKey', 'your masterSecret')

//easy push
client.push().setPlatform(JPush.ALL)
    .setAudience(JPush.ALL)
    .setNotification('Hi, JPush', JPush.ios('ios alert', 'happy', 5))
    .send(function(err, res) {
        if (err) {
            console.log(err.message)
        } else {
            console.log('Sendno: ' + res.sendno)
            console.log('Msg_id: ' + res.msg_id)
        }
    });
```

### Expert Mode (Advanced)

```js
client.push().setPlatform('ios', 'android')
    .setAudience(JPush.tag('555', '666'), JPush.alias('666,777'))
    .setNotification('Hi, JPush', JPush.ios('ios alert'), JPush.android('android alert', null, 1))
    .setMessage('msg content')
    .setOptions(null, 60)
    .send(function(err, res) {
        if (err) {
            console.log(err.message)
        } else {
            console.log('Sendno: ' + res.sendno)
            console.log('Msg_id: ' + res.msg_id)
        }
    });
```

For the method of the Payload object, refer to [the detailed API documentation](https://github.com/jpush/jpush-api-nodejs-client/blob/master/doc/api.md).

## Get Statistics

The Node lib simply encapsulates the interface for obtaining statistics and passes in the msg_id list returned by the push API. Multiple msg_ids are separated by commas, and up to 100 msg_ids are supported. For more detailed requirements, please refer to the [Report API documentation](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_report/).

```js
var JPush = require("../lib/JPush/JPush.js");
var client = JPush.buildClient('your appKey', 'your masterSecret');

client.getReportReceiveds('746522674,344076897', function(err, res) {
    if (err) {
        console.log(err.message)
    } else {
        for (var i = 0; i < res.length; i++) {
            console.log(res[i].android_received)
            console.log(res[i].ios_apns_sent)
            console.log(res[i].msg_id)
        }
    }
});
```

## Close Log

```js
// 在构建 JPushClient 对象的时候, 指定 isDebug 参数。
var client = JPush.buildClient({
    appKey:'47a3ddda34b2602fa9e17c01',
    masterSecret:'d94f733358cca97b18b2cb98',
    isDebug:false
});
// or
var client = JPush.buildClient('47a3ddda34b2602fa9e17c01', 'd94f733358cca97b18b2cb98', null, false);
```

> At present, the debug module is used to control the log output. To view the related log information of JPush, please configure the DEBUG environment variable 'jpush' first.