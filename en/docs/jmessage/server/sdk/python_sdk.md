# JMessage API Python SDK

[Github](https://github.com/jpush/jmessage-api-python-client)

## Introduction

This is the Python development package for the JMessage REST API, which is provided by the JPush officially and generally supports the latest API features.

Corresponding REST API documentation：[https://docs.jiguang.cn/jmessage/server/rest_api_im/](https://docs.jiguang.cn/jmessage/server/rest_api_im/)

## Support

Python 2.7

## Installation

Install Pip

```
pip install jmessage
```

Run after downloading

```
python setup.py install
```

## Samples

> The following code is taken from example/users/regist_user.py under the project directory

```python
from jmessage import users
from jmessage import common
from conf import *
import json
jmessage=common.JMessage(app_key,master_secret)
users=jmessage.create_users()
user= [users.build_user("user","password")]
response=users.regist_user(user)
print (response.content)
```

> The following code is taken from the example/messages/send_message.py under the project directory

```python
from jmessage import users
from jmessage import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)
messages=jmessage.create_messages()
message=messages.build_message(1,"single","admin","text",
                                "xiaohuihui","admin","Hello, JMessage!")
response=messages.send_messages(message)
print (response.content)
```

> The following code is taken from example/groups/create_groups.py under the project directory

```python
from jmessage import users
from jmessage import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)
groups=jmessage.create_groups()
group=groups.build_group(owner_username="dev_fang", name="jpush",
                          members_username=["xiaohuihui"], desc="jpush group")
response=groups.create_group(group)
print (response.content)
```