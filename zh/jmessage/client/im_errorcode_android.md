# IM SDK ErrorCode 定义

以下列表里的 ErrorCode 有可能在 SDK 的调用过程中出现。供参考理解其含义。


## JMessage Android

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
    <tr>
        <td>871101</td>
        <td>Invalid request parameters.</td>
        <td>请求参数不合法</td>
    </tr>
    <tr>
        <td>871102</td>
        <td>Request failed.please check your network connection.</td>
        <td>请求失败，请检查网络</td>
    </tr>
    <tr>
        <td>871103</td>
        <td>Server returned an unexpected error code.</td>
        <td>服务器内部错误</td>
    </tr>
    <tr>
        <td>871104</td>
        <td>Server internal error.</td>
        <td>服务器内部错误</td>
    </tr>
    <tr>
        <td>871105</td>
        <td>User info not found.</td>
        <td>请求的用户信息不存在</td>
    </tr>
    <tr>
        <td>871201</td>
        <td>Get response timeout,please try again later.</td>
        <td>响应超时</td>
    </tr>
    <tr>
        <td>871300</td>
        <td>Have not logged in.</td>
        <td>api调用发起者尚未登录</td>
    </tr>
    <tr>
        <td>871301</td>
        <td>Invalid parameters.</td>
        <td>api调用传入的参数不合法</td>
    </tr>
    <tr>
        <td>871302</td>
        <td>Message content exceeds its max length.</td>
        <td>发送消息的消息体过大，整个消息体大小不能超过4k</td>
    </tr>
    <tr>
        <td>871303</td>
        <td>Invalid username.</td>
        <td>用户名不合法</td>
    </tr>
    <tr>
        <td>871304</td>
        <td>Invalid password.</td>
        <td>密码不合法</td>
    </tr>
    <tr>
        <td>871305</td>
        <td>Invalid name.</td>
        <td>名称不合法（包括nickname groupname notename）  </td>
    </tr>
    <tr>
        <td>871306</td>
        <td>Invalid input.</td>
        <td>其他输入不合法</td>
    </tr>
    <tr>
        <td>871307</td>
        <td>Some user not exists,operate failed.</td>
        <td>添加或移除群成员时，传入的成员列表中有用户不存在</td>
    </tr>
    <tr>
        <td>871308</td>
        <td>SDK have not init yet.</td>
        <td>SDK尚未初始化</td>
    </tr>
    <tr>
        <td>871309</td>
        <td>Attached file not found.</td>
        <td>消息中包含的文件不存在</td>
    </tr>
    <tr>
        <td>871310</td>
        <td>Network not available,please check your network connection.</td>
        <td>网络连接已断开，请检查网络</td>
    </tr>
    <tr>
        <td>871311</td>
        <td>User avatar not specified. download avatar failed.</td>
        <td>用户未设定头像，下载头像失败</td>
    </tr>
    <tr>
        <td>871312</td>
        <td>Create image content failed.</td>
        <td>创建ImageContent失败</td>
    </tr>
    <tr>
        <td>871313</td>
        <td>Message parse error,version not match.</td>
        <td>消息解析出错，协议版本号不匹配</td>
    </tr>
    <tr>
        <td>871314</td>
        <td>Message parse error,lack of key parameter.</td>
        <td>消息解析出错，缺少关键参数</td>
    </tr>
    <tr>
        <td>871315</td>
        <td>Message parse error,check logcat for more information</td>
        <td>消息解析出错</td>
    </tr>
    <tr>
        <td>871317</td>
        <td>Target user cannot be yourself.</td>
        <td>操作目标用户不能是自己</td>
    </tr>
    <tr>
        <td>871318</td>
        <td>Illegal message content.</td>
        <td>不合法的消息体，出现这个问题可能是由于上层没有参照集成文档进行混淆配置导致的，关于jmessage的混淆配置见<a href="../jmessage_android_guide/" target="_blank">集成指南</a></td>
    </tr>
    <tr>
        <td>871319</td>
        <td>Create ForwardMessage failed</td>
        <td>创建转发消息失败，具体原因见logcat打印</td>
    </tr>
    <tr>
        <td>871320</td>
        <td>Set message HaveRead status failed.</td>
        <td>将消息标记为已读时出现问题，可能这条消息已经是已读状态，或者这条消息本身不是接受类型的消息</td>
    </tr>
    <tr>
        <td>871321</td>
        <td>Get receipt details failed.</td>
        <td>获取未回执详情失败，只有消息的发送者可以查询消息的未回执详情</td>
    </tr>
    <tr>
        <td>871322</td>
        <td>Get receipt details failed.</td>
        <td>获取未回执详情失败，这条消息尚未成功发送，只有成功发送的消息可以查询未回执详情</td>
    </tr>
    <tr>
        <td>871323</td>
        <td>Chatroom not exist.</td>
        <td>请求的聊天室信息未找到，该聊天室不存在</td>
    </tr>
    <tr>
        <td>871324</td>
        <td>Illegal message content type, when send message.</td>
        <td>发送消息时消息体类型不合法，注意eventNotification和prompt类型的消息体不能发送</td>
    </tr>
    <tr >
        <td>871325</td>
        <td>Illegal message status. only created or send_failed message can be sent.</td>
        <td>发送消息时消息状态不合法，只有消息状态为创建和发送失败的消息可以被发送</td>
    </tr>
    <tr>
        <td>871326</td>
        <td>unsupported operation.</td>
        <td>不支持的操作，例如聊天室撤回消息</td>
    </tr>
    <tr>
        <td>871327</td>
        <td>operation is cancelled</td>
        <td>操作已被取消，上层调用取消接口（消息发送取消，附件下载取消），取消成功后返回此错误码</td>
    </tr>
    <tr>
        <td>871402</td>
        <td>Upload file failed.auth error.</td>
        <td>文件上传失败</td>
    </tr>
    <tr>
        <td>871403</td>
        <td>Upload file failed.</td>
        <td>文件上传失败</td>
    </tr>
    <tr>
        <td>871404</td>
        <td>Download file failed.</td>
        <td>文件下载失败</td>
    </tr>
    <tr>
        <td>871501</td>
        <td>Push register error,appkey and appid not match.</td>
        <td>appkey与包名不匹配或者token无效</td>
    </tr>
    <tr>
        <td>871502</td>
        <td>Push register error,invalid appkey.</td>
        <td>appKey无效。请检查 AndroidManifest.xml 里的 appKey 配置，它必须是从 JPush 控制台创建应用得到的。</td>
    </tr>
    <tr>
        <td>871503</td>
        <td>Push register error,appkey not matches platform</td>
        <td>appKey与平台不匹配。有可能在 JPush 控制台上，未配置此 appKey 支持 Android 平台。</td>
    </tr>
    <tr>
        <td>871504</td>
        <td>Push register not finished.</td>
        <td>Push 注册未完成，请稍后重试。如果持续出现这个问题，可能你的 JPush 配置不正确。</td>
    </tr>
    <tr>
        <td>871505</td>
        <td>Push register error,package not exists.</td>
        <td>Push 注册失败,对应包名在控制台上不存在。</td>
    </tr>
    <tr>
        <td>871506</td>
        <td>Push register error,invalid IMEI.</td>
        <td>Push 注册失败，设备IMEI不合法</td>
    </tr>

</table>
</div>

## JMRTC Android
<div class="table-d" align="center">
<table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
        <th >Code</th>
        <th>Error Message</th>
        <th>说明</th>
    </tr>
    <tr>
       <td>0</td>
       <td>ok</td>
       <td>成功</td>
    </tr>
    <tr>
        <td>872100</td>
        <td>Jmrtc engine init failed. appkey is empty.</td>
        <td>音视频引擎初始化失败，appkey为空</td>
    </tr>
    <tr>
        <td>872101</td>
        <td>Jmrtc engine init failed. due to some error occurs . see logcat for more detail.</td>
        <td>音视频引擎由于一些问题初始化失败，详情请看日志</td>
    </tr>
    <tr>
        <td>872102</td>
        <td>Jmrtc engine init failed. due to network exception.</td>
        <td>音视频引擎初始化失败，由于网络异常造成</td>
    </tr>
    <tr>
        <td>872103</td>
        <td>Jmrtc engine init failed. due to server return error.</td>
        <td>音视频引擎初始化失败，由于服务器端返回内容错误造成</td>
    </tr>
    <tr>
        <td>872104</td>
        <td>Jmrtc engine init failed. due to server internal error.</td>
        <td>音视频引擎初始化失败，由于服务器端内部错误造成</td>
    </tr>
    <tr>
        <td>872105</td>
        <td>Jmrtc engine init failed. due to required permission not granted.</td>
        <td>音视频引擎初始化失败，由于需要的权限没有获取成功造成</td>
    </tr>
    <tr>
        <td>872106</td>
        <td>Jmrtc engine have not init yet.</td>
        <td>音视频引擎还未初始化</td>
    </tr>
    <tr>
        <td>872001</td>
        <td>Can not send %s signaling message . state error. cur state is %s.</td>
        <td>状态机当前状态不能发起此行为</td>
    </tr>
    <tr>
        <td>872002</td>
        <td>State time out. cur state is %s. will return to idle state immediately.</td>
        <td>状态机状态超时，将回到idle状态</td>
    </tr>
    <tr>
        <td>872003</td>
        <td>Invite user failed. user %s is already in chat.</td>
        <td>邀请用户失败，用户已在聊天频道中</td>
    </tr>
    <tr>
        <td>872004</td>
        <td>Received a signaling message but engine not init yet. should init engine first.</td>
        <td>收到信令，但当前引擎处于未初始化状态，先进行初始化操作</td>
    </tr>
</table>
</div>

<br>
若以上列表中没有找到对应的错误码，可查看[服务器端错误码](./im_errorcode_server/)

## 相关文档

+ [iOS SDK 错误码](../client/im_errorcode_ios/)
+ [服务器端错误码](./im_errorcode_server/)