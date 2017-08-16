#API Push Schedule

## 概述

API 层面支持定时功能。  
这是一个相对独立的任务执行模块，维护一个 Schedule 对象。

### 调用地址

POST [https://api.jpush.cn](https://api.jpush.cn)

### 调用验证

HTTP Header（头）里加一个字段（Key/Value对）：  
Authorization: Basic base64_auth_string  
其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)  
即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

## Schedule 对象定义

```
{
   "cid": "7103a4c428a0b98974ec1849-711161d4-5f17-4d2f-b855-5e5a8909b26e",
   "name": "Schedule_Name",
   "enabled": true,
   "trigger": {
        "single":{ 
            "time": "2014-09-17 12:00:00"  //YYYY-MM-DD HH:MM:SS
         }
   },
   "push": {
     "platform": "all",
     "audience": "all",
     "notification": {
          "alert" : "Hello, JPush!"
     },
     "message": {
          "msg_content":"Message!"
     },
     "options": {
          "time_to_live":60
     }
  } 
}
  
{ 
  "name": "Schedule_Name",
  "enabled": true,
  "trigger": {
     "periodical": {
          "start":"2014-09-17 12:00:00",
          "end": "2014-09-18 12:00:00", 
          "time": "12:00:00", 
          "time_unit": "WEEK",   //month, week, day, 大小写不敏感
          "frequency": 1,
          "point": ["WED","FRI"]   //time_unit为day时候，point不能存在。WED,FRI 大小写不敏感。month:"01","02"
     }
  }, 
  "push": { 
        "platform": "all", 
        "audience": "all",
        "notification": {"alert" : "Hello, JPush!" }, 
        "message": {"msg_content":"Message!" }, 
        "options": {"time_to_live":60}
   }
}
```

***字段说明：***

每一个schedule任务，都由name、enabled、trigger、push这四个小节组成。

+ cid
	+ 和 push api 中 cid 用法一致，详见 [cid 说明](rest_api_v3_push/#cid) 。注：schedule payload 中的 push 字段中含有 cid 字段将会被忽略。	
+ name
	+ 表示schedule任务的名字，由schedule-api在用户成功创建schedule任务后返回，不得超过255字节，由汉字、字母、数字、下划线组成。
+ enabled
	+ 表示任务当前状态，布尔值，必须为true或false，创建任务时必须为true。
+ trigger 
	+ 表示schedule任务的触发条件，当前只支持定时任务（single）与定期任务（periodical）。
		+ single
			+ 表示定时任务  
				+ time为必选项且格式为"YYYY-mm-dd HH:MM:SS“，如"2014-02-15 13:16:59"，不能为"2014-2-15 13:16:59"或"2014-12-15 13:16"，即日期时间格式必须完整。
		+ periodical
			+ 表示定期任务
				+ start 表示定期任务有效起始时间，格式与必须严格为: "YYYY-mm-dd HH:MM:SS"，且时间必须为24小时制。
				+ end  表示定期任务的过期时间，格式同上。定时任务不超过一年。
				+ time 表示触发定期任务的定期执行时间，格式严格为: "HH:MM:SS"，且为24小时制。
				+ time_unit 表示定期任务的执行的最小时间单位有："day"、"week" 及"month" 三种。大小写不敏感，如"day", "Day", "DAy" 均为合法的time_unit。
				+ frequency 此项与time_unit的乘积共同表示的定期任务的执行周期，如time_unit为day，frequency为2，则表示每两天触发一次推送，目前支持的最大值为100。
				+ point 一个列表，此项与time_unit相对应：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >time_unit</th>
			<th >point</th>
			<th >描述</th>
		</tr>
		<tr >
			<td>day</td>
			<td>NIL</td>
			<td>当time_unit为day时point此项无效</td>
		</tr>
		<tr >
			<td>week</td>
			<td>"MON","TUE","WED","THU","FRI","SAT","SUN"</td>
			<td>当time_unit为week时，point为对应项的一项或多项，表示星期几进行触发,point中的值大小写不敏感</td>
		</tr>
		<tr >
			<td>month</td>
			<td>"01","02","03" .... "31"</td>
			<td>当time_unit为month时，point为当前进行月对应的日期，且必须有效，如month为2月，则31或30日是不会进行触发的</td>
		</tr>
	</table>
</div>



## 创建定时任务

```
POST https://api.jpush.cn/v3/schedules
```


### Example Request

***Request Header***

```
POST /v3/schedules
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```

***Request Data***

```
{
 "name": "&#23450;时推送示例", 
 "enabled": true, 
 "trigger": { 
     "periodical": { 
       "start":"2014-09-17 12:00:00", 
       "end": "2014-10-18 12:00:00", 
       "time": "12:00:00", 
       "time_unit": "WEEK", //month, week, day, &#22823;小写不敏感 
       "frequency": 2, 
       "point": ["WED","FRI"] //time_unit&#20026;day时候，point不能存在。WED,FRI 大小写不敏感。month:"01","02" 
     }
  },
 "push": {
     "platform": "all",
     "audience": "all", 
     "notification": {
          "ios": {
              "alert":"this a test",
              "sound":"default",
              "badge":"+1"
           }
      },
     "message": {}, 
     "options": {"apns_production":"false"}
  } 
}
```

***Request Data 说明***

+ 由于定时任务相对简单，我们例中只对定期任务进行说明
+ 以上表示创建一个定期任务，起始生效时间必须'2014-09-17 12:00:00之后'第一个time时间点，过期时间为'2014-10-18 12:00:00'，在有效期内每两周的周三、周五中午12点分别执行一次
+ 定期任务首次创建时的触发时间不得晚于其end中指定的时间。否则创建失败
+ 定期任务（包括定时任务）首次创建时其enabled项必须为true。不能创建enabled:false的任务，否则创建失败
+ push 必须为有效合法的push动作，否则创建失败。

### Example Response

***Success Response***

```
HTTP/1.1 200 CREATED 
 Content-Type: application/json; charset=utf-8
```

```
{
    "schedule_id":"0eac1b80-c2ac-4b69-948b-c65b34b96512",
    "name":"&#23450;时推送示例"    //长度最大255字节，数字、字母、下划线、汉字。
}
```

***Failed Response***

```
HTTP/1.1 400 BAD REQUEST
 Content-Type: application/json; charset=utf-8
```

```
{
  "error":
  {
    "code":8400,
    "message":"error message"
  }
}
```

## 获取有效的schedule列表

```
GET https://api.jpush.cn/v3/schedules?page=
```

获取当前有效（endtime未过期）的 schedule 列表

###Example Request

***Request Header***

```
GET /v3/schedules?page=
 Authorization: Basic (base64 auth string) 
 Content-Type: application/json
 Accept: application/json
```

+ 返回当前请求页的详细的schedule-task列表，如未指定page则page为1。
+ 排序规则:创建时间,由schedule-service完成。
+ 如果请求页数大于总页数，则 page为请求值，schedules为空。
+ 每页最多返回50个task，如请求页实际的task的个数小于50，则返回实际数量的task。

###Example Response

***Success Response***

```
HTTP/1.1 200 OK 
 Content-Type: application/json; charset=utf-8
```
```
{
    "total_count":1000,  //&#25968;字 表示总数
    "total_pages":5,      //&#24635;页数。
    "page":4,     //&#24403;前为第四页。
    "schedules":[
        {"schedule_id":"0eac1b80-c2ac-4b69-948b-c65b34b96512","name":"","enabled":...},{}, //&#35814;细信息列表。
    ]
}
```
+ 以上表示总共1000个schedule-task, 总共5页，当前为第4页，包含50个schedule-task的信息。
+ 返回的schedules为schedule-task的详细信息列表。

## 获取指定的定时任务

```
 GET https://api.jpush.cn/v3/schedules/{schedule_id}
```

###Example Request

***Request Header***

```
GET /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```
+ 获取当前用户的schedule任务id为{schedule_id}的定时任务的详情。

###Example Response

***Success Reponse***

```
HTTP/1.1 200 OK 
 Content-Type: application/json; charset=utf-8
```

***Response Data***

```
{ 
      "schedule_id":"0eac1b80-c2ac-4b69-948b-c65b34b96512"
      "name": "&#23450;时推送示例", 
      "enabled": true, 
      "trigger": {
         ...
       },
      "push": { ... }
}
```

+ 如schedule_id不存在，则返回404，否则返回实际schedule-task的详情。

## 修改指定的Schedule

```
PUT https://api.jpush.cn/v3/schedules/{schedule_id}
```

###Example Request

```
PUT /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string) 
 Content-Type: application/x-www-form-urlencoded
 Accept: application/json
```
+ 更新指定id的schedule任务。

```
{
   "name": "task", 
   "enabled": true, 
   "trigger": { 
        
    },
   "push": { ... } 
}
```
+ 更新操作可为 "name"，"enabled"、"trigger"或"push" 四项中的一项或多项。
+ 不支持部分更新，如更新之前的任务为：

```
{ 
  "name": "&#23450;时推送示例", 
  "enabled": true, 
  "trigger": {
     "periodical": { 
     "start":"2014-09-17 12:00:00", 
     "end": "2014-10-18 12:00:00", 
     "time": "12:00:00", 
     "time_unit": "WEEK",
     "frequency": 2, 
     "point": ["WED","FRI"]
    }
  },
  "push": {
        "platform":"ios",
        "options":{"apns_production":"false"},
        "audience":"all",
        "notification" : {"alert":"&#23450;时任务更新"}
   }
}
```
+ 则以下为错误的更新及与之对应的正确的更新示例：

```
## WRONG: 更新push中的平台为安卓：
    { 
      "push":{"platform":"android"}
    }
## RIGHT: 更新push中的平台为安卓：
    {
      "push":{       
          "platform":"android",
          "options":{"apns_production":"false"},
          "audience":"all",
          "notification" : {"alert":"&#23450;时任务更新"}
       }
    }
    ## 此处的push更新后必须仍是有效的，否则也会更新失败。
 
## WRONG： 更新periodical中的过期时间延后一个月:
   {
      "trigger":{
         "end":"2014-11-18 12:00:00"
      }
   &#65373;
## RIGHT:  更新periodical中的过期时间延后一个月：
   {
      "trigger":{
        "periodical": { 
           "start":"2014-09-17 12:00:00", 
           "end": "2014-11-18 12:00:00", 
           "time": "12:00:00", 
           "time_unit": "WEEK",
           "frequency": 2, 
           "point": ["WED","FRI"]
        }
      }
   }
   ## time、time_unit、frequency、point的更新同上。
   ## 更新后的trigger必须仍是有效合法的，否则即使trigger整体更新也会失败。可以更新enable:false的任务。
   ## 定时任务(single)与定期任务(periodical)之间不能进行相互更新，即，原先为single类任务，则不能更新为periodical任务，反之亦然。
   ## 不能更新已过期的schedule任务
```


###Example Response

***Success Response***

```
HTTP/1.0 200 CREATED
 Content-Type: application/json
```

```
{ 
  "name": "&#23450;时推送示例", 
  "enabled": true, 
  "trigger": { 
    "periodical": { 
    "start":"2014-09-17 12:00:00",
    "end": "2014-11-18 12:00:00",
    "time": "12:00:00",
    "time_unit": "WEEK", 
    "frequency": 2, 
    "point": ["WED","FRI"] }
   }, 
  "push": {
   "platform":"andiro", 
   "options":{"apns_production":"false"}, 
   "audience":"all", 
   "notification" : {"alert":"&#23450;时任务更新"}
   }
}
```

***Fail Response***

+ schedule_id无效，不是有效的uuid。

```
HTTP/1.0 404 Not Found
 Content-Type: application/json
```

+ 更新操作不合法

```
HTTP/1.0 400 BAD REQUEST
 Content-Type: application/json
```

##删除指定的Schedule任务

```
DELETE https://api.jpush.cn/v3/schedules/{schedule_id}
```

schedule\_id为已创建的schedule任务的id，如果schedule_id不合法即不是有效的uuid，则404。

###Example Request

```
DELETE /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```

###Example Response

***Success Response***

```
HTTP/1.0 200 
  Content-Type: application/json
  Content-Length: 0
```

***Failed Response***

```
HTTP/1.0 404 Not Found 
  Content-Type: application/json
  Content-Length: 0
```

```
{
  "error":{
    "code":8404,
    "message":"..."
  }
}
```

## 错误码描述

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th >HTTP</th>
			<th >描述</th>
			<th>Error Message</th>
			<th>详细解释</th>
		</tr>
		<tr >
			<td>8000</td>
			<td>200</td>
			<td>正确返回</td>
			<td>nil</td>
			<td>成功状态码</td>
		</tr>
		<tr >
			<td>8104</td>
			<td>404</td>
			<td>请求的schedule任务，不存在</td>
			<td>Request schedule operation doesn't exist</td>
			<td>请求的定时api操作不存在</td>
		</tr>
		<tr >
			<td>8101</td>
			<td>401</td>
			<td>鉴权失败</td>
			<td>Basic authentication failed.</td>
			<td>appkey masterscrect 不匹配</td>
		</tr>
		<tr >
			<td>8100</td>
			<td>400</td>
			<td>参数无效</td>
			<td>The schedule-task is invalid：section is invalid;has been at term;expired;request data is not json;update target task;Delete target task;schedule request is not exist</td>
			<td>参数不合法或者无效，没通过校验</td>
		</tr>
		<tr >
			<td>8203</td>
			<td>503</td>
			<td>系统内部错误，建议稍后重试</td>
			<td>Execute action timeout, please try later again</td>
			<td>与schedule-server 通信错误</td>
		</tr>
		<tr >
			<td>8200</td>
			<td>500</td>
			<td>系统内部错误</td>
			<td>Server internal error.</td>
			<td>发生未预料错误。</td>
		</tr>
	</table>
</div>

***错误返回格式***

```
{"error":{"code":errcode, "message":"error message"}}
```

## 调用限制
+ 定时最多有效数（当前未过期数）与周期最多有效数（当前未过期数）总数 100个。超过后失败。
+ 最大频率当前为100/分。
+ periodical任务的最大跨度为12个月。