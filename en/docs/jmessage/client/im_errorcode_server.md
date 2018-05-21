# IM SDK ErrorCode Definition

## Server Error

The error code reported by the JMessage server may appear in the SDK of each platform.

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th>Code</th>
			<th>Error Message</th>
			<th>Instructions</th>
		</tr><tr>
			<td>898000</td>
			<td>Server internal error</td>
			<td>Internal error</td>
		</tr><tr>
			<td>898001</td>
			<td>User exist</td>
			<td>User already exists</td>
		</tr><tr>
			<td>898002</td>
			<td>No such user</td>
			<td>User does not exist</td>
		</tr><tr>
			<td>898003</td>
			<td>Parameter invalid!</td>
			<td>The request parameter is illegal</td>
		</tr><tr>
			<td>898004</td>
			<td>Password error</td>
			<td>Password update operation, user password error</td>
		</tr><tr>
			<td>898006</td>
			<td>Group id invalid</td>
			<td>Group id does not exist</td>
		</tr><tr>
			<td>898007</td>
			<td>Missing authen info</td>
			<td>Check information is empty</td>
		</tr><tr>
			<td>898008</td>
			<td>Basic authentication failed.</td>
			<td>Failed to verify</td>
		</tr><tr>
			<td>898009</td>
			<td>Appkey not exists</td>
			<td>Appkey does not exist</td>
		</tr><tr>
			<td>898010</td>
			<td>Token expired</td>
			<td>The API request token expired. The SDK will automatically reacquire the token under normal circumstances.</td>
		</tr><tr>
			<td>898011</td>
			<td>no auth to query other appkey's user or appkey no exist</td>
			<td>The queried appkey does not have cross-application permissions or appkey does not exist</td>
		</tr><tr>
			<td>898030</td>
			<td>Server response time out, please try again later</td>
			<td>The system is busy and try again later</td>
		</tr><tr>
			<td>899000</td>
			<td>Server internal error</td>
			<td>Internal system error</td>
		</tr><tr>
			<td>899001</td>
			<td>User exist</td>
			<td>User already exists</td>
		</tr><tr>
			<td>899002</td>
			<td>No such user</td>
			<td>User does not exist</td>
		</tr><tr>
			<td>899003</td>
			<td>parameter invalid</td>
			<td>Parameter error. Request Body parameter does not meet the requirements; resend value does not meet the requirements; user name or password is not legal; Group id is illegal</td>
		</tr><tr>
			<td>899006</td>
			<td>Group id invalid</td>
			<td>Group id does not exist</td>
		</tr><tr>
			<td>899007</td>
			<td>Missing authen info</td>
			<td>Check information is empty</td>
		</tr><tr>
			<td>899008</td>
			<td>Basic authentication failed</td>
			<td>Failed to verify</td>
		</tr><tr>
			<td>899009</td>
			<td>Appkey not exit</td>
			<td>Appkey does not exist</td>
		</tr><tr>
			<td>899011</td>
			<td>Repeat to add the members</td>
			<td>Repeatly adding members</td>
		</tr><tr>
			<td>899012</td>
			<td>No enough space for members</td>
			<td>No enough place to add members of this request</td>
		</tr><tr>
			<td>899013</td>
			<td>User list is bigger than 500</td>
			<td>Registration list is greater than 500, and maximum length of batch registration is 500</td>
		</tr><tr>
			<td>899014</td>
			<td>User list is bigger than 500</td>
			<td>Add operation succeeds. In the remove operation, there is username not exist in the discussion group, the removal fails.</td>
		</tr><tr>
			<td>899015</td>
			<td>User 's group are full can not continue</td>
			<td>Groups the user joins reach the upper limit.</td>
		</tr><tr>
			<td>899016</td>
			<td>No authority to send message</td>
			<td>User does not have administrator rights to send information.</td>
		</tr><tr>
			<td>899017</td>
			<td>There are usernames exist in blacklist</td>
			<td>The user has been added to the blacklist.</td>
		</tr><tr>
			<td>899018</td>
			<td>Admin can not be added into blacklist</td>
			<td>Administrators cannot be added to the blacklist.</td>
		</tr><tr>
			<td>899019</td>
			<td>Here are usernames not exist in blacklist</td>
			<td>Deleted target blacklist user does not exist in the blacklist.</td>
		</tr><tr>
			<td>899020</td>
			<td>no auth to operating other appkey</td>
			<td>Cross application fails.</td>
		</tr><tr>
			<td>899021</td>
			<td>should use cross app api</td>
			<td>Query fails. Should use cross-application APIs</td>
		</tr><tr>
			<td>899043</td>
			<td>duplicate add user</td>
			<td>This user has been set to messages Do-Not-Disturb. Error of repeated settings.</td>
		</tr><tr>
			<td>899044</td>
			<td>user is not exist in setting</td>
			<td>The user does not exist in the current setting when canceling the Do-Not-Disturb user.</td>
		</tr><tr>
			<td>899045</td>
			<td>group is not exist</td>
			<td>The group does not exist in the system when setting group message Do-Not-Disturb.</td>
		</tr><tr>
			<td>899046</td>
			<td>user is not in group</td>
			<td>The user is not in the group when the group message is set to Do-Not-Disturb.</td>
		</tr><tr>
			<td>899047</td>
			<td>duplicate add group</td>
			<td>This group has been set to message Do-Not-Disturb. Error of repeated settings.</td>
		</tr><tr>
			<td>899048</td>
			<td>already open global</td>
			<td>Has been set to global Do-Not-Disturb. Error of repeated settings.</td>
		</tr><tr>
			<td>899049</td>
			<td>group is not exist in setting</td>
			<td>The group does not exist in the current settings when canceling the Do-Not-Disturb groups.</td>
		</tr><tr>
			<td>899050</td>
			<td>already close global</td>
			<td>Has been set to global Do-Not-Disturb. Error of repeated settings.</td>
		</tr><tr>
			<td>899070</td>
			<td></td>
			<td>The added friend already exists in the buddy list.</td>
		</tr><tr>
			<td>899071</td>
			<td></td>
			<td>The updated friend does not exist in the buddy list.</td>
		</tr><tr>
			<td>899030</td>
			<td>Server response time out, please try again later</td>
			<td>The system is busy and try again later</td>
		</tr><tr>
			<td>899081</td>
			<td>room id no exist</td>
			<td>Chat room ID does not exist</td>
		</tr><tr>
			<td>899082</td>
			<td>user not in room</td>
			<td>The user is not in the chat room</td>
		</tr><tr>
			<td>800003</td>
			<td>appkey not exist</td>
			<td>Appkey is not registered</td>
		</tr><tr>
			<td>800005</td>
			<td>user not exist</td>
			<td>User ID is not registered (appkey does not have this UID)</td>
		</tr><tr>
			<td>800006</td>
			<td>user not exist</td>
			<td>User ID does not exist (the UID is not in the database)</td>
		</tr><tr>
			<td>800008</td>
			<td>invalid request</td>
			<td>Request type can not be recognized.</td>
		</tr><tr>
			<td>800009</td>
			<td>system error</td>
			<td>Server system error</td>
		</tr><tr>
			<td>800012</td>
			<td>user never login</td>
			<td>The initiated user is in the logout status and never logged in after registering the account. You need to log in first.</td>
		</tr><tr>
			<td>800013</td>
			<td>user logout</td>
			<td>The initiated user is in the logout state and the requested user has logged out. You need to log in first.</td>
		</tr><tr>
			<td>800014</td>
			<td>appkey not match</td>
			<td>Initiated user appkey does not match the target.</td>
		</tr><tr>
			<td>800016</td>
			<td>device not match</td>
			<td>The user equipment initiated does not match, which is caued by the mismatch of the current requesting device and the device last logged in. Need to log in first.</td>
		</tr><tr>
			<td>800017</td>
			<td>beyond the frequency limit</td>
			<td>Frequency of sending request exceeds system limit.</td>
		</tr><tr>
			<td>800018</td>
			<td>group id not exist</td>
			<td>Group ID does not exist</td>
		</tr><tr>
			<td>800019</td>
			<td>req user not in group</td>
			<td>The requesting user is not in the group</td>
		</tr><tr>
			<td>800020</td>
			<td>request user no permission</td>
			<td>Request user has no operation permission</td>
		</tr><tr>
			<td>801003</td>
			<td>user not exist</td>
			<td>Login user name is not registered, and the login fails.</td>
		</tr><tr>
			<td>801004</td>
			<td>invalid password</td>
			<td>Login user password is incorrect, and login fails.</td>
		</tr><tr>
			<td>801005</td>
			<td>invalid device</td>
			<td>Login user device is incorrect and the login fails.</td>
		</tr><tr>
			<td>801006</td>
			<td>user disabled</td>
			<td>Logged user is disabled, and login fails</td>
		</tr><tr>
			<td>801007</td>
			<td>multi channel online error</td>
			<td>Multi-channel simultaneous login error, and login fails.</td>
		</tr><tr>
			<td>802002</td>
			<td>username not match</td>
			<td>Logout user name is not matched login user name, and logout fails.</td>
		</tr><tr>
			<td>803001</td>
			<td>system error</td>
			<td>Failed to send message, since storage status is abnormal.</td>
		</tr><tr>
			<td>803002</td>
			<td>system error</td>
			<td>Failed to send message, since system network is abnormal</td>
		</tr><tr>
			<td>803003</td>
			<td>target user not exist</td>
			<td>Failed to send message, since target user is not registered or does not exist</td>
		</tr><tr>
			<td>803004</td>
			<td>target group not exist</td>
			<td>Failed to send message, since target discussion group does not exist</td>
		</tr><tr>
			<td>803005</td>
			<td>user not in group</td>
			<td>Failed to send message, since the initiator is not in target group.</td>
		</tr><tr>
			<td>803006</td>
			<td>user not permitted</td>
			<td>Failed to send message, due to insufficient privilege of initiator, or mismatched category.</td>
		</tr><tr>
			<td>803007</td>
			<td>length of message exceed limit</td>
			<td>Failed to send message, since the length of the message exceeds the limit.</td>
		</tr><tr>
			<td>803008</td>
			<td>user in blacklist</td>
			<td>Failed to send message, since the sender has been blacklisted by the receiver, which is only for single chat</td>
		</tr><tr>
			<td>803009</td>
			<td>the message contains sensitive word: the word</td>
			<td>Failed to send the message. The message contains sensitive vocabulary: specific sensitive words</td>
		</tr><tr>
			<td>803010</td>
			<td>beyond the frequency limit</td>
			<td>Failed to send the message. The sending frequency exceeds the system limit and cannot sent. The client limits 60 messages per minute.</td>
		</tr><tr>
			<td>803011</td>
			<td>msg content json error</td>
			<td>Failed to send message, due to misconfigured message format.</td>
		</tr><tr>
			<td>803012</td>
			<td>can not chat while silent</td>
			<td>Failed to send the message, since the requesting user is banned by the administrator.</td>
		</tr><tr>
			<td>805001</td>
			<td>target user not exist</td>
			<td>Target user does not exist.</td>
		</tr><tr>
			<td>805002</td>
			<td>already is friend</td>
			<td>Failed to add friends. Already friends</td>
		</tr><tr>
			<td>805003</td>
			<td>user not friend</td>
			<td>Failed to delete friend. The target user is not your friend.</td>
		</tr><tr>
			<td>805004</td>
			<td>invalid friend memo</td>
			<td>Failed to modify the friend's comment. The comment is invalid and cannot be modified</td>
		</tr><tr>
			<td>805006</td>
			<td>invitation event is not valid</td>
			<td>Failed to add friend. Invitation event is invalid.</td>
		</tr><tr>
			<td>808001</td>
			<td>group name invalid</td>
			<td>Group name was empty when creating a group, and group creation fails.</td>
		</tr><tr>
			<td>808002</td>
			<td>user not permitted to create group</td>
			<td>The user did not have the permission to create a group, and the creation fails.</td>
		</tr><tr>
			<td>808003</td>
			<td>amount of group exceed limit</td>
			<td>Groups the user has reach the maximum number and can no longer be created.</td>
		</tr><tr>
			<td>808004</td>
			<td>length of group name exceed limit</td>
			<td>Length of group name exceeds the limit and the group creation fails.</td>
		</tr><tr>
			<td>808005</td>
			<td>length of group desc exceed limit</td>
			<td>The length of the group description exceeds the limit and the group creation fails</td>
		</tr><tr>
			<td>810002</td>
			<td>add member list is null</td>
			<td>The added member list is empty</td>
		</tr><tr>
			<td>810005</td>
			<td>have member not register</td>
			<td>Added member list contains unregistered members</td>
		</tr><tr>
			<td>810007</td>
			<td>repeated added member</td>
			<td>Added members list has duplicated members.</td>
		</tr><tr>
			<td>810008</td>
			<td>amount of member exceed group limit</td>
			<td>The number of added members exceeds the maximum number of the group</td>
		</tr><tr>
			<td>810009</td>
			<td>amount of group exceed member limit</td>
			<td>The number of groups owned by a member in the added member list has reached the upper limit</td>
		</tr><tr>
			<td>811002</td>
			<td>del member list is null</td>
			<td>The deleted member list is empty.</td>
		</tr><tr>
			<td>811005</td>
			<td>have member not register</td>
			<td>There is the member in the deleted member list is not registered.</td>
		</tr><tr>
			<td>811006</td>
			<td>member of group not permitted deleted</td>
			<td>The user does not have permission to delete some member in the deleted member list.</td>
		</tr><tr>
			<td>811007</td>
			<td>repeated deleted member</td>
			<td>Members in the deleted member list is deleted again.</td>
		</tr><tr>
			<td>811008</td>
			<td>have member not in group</td>
			<td>Members in the deleted members list are not in this group.</td>
		</tr><tr>
			<td>812003</td>
			<td>length of group name exceed limit</td>
			<td>Group name exceeds the maximum length.</td>
		</tr><tr>
			<td>812004</td>
			<td>length of group desc exceed limit</td>
			<td>Group description exceeds the limit.</td>
		</tr><tr>
			<td>818001</td>
			<td>zero member</td>
			<td>When the user adds a blacklist, the member list is empty and the addition fails</td>
		</tr><tr>
			<td>818002</td>
			<td>member not exist</td>
			<td>When the user adds a blacklist, the member in the member list does not exist and the addition fails.</td>
		</tr><tr>
			<td>818003</td>
			<td>member not permitted added</td>
			<td>When the user adds a blacklist, members in the member list cannot be added and the addition fails.</td>
		</tr><tr>
			<td>819001</td>
			<td>zero member</td>
			<td>When the user removes friends from the blacklist, the member list is empty and the operation fails</td>
		</tr><tr>
			<td>819002</td>
			<td>member not exist</td>
			<td>When the user deletes the blacklist, the member in the member list does not exist and the deletion fails.</td>
		</tr><tr>
			<td>831001</td>
			<td>member already set</td>
			<td>The member is already in the Do-Not-Disturb state when the user adds the member message Do-Not-Disturb.</td>
		</tr><tr>
			<td>832001</td>
			<td>member never set</td>
			<td>The user is not in the Do-Not-Disturb state when he deletes the member message Do-Not-Disturb.</td>
		</tr><tr>
			<td>833001</td>
			<td>group not exist</td>
			<td>The group does not exist when the user adds the group message Do-Not-Disturb.</td>
		</tr><tr>
			<td>833002</td>
			<td>user not in group</td>
			<td>The user does not exist in the group when he adds the group message Do-Not-Disturb.</td>
		</tr><tr>
			<td>833003</td>
			<td>group already set</td>
			<td>The group is already in the Do-Not-Disturb state when the user adds the group message Do-Not-Disturb.</td>
		</tr><tr>
			<td>834001</td>
			<td>group never set</td>
			<td>The group is not in the Do-Not-Disturb state when the user deletes the group message Do-Not-Disturb.</td>
		</tr><tr>
			<td>835001</td>
			<td>already set</td>
			<td>The user is in the global Do-Not-Disturb state when he adds the global Do-Not-Disturb.</td>
		</tr><tr>
			<td>836001</td>
			<td>never set</td>
			<td>The user is not in the global Do-Not-Disturb state when he deletes the global Do-Not-Disturb.</td>
		</tr><tr>
			<td>842001</td>
			<td>group not exist</td>
			<td>The group does not exist when the user adds a group message blocking.</td>
		</tr><tr>
			<td>842002</td>
			<td>user not in group</td>
			<td>The user is not in this group when he adds a group message blocking.</td>
		</tr><tr>
			<td>842003</td>
			<td>group already set</td>
			<td>The group is already in a message blocking state when the user adds a group message blocking</td>
		</tr><tr>
			<td>843001</td>
			<td>group never set</td>
			<td>The group is not in message blocking state when the user deletes the group message blocking</td>
		</tr><tr>
			<td>847001</td>
			<td>user not in chatroom</td>
			<td>Failed to send chat room message, since the sender is not in the chat room.</td>
		</tr><tr>
			<td>847002</td>
			<td>user baned to post</td>
			<td>Failed to send the chat room message, since the sender is banned in the chat room.</td>
		</tr><tr>
			<td>847003</td>
			<td>chatroom not exist</td>
			<td>Failed to send chat room message, since the chat room does not exist.</td>
		</tr><tr>
			<td>847004</td>
			<td>length of chatroom message exceed limit</td>
			<td>Failed to send chat room message, since message length exceeds limit</td>
		</tr><tr>
			<td>847005</td>
			<td>chatroom msg content json error</td>
			<td>Failed to send chat room message with incorrect message content format</td>
		</tr><tr>
			<td>850001</td>
			<td>chatroom not exist</td>
			<td>Delete non-existent chat rooms</td>
		</tr><tr>
			<td>851001</td>
			<td>repeated invit chatroom member</td>
			<td>When inviting members to a chat room, there are duplicate members in the list of invited members and the invitation fails.</td>
		</tr><tr>
			<td>851002</td>
			<td>invit member not exist</td>
			<td>When inviting members to the chat room, the invited member list has unregistered members and the invitation fails</td>
		</tr><tr>
			<td>851003</td>
			<td>member has in the chatroom</td>
			<td>When inviting or joining a chat room, the invited or joined member is already in the chat room, and the invitation or join fails.</td>
		</tr><tr>
			<td>851004</td>
			<td>chatroom not exist</td>
			<td>Invite or join a non-existent chat room</td>
		</tr><tr>
			<td>851005</td>
			<td>zero member</td>
			<td>When inviting members to the chat room, the list of invited members is empty, and the invitation fails.</td>
		</tr><tr>
			<td>851006</td>
			<td>amount of member exceed chatroom limit</td>
			<td>The number of invited people exceeds the number of people remaining in the chat room when inviting or joining a chat</td>
		</tr><tr>
			<td>852001</td>
			<td>user not in chatroom</td>
			<td>When kicking out or exiting the chat room, the user is not actually in the chat room and kicking or exiting the chat room fails.</td>
		</tr><tr>
			<td>852002</td>
			<td>chatroom not exist</td>
			<td>Kick out or exit a non-existent chat room</td>
		</tr><tr>
			<td>852003</td>
			<td>zero member</td>
			<td>When kicking out the member, the kicking out member list is empty and kicking out the member fails.</td>
		</tr><tr>
			<td>852004</td>
			<td>owner can not leave chatroom</td>
			<td>There is an owner user exiting the chat room when kicking or leaving the chat room</td>
		</tr><tr>
			<td>853001</td>
			<td>chatroom not exist</td>
			<td>Update non-existent chat room information</td>
		</tr><tr>
			<td>853002</td>
			<td>owner not in chatroom</td>
			<td>The new owner is not in the chat room when updating the owner of chat room.</td>
		</tr><tr>
			<td>855001</td>
			<td>out of time</td>
			<td>Failed to withdraw the message. Exceeds the withdrawal time.</td>
		</tr><tr>
			<td>855002</td>
			<td>request user is not message sender</td>
			<td>Failed to withdraw the message. The requesting party is not the sender of the message.</td>
		</tr><tr>
			<td>855003</td>
			<td>request message not exist</td>
			<td>Failed to withdraw the message. The message requested to withdraw does not exist.</td>
		</tr><tr>
			<td>855004</td>
			<td>message already retract</td>
			<td>Failed to withdraw the message. The message has been withdrawn</td>
		</tr><tr>
			<td>856001</td>
			<td>this request already process</td>
			<td>Approval expired. The invitation for adding members has been processed</td>
		</tr><tr>
			<td>856002</td>
			<td>invalid request data</td>
			<td>Request data is invalid.</td>
		</tr><tr>
			<td>857001</td>
			<td>target group not exist</td>
			<td>Target group does not exist</td>
		</tr><tr>
			<td>857002</td>
			<td>target not online</td>
			<td>The goal is not online.</td>
		</tr><tr>
			<td>857003</td>
			<td>target user not exist</td>
			<td>Target user does not exist.</td>
		</tr><tr>
			<td>857004</td>
			<td>length of trans cmd exceed limit</td>
			<td>Length of transmitted message exceeds the limit.</td>
		</tr><tr>
			<td>857005</td>
			<td>user not in group</td>
			<td>The request user is not in the group.</td>
		</tr><tr>
			<td>857006</td>
			<td>target can't be self</td>
			<td>The goal cannot be yourself.</td>
		</tr><tr>
			<td>859001</td>
			<td>user already in the group</td>
			<td>The user is already in the target group.</td>
		</tr><tr>
			<td>859002</td>
			<td>group type not support</td>
			<td>Target group type does not support the application.</td>
		</tr><tr>
			<td>765001</td>
			<td>target not in group</td>
			<td>Target user is not in the group.</td>
		</tr><tr>
			<td>765002</td>
			<td>request user no permission</td>
			<td>Request user has no operation permission.</td>
		</tr>
	</table>
</div>

## Related Documents

+ [iOS SDK Error Code](../client/im_errorcode_ios/)
+ [Android SDK Error Code](../client/im_errorcode_android/)