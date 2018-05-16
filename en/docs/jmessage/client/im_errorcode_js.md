# IM Web ErrorCode 定义

以下列表里的 ErrorCode 有可能在 SDK 的调用过程中出现。供参考理解其含义。


## JMessage Web

只会出现在 Web SDK 里的错误码。



| Code   | Err Message                              | DESCRIPTION         |
| ------ | ---------------------------------------- | ------------------- |
| 0      | success                                  | 请求成功                |
| 880001 | missing error                            | 未知错误码               |
| 880002 | invalid parameter                        | 参数不合法               |
| 880003 | invalid value                            | 非法内容格式              |
| 880004 | invalid type                             | 非法内容格式              |
| 880005 | file not exist                           | 文件不存在               |
| 880006 | login out before register                | 注册之前先退出             |
| 880007 | register limit                           | 被限制注册               |
| 880008 | msg_id not valid                         | msg_id 非法           |
| 880101 | appkey not exist                         | appkey 不存在          |
| 880102 | signatu fail                             | 签名错误                |
| 880103 | user not exist                           | 用户不存在               |
| 880104 | invalid password                         | 密码错误                |
| 880106 | signatu is expire                        | 签名过期                |
| 880107 | already login,please login out before login | 已经是登录状态             |
| 880109 | repetitive operation                     | 重复登录操作              |
| 880110 | multi channel online error,please update your sdk version | 多通道错误，更新sdk版本       |
| 880111 | user disabled                            | 用户被禁用               |
| 880203 | target user not exist                    | 目标用户不存在             |
| 880204 | target group not exist                   | 目标群组不存在             |
| 880205 | user not in group                        | 用户不在群组              |
| 880206 | length of message exceed limit           | 消息大小超过限制            |
| 880207 | user in blacklist                        | 用户被对方拉黑             |
| 880208 | message is sensitive                     | 消息包含敏感词汇            |
| 880209 | beyond the frequency limit               | 发送速度超过限制            |
| 880210 | file size exceed the limit               | 文件大小超过限制            |
| 880212 | can not chat while silent                | 禁言中                 |
| 880402 | not permitted to create group            | 没有创建群组的权限           |
| 880403 | amount of group exceed limit             | 群数量到达上限             |
| 880404 | length of group name exceed limit        | 群名字超过长度限制，创建失败      |
| 880405 | length of group desc exceed limit        | 群描述长度超过限制           |
| 880602 | zero member                              | 目标为空                |
| 880604 | user not permitted add member to group   | 没权限添加群成员            |
| 880606 | member not permitted added to group      | 成员列表中有用户没有被添加到群组的权限 |
| 880607 | repeated added                           | 重复添加                |
| 880608 | num exceed  limit                        | 数量超过限制              |
| 880609 | amount of group exceed member limit      | 成员列表中存在成员的群组数量超过限制  |
| 880610 | user already in the group                | 用户已经在群里面            |
| 880611 | group type not support                   | 群类型不支持该操作           |
| 880612 | this request already process             | 已经处理                |
| 880614 | no permission                            | 无权限操作               |
| 880704 | user not permitted delete member of group | 用户没有删除群成员的权限        |
| 880705 | member of group not permitted deleted    | 成员列表中存在成员用户没权限删除    |
| 880903 | member not permitted added               | 成员列表中有成员不能被添加，添加失败  |
| 880904 | repeated added member                    | 重复添加                |
| 881101 | member already set                       | 该成员已处于免打扰状态         |
| 881102 | member never set                         | 该成员不处于免打扰状态         |
| 881105 | group already set                        | 该群组已处于免打扰状态         |
| 881106 | group never set                          | 该群组不处于免打扰状态         |
| 881107 | already set                              | 已经设置免打扰             |
| 881108 | never set                                | 没有设置免打扰             |
| 881203 | group already set                        | 已经设置了屏蔽             |
| 881204 | group never set                          | 群未设置屏蔽              |
| 881302 | already is friend                        | 已经是好友               |
| 881303 | user not friend                          | 非好友关系               |
| 881304 | invalid friend memo                      | 非法备注                |
| 881305 | Invitation event is not valid            | 添加好友失败：邀请事件无效       |
| 881401 | out of time                              | 超出撤回时间              |
| 881402 | request user is not message sender       | 请求撤回方不是消息发送方        |
| 881403 | request message not exist                | 消息不存在               |
| 881404 | message already retract                  | 已经撤回                |
| 881501 | user not in chatroom                     | 用户不在聊天室             |
| 881502 | user baned to post                       | 用户被禁止发消息            |
| 881503 | chatroom not exist                       | 聊天室不存在              |
| 881504 | length of chatroom message exceed limit  | 消息长度超出限制            |
| 881507 | member has in the chatroom               | 用户已经在聊天室            |
| 881508 | amount of member exceed chatroom limit   | 超过聊天室人数限制           |
| 881509 | msg format err                           | 消息格式错误              |
| 881602 | target user not login                    | 目标用户未登录             |
| 881604 | length of trans cmd exceed limit         | 消息长度超出限制            |
| 881701 | user not admin                           | 用户不是群管理员            |
| 882001 | server internal error                    | 系统内部错误              |
| 882002 | user exit，no such user，password error，uid invalid，gid invalid | 视操作而定               |
| 882003 | invalid parameter                        | 参数不合法               |
| 882004 | auth fail                                | 无效授权                |
| 882005 | response time out，try again later        | 系统繁忙，稍后重试           |
