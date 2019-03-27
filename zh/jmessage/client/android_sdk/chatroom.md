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

### 聊天室对象
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

### 获取应用下聊天室列表
***Since 2.4.0***
```
	/**
	 * 获取当前应用appkey所属下聊天室信息列表。
	 *
	 * @param start    起始位置
	 * @param count    获取个数
	 * @param callback 接口回调
	 * @since 2.4.0
	 */
	ChatRoomManager.getChatRoomListByApp(int start, int count, RequestCallback<List<ChatRoomInfo>> callback);
```

### 获取当前用户加入的聊天室列表
***Since 2.4.0***
```
	/**
	 * 获取当前用户所加入的所有聊天室的信息列表。
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
### 获取聊天室会话
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

### 聊天室消息
***Since 2.4.0***
```
ChatRoomMessageEvent
```
用户进入聊天室之后，收到聊天室消息时，sdk会主动上抛此事件通知上层，具体处理方法见[事件处理](./event)一节。

### 聊天室管理员
***Since 2.8.0***

#### 设置聊天室管理员
***Since 2.8.0***
```
    /**
     * 将指定用户设置为聊天室的房管,只有房主有此权限，房管可设置聊天室的黑名单
     *
     * @param roomID 聊天室的roomID
     * @param userInfos 准备设置为房管的用户UserInfo列表
     * @param callback 回调
     * @since 2.8.0
     */
    ChatRoomManager.addChatRoomAdmin(long roomID, List<UserInfo> userInfos, BasicCallback callback);
```

#### 取消聊天室管理员
***Since 2.8.0***
```
    /**
     * 取消指定用户的聊天室房管身份，只有房主有此权限
     *
     * @param roomID 聊天室的roomID
     * @param userInfos 准备取消房管的用户UserInfo列表
     * @param callback 回调
     * @since 2.8.0
     */
    ChatRoomManager.delChatRoomAdmin(long roomID, List<UserInfo> userInfos, BasicCallback callback);
```

#### 获取聊天室管理员用户列表
***Since 2.8.0***
```
    /**
     * 获取聊天室的房管用户列表
     *
     * @param roomID 聊天室的roomID
     * @param callback 回调
     * @since 2.8.0
     */
    ChatRoomManager.getChatRoomAdminList(long roomID, RequestCallback<List<UserInfo>> callback);
```

### 聊天室黑名单
***Since 2.8.0***

#### 将用户添加至聊天室黑名单
***Since 2.8.0***
```
    /**
     * 将用户添加至聊天室黑名单，只有聊天室的房主和房管有此权限, 被设置黑名单用户会被立即踢出聊天室。
     *
     * @param roomID 聊天室的roomID
     * @param userInfos 准备加入聊天室黑名单的用户userInfo集合
     * @param callback
     * @since 2.8.0
     */
    ChatRooomManager.addChatRoomBlacklist(long roomID, List<UserInfo> userInfos, BasicCallback callback);
```

####  将用户从聊天室黑名单中移除
***Since 2.8.0***
```
    /**
     * 将用户从聊天室黑名单中移除，只有聊天室的房主和房管有此权限
     *
     * @param roomID 聊天室的roomID
     * @param userInfos 准备移出聊天室黑名单的用户userInfo集合
     * @param callback 回调
     * @since 2.8.0
     */
    ChatRooomManager.delChatRoomBlacklist(long roomID, List<UserInfo> userInfos, BasicCallback callback);
```

#### 获取聊天室的黑名单用户列表
***Since 2.8.0***
```
    /**
     * 获取聊天室的黑名单用户列表,按照被拉黑时间倒序排列
     *
     * @param roomID 聊天室的roomID
     * @param callback 回调
     * @since 2.8.0
     */
    ChatRoomManager.getChatRoomBlacklist(long roomID, RequestCallback<List<UserInfo>> callback);
```

### 聊天室禁言
***Since 2.8.2***  
聊天室owner或者管理员可以禁言聊天室成员

#### 将指定用户添加进聊天室的禁言列表
```
    /**
     * 将指定用户添加进聊天室的禁言列表(批量设置一次最多500个)，禁言时间下限5分钟，上限1年
     * 聊天室owner或者管理员可以禁言聊天室成员，管理员或owner不能被禁言, 重复调用此接口将根据当前时间重新计算结束时间。
     * 禁言成功聊天室成员会收到{@link cn.jpush.im.android.api.event.ChatRoomNotificationEvent}
     *
     * @param roomId 聊天室的roomId
     * @param userInfos 准备加入聊天室禁言名单的用户
     * @param times 禁言时间，单位：毫秒,禁言时间最少5分钟（300000毫秒），最长一年（31536000000毫秒) 即300000 <= times <= 31536000000
     * @param callback 禁言结果回调
     * @since 2.8.2
     */
    ChatRoomManager.addChatRoomSilence(long roomId, Collection<UserInfo> userInfos, long times, BasicCallback callback);
```

#### 将指定用户从聊天室禁言列表中移除
```
    /**
     * 将指定用户从聊天室禁言名单中移除(批量设置一次最多500个)
     * 只有房主和管理员可设置,取消成功聊天室成员会收到{@link cn.jpush.im.android.api.event.ChatRoomNotificationEvent}
     *
     * @param roomId 聊天室的roomId
     * @param userInfos 将要被解除禁言的用户信息，size <= 500
     * @param callback 解除禁言结果回调
     * @since 2.8.2
     */
    ChatRoomManager.delChatRoomSilence(long roomId, Collection<UserInfo> userInfos, BasicCallback callback);
```

#### 获取聊天室禁言列表
```
	/**
	 * 获取聊天室禁言列表以添加入禁言的先后的时间倒序排序（后加入的在前），从start位置开始获取count个禁言信息。
	 * 例如总共20个被禁言，分页每次获取15人，第一次获取 start: 0, count : 15,返回15个人的禁言信息，第二次获取 start : 15, count : 15 返回5个人的禁言信息。
	 * 禁言用户总数在回调中会返回。
	 *
	 * @param roomId 聊天室的roomId
	 * @param start 获取禁言列表开始位置，从第 start 个开始，start >= 0
	 * @param count 获取禁言信息数量, count > 0
	 * @param callback 结果回调{@link GetChatRoomSilencesCallback}
	 * @since 2.8.2
	 */
	ChatRoomManager.getChatRoomSilencesFromNewest(long roomId, int start, int count, GetChatRoomSilencesCallback callback);
```

#### 查询用户在聊天室的禁言状态
```
    /**
     * 获取用户在聊天室的禁言状态，如果用户未处于禁言状态，回调中SilenceInfo为null
     *
     * @param roomId 聊天室的roomId
     * @param username 用户名
     * @param appkey 用户所在应用 AppKey，不填这默认本应用
     * @param callback 结果回调, 如果用户未处于禁言状态，回调中SilenceInfo为null
     * @since 2.8.2
     */
    ChatRoomManager.getChatRoomMemberSilence(final long roomId, String username, String appkey, final RequestCallback<SilenceInfo> callback);
```

### 聊天室通知事件
聊天室管理员和黑名单，禁言列表变更时会下发此事件
***Since 2.8.0***
```
ChatRoomNotificationEvent
```

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

// 设置聊天室管理员
ChatRoomManager.addChatRoomAdmin(roomID, Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postTextToDisplay("addChatRoomAdmin", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("addChatRoomAdmin", responseCode, responseMessage, "设置房管失败");
		}
	}
});

// 取消聊天室管理员
ChatRoomManager.delChatRoomAdmin(roomID, Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postTextToDisplay("delChatRoomAdmin", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("delChatRoomAdmin", responseCode, responseMessage, "取消房管失败");
		}
	}
});

// 获取聊天室管理员用户列表
ChatRoomManager.getChatRoomAdminList(roomID, new RequestCallback<List<UserInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<UserInfo> result) {
		if (0 == responseCode) {
			StringBuilder builder = new StringBuilder();
			if (result.size() > 0) {
				for (UserInfo userInfo : result) {
					builder.append(userInfo.getUserName()).append("\n");
				}
			} else {
				builder.append("该聊天室还没有房管");
			}
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, builder.toString());
		} else {
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, "获取聊天室房管列表失败");
		}
	}
});

//  将用户添加至聊天室黑名单
ChatRoomManager.addChatRoomBlacklist(roomID, Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postTextToDisplay("addChatRoomBlacklist", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("addChatRoomBlacklist", responseCode, responseMessage, "添加聊天室黑名单失败");
		}
	}
});

// 将用户从聊天室黑名单中移除
ChatRoomManager.delChatRoomBlacklist(roomID, Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0== responseCode) {
			postTextToDisplay("delChatRoomBlacklist", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("delChatRoomBlacklist", responseCode, responseMessage, "从黑名单中移除失败");
		}
	}
});

// 获取聊天室的黑名单用户列表
ChatRoomManager.getChatRoomBlacklist(roomID, new RequestCallback<List<UserInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<UserInfo> result) {
		if (0 == responseCode) {
			StringBuilder builder = new StringBuilder();
			if (result.size() > 0) {
				for (UserInfo userInfo : result) {
					builder.append(userInfo.getUserName()).append("\n");
				}
			} else {
				builder.append("该聊天室黑名单列表为空");
			}
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, builder.toString());
		} else {
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, "获取聊天室黑名单列表失败");
		}
	}
});

// 将指定用户添加进聊天室的禁言列表
ChatRoomManager.addChatRoomSilence(roomId, Collections.singletonList(info), times, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postTextToDisplay("addChatRoomSilence", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("addChatRoomSilence", responseCode, responseMessage, "设置禁言失败");
		}
	}
});

// 将指定用户从聊天室禁言名单中移除
ChatRoomManager.delChatRoomSilence(roomId, Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			postTextToDisplay("delChatRoomSilence", responseCode, responseMessage, null);
		} else {
			postTextToDisplay("delChatRoomSilence", responseCode, responseMessage, "设置禁言失败");
		}
	}
});

// 获取聊天室禁言列表
ChatRoomManager.getChatRoomSilencesFromNewest(roomID, silenceStart, silenceCount, new GetChatRoomSilencesCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<SilenceInfo> silenceInfos, int total) {
		if (0 == responseCode) {
			StringBuilder builder = new StringBuilder();
			builder.append("聊天室禁言总量:").append(total).append(",本次获取到数量:")
					.append(silenceInfos.size()).append("\n");
			if (silenceInfos.size() > 0) {
				for (SilenceInfo silenceInfo : silenceInfos) {
					builder.append("username:").append(silenceInfo.getUserInfo().getUserName()).append("\n");
					builder.append("silenceStart:").append(silenceInfo.getSilenceStartTime()).append("\n");
					builder.append("silenceEnd:").append(silenceInfo.getSilenceEndTime()).append("\n\n");
				}
			}
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, builder.toString());
		} else {
			postTextToDisplay("getChatRoomAdminList", responseCode, responseMessage, "获取禁言列表失败");
		}
	}
});

// 查询用户在聊天室的禁言状态
ChatRoomManager.getChatRoomMemberSilence(roomID, username, appkey, new RequestCallback<SilenceInfo>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, SilenceInfo result) {
		if (0 == responseCode) {
			StringBuilder builder = new StringBuilder();
			if (result != null) {
				builder.append("usname:").append(result.getUserInfo().getUserName()).append("\n");
				builder.append("silenceStart:").append(result.getSilenceStartTime()).append("\n");
				builder.append("silenceEnd:").append(result.getSilenceEndTime()).append("\n");
			} else {
				builder.append("该用户没有被禁言");
			}
			postTextToDisplay("getChatRoomMemberSilence", responseCode, responseMessage, builder.toString());
		} else {
			postTextToDisplay("getChatRoomMemberSilence", responseCode, responseMessage, "获取用户禁言状态失败");
		}
	}
});
```


