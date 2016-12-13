# JMessage API Python SDK

## 简介
这是 JMessage REST API 的 Python 封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。

对应的 REST API 文档：http://docs.jiguang.cn/server/rest_api_im/

## 支持

Python 2.7

## 安装

下载之后运行
```
python setup.py install 
```

(稍后支持 pip 安装)

## 样例
>以下代码截取自项目目录下的 example/users/regist_user.py

```
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

>以下代码截取自项目目录下的 example/messages/send_message.py

```
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

>以下代码截取自项目目录下的 example/groups/create_groups.py

```

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
