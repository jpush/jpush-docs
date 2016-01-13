## IM SDK ErrorCode 定义

以下列表里的 ErrorCode 有可能在 SDK 的调用过程中出现。供参考理解其含义。

#### JMessage iOS

只会出现在 iOS SDK 里的错误码。

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th>Error Message</th>
			<th>说明</th>
		</tr>
		
		
    <tr>
      <td>860015</td>
      <td>Network downloading media failed.</td>
      <td>媒体文件下载失败</td>
    </tr>
    <tr>
      <td>860018</td>
      <td>Network uploading media failed</td>
      <td>媒体文件上传失败</td>
    </tr>
    <tr>
      <td>860020</td>
      <td>Getting upload token failed</td>
      <td>获取媒体文件上传 token 失败</td>
    </tr>
    <tr>
      <td>860021</td>
      <td>Network result is invalid</td>
      <td>服务器端返回的数据非预期</td>
    </tr>
    
    <tr>
      <td>861004</td>
      <td>DB Migrating failed</td>
      <td>SDK数据库升级失败</td>
    </tr>
    <tr>
      <td>861100</td>
      <td>Appkey is invalid</td>
      <td>Appkey 不合法</td>
    </tr>
    <tr>
      <td>861101</td>
      <td>Internal param check failure</td>
      <td>内部参数校验出错</td>
    </tr>
    <tr>
      <td>863001</td>
      <td>Username is invalid</td>
      <td>无效的用户名</td>
    </tr>
    <tr>
      <td>863002</td>
      <td>Password is invalid</td>
      <td>无效的密码</td>
    </tr>
    <tr>
      <td>863004</td>
      <td>User is not at Login state</td>
      <td>用户未在登录状态</td>
    </tr>
    <tr>
      <td>864001</td>
      <td>It is not a media message</td>
      <td>不是媒体消息</td>
    </tr>
    <tr>
      <td>864002</td>
      <td>Media resource is missing</td>
      <td>媒体资源意外丢失</td>
    </tr>
    <tr>
      <td>864003</td>
      <td>Media crc32 code is invalid</td>
      <td>媒体CRC码无效</td>
    </tr>
    <tr>
      <td>864004</td>
      <td>Media crc check failure</td>
      <td>媒体CRC校验失败</td>
    </tr>
    <tr>
      <td>864005</td>
      <td>Uploading media file is empty</td>
      <td>上传的媒体文件意外丢失</td>
    </tr>
    <tr>
      <td>865001</td>
      <td>Message content is invalid</td>
      <td>无效的消息内容</td>
    </tr>
    <tr>
      <td>865002</td>
      <td>Message is nil</td>
      <td>消息为空</td>
    </tr>
    <tr>
      <td>865003</td>
      <td>Message is not prepared for sending</td>
      <td>消息未满足发送的条件</td>
    </tr>
    <tr>
      <td>865004</td>
      <td>You are not in the group for sending message</td>
      <td>你不是发送群聊消息的群组成员</td>
    </tr>
    <tr>
      <td>866001</td>
      <td>Unknown conversation type</td>
      <td>未知的会话类型</td>
    </tr>
    <tr>
      <td>866002</td>
      <td>Conversation username is invalid</td>
      <td>单聊会话用户名无效</td>
    </tr>
    <tr>
      <td>866003</td>
      <td>Conversation groupId is invalid</td>
      <td>群聊会话群组ID无效</td>
    </tr>
    <tr>
      <td>867001</td>
      <td>GroupId is invalid</td>
      <td>无效的群组ID</td>
    </tr>
    <tr>
      <td>867002</td>
      <td>Group fields are invalid</td>
      <td>群组字段无效</td>
    </tr>
    <tr>
      <td>869999</td>
      <td>Unknown SDK error</td>
      <td>未知的SDK错误码</td>
    </tr>


    
</table>
</div>

#### JMessage Android

只会出现在 Android SDK 里的错误码。

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th>Error Message</th>
			<th>说明</th>
		</tr>
	<tr >
	  <td>0</td>
	  <td>Success</td>
	  <td>成功</td>
	</tr>
    <tr >
      <td>871101</td>
      <td></td>
      <td>请求参数不合法</td>
    </tr>
    <tr >
      <td>871102</td>
      <td></td>
      <td>请求失败，请检查网络</td>
    </tr>
    <tr >
      <td>871103</td>
      <td></td>
      <td>服务器内部错误</td>
    </tr>
    <tr >
      <td>871104</td>
      <td></td>
      <td>服务器内部错误</td>
    </tr>
    <tr >
      <td>871201</td>
      <td></td>
      <td>响应超时</td>
    </tr>
    <tr >
      <td>871300</td>
      <td></td>
      <td>api调用发起者尚未登录</td>
    </tr>
    <tr >
      <td>871301</td>
      <td></td>
      <td>api调用传入的参数不合法</td>
    </tr>
    <tr >
      <td>871302</td>
      <td></td>
      <td>发送消息的消息体过大，整个消息体大小不能超过4k</td>
    </tr>
    <tr >
      <td>871303</td>
      <td></td>
      <td>用户名不合法</td>
    </tr>
    <tr >
      <td>871304</td>
      <td></td>
      <td>密码不合法</td>
    </tr>
    <tr >
      <td>871305</td>
      <td></td>
      <td>名称不合法（包括nickname groupname notename）  </td>
    </tr>
    <tr >
      <td>871306</td>
      <td></td>
      <td>其他输入不合法</td>
    </tr>
    <tr >
      <td>871307</td>
      <td></td>
      <td>添加或移除群成员时，传入的成员列表中有用户不存在</td>
    </tr>
    <tr >
      <td>871308</td>
      <td></td>
      <td>SDK尚未初始化</td>
    </tr>
    <tr >
      <td>871309</td>
      <td></td>
      <td>消息中包含的文件不存在</td>
    </tr>
    <tr >
      <td>871310</td>
      <td></td>
      <td>网络连接已断开，请检查网络</td>
    </tr>
    <tr >
      <td>871311</td>
      <td></td>
      <td>用户未设定头像，下载头像失败</td>
    </tr>
    <tr >
      <td>871312</td>
      <td></td>
      <td>创建ImageContent失败</td>
    </tr>
    <tr >
      <td>871402</td>
      <td></td>
      <td>文件上传失败</td>
    </tr>
    <tr >
      <td>871403</td>
      <td></td>
      <td>文件上传失败</td>
    </tr>
    <tr >
      <td>871404</td>
      <td></td>
      <td>文件下载失败</td>
    </tr>
    <tr >
      <td>871501</td>
      <td></td>
      <td>appkey与包名不匹配或者token无效</td>
    </tr>
    <tr >
      <td>871502</td>
      <td></td>
      <td>appkey无效</td>
    </tr>
    <tr >
      <td>871503</td>
      <td></td>
      <td>appkey与platform不匹配</td>
    </tr>
	</table>
</div>

#### Server Error 

JMessage 服务器端报的错误码。有可能出现在各平台的 SDK 里。

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th>Error Message</th>
			<th>说明</th>
		</tr>
		<tr >
			<td>898000</td>
			<td>Server internal error</td>
			<td>内部错误</td>
		</tr>
		<tr >
			<td>898001</td>
			<td>User exists</td>
			<td>用户已存在</td>
		</tr>
		<tr >
			<td>898002</td>
			<td>No sush user</td>
			<td>用户不存在</td>
		</tr>
		<tr >
			<td>898003</td>
			<td>Parameter invalid!</td>
			<td>请求参数不合法 </td>
		</tr>
		<tr >
			<td>898004</td>
			<td>Password error</a></td>
			<td>更新密码操作，用户密码错误</td>
		</tr>
		<tr >
			<td>898006</td>
			<td>Gid invalid</td>
			<td>Gid不存在</td>
		</tr>
		<tr >
			<td>898007</td>
			<td>Missing authen info</td>
			<td>校验信息为空</td>
		</tr>
		<tr >
			<td>898008</td>
			<td>Basic authentication failed.</td>
			<td>校验失败</td>
		</tr>
		<tr >
			<td>898009</td>
			<td>Appkey not exists</td>
			<td>appkey不存在</td>
		</tr>
		<tr >
			<td>898030</td>
			<td>Server response time out, please try again later</td>
			<td>系统繁忙，稍后重试</td>
		</tr>
		<tr >
			<td>899000</td>
			<td>Server internal error</td>
			<td>系统内部错误</td>
		</tr>
		<tr >
			<td>899001</td>
			<td>User exist</td>
			<td>用户已存在</td>
		</tr>
		<tr >
			<td>899002</td>
			<td>No such user</td>
			<td>用户不存在</td>
		</tr>
		<tr >
			<td>899003</td>
			<td>parameter invalid</td>
			<td>参数错误，Request Body参数不符合要求;resend 值不符合要求;用户名或者密码不合法;群组Gid不合法</td>
		</tr>
		<tr >
			<td>899007</td>
			<td>Missing authen info</td>
			<td>校验信息为空</td>
		</tr>
		<tr >
			<td>899008</td>
			<td>Basic authentication failed</td>
			<td>校验失败</td>
		</tr>
		<tr >
			<td>899009</td>
			<td>Appkey not exit</td>
			<td>Appkey不存在</td>
		</tr>
		<tr >
			<td>899011</td>
			<td>Repeat to add the members</td>
			<td>重复添加群成员</td>
		</tr>
		<tr >
			<td>899012</td>
			<td>No enough space for members</td>
			<td>没有足够位置添加此次请求的成员</td>
		</tr>
		<tr >
			<td>899013</td>
			<td>User list is bigger than 500</td>
			<td>注册列表大于500，批量注册最大长度为500</td>
		</tr>
		<tr >
			<td>899014</td>
			<td>User list is bigger than 500</td>
			<td>添加操作操作成功 remove操作有username不存在讨论组中 remove失败</td>
		</tr>
		<tr >
			<td>899015</td>
			<td>User 's group are 100 can not continue</td>
			<td>用户加入讨论组达到上限</td>
		</tr>
		<tr >
			<td>899016</td>
			<td>No authority to send message</td>
			<td>用户没有管理员权限发送信息</td>
		</tr>
		<tr >
			<td>899017</td>
			<td>There are usernames exist in blacklist</td>
			<td>用户已经被添加进黑名单</td>
		</tr>
		<tr >
			<td>899018</td>
			<td>Admin can not be added into blacklist</td>
			<td>管理员不能被添加进黑名单</td>
		</tr>
		<tr >
			<td>899019</td>
			<td>Here are usernames not exist in blacklist</td>
			<td>删除目标黑名单用户不存在黑名单中</td>
		</tr>
		<tr >
			<td>899030</td>
			<td>Server response time out, please try again later</td>
			<td>系统繁忙，稍后重试</td>
		</tr>
		<tr >
			<td>800003</td>
			<td>Appkey not register</td>
			<td>appkey未注册</td>
		</tr>
		<tr >
			<td>800005</td>
			<td>User id not register</td>
			<td>用户ID未注册（appkey无该UID）</td>
		</tr>
		<tr >
			<td>800006</td>
			<td>User id not exist</a></td>
			<td>用户ID不存在（数据库中无该UID）</td>
		</tr>
		<tr >
			<td>800009</td>
			<td>System error</td>
			<td>服务器系统错误</td>
		</tr>
		<tr >
			<td>800010</td>
			<td>Sync couchbase error</td>
			<td>服务器系统错误</td>
		</tr>
		<tr >
			<td>800011</td>
			<td>Sync mysql error</td>
			<td>服务器系统错误</td>
		</tr>
		<tr >
			<td>800012</td>
			<td>user logout</td>
			<td>发起的用户处于登出状态，账号可能从未登录过，或者被踢下线</td>
		</tr>
		<tr >
			<td>800013</td>
			<td>User offline</td>
			<td>发起的用户处于离线状态</td>
		</tr>
		<tr >
			<td>800014</td>
			<td>Appkey not match</td>
			<td>发起的用户appkey与目标不匹配</td>
		</tr>
		<tr >
			<td>801003</td>
			<td>Invalid user name or password</td>
			<td>登录的用户名未注册，登录失败</td>
		</tr>
		<tr >
			<td>801004</td>
			<td>Invalid user name or password</td>
			<td>登录的用户密码错误，登录失败</td>
		</tr>
		<tr >
			<td>803001</td>
			<td></td>
			<td>发送消息失败，状态存储异常</td>
		</tr>
		<tr >
			<td>803002</td>
			<td></td>
			<td>发送消息失败，系统网络异常</td>
		</tr>
		<tr >
			<td>803003</td>
			<td></td>
			<td>发送消息失败，目标用户未注册或不存在</td>
		</tr>
		<tr >
			<td>803004</td>
			<td></td>
			<td>发送消息失败，目标讨论组不存在</td>
		</tr>
		<tr >
			<td>803005</td>
			<td></td>
			<td>发送消息失败，发起者不在目标讨论组中</td>
		</tr>
		<tr >
			<td>803006</td>
			<td></td>
			<td>发送消息失败，发起者权限不够或者类别不匹配</td>
		</tr>
		<tr >
			<td>803007</td>
			<td></td>
			<td>发送消息失败，消息长度超过限制</td>
		</tr>
		<tr >
			<td>803008</td>
			<td></td>
			<td>发送消息失败，发送者已被接收者拉入黑名单，仅限单聊</td>
		</tr>
		<tr >
			<td>808002</td>
			<td>User have not right to create group</td>
			<td>用户无创建讨论组权限，创建讨论组失败</td>
		</tr>
		<tr >
			<td>808003</td>
			<td>The amount of group exceed limit</td>
			<td>用户拥有的讨论组数量已达上限,无法再创建</td>
		</tr>
		<tr >
			<td>809002</td>
			<td>User not in the group</td>
			<td>用户退出讨论组时，用户不在该讨论组中，退出讨论组失败</td>
		</tr>
		<tr >
			<td>810003</td>
			<td>User not in the group</td>
			<td>用户添加成员到讨论组时，用户不在该讨论组中，添加成员失败</td>
		</tr>
		<tr >
			<td>810004</td>
			<td>User not have right of group to add member</td>
			<td>用户添加成员到讨论组时，用户没有往讨论组中添加成员的权限，添加成员失败</td>
		</tr>
		<tr >
			<td>810005</td>
			<td>Member not register</td>
			<td>用户添加成员到讨论组时，添加的成员列表中有成员未注册，添加成员失败</td>
		</tr>
		<tr >
			<td>810006</td>
			<td>User have not right to add member in the group</td>
			<td>用户添加成员到讨论组时，添加的成员列表中有成员该用户没有权限进行添加，添加成员失败</td>
		</tr>
		<tr >
			<td>810007</td>
			<td>Member repeated add</td>
			<td>用户添加成员到讨论组时，添加的成员列表中有成员重复添加，添加成员失败</td>
		</tr>
		<tr >
			<td>810008</td>
			<td>The amount of member exceed group limit</td>
			<td>用户添加成员到讨论组时，添加的成员数量超出讨论组拥有的最大成员数上限，添加成员失败</td>
		</tr>
		<tr >
			<td>810009</td>
			<td>The amount of group exceed member limit</td>
			<td>用户添加成员到讨论组时，添加的成员列表中有成员拥有的讨论组数量已达上限，添加成员失败</td>
		</tr>
		<tr >
			<td>811003</td>
			<td>User not in the group</td>
			<td>用户删除讨论组成员时，用户不在该讨论组中，删除成员失败</td>
		</tr>
		<tr >
			<td>811004</td>
			<td>User not have right of group to remove member</td>
			<td>用户删除讨论组成员时，用户没有删除讨论组中成员的权限，删除成员失败</td>
		</tr>
		<tr >
			<td>811005</td>
			<td>Member not register</td>
			<td>用户删除讨论组成员时，删除的成员列表中有成员未注册，删除成员失败</td>
		</tr>
		<tr >
			<td>811006</td>
			<td>User have not right to remove member from the group</td>
			<td>用户删除讨论组成员时，删除的成员列表中有成员该用户没有权限进行删除，删除成员失败</td>
		</tr>
		<tr >
			<td>811007</td>
			<td>Member repeated remove</td>
			<td>用户删除讨论组成员时，删除的成员列表中有成员重复删除，删除成员失败</td>
		</tr>
		<tr >
			<td>811008</td>
			<td>Member not in the group</td>
			<td>用户删除讨论组成员时，删除的成员列表中有成员不在该讨论组中，删除成员失败</td>
		</tr>
		<tr >
			<td>812001</td>
			<td>group id not exist</td>
			<td>用户修改讨论组信息时，讨论组ID不存在，修改讨论组信息失败</td>
		</tr>
		<tr >
			<td>812002</td>
			<td>User not in the group</td>
			<td>用户修改讨论组信息时，用户不在该讨论组中，修改讨论组信息失败</td>
		</tr>
		<tr >
			<td>812003</td>
			<td>length of group name exceed limit</td>
			<td>用户修改讨论组信息时，讨论组名超出长度上限，修改讨论组信息失败</td>
		</tr>
		<tr >
			<td>812004</td>
			<td>length of group desc exceed limit</td>
			<td>用户修改讨论组信息时，讨论组描述超出上限，修改讨论组信息失败</td>
		</tr>
		<tr >
			<td>818001</td>
			<td></td>
			<td>用户添加黑名单时，成员列表为空，添加失败</td>
		</tr>
		<tr >
			<td>818002</td>
			<td></td>
			<td>用户添加黑名单时，成员列表中有成员不存在，添加失败</td>
		</tr>
		<tr >
			<td>818003</td>
			<td></td>
			<td>用户添加黑名单时，成员列表中有成员不能被添加，添加失败</td>
		</tr>
		<tr >
			<td>819001</td>
			<td></td>
			<td>用户移除好友出黑名单时，成员列表为空，操作失败</td>
		</tr>


</table>
</div>



