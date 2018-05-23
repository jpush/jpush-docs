# Definition of IM Web ErrorCode

The ErrorCode in the following list may appear during the SDK's call. Below is for your reference.


## JMessage Web

Error codes only appear in the Web SDK.

| Code| 	Error Message	| DESCRIPTION| 
| ------ | ---------------------------------------- | ------------------- |
| 0	| success	| Successful | request| 
| 880001| 	missing error	| Unknown error code| 
| 880002| 	invalid parameter| 	The parameter is illegal| 
| 880003| 	invalid value| 	Illegal content format| 
| 880004| 	invalid type| 	Illegal content format| 
| 880005| 	file not exist| 	File does not exist| 
| 880006| 	login out before register| 	Sign out before registering| 
| 880007| 	register limit	| Limited registration| 
| 880008| 	msg_id not valid| 	Msg_id is illegal| 
| 880101| 	appkey not exist| 	Appkey does not exist| 
| 880102| 	signatu fail	| Signature error| 
| 880103| 	user not exist	| User does not exist| 
| 880104| 	invalid password| 	Wrong password| 
| 880106| 	signatu is expire	| Signature expired| 
| 880107| 	already login,please login out before login	| Already logged in| 
| 880109| 	repetitive operation	| Repeated login operation| 
| 880110| 	multi channel online error,please update your sdk version	| Multichannel error, please update sdk version| 
| 880111| 	user disabled	| User is disabled| 
| 880203| 	target user not exist| 	Target user does not exist| 
| 880204| 	target group not exist| 	Target group does not exist| 
| 880205| 	user not in group	| User not in group| 
| 880206| 	length of message exceed limit| 	Message size exceeds the limit| 
| 880207| 	user in blacklist	| User in blacklist| 
| 880208| 	message is sensitive| 	Message contains sensitive words| 
| 880209| 	beyond the frequency limit	| Sending speed exceeds the limit| 
| 880210| 	file size exceed the limit	| File size exceeds the limit| 
| 880212| 	can not chat while silent	| Banned| 
| 880402| 	not permitted to create group| 	No permission to create a group| 
| 880403| 	amount of group exceed limit	| The number of groups reaches the upper limit| 
| 880404| 	length of group name exceed limit| 	Length of group name exceeds the limit, and the creation fails.| 
| 880405| 	length of group desc exceed limit	| Length of group description exceeds the limit| 
| 880602| 	zero member	| Target is empty| 
| 880604| 	user not permitted add member to group| 	No permission to add group members| 
| 880606| 	member not permitted added to group	| There is the user in the member list that has not been added to the group | 
| 880607| 	repeated added	| Repeatedly added| 
| 880608| 	num exceed limit| 	Quantity exceeds the limit| 
| 880609| 	amount of group exceed member limit	| There is the user in the member list whose number of group exceeds the limit| 
| 880610| 	user already in the group| 	The user is already in the group| 
| 880611| 	group type not support	| Group type does not support this operation| 
| 880612| 	this request already process| 	Already processed| 
| 880614| 	no permission	| No permission to operate| 
| 880704| 	user not permitted delete member of group	| The user did not have the permission to delete group members| 
| 880705| 	member of group not permitted deleted	| There is the user in the member list who does not have permission to delete| 
| 880903| 	member not permitted added	| There is the user in the member list who cannot be added and the addition fails.| 
| 880904| 	repeated added member| 	Repeatedly added| 
| 881101| 	member already set| 	The member is already in the DND status| 
| 881102| 	member never set	| The member is not in the DND status| 
| 881105| 	group already set	| The group is already in the DND status | 
| 881106| 	group never set	| The group is not in the DND status| 
| 881107| 	already set	| Has set Do-Not-Disturb| 
| 881108| 	never set	| Not set Do-Not-Disturb| 
| 881203| 	group already set| 	Already set up blocking| 
| 881204| 	group never set	| Not set up group blocking yet| 
| 881302| 	already is friend	| Already a friend| 
| 881303| 	user not friend	| Non-friendship| 
| 881304| 	invalid friend memo| 	Illegal note| 
| 881305| 	Invitation event is not valid| 	Failed to add friends: Invalid invitation event| 
| 881401| 	out of time	| Exceed the withdrawal time| 
| 881402| 	request user is not message sender| 	The requesting withdraw party is not the sender of the message| 
| 881403| 	request message not exist| 	Message does not exist| 
| 881404| 	message already retract| 	Has been withdrawn already| 
| 881501| 	user not in chatroom	| The user is not in the chat room| 
| 881502| 	user baned to post| 	The user is forbidden to send messages| 
| 881503| 	chatroom not exist| 	Chat room does not exist| 
| 881504| 	length of chatroom message exceed limit| 	Message length exceeds the limit| 
| 881507| 	member has in the chatroom	| The user is already in the chat room| 
| 881508| 	amount of member exceed chatroom limit| 	Exceed the number of chat rooms| 
| 881509| 	msg format err	| Wrong message format| 
| 881602| 	target user not login| 	The target user is not logged in| 
| 881604| 	length of trans cmd exceed limit| 	Message length exceeds the limit| 
| 881701| 	user not admin	| The user is not a group administrator| 
| 882001| 	server internal error| 	Internal system error| 
| 882002| 	user exit，no such user，password error，uid invalid，gid invalid	| Depend on the operation| 
| 882003| 	invalid parameter	| The parameter is illegal| 
| 882004| 	auth fail	| Invalid authorization| 
| 882005| 	response time out，try again later| 	The system is busy and try again later| 

