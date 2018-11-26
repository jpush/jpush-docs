<h1>好友管理</h1>


## 概述

jmessage android sdk 从1.4.0版本开始提供接口实现对用户好友关系的托管，以及相关好友请求的发送和接收。  

好友模块仅实现对用户好友关系的托管，以及相关好友请求的发送和接收。除此之外的任何建立在好友关系之上的功能（如仅限于好友之间才能进行的聊天等），需要开发者的应用层自己实现。jmessage本身是无好友通信模式。



### 发送好友添加请求
发送添加好友请求。在对方未做回应的前提下，允许重复发送添加好友的请求。请求发送后对方会收到一条好友请求的[ContactNotifyEvent](#ContactEvent)事件。

```
public static void sendInvitationRequest(final String targetUsername,String appKey, final String reason, final BasicCallback callback)
```

参数定义

+ String targetUsername 被邀请方用户名
+ String appKey 被邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ String reason 申请理由
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.sendInvitationRequest("test_user", "test_appkey", "hello", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //好友请求请求发送成功
                } else {
                    //好友请求发送失败
                }
            }
        });
```


### 接受好友请求
接受对方的好友请求，操作成功后，对方会出现在自己的好友列表中，双方建立起好友关系。请求发送后对方会收到一条好友请求被接受的[ContactNotifyEvent](#ContactEvent)事件。

```
ContactManager.acceptInvitation(final String targetUsername, String appKey, final BasicCallback callback)
```

参数定义

+ String targetUsername 邀请方的用户名
+ String appKey 邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.acceptInvitation("test_user", "test_appkey", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //接收好友请求成功
                } else {
                    //接收好友请求失败
                }
            }
        });
```


### 拒绝好友请求
拒绝对方的好友请求。请求发送后对方会收到一条好友请求被拒绝的[ContactNotifyEvent](#ContactEvent)事件。

```
ContactManager.declineInvitation(final String targetUsername, String appKey, String reason, final BasicCallback callback)
```

参数定义

+ String targetUsername 邀请方用户名
+ String appKey 邀请方用户的appKey,如果为空则默认从本应用appKey下查找用户。
+ String reason 拒绝理由
+ BasicCallback callback 结果回调

代码示例：

```
ContactManager.declineInvitation("test_user", "test_appkey", "sorry~", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //拒绝好友请求成功
                } else {
                    //拒绝好友请求失败
                }
            }
        });
```

### 获取好友列表
获取当前登录用户的好友列表，异步返回结果。

```
ContactManager.getFriendList(final GetUserInfoListCallback callback)
```

参数定义

+ GetUserInfoListCallback callback 结果回调。

代码示例：

```
ContactManager.getFriendList(new GetUserInfoListCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage, List<UserInfo> userInfoList) {
                if (0 == responseCode) {
                    //获取好友列表成功
                } else {
                    //获取好友列表失败
                }
            }
        });
```

### 删除好友
将用户从你的好友列表中移除，移除成功后，对方会收到一条好友被移除的[ContactNotifyEvent](#ContactEvent)事件。

```
userinfo.removeFromFriendList(BasicCallback callback)
```

参数定义

+ BasicCallback callback 结果回调

代码示例：

```
userinfo.removeFromFriendList(new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //移出好友列表成功
                } else {
                    //移出好友列表失败
                }
            }
        });
```

### 更新用户备注名/备注信息
为好友添加备注名和备注信息。仅当用户存在于你的好友列表中时，才能更新其备注名和备注信息。

```
userinfo.updateNoteName(String noteName, BasicCallback callback)

userinfo.updateNoteText(String noteText, BasicCallback callback)
```

参数定义：

+ String noteName 新的备注名
+ String noteText 新的备注信息
+ BasicCallback callback 结果回调

代码示例：

```
userinfo.updateNoteName("new_note_name", new BasicCallback() {
            @Override
            public void gotResult(int responseCode, String responseMessage) {
                if (0 == responseCode) {
                    //更新备注名成功
                } else {
                    //更新备注名失败
                }
            }
        });
```

### <span id="ContactEvent">好友相关通知事件</span>

新增联系人相关通知事件`ContactNotifyEvent`,具体事件处理方法见：[事件处理](./event)一节
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getType()</td>
      <td >ContactNotifyEvent.Type</td>
      <td >获取联系人通知事件的具体类型，具体类型见[Type](../im_android_api_docs/cn/jpush/im/android/api/event/ContactNotifyEvent.Type.html)定义</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >String</td>
      <td >获取事件发生的理由，该字段由对方发起请求时所填，对方如果未填则将返回默认字符串</td>
    </tr>
    <tr >
      <td >getFromUsername()</td>
      <td >String</td>
      <td >获取事件发送者的username</td>
    </tr>
    <tr >
      <td >getFromUserAppKey()</td>
      <td >String</td>
      <td >获取事件发送者用户所属应用的appKey</td>
    </tr>
  </table>
</div>


示例代码：

```
class ContactNotifyEventReceiver extends Activity{

  @Override
  protected void onCreate() {
    super.onCreate(savedInstanceState);
    JMessageClient.registerEventReceiver(this);
  }

  @Override
  protected void onDestroy() {
    JMessageClient.unRegisterEventReceiver(this);
    super.onDestroy();
  }
  
  public void onEvent(ContactNotifyEvent event) {
        String reason = event.getReason();
        String fromUsername = event.getFromUsername();
        String appkey = event.getfromUserAppKey();

        switch (event.getType()) {
            case invite_received://收到好友邀请
                //...
                break;
            case invite_accepted://对方接收了你的好友邀请
                //...
                break;
            case invite_declined://对方拒绝了你的好友邀请
                //...
                break;
            case contact_deleted://对方将你从好友中删除
                //...
                break;
            default:
                break;
        }
    }

}

```

