<h1>JPush API Python Client</h1>
JPush's officially supported Python client library for accessing JPush APIs.

版本更新：[Release页面](https://github.com/jpush/jpush-api-python-client/releases)。下载更新请到这里。

### Dependencies

You need to install requests, the python http library, to use jpush python client.

```
$ sudo pip install requests
```

### Installation

To install jpush-api-python-client, simply:

```
$ sudo pip install jpush
```
or alternatively install via easy_install:

```
$ sudo easy_install jpush
```
or from source:

```
$ sudo python setup.py install
```
### Examples

Details refer to [examples](https://github.com/jpush/jpush-api-python-client/blob/master/examples)

#### Simple iOS Push

```
import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
push = _jpush.create_push()
push.audience = jpush.all_
ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1':'v1'})
push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
push.options = {"time_to_live":86400, "sendno":12345,"apns_production":True}
push.platform = jpush.platform("ios")
push.send()
```


#### Get taglist

```
import jpush as jpush
from conf import app_key, master_secret
_jpush = jpush.JPush(app_key, master_secret)
device = _jpush.create_device()
device.get_taglist()
```

### Thanks to

[crystal-wei](https://github.com/crystal-wei) for reporting the jpush-api-python-client issues;

