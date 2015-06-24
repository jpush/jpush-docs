## IM ErrorCode 定义

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th style="padding: 0 5px;text-align:center;" >Code</th>
			<th style="padding: 0 5px;" >Error Message</th>
			<th style="padding: 0 5px;" >说明</th>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">0</td>
			<td style="padding: 0 5px;">success</td>
			<td style="padding: 0 5px;">成功</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898000</td>
			<td style="padding: 0 5px;">Server internal error</td>
			<td style="padding: 0 5px;">内部错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898001</td>
			<td style="padding: 0 5px;">User exists</td>
			<td style="padding: 0 5px;">用户已存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898002</td>
			<td style="padding: 0 5px;">No sush user</td>
			<td style="padding: 0 5px;">用户不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898003</td>
			<td style="padding: 0 5px;">Parameter invalid!</td>
			<td style="padding: 0 5px;">请求参数不合法 </td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898004</td>
			<td style="padding: 0 5px;">Password error</a></td>
			<td style="padding: 0 5px;">密码错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898006</td>
			<td style="padding: 0 5px;">gid invalid</td>
			<td style="padding: 0 5px;">gid不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898006</td>
			<td style="padding: 0 5px;">gid invalid</td>
			<td style="padding: 0 5px;">gid 不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898008</td>
			<td style="padding: 0 5px;">Basic authentication failed.</td>
			<td style="padding: 0 5px;">校验失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">898009</td>
			<td style="padding: 0 5px;">appkey not exists</td>
			<td style="padding: 0 5px;">appkey不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">808030</td>
			<td style="padding: 0 5px;">Server response time out, please try again later</td>
			<td style="padding: 0 5px;">系统繁忙，稍后重试</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800002</td>
			<td style="padding: 0 5px;">appkey info is nil</td>
			<td style="padding: 0 5px;">appkey信息为空</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800003</td>
			<td style="padding: 0 5px;">appkey not register</td>
			<td style="padding: 0 5px;">appkey未注册</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800005</td>
			<td style="padding: 0 5px;">user id not register</td>
			<td style="padding: 0 5px;">用户ID未注册（appkey无该UID）</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800006</td>
			<td style="padding: 0 5px;">user id not exist</a></td>
			<td style="padding: 0 5px;">用户ID不存在（数据库中无该UID）</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800009</td>
			<td style="padding: 0 5px;">system error</td>
			<td style="padding: 0 5px;">服务器系统错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800010</td>
			<td style="padding: 0 5px;">sync couchbase error</td>
			<td style="padding: 0 5px;">服务器系统错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800011</td>
			<td style="padding: 0 5px;">sync mysql error</td>
			<td style="padding: 0 5px;">服务器系统错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800012</td>
			<td style="padding: 0 5px;">user never login</td>
			<td style="padding: 0 5px;">发起的用户从未登录过</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800013</td>
			<td style="padding: 0 5px;">user logout</td>
			<td style="padding: 0 5px;">发起的用户已登出</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">800014</td>
			<td style="padding: 0 5px;">appkey not match</td>
			<td style="padding: 0 5px;">发起的用户appkey与目标不匹配</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">801003</td>
			<td style="padding: 0 5px;">user name not register</td>
			<td style="padding: 0 5px;">用户名不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">801004</td>
			<td style="padding: 0 5px;">user password is wrong</td>
			<td style="padding: 0 5px;">用户密码错误</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803001</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，系统内部异常</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803002</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，系统网络异常</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803003</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，目标用户未注册或从未登录过</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803004</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，目标讨论组不存在</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803005</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，发起者不在目标讨论组中</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">803006</td>
			<td style="padding: 0 5px;"></td>
			<td style="padding: 0 5px;">发送消息失败，发起者权限不够或者类别不匹配</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">808002</td>
			<td style="padding: 0 5px;">user have not right to create group</td>
			<td style="padding: 0 5px;">用户无创建讨论组权限，创建讨论组失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">808003</td>
			<td style="padding: 0 5px;">the amount of group exceed limit</td>
			<td style="padding: 0 5px;">用户拥有的讨论组数量已达上限,无法再创建</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">809002</td>
			<td style="padding: 0 5px;">user not in the group</td>
			<td style="padding: 0 5px;">用户退出讨论组时，用户不在该讨论组中，退出讨论组失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810003</td>
			<td style="padding: 0 5px;">user not in the group</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，用户不在该讨论组中，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810004</td>
			<td style="padding: 0 5px;">user not have right of group to add member</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，用户没有往讨论组中添加成员的权限，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810005</td>
			<td style="padding: 0 5px;">member not register</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，添加的成员列表中有成员未注册，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810006</td>
			<td style="padding: 0 5px;">user have not right to add member in the group</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，添加的成员列表中有成员该用户没有权限进行添加，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810007</td>
			<td style="padding: 0 5px;">member repeated add</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，添加的成员列表中有成员重复添加，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810008</td>
			<td style="padding: 0 5px;">the amount of member exceed group limit</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，添加的成员数量超出讨论组拥有的最大成员数上限，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">810009</td>
			<td style="padding: 0 5px;">the amount of group exceed member limit</td>
			<td style="padding: 0 5px;">用户添加成员到讨论组时，添加的成员列表中有成员拥有的讨论组数量已达上限，添加成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811003</td>
			<td style="padding: 0 5px;">user not in the group</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，用户不在该讨论组中，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811004</td>
			<td style="padding: 0 5px;">user not have right of group to remove member</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，用户没有删除讨论组中成员的权限，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811005</td>
			<td style="padding: 0 5px;">member not register</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，删除的成员列表中有成员未注册，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811006</td>
			<td style="padding: 0 5px;">user have not right to remove member from the group</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，删除的成员列表中有成员该用户没有权限进行删除，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811007</td>
			<td style="padding: 0 5px;">member repeated remove</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，删除的成员列表中有成员重复删除，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">811008</td>
			<td style="padding: 0 5px;">member not in the group</td>
			<td style="padding: 0 5px;">用户删除讨论组成员时，删除的成员列表中有成员不在该讨论组中，删除成员失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">812002</td>
			<td style="padding: 0 5px;">user not in the group</td>
			<td style="padding: 0 5px;">用户修改讨论组信息时，用户不在该讨论组中，修改讨论组信息失败</td>
		</tr>
		
    <!-- Android SDK 相关 -->		
    <tr >
      <td style="padding: 0 5px; " >871101</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >请求参数不合法</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871102</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >请求失败，请检查网络</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871103</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >服务器内部错误</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871104</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >服务器内部错误</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871201</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >响应超时</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871300</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >api调用发起者尚未登录</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871301</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >api调用传入的参数不合法</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871302</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >发送消息的消息体过大，整个消息体大小不能超过4k</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871303</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >用户名不合法</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871304</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >密码不合法</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871305</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >名称不合法（包括nickname groupname notename）  </td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871306</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >其他输入不合法</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871307</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >添加或移除群成员时，传入的成员列表中有用户不存在</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871308</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >SDK尚未初始化</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871309</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >消息中包含的文件不存在</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871402</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >文件上传失败</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871403</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >文件上传失败</td>
    </tr>
    <tr >
      <td style="padding: 0 5px; " >871404</td>
      <td style="padding: 0 5px;"></td>
      <td style="padding: 0 5px; " >文件下载失败</td>
    </tr>

	</table>
</div>
