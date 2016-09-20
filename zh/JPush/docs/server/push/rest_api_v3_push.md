#Push API <small>v3</small>


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
POST  https://api.jpush.cn/v3/push

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

HTTP Header（头）里加一个字段（Key/Value对）：

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
	</table>
</div>

### 示例与说明

```
{
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
            "extras": {
                "newsid": 321
            }
        },
        "ios": {
            "alert": "Hi, JPush!",
            "sound": "default",
            "badge": "+1",
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
    	"content":"sms msg content",
    	"delay_time":3600
	},
    "options": {
        "time_to_live": 60,
        "apns_production": false
    }
}

```

## platform：推送平台

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios", "winphone"。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;  padding-bottom: 0;margin-bottom: 0;">
<p>如果目标平台为 iOS 平台 需要在 options 中通过 apns_production 字段来设定推送环境。True 表示推送生产环境，False 表示要推送开发环境； 如果不指定则为推送生产环境</p>
</div>
<br>

推送到所有平台：

	{ "platform" : "all" }

指定特定推送平台：

	{ "platform" : ["android", "ios"] }

## audience：推送目标

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册ID、分群、广播等。

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
			<td>标签</td>
			<td>数组。多个标签之间是 OR 的关系，即取并集。 </td>
			<td>用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。<ul style="margin-bottom: 0;"><li>有效的 tag 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|￥。</li><li>限制：每一个 tag 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>tag_and</td>
			<td>JSON Array</td>
			<td>标签AND</td>
			<td>数组。多个标签之间是 AND 关系，即取交集。</td>
			<td>注册与 tag 区分。一次推送最多 20 个。</td>
		</tr>
		<tr >
			<td>alias</td>
			<td>JSON Array</td>
			<td>别名</td>
			<td>数组。多个别名之间是 OR 关系，即取并集。</td>
			<td>用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。<ul style="margin-bottom: 0;"><li>有效的 alias 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符@!#$&*+=.|￥。</li><li>限制：每一个 alias 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>registration_id</td>
			<td>JSON Array</td>
			<td>注册ID</td>
			<td>数组。多个注册ID之间是 OR 关系，即取并集。</td>
			<td>设备标识。一次推送最多 1000 个。</td>
		</tr>
	</table>
</div>


<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>每种类型的值都是数组（Array），数组内多个值之间隐含的关系是是 OR，即取并集。但 tag_and 不同，其数组里多个值之间是 AND 关系，即取交集。</p>
<p>4 种类型至少需要有其一。如果值数组长度为 0，表示该类型不存在。</p>
<p>这几种类型可以并存时，多项的隐含关系是 AND，即取几种类型结果的交集。</p>
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

+ 推送给多个注册ID：

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
		"tag" : [ "深圳", "广州" ]
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
			<td>如果指定了，则通知里原来展示 App名称的地方，将展示成这个字段。</td>
		</tr>
		<tr >
			<td>builder_id</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏样式ID</td>
			<td>Android SDK 可设置通知栏样式，这里根据样式 ID 来指定该使用哪套样式。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>扩展字段</td>
			<td>这里自定义 JSON 格式的 Key/Value 信息，以供业务使用。</td>
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
			<td>这里指定内容将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。支持字符串形式也支持官方定义的<a href="https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/TheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH107-SW1">alert payload</a> 结构</td>
		</tr>
		<tr >
			<td>sound</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%">通知提示声音</td>
			<td>如果无此字段，则此消息无声音提示；有此字段，如果找到了指定的声音就播放该声音，否则播放默认声音,如果此字段为空字符串，iOS 7 为默认声音，iOS 8 为无声音。(消息) 说明：JPush 官方 API Library (SDK) 会默认填充声音字段。提供另外的方法关闭声音。</td>
		</tr>
		<tr >
			<td>badge</td>
			<td>int</td>
			<td>可选</td>
			<td width="20%">应用角标</td>
			<td>如果不填，表示不改变角标数字；否则把角标数字改为指定的数字；为 0 表示清除。JPush 官方 API Library(SDK) 会默认填充badge值为"+1",详情参考：<a href="http://blog.jpush.cn/ios_apns_badge_plus/">badge +1</a></td>
		</tr>
		<tr >
			<td>content-available</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">推送唤醒</td>
			<td>推送的时候携带"content-available":true 说明是 Background Remote Notification，如果不携带此字段则是普通的Remote Notification。详情参考：<a href="../../client/iOS/ios_new_features/#ios-7-background-remote-notification">Background Remote Notification</a></td>
		</tr>
		<tr >
			<td>category</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%"> </td>
			<td>IOS8才支持。设置APNs payload中的"category"字段值</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td width="20%">扩展字段</td>
			<td>这里自定义 Key/value 信息，以供业务使用。</td>
		</tr>
	</table>
</div>


<br>
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>iOS 通知 JPush 要转发给 APNs 服务器。APNs 协议定义通知长度为 2048 字节。</p>
<p>JPush 因为需要重新组包，并且考虑一点安全冗余，要求"iOS":{ } 及大括号内的总体长度不超过：2000 个字节。JPush 使用 utf-8 编码，所以一个汉字占用 3 个字节长度。</p>
<br>
 
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

**客户端收到apns**

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
iOS 平台上，此部分内容在推送应用内消息通道（非APNS）获取。Windows Phone 暂时不支持应用内消息。

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
Android 1.6.2及以下版本 接收notification 与message并存（即本次api调用同时推送通知和消息）的离线推送， 只能收到通知部分，message 部分没有透传给 App。

Android 1.6.3及以上SDK 版本已做相应调整，能正常接收同时推送通知和消息的离线记录。

iOS 1.7.3及以上的版本才能正确解析v3的message，但是无法解析v2推送通知同时下发的应用内消息。

```

## sms_message：短信补充

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>使用短信业务，会产生额外的运营商费用，具体请咨询商务，联系电话：400-612-5955  商务QQ：800024881</p>
</div>

<br>

用于设置短信推送内容以及短信发送的延迟时间。手机接收号码,开发者需要先把用户的手机号码与设备的registration id匹配。绑定方法：[服务端-Device-更新设备](rest_api_v3_device/#device)

与原有 JSON 业务协议相匹配，消息有如下字段信息：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>示例</th>
		</tr>
		<tr >
			<td>content</td>
			<td>string</td>
			<td>必填</td>
			<td>不能超过480个字符。"你好,JPush"为8个字符。超过67个字符的内容（含签名）会被拆分成多条短信下发。</td>
		</tr>
		<tr >
			<td>delay_time</td>
			<td>int</td>
			<td>必填</td>
			<td>单位为秒，不能超过24小时。设置为0，表示立即发送短信。该参数仅对android平台有效，iOS 和 Winphone平台则会立即发送短信</td>
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
			<td>纯粹用来作为 API 调用标识，API 返回时被原样返回，以方便 API 调用方匹配请求与返回。</td>
		</tr>
		<tr >
			<td>time_to_live</td>
			<td>int</td>
			<td>可选</td>
			<td>离线消息保留时长(秒)</td>
			<td>推送当前用户不在线时，为该用户保留多长时间的离线消息，以便其上线时再次推送。默认 86400 （1 天），最长 10 天。设置为 0 表示不保留离线消息，只有推送当前在线的用户可以收到。</td>
		</tr>
		<tr >
			<td>override_msg_id</td>
			<td>long</td>
			<td>可选</td>
			<td>要覆盖的消息ID</td>
			<td>如果当前的推送要覆盖之前的一条推送，这里填写前一条推送的 msg_id 就会产生覆盖效果，即：1）该 msg_id 离线收到的消息是覆盖后的内容；2）即使该 msg_id Android 端用户已经收到，如果通知栏还未清除，则新的消息内容会覆盖之前这条通知；覆盖功能起作用的时限是：1 天。如果在覆盖指定时限内该 msg_id 不存在，则返回 1003 错误，提示不是一次有效的消息覆盖操作，当前的消息不会被推送。</td>
		</tr>
		<tr >
			<td>apns_production</td>
			<td>boolean</td>
			<td>可选</td>
			<td>APNs是否生产环境</td>
			<td>True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。JPush 官方 API LIbrary (SDK) 默认设置为推送 “开发环境”。</td>
		</tr>
		<tr >
			<td>big_push_duration</td>
			<td>int</td>
			<td>可选</td>
			<td>定速推送时长(分钟)</td>
			<td>又名缓慢推送，把原本尽可能快的推送速度，降低下来，给定的n分钟内，均匀地向这次推送的目标用户推送。最大值为1400.未设置则不是定速推送。</td>
		</tr>
	</table>
</div>

## 推送校验 API
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
			<td>必须改正</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1003</td>
			<td>参数值不合法</td>
			<td>必须改正，如Audience参数中tag，alias，registration_id有空值，错误提示Empty tag/alias/registration_id is not allowed!</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1004</td>
			<td>验证失败</td>
			<td>必须改正。详情请看：<a href="./#_5">调用验证</a></td>
			<td>401</td>
		</tr>
		<tr >
			<td>1005</td>
			<td>消息体太大</td>
			<td>必须改正。
				Android平台Notification+Message长度限制为4000字节；
				iOS Notification 中 “iOS”:{ } 及大括号内的总体长度不超过：2000个字节（包括自定义参数和符号），iOS 的 Message部分长度不超过 4000 字节；
				WinPhone平台Notification长度限制为4000字节</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1008</td>
			<td>app_key参数非法</td>
			<td>必须改正</td>
			<td>400</td>
		</tr>
		<tr >
			<td>1011</td>
			<td>没有满足条件的推送目标</td>
			<td>请检查audience</td>
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
			<td>稍后重试</td>
			<td>503</td>
		</tr>
	</table>
</div>


## 参考
+ HTTP 返回码：[HTTP-Status-Code](http_status_code/)
+ 获取推送送达API：[Report-API](rest_api_v3_report)
+ 老版本 Push API：[Push API v2](../old/rest_api_v2_push)
+ HTTP 规范参考：[HTTP基本认证](http://zh.wikipedia.org/zh/HTTP基本认证)
+ Apple APNs 规范：[Apple Push Notification Service](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100-SW12)
+ Microsoft MPNs 规范：[Push notifications for Windows Phone 8](http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff402558(v=vs.105).aspx)

