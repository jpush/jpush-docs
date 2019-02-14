<h1>群组管理</h1>

## 概述

把多个 username 加入到同一个群组内，在群组内发送群组消息。

- 创建私有群组、创建公开群组（3.4.0版本新增[公开群组](#PublicGroup)）
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
/*!
 * @abstract 创建群组(只能创建私有群)
 *
 * @param groupName 群组名称
 * @param groupDesc 群组描述信息
 * @param usernameArray 初始成员列表。NSArray 里的类型是 NSString
 * @param handler 结果回调。正常返回 resultObject 的类型是 JMSGGroup。
 *
 * @discussion 向服务器端提交创建群组请求，返回生成后的群组对象.
 * 返回群组对象, 群组ID是App 需要关注的, 是后续各种群组维护的基础.
 */
+ (void)createGroupWithName:(NSString * JMSG_NULLABLE )groupName
                       desc:(NSString *JMSG_NULLABLE)groupDesc
                memberArray:(NSArray JMSG_GENERIC(__kindof NSString *) *JMSG_NULLABLE)usernameArray
          completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### <span id="PublicGroup">创建公开群组</span>
***Since 3.4.0***  
3.4.0版本新增公开群组类型。公开群组可通过入群申请，经群主或管理员审核通过的方式加入。公开群组群主或管理员直接邀请即可加入。群成员邀请入群需群主或管理员审批 [入群申请与审批](#ApplyAndProcess)

```
/*!
 * @abstract 创建群组（可创建私有群、公开群）
 *
 * @param groupInfo     群信息类，如：群名、群类型等，详细请查看 JMSGGroupInfo 类
 * @param usernameArray 初始成员列表。NSArray 里的类型是 NSString
 * @param handler       结果回调。正常返回 resultObject 的类型是 JMSGGroup。
 *
 * @discussion 向服务器端提交创建群组请求，返回生成后的群组对象.
 * 返回群组对象, 群组ID是App 需要关注的, 是后续各种群组维护的基础.
 */
+ (void)createGroupWithGroupInfo:(JMSGGroupInfo *)groupInfo
                     memberArray:(NSArray JMSG_GENERIC(__kindof NSString *) *JMSG_NULLABLE)usernameArray
               completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 解散群组

```
/*!
 * @abstract 解散群组
 *
 * @patam gid     需要解散的群组 id
 * @param handler 结果回调,error = nil 表示操作成功
 *
 * @discussion 只有群主才有权限解散群。
 */
+ (void)dissolveGroupWithGid:(NSString *)gid handler:(JMSGCompletionHandler)handler;
```
 
### 群组信息
#### 获取群信息

```
/*!
 * @abstract 获取群组信息
 *
 * @param groupId 待获取详情的群组ID
 * @param handler 结果回调. 正常返回时 resultObject 类型是 JMSGGroup.
 *
 * @discussion 如果考虑性能损耗, 在群聊时获取群组信息, 可以获取 JMSGConversation -> target 属性.
 */
+ (void)groupInfoWithGroupId:(NSString *)groupId
           completionHandler:(JMSGCompletionHandler)handler;
```

#### <span id="UpdageGroupInfo">更新群信息</span>
为了上层在修改群信息时更加方便、快捷的实现，SDK 新增了群信息类 `JMSGGroupInfo `，在修改群信息时可以实现一个接口修改多个信息，具体如下:

***JMSGGroupInfo***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >gid</td>
      <td >NSString</td>
      <td >群 id</td>
    </tr>
	<tr >
      <td >name</td>
      <td >NSString</td>
      <td >群名称</td>
    </tr>
	<tr >
      <td >desc</td>
      <td >NSString</td>
      <td >群描述</td>
    </tr>
	<tr >
      <td >avatarData</td>
      <td >NSData</td>
      <td >群头像数据，此属性只用来修改群信息，切勿从此类拿来此属性来展示</td>
    </tr>
	<tr >
      <td >avatar</td>
      <td >NSString</td>
      <td >群头像的媒体文件ID</td>
    </tr>
	<tr >
      <td >groupType</td>
      <td >JMSGGroupType</td>
      <td >群组类型，私有、公开</td>
    </tr>
	<tr >
      <td >maxMemberCount</td>
      <td >NSString</td>
      <td >群组人数上限，注意：仅限于创建群组时可以设置，必须大于2</td>
    </tr>
	<tr >
      <td >ctime</td>
      <td >SInt64</td>
      <td >群组创建时间</td>
    </tr>
  </table>
</div>

```
/*!
 * @abstract 更新群信息（统一字段上传）
 *
 * @param gid         群组 id
 * @param groupInfo   群信息类，详细请查看 JMSGGroupInfo 类
 * @param handler     结果回调. 正常返回时, resultObject 为 nil.
 *
 * @discussion 注意：修改群名称和群描述时参数不允许传空字符串，群类型不允许修改
 */
+ (void)updateGroupInfoWithGid:(NSString *)gid
                     groupInfo:(JMSGGroupInfo *)groupInfo
             completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 群头像
##### 获取群头像
群组头像是有缩略图和大图之分的，具体请查看 API 文档，这里只列出缩略图接口。  
接口都是优先返回本地缓存，如果本地没有则是会发起网络请求。

```
/*!
 * @abstract 获取头像缩略图文件数据
 *
 * @param handler 结果回调。回调参数:
 *
 * - data     头像数据;
 * - objectId 群组 gid;
 * - error    不为nil表示出错;
 *
 * 如果 error 为 nil, data 也为 nil, 表示没有头像数据.
 *
 * @discussion 需要展示缩略图时使用。
 * 如果本地已经有文件，则会返回本地，否则会从服务器上下载。
 */
- (void)thumbAvatarData:(JMSGAsyncDataHandler)handler;
```

##### 更新群头像
修改头像有单独的接口，并且支持附带图片格式，上层也可以通过[更新群信息的统一修改接口](#UpdageGroupInfo)上传头像。

```
/*!
 * @abstract 更新群头像（支持传图片格式）
 *
 * @param groupId         待更新的群组ID
 * @param avatarData      头像数据
 * @param avatarFormat    头像格式，可以为空，不包括"."
 * @param handler         回调
 *
 * @discussion 头像格式参数直接填格式名称，不要带点。正确：@"png"，错误：@".png"
 */
+ (void)updateGroupAvatarWithGroupId:(NSString *JMSG_NONNULL)groupId
                          avatarData:(NSData *JMSG_NONNULL)avatarData
                        avatarFormat:(NSString *JMSG_NULLABLE)avatarFormat
                   completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

##### 获取头像本地路径

```
/*!
 * @abstract 获取头像缩略文件的本地路径
 *
 * @return 返回本地路，返回值只有在下载完成之后才有意义
 */
- (NSString *JMSG_NULLABLE)thumbAvatarLocalPath;
```

#### 修改群类型

```
/*!
 * @abstract 修改群组类型
 *
 * @param type    群类型，公开群、私有群
 * @param handler 结果回调。error = nil 表示成功
 *
 * @discussion 对于已经创建的群组，可以通过此接口来修改群组的类型
 */
- (void)changeGroupType:(JMSGGroupType)type handler:(JMSGCompletionHandler)handler;
```

### 群成员信息
群组成员是由 `JMSGUser` 对象组成的，但是群成员有更多的独有属性，如：群昵称、入群时间等，所以从 `JMessage v3.7.0` 开始新建群组成员信息类 `JMSGGroupMemberInfo`。 
在 `JMSGGroupMemberInfo` 类中包含了群成员 `JMSGUser` 对象、群昵称、入群时间、成员角色等属性。

***JMSGGroupMemberInfo***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性</th>
      <th width="40px">类型</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >user</td>
      <td >JMSGUser</td>
      <td >成员用户信息</td>
    </tr>
	<tr >
      <td >ctime</td>
      <td >UInt64</td>
      <td >入群时间</td>
    </tr>
	<tr >
      <td >groupNickname</td>
      <td >NSString</td>
      <td >群成员群昵称</td>
    </tr>
	<tr >
      <td >memberType</td>
      <td >JMSGGroupMemberType</td>
      <td >群成员身份，0：普通成员 1：群主 2：管理员</td>
    </tr>
  </table>
</div>

### 群成员管理
#### 获取群成员列表

```
/*!
 * @abstract 获取所有群成员信息列表
 *
 * @handler 成员列表. 类型为 NSArray，里面元素为 JMSGGroupMemberInfo.
 *
 * @discussion 返回数据中的 JMSGGroupMemberInfo 包含了成员 user 信息、入群时间、群昵称等
 */
- (void)memberInfoList:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 添加群成员
***注意：*** reason 字段只对公开群起作用

```
/*!
 * @abstract 添加群组成员
 *
 * @param usernameArray 用户名数组。数组里的成员类型是 NSString
 * @param userAppKey    用户的 AppKey，这批添加的成员必须在同一个 AppKey 下的用户
 * @param reason        邀请原因，可选
 *
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)addMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                             appKey:(NSString *JMSG_NULLABLE)userAppKey
                             reason:(NSString *JMSG_NULLABLE)reason
                  completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 删除群成员

```
/*!
 * @abstract 删除群组成员
 *
 * @param usernameArray 用户名数据. 数组里的成员类型是 NSString
 * @param handler 结果回调。正常返回时 resultObject 为 nil.
 */
- (void)removeMembersWithUsernameArray:(NSArray JMSG_GENERIC(__kindof NSString *) *)usernameArray
                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 移交群主

```
/*!
 * @abstract 移交群主
 *
 * @param username 新群主用户名
 * @param appkey   新群主用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 */
- (void)transferGroupOwnerWithUsername:(NSString *JMSG_NONNULL)username
                                appKey:(NSString *JMSG_NULLABLE)appkey
                     completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
#### 设置群成员昵称

```
/*!
 * @abstract 设置成员群昵称
 *
 * @param nickname 群昵称
 * @param username 目标用户的 username
 * @param appKey   目标用户的 appKey,若传入空则默认使用本应用appKey
 */
- (void)setGroupNickname:(NSString *JMSG_NULLABLE)nickname
                username:(NSString *JMSG_NONNULL)username
                  appKey:(NSString *JMSG_NULLABLE)appKey
                 handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 群组管理员
+ 范围：私有群和公开群都增加管理员角色。
+ 描述：仅群主可对群管理员进行管理，可指定群内任意成员成为管理员，也可取消管理员身份。
+ 管理员权限：拥有普通群成员的所有基础功能和权限，除此之外还拥有更高的权限:设置禁言、审批入群.

#### 获取管理员列表

```
/*!
 * @abstract 管理员列表
 *
 * @return 管理员列表. NSArray 里成员类型是 JMSGUser
 *
 * @discussion 注意：返回列表中不包含群主；仅在获取群成员成功后此接口才有效
 */
- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)groupAdminMembers;
```

#### 添加管理员

```
/*!
 * @abstract 添加管理员
 *
 * @param usernames 用户名列表
 * @param appkey   用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 注意：非 VIP 应用最多设置 15 个管理员，不包括群主本身
 */
- (void)addGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                            appKey:(NSString *JMSG_NULLABLE)appkey
                 completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```
    
#### 删除管理员

```
/*!
 * @abstract 删除管理员
 *
 * @param usernames 用户名 列表
 * @param appkey   用户 AppKey，不填则默认为本应用 AppKey
 * @param handler 结果回调。error 为 nil 表示成功.
 */
- (void)deleteGroupAdminWithUsernames:(NSArray <__kindof NSString *>*)usernames
                               appKey:(NSString *JMSG_NULLABLE)appkey
                    completionHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 群消息屏蔽
群组被设置为屏蔽之后，将收不到该群的消息。但是群成员变化事件还是能正常收到  

#### 设置群消息屏蔽

```
/*!
 * @abstract 设置群组消息屏蔽
 *
 * @param isShield 是否群消息屏蔽 YES:是 NO: 否
 * @param handler 结果回调。回调参数： error 为 nil, 表示设置成功
 *
 * @discussion 针对单个群组设置群消息屏蔽
 */
- (void)setIsShield:(BOOL)isShield handler:(JMSGCompletionHandler)handler;
```

#### 判断群组是否被屏蔽

```
/*!
 * @abstract 该群是否已被设置为消息屏蔽
 *
 * @discussion YES:是 , NO: 否
 */
@property(nonatomic, assign, readonly) BOOL isShieldMessage;
```

#### 获取当前用户的群屏蔽列表

```
/*!
 * @abstract 获取所有设置群消息屏蔽的群组
 *
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGGroup
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 从服务器获取，返回所有设置群消息屏蔽的群组。
 */
+ (void)shieldList:(JMSGCompletionHandler)handler;
```


### <span id="group-@function">群组@功能</span>
消息发送方可以发一条带有@list的消息。 接收方收到带有@list的消息之后，如果@list中包含了自己，则在sdk默认弹出的通知栏提示中会有相应的提示，如"xxx在群中@了你"。

#### 创建@群成员的消息
JMSGMessage


```
/*!
 * @abstract 创建@人的群聊消息
 *
 * @param content 消息内容对象
 * @param groupId 群聊ID
 * @param at_list @对象的数组
 *
 * #### 注意：
 *
 * 1、单独调用此接口创建消息，SDK 不会本地保存消息，再调用发送接口时才会保存；
 *
 * 2、如果上层希望创建消息时就本地化保存，请使用 [JMSGConversation createMessageWithContent:]
 */
+ (JMSGMessage *)createGroupMessageWithContent:(JMSGAbstractContent *)content
                                       groupId:(NSString *)groupId
                                       at_list:(NSArray<__kindof JMSGUser *> *)at_list;
```

#### 创建@全体群成员的消息

JMSGMessage

```
/*!
 * @abstract 创建@所有人的群聊消息
 *
 * @param content 消息内容对象
 * @param groupId 群聊ID
 *
 * #### 注意：
 *
 * 1、单独调用此接口创建消息，SDK 不会本地保存消息，再调用发送接口时才会保存；
 *
 * 2、如果上层希望创建消息时就本地化保存，请使用 [JMSGConversation createMessageWithContent:]
 */
+ (JMSGMessage *)createGroupAtAllMessageWithContent:(JMSGAbstractContent *)content
                                            groupId:(NSString *)groupId;
```

#### 判断消息是否@了自己
JMSGMessage

```
/*!
 * @abstract 是否是@自己的消息（只针对群消息，单聊消息无@功能）
 */
- (BOOL)isAtMe;
```

#### 判断消息是否是@全体成员
JMSGMessage

```
/*!
 * @abstract 是否是@所有人的消息（只针对群消息，单聊消息无@功能）
 */
- (BOOL)isAtAll;
```

#### 获取消息中@的群成员列表
JMSGMessage

```
/*!
 * @abstract 获取消息体中所有@对象（只针对群消息，单聊消息无@功能）
 *
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser
 * 注意：如果该消息为@所有人消息时，resultObject 返回nil，可以通过 isAtAll 接口来判断是否是@所有人的消息
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示获取成功
 * 如果 error 不为 nil,表示获取失败
 *
 * @discussion 从服务器获取，返回消息的所有@对象。
 */
- (void)getAt_List:(JMSGCompletionHandler)handler;
```

#### 发送@人消息
JMSGConversation

```
/*!
 * @abstract 发送@人消息（已经创建好对象的）
 *
 * @param message 通过消息创建类接口，创建好的消息对象
 * @param userList @对象的数组
 *
 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 JMSGMessageDelegate中的onReceiveMessage: error:方法来注册消息发送结果
 */
- (void)sendMessage:(JMSGMessage *)message at_list:(NSArray<__kindof JMSGUser *> *)userList;
```

#### 发送@所有人消息
JMSGConversation

```
/*!
 * @abstract 发送@所有人消息（已经创建好对象的）
 *
 * @param message 通过消息创建类接口，创建好的消息对象
 *
 * @discussion 发送消息的多个接口，都未在方法上直接提供回调。你应通过 JMSGMessageDelegate中的onReceiveMessage: error:方法来注册消息发送结果
 */
- (void)sendAtAllMessage:(JMSGMessage *)message;
```


### <span id="ApplyAndProcess">入群申请和审批</span>
申请入群和审批，适用于[公开群组](#PublicGroup)。

#### 申请入群

```
/*!
 * @abstract 申请加入群组
 *
 * @param gid     群组 gid
 * @param reason   申请原因
 * @param handler 结果回调
 *
 * @discussion 只有公开群需要申请才能加入，私有群不需要申请。
 */
+ (void)applyJoinGroupWithGid:(NSString *JMSG_NONNULL)gid
                       reason:(NSString *JMSG_NULLABLE)reason
            completionHandler:(JMSGCompletionHandler)handler;
```

##### 申请入群事件
申请入群事件`JMSGApplyJoinGroupEvent`，收到群成员申请入群通知时，SDK 将会抛出此事件通知上层。
具体处理方法见[事件处理](./event#apply-join-group)一节。


#### 管理员审批入群申请

```
/*!
 * @abstract 管理员审批入群申请
 *
 * @patam eventId     入取申请事件的 id，详情请查看 JMSGApplyJoinGroupEvent 类
 * @param gid         群组 gid
 * @param joinUser    入群的用户
 * @param applyUser   发起申请的的用户，如果是主动申请入群则和 member 是相同的
 * @param isAgree     是否同意申请，YES : 同意， NO: 不同意
 * @param reason      拒绝申请的理由，选填
 * @param handler     结果回调
 *
 * @discussion 只有管理员才有权限审批入群申请，SDK 不会保存申请入群事件(JMSGApplyJoinGroupEvent)，上层可以自己封装再保存，或则归档直接保存，以便此接口取值调用。
 */
+ (void)processApplyJoinGroupEventID:(NSString *JMSG_NONNULL)eventId
                                 gid:(NSString *JMSG_NONNULL)gid
                            joinUser:(JMSGUser *JMSG_NONNULL)joinUser
                           applyUser:(JMSGUser *JMSG_NONNULL)applyUser
                             isAgree:(BOOL)isAgree
                              reason:(NSString *JMSG_NULLABLE)reason
                             handler:(JMSGCompletionHandler)handler;
```

通过接收到的`JMSGApplyJoinGroupEvent `进行审批操作,审批不能多人操作，当一人同意或拒绝后其他管理者或群主会收到 `JMSGGroupAdminApprovalEvent `


##### 管理员审批事件通知
+ 管理员拒绝入群申请事件 `JMSGGroupAdminRejectApplicationEvent`
+ 管理员审批事件 `JMSGGroupAdminApprovalEvent`，只有管理员会收到此事件

当有一个群管理员或群主审批过群成员审批事件， SDK 将会抛出此类事件通知上层,
只有该审批事件对应群的群主和群管理员会收到此事件。具体处理方法见[事件处理](./event#admin-reject-application)一节

### 群成员禁言
禁言后用户可正常接收消息，但无法向被禁言的群组中发送消息，解禁后可正常发送消息。
#### 群成员禁言状态设置

```
/*!
 * @abstract 群成员禁言设置
 *
 * @param isSilence 是否禁言， YES:是 NO: 否
 * @param username  待设置的用户的 username
 * @param username  带待设置的用户的 appKey,若传入空则默认使用本应用appKey
 * @param handler   结果回调
 *
 * @discussion 注意: 目前 SDK 只支持群主设置群里某个用户禁言
 */
- (void)setGroupMemberSilence:(BOOL)isSilence
                     username:(NSString *JMSG_NONNULL)username
                       appKey:(NSString *JMSG_NULLABLE)appKey
                      handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 获取禁言列表

```
/*!
 * @abstract 禁言列表
 *
 * @return 禁言的成员列表. NSArray 里成员类型是 JMSGUser
 *
 * @discussion 仅在获取群成员成功后此接口才有效
 */
- (NSArray JMSG_GENERIC(__kindof JMSGUser *)*)groupSilenceMembers;
```

#### 判断用户是否被禁言

```
/*!
 * @abstract 判断用户在该群内是否被禁言
 *
 * @param username  待判断用户的用户名
 * @param appKey    待判断用户的appKey，若传入空则默认使用本应用appKey
 */
- (BOOL)isSilenceMemberWithUsername:(NSString *JMSG_NONNULL)username
                             appKey:(NSString *JMSG_NULLABLE)appKey;
```

### 群公告
+ 支持群主和管理员进行发布、删除、置顶和取消置顶操作；
+ 目前单个群最大群公告数量为 100

***JMSGGroupAnnouncement***

<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="20px">属性/方法</th>
      <th width="40px">类型/返回值</th>
      <th width="300px">说明</th>
    </tr>
	<tr >
      <td >announcementId</td>
      <td >UInt32</td>
      <td >公告 id</td>
    </tr>
	<tr >
      <td >gid</td>
      <td >NSString</td>
      <td > 群组 id</td>
    </tr>
	<tr >
      <td >text</td>
      <td >NSString</td>
      <td > 公告内容</td>
    </tr>
	<tr >
      <td >publisher</td>
      <td >JMSGUser</td>
      <td >发布者</td>
    </tr>
	<tr >
      <td >publishTime</td>
      <td >UInt64</td>
      <td >发布时间</td>
    </tr>
	<tr >
      <td >isTop</td>
      <td >BOOL</td>
      <td >是否置顶</td>
    </tr>
	<tr >
      <td >topTime</td>
      <td >UInt64</td>
      <td >置顶时间</td>
    </tr>
	<tr >
      <td > toJsonString </td>
      <td > NSString</td>
      <td > 公告对象转换为 JSON 字符串</td>
    </tr>
	<tr >
      <td > fromJson: </td>
      <td > JMSGGroupAnnouncement</td>
      <td >将合法的 json 字符串转为公告对象</td>
    </tr>
  </table>
</div>


#### 发布群公告
发布群公告时，开发者可选择是否发送群消息通知群成员，或者自己定制消息通知其他群成员。

```
/*!
 * @abstract 发布群公告
 *
 * @param announcement 公告内容，大小必须在 1KB 以内
 * @param sendMessage 发布成功后是否需要发一条消息通知群成员，默认：YES
 * @param handler 结果回调。resultObject 为 JMSGGroupAnnouncement对象， error 为 nil 表示成功.
 *
 * @discussion
 * #### 注意：
 *
 * 如果 sendMessage = NO，则 SDK 不会自动发送消息，上层可以在回调或者收到事件后，自己发送消息；
 * 如果 sendMessage = YES，则在发布公告成功后 SDK 会自动在群里发布一条文本消息，文本内容就是公告内容，另外消息的 extras 里会附带公告的相关数据，上层可根据此数据将 message 对应到相应的公告， extras 里的 key-value 如下，
 *
 *    ```
 *    key(String)       = "jmessage_group_announcement"
 *    value(JsonString) = {
 *                        "id" : 公告 id,
 *                        "text" : 公告内容 text,
 *                        "publisher_uid" : 发布者 uid,
 *                        "ctime" : 公告发布时间,
 *                        "isTop" : 是否置顶,
 *                        "topTime" : 置顶时间,
 *                        "gid" : 群 gid
 *                      }
 *    ```
 * 群公告最多100条，发布公告后会有对应事件下发，上层通过 [JMSGGroupDelegate onReceiveGroupAnnouncementEvents:] 监听
 *
 * @since 3.8.0
 */
- (void)publishGroupAnnouncement:(NSString *JMSG_NONNULL)announcement
                     sendMessage:(BOOL)sendMessage
                         handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 获取群公告

```
/*!
 * @abstract 获取群公告列表
 *
 * @param handler 结果回调。resultObject 是 NSArray 类型，元素是 JMSGGroupAnnouncement
 *
 * @since 3.8.0
 */
- (void)groupAnnouncementList:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```


#### 删除群公告

```
/*!
 * @abstract 删除群公告
 *
 * @param announcementID 公告id
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 删除公告后会有对应事件下发，上层通过 [JMSGGroupDelegate onReceiveGroupAnnouncementEvents:] 监听
 * @since 3.8.0
 */
- (void)deleteGroupAnnouncement:(NSString *JMSG_NONNULL)announcementID
                        handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```


#### 置顶群公告

```
/*!
 * @abstract 置顶/取消置顶 群公告
 *
 * @param isTop 置顶参数，YES:置顶，NO:取消置顶
 * @param ID    公告 id
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 置顶公告后会有对应事件下发，上层通过 [JMSGGroupDelegate onReceiveGroupAnnouncementEvents:] 监听
 * @since 3.8.0
 */
- (void)setGroupAnnouncementTop:(BOOL)isTop
                 announcementID:(NSString *JMSG_NONNULL)ID
                        handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

### 群组黑名单
+ 由群主和管理员管理，被拉入黑名单用户会被主动踢出群组，且无法再次加入

#### 黑名单列表

```
/*!
 * @abstract 群黑名单列表
 *
 * @handler 结果回调. resultObject 是 NSArray 类型，元素是 JMSGUser
 *
 * @since 3.8.0
 */
- (void)groupBlacklistHandler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 添加黑名单

```
/*!
 * @abstract 添加群黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @discussion 黑名单上限100个，超出将无法设置成功，被拉入黑名单用户会被主动踢出群组，且无法再次加入.
 * @since 3.8.0
 */
- (void)addGroupBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                                appKey:(NSString *JMSG_NULLABLE)appKey
                               handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```

#### 移除黑名单

```
/*!
 * @abstract 删除群黑名单
 *
 * @param usernames 用户名列表
 * @param appkey   用户 appKey，usernames 中的所有用户必须在同一个 AppKey 下，不填则默认为本应用 appKey
 * @param handler 结果回调。error 为 nil 表示成功.
 *
 * @since 3.8.0
 */
- (void)deleteGroupBlacklistWithUsernames:(NSArray <__kindof NSString *>*)usernames
                                   appKey:(NSString *JMSG_NULLABLE)appKey
                                  handler:(JMSGCompletionHandler JMSG_NULLABLE)handler;
```


### 群组免打扰
#### 是否设置免打扰
```
/*!
 * @abstract 该群是否已被设置为免打扰
 *
 * @discussion YES:是 , NO: 否
 */
@property(nonatomic, assign, readonly) BOOL isNoDisturb;
```

#### 设置免打扰

```
/*!
 * @abstract 设置群组消息免打扰（支持跨应用设置）
 *
 * @param isNoDisturb 是否免打扰 YES:是 NO: 否
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 相应对象
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 针对单个群组设置免打扰
 * 这个接口支持跨应用设置免打扰
 */
- (void)setIsNoDisturb:(BOOL)isNoDisturb handler:(JMSGCompletionHandler)handler;
```
#### 获取免打扰列表

```
/*!
 * @abstract 用户免打扰列表
 *
 * @param handler 结果回调。回调参数：
 *
 * - resultObject 类型为 NSArray，数组里成员的类型为 JMSGUser、JMSGGroup
 * - error 错误信息
 *
 * 如果 error 为 nil, 表示设置成功
 * 如果 error 不为 nil,表示设置失败
 *
 * @discussion 从服务器获取，返回用户的免打扰列表。
 * 建议开发者在 SDK 完全启动之后，再调用此接口获取数据
 */
+ (void)noDisturbList:(JMSGCompletionHandler)handler;
```
