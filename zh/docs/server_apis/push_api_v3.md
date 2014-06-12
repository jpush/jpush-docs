# Push API v3


### 推送

#### 功能说明

向某单个设备或者某设备列表推送一条通知、或者消息。

推送的内容只能是 JSON 表示的一个推送对象。

调用地址：  
POST https://api.jpush.cn/v3/push

#### 请求示例

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d  '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush!"}}'
 
> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

#### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"sendno":"18","msg_id":"1828256757"}
```

### 调用验证

HTTP Header（头）里加一个字段（Key/Value对）：

    Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)

即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

### 推送对象

一个推送对象，以 JSON 格式表达，表示一条推送相关的所有信息，最多包含以下五个方面：

| 关键字 |  |  含义 |
| --------- | - | ------- |
| platform | 必填 | 推送平台设置 |
| audience | 必填 | 推送设备指定 |
| notification | 可选 | 通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存 |
| message | 可选 | 消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存 |
| options | 可选  | 推送参数 |


```
{
   "platform": "all",
   "audience" : {
      "tag" : ["深圳", "北京"]
   },
   "notification" : {
      "alert" : "Hi, JPush!",
      "android" : {}, 
      "ios" : {
         "extras" : { "newsid" : 321}
      }
   },
   "options" : {
      "time_to_live" : 60
   }
}
```

#### platform 

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios", "winphone"。

推送到所有平台：

    { "platform" : "all" }

指定特定推送平台：

    { "platform" : ["android", "winphone"] }

#### audience

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册ID、分群、广播等。

##### all

如果要发广播（全部设备），则直接填写 “all”。

##### 推送目标

广播外的设备选择方式，有如下几种：

| 关键字 |  | 含义 | 值类型 | 说明 |  
| --------  | - | ------- | -------- | ------- |  
| tag | JSON Array | 标签 | 数组。多个标签之间是 OR 的关系，即取并集。 | 用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。 |
| tag_and | JSON Array | 标签AND | 数组。多个标签之间是 AND 关系，即取交集。 | 注册与 tag 区分。一次推送最多 20 个。 |
| alias | JSON Array | 别名	 | 数组。多个别名之间是 OR 关系，即取并集。 | 用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。  |
| registration_id | JSON Array | 注册ID | 数组。多个注册ID之间是 OR 关系，即取并集。	 | 设备标识。一次推送最多 1000 个。  |

每种类型的值都是数组（Array），数组里多个值之间隐含的关系是是 OR，即取并集。但 tag_and 不同，其数组里多个值之间是 AND 关系，即取交集。

4 种类型至少需要有其一。如果值数组长度为 0，表示该类型不存在。

这几种类型可以并存。并存时多项的隐含关系是 AND，即取交集。

##### 示例

推送给全部（广播）：

```
{
   "platform": "all",
   "audience" : "all",
   "notification" : {
      "alert" : "Hi, JPush!",
   }
}
```

推送给多个标签（只要在任何一个标签范围内都满足）：在深圳、广州、或者北京

```
{
    "audience" : {
        "tag" : [ "深圳", "广州", "北京" ]
    }
}
```

推送给多个标签（需要同时在多个标签范围内）：在深圳并且是“女”

```
{
    "audience" : {
        "tag_and" : [ "深圳", "女" ]
    }
}
```

推送给多个别名：

```
{
    "audience" : {
        "alias" : [ "4314", "892", "4531" ]
    }
}
```

推送给多个注册ID：

```
{
    "audience" : {
        "registration_id" : [ "4312kjklfds2", "8914afd2", "45fdsa31" ]
    }
}
```

可同时推送指定多类推送目标：在深圳或者广州，并且是 ”女“ “会员”

```
{
    "audience" : {
        "tag" : [ "深圳", "广州" ]
        "tag_and" : [ “女”, "会员“ ]
    }
}
```


#### notification

“通知”对象，是一条推送的实体内容对象之一（另一个是“消息”），是会作为“通知”推送到客户端的。

其下属属性包含 4 种，3 个平台属性，以及一个 "alert" 属性。

##### alert

通知的内容在各个平台上，都可能只有这一个最基本的属性 "alert"。

这个位置的 "alert" 属性（直接在 notification 对象下），是一个快捷定义，各平台的 alert 信息如果都一样，则可不定义。如果各平台有定义，则覆盖这里的定义。

```
{
    "notification" : {
        "alert" : "Hello, JPush!"
    }
}
```

上面定义的 notification 对象，将被推送到 "platform" 指定的多个平台，并且其通知 alert 信息都一样。

##### android

Android 平台上的通知。

被 JPush SDK 按照一定的通知栏样式展示。

支持的字段有：

| 关键字 | | 含义 | 说明 |
| --------- | - | ----- | ------ |
| alert | string | 必填 | 通知内容 | 这里指定了，则会覆盖上级统一指定的 alert 信息；内容可以为空字符串，则表示不展示到通知栏。 |
| title | string | 可选 | 通知标题 | 如果指定了，则通知里原来展示 App名称的地方，将展示成这个字段。 | 
| builder_id | int | 可选 | 通知栏样式ID | Android SDK 可设置通知栏样式，这里根据样式 ID 来指定该使用哪套样式。 |
| extras | JSON Array | 可选 | 扩展字段 | 这里自定义 JSON 格式的 Key/Value 信息，以供业务使用。 |

```
{
    "notification" : {
        "android" : {
             "alert" : "hello, JPush!", 
             "title" : "JPush test", 
             "builder_id" : 3, 
             "extras" : {
                  "news_id" : 134, 
                  "my_key" : "a value"
             }
        }
    }
}
```




### 调用返回

### 参考

