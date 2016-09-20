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
      <td>863006</td>
      <td>User repeat Login fault</td>
      <td>重复登录的错误</td>
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

