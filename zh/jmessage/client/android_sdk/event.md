<h1>事件处理</h1>


## 概述
当sdk收到某些后台下发的数据，或者发生了某些需要上层关注的事件时，sdk会上抛事件对象通知给上层，例如，[在线消息事件](../im_android_api_docs/cn/jpush/im/android/api/event/MessageEvent.html)、[会话刷新事件](../im_android_api_docs/cn/jpush/im/android/api/event/ConversationRefreshEvent.html)、[用户下线事件](../im_android_api_docs/cn/jpush/im/android/api/event/LoginStateChangeEvent.html)等。  
应用上层需要根据实际情况决定是否需要接收并且处理事件。

### 事件接收类的注册
应用层可以在任意类中注册事件接收，sdk会持有这个类的强引用，上层需要注意在合适的地方解绑事件接收。  
如果要实现全局事件监听，或者在应用的整个生命周期内都需要监听事件的话，建议放在application类里，不要放在类似activity、或者fragmemt、service之类的组件中。

```
JMessageClient.registerEventReceiver(Object receiver);
JMessageClient.registerEventReceiver(Object receiver, int priority);
```

参数说明

+ Object receiver 消息接收类对象
+ int priority 定义事件接收者接收事件的优先级，默认值为0，优先级越高将越先接收到事件。（优先级只对同一个线程模式中的接收者有效）

### 事件接收类的解绑
```
JMessageClient.unRegisterEventReceiver(Object receiver);
```

参数说明

+ Object receiver 消息接收类对象，对象解绑之后将不再接收到任何event。

### 事件接收
注册事件接收类之后，需要在消息接收类中实现如下方法来接收对应消息。sdk将根据实现方法的方法名来区分不同的线程模式，常用的线程模式有onEvent(默认线程模式)和onEventMainThread(主线程模式)两种。

可以通过定义不同类型的参数，来接收不同种类的事件。具体事件类型定义见 “事件类型” 一节

#### 子线程模式（默认线程）
```
public void onEvent(EventEntity event){
  //do your own business
}
```
方法体将在子线程中被调用， 可以用来处理耗时操作。

参数定义

+ EventEntity event 事件对象。（ 指代下文的具体事件类型实体类型，具体用法可以参考“示例代码“。）

#### 主线程模式
```
public void onEventMainThread(EventEntity event){
  //do your own business
}
```
方法体将在主线程中被调用，可以用来刷新UI。
参数定义

+ EventEntity event 事件对象。EventEntity指代的是下文的具体事件类型


### 用户事件
**当前登录用户信息被更新事件实体类 MyInfoUpdatedEvent**

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">方法</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取更新之后的我的userinfo</td>
    </tr>
    </table>
</div>

**用户下线事件UserLogoutEvent**  
***(已过时，请使用LoginStateChangeEvent代替)***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前被登出账号的信息</td>
    </tr>
  </table>
</div>

</br>

**用户被删除事件UserDeletedEvent**  
***(已过时，请使用LoginStateChangeEvent代替)***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前被删除账号的信息</td>
    </tr>
  </table>
</div>

</br>

**用户登录状态变更事件LoginStateChangeEvent**
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMyInfo()</td>
      <td >UserInfo</td>
      <td >获取当前登录状态改变的账号的信息</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >Reason</td>
      <td >获取登录状态变更原因。</td>
    </tr>
  </table>
</div>


### 消息/会话事件
**在线消息事件实体类 MessageEvent**
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">方法</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMessage()</td>
      <td >Message</td>
      <td >获取消息对象</td>
    </tr>
  </table>
</div>

</br>

**离线消息事件实体类 OfflineMessageEvent**  
***Since 2.1.0***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">方法</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取收到离线消息的会话对象</td>
    </tr>
    <tr >
      <td >getNewMessageList()</td>
      <td >List<Message></td>
      <td >获取收到的离线消息列表,包含了该会话此次离线收到的所有离线消息列表。其中也有可能包含自己发出去的消息。</td>
    </tr>
    <tr >
      <td >getOfflineMsgCnt()</td>
      <td >int</td>
      <td >获取此次事件中该会话的离线消息总数。</td>
    </tr>
  </table>
</div>

**会话刷新事件实体类 ConversationRefreshEvent**

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">方法</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取需要被刷新的会话对象</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >Reason</td>
      <td >获取事件发生的原因，包括消息漫游完成、会话信息更新等</td>
    </tr>
  </table>
</div>

**消息被对方撤回通知事件MessageRetractEvent**  
***Since 2.2.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >Conversation</td>
      <td >获取被撤回消息所属的会话对象</td>
    </tr>
    <tr >
      <td >getRetractedMessage()</td>
      <td >Message</td>
      <td >获取被撤回的message对象.  
      (注意!此时获取到的Message的MessageContent对象已经从撤回前的真正的消息内容变为了PromptContent类型的提示文字)</td>
    </tr>
  </table>
</div>

**消息未回执人数变更事件MessageReceiptStatusChangeEvent**  
***Since 2.3.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getConversation()</td>
      <td >`Conversation`</td>
      <td >获取未回执数变更的消息所属的会话对象</td>
    </tr>
    <tr >
      <td >getMessageReceiptMetas()</td>
      <td >`List<MessageReceiptMeta>`</td>
      <td >获取未回执数发生变化的消息的MessageReceiptMeta。其中包括了消息的serverMsg Id、当前的未回执人数、以及未回执人数更新的时间</td>
    </tr>
  </table>
</div>


### 群组事件
**群成员变化相关事件**  
群组成员变化相关事件因为sdk需要入库，所以sdk会将相关事件以消息事件的方式上抛，用户可以将群组中产生的成员变化事件理解成一条特殊的消息，其消息类型为eventNotification，例如：

```
  //用户在线期间，如果群组中发生了成员变化事件，sdk也会通过上抛MessageEvent的方式来通知上层
  public void onEvent(MessageEvent event) {
    Message msg = event.getMessage();
	//获取消息类型，如text voice image eventNotification等。
    switch (msg.getContentType()) {
      //处理事件提醒消息，此处message的contentType类型为eventNotification。
      case eventNotification:
        //获取事件发生的群的群信息
        GroupInfo groupInfo = (GroupInfo) msg.getTargetInfo();
        //获取事件具体的内容对象
        EventNotificationContent eventNotificationContent = (EventNotificationContent)msg.getContent();
        //获取事件具体类型
        switch (eventNotificationContent.getEventNotificationType()){ 
          case group_member_added:
          //群成员加群事件
          break;
          case group_member_removed:
          //群成员被踢事件
          break;
          case group_member_exit:
          //群成员退群事件
          break;
          case group_info_updated://since 2.2.1
          //群信息变更事件
          break;
          ...
        }
        break;
    }
  }

  //用户离线期间，如果群组中发生了成员变化事件，sdk也会通过上抛OfflineMessageEvent
  //的方式来通知上层，处理方式类似上面的MessageEvent
  public void onEvent(OfflineMessageEvent event) {
    List<Message> msgs = event.getOfflineMessageList();
    for (Message msg:msgs) {
       //...
    }
  }

```

**群成员审批事件GroupApprovalEvent**  
***Since 2.4.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getType()</td>
      <td >`Type`</td>
      <td >获取群成员审批通知事件类型，主动申请入群是`Type.apply_join_group`，邀请入群是`Type.invited_into_group`</td>
    </tr>
    <tr >
      <td >getFromUserInfo()</td>
      <td >`UserInfo`</td>
      <td >获取群成员审批事件发起方`UserInfo`，主动申请入群时是申请人`UserInfo`，邀请入群时是邀请人`UserInfo`</td>
    </tr>
    <tr >
      <td >getApprovalUserInfoList()</td>
      <td >`List<UserInfo>`</td>
      <td >获取需要审批入群的用户`UserInfo`</td>
    </tr>
	<tr >
	  <td>getApprovalUserCount()</td>
	  <td>`int`</td>
	  <td>获取需要审批入群的用户的人数</td>
	</tr>
    <tr >
      <td >getReason()</td>
      <td >`String`</td>
      <td >获取事件发生的理由，主动申请入群时是申请理由(可为null)，邀请入群时是null</td>
    </tr>
	<tr >
      <td >acceptGroupApproval()</td>
      <td >`void`</td>
      <td >入群审批同意,需要指定`username`，`appKey`</td>
    </tr>
	<tr >
      <td >refuseGroupApproval()</td>
      <td >`void`</td>
      <td >入群审批拒绝,需要指定`username`，`appKey`，`reason`(可为null)</td>
    </tr>
  </table>
</div>

**群成员审批拒绝事件GroupApprovalRefuseEvent**  
***Since 2.4.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getFromUserInfo()</td>
      <td >`UserInfo`</td>
      <td >获取事件发起方userInfo，在本事件中为群主信息</td>
    </tr>
    <tr >
      <td >getToUserInfoList()</td>
      <td >`List<UserInfo>`</td>
      <td >获取事件对象用户信息列表，在本事件中为被拒绝入群的用户`UserInfo`列表</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >`String`</td>
      <td >获取事件发生的理由, 在本事件中为群主审批拒绝的理由</td>
    </tr>
    <tr >
      <td >getGid()</td>
      <td >`long`</td>
      <td >返回实际群组Gid</td>
    </tr>
  </table>
</div>

**已审批事件通知GroupApprovedNotificationEvent**  
***Since 2.5.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getApprovalEventID()</td>
      <td >`long`</td>
      <td >获取对应的入群审批事件ID</td>
    </tr>
	<tr >
      <td >getApprovalResult()</td>
      <td >`boolean`</td>
      <td >获取入群审批结果</td>
    </tr>
    <tr >
      <td >getGroupID()</td>
      <td >`long`</td>
      <td >获取入群审批事件对应的群组ID</td>
    </tr>
	<tr >
      <td >getOperator()</td>
      <td >`UserInfo`</td>
      <td >获取该次入群审批的操作者用户信息</td>
    </tr>
    <tr >
      <td >getApprovedUserInfoList()</td>
      <td >`List<UserInfo>`</td>
      <td >获取已被审批过的用户信息，这些用户的入群审批已经被审批</td>
    </tr>
  </table>
</div>

**群成员昵称修改事件GroupMemNicknameChangedEvent**  
***Since 2.7.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getGroupID()</td>
      <td >`long`</td>
      <td >获取群组id</td>
    </tr>
	<tr >
      <td >getChangeEntities()</td>
      <td >`List<ChangeEntity>`</td>
      <td >获取昵称修改事件列表,按照时间升序排列</td>
    </tr>
  </table>
</div>

**群公告变更事件GroupAnnouncementChangedEvent**  
***Since 2.8.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getGroupID()</td>
      <td >`long`</td>
      <td >获取群组id</td>
    </tr>
	<tr >
      <td >getChangeEntities()</td>
      <td >`List<ChangeEntity>`</td>
      <td >获取公告变更事件列表，按照时间升序排列</td>
    </tr>
  </table>
</div>

**群黑名单变更事件GroupBlackListChangedEvent**  
***Since 2.8.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getGroupID()</td>
      <td >`long`</td>
      <td >获取群组id</td>
    </tr>
	<tr >
      <td >getChangeEntities()</td>
      <td >`List<ChangeEntity>`</td>
      <td >获取黑名单变更事件列表，按照时间升序排列</td>
    </tr>
  </table>
</div>



### 聊天室事件
**聊天室消息事件ChatRoomMessageEvent**  
***Since 2.4.0***
聊天室消息因为sdk不会入库，所以没有走正常的消息事件，而是单独的聊天室消息事件。注意和消息事件做区分
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMessages()</td>
      <td >`List<Message>`</td>
      <td >获取聊天室消息事件中包含的消息列表</td>
    </tr>
  </table>
</div>


**聊天室通知事件ChatRoomNotificationEvent**  
***Since 2.8.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getEventID()</td>
      <td >`long`</td>
      <td >获取事件ID</td>
    </tr>
	<tr >
      <td >getRoomID()</td>
      <td >`long`</td>
      <td >获取事件对应聊天室的房间ID</td>
    </tr>
	<tr >
      <td >getType()</td>
      <td >`Type`</td>
      <td >获取事件类型</td>
    </tr>
    <tr >
      <td >getOperator(GetUserInfoCallback callback)</td>
      <td >`void`</td>
      <td >获取事件操作者用户信息</td>
    </tr>
	<tr >
      <td >getTargetUserInfoList(GetUserInfoListCallback callback)</td>
      <td >`void`</td>
      <td >获取目标用户信息列表</td>
    </tr>
    <tr >
      <td >getCtime()</td>
      <td >`long`</td>
      <td >取事件发生时间，单位-毫秒</td>
    </tr>
  </table>
</div>



### 好友事件
**好友相关事件通知实体类ContactNotifyEvent**  
***Since 1.4.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getType()</td>
      <td >`Type`</td>
      <td >获取好友通知事件的具体类型。</td>
    </tr>
    <tr >
      <td >getReason()</td>
      <td >`String`</td>
      <td >获取事件发生的理由，该字段由对方发起请求时所填。</td>
    </tr>    
    <tr >
      <td >getFromUsername()</td>
      <td >`String`</td>
      <td >获取事件发起者用户的username</td>
    </tr>
    <tr >
      <td >getfromUserAppKey()</td>
      <td >`String`</td>
      <td >获取事件发起者用户所属应用的appKey</td>
    </tr>
  </table>
</div>

### 命令透传事件
**命令透传事件实体类CommandNotificationEvent**  
***Since 2.3.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getSenderUserInfo()</td>
      <td >`UserInfo`</td>
      <td >获取命令透传消息发送者的UserInfo</td>
    </tr>
    <tr >
      <td >getType()</td>
      <td >`Type`</td>
      <td >获取命令透传消息对象的类型，单聊是`Type.single`,群聊则是`Type.group`,如果是自己已登录设备间的命令透传则是`Type.self`</td>
    </tr>    
    <tr >
      <td >getTargetInfo()</td>
      <td >`Objcet`</td>
      <td >获取命令透传消息发送对象的Info。若对象是单聊用户则是`UserInfo`,对象是群组则是`GroupInfo`，使用时强制转型</td>
    </tr>
    <tr >
      <td >getMsg()</td>
      <td >`String`</td>
      <td >获取命令透传消息的实际内容</td>
    </tr>
  </table>
</div>


### 通知栏点击事件
**通知栏点击事件实体类NotificationClickEvent**

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="30px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getMessage()</td>
      <td >Message</td>
      <td >获取点击的通知所对应的消息对象</td>
    </tr>
  </table>
</div>



### 示例代码
接收消息事件
```Java
class MessageEventReceiver extends Activity {

  @Override
  protected void onCreate() {
    super.onCreate(savedInstanceState);
    //这里只是为了展示注册事件接受者接口的用法，实际上开发者可以在任意类中注册事件接收者
    //，而不仅仅在Activity中。 下同
    JMessageClient.registerEventReceiver(this);
  }

  @Override
  protected void onDestroy() {
    JMessageClient.unRegisterEventReceiver(this);
    super.onDestroy();
  }

  //用户在线期间收到的消息都会以MessageEvent的方式上抛
  public void onEvent(MessageEvent event) {
    Message msg = event.getMessage();

    switch (msg.getContentType()) {
      case text:
        //处理文字消息
        TextContent textContent = (TextContent) msg.getContent();
        textContent.getText();
        break;
      case image:
        //处理图片消息
        ImageContent imageContent = (ImageContent) msg.getContent();
        imageContent.getLocalPath();//图片本地地址
        imageContent.getLocalThumbnailPath();//图片对应缩略图的本地地址
         break;
      case voice:
        //处理语音消息
        VoiceContent voiceContent = (VoiceContent) msg.getContent();
        voiceContent.getLocalPath();//语音文件本地地址
        voiceContent.getDuration();//语音文件时长
        break;
      case custom:
        //处理自定义消息
        CustomContent customContent = (CustomContent) msg.getContent();
        customContent.getNumberValue("custom_num"); //获取自定义的值
        customContent.getBooleanValue("custom_boolean");
        customContent.getStringValue("custom_string");
        break;
      case eventNotification:
        //处理事件提醒消息
        EventNotificationContent eventNotificationContent = (EventNotificationContent)msg.getContent();
        switch (eventNotificationContent.getEventNotificationType()){
          case group_member_added:
          //群成员加群事件
          break;
          case group_member_removed:
          //群成员被踢事件
          break;
          case group_member_exit:
          //群成员退群事件
          break;
          case group_info_updated://since 2.2.1
          //群信息变更事件
          break;
        }
        break;
      case unknown:
        // 处理未知消息，未知消息的Content为PromptContent 默认提示文本为“当前版本不支持此类型消息，请更新sdk版本”，上层可选择不处理
        PromptContent promptContent = (PromptContent) msg.getContent();
        promptContent.getPromptType();//未知消息的type是unknown_msg_type
        promptContent.getPromptText();//提示文本，“当前版本不支持此类型消息，请更新sdk版本”
        break;
    }
  }
  
  //用户离线期间收到的消息会以OfflineMessageEvent的方式上抛，处理方式类似上面的
  //MessageEvent
  public void onEvent(OfflineMessageEvent event) {
    List<Message> msgs = event.getOfflineMessageList();
    for (Message msg:msgs) {
       //...
    }
  }
}
```

接收通知栏点击事件
```Java
class NotificationClickEvent extends Activity{
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
    public void onEvent(NotificationClickEvent event){
        Intent notificationIntent = new Intent(mContext, ChatActivity.class);
        mContext.startActivity(notificationIntent);//自定义跳转到指定页面
    }

}
```
用户登录状态变更事件
```
class UserLogoutEventReceiver extends Activity{
    @Override
    protected void onCreate() {
        super.onCreate(savedInstanceState);
        JMessageClient.registerEventReceiver(this);
    }
    @Override
    protected void onDestroy() {
        JMessageClient.unRegisterEventReceiver(this);
        super.onDestroy();``
    }
    public void onEvent(LoginStateChangeEvent event){
        LoginStateChangeEvent.Reason reason = event.getReason();//获取变更的原因
        UserInfo myInfo = event.getMyInfo();//获取当前被登出账号的信息
        switch (reason) {
            case user_password_change:
            	//用户密码在服务器端被修改
                break;
            case user_logout:
            	//用户换设备登录
                break;
            case user_deleted:
            	//用户被删除
                break;
        }
     }

}
```

