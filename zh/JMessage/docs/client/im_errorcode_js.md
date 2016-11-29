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
| 880101 | appkey not exist                         | appkey 不存在          |
| 880102 | signatu fail                             | 签名错误                |
| 880103 | user not existr                          | 用户不存在               |
| 880104 | invalid password.                        | 密码错误                |
| 880203 | target user not exist                    | 目标用户不存在             |
| 880204 | target group not exist                   | 目标群组不存在             |
| 880205 | user not in group                        | 用户不在群组              |
| 880206 | length of message exceed limit.          | 消息大小超过限制            |
| 880207 | user in blacklist                        | 用户被对方拉黑             |
| 880208 | message is sensitive                     | 消息包含敏感词汇            |
| 880402 | not permitted to create group            | 没有创建群组的权限           |
| 880403 | amount of group exceed limit             | 群数量到达上限             |
| 880404 | length of group name exceed limit        | 群名字超过长度限制，创建失败      |
| 880405 | length of group desc exceed limit        | 群描述长度超过限制           |
| 880502 | user not in group                        | 用户不在群里面             |
| 880602 | zero member                              | 添加的群成员为空            |
| 880603 | user not in group                        | 用户不在群里面             |
| 880604 | user not permitted add member to group   | 没权限添加群成员            |
| 880606 | member not permitted added to group      | 成员列表中有用户没有被添加到群组的权限 |
| 880608 | amount of member exceed group limit      | 群成员数量超过限制           |
| 880609 | amount of group exceed member limit      | 成员列表中存在成员的群组数量超过限制  |
| 880703 | user not in group                        | 删除的群成员列表存在成员不属于该群组  |
| 880704 | user not permitted delete member of group | 用户没有删除群成员的权限        |
| 880705 | member of group not permitted deleted    | 成员列表中存在成员用户没权限删除    |
| 880803 | length of group name exceed limit        | 群组名长度超过限制           |
| 880804 | length of group desc exceed limit        | 群组描述长度超过限制          |
| 880903 | member not permitted added               | 成员列表中有成员不能被添加，添加失败  |
| 881002 | member not exist                         | 成员列表中有不存在的成员        |
| 881101 | member already set                       | 该成员已处于免打扰状态         |
| 881102 | member never set                         | 该成员不处于免打扰状态         |
| 881103 | group not exist                          | 该群组不存在              |
| 881104 | user not in group                        | 用户不存在该群组中           |
| 881105 | group already set                        | 该群组已处于免打扰状态         |
| 881106 | group never set                          | 该群组不处于免打扰状态         |
| 881107 | already set                              | 已经这只免打扰             |
| 881108 | never set                                | 没有设置免打扰             |
| 882001 | server internal error                    | 系统内部错误              |
| 882002 | user exit，no such user，password error，uid invalid，gid invalid | 视操作而定               |
| 882003 | invalid parameter                        | 参数不合法               |
| 882004 | auth fail                                | 无效授权                |
| 882005 | response time out，try again later        | 系统繁忙，稍后重试           |
