<h1>群组管理</h1>

## 概述

把多个 username 加入到同一个群组内，在群组内发送群组消息。

- 创建私有群组、创建公开群组（2.4.0版本新增[公开群组](#PublicGroup)）
- 加入，退出群组；
- 加群组成员、移除群组成员；
- 群组管理员
- 申请加入和审批
- 禁言、消息屏蔽
- 群@功能



### 创建群组

群组分为私有群组、公开群组。

- 私有群组无法申请加入，群内成员邀请即可加入。
- 公开群组可通过获取公开群组列表获取。
- 公开群组可通过发起加入申请，群主或管理员审核通过的方式加入。
- 公开群组群主或管理员直接邀请即可加入，群成员邀请入群需群主或管理员审批。

#### 创建私有群组

```
JMessageClient.createGroup(String groupName, String groupDesc, CreateGroupCallback callback);

@since 2.3.0
JMessageClient.createGroup(String groupName, String groupDesc, File groupAvatarFile, String format, CreateGroupCallback callback);
```  
参数说明

+ String groupName 群名称
+ String groupDesc 群描述
+ File groupAvatarFile 群头像文件
+ String format 头像文件扩展名，注意名称中不要包括"."
+ CreateGroupCallback callback 结果回调

回调
```
  public abstract void gotResult(int responseCode, String responseMsg, long groupId);
```  
+ long groupId 新创建成功的群组ID（resopnseCode = 0 时）。

#### <span id="PublicGroup">创建公开群组</span>
***Since 2.4.0***  
2.4.0版本新增公开群组类型。公开群组可通过入群申请，经群主或管理员审核通过的方式加入。公开群组群主或管理员直接邀请即可加入。群成员邀请入群需群主或管理员审批
。
  
```
    /**
     * 创建公开群组, 群组创建成功后，创建者会默认包含在群成员中。
     * 公开群组与私有群组的区别是公开群组只有群主和管理员邀请入群才能直接入群，群内其他人员邀请他人入群需要经过群主或管理员审批，
     * 管理员相关见{@link GroupInfo#addGroupKeeper(List, BasicCallback)}, 同时公开群组支持申请入群操作{@link JMessageClient#applyJoinGroup(long, String, BasicCallback)},
     * 申请入群时也需要群主或管理员审批, 需要审批入群时群主和管理员会收到{@link cn.jpush.im.android.api.event.GroupApprovalEvent}事件
     * 通过{@link GroupInfo#getGroupType()}得到群组类型
     *
     * @param groupName 群组名称
     * @param groupDesc 群组描述
     * @param callback  回调接口
     * @since 2.4.0
     */
    JMessageClient.createPublicGroup(String groupName, String groupDesc,
                                             CreateGroupCallback callback);
	
    /**
     * 创建公开群组，群组创建成功后，创建者会默认包含在群成员中。
     * 公开群组定义参考{@link JMessageClient#createPublicGroup(String, String, CreateGroupCallback)}
     * 使用此接口创建群组时可以指定群头像,并且可以指定头像文件在后台存储时的扩展名，如果填空或者不填，则后台存储文件时将没有扩展名。
     *
     * @param groupName       群组名称
     * @param groupDesc       群组描述
     * @param groupAvatarFile 群组头像文件
     * @param format          头像文件扩展名，注意名称中不要包括"."
     * @param callback        回调接口
     * @since 2.4.0
     */
    JMessageClient.createPublicGroup(final String groupName, final String groupDesc, final File groupAvatarFile, String format,
                                             final CreateGroupCallback callback);
```

### 解散群组
***Since 2.5.0***

```
    /**
     * 解散指定的群组，只有群的群主有权限解散。
     * 群组解散后会以message的形式通知到群内所有成员，类型为{@link cn.jpush.im.android.api.content.EventNotificationContent.EventNotificationType#group_dissolved}
     *
     * @param groupID 群组id
     * @param callback 回调
     * @since 2.5.0
     */
    JMessageClient.adminDissolveGroup(long groupID, BasicCallback callback);
```

### 群组信息
#### 获取群组列表
```
JMessageClient.getGroupIDList(GetGroupIDListCallback callback)
```
回调
```
public abstract void gotResult(int responseCode, String responseMessage,
            List<Long> groupIDList)
```
+ `List<Long>` groupIDList  当前用户所加入的群组的groupID的list

#### 获取公开群组列表
***Since 2.4.1***

可获取指定[appkey](../../guideline/faq/#getappkey)所属下公开群组基本信息

```
    /**
     * 获取指定应用appKey所属下公开群组基本信息, 如果appKey为空则默认使用本应用appKey.
     * 公开群组定义见{@link JMessageClient#createPublicGroup(String, String, CreateGroupCallback)}，
     * 群基本信息定义见{@link GroupBasicInfo}
     *
     * @param appKey   指定应用的appKey
     * @param start    起始位置
     * @param count    获取个数
     * @param callback 接口回调
     * @since 2.4.1
     */
    JMessageClient.getPublicGroupListByApp(String appKey, int start, int count, RequestCallback<List<GroupBasicInfo>> callback);
```

**代码示例**

```
//获取指定应用下所有公开群组
JMessageClient.getPublicGroupListByApp(appkey, start, count, new RequestCallback<List<GroupBasicInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<GroupBasicInfo> groupBasicInfos) {
		if (responseCode == 0) {
			String result = "";
			for (GroupBasicInfo groupBasicInfo : groupBasicInfos) {
				result += "GroupID: " + groupBasicInfo.getGroupID() + ", GroupType: " + groupBasicInfo.getGroupType() +
						", GroupName: " + groupBasicInfo.getGroupName() + ", GroupDescription: " + groupBasicInfo.getGroupDescription() +
						", GroupAvatarMediaID: " + groupBasicInfo.getAvatar() + ", GroupMaxMemberCount: " + groupBasicInfo.getMaxMemberCount()+ "\n\n";
			}
			tvDisplay.setText(result);
			tvDisplay.post(new Runnable() {
				@Override
				public void run() {
					scrollView.fullScroll(ScrollView.FOCUS_DOWN);
				}
			});
		} else {
			tvDisplay.setText("获取失败!\nresponseCode:" + responseCode + "\nresponseMsg" + responseMessage);
		}
	}
});
```

#### 获取群组信息
```
JMessageClient.getGroupInfo(long groupId, GetGroupInfoCallback callback)
```
参数说明

+ long groupId 群ID
+ GetGroupInfoCallback callback 结果回调

回调
```
  public void gotResult(int responseCode, String responseMessage, GroupInfo groupInfo)
```
+ GroupInfo groupInfo 返回的群组信息对象

#### 更新群组名称
```
groupInfo.updateName(String groupName, BasicCallback callback);
```
参数说明

+ String groupName 新的名称
+ BasicCallback callback 结果回调

#### 更新群组描述
```
groupInfo.updateDescription(String groupDesc, BasicCallback callback);
```
参数说明

+ String groupName 新的群组详情描述
+ BasicCallback callback 结果回调

#### 更新群组头像
**Since 2.3.0**

```
groupInfo.updateAvatar(File avatar, String format, BasicCallback callback);
```
参数说明

+ File avatar 群头像文件
+ String format 文件扩展名，注意名称中不要包含“.”
+ BasicCallback callback 结果回调

#### 修改群组类型
***Since 2.6.1***

```
groupInfo.changeGroupType(Type type, BasicCallback callback);
```
参数说明

+ Type type 群组类型
+ BasicCallback callback 结果回调

### 群成员信息
#### 获取群组成员列表
```
JMessageClient.getGroupMembers(long groupID,
      RequestCallback<List<GroupMemberInfo>> callback)
```
参数说明

+ long groupId 群组ID
+ RequestCallback callback

回调

```
  public void gotResult(int responseCode, String responseMessage, List<GroupMemberInfo> members);
```  
+ List GroupMemberInfos 成员列表(GroupMemberInfo)。

#### 群成员信息
群成员信息实体类 GroupMemberInfo  
***Since 2.7.0***
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">方法</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >getType()</td>
      <td >Type</td>
      <td >获取群成员类别：群主，群管理员，普通群成员</td>
    </tr>
    <tr >
      <td >isKeepSilence()</td>
      <td >boolean</td>
      <td >群成员在群内是否被禁言 true被禁言，false没有被禁言</td>
    </tr>
    <tr >
      <td >getUserInfo()</td>
      <td >UserInfo</td>
      <td >获取群成员对应的用户信息</td>
    </tr>
    <tr >
      <td >getNickName()</td>
      <td >String</td>
      <td >获取群成员昵称</td>
    </tr>
	<tr >
      <td >getDisplayName()</td>
      <td >String</td>
      <td >获取群成员在群内的展示名，展示名返回优先级为：群昵称>备注名>用户昵称>用户名</td>
    </tr>
    <tr >
      <td >getJoinGroupTime()</td>
      <td >long</td>
      <td >获取入群时间，单位豪秒</td>
    </tr>
  </table>
</div>

#### 设置群成员昵称
***Since 2.7.0***

```
    /**
     * 修改群成员昵称,群成员仅能修改自己在此群的昵称，管理员或群主修改任何普通群成员在此群的昵称，群成员类型见{@link GroupMemberInfo#type}
     *
     * @param username 群成员用户名
     * @param appKey 群成员appKey,传入空则默认使用本应用appKey
     * @param nickName 昵称
     * @param callback 结果回调
     * @since 2.7.0
     */
    groupInfo.setMemNickname(String username, String appKey, String nickName, BasicCallback callback);
```


### 群成员管理
#### 添加群组成员
```
JMessageClient.addGroupMembers(long groupID, String appKey, List<String> userNameList, BasicCallback callback)
```  
参数说明

+ long groupId 待加群的群组ID。创建群组时返回的。
+ String appkey 被添加的群成员所属的appkey，不填则默认为本应用appkey
+ List usernameList 群组成员列表，使用成员 username。
+ BasicCallback callback 结果回调


#### 添加群组成员,附带reason参数，注意只对[公开群组](#PublicGroup)有效
***Since 2.6.1***

```
JMessageClient.addGroupMembers(final long groupID, final String appKey, final List<String> userNameList, final String reason, final BasicCallback callback);
```
参数说明

+ long groupId 待加群的群组ID。创建群组时返回的。
+ String appkey 被添加的群成员所属的appkey，不填则默认为本应用appkey
+ List usernameList 群组成员列表，使用成员 username。
+ String reason 公开群组邀请人入群的理由
+ BasicCallback callback 结果回调

#### 移除群组成员
```
JMessageClient.removeGroupMembers(long groupId, String appKey, List<String> usernameList, BasicCallback callback);
```
参数说明

+ long groupId 待删除成员的群ID。
+ String appkey 被移除的群成员所属的appkey，不填则默认为本应用appkey
+ List usernameList 待删除的成员列表。
+ BasicCallback callback 结果回调。

#### 移交群主
***Since 2.5.0***

```
    /**
     * 移交群主,将群主移交給指定群内成员,移交群主后原群主成为普通群成员.<br/>
     * 移交群主成功后群内所有成员会收到群主变更事件，SDK收到事件会以类型为{@link cn.jpush.im.android.api.content.EventNotificationContent.EventNotificationType#group_owner_changed}
     * 的消息事件方式上报
     *
     * @param username 待移交者用户名
     * @param appKey 待移交者appKey, 若传入空则默认使用本应用appKey
     * @since 2.5.0
     */
    groupInfo.changeGroupAdmin(String username, String appKey, BasicCallback callback);
```

#### 退出群组
```
JMessageClient.exitGroup(long groupId, BasicCallback callback);
```
参数说明

+ long groupId 待退出的群ID。
+ BasicCallback callback 结果回调。

### 群组管理员
***Since 2.5.0***  
2.5.0版本新增群组管理员。管理员可以移除、禁言普通群成员，并且在公开群组里可以直接添加群成员和审核入群审批。群主可以添加、取消管理员并且移除或禁言管理员。
#### 添加群管理员
***Since 2.5.0*** 

```
    /**
     * 添加群管理员
     *
     * @param userInfos 群成员UserInfo列表
     * @param callback 回调
     * @since 2.5.0
     */
    groupInfo.addGroupKeeper(List<UserInfo> userInfos, BasicCallback callback);
```

#### 取消管理员
***Since 2.5.0***

```
    /**
     * 取消群管理员，管理员角色描述详见官方文档<a href="https://docs.jiguang.cn/jmessage/client/im_sdk_android/">群组管理员<a/>
     *
     * @param userInfos 群成员UserInfo列表
     * @param callback 回调
     * @since 2.5.0
     */
    groupInfo.removeGroupKeeper(List<UserInfo> userInfos, BasicCallback callback);
```

#### 获取管理员列表
***Since 2.5.0***

```
    /**
     * 获取群管理员列表, 返回群内管理员的成员信息列表，管理员角色描述详见官方文档<a href="https://docs.jiguang.cn/jmessage/client/im_sdk_android/">群组管理员<a/>
     *
     * @return 管理员的成员信息列表
     * @since 2.5.0
	 * @deprecated deprecated in jmessage 2.7.0 use{@link #getGroupKeeperMemberInfos()}instead
     */
    groupInfo.getGroupKeepers();

    /**
     * 获取群管理员列表, 返回群内管理员的成员{@link GroupMemberInfo}列表
     *
     * @return 管理员的成员GroupMemberInfo列表
     * @since 2.7.0
     */
    groupInfo.getGroupKeeperMemberInfos();
```
**代码示例**

```
//添加管理员
groupInfo.addGroupKeeper(userInfos, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (responseCode == 0) {
			Toast.makeText(getApplicationContext(), "添加管理员成功", Toast.LENGTH_SHORT).show();
		} else {
			Toast.makeText(getApplicationContext(), "添加管理员失败", Toast.LENGTH_SHORT).show();
			mTvGroupKeeper.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

//取消管理员
groupInfo.removeGroupKeeper(userInfos, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (responseCode == 0) {
			Toast.makeText(getApplicationContext(), "取消管理员成功", Toast.LENGTH_SHORT).show();
		} else {
			Toast.makeText(getApplicationContext(), "取消管理员失败", Toast.LENGTH_SHORT).show();
			mTvGroupKeeper.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

//获取管理员列表
List<GroupMemberInfo> memberInfos = groupInfo.getGroupKeeperMemberInfos();
String result = "这里只展示username:";
for (GroupMemberInfo memberInfo : memberInfos) {
	if (memberInfo != null) {
		result += "\n" + memberInfo.getUserInfo().getUserName();
	}
}
mTvGroupKeeper.setText(result);
```

### 群消息屏蔽
群组被设置为屏蔽之后，将收不到该群的消息。但是群成员变化事件还是能正常收到  
***Since 2.1.0***
#### 设置群消息屏蔽
```
groupinfo.setBlockGroupMessage(int blocked, BasicCallback callback)
```
参数说明

+ int blocked 是否屏蔽群消息。 1 - 屏蔽，0 - 取消屏蔽
+ BasicCallback callback 结果回调。

#### 判断群组是否被屏蔽
```
groupinfo.isGroupBlocked();
```
返回

+ int 1 - 已被屏蔽，0 - 未被屏蔽

#### 获取当前用户的群屏蔽列表
```
JMessageClient.getBlockedGroupsList(GetGroupInfoListCallback callback)
```
参数说明

+ GetGroupInfoListCallback callback 结果回调。

### 群组@功能
消息发送方可以发一条带有@list的消息。  
接收方收到带有@list的消息之后，如果@list中包含了自己，或者是@全体成员，则在sdk默认弹出的通知栏提示中会有相应的提示，如"xxx在群中@了你"。  
#### 创建@群成员的消息
***Since 2.1.0***  

```
conversation.createSendMessage(MessageContent content, List<UserInfo> atList, String customFromName)
```
参数说明

+ MessageContent content 消息内容对象
+ List<UserInfo> atList 被@用户的userInfo list
+ String customFromName 自定义fromName

返回

+ Message 消息对象。

#### 创建@全体群成员的消息
***Since 2.2.0***  

```
conversation.createSendMessageAtAllMember(MessageContent content, String customFromName)
```
参数说明

+ MessageContent content 消息内容对象
+ String customFromName 自定义fromName

返回

+ Message 一条包含@全体成员信息的消息对象。

#### 判断消息是否@了自己
***Since 2.1.0***  

```
message.isAtMe()
```
返回

+ boolean true - atList中包含了自己， false - atList中不包含自己

#### 判断消息是否是@全体成员
***Since 2.2.0***  

```
message.isAtAll()
```
返回

+ boolean true - 是@全体成员， false - 不是@全体成员

#### 获取消息中@的群成员列表
***Since 2.1.0***  

```
message.getAtUserList(GetUserInfoListCallback callback)
```
参数说明

+ GetUserInfoListCallback callback 获取用户列表的回调接口。注意当这条消息是一条@全体成员的消息时，此接口将返回空。

#### 代码示例

``` java
	//消息发送方
    Conversation conv = Conversation.createGroupConversation(gid);
    GroupInfo groupInfo = (GroupInfo) conv.getTargetInfo();
    List<UserInfo> atList = new ArrayList<UserInfo>();
    atList.add(groupInfo.getGroupMember("user1", appkey).getUserInfo());//获取到被@的群成员的userinfo，并填充到atList中去。
    atList.add(groupInfo.getGroupMember("user2", appkey).getUserInfo());
    
    //创建一条带有atList的消息。
    Message msg = conv.createSendMessage(new TextContent("a message with atList!"), atList, null);
    JMessageClient.sendMessage(msg);//发送消息



	//消息接收方
	public void onEvent(MessageEvent event){
		Message msg = event.getMessage();//收到消息事件，从消息事件中拿到消息对象
		msg.isAtMe(); //判断这条消息是否@了我
		
		//获取消息中包含的完整的atList
		msg.getAtUserList(new GetUserInfoListCallback() {
		    @Override
		    public void gotResult(int responseCode, String responseMessage, List<UserInfo> userInfoList) {
		        if(responseCode == 0){
		        	//获取atList成功
		        }else{
		        	//获取atList失败
		        }
		    }
      });
	}
```


### 入群申请和审批
申请入群和审批，适用于[公开群组](#PublicGroup)。
#### 申请入群
***Since 2.4.0***  

```
    /**
     * 申请加入群组，只有公开群组(公开群组定义参考{@link JMessageClient#createPublicGroup(String, String, CreateGroupCallback)}),
     * 才能发送入群申请
     *
     * @param groupID  申请加入群组的gid
     * @param reason   申请理由，可为null
     * @param callback
     * @since 2.4.0
     */
    JMessageClient.applyJoinGroup(long groupID, String reason, BasicCallback callback);
```

#### <span id="GroupApprovalEvent">群成员审批事件</span>
***Since 2.4.0***  

```
GroupApprovalEvent
```
群成员审批事件，收到群成员审批通知时，sdk将会抛出此事件通知上层。
具体处理方法见[事件处理](./event)一节。

####<span id="GroupApprovedNotificationEvent">已审批事件通知</span>
***Since 2.5.0***

```
GroupApprovedNotificationEvent
```
群成员审批事件已经被审批通知事件，当有一个群管理员或群主审批过群成员审批事件，sdk将会抛出此事件通知上层,
只有该审批事件对应群的群主和群管理员会收到此事件。具体处理方法见[事件处理](./event)一节

#### 入群审批
***Since 2.4.0***  
通过接收到的[群成员审批事件](#GroupApprovalEvent)进行审批操作,审批不能多人操作，当一人同意或拒绝后其他管理者或群主收到[已审批事件通知](#GroupApprovedNotificationEvent)

```
	/**
	 * 入群审批同意，操作成功后，群内所有成员包括被审批人自己都会收到一个包含群成员变化的EventNotification类型的消息
	 *
	 * @param username 被同意加入群组用户的username
	 * @param appKey 被同意入群者的appKey，若传入空则默认使用本应用的appKey
	 * @param callback 操作结果回调
	 */
	groupApprovalEvent.acceptGroupApproval(String username, String appKey, final BasicCallback callback);

	/**
	 * 入群审批拒绝，操作成功后，该次审批请求的发起方(Type为{@link Type#apply_join_group}时是申请人 Type为{@link Type#invited_into_group}时是邀请人)
	 * 会收到一个审批拒绝通知事件{@link GroupApprovalRefuseEvent}
	 *
	 * @param username 被拒绝加入群组用户的username
	 * @param appKey 被拒绝入群者的appKey, 若传入空则默认使用本应用的appKey
	 * @param reason 拒绝理由，可填null
	 * @param callback 操作结果回调
	 */
	groupApprovalEvent.refuseGroupApproval(String username, String appKey, String reason, BasicCallback callback);
```

#### 入群审批审批事件批量同意
***Since 2.6.1***

```

    /**
     * 批量同意审批事件内所有成员进群.
     * <p>
     * 操作成功后，事件GroupApprovalEvent对象内包含的所有待审批的用户都会被批准入群。之后，
     * 群内所有成员包括被审批人自己都会收到一个包含群成员变化的EventNotification类型的消息
     *
     * @param events     待处理的事件对象集合
     * @param sendNotify 预留字段，暂时无用
     * @param callback   操作结果回调
     * @since 2.6.1
     */
    GroupApprovalEvent.acceptGroupApprovalInBatch(Collection<GroupApprovalEvent> events, boolean sendNotify, BasicCallback callback);
```

#### 群成员审批拒绝事件
***Since 2.4.0***  

```
GroupApprovalRefuseEvent
```
群成员审批拒绝通知事件，收到群成员审批拒绝通知时，sdk将会抛出此事件通知上层，具体处理方法见[事件处理](./event)一节

#### 入群审批代码示例：

```
//申请入群
JMessageClient.applyJoinGroup(Long.parseLong(mEt_groupID.getText().toString()), reason, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		mProgressDialog.dismiss();
		if (responseCode == 0) {
			Toast.makeText(ApplyJoinGroupActivity.this, "申请成功", Toast.LENGTH_SHORT).show();
		} else {
			Log.d(TAG, "apply failed. code :" + responseCode + " msg : " + responseMessage);
			Toast.makeText(ApplyJoinGroupActivity.this, "申请失败", Toast.LENGTH_SHORT).show();
		}
	}
});

//入群审批
event.acceptGroupApproval(username, appKey, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			Toast.makeText(getApplicationContext(), "添加成功", Toast.LENGTH_SHORT).show();
		} else {
			Log.i(TAG, "acceptApplyJoinGroup failed,"+ " code = " + responseCode + ";msg = " + responseMessage);
			Toast.makeText(getApplicationContext(), "添加失败", Toast.LENGTH_SHORT).show();
		}
	}
}); //入群审批同意

event.refuseGroupApproval(username, appKey, reason, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (0 == responseCode) {
			Toast.makeText(getApplicationContext(), "拒绝成功", Toast.LENGTH_SHORT).show();
		} else {
			Log.i(TAG, "refuseApplyJoinGroup failed,"+ " code = " + responseCode + ";msg = " + responseMessage);
			Toast.makeText(getApplicationContext(), "拒绝失败", Toast.LENGTH_SHORT).show();
		}
	}
}); //入群审批拒绝

GroupApprovalEvent.acceptGroupApprovalInBatch(events, false, new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		textView.append("批量审批请求发送完成。 responseCode = " + responseCode + " responseMessage = " + responseMessage + "\n");
		scrollView.fullScroll(ScrollView.FOCUS_DOWN);
		events.clear();
	}
}); // 入群审批批量同意

```

### 群成员禁言
***Since 2.4.0***  
2.4.0版本新增群成员禁言状态设置,禁言后用户可正常接收消息，但无法向被禁言的群组中发送消息，解禁后可正常发送消息。
#### 群成员禁言状态设置
***Since 2.4.0***

```
	/**
	 * 群成员禁言状态设置,禁言后用户可正常接收消息，但无法向被禁言的群组中发送消息
	 * 解禁后可正常发送消息,禁言状态设置成功后群内所有成员将会收到群禁言通知事件
	 * sdk收到群禁言通知事件后会以类型为{@link cn.jpush.im.android.api.enums.ContentType#eventNotification}
	 * 的消息事件方式上报
	 *
	 * @param username 待设置群成员的username
	 * @param appKey 待设置群成员的appKey，传入空则默认使用本应用appKey
	 * @param keepSilence //true 设置禁言， false 取消禁言
	 * @param callback
	 * @since 2.4.0
	 */
	groupInfo.setGroupMemSilence(String username, String appKey, boolean keepSilence, BasicCallback callback);
```

#### 获取禁言列表
***Since 2.4.0***

```
	/**
	 * 获取群成员禁言列表，返回群内被禁言的成员信息列表
	 *
	 * @return List<UserInfo>
	 * @since 2.4.0
	 * @deprecated deprecated in jmessage 2.7.0 use {@link #getGroupSilenceMemberInfos()} instead
	 */
	groupInfo.getGroupSilenceMembers();

    /**
     * 获取群成员禁言列表，返回群内被禁言的成员{@link GroupMemberInfo}列表
     *
     * @return 群内被禁言的成员GroupMemberInfo列表
     * @since 2.7.0
     */
    groupInfo.getGroupSilenceMemberInfos();
```

#### 判断用户是否被禁言
***Since 2.4.0***

```
	/**
	 * 判断用户在该群内是否被禁言，若被禁言返回true，否则返回false
	 *
	 * @param username 待判断用户的用户名
	 * @param appKey 待判断用户的appKey，若传入空则默认使用本应用appKey
	 * @return boolean
	 * @since 2.4.0
	 */
	groupInfo.isKeepSilence(String username, String appKey);
```

**群成员禁言相关代码示例**

```
//设置群成员禁言状态
JMessageClient.getGroupInfo(mGroupID, new GetGroupInfoCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage, GroupInfo groupInfo) {
		if (0 == responseCode) {
			groupInfo.setGroupMemSilence(mNames, mAppKey, keepSilence, new BasicCallback() {
				@Override
				public void gotResult(int i, String s) {
					mProgressDialog.dismiss();
					if (0 == i) {
						Toast.makeText(getApplicationContext(), keepSilence ? "设置禁言成功" : "取消禁言成功", Toast.LENGTH_SHORT).show();
					} else {
						Toast.makeText(getApplicationContext(), keepSilence ? "设置禁言失败" : "取消禁言失败", Toast.LENGTH_SHORT).show();
						Log.i(TAG, "GroupInfo.setGroupMemSilence " + ", responseCode = " + i + " ; Desc = " + s);
					}
				}
			});
		} else {
			mProgressDialog.dismiss();
			Toast.makeText(getApplicationContext(), keepSilence ? "设置禁言失败" : "取消禁言失败", Toast.LENGTH_SHORT).show();
			Log.i(TAG, "getGroupInfo failed " + ", responseCode = " + responseCode + " :Desc = " + responseMessage);
		}
	}
});

//获取群成员禁言列表
JMessageClient.getGroupInfo(mGetId, new GetGroupInfoCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage, GroupInfo groupInfo) {
		mProgressDialog.dismiss();
		if (responseCode == 0) {
			List<GroupMemberInfo> silenceMembers = groupInfo.getGroupSilenceMemberInfos();
			StringBuilder sb = new StringBuilder();
			for (GroupMemberInfo info : silenceMembers) {
				sb.append(info.getUserInfo().getUserName());
				sb.append("\n");
			}
			mTv_showGroupInfo.append("群成员禁言信息列表(这里获取name,需要其他信息请自行获取)：\n" + sb.toString());
			Toast.makeText(getApplicationContext(), "获取成功", Toast.LENGTH_SHORT).show();
		} else {
			Log.i("GetGroupInfoActivity", "groupInfo.getGroupMembers" + ", responseCode = " + responseCode + " ; Desc = " + responseMessage);
			Toast.makeText(getApplicationContext(), "获取失败", Toast.LENGTH_SHORT).show();
		}
	}
});

//判断用户是否被禁言
JMessageClient.getGroupInfo(mGetId, new GetGroupInfoCallback() {
	@Override
	public void gotResult(int i, String s, GroupInfo groupInfo) {
		if (i == 0) {
			mProgressDialog.dismiss();
			Toast.makeText(getApplicationContext(), groupInfo.isKeepSilence(name, appKey) ? "已被禁言" : "没有被禁言或者用户不存在或不在指定群", Toast.LENGTH_SHORT).show();
		} else {
			mProgressDialog.dismiss();
			Log.i("GetGroupInfoActivity", "groupInfo.getGroupMemberSilenceStatus" + ", responseCode = " + i + " ; Desc = " + s);
			Toast.makeText(getApplicationContext(), "获取失败", Toast.LENGTH_SHORT).show();
		}
	}
});
```

### 群公告

#### 发布群公告
*** Since 2.8.0 ***
```
    /**
     * 发布群公告（只有群主和管理员有权限发送），选择是否向群中发布消息，sendMessage为true代表发送，false不发送<br/>
     * 注意只有发送公告成功时才会向群中发布消息，创建的消息在回调中返回，如果发送公告失败或者创建消息失败则回调中message为null。<br/>
     * 消息的发送是否成功可以通过{@link cn.jpush.im.android.api.enums.MessageStatus}判断,
     * <p>Message的extra里带有公告的实现，key为""jmessage_group_announcement"， value为jsonString:
     * <pre>
     * {"id": 公告id,"text":"公告内容text,"publisher_uid"：发布者uid,"ctime" : 公告发布时间,"gid":群组id}
     * <pre/>
     * 获取方式如下:
     * <pre>
     * String announceJson = message.getContent.getStringExtras("jmessage_group_announcement");
     * </pre></p>
     * 可自己通过字段去解析json字符串，也可通过{@link GroupAnnouncement#fromJson(String)}得到公告对象
     * 如果needSendMessage为false, 回调中message一直为null。<br/>
     * 群公告最多100条，超过老的将会被删除，发布群公告成功时群内所有人会收到{@link cn.jpush.im.android.api.event.GroupAnnouncementChangedEvent}
     * @param text 公告内容字节数不能超过1K(utf-8)
     * @param needSendMessage 是否需要发送消息
     * @param callback PublishAnnouncementCallback 回调中包含创建的公告和消息
     * @since 2.8.0
     */
    groupInfo.publishGroupAnnouncement(String text, Boolean needSendMessage, PublishAnnouncementCallback callback);
``` 

#### 获取群公告
*** Since 2.8.0 ***
```
    /**
     * 按照顺序(置顶时间倒序，创建时间倒序)获取群内所有公告.<br/>
     *
     * @param callback 回调,如果获取成功但群没有公告则返回一个empty list
     * @since 2.8.0
     */
    groupInfo.getAnnouncementsByOrder(RequestCallback<List<GroupAnnouncement>> callback);
```

#### 删除群公告
*** Since 2.8.0 ***
```
    /**
     * 删除群内指定id的公告，只有群主和管理员有权限删除<br/>
     * 删除群公告成功时群内所有成员会收到{@link cn.jpush.im.android.api.event.GroupAnnouncementChangedEvent}
	 *
     * @param announceID 公告id 通过{@link GroupAnnouncement#getAnnounceID()}获取
     * @param callback 回调
     * @since 2.8.0
     */
    groupInfo.delGroupAnnouncement(int announceID, BasicCallback callback);
```

#### 置顶群公告
*** Since 2.8.0 ***
```
    /**
     * 设置置顶状态,本设置为改变置顶状态和置顶时间，同时会导致公告的排序发生改变{@link #getAnnouncementsByOrder(RequestCallback)}<br/>
     * 设置成功时，群内所有成员会收到{@link cn.jpush.im.android.api.event.GroupAnnouncementChangedEvent}
     *
     * @param announceID 公告id, 通过{@link GroupAnnouncement#getAnnounceID()}获取
     * @param isTop true置顶， false取消置顶
     * @param callback 回调
     * @since 2.8.0
     */
groupInfo.setTopAnnouncement(int announceID, boolean isTop, BasicCallback callback);
```
**群公告相关代码示例**
```
// 发布群公告
String text = mEtText.getText().toString();
boolean needSendMessage = Boolean.valueOf(mEtSendMessage.getText().toString());
groupInfo.publishGroupAnnouncement(text, needSendMessage, new PublishAnnouncementCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage, GroupAnnouncement announcement, Message message) {
		if (ErrorCode.NO_ERROR == responseCode) {
			Toast.makeText(getApplicationContext(), "发布公告成功", Toast.LENGTH_SHORT).show();
		} else {
			Toast.makeText(getApplicationContext(), "发布公告失败", Toast.LENGTH_SHORT).show();
			mTvResult.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

// 获取群公告
groupInfo.getAnnouncementsByOrder(new RequestCallback<List<GroupAnnouncement>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<GroupAnnouncement> announcements) {
		if (ErrorCode.NO_ERROR == responseCode) {
			StringBuilder result = new StringBuilder();
			for (GroupAnnouncement announcement : announcements) {
				result.append("公告ID:" + announcement.getAnnounceID() + "\n");
				result.append("公告内容:" + announcement.getText() + "\n");
				result.append("公告创建时间:" + announcement.getCtime() + "\n");
				result.append("公告是否置顶:" + announcement.isTop() + "\n");
				result.append("公告置顶时间:" + announcement.getTopTime() + "\n");
				result.append("公告发布者(username):" + announcement.getPublisher().getUserName() + "\n\n");
			}
			Toast.makeText(getApplicationContext(), "获取公告成功", Toast.LENGTH_SHORT).show();
			mTvResult.setText(result.toString());
		} else {
			Toast.makeText(getApplicationContext(), "获取公告失败", Toast.LENGTH_SHORT).show();
			mTvResult.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

// 删除群公告
try {
	int announceID = Integer.valueOf(mEtAnnounceID.getText().toString());
	groupInfo.delGroupAnnouncement(announceID, new BasicCallback() {
		@Override
		public void gotResult(int responseCode, String responseMessage) {
			if (ErrorCode.NO_ERROR == responseCode) {
				Toast.makeText(getApplicationContext(), "删除公告成功", Toast.LENGTH_SHORT).show();
			} else {
				Toast.makeText(getApplicationContext(), "删除公告失败", Toast.LENGTH_SHORT).show();
				mTvResult.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
			}
		}
	});
} catch (NumberFormatException e) {
	Toast.makeText(getApplicationContext(), "请输入合法公告ID", Toast.LENGTH_SHORT).show();
}

// 置顶群公告
try {
	int announceID = Integer.valueOf(mEtAnnounceID.getText().toString());
	groupInfo.setTopAnnouncement(announceID, isTop, new BasicCallback() {
		@Override
		public void gotResult(int responseCode, String responseMessage) {
			StringBuilder result = new StringBuilder();
			result.append(isTop ? "置顶" : "取消置顶");
			if (ErrorCode.NO_ERROR == responseCode) {
				result.append("成功");
				Toast.makeText(getApplicationContext(), result.toString(), Toast.LENGTH_SHORT).show();
			} else {
				result.append("失败");
				Toast.makeText(getApplicationContext(), result.toString(), Toast.LENGTH_SHORT).show();
				mTvResult.setText("responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
			}
		}
	});
} catch (NumberFormatException e) {
	Toast.makeText(getApplicationContext(), "请输入合法公告ID", Toast.LENGTH_SHORT).show();
}
```

### 群组黑名单
群黑名单用以屏蔽某些不良用户, 被加入黑名单的用户无法再次加入该群组除非从黑名单中移除，如果被加入黑名单的用户已经在群中会被踢出群。

#### 将用户添加至黑名单
*** Since 2.8.0 ***
```
    /**
     * 将用户加到群组黑名单，只有群主和管理员有此权限, 被加入黑名单的用户如果在群内会被踢出群组，黑名单中的用户无法再加入群组<br/>
     * 操作成功后群内成员将收到群黑名单变更事件{@link cn.jpush.im.android.api.event.GroupBlackListChangedEvent}
     *
     * @param userInfos 准备加入黑名单的用户userInfo集合
     * @param callback 回调
     * @since 2.8.0
     */
    groupInfo.addGroupBlacklist(List<UserInfo> userInfos, BasicCallback callback);
```

#### 将用户从群组黑名单中移除
*** Since 2.8.0 ***
```
    /**
     * 将用户从群组黑名单中移除，只有群主和管理员有此权限.<br/>
     * 操作成功后群内成员将收到群黑名单变更事件{@link cn.jpush.im.android.api.event.GroupBlackListChangedEvent}
     *
     * @param userInfos 准备移出黑名单的用户userInfo集合
     * @param callback 回调
     * @since 2.8.0
     */
    groupInfo.delGroupBlacklist(List<UserInfo> userInfos, BasicCallback callback);
```

#### 获取群组黑名单用户列表
*** Since 2.8.0 ***
```
    /**
     * 获取群组的黑名单用户列表, 按照被拉黑时间倒序排列
     *
     * @param callback 回调
     * @since 2.8.0
     */
    groupInfo.getGroupBlackList(RequestCallback<List<UserInfo>> callback);
```

**群组黑名单代码相关示例**
```
// 将用户加到群组黑名单
groupInfo.addGroupBlacklist(Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (ErrorCode.NO_ERROR == responseCode) {
			Toast.makeText(getApplicationContext(), "添加成功", Toast.LENGTH_SHORT).show();
		} else {
			Toast.makeText(getApplicationContext(), "添加失败", Toast.LENGTH_SHORT).show();
			mTvShowResult.setText("添加用户到黑名单失败:\n" + "responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

// 将用户从群组黑名单中移除
groupInfo.delGroupBlacklist(Collections.singletonList(info), new BasicCallback() {
	@Override
	public void gotResult(int responseCode, String responseMessage) {
		if (ErrorCode.NO_ERROR == responseCode) {
			Toast.makeText(getApplicationContext(), "移除成功", Toast.LENGTH_SHORT).show();
		} else {
			Toast.makeText(getApplicationContext(), "移除失败", Toast.LENGTH_SHORT).show();
			mTvShowResult.setText("将用户从黑名单中移除失败:\n" + "responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});

// 获取群组黑名单用户列表
groupInfo.getGroupBlackList(new RequestCallback<List<UserInfo>>() {
	@Override
	public void gotResult(int responseCode, String responseMessage, List<UserInfo> result) {
		if (ErrorCode.NO_ERROR == responseCode) {
			Toast.makeText(getApplicationContext(), "获取成功", Toast.LENGTH_SHORT).show();
			StringBuilder builder = new StringBuilder();
			if (result.size() > 0) {
				builder.append("群组黑名单:\n");
				for (UserInfo userInfo : result) {
					builder.append("用户名:").append(userInfo.getUserName()).append("\n");
					builder.append("appKey:").append(userInfo.getAppKey()).append("\n\n");
				}
			} else {
				builder.append("群组的黑名单为空");
			}
			mTvShowResult.setText(builder.toString());
		} else {
			Toast.makeText(getApplicationContext(), "获取失败", Toast.LENGTH_SHORT).show();
			mTvShowResult.setText("获取群黑名单失败:\n" + "responseCode:" + responseCode + "\nresponseMessage:" + responseMessage);
		}
	}
});
```
