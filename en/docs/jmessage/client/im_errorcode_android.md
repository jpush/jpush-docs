# Definition of IM SDK ErrorCode 

ErrorCodes in the following list may appear during the SDK call. The list below is for reference.


## JMessage Android

Error codes only appear in the Android SDK

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th>Error Message</th>
			<th>Instruction</th>
		</tr>
	<tr >
	  <td>0</td>
	  <td>Success</td>
	  <td>success</td>
	</tr>
    <tr >
      <td>871101</td>
      <td>Invalid request parameters.</td>
      <td>The request parameter is illegal</td>
    </tr>
    <tr >
      <td>871102</td>
      <td>Request failed.please check your network connection.</td>
      <td>Request failed. Please check the network</td>
    </tr>
    <tr >
      <td>871103</td>
      <td>Server returned an unexpected error code.</td>
      <td>Server internal error</td>
    </tr>
    <tr >
      <td>871104</td>
      <td>Server internal error.</td>
      <td>Server internal error</td>
    </tr>
    <tr >
      <td>871105</td>
      <td>User info not found.</td>
      <td>Requested user information does not exist</td>
    </tr>
    <tr >
      <td>871201</td>
      <td>Get response timeout,please try again later.</td>
      <td>Response timeout</td>
    </tr>
    <tr >
      <td>871300</td>
      <td>Have not logged in.</td>
      <td>Initiator of api call has not logged in</td>
    </tr>
    <tr >
      <td>871301</td>
      <td>Invalid parameters.</td>
      <td>Parameters passed by api call is illegal</td>
    </tr>
    <tr >
      <td>871302</td>
      <td>Message content exceeds its max length.</td>
      <td>The body of the sent message is too large. The size of the entire message body cannot exceed 4k.</td>
    </tr>
    <tr >
      <td>871303</td>
      <td>Invalid username.</td>
      <td>Username is illegal.</td>
    </tr>
    <tr >
      <td>871304</td>
      <td>Invalid password.</td>
      <td>Password is illegal</td>
    </tr>
    <tr >
      <td>871305</td>
      <td>Invalid name.</td>
      <td>Name is illegal (including nickname groupname notename)</td>
    </tr>
    <tr >
      <td>871306</td>
      <td>Invalid input.</td>
      <td>Other input is illegal</td>
    </tr>
    <tr >
      <td>871307</td>
      <td>Some user not exists,operate failed.</td>
      <td>When adding or removing a group member, the user in the incoming member list does not exist</td>
    </tr>
    <tr >
      <td>871308</td>
      <td>SDK have not init yet.</td>
      <td>SDK has not been initialized</td>
    </tr>
    <tr >
      <td>871309</td>
      <td>Attached file not found.</td>
      <td>The file contained in the message does not exist</td>
    </tr>
    <tr >
      <td>871310</td>
      <td>Network not available,please check your network connection.</td>
      <td>The network connection has been disconnected. Please check the network</td>
    </tr>
    <tr >
      <td>871311</td>
      <td>User avatar not specified. download avatar failed.</td>
      <td>The user did not set the avatar and the downloading of avatar failed</td>
    </tr>
    <tr >
      <td>871312</td>
      <td>Create image content failed.</td>
      <td>Create ImageContent fails</td>
    </tr>
    <tr >
      <td>871313</td>
      <td>Message parse error,version not match.</td>
      <td>Message parsing goes wrong, and protocol version number does not match</td>
    </tr>
    <tr >
      <td>871314</td>
      <td>Message parse error,lack of key parameter.</td>
      <td>Message parsing goes wrong, and key parameters is missed</td>
    </tr>
    <tr >
      <td>871315</td>
      <td>Message parse error,check logcat for more information</td>
      <td>Message parsing goes wrong</td>
    </tr>
    <tr >
      <td>871317</td>
      <td>Target user cannot be yourself.</td>
      <td>Target user of the operation cannot be yourself</td>
    </tr>
    <tr >
      <td>871318</td>
      <td>Illegal message content.</td>
      <td>Illegal message body. This problem may be caused by the upper layer not obfuscate the configuration according to integration document. About confusion configuration of jmessage, please see <a href="../jmessage_android_guide/" target="_blank">Integration Guide</a>.</td>
    </tr>
    <tr >
      <td>871319</td>
      <td>Create ForwardMessage failed</td>
      <td>Failed to create forwarding message. See logcat for details</td>
    </tr>
    <tr >
      <td>871320</td>
      <td>Set message HaveRead status failed.</td>
      <td>There was a problem when flagging a message as read. It may be that the message is already read, or the message itself is not an accepted message</td>
    </tr>
    <tr >
      <td>871321</td>
      <td>Get receipt details failed.</td>
      <td>Failed to get unreceipted details. Only the sender of the message can query the unreceipted details of the message</td>
    </tr>
    <tr >
      <td>871322</td>
      <td>Get receipt details failed.</td>
      <td>Failed to get unreceipted details means that this message has not been sent successfully. Only the message has sent successfully can query the unreceipted details.</td>
    </tr>
	<tr >
	  <td>871323</td>
	  <td>Chatroom not exist.</td>
	  <td>The requested chat room information was not found. The chat room does not exist</td>
	</tr>
	<tr >
	  <td>871324</td>
	  <td>Illegal message content type, when send message.</td>
	  <td>The message body type is illegal when sending a message. Note that the message body of eventNotification and prompt cannot be sent
    </td>
	</tr>
    <tr >
      <td>871402</td>
      <td>Upload file failed.auth error.</td>
      <td>Uploading file fails</td>
    </tr>
    <tr >
      <td>871403</td>
      <td>Upload file failed.</td>
      <td>Uploading file fails</td>
    </tr>
    <tr >
      <td>871404</td>
      <td>Download file failed.</td>
      <td>Downloading file failed.</td>
    </tr>
    <tr >
      <td>871501</td>
      <td>Push register error,appkey and appid not match.</td>
      <td>Appkey does not match package name or token is invalid</td>
    </tr>
    <tr >
      <td>871502</td>
      <td>Push register error,invalid appkey.</td>
      <td>appKey is invalid. Please check the appKey configuration in AndroidManifest.xml, which must be created from the JPush console.</td>
    </tr>
    <tr >
      <td>871503</td>
      <td>Push register error,appkey not matches platform</td>
      <td>appKey does not match the platform. It is possible that on the JPush console, this appKey is not configured to support the Android platform.</td>
    </tr>
    <tr>
      <td>871504</td>
      <td>Push register not finished.</td>
      <td>Push registration is not completed. Please try again later. If this problem persists, your JPush configuration may be incorrect.</td>
    </tr>
    <tr>
      <td>871505</td>
      <td>Push register error,package not exists.</td>
      <td>Push registration fails, and the corresponding package name does not exist on the console.</td>
    </tr>
    <tr>
      <td>871506</td>
      <td>Push register error,invalid IMEI.</td>
      <td>Push registration fails and device IMEI is invalid</td>
    </tr>

</table>
</div>
<br>

If the corresponding error code is not found in the above list, you can view [the Server Error Code](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)

## Related Documents

+ [iOS SDK Error Code](../client/im_errorcode_ios/)
+ [Server Error Code](https://docs.jiguang.cn/jmessage/client/im_errorcode_server/)

