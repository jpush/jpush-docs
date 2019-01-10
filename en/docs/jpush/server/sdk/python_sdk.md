# JPush API Python Client

[Github Source Code](https://github.com/jpush/jpush-api-python-client)

## Overview
This is a Python version development package for the JPush REST API. It is provided by JPush officially and generally supports the latest API features.
Corresponding REST API documentation: https://docs.jiguang.cn/jpush/server/push/server_overview/

## Compatible Version

* Python 2.7
* Python 3

## Environment Configuration

Pip Method:：

```
sudo pip install jpush
```

Easy_install Method：

```
sudo easy_install jpush
```

Source Code Method：

```
sudo python setup.py install
```

## Sample Code
> Sample code is in the examples folder of jpush-api-python-client, [click to view all examples](https://github.com/jpush/jpush-api-python-client/tree/master/examples).

> The following fragment comes from the file in the project code: example_all.py in the examples/push_examples directory of jpush-api-python-client

> This sample demonstrates message push, log settings, and exception handling.

```python
_jpush = jpush.JPush(app_key, master_secret)
push = _jpush.create_push()
# if you set the logging level to "DEBUG",it will show the debug logging.
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn error")
except common.JPushFailure:
    print ("JPushFailure")
except:
    print ("Exception")
```

## Log Description

The default logging level is WARNING , which is set to DEBUG in order to facilitate debugging. The setting method is:

```python
_jpush.set_logging("DEBUG")
```

## Exception Description

* Unauthorized
    * AppKey, Master Secret error. Must correct if the verification fails
* APIConnectionException
    * Include incorrect information: timeouts, no network, etc.
* JPushFailure
    * The request is wrong. Please refer to the business return code.

## HTTP Status Code

Reference document:：http://docs.jiguang.cn/jpush/server/push/http_status_code/
Push v3 API Status Code  Reference document：http://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/　
Report API Status Code  Reference Document：http://docs.jiguang.cn/jpush/server/push/rest_api_v3_report/
Device API Status Code  Reference Document：http://docs.jiguang.cn/jpush/server/push/rest_api_v3_device/
Push Schedule API Status Code  Reference Document：http://docs.jiguang.cn/jpush/server/push/rest_api_push_schedule/　

[Release page](https://github.com/jpush/jpush-api-python-client/releases) has a detailed version for record releasing and downloading.
