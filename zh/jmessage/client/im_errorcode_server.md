# IM SDK ErrorCode 定义

## Server Error 

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
			<td>User exist</td>
			<td>用户已存在</td>
		</tr>
		<tr >
			<td>898002</td>
			<td>No such user</td>
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
			<td>898011</td>
			<td>no auth to query other appkey's user or appkey no exist</td>
			<td>查询的appkey不具备跨应用权限 或者appkey不存在</td>
		</tr>
		<tr >
			<td>898030</td>
			<td>Server response time out, please try again later</td>
			<td>系统繁忙，稍后重试</td>
		</tr>
		<tr>
			<td>898031</td>
			<td>project not exist</td>
			<td>音视频服务还未开通，请参考doc和portal里的规则开通服务</td>
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
			<td>User 's group are full can not continue</td>
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
			<td>899020</td>
			<td>no auth to operating other appkey</td>
			<td>跨应用失败</td>
		</tr>
		
		<tr >
			<td>899021</td>
			<td>should use cross app api</td>
			<td>查询失败 应该使用跨应用api</td>
		</tr>
		
		<tr >
			<td>899043</td>
			<td>duplicate add user</td>
			<td>已经设置此用户为消息免打扰，重复设置错误</td>
		</tr>
		
		<tr >
			<td>899044</td>
			<td>user is not exist in setting</td>
			<td>取消消息免打扰用户时，该用户不存在当前设置中</td>
		</tr>
		
		<tr >
			<td>899045</td>
			<td>group is not exist</td>
			<td>设置群组消息免打扰时，群组不存在该系统中</td>
		</tr>
		
		<tr>
			<td>899046</td>
			<td>user is not in group</td>
			<td>设置群组消息免打扰时，设置的群组，用户不在该群组中</td>
		</tr>
		
		<tr>
			<td>899047</td>
			<td>duplicate add group</td>
			<td>已经设置此群组为消息免打扰，重复设置错误</td>
		</tr>
		
		<tr >
			<td>899048</td>
			<td>already open global</td>
			<td>已经设置全局为消息免打扰，重复设置错误</td>
		</tr>
		
		<tr>
			<td>899049</td>
			<td>group is not exist in setting</td>
			<td>取消消息免打扰群组时，该群组不存在当前设置中</td>
		</tr>
		
		<tr>
			<td>899050</td>
			<td>already close global</td>
			<td>已经设置全局为消息免打扰，重复设置错误</td>
		</tr>
		
		<tr>
			<td>899070</td>
			<td></td>
			<td>添加的好友已经存在好友列表中</td>
		</tr>
		
		<tr>
			<td>899071</td>
			<td></td>
			<td>更新的好友不存在好友列表中</td>
		</tr>
		
		<tr >
			<td>899030</td>
			<td>Server response time out, please try again later</td>
			<td>系统繁忙，稍后重试</td>
		</tr>
    <tr >
      <td>899081</td>
			<td>room id no exist</td>
			<td>聊天室ID不存在</td>
		</tr>
		<tr>
			<td>899082</td>
			<td>user not in room</td>
			<td>用户不在聊天室中</td>
		</tr>
		<tr >
			<td>800003</td>
			<td>appkey not exist</td>
			<td>appkey未注册</td>
		</tr>
		<tr >
			<td>800005</td>
			<td>user not exist</td>
			<td>用户ID未注册（appkey无该UID）</td>
		</tr>
		<tr >
			<td>800006</td>
			<td>user not exist</a></td>
			<td>用户ID不存在（数据库中无该UID）</td>
		</tr>
		<tr >
		    <td>800008</td>
			<td>invalid request</td>
			<td>请求类型无法识别</td>
		</tr>
		<tr >
			<td>800009</td>
			<td>system error</td>
			<td>服务器系统错误</td>
		</tr>
		<tr >
			<td>800012</td>
			<td>user never login</td>
			<td>发起的用户处于登出状态，账号注册以后从未登录过，需要先登录</td>
		</tr>
		<tr >
			<td>800013</td>
			<td>user logout</td>
			<td>发起的用户处于登出状态，请求的用户已经登出，需要先登录</td>
		</tr>
		<tr >
			<td>800014</td>
			<td>appkey not match</td>
			<td>发起的用户appkey与目标不匹配</td>
		</tr>
		<tr >
			<td>800016</td>
			<td>device not match</td>
			<td>发起的用户设备不匹配,当前请求的设备与上次登录的设备不匹配导致，需要先登录</td>
		</tr>
		<tr >
		    <td>800017</td>
			<td>beyond the frequency limit</td>
			<td>发送请求频率超过系统限制</td>
		</tr>
		<tr >
		    <td>800018</td>
			<td>group id not exist</td>
			<td>群组ID不存在</td>
		</tr>
		<tr >
		    <td>800019</td>
			<td>req user not in group</td>
			<td>请求用户不在群组中</td>
		</tr>
		<tr >
		    <td>800020</td>
			<td>request user no permission</td>
			<td>请求用户无操作权限</td>
		</tr>
		<tr >
			<td>801003</td>
			<td>user not exist</td>
			<td>登录的用户名未注册，登录失败</td>
		</tr>
		<tr >
			<td>801004</td>
			<td>invalid password</td>
			<td>登录的用户密码错误，登录失败</td>
		</tr>
		<tr >
			<td>801005</td>
			<td>invalid device</td>
			<td>登录的用户设备有误，登录失败</td>
		</tr>
		<tr >
			<td>801006</td>
			<td>user disabled</td>
			<td>登录的用户被禁用，登录失败</td>
		</tr>
		<tr >
			<td>801007</td>
			<td>multi channel online error</td>
			<td>多通道同时登录错误，登录失败</td>
		</tr>
		<tr >
			<td>802002</td>
			<td>username not match</td>
            <td>登出用户名和登录用户名不匹配，登出失败</td>
		</tr>
		<tr >
			<td>803001</td>
			<td>system error</td>
			<td>发送消息失败，状态存储异常</td>
		</tr>
		<tr >
			<td>803002</td>
			<td>system error</td>
			<td>发送消息失败，系统网络异常</td>
		</tr>
		<tr >
			<td>803003</td>
			<td>target user not exist</td>
			<td>发送消息失败，目标用户未注册或不存在</td>
		</tr>
		<tr >
			<td>803004</td>
			<td>target group not exist</td>
			<td>发送消息失败，目标讨论组不存在</td>
		</tr>
		<tr >
			<td>803005</td>
			<td>user not in group</td>
			<td>发送消息失败，发起者不在目标讨论组中</td>
		</tr>
		<tr >
			<td>803006</td>
			<td>user not permitted</td>
			<td>发送消息失败，发起者权限不够或者类别不匹配</td>
		</tr>
		<tr >
			<td>803007</td>
			<td>length of message exceed limit</td>
			<td>发送消息失败，消息长度超过限制</td>
		</tr>
		<tr >
			<td>803008</td>
			<td>user in blacklist</td>
			<td>发送消息失败，发送者已被接收者拉入黑名单，仅限单聊</td>
		</tr>
		<tr>
			<td>803009</td>
			<td>the message contains sensitive word: the word</td>
			<td>发送消息失败，消息内容包含敏感词汇：具体敏感词</td>
		</tr>
		<tr >
			<td>803010</td>
			<td>beyond the frequency limit</td>
			<td>发送消息失败，发送频率超过系统限制，无法发送，客户端限制每分钟60条</td>
		</tr>
		<tr >
		    <td>803011</td>
			<td>msg content json error</td>
			<td>发送消息失败，消息格式配置错误</td>
		</tr>
		<tr >
		    <td>803012</td>
			<td>can not chat while silent</td>
			<td>发送消息失败，请求用户被管理员禁言</td>
		</tr>
		<tr >
		    <td>805001</td>
			<td>target user not exist</td>
			<td>目标用户不存在</td>
		</tr>
		<tr >
        	<td>805002</td>
	        <td>already is friend</td>
            <td>添加好友失败：双方已经是好友</td>
		</tr>
		<tr >
		    <td>805003</td>
			<td>user not friend</td>
			<td>删除好友失败：目标用户并不是自己的好友</td>
		</tr>
		<tr>
		    <td>805004</td>
			<td>invalid friend memo</td>
			<td>修改好友备注失败：备注内容无效，无法修改</td>
		</tr>
		<tr >
		    <td>805006</td>
			<td>invitation event is not valid</td>
			<td>添加好友失败：邀请事件无效</td>
		</tr>
		<tr >
		    <td>808001</td>
			<td>group name invalid</td>
			<td>创建群组时群名为空，创建群组失败</td>
		</tr>
		<tr >
			<td>808002</td>
			<td>user not permitted to create group</td>
			<td>用户无创建群组权限，创建群组失败</td>
		</tr>
		<tr >
			<td>808003</td>
			<td>amount of group exceed limit</td>
			<td>用户拥有的群组数量已达上限,无法再创建</td>
		</tr>
		<tr >
			<td>808004</td>
			<td>length of group name exceed limit</td>
			<td>群组名长度超出上限，创建群组失败</td>
		</tr>
		<tr >
			<td>808005</td>
			<td>length of group desc exceed limit</td>
			<td>群组描述长度超出上限，创建群组失败</td>
		</tr>
		<tr >
			<td>810002</td>
			<td>add member list is null</td>
			<td>添加的成员列表为空</td>
		</tr>
		<tr >
			<td>810005</td>
			<td>have member not register</td>
			<td>添加的成员列表中包含未注册成员</td>
		</tr>
		<tr >
			<td>810007</td>
			<td>repeated added member</td>
			<td>添加的成员列表中有成员重复添加</td>
		</tr>
		<tr >
			<td>810008</td>
			<td>amount of member exceed group limit</td>
			<td>添加的成员数量超出群组拥有的最大成员数上限</td>
		</tr>
		<tr >
			<td>810009</td>
			<td>amount of group exceed member limit</td>
			<td>添加的成员列表中有成员拥有的群组数量已达上限</td>
		</tr>
		<tr >
			<td>811002</td>
			<td>del member list is null</td>
			<td>删除的成员列表为空</td>
		</tr>
		<tr >
			<td>811005</td>
			<td>have member not register</td>
			<td>删除的成员列表中有成员未注册</td>
		</tr>
		<tr >
			<td>811006</td>
			<td>member of group not permitted deleted</td>
			<td>删除的成员列表中有成员该用户没有权限进行删除</td>
		</tr>
		<tr >
			<td>811007</td>
			<td>repeated deleted member</td>
			<td>删除的成员列表中有成员重复删除</td>
		</tr>
		<tr >
			<td>811008</td>
			<td>have member not in group</td>
			<td>删除的成员列表中有成员不在该群组中</td>
		</tr>
		<tr >
			<td>812003</td>
			<td>length of group name exceed limit</td>
			<td>群组名超出长度上限</td>
		</tr>
		<tr >
			<td>812004</td>
			<td>length of group desc exceed limit</td>
			<td>群组描述超出上限</td>
		</tr>
		<tr >
			<td>818001</td>
			<td>zero member</td>
			<td>用户添加黑名单时，成员列表为空，添加失败</td>
		</tr>
		<tr >
			<td>818002</td>
			<td>member not exist</td>
			<td>用户添加黑名单时，成员列表中有成员不存在，添加失败</td>
		</tr>
		<tr >
			<td>818003</td>
			<td>member not permitted added</td>
			<td>用户添加黑名单时，成员列表中有成员不能被添加，添加失败</td>
		</tr>
		<tr >
			<td>819001</td>
			<td>zero member</td>
			<td>用户移除好友出黑名单时，成员列表为空，操作失败</td>
		</tr>
		<tr >
		  <td>819002</td>
			<td>member not exist</td>
			<td>用户删除黑名单时，成员列表中有成员不存在，删除失败</td>
		</tr>
		<tr >
			<td>831001</td>
			<td>member already set</td>
			<td>用户添加成员消息免打扰时，该成员已处于免打扰状态</td>
		</tr>
		<tr >
			<td>832001</td>
			<td>member never set</td>
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
			<td>group already set</td>
			<td>用户添加群组消息免打扰时，该群组已处于免打扰状态</td>
		</tr>
		<tr >
			<td>834001</td>
			<td>group never set</td>
			<td>用户删除群组消息免打扰时，该群组不处于免打扰状态</td>
		</tr>
		<tr >
			<td>835001</td>
			<td>already set</td>
			<td>用户添加全局消息免打扰时，该用户已处于全局免打扰状态</td>
		</tr>
		<tr >
			<td>836001</td>
			<td>never set</td>
			<td>用户删除全局消息免打扰时，该用户不处于全局免打扰状态</td>
		</tr>
		<tr>
			<td>842001</td>
			<td>group not exist</td>
			<td>用户添加群组消息屏蔽时，该群组不存在</td>
		</tr>
		<tr>
			<td>842002</td>
			<td>user not in group</td>
			<td>用户添加群组消息屏蔽时，用户不在该群组中</td>
		</tr>
		<tr>
			<td>842003</td>
			<td>group already set</td>
			<td>用户添加群组消息屏蔽时，该群组已处于消息屏蔽状态</td>
		</tr>
		<tr>
			<td>843001</td>
			<td>group never set</td>
			<td>用户删除群组消息屏蔽时，该群组不处于消息屏蔽状态</td>
		</tr>
		<tr>
			<td>847001</td>
			<td>user not in chatroom</td>
			<td>发送聊天室消息失败，发起者不在该聊天室中</td>
		</tr>
		<tr>
			<td>847002</td>
			<td>user baned to post</td>
			<td>发送聊天室消息失败，发起者在该聊天室中被禁言</td>
		</tr>
		<tr>
			<td>847003</td>
			<td>chatroom not exist</td>
			<td>发送聊天室消息失败，该聊天室不存在</td>
		</tr>
		<tr>
			<td>847004</td>
			<td>length of chatroom message exceed limit</td>
			<td>发送聊天室消息失败，消息长度超过限制</td>
		</tr>
		<tr>
			<td>847005</td>
			<td>chatroom msg content json error</td>
			<td>发送聊天室消息失败，消息内容格式错误</td>
		</tr>
		<tr>
			<td>850001</td>
			<td>chatroom not exist</td>
			<td>删除不存在的聊天室</td>
		</tr>
		<tr>
			<td>851001</td>
			<td>repeated invit chatroom member</td>
			<td>邀请成员到聊天室时，邀请的成员列表中有重复的成员，邀请失败</td>
		</tr>
		<tr>
			<td>851002</td>
			<td>invit member not exist</td>
			<td>邀请成员到聊天室时，邀请的成员列表中有未注册成员，邀请失败</td>
		</tr>
		<tr>
			<td>851003</td>
			<td>member has in the chatroom</td>
			<td>邀请或加入到聊天室时，邀请或加入的成员已在聊天室中，邀请或加入失败</td>
		</tr>
		<tr>
			<td>851004</td>
			<td>chatroom not exist</td>
			<td>邀请或加入不存在的聊天室</td>
		</tr>
		<tr>
			<td>851005</td>
			<td>zero member</td>
			<td>邀请成员到聊天室时，邀请的成员列表为空，邀请成员失败</td>
		</tr>
		<tr>
			<td>851006</td>
			<td>amount of member exceed chatroom limit</td>
			<td>邀请或加入聊天时，邀请的人员数量超过聊天室剩余加入的人员数量</td>
		</tr>
		<tr>
			<td>852001</td>
			<td>user not in chatroom</td>
			<td>踢出或退出聊天室时，该用户其实并不在该聊天室中，踢出或退出聊天室失败</td>
		</tr>
		<tr>
			<td>852002</td>
			<td>chatroom not exist</td>
			<td>踢出或退出不存在的聊天室</td>
		</tr>
		<tr>
			<td>852003</td>
			<td>zero member</td>
			<td>踢出成员到聊天室时，踢出的成员列表为空，踢出成员失败</td>
		</tr>
		<tr>
			<td>852004</td>
			<td>owner can not leave chatroom</td>
			<td>踢出或退出聊天室时，存在owner用户退出聊天室</td>
		</tr>
    <tr>
			<td>853001</td>
			<td>chatroom not exist</td>
			<td>更新不存在的聊天室信息</td>
		</tr>
		<tr>
			<td>853002</td>
			<td>owner not in chatroom</td>
			<td>更新聊天室owner时，新的owner并不在该聊天室中</td>
    </tr>
		<tr>
			<td>855001</td>
			<td>out of time</td>
			<td>消息撤回失败，超出撤回时间</td>
		</tr>
		<tr>
			<td>855002</td>
			<td>request user is not message sender</td>
			<td>消息撤回失败，请求撤回方不是消息发送方</td>
		</tr>
		<tr>
			<td>855003</td>
			<td>request message not exist</td>
			<td>消息撤回失败，请求撤回消息不存在</td>
		</tr>
		<tr>
			<td>855004</td>
			<td>message already retract</td>
			<td>消息撤回失败，该消息已经撤回</td>
		</tr>
		<tr>
			<td>856001</td>
			<td>this request already process</td>
			<td>审批失效，该添加成员邀请已经被处理</td>
		</tr>
		<tr>
			<td>856002</td>
			<td>invalid request data</td>
			<td>请求数据无效</td>
		</tr>
		<tr>
			<td>857001</td>
			<td>target group not exist</td>
			<td>目标群组不存在</td>
		</tr>
		<tr>
			<td>857002</td>
			<td>target not online</td>
			<td>目标不在线</td>
		</tr>
		<tr>
			<td>857003</td>
			<td>target user not exist</td>
			<td>目标用户不存在</td>
		</tr>
		<tr>
			<td>857004</td>
			<td>length of trans cmd exceed limit</td>
			<td>透传消息长度超过限制</td>
		</tr>
		<tr>
			<td>857005</td>
			<td>user not in group</td>
			<td>请求用户不在群组中</td>
		</tr>
		<tr>
			<td>857006</td>
			<td>target can't be self</td>
			<td>目标不能为自己</td>
		</tr>
		<tr>
			<td>859001</td>
			<td>user already in the group</td>
			<td>用户已经在目标群组中</td>
		</tr>
		<tr>
			<td>859002</td>
			<td>group type not support</td>
			<td>目标群组类型不支持申请入群</td>
		</tr>
		<tr>
			<td>765001</td>
			<td>target not in group</td>
			<td>目标用户不在群组中</td>
		</tr>
		<tr>
			<td>765002</td>
			<td>request user no permission</td>
			<td>请求用户无操作权限</td>
		</tr>
		<tr>
			<td>7100001</td>
			<td>notify target is null or target logout</td>
			<td>音视频信令通知目标用户为空或者目标已全部登出</td>
		</tr>
		<tr>
			<td>7100002</td>
			<td>invite targe logout</td>
			<td>音视频被邀请的用户已登出</td>
		</tr>
		<tr>
			<td>7100006</td>
			<td>not enough rtc trial time</td>
			<td>音视频服务试用时长不够，停用</td>
		</tr>
</table>
</div>

## 相关文档

+ [iOS SDK 错误码](../client/im_errorcode_ios/)
+ [Android SDK 错误码](../client/im_errorcode_android/)





