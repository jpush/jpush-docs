<h1>聊天室管理</h1>


## 概述

jmessage android sdk 从2.4.0版本开始提供聊天室功能，包括查询基本信息，加入聊天室，退出聊天室等。

**聊天室和群组的主要区别在于：**

+ 聊天室的消息没有推送通知和离线保存，也没有常驻成员的概念，只要进入聊天室即可接收消息，开始聊天。
一旦退出聊天室，不再会接收到任何消息、通知和提醒。  

+ 本地获取聊天室会话对象需要通过单独的接口  `JMessageClient.getChatRoomConversationList`或者  `JMessageClient.getChatRoomConversation`获取。  
`JMessageClient.getConversationList`接口不会返回聊天室的会话对象。 
 
+ 在线收到聊天室消息时，sdk仅仅只会将消息通过`ChatRoomMessageEvent`事件上抛，不会将消息落地。上层通过聊天室会话对象获取message时，sdk将返回空。  


<font color= SteelBlue>注意：进入聊天室会自动获取最近50条消息，通过`ChatRoomMessageEvent `事件上抛给应用层。客户端目前不支持创建聊天室</font>

### 聊天室信息对象
***Since 2.4.0***  
聊天室信息对象`ChatRoomInfo`
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="100px">方法</th>
      <th width="20px">类型</th>
      <th width="300px">说明</th>
    </tr>
    <tr >
      <td >getRoomID()</td>
      <td >`long`</td>
      <td >获取聊天室id</td>
    </tr>
    <tr >
      <td >getName()</td>
      <td >`String`</td>
      <td >获取聊天室名称</td>
    </tr>
    <tr >
      <td >getAppKey()</td>
      <td >`String`</td>
      <td >获取聊天室所属AppKey</td>
    </tr>
    <tr >
      <td >getOwnerInfo()</td>
      <td >`UserInfo`</td>
      <td >获取聊天室拥有者UserInfo</td>
    </tr>
	<tr >
      <td >getMaxMemberCount()</td>
      <td >`int`</td>
      <td >获取聊天室允许的最大成员数量</td>
    </tr>
	<tr >
      <td >getDescription()</td>
      <td >`String`</td>
      <td >获取聊天室描述</td>
    </tr>
	<tr >
      <td >getTotalMemberCount()</td>
      <td >`int`</td>
      <td >获取聊天室当前成员数量</td>
    </tr>
	<tr >
	  <td >getCreateTime()</td>
	  <td>`int`</td>
	  <td >获取聊天室创建时间 单位-秒</td>
	</tr>
  </table>
</div>

### 获取当前应用appkey所属下聊天室信息
***Since 2.4.0***
```
	/**
	 * 获取当前应用appkey所属下聊天室信息。
	 *
	 * @param start    起始位置
	 * @param count    获取个数
	 * @param callback 接口回调
	 * @since 2.4.0
	 */
	ChatRoomManager.getChatRoomListByApp(int start, int count, RequestCallback<List<ChatRoomInfo>> callback);
```

### 获取当前用户所加入的所有聊天室的信息
***Since 2.4.0***
```
	/**
	 * 获取当前用户所加入的所有聊天室的信息。
	 *
	 * @param callback 接口回调
	 * @since 2.4.0
	 */
	ChatRoomManager.getChatRoomListByUser(RequestCallback<List<ChatRoomInfo>> callback);
```

### 查询指定roomID的聊天室信息
***Since 2.4.0***
```
	/**
	 * 查询指定roomID的聊天室信息。
	 *
	 * @param roomIDs  待查询的roomID集合
	 * @param callback 接口回调
	 * @since 2.4.0
	 */
	ChatRoomManager.getChatRoomInfos(Set<Long> roomIDs, final RequestCallback<List<ChatRoomInfo>> callback);
```

### 进入聊天室
***Since 2.4.0***
```
    /**
     * 进入聊天室.
     * 用户只有成功调用此接口之后，才能收到聊天室消息，以及在此聊天室中发言。
     * 成功进入聊天室之后，会将聊天室中最近若干条聊天记录同步到本地并以{@link cn.jpush.im.android.api.event.ChatRoomMessageEvent}事件的形式通知到上层。
     *
     * @param roomID   聊天室的roomID
     * @param callback 接口回调
     * @since 2.4.0
     */
    ChatRoomManager.enterChatRoom(long roomID, final RequestCallback<Conversation> callback);
```

### 离开聊天室
***Since 2.4.0***
```
    /**
     * 离开聊天室.
     * 成功调用此接口之后，用户将能不在此聊天室收发消息。
     *
     * @param roomID   聊天室的roomID
     * @param callback 接口回调
     * @since 2.4.0
     */
    ChatRoomManager.leaveChatRoom(long roomID, final BasicCallback callback);
```
### 获取聊天室会话信息
***Since 2.4.0***
```
    /**
     * 获取聊天室会话信息
     *
     * @param roomID 群组的groupID
     * @return 返回会话信息，若不存在和指定对象的会话则返回null
     * @since 2.4.0
     */
    JMessageClient.getChatRoomConversation(long roomID);
```

### 从本地获取用户的聊天室会话列表
***Since 2.4.0***
```
    /**
     * 从本地数据库中获取包含所有的聊天室会话的列表
     *
     * @return 返回当前用户的聊天室会话列表，没有则返回空的列表
     * @since 2.4.0
     */
    JMessageClient.getChatRoomConversationList();
```

### 创建聊天室会话
***Since 2.4.0***
```
    /**
     * 创建聊天室会话，如果本地已存在对应会话，则不会重新创建，直接返回本地会话对象。
     *
     * @param roomID 聊天室的roomID
     * @return 会话对象
     * @since 2.4.0
     */
    Conversation.createChatRoomConversation(long roomID);
```

### 删除聊天室会话
***Since 2.4.0***
```
    /**
     * 删除聊天室会话，同时删除掉本地相关缓存文件
     *
     * @param roomID 聊天室roomID
     * @return 删除成功返回true, 否则返回false
     * @since 2.4.0
     */
    JMessageClient.deleteChatRoomConversation(long roomID);
```

### 聊天室消息事件
***Since 2.4.0***
```
ChatRoomMessageEvent
```
用户进入聊天室之后，收到聊天室消息时，sdk会主动上抛此事件通知上层，具体处理方法见[事件处理](./event)一节。

### 聊天室相关代码示例
```
// 获取当前应用appkey所属下聊天室信息
ChatRoomManager.getChatRoomListByApp(start, count, new RequestCallback<List<ChatRoomInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<ChatRoomInfo> chatRoomInfos) {
		String result = null != chatRoomInfos ? chatRoomInfos.toString() : null;
		postTextToDisplay("getChatRoomListByApp", responseCode, responseMessage, result);
	}
});

// 获取当前用户所加入的所有聊天室的信息
ChatRoomManager.getChatRoomListByUser(new RequestCallback<List<ChatRoomInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<ChatRoomInfo> chatRoomInfos) {
		String result = null != chatRoomInfos ? chatRoomInfos.toString() : null;
		postTextToDisplay("getChatRoomListByUser", responseCode, responseMessage, result);
	}
});

// 查询指定roomID的聊天室信息
ChatRoomManager.getChatRoomInfos(Collections.singleton(roomID), new RequestCallback<List<ChatRoomInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<ChatRoomInfo> chatRoomInfos) {
		String result = null != chatRoomInfos ? chatRoomInfos.toString() : null;
		postTextToDisplay("getChatRoomInfos", responseCode, responseMessage, result);
	}
});

// 进入聊天室
ChatRoomManager.enterChatRoom(roomID, new RequestCallback<Conversation>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, Conversation conversation) {
		String result = null != conversation ? conversation.toString() : null;
		postTextToDisplay("enterChatRoom", responseCode, responseMessage, result);
	}
});

// 离开聊天室
ChatRoomManager.leaveChatRoom(roomID, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		postTextToDisplay("leaveChatRoom", responseCode, responseMessage, null);
	}
});

// 发送聊天室消息
Conversation conv = JMessageClient.getChatRoomConversation(roomID);
if (null == conv) {
	conv = Conversation.createChatRoomConversation(roomID);
}
String text = etInputText.getText().toString();
final Message msg = conv.createSendTextMessage(text);//实际聊天室可以支持所有类型的消息发送，demo为了简便，仅仅实现了文本类型的消息发送，其他的消息类型参考消息发送相关文档
msg.setOnSendCompleteCallback(new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postMessageToDisplay("MessageSent", responseCode, responseMessage, msg);
		} else {
			postTextToDisplay("MessageSent", responseCode, responseMessage, "消息发送失败");
		}
	}
});
JMessageClient.sendMessage(msg);

// 接收聊天室消息
public void onEventMainThread(ChatRoomMessageEvent event) {
	Log.d("tag", "ChatRoomMessageEvent received .");
	List<Message> msgs = event.getMessages();
	for (Message msg : msgs) {
		//这个页面仅仅展示聊天室会话的消息
		postMessageToDisplay("MessageReceived", event.getResponseCode(), event.getResponseDesc(), msg);
	}
}
```


