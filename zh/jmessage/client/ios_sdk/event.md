<h1>事件处理</h1>


## 概述
当 SDK 收到某些后台下发的数据，或者发生了某些需要上层关注的事件时，SDK 会上抛事件对象通知给上层，例如，[好友事件](./jmessage_ios_appledoc_html/Classes/JMSGFriendNotificationEvent.html)、[入群申请事件](./jmessage_ios_appledoc_html/Classes/JMSGApplyJoinGroupEvent.html)、[用户登录状态变更事件](./jmessage_ios_appledoc_html/Classes/JMSGUserLoginStatusChangeEvent.html)等。  
应用上层需要根据实际情况决定是否需要接收并且处理事件。


### 添加监听代理
只有添加了代理，并且上层实现代理方法，才能够接收到相关事件，SDK 所有代理的添加都是通过此接口设置：

##### JMessage 

```
/*!
 * @abstract 增加回调(delegate protocol)监听
 *
 * @param delegate 需要监听的 Delegate Protocol
 * @param conversation 允许为nil
 *
 * - 为 nil, 表示接收所有的通知, 不区分会话.
 * - 不为 nil，表示只接收指定的 conversation 相关的通知.
 *
 * @discussion 默认监听全局 JMessageDelegate 即可.
 *
 * 这个调用可以在任何地方, 任何时候调用, 可以在未进行 SDK
 * 启动 setupJMessage:appKey:channel:apsForProduction:category: 时就被调用.
 *
 * 并且, 如果你有必要接收数据库升级通知 JMSGDBMigrateDelegate,
 * 就应该在 SDK 启动前就调用此方法, 来注册通知接收.
 * 这样, SDK启动过程中发现需要进行数据库升级, 给 App 发送数据库升级通知时,
 * App 才可以收到并进行处理.
 */
+ (void)addDelegate:(id <JMessageDelegate>)delegate withConversation:(JMSGConversation *)conversation;
```

### 用户事件
此类事件总体分为：用户信息变更和登录状态变更事件，当前登录用户的登录状态发生变化或者异常时，SDK 会上抛此类型事件，上层通过 [JMSGUserDelegate](./jmessage_ios_appledoc_html/Protocols/JMSGUserDelegate.html) 类里的方法来监听此类事件。

##### 事件类型

```
typedef NS_ENUM(NSInteger, JMSGLoginStatusChangeEventType) {
  // 用户登录状态变更事件
  /// 事件类型: 登录被踢
  kJMSGEventNotificationLoginKicked = 1,
  /// 事件类型: 非客户端修改密码强制登出事件
  kJMSGEventNotificationServerAlterPassword = 2,
  /// 事件类型：用户登录状态异常事件（需要重新登录）
  kJMSGEventNotificationUserLoginStatusUnexpected = 70,
  /// 事件类型：当前登录用户信息变更通知事件(非客户端修改)
  kJMSGEventNotificationCurrentUserInfoChange = 40,
  /// 事件类型：当前登录用户被删除事件（本地用户信息会被清空）
  kJMSGEventNotificationCurrentUserDeleted = 10001,
  /// 事件类型：当前登录用户被禁用事件（本地用户信息会被清空）
  kJMSGEventNotificationCurrentUserDisabled = 10002,
};
```

##### 监听方法

```
/*!
 * @abstract 监听当前用户登录状态变更事件
 *
 * @discussion 可监听：当前登录用户被踢、非客户端修改密码强制登出、登录状态异常、被删除、被禁用、信息变更等事件
 *
 * @since 3.5.0
 */
@optional
- (void)onReceiveUserLoginStatusChangeEvent:(JMSGUserLoginStatusChangeEvent *)event;
```

### <span id="message-event">消息事件</span>
与消息 `JMSGMessage` 有关的事件都称之为**消息事件**，但是消息事件又可分为如下两类：

+ **普通的消息事件**：这类事件都是有单独的方法监听，不会入库，SDK 也不会将其主动加入消息记录中。
+ **特殊的消息事件**：这是类事件 SDK 会封装为一个消息对象 message 上抛，这些消息事件会入库到消息记录里。这类事件其实就是群会话里的事件，比如：用户加入群组、用户被踢出群组等，


#### 特殊的消息事件
称之为“特殊”，是因为写类型的事件 SDK 会封装成 `JMSGMessage` 对象后上抛给上层，而其他类型的消息则是通过 `JMSGNotificationEvent` 对象上抛的。

##### 事件类型

```
typedef NS_ENUM(NSInteger, JMSGEventNotificationType) {
  // 消息事件
  /// 事件类型: 群组被创建
  kJMSGEventNotificationCreateGroup = 8,
  /// 事件类型: 退出群组
  kJMSGEventNotificationExitGroup = 9,
  /// 事件类型: 群组添加新成员
  kJMSGEventNotificationAddGroupMembers = 10,
  /// 事件类型: 群组成员被踢出
  kJMSGEventNotificationRemoveGroupMembers = 11,
  /// 事件类型: 群信息更新
  kJMSGEventNotificationUpdateGroupInfo = 12,
  /// 事件类型: 群禁言通知事件
  kJMSGEventNotificationGroupMemberSilence = 65,
  /// 事件类型: 管理员角色变更通知事件
  kJMSGEventNotificationGroupAdminChange = 80,
  /// 事件类型: 群主变更通知事件
  kJMSGEventNotificationGroupOwnerChange = 82,
  /// 事件类型: 群类型变更通知事件
  kJMSGEventNotificationGroupTypeChange = 83,
  /// 事件类型: 解散群组
  kJMSGEventNotificationDissolveGroup = 11001,
  /// 事件类型: 群组成员上限变更
  kJMSGEventNotificationGroupMaxMemberCountChange = 11002,
};
```

##### 监听方法
这类特殊的消息事件的监听分为：在线、离线、漫游。

+ 在线监听方法

```
/*!
 * @abstract 接收消息(服务器端下发的)回调
 *
 * @param message 接收到下发的消息
 * @param error 不为 nil 表示接收消息出错
 *
 * @discussion 应检查 error 是否为空来判断有没有出错. 如果未出错, 则成功.
 * 留意的是, 这里的 error 不包含媒体消息下载文件错误. 这类错误有单独的回调 onReceiveMessageDownloadFailed:
 *
 * 收到的消息里, 也包含服务器端下发的各类消息事件, 比如有人被加入了群聊. 这类消息事件处理为特殊的 JMSGMessage 类型.
 *
 * 事件类的消息, 基于 JMSGMessage 类里的 contentType 属性来做判断,
 * contentType = kJMSGContentTypeEventNotification.
 */
@optional
- (void)onReceiveMessage:(JMSGMessage *)message error:(NSError *)error;
```

+ 离线监听方法

```
/*!
 * @abstract 同步离线消息、离线事件通知
 *
 * @param conversation    同步离线消息的会话
 * @param offlineMessages 离线消息、离线事件数组
 *
 * @discussion 注意：
 *
 * SDK 会将消息下发分为在线下发和离线下发两种情况,
 * 其中用户在离线状态(包括用户登出或者网络断开)期间所收到的消息我们称之为离线消息.
 *
 * 当用户上线收到这部分离线消息后,这里的处理与之前版本不同的是:
 *
 * 3.1.0 版本之前: SDK 会和在线时收到的消息一样,每收到一条消息都会上抛一个在线消息 JMSGMessage 来通知上层.
 *
 * 3.1.0 版本之后: SDK 会以会话为单位，不管该会话有多少离线消息，SDK同步完成后每个会话只上抛一次.
 *
 * 3.2.1 版本之后: SDK 会以会话为单位，不管该会话有多少离线事件，SDK同步完成后每个会话只上抛一次
 *
 * 注意：一个会话最多触发两次这个代理，即：离线消息和离线事件各一次,这样会大大减轻上层在收到消息刷新 UI 的压力.
 *
 * 上层通过此代理方法监听离线消息同步的会话,详见官方文档.
 *
 */
@optional
- (void)onSyncOfflineMessageConversation:(JMSGConversation *)conversation
                         offlineMessages:(NSArray JMSG_GENERIC(__kindof JMSGMessage *)*)offlineMessages;
```


+ 漫游监听方法

	漫游消息事件则是通过如下方法监听，此方法只会通知上层是某个会话有漫游消息事件，而不会上抛具体的消息事件列表，需上层调用接口从本地获取。

```
/*!
 * @abstract 同步漫游消息通知
 *
 * @param conversation 同步漫游消息的会话
 *
 * @discussion 注意：
 *
 * 当 SDK 触发此函数时，说明该会话有同步下漫游消息，并且已经存储到本地数据库中，
 * 上层可通过 JMSGConversation 类中的获取message的方法刷新UI.
 *
 * @since 3.1.0
 */
@optional
- (void)onSyncRoamingMessageConversation:(JMSGConversation *)conversation;
```

#### 普通的消息事件
##### <span id="message-retract-event">消息撤回事件</span>

由消息发送方发起调用，在一定时间内，SDK 可以撤回会话中某条消息，一旦消息撤回成功，用户会收到 SDK 上抛的一个 [JMSGMessageRetractEvent](./jmessage_ios_appledoc_html/Classes/JMSGMessageRetractEvent.html) 事件，上层通过下面的代理来监听。

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >conversation</td>
      <td >JMSGConversation</td>
      <td >消息撤回所属会话</td>
    </tr>
	<tr >
      <td >retractMessage</td>
      <td >JMSGMessage</td>
      <td >撤回之后的消息</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听消息撤回事件
 *
 * @param retractEvent 下发的通知事件，事件类型请查看 JMSGMessageRetractEvent 类
 *
 * @since 3.2.0
 */
@optional
- (void)onReceiveMessageRetractEvent:(JMSGMessageRetractEvent *)retractEvent;
```

##### <span id="message-receipt-change-event">消息回执事件</span>

对于消息接收方，可以将一条消息标记为已读，标记成功后，这条消息的已读状态会记录在本地，SDK 还将主动上抛一个 [JMSGMessageReceiptStatusChangeEvent](./jmessage_ios_appledoc_html/Classes/JMSGMessageReceiptStatusChangeEvent.html) 通知事件

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >conversation</td>
      <td >JMSGConversation</td>
      <td >消息所属会话</td>
    </tr>
	<tr >
      <td >messages</td>
      <td >NSArray(JMSGMessage)</td>
      <td >已读回执变更的消息列表</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听消息回执状态变更事件
 *
 * @param receiptEvent 下发的通知事件，事件类型请查看 JMSGMessageReceiptStatusChangeEvent 类
 *
 * @discussion 上层可以通过 receiptEvent 获取相应信息
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageReceiptStatusChangeEvent:(JMSGMessageReceiptStatusChangeEvent *)receiptEvent;
```


### 群组事件
这里说的群组事件是指需要单独方法来监听的群事件，与[消息事件](#message-event)是有区别的。此类事件上层通过 [JMSGGroupDelegate](./jmessage_ios_appledoc_html/Protocols/JMSGGroupDelegate.html) 类里的代理方法来监听。

#### 群信息变更通知事件
群信息变更后，后台下发的通知给到SDK，SDK 会主动更新群信息，然后再出发上抛并触发代理方法，上层通过实现该代理可监听群信息变更通知。
##### 监听方法

```
/*!
 * @abstract 群组信息 (GroupInfo) 变更通知
 *
 * @param group 变更后的群组对象
 *
 * @discussion 如果想要获取通知, 需要先注册回调. 具体请参考 JMessageDelegate 里的说明.
 */
@optional
- (void)onGroupInfoChanged:(JMSGGroup *)group;
```

#### <span id="apply-join-group">申请入群通知事件</span>
该事件通知只适用于公开群，并且只有群主和管理员会收到此事件，事件内的具体参数请查看 [JMSGApplyJoinGroupEvent](./jmessage_ios_appledoc_html/Classes/JMSGApplyJoinGroupEvent.html)

##### 事件
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >eventID</td>
      <td >NSString</td>
      <td >事件的 id</td>
    </tr>
	<tr >
      <td >groupID</td>
      <td >NSString</td>
      <td >群 gid</td>
    </tr>
	<tr >
      <td >isInitiativeApply</td>
      <td >BOOL</td>
      <td >YES：主动申请加入，NO：被邀请加入</td>
    </tr>
	<tr >
      <td >sendApplyUser</td>
      <td >JMSGUser</td>
      <td >发起申请的 user</td>
    </tr>
	<tr >
      <td >joinGroupUsers</td>
      <td >NSArray(JMSGUser)</td>
      <td >被邀请入群的 user 数组</td>
    </tr>
	<tr >
      <td >reason</td>
      <td >NSString</td>
      <td >原因</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听申请入群通知
 *
 * @param event 申请入群事件
 *
 * @discussion 只有群主和管理员能收到此事件；申请入群事件相关参数请查看 JMSGApplyJoinGroupEvent 类，在群主审批此事件时需要传递事件的相关参数
 *
 * @since 3.4.0
 */
@optional
- (void)onReceiveApplyJoinGroupApprovalEvent:(JMSGApplyJoinGroupEvent *)event;
```
####  <span id="admin-reject-application">管理员拒绝入群申请通知事件</span>
该事件通知只适用于公开群，只有申请方和被申请方会收到此事件，相关参数和返回值请详看 [JMSGGroupAdminRejectApplicationEvent](./jmessage_ios_appledoc_html/Classes/JMSGGroupAdminRejectApplicationEvent.html)

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >groupID</td>
      <td >NSString</td>
      <td >群 gid</td>
    </tr>
	<tr >
      <td >rejectReason</td>
      <td >NSString</td>
      <td >拒绝原因</td>
    </tr>
	<tr >
      <td >groupManager</td>
      <td >JMSGUser</td>
      <td >操作的管理员</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听管理员拒绝入群申请通知
 *
 * @param event 拒绝入群申请事件
 *
 * @discussion 只有申请方和被申请方会收到此事件；拒绝的相关描述和原因请查看 JMSGGroupAdminRejectApplicationEvent 类
 *
 * @since 3.4.0
 */
@optional
- (void)onReceiveGroupAdminRejectApplicationEvent:(JMSGGroupAdminRejectApplicationEvent *)event;
```
#### 管理员审批通知事件
该事件通知只适用于公开群，只有管理员才会收到该事件,当管理员同意或拒绝了某个入群申请事件时，其他管理员就会收到该事件，相关属性请查看 [JMSGGroupAdminApprovalEvent](. ios_sdk/jmessage_ios_appledoc_html/Classes/JMSGGroupAdminApprovalEvent.html) 类

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >isAgreeApply</td>
      <td >BOOL</td>
      <td >管理员是否同意申请，YES：同意，NO：拒绝</td>
    </tr>
	<tr >
      <td >applyEventID</td>
      <td >NSString</td>
      <td >申请入群事件的事件 id</td>
    </tr>
	<tr >
      <td >groupID</td>
      <td >NSString</td>
      <td >群 gid</td>
    </tr>
	<tr >
      <td >groupAdmin</td>
      <td >JMSGUser</td>
      <td >操作的管理员</td>
    </tr>
	<tr >
      <td >users</td>
      <td >NSArray(JMSGUser)</td>
      <td >申请或被邀请加入群的用户，即：实际入群的用户</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听管理员审批通知
 *
 * @param event 管理员审批事件
 *
 * @discussion 只有管理员才会收到该事件；当管理员同意或拒绝了某个入群申请事件时，其他管理员就会收到该事件，相关属性请查看 JMSGGroupAdminApprovalEvent 类
 *
 * @since 3.5.0
 */
@optional
- (void)onReceiveGroupAdminApprovalEvent:(JMSGGroupAdminApprovalEvent *)event;
```

#### 群成员群昵称变更通知事件
该事件适用于任何类型的群组，当群内某个成员改变了在群里的群昵称，SDK 会上抛该事件，如果是离线修改，SDK 会把同一个群内的所有修改昵称的事件一起上抛，事件具体相关属性请查看 [JMSGGroupNicknameChangeEvent](./jmessage_ios_appledoc_html/Classes/JMSGGroupNicknameChangeEvent.html) 类

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >group</td>
      <td >JMSGGroup</td>
      <td >群组</td>
    </tr>
	<tr >
      <td >fromMemberInfo</td>
      <td >JMSGGroupMemberInfo</td>
      <td >修改昵称的群成员</td>
    </tr>
	<tr >
      <td >toMemberInfo</td>
      <td >JMSGGroupMemberInfo</td>
      <td >被修改昵称的群成员</td>
    </tr>
	<tr >
      <td >ctime</td>
      <td >UInt64</td>
      <td >事件时间</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 群成员群昵称变更通知
 *
 * @param events 群成员昵称变更事件列表
 *
 * @discussion 如果是离线事件，SDK 会将所有的修改记录加入数组上抛。事件具体相关属性请查看 JMSGGroupNicknameChangeEvent 类
 *
 * @since 3.7.0
 */
@optional
- (void)onReceiveGroupNicknameChangeEvents:(NSArray<__kindof JMSGGroupNicknameChangeEvent*>*)events;
```

#### 群公告变更通知事件
该事件适用于任何类型群组，群公告最多100条，发布公告、置顶公告、删除公告都会有事件下发，下发的 [JMSGGroupAnnouncementEvent](./jmessage_ios_appledoc_html/Classes/JMSGGroupAnnouncementEvent.html) 属性并不是全部都有值，比如：删除公告事件里只有公告 id 是有值的。

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >announcement</td>
      <td >JMSGGroupAnnouncement</td>
      <td >群公告</td>
    </tr>
	<tr >
      <td >fromUser</td>
      <td >JMSGUser</td>
      <td >事件操作者</td>
    </tr>
	<tr >
      <td >group</td>
      <td >JMSGGroup</td>
      <td >群组</td>
    </tr>
	<tr >
      <td >ctime</td>
      <td >UInt64</td>
      <td >事件时间</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 群公告变更通知
 *
 * @param event 群公告事件列表
 *
 * @discussion 事件具体相关属性请查看 JMSGGroupAnnouncementEvent 类
 *
 * @since 3.8.0
 */
@optional
- (void)onReceiveGroupAnnouncementEvents:(NSArray<__kindof JMSGGroupAnnouncementEvent*>*)events;
```

#### 群组黑名单变更通知事件
该事件适用于任何类型群组，黑名单上限100个，超出将无法设置成功，被拉入黑名单用户会被主动踢出群组，且无法再次加入。事件具体相关属性请查看 [JMSGGroupBlacklistChangeEvent](./jmessage_ios_appledoc_html/Classes/JMSGGroupBlacklistChangeEvent.html) 类

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >group</td>
      <td >JMSGGroup</td>
      <td > 群组 </td>
    </tr>
	<tr >
      <td >fromUser</td>
      <td >JMSGUser</td>
      <td >事件操作者</td>
    </tr>
	<tr >
      <td >targetList</td>
      <td >NSArray(JMSGUser)</td>
      <td >被加入/被删除 群组黑名单的用户列表</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 群组黑名单变更通知
 *
 * @param event 群组黑名单事件列表
 *
 * @discussion 事件具体相关属性请查看 JMSGGroupBlacklistChangeEvent 类
 *
 * @since 3.8.0
 */
- (void)onReceiveGroupBlacklistChangeEvents:(NSArray<__kindof JMSGGroupBlacklistChangeEvent*>*)events;
```


### <span id="chatroom-event">聊天室事件</span>
#### 聊天室管理员变更事件通知
##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >chatRoom</td>
      <td >JMSGChatRoom</td>
      <td >聊天室</td>
    </tr>
	<tr >
      <td >fromUser</td>
      <td >JMSGUser</td>
      <td >事件操作者</td>
    </tr>
	<tr >
      <td >targetList</td>
      <td >NSArray(JMSGUser)</td>
      <td >被添加/被删除 聊天室管理员的用户列表</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 聊天室管理员变更通知
 *
 * @param event 管理员事件列表
 *
 * @discussion 事件具体相关属性请查看 JMSGChatRoomAdminChangeEvent 类
 *
 * @since 3.8.0
 */
- (void)onReceiveChatRoomAdminChangeEvents:(NSArray<__kindof JMSGChatRoomAdminChangeEvent*>*)events;
```

#### 聊天室黑名单变更事件通知

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >chatRoom</td>
      <td >JMSGChatRoom</td>
      <td >聊天室</td>
    </tr>
	<tr >
      <td >fromUser</td>
      <td >JMSGUser</td>
      <td >事件操作者</td>
    </tr>
	<tr >
      <td >targetList</td>
      <td >NSArray(JMSGUser)</td>
      <td >被添加/被删除 聊天室黑名单的用户列表</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 聊天室黑名单变更通知
 *
 * @param event 黑名单事件列表
 *
 * @discussion 事件具体相关属性请查看 JMSGChatRoomBlacklisChangetEvent 类
 *
 * @since 3.8.0
 */
- (void)onReceiveChatRoomBlacklistChangeEvents:(NSArray<__kindof JMSGChatRoomBlacklisChangetEvent*>*)events;
```


### <span id="friend-event">好友事件</span>
可监听：加好友、删除好友、好友更新等事件，具体相关属性请查看 [JMSGFriendNotificationEvent](./jmessage_ios_appledoc_html/Classes/JMSGFriendNotificationEvent.html)

**注意：**好友相关事件 SDK 并没有做本地化存储，上层想要做记录这些事件，则需要上层自己实现存储。

##### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性/方法</th>
      <th width="40px">类型/返回值</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >eventID</td>
      <td >NSString</td>
      <td >事件的 id</td>
    </tr>
	<tr >
      <td >getReason</td>
      <td >NSString</td>
      <td >获取事件发生的理由</td>
    </tr>
	<tr >
      <td >getFromUsername</td>
      <td >NSString</td>
      <td >事件发送者的username</td>
    </tr>
	<tr >
      <td >getFromUser</td>
      <td >JMSGUser</td>
      <td >获取事件发送者user</td>
    </tr>
  </table>
</div>

##### 监听方法

```
/*!
 * @abstract 监听好友相关事件
 *
 * @discussion 可监听：加好友、删除好友、好友更新等事件
 *
 * @since 3.5.0
 */
@optional
- (void)onReceiveFriendNotificationEvent:(JMSGFriendNotificationEvent *)event;
```


### 透传命令事件
+ 命令透传发送后台不会为其离线保存，只会在对方用户在线的前提下将命令推送给对方。
+ SDK 收到命令之后也不会本地保存，不发送通知栏通知，整体快速响应。
+ 透传命令分为会话间透传、设备间透传

开发者可以通过命令透传拓展一些在线场景下的辅助功能，如：实现输入状态提示、控制其他端下线等。
事件相关属性请查看 [JMSGMessageTransparentEvent](./jmessage_ios_appledoc_html/Classes/JMSGMessageTransparentEvent.html) 类

#### 事件

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >eventType</td>
      <td >JMSGEventNotificationType</td>
      <td >事件类型</td>
    </tr>
	<tr >
      <td >transMessageType</td>
      <td >JMSGTransMessageType</td>
      <td >消息透传的类型,单聊、群聊、设备间透传消息</td>
    </tr>
	<tr >
      <td >sendUser</td>
      <td >JMSGUser</td>
      <td >透传消息的发送者</td>
    </tr>
	<tr >
      <td >target</td>
      <td >id</td>
      <td >透传消息的目标对象，JMSGUser、JMSGGroup</td>
    </tr>
	<tr >
      <td >transparentText</td>
      <td >NSString</td>
      <td >透传消息内容</td>
    </tr>
	<tr >
      <td >conversation</td>
      <td >JMSGConversation</td>
      <td >透传消息所属会话</td>
    </tr>
  </table>
</div>

#### 监听方法

```
/*!
 * @abstract 监听消息透传事件
 *
 * @param transparentEvent 下发的通知事件，事件类型请查看 JMSGMessageTransparentEvent 类
 *
 * @discussion 消息透传的类型：单聊、群聊、设备间透传消息
 *
 * @since 3.3.0
 */
@optional
- (void)onReceiveMessageTransparentEvent:(JMSGMessageTransparentEvent *)transparentEvent;
```
