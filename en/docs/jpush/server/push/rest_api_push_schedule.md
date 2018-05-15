# Schedule API <small>v3</small>

## Overview

The API level supports timing functions.
This is a relatively independent task execution module that maintains a Schedule object.

### Call Address

https://api.jpush.cn/v3/schedules

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>If the created Jiguang application is allocated to the Beijing computer room and the API caller's server is also located in Beijing, it is more suitable to call the API of the Jiguang Beijing computer room, which can improve the response speed.</p>
<p>The room where the application is located can be seen through Application Settings -> Application Info of the Jiguang Web Console. If the application locates in the Beijing computer room, the calling address of each API will be given at the same time.</p>

<p>Call address of Push API in Beijing computer room: https://bjapi.push.jiguang.cn/v3/push/schedules </p>
<p>For the detailed mapping relationship, see the "Server Location" information in "Application Information".</p>
</div>

## Call Verification
Add a field (Key/Value pair) in the HTTP Header (header):
Authorization: Basic base64_auth_string
The generation algorithm of base64_auth_string is: base64(appKey:masterSecret)
That is, add a colon to the appKey, plus the string assembled by masterSecret, and do a base64 conversion.

## Definition of Schedule Object

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

**Field Description：**

Each schedule task consists of four sections: name, enabled, trigger, and push.

+ cid
    + Same as cid in push api, see cid description for details. Note: The cid field in the push field of the schedule api payload will be ignored.
+ push
    + Refer to the fields in the push api
+ name
    + Indicate the name of the schedule task, which is returned by the schedule-api after the user successfully creates the schedule task. It must not exceed 255 bytes and consists of Chinese characters, letters, numbers, and underscores.。
+ enabled
    + Indicate the status quo of the task. Boolean must be true or false. Must be true when creating the task.
+ trigger
    + Indicate the trigger condition of the schedule task. Currently, only the timed tasks (single) and scheduled tasks are supported.
        + single(Indicate timed tasks)
            + time is required and the format is "YYYY-mm-dd HH:MM:SS", such as "2014-02-15 13:16:59". The format cannot be "2014-2-15 13:16:59" or "2014-12-15 13:16", that is, the date and time format must be complete.
        + periodical(Indicate scheduled tasks)
            * start indicates the start time of the scheduled task. The format must be strictly: "YYYY-mm-dd HH:MM:SS", and the time must be 24 hours.
            * end indicates the expiration time of a scheduled task. The format is the same as above. Scheduled tasks do not exceed one year.
            * time indicates the periodic execution time of the scheduled task. The format must be strictly: "HH:MM:SS" and it is a 24-hour clock.
            * time_unit indicates that the minimum time units for the execution of scheduled tasks include: "day", "week", and "month". Case insensitive, such as "day", "Day", "DAy" are all legitimate time_unit.
            * frequency: The execution period of scheduled task represents by the product of this item and time_unit. For example, when time_unit is day and frequency is 2, it means that the push is triggered every two days. The maximum value supported is 100.
            * point: A list that corresponds to time_unit.

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Time_unit</th>
      <th >Point</th>
      <th >Description</th>
    </tr>
    <tr >
      <td>day</td>
      <td>NIL</td>
      <td>Point is invalid when time_unit is day</td>
    </tr>
    <tr >
      <td>week</td>
      <td>"MON","TUE","WED","THU","FRI","SAT","SUN"</td>
      <td>When time_unit is week, point is one or more items of the corresponding item, indicating that which day of the week is triggered, and the value in point is case-insensitive.</td>
    </tr>
    <tr >
      <td>month</td>
      <td>"01","02","03" .... "31"</td>
      <td>When time_unit is month, point is the date corresponding to the current month, and it must be valid. If month is 2 months, 31 or 30 will not be triggered.</td>
    </tr>
  </table>
</div>

## Create a Scheduled Task

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

**Description of Request Data**

+ Due to timed task is relatively simple, we only describe scheduled tasks in our example
+ The above indicates that a scheduled task is created. The effective time must be '2014-09-17 after 12:00:00', the first time point, and the expiration time is '2014-10-18 12:00:00'. During the validity period, execute Wednesday and Friday of every two weeks at 12 noon
+ The time when the scheduled task was first created must not be later than the time specified in its end, otherwise it will fail to create
+ The enabled item must be true when the scheduled task (including timed tasks) is first created. Cannot create a task with enabled:false, otherwise the creation fails
+ Push must be a valid and legal push action, otherwise the creation fails

### Example Response

***Success Response***

```
HTTP/1.1 200 CREATED
 Content-Type: application/json; charset=utf-8
{
    "schedule_id":"0eac1b80-c2ac-4b69-948b-c65b34b96512",
    "name":"&#23450;时推送示例"    //长度最大255字节，数字、字母、下划线、汉字。
}
```

***Failed Response***

```
HTTP/1.1 400 BAD REQUEST
 Content-Type: application/json; charset=utf-8
{
  "error":
  {
    "code":8400,
    "message":"error message"
  }
}
```

##Get a List of Valid Schedules

```
GET https://api.jpush.cn/v3/schedules?page=
```

Get a list of schedules that are currently valid (endtime is not expired)

### Example Request

***Request Header***


```
GET /v3/schedules?page=
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```

+ Return the detailed schedule-task list of the current request page. If no page is specified, the page is 1
+ Sorting rules: creation time, completed by schedule-service
+ If the number of requested pages is greater than the total number of pages, page is the request value and schedules is empty
+ A maximum of 50 tasks are returned per page. If the actual number of tasks on the request page is less than 50, the actual number of tasks is returned.

### Example Response

***Success Response***

```
HTTP/1.1 200 OK
 Content-Type: application/json; charset=utf-8
{
    "total_count":1000,  //&#25968;字 表示总数
    "total_pages":5,      //&#24635;页数。
    "page":4,     //&#24403;前为第四页。
    "schedules":[
        {"schedule_id":"0eac1b80-c2ac-4b69-948b-c65b34b96512","name":"","enabled":...},{}, //&#35814;细信息列表。
    ]
}
```

+ The above represents a total of 1000 schedule-tasks. It is a total of 5 pages, and page 4 currently displays, containing information for 50 schedule-tasks.
+ The returned schedules are a detailed list of schedule-tasks.

## Get Specified Scheduled Task

```
 GET https://api.jpush.cn/v3/schedules/{schedule_id}
```

### Example Request

***Request Header***

```
GET /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```

+ Get the details of the scheduled task with the current user's schedule task id {schedule_id}

### Example Response

***Success Reponse***

```
HTTP/1.1 200 OK
 Content-Type: application/json; charset=utf-8
Response Data
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
+ If schedule_id does not exist, it returns 404, otherwise it returns the details of the actual schedule-task.

##Modify a Specified Schedule

```
PUT https://api.jpush.cn/v3/schedules/{schedule_id}
```

### Example Request

```
PUT /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string)
 Content-Type: application/x-www-form-urlencoded
 Accept: application/json
```

+ Update the scheduled task of the specified id

```
{
   "name": "task",
   "enabled": true,
   "trigger": {

    },
   "push": { ... }
}
```

+ Update operation can be one or more of the "name", "enabled", "trigger", or "push".
+ Does not support partial updates, such as tasks prior to updating：

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

+ The following are examples of the incorrect updates and the corresponding right updates：

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

### Example Response

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

+ schedule_id is invalid, and not a valid uuid

```
HTTP/1.0 404 Not Found
 Content-Type: application/json
```

+ The update operation is illegal

```
HTTP/1.0 400 BAD REQUEST
 Content-Type: application/json
```

## Delete the Specified Schedule Task

```
DELETE https://api.jpush.cn/v3/schedules/{schedule_id}
```

Schedule_id is the id of the created schedule task. If the schedule_id is invalid, that is, it is not a valid uuid, then 404.

### Example Request

```
DELETE /v3/schedules/{schedule_id}
 Authorization: Basic (base64 auth string)
 Content-Type: application/json
 Accept: application/json
```

### Example Response

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

## Description of Error Code
<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <td>Code</td>
      <td>HTTP</td>
      <td>Description</td>
      <td>Error Message</td>
      <td>Detailed Explanation</td>
    </tr>
    <tr>
      <td>8000</td>
      <td>200</td>
      <td>Return correctly</td>
      <td>nil</td>
      <td>Success status code</td>
    </tr>
    <tr>
      <td>8104</td>
      <td>404</td>
      <td>The requested schedule task does not exist</td>
      <td>Request schedule operation doesn't exist</td>
      <td>The requested timing api operation does not exist</td>
    </tr>
    <tr>
      <td>8101</td>
      <td>401</td>
      <td>Authentication failed</td>
      <td>Basic authentication failed.</td>
      <td>Appkey masterscrect does not match</td>
    </tr>
    <tr>
      <td>8100</td>
      <td>400</td>
      <td>Invalid parameter</td>
      <td>The schedule-task is invalid: section is invalid; has been at term; expired; request data is not json; update target task; Delete target task; schedule request is not exist.</td>
      <td>The parameter is illegal or invalid and has not passed the check</td>
    </tr>
    <tr>
      <td>8203</td>
      <td>503</td>
      <td>Internal system error. it is recommended to try again later</td>
      <td>Execute action timeout, please try later again</td>
      <td>Communication error with schedule-server</td>
    </tr>
    <tr>
      <td>8200</td>
      <td>500</td>
      <td>Internal system error</td>
      <td>Server internal error.</td>
      <td>An unexpected error occurred.</td>
    </tr>
  </table>
</div>

***Format of Error Return***

```
{"error":{"code":errcode, "message":"error message"}}
```

## Call Limits

+ The total number of maximum valid timers (the unexpired number currently) and maximum valid cycles (the unexpired number currently) is 100. Failed after exceeding.
+ The maximum frequency is currently 100/minute
+ The periodical task has a maximum span of 12 months.