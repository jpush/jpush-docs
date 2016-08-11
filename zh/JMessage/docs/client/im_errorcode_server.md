## IM SDK ErrorCode 定义

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
			<td>Group id invalid</td>
			<td>Group id不存在</td>
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

			<td>898010</td>
			<td>Token expired</td>
			<td>API请求 token 过期。正常情况下SDK会自动重新获取 token。</td>
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
			<td>参数错误，Request Body参数不符合要求;resend 值不符合要求;用户名或者密码不合法;群组Group id不合法</td>
		</tr>
		<tr >
			<td>899006</td>
			<td>Group id invalid</td>
			<td>Group id 不存在</td>
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
			<td>800012</td>
			<td>user logout</td>
			<td>发起的用户处于登出状态，账号注册以后从未登录过，需要先登录</td>
		</tr>
		<tr >
			<td>800013</td>
			<td>user logout</td>
			<td>发起的用户处于登出状态，请求的用户已经登出，需要先登录</td>
		</tr>
		<tr >
			<td>800014</td>
			<td>Appkey not match</td>
			<td>发起的用户appkey与目标不匹配</td>
		</tr>
		<tr >
			<td>800016</td>
			<td>Devices not match</td>
			<td>发起的用户设备不匹配,当前请求的设备与上次登录的设备不匹配导致，需要先登录</td>
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
			<td>801005</td>
			<td>invalid device</td>
			<td>登录的用户设备有误，登录失败</td>
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
			<td>803010</td>
			<td></td>
			<td>发送消息失败，发送频率超过系统限制，无法发送，客户端限制每分钟60条</td>
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
			<td>808004</td>
			<td>length of group name exceed limit	</td>
			<td>讨论组名长度超出上限，创建讨论组失败</td>
		</tr>
		<tr >
			<td>808005</td>
			<td>length of group desc exceed limit</td>
			<td>讨论组描述长度超出上限，创建讨论组失败</td>
		</tr>
		<tr >
			<td>809001</td>
			<td>Group id not exist</td>
			<td>用户退出讨论组时，讨论组ID不存在，退出讨论组失败</td>
		</tr>
		<tr >
			<td>809002</td>
			<td>User not in the group</td>
			<td>用户退出讨论组时，用户不在该讨论组中，退出讨论组失败</td>
		</tr>
		<tr >
			<td>810001</td>
			<td>Group id not exist</td>
			<td>用户添加成员到讨论组时，讨论组ID不存在，添加成员失败</td>
		</tr>
		<tr >
			<td>810002</td>
			<td>zero member</td>
			<td>用户添加成员到讨论组时，添加的成员列表为空，添加成员失败</td>
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
			<td>811001</td>
			<td>Group id not exist</td>
			<td>用户删除讨论组成员时，讨论组ID不存在，删除成员失败</td>
		</tr>
		<tr >
			<td>811002</td>
			<td>Group id not exist</td>
			<td>用户删除讨论组成员时，删除的成员列表为空，删除成员失败</td>
		</tr>
		<tr >
			<td>811003</td>
			<td>zero member</td>
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
			<td>Group id not exist</td>
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
		<tr >
			<td>831001</td>
			<td>member already setted</td>
			<td>用户添加成员消息免打扰时，该成员已处于免打扰状态</td>
		</tr>
		<tr >
			<td>832001</td>
			<td>member never setted</td>
			<td>用户删除成员消息免打扰时，该成员不处于免打扰状态</td>
		</tr>
		<tr >
			<td>833001</td>
			<td>group not exist</td>
			<td>用户添加群组消息免打扰时，该群组不存在</td>
		</tr>
		<tr >
			<td>833002</td>
			<td>user not in group</td>
			<td>用户添加群组消息免打扰时，用户不存在该群组中</td>
		</tr>
		<tr >
			<td>833003</td>
			<td>group already setted</td>
			<td>用户添加群组消息免打扰时，该群组已处于免打扰状态</td>
		</tr>
		<tr >
			<td>834001</td>
			<td>group never setted</td>
			<td>用户删除群组消息免打扰时，该群组不处于免打扰状态</td>
		</tr>
		<tr >
			<td>835001</td>
			<td>already setted</td>
			<td>用户添加全局消息免打扰时，该用户已处于全局免打扰状态</td>
		</tr>
		<tr >
			<td>836001</td>
			<td>never setted</td>
			<td>用户删除全局消息免打扰时，该用户不处于全局免打扰状态</td>
		</tr>
</table>
</div>



