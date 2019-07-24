# Push API <small>v3</small>


<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>这是 Push API 最近的版本。</p>
<p>相比于 API v2 版本，v3 版本的改进为：</p>
<ul style="margin-bottom: 0;">
<li>完全基于 https，不再提供 http 访问；</li>
<li>使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；</li>
<li>推送内容完全使用 JSON 的格式；</li>
<li>支持的功能有所改进：支持多 tag 的与或操作；可单独发送通知或者自定义消息，也可同时推送通知与自定义消息；windows phone 目前只有通知。</li>
</ul>
</div>


## 推送概述

### 功能说明

向某单个设备或者某设备列表推送一条通知、或者消息。  
推送的内容只能是 JSON 表示的一个推送对象。

### 调用地址 
https://api.jpush.cn/v3/push

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">

<p>如果创建的极光应用分配的北京机房，并且 API 调用方的服务器也位于北京，则比较适合调用极光北京机房的 API，可以提升一定的响应速度。</p>
<p>通过极光 Web 控制台 “应用设置” -> "应用信息" 中可以看到应用所在机房。如果应用所在地为北京机房，同时会给出各 API 的调用地址。</p>

<p>北京机房 Push API 调用地址： https://bjapi.push.jiguang.cn/v3/push </p>
<p>详细对应关系见 “应用信息” 中 “服务器所在地” 后的信息。</p>

</div>

### 请求示例

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush !","android":{"extras":{"android-key1":"android-value1"}},"ios":{"sound":"sound.caf","badge":"+1","extras":{"ios-key1":"ios-value1"}}}}'

> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"sendno":"18","msg_id":"1828256757"}
```



## 调用验证

HTTP Header（头）里加一个字段（Key/Value 对）：

	Authorization: Basic base64_auth_string

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)  
即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。






## 推送对象

一个推送对象，以 JSON 格式表达，表示一条推送相关的所有信息。

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th>关键字</th>
			<th >选项</th>
			<th >含义</th>
		</tr>
		<tr >
			<td>platform</td>
			<td>必填</td>
			<td>推送平台设置</td>
		</tr>
		<tr >
			<td>audience</td>
			<td>必填</td>
			<td>推送设备指定</td>
		</tr>
		<tr >
			<td>notification</td>
			<td>可选</td>
			<td>通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存</td>
		</tr>
		<tr >
			<td>message</td>
			<td>可选</td>
			<td>消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存 </td>
		</tr>
		<tr>
			<td>sms_message</td>
			<td>可选</td>
			<td>短信渠道补充送达内容体</td>
		</tr>
		<tr >
			<td>options</td>
			<td>可选</td>
			<td>推送参数 </td>
		</tr>
		<tr >
			<td>cid</td>
			<td>可选</td>
			<td>用于防止 api 调用端重试造成服务端的重复推送而定义的一个标识符。</td>
		</tr>
	</table>
</div>

### 示例与说明

```
{
    "cid": "8103a4c628a0b98974ec1949-711261d4-5f17-4d2f-a855-5e5a8909b26e",
    "platform": "all",
    "audience": {
        "tag": [
            "深圳",
            "北京"
        ]
    },
    "notification": {
        "android": {
            "alert": "Hi, JPush!",
            "title": "Send to Android",
            "builder_id": 1,
            "large_icon": "http://www.jiguang.cn/largeIcon.jpg",
            "intent": {
                "url": "intent:#Intent;component=com.jiguang.push/com.example.jpushdemo.SettingActivity;end",
            },
            "extras": {
                "newsid": 321
            }
        },
        "ios": {
            "alert": "Hi, JPush!",
            "sound": "default",
            "badge": "+1",
            "thread-id": "default"
            "extras": {
                "newsid": 321
            }
        }
    },
    "message": {
        "msg_content": "Hi,JPush",
        "content_type": "text",
        "title": "msg",
        "extras": {
            "key": "value"
        }
    },
    "sms_message":{
       "temp_id":1250,
       "temp_para":{
       		"code":"123456"
       },
    	"delay_time":3600,
    	"active_filter":false
	},
    "options": {
        "time_to_live": 60,
        "apns_production": false,
        "apns_collapse_id":"jiguang_test_201706011100"
    }
}

```

## platform：推送平台

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios", "winphone"。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>如果目标平台为 iOS 平台，推送 Notification 时需要在 options 中通过 apns_production 字段来设定推送环境。True 表示推送生产环境，False 表示要推送开发环境； 如果不指定则为推送生产环境；一次只能推送给一个环境。</p>
</div>
<br>

推送到所有平台：

	{ "platform" : "all" }

指定特定推送平台：

	{ "platform" : ["android", "ios"] }

## audience：推送目标

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册 ID、分群、广播等。

### all

如果要发广播（全部设备），则直接填写 “all”。

### 推送目标

广播外的设备选择方式，有如下几种：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr bgcolor="#D3D3D3">
			<th >关键字</th>
			<th >类型</th>
			<th >含义</th>
			<th >说明</th>
			<th >备注</th>
		</tr>
		<tr >
			<td>tag</td>
			<td>JSON Array</td>
			<td>标签OR</td>
			<td>数组。多个标签之间是 OR 的关系，即取并集。 </td>
			<td>用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。<ul style="margin-bottom: 0;"><li>有效的 tag 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|￥。</li><li>限制：每一个 tag 的长度限制为 40 字节。（判断长度需采用 UTF-8 编码）</li></td>
		</tr>
		<tr >
			<td>tag_and</td>
			<td>JSON Array</td>
			<td>标签AND</td>
			<td>数组。多个标签之间是 AND 关系，即取交集。</td>
			<td>注意与 tag 区分。一次推送最多 20 个。</td>
		</tr>
		<tr >
			<td>tag_not</td>
			<td>JSON Array</td>
			<td>标签NOT</td>
			<td>数组。多个标签之间，先取多标签的并集，再对该结果取补集。</td>
			<td>一次推送最多 20 个。</td>
		</tr>
		<tr >
			<td>alias</td>
			<td>JSON Array</td>
			<td>别名</td>
			<td>数组。多个别名之间是 OR 关系，即取并集。</td>
			<td>用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。<ul style="margin-bottom: 0;"><li>有效的 alias 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|￥。</li><li>限制：每一个 alias 的长度限制为 40 字节。（判断长度需采用 UTF-8 编码）</li></td>
		</tr>
		<tr >
			<td>registration_id</td>
			<td>JSON Array</td>
			<td>注册ID</td>
			<td>数组。多个注册 ID 之间是 OR 关系，即取并集。</td>
			<td>设备标识。一次推送最多 1000 个。客户端集成 SDK 后可获取到该值。</td>
		</tr>
		
		<tr >
			<td>segment</td>
			<td>JSON Array</td>
			<td>用户分群 ID </td>
			<td>在页面创建的用户分群的 ID。定义为数组，但目前限制一次只能推送一个。</td>
			<td>目前限制是一次只能推送一个。</td>
		</tr>
		
		<tr>
			<td>abtest</td>
			<td>JSON Array</td>
			<td>A/B Test ID</td>
			<td>在页面创建的 A/B 测试的 ID。定义为数组，但目前限制是一次只能推送一个。</td>
			<td>目前限制一次只能推送一个。</td>
		</tr>
	</table>
</div>


<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>以上几种类型至少需要有其一。如果值数组长度为 0，表示该类型不存在。</p>
<p>这几种类型可以并存，多项的隐含关系是 AND，即取几种类型结果的交集。</p>
<p>例如：

"audience" : {
        "tag" : [ "tag1", "tag2" ],
        "tag\_and" : [ "tag3", "tag4"],
        "tag\_not" : [ "tag5", "tag6"]
    }

先计算 "tag" 字段的结果 ***`tag1或tag2=A`***;

再计算 "tag\_and" 字段的结果 ***`tag3且tag4=B`***;

再计算 "tag\_not" 字段的结果 ***`非(tag5或tag6)=C`*** 

"audience" 的最终结果为  ***`A且B且C`*** 。 </p>
</div>
<br>


### 示例

+ 推送给全部（广播）：

```
{
   "platform": "all",
   "audience" : "all",
   "notification" : {
      "alert" : "Hi, JPush!",
      "android" : {}, 
      "ios" : {
         "extras" : { "newsid" : 321}
      }
   }
}
```

+ 推送给多个标签（只要在任何一个标签范围内都满足）：在深圳、广州、或者北京

```
{
	"audience" : {
		"tag" : [ "深圳", "广州", "北京" ]
	}
}
```

+ 推送给多个标签（需要同时在多个标签范围内）：在深圳并且是“女”

```
{
	"audience" : {
		"tag_and" : [ "深圳", "女" ]
	}
}
```

+ 推送给多个别名：

```
{
	"audience" : {
		"alias" : [ "4314", "892", "4531" ]
	}
}
```

+ 推送给多个注册 ID：

```
{
	"audience" : {
		"registration_id" : [ "4312kjklfds2", "8914afd2", "45fdsa31" ]
	}
}
```

+ 可同时推送指定多类推送目标：在深圳或者广州，并且是 “女” “会员”

```
{
	"audience" : {
		"tag" : [ "深圳", "广州" ],
		"tag_and" : [ "女", "会员"]
	}
}
```


## notification：通知

“通知”对象，是一条推送的实体内容对象之一（另一个是“消息”），是会作为“通知”推送到客户端的。  
其下属属性包含 4 种，3 个平台属性，以及一个 "alert" 属性。

### alert

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

### android

Android 平台上的通知，JPush SDK 按照一定的通知栏样式展示。

支持的字段有：


<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%" >选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td>通知内容</td>
			<td>这里指定了，则会覆盖上级统一指定的 alert 信息；内容可以为空字符串，则表示不展示到通知栏。</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>通知标题</td>
			<td>如果指定了，则通知里原来展示 App 名称的地方，将展示成这个字段。</td>
		</tr>
		<tr >
			<td>builder_id</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏样式 ID</td>
			<td>Android SDK 可<a href="https://docs.jiguang.cn/jpush/client/Android/android_api/#api_8">设置通知栏样式</a>，这里根据样式 ID 来指定该使用哪套样式，android 8.0 开始建议采用<a href="https://docs.jiguang.cn/jpush/client/Android/android_api/#notificationchannel">NotificationChannel配置</a>。</td>
		</tr>
		<tr >
			<td>channel_id</td>
			<td>String</td>
			<td>可选</td>
			<td>android通知channel_id</td>
			<td>不超过1000字节，Android 8.0开始可以进行<a href="https://docs.jiguang.cn/jpush/client/Android/android_api/#notificationchannel">NotificationChannel配置</a>，这里根据channel ID 来指定通知栏展示效果。</td>
		</tr>
		<tr >
			<td>priority</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏展示优先级</td>
			<td>默认为 0，范围为 -2～2。</td>
		</tr>
		<tr >
			<td>category</td>
			<td>string</td>
			<td>可选</td>
			<td>通知栏条目过滤或排序</td>
			<td>完全依赖 rom 厂商对 category 的处理策略</td>
		</tr>
		<tr >
			<td>style</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏样式类型</td>
			<td>默认为 0，还有 1，2，3 可选，用来指定选择哪种通知栏样式，其他值无效。有三种可选分别为 bigText=1，Inbox=2，bigPicture=3。</td>
		</tr>
		<tr >
			<td>alert_type</td>
			<td>int</td>
			<td>可选</td>
			<td>通知提醒方式</td>
			<td>可选范围为 -1～7 ，对应 Notification.DEFAULT_ALL = -1 或者 Notification.DEFAULT_SOUND = 1, Notification.DEFAULT_VIBRATE = 2, Notification.DEFAULT_LIGHTS = 4 的任意 “or” 组合。默认按照 -1 处理。  </td>
		</tr>
		<tr >
			<td>big_text</td>
			<td>string</td>
			<td>可选</td>
			<td>大文本通知栏样式</td>
			<td>当 style = 1 时可用，内容会被通知栏以大文本的形式展示出来。支持 api 16 以上的 rom。</td>
		</tr>
		<tr >
			<td>inbox</td>
			<td>JSONObject</td>
			<td>可选</td>
			<td>文本条目通知栏样式</td>
			<td>当 style = 2 时可用， json 的每个 key 对应的 value 会被当作文本条目逐条展示。支持 api 16 以上的 rom。</td>
		</tr>
		<tr >
			<td>big_pic_path</td>
			<td>string</td>
			<td>可选</td>
			<td>大图片通知栏样式</td>
			<td>当 style = 3 时可用，可以是网络图片 url，或本地图片的 path，目前支持 .jpg 和 .png 后缀的图片。图片内容会被通知栏以大图片的形式展示出来。如果是 http／https 的 url，会自动下载；如果要指定开发者准备的本地图片就填 sdcard 的相对路径。支持 api 16 以上的 rom。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>扩展字段</td>
			<td>这里自定义 JSON 格式的 Key / Value 信息，以供业务使用。</td>
		</tr>
		<tr >
			<td>large_icon</td>
			<td>string</td>
			<td>可选</td>
			<td>通知栏大图标</td>
			<td>图标路径可以是以http或https开头的网络图片，如：http:jiguang.cn/logo.png ,图标大小不超过 30 k;
也可以是位于drawable资源文件夹的图标路径，如：R.drawable.lg_icon；<br/>如果有此字段值，推送一定走极光自有通道下发。 </td>
		</tr>
		<tr >
			<td>intent</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>指定跳转页面</td>
			<td>使用 intent 里的 url 指定点击通知栏后跳转的目标页面;<br/>如果有此字段值，推送一定走极光自有通道下发。</td>
		</tr>
	</table>
</div>

<br>

```
{
	"notification" : {
		"android" : {
			 "alert" : "hello, JPush!", 
			 "title" : "JPush test", 
			 "builder_id" : 3, 
			 "style":1  // 1,2,3
			 "alert_type":1 // -1 ~ 7
			 "big_text":"big text content",
			 "inbox":JSONObject,
			 "big_pic_path":"picture url",
			 "priority":0, // -2~2
			 "category":"category str",
			 "large_icon": "http://www.jiguang.cn/largeIcon.jpg",
           "intent": {
                "url": "intent:#Intent;component=com.jiguang.push/com.example.jpushdemo.SettingActivity;end",
            },
			 "extras" : {
				  "news_id" : 134, 
				  "my_key" : "a value"
			 }
		}
	}
}
```

### iOS

iOS 平台上 APNs 通知结构。  
该通知内容会由 JPush 代理发往 Apple APNs 服务器，并在 iOS 设备上在系统通知的方式呈现。  
该通知内容满足 APNs 的规范，支持的字段如下：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th width="20%">含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string或JSON Object</td>
			<td>必填</td>
			<td width="20%">通知内容</td>
			<td>这里指定内容将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。支持字符串形式也支持官方定义的<a href="https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html"> alert payload</a> 结构，在该结构中包含 title 和 subtitle 等官方支持的 key</td>
		</tr>
		<tr >
			<td>sound</td>
			<td>string 或 JSON Object</td>
			<td>可选</td>
			<td width="20%">通知提示声音或警告通知</td>
			<td>普通通知： string类型，如果无此字段，则此消息无声音提示；有此字段，如果找到了指定的声音就播放该声音，否则播放默认声音，如果此字段为空字符串，iOS 7 为默认声音，iOS 8 及以上系统为无声音。说明：JPush 官方 SDK 会默认填充声音字段，提供另外的方法关闭声音，详情查看各 SDK 的源码。<br>
			告警通知： JSON Object ,支持官方定义的<a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification#2990112"> payload</a> 结构，在该结构中包含 critical 、name 和 volume 等官方支持的 key .</td>
		</tr>
		<tr >
			<td>badge</td>
			<td>int</td>
			<td>可选</td>
			<td width="20%">应用角标</td>
			<td>如果不填，表示不改变角标数字，否则把角标数字改为指定的数字；为 0 表示清除。JPush 官方 SDK 会默认填充 badge 值为 "+1",详情参考：<a href="http://blog.jpush.cn/ios_apns_badge_plus/">badge +1</a></td>
		</tr>
		<tr >
			<td>content-available</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">推送唤醒</td>
			<td>推送的时候携带 "content-available":true 说明是 Background Remote Notification，如果不携带此字段则是普通的 Remote Notification。详情参考：<a href="../../../client/iOS/ios_new_fetures/#ios-7-background-remote-notification">Background Remote Notification</a></td>
		</tr>
		<tr >
			<td>mutable-content</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">通知扩展</td>
			<td>推送的时候携带 ”mutable-content":true 说明是支持iOS10的UNNotificationServiceExtension，如果不携带此字段则是普通的 Remote Notification。详情参考：<a href="../../../client/iOS/ios_new_fetures/#ios-10-service-extension">UNNotificationServiceExtension</a></td>
		</tr>
		<tr >
			<td>category</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%"> </td>
			<td>IOS 8 才支持。设置 APNs payload 中的 "category" 字段值</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td width="20%">附加字段</td>
			<td>这里自定义 Key / value 信息，以供业务使用。</td>
		</tr>
		<tr >
			<td>thread-id</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%">通知分组</td>
			<td>ios 的远程通知通过该属性来对通知进行分组，同一个 thread-id 的通知归为一组。</td>
		</tr>
	</table>
</div>


<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>iOS 通知 JPush 要转发给 APNs 服务器。APNs 协议定义通知长度为 2048 字节。</p>
<p>JPush 因为需要重新组包，并且考虑一点安全冗余，要求 "iOS":{ } 及大括号内的总体长度不超过：2000 个字节。JPush 使用 utf-8 编码，所以一个汉字占用 3 个字节长度。</p>
</div>
<br>

**服务端发送消息串**

```
{
	"notification" : {
	     "ios" : {
	             "alert" : "hello, JPush!", 
	             "sound" : "sound.caf", 
	             "badge" : 1, 
	             "extras" : {
	                  "news_id" : 134, 
	                  "my_key" : "a value"
	             }
	       	}
	   }
}				 
```

**客户端收到 apns**

```
{
    "_j_msgid" = 813843507;
    aps =     {
        alert = "hello,JPush!";
        badge = 1;
        sound = "sound.caf";
    };
    "my_key" = "a value";
    "news_id" = 134;
}
```

### winphone

Windows Phone 平台上的通知。  
该通知由 JPush 服务器代理向微软的 MPNs 服务器发送，并在 Windows Phone 客户端的系统通知栏上展示。  
该通知满足 MPNs 的相关规范。当前 JPush 仅支持 toast 类型：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%" >选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td>通知内容</td>
			<td>会填充到 toast 类型 text2 字段上。这里指定了，将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>通知标题</td>
			<td>会填充到 toast 类型 text1 字段上。</td>
		</tr>
		<tr >
			<td>_open_page</td>
			<td>string</td>
			<td>可选</td>
			<td>点击打开的页面名称</td>
			<td>点击打开的页面。会填充到推送信息的 param 字段上，表示由哪个 App 页面打开该通知。可不填，则由默认的首页打开。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>扩展字段</td>
			<td>作为参数附加到上述打开页面的后边。</td>
		</tr>
	</table>
</div>

<br>

```
	{
	    "notification" : {
	        "winphone" : {
	             "alert" : "hello, JPush!", 
	             "title" : "Push Test", 
	             "_open_page" : "/friends.xaml", 
	             "extras" : {
	                  "news_id" : 134, 
	                  "my_key" : "a value"
	             }
	        }
	    }
	}
```


## message：自定义消息

应用内消息。或者称作：自定义消息，透传消息。  
此部分内容不会展示到通知栏上，JPush SDK 收到消息内容后透传给 App。需要 App 自行处理。  
iOS 在推送应用内消息通道（非 APNS）获取此部分内容，即需 App 处于前台。Windows Phone 暂时不支持应用内消息。

消息包含如下字段：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>含义</th>
		</tr>
		<tr >
			<td>msg_content</td>
			<td>string</td>
			<td>必填</td>
			<td>消息内容本身</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>消息标题</td>
		</tr>
		<tr >
			<td>content_type</td>
			<td>string</td>
			<td>可选</td>
			<td>消息内容类型</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>JSON 格式的可选参数</td>
		</tr>
	</table>
</div>


<br>

```
Android 1.6.2 及以下版本 接收 notification 与 message 并存（即本次 api 调用同时推送通知和消息）的离线推送， 只能收到通知部分，message 部分没有透传给 App。

Android 1.6.3 及以上 SDK 版本已做相应调整，能正常接收同时推送通知和消息的离线记录。

iOS 1.7.3 及以上的版本才能正确解析 v3 的 message，但是无法解析 v2 推送通知同时下发的应用内消息。
```

## sms_message：短信补充

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>1. 使用短信业务，会产生额外的运营商费用，具体请咨询商务，联系电话：400-612-5955，商务 QQ：800024881</p>
<p>2. 短信由签名和正文内容两部分组成。应运营商规定，签名和正文内容需审核。参考 <a href="https://docs.jiguang.cn/jsms/guideline/jsms_terminology/">名词解释</a> </p>
<p>3. 签名设置参考 <a href="https://docs.jiguang.cn/jsms/guideline/JSMS_consoleguide/#_9">《控制台操作指南》之签名设置</a> 和 <a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_sign/">短信签名 API</a> 。</p>
<p>4. 自 2018 年 3 月起，短信补充的开发者必须提交正文内容模板，审核通过后即可使用。因此推送时需要填写 temp_id（如果模版有设置参数则需要填写 temp_para）。参考 <a href="https://docs.jiguang.cn/jsms/guideline/JSMS_consoleguide/#_12">《控制台操作指南》之模板设置</a> 和 <a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_templates/">短信模板 API</a> 。</p>
</div>
<br>
sms_message 用于设置短信推送内容以及短信发送的延迟时间。   

开发者需要先把用户的手机号码与设备的 registrationID 匹配。绑定方法：<a href="https://docs.jiguang.cn/jpush/server/push/rest_api_v3_device/#_3">服务端-Device-更新设备</a>; 
<a href="https://docs.jiguang.cn/jpush/client/Android/android_api/#_61">Android API-设置手机号码</a>; <a href="https://docs.jiguang.cn/jpush/client/iOS/ios_api/#_151">iOS API-设置手机号码</a>；

与原有 JSON 业务协议相匹配，消息有如下字段信息：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>说明</th>
		</tr>
		<tr >
			<td>delay_time</td>
			<td>int</td>
			<td>必填</td>
			<td>单位为秒，不能超过 24 小时。设置为 0，表示立即发送短信。该参数仅对 android 和 iOS 平台有效，Winphone 平台则会立即发送短信。</td>
		</tr>
		<tr >
			<td>signid</td>
			<td>int</td>
			<td>选填</td>
			<td>签名ID，该字段为空则使用应用默认签名。</td>
		</tr>
		<tr >
			<td>temp_id</td>
			<td>long</td>
			<td>必填</td>
			<td>短信补充的内容模板 ID。没有填写该字段即表示不使用短信补充功能。</td>
		</tr>
       <tr >
			<td>temp_para</td>
			<td>JSON</td>
			<td>可选</td>
			<td>短信模板中的参数。 </td>
		</tr>
		<tr >
			<td>active_filter</td>
			<td>boolean</td>
			<td>可选</td>
			<td>active_filter 字段用来控制是否对补发短信的用户进行活跃过滤，默认为 true ，做活跃过滤；为 false，则不做活跃过滤； </td>
		</tr>
	</table>
</div>


## options：可选参数

推送可选项。

当前包含如下几个可选项：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>sendno</td>
			<td>int</td>
			<td>可选</td>
			<td>推送序号</td>
			<td>纯粹用来作为 API 调用标识，API 返回时被原样返回，以方便 API 调用方匹配请求与返回。值为 0 表示该 messageid 无 sendno，所以字段取值范围为非 0 的 int.</td>
		</tr>
		<tr >
			<td>time_to_live</td>
			<td>int</td>
			<td>可选</td>
			<td>离线消息保留时长(秒)</td>
			<td>推送当前用户不在线时，为该用户保留多长时间的离线消息，以便其上线时再次推送。默认 86400 （1 天），最长 10 天。设置为 0 表示不保留离线消息，只有推送当前在线的用户可以收到。该字段对 iOS 的 Notification 消息无效。</td>
		</tr>
		<tr >
			<td>override_msg_id</td>
			<td>long</td>
			<td>可选</td>
			<td>要覆盖的消息 ID</td>
			<td>如果当前的推送要覆盖之前的一条推送，这里填写前一条推送的 msg_id 就会产生覆盖效果，即：1）该 msg_id 离线收到的消息是覆盖后的内容；2）即使该 msg_id Android 端用户已经收到，如果通知栏还未清除，则新的消息内容会覆盖之前这条通知；覆盖功能起作用的时限是：1 天。如果在覆盖指定时限内该 msg_id 不存在，则返回 1003 错误，提示不是一次有效的消息覆盖操作，当前的消息不会被推送；该字段仅对 Android 有效。</td>
		</tr>
		<tr >
			<td>apns_production</td>
			<td>boolean</td>
			<td>可选</td>
			<td>APNs 是否生产环境</td>
			<td>True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。但注意，JPush 服务端 SDK 默认设置为推送 “开发环境”。该字段仅对 iOS 的 Notification 有效。</td>
		</tr>
		<tr >
			<td>apns_collapse_id</td>
			<td>string</td>
			<td>可选</td>
			<td>更新 iOS 通知的标识符</td>
			<td> APNs 新通知如果匹配到当前通知中心有相同 apns-collapse-id 字段的通知，则会用新通知内容来更新它，并使其置于通知中心首位。collapse id 长度不可超过 64 bytes。</td>
		</tr>
		<tr >
			<td>big_push_duration</td>
			<td>int</td>
			<td>可选</td>
			<td>定速推送时长(分钟)</td>
			<td>又名缓慢推送，把原本尽可能快的推送速度，降低下来，给定的 n 分钟内，均匀地向这次推送的目标用户推送。最大值为 1400。未设置则不是定速推送。</td>
		</tr>
	</table>
</div>

## cid：推送唯一标识符

### 调用地址
GET https://api.jpush.cn/v3/push/cid[?count=n[&type=xx]]

### 功能说明
cid 是用于防止 api 调用端重试造成服务端的重复推送而定义的一个推送参数。

用户使用一个 cid 推送后，再次使用相同的 cid 进行推送，则会直接返回第一次成功推送的结果，不会再次进行推送。

CID 的有效期为 1 天。CID 的格式为：{appkey}-{uuid}

在使用 cid 之前，必须通过接口获取你的 cid 池。获取时 type=push 或者不传递 type 值。

### 调用示例

**Request Header**
 
```
curl --insecure -X GET -v https://api.jpush.cn/v3/push/cid?count=3 -H "Content-Type: application/json" -u "2743204aad6fe2572aa2d8de:e674a3d0fd42a53b9a58121c"
```

```
GET /v3/push/cid?count=3
Authorization: Basic (base64 auth string)
Content-Type: text/plain
Accept: application/json
```

**Request Params**

```
count
	可选参数。数值类型，不传则默认为 1。范围为 [1, 1000]
type
	可选参数。CID 类型。取值：push（默认），schedule
```

**Response Header**
 
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
 
 Response Data  
 
{
 "cidlist":[
 "8103a4c628a0b98994ec1949-128eeb45-471c-49f3-b442-a05c20c9ed56",
 "8103a4c628a0b98994ec1949-6e44d7f1-89f5-48a8-bec4-e359c15b13e5",
 "8103a4c628a0b98994ec1949-47e0a960-ce67-4e71-94ce-b4b9e8813af0"
 ]
}
```

**Response Params**

```
cidlist
	cid 列表
```



## Group Push API：应用分组推送 

### 调用地址
POST  https://api.jpush.cn/v3/grouppush

### 功能说明
该 API 用于为开发者在 portal 端创建的应用分组创建推送。

groupkey 可以在创建的分组信息中获取，使用起来同 appkey 类似，但在使用的时候前面要加上 “group-” 前缀。

***注***：暂不支持 option 中 override\_msg\_id 的属性；分组推送仅在官网支持设置定时，调 Schedule API 时不支持。

### 调用示例

```
curl --insecure -X POST -v https://api.jpush.cn/v3/grouppush -H "Content-Type: application/json" -u "group-e4c938578ee598be517a2243:71d1dc4dae126674ed386b7b" -d '{"platform":["android"],"audience":"all","notification":{"android":{"alert":"notification content","title":"notification title"}},"message":{"msg_content":"message content"}}'
```


## 批量单推（VIP专属接口） 

### 调用地址
POST  https://api.jpush.cn/v3/push/batch/regid/single <br/>
POST  https://api.jpush.cn/v3/push/batch/alias/single

***注***：/v3/push/batch/regid/single 针对的是RegID方式批量单推，/v3/push/batch/alias/single 针对的是Alias方式批量单推

### 功能说明
如果您在给每个用户的推送内容都不同的情况下，可以使用此接口。

如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### 调用说明
使用此接口前，您需要配合使用 [cid:推送唯一标识符](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#cid) 接口提前获取到 cid 池，获取时 type=push 或者不传递 type 值；获取到cid值后，传递参数格式如下：

```
{"pushlist":{
    "cid值1":{     
        ...
    },
    "cid值2":{     
        ...
    },
    ...
}}

```

### 调用示例

**Request Header**

> POST /v3/push/batch/regid/single HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==

或者
> POST /v3/push/batch/alias/single HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==


**Request Params**

```
pushlist
	必填参数。JSON类型
cid值
	必填参数。JSON类型，取值：push（默认），JSON Value部分具体字段参考下面表格说明
```
<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th>关键字</th>
			<th >选项</th>
			<th >含义</th>
		</tr>
		<tr >
			<td>platform</td>
			<td>必填</td>
			<td>推送平台设置</td>
		</tr>
		<tr >
			<td>target</td>
			<td>必填</td>
			<td>推送设备指定。<br/>如果是调用RegID方式批量单推接口（/v3/push/batch/regid/single），那此处就是指定regid值；<br/>如果是调用Alias方式批量单推接口（/v3/push/batch/alias/single），那此处就是指定alias值。</td>
		</tr>
		<tr >
			<td>notification</td>
			<td>可选</td>
			<td>通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存</td>
		</tr>
		<tr >
			<td>message</td>
			<td>可选</td>
			<td>消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存 </td>
		</tr>
		<tr>
			<td>sms_message</td>
			<td>可选</td>
			<td>短信渠道补充送达内容体</td>
		</tr>
		<tr >
			<td>options</td>
			<td>可选</td>
			<td>推送参数 </td>
		</tr>
	</table>
</div>

完整参数示例：
```
{"pushlist":{
    "cid1":{     
        "platform": "all",
        "target": "aliasvalue1",       // 此处填写的是regid值或者alias值
        "notification": {
            ...    // 省略参数同push api部分
        },
        "message": {
            ...   // 省略参数同push api部分
        },
        "sms_message":{
            ...  // 省略参数同push api部分
        },
        "options": {
            ...  // 省略参数同push api部分
        }
    },
    "cid2":{     
        "platform": "all",
        "target": "aliasvalue2",       // 此处填写的是regid值或者alias值
        "notification": {
            ...
        },
        "message": {
            ...
        },
        "sms_message":{
            ...
        },
        "options": {
            ...
        }
    },
    ...
}}
```

**Response**

成功返回：
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
 
Success Response Data
{
    "cid1"：{
        "msg_id":134123478
    },
    "cid1"：{
        "msg_id":134123478,
        "error":{
            "code":1011,
            "message":"****"
        }
    },
    "cid3"：{
        "error":{
            "code":1009,
            "message":"****"
        }
    },
    ...
}
```

失败返回：
```
HTTP/1.1 400 OK
Content-Type: application/json; charset=utf-8
 
 Failed Response Data 
{
    "error":{
        "message":"Authen failed",
        "code":1004
    }
}
```


## 推送校验 API

### 调用地址
POST https://api.jpush.cn/v3/push/validate

### 功能说明
该 API 只用于验证推送调用是否能够成功，与推送 API 的区别在于：不向用户发送任何消息。
其他字段说明：同推送 API。

## 调用返回


<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th >描述</th>
			<th >详细解释</th>
			<th >HTTP Status Code</th>
		</tr>
		<tr >
			<td>1000</td>
			<td>系统内部错误</td>
			<td>服务器端内部逻辑错误，请稍后重试。</td>
			<td>500</td>
		</tr>
		<tr >
			<td>1001</td>
			<td>只支持 HTTP Post 方法</td>
			<td>不支持 Get 方法。</td>
			<td>405</td>
		</tr>
		<tr >
			<td>1002</td>
			<td>缺少了必须的参数</td>
			<td>必须改正，检查要求必填的参数是否未写</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1003</td>
			<td>参数值不合法</td>
			<td>必须改正。参数不合法的情况如：Audience 参数中 tag，alias，registration_id 有空值；单发指定的 registration_id 非法或者格式错误。 </td>
			<td>400</td>
		</tr>
		<tr >
			<td>1004</td>
			<td>验证失败</td>
			<td>必须改正。检查 Appkey 与 MasterSecret，详情请看：<a href="./#_5">调用验证</a></td>
			<td>401</td>
		</tr>
		<tr >
			<td>1005</td>
			<td>消息体太大</td>
			<td>必须改正。
				Android 平台 Notification+Message 长度限制为 4000 字节；
				iOS Notification 中 “iOS”:{ } 及大括号内的总体长度不超过：2000 个字节（包括自定义参数和符号），iOS 的 Message 部分长度不超过 4000 字节；
				WinPhone 平台 Notification 长度限制为 1000 字节</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1008</td>
			<td>app_key 参数非法</td>
			<td>必须改正，请仔细对比你所传的 Appkey 是否与应用信息中的一致，是否多了空格</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1009</td>
			<td>推送对象中有不支持的 key</td>
			<td>必须改正，提示：Android 属性不支持 sound 字段；是否将 content-available 错误地写为 content_available，builder_id 错误地写为 build_id；除文档中指定的字段外，还需传递自定义的 key 请在 extras 中填写。</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1011</td>
			<td>没有满足条件的推送目标</td>
			<td>请检查是否有设备满足 audience 的目标条件（别名与标签是否设置成功）；若客户端未完成 SDK 集成，服务端先做测试，需下载 demo 安装到手机上再做推送；第一次集成成功，若采用广播推送请等待 10 分钟。</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1012</td>
			<td>符合当前条件的推送已超过限制</td>
			<td>定速推送超过限制</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1020</td>
			<td>只支持 HTTPS 请求</td>
			<td>必须改正</td>
			<td>404</td>
		</tr>
		<tr >
			<td>1030</td>
			<td>内部服务超时</td>
			<td>稍后重试，若多次重试无法成功，请联系 support@jpush.cn</td>
			<td>503</td>
		</tr>
		<tr>
			<td>2002</td>
			<td>API调用频率超出该应用的限制</td>
			<td>注意<a href="https://docs.jiguang.cn/jpush/server/push/server_overview/#api_1"> API 频率控制</a>，可联系极光商务或技术支持开通更高的 API 调用频率</td>
			<td>429</td>
		</tr>
		<tr>
			<td>2003</td>
			<td>该应用 appkey 已被限制调用 API</td>
			<td>联系技术支持查明限制原因和寻求帮助</td>
			<td>403</td>
		</tr>
		<tr>
			<td>2004</td>
			<td>无权限执行当前操作</td>
			<td>必须改正。当前调用 API 的源 ip 地址不在该应用的 ip 白名单中，请在官网应用设置中配置 IP 白名单。</td>
			<td>403</td>
		</tr>
		<tr>
			<td>2005</td>
			<td>信息发送量超出合理范围。</td>
			<td>检测到目标用户累计发送消息量过大，超过合理的使用范围，需要检查业务逻辑或者联系技术支持。</td>
			<td>403</td>
		</tr>
		<tr>
			<td>2006</td>
			<td>非VIP用户。</td>
			<td>接口只针对VIP用户开放。</td>
			<td>403</td>
		</tr>
		<tr>
			<td>2007</td>
			<td>无权调用此接口。</td>
			<td>请联系商务开通使用权限。</td>
			<td>403</td>
		</tr>
	</table>
</div>


## 参考
+ HTTP 返回码：[HTTP-Status-Code](http_status_code/)
+ 获取推送送达 API：[Report-API](rest_api_v3_report)
+ 老版本 Push API：[Push API v2](../old/rest_api_v2_push)
+ HTTP 规范参考：[HTTP 基本认证](http://zh.wikipedia.org/zh/HTTP基本认证)
+ Apple APNs 规范：[Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)
+ Microsoft MPNs 规范：[Push notifications for Windows Phone 8](http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff402558(v=vs.105).aspx)

