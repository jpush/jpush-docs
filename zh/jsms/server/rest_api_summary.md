
# 服务端 REST API 概述

JSMS 提供遵从 REST 规范的 HTTP API，以供开发者远程调用 JSMS 提供的服务。

与此同时，为方便开发者使用 JSMS API，还提供[多种常用编程语言的开发包（SDK）](../resources/#sdk_1)。

</br>
## REST API 基本约束

* API 被设计为符合 HTTP, REST 规范。例如：查询请求使用 Get 方法，提交请求使用 Post 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
* 如无特殊说明，调用参数值应转码为：UTF-8, URL编码 [^1]。

 [1]: [URL编码 - WikiPedia定义](http://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

</br>
## API 资源列表

### 短信发送 API
<div class="table-d" align="center" >
        <table border="1" width = "100%">
                <tr  bgcolor="#D3D3D3" >
                        <th style="width: 185px;">名称</th>
                        <th>资源</th>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms/#api_1">发送文本验证码短信 API<a/></td>
                        <td>POST https://api.sms.jpush.cn/v1/codes</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms/#api_2">发送语音验证码短信 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/voice_codes</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms/#api_3">验证码验证 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/codes/{msg_id}/valid</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms/#api_4">发送单条模板短信 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/messages</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms/#api_5">发送批量模板短信 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/messages/batch</td>
                </tr>
        </table>
</div>

### 短信定时发送 API

<div class="table-d" align="center" >
        <table border="1" width = "100%">
                <tr  bgcolor="#D3D3D3" >
                        <th style="width: 185px;">名称</th>
                        <th>资源</th>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_1">单条定时短信提交 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/schedule</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_2">批量定时短信提交 API</a></td>
                        <td>POST https://api.sms.jpush.cn/v1/schedule/batch</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_3">单条定时短信修改 API</a></td>
                        <td>PUT https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_4">批量定时短信修改 API</a></td>
                        <td>PUT https://api.sms.jpush.cn/v1/schedule/batch/{schedule_id}</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_5">定时短信查询API</a></td>
                        <td>GET https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_api_jsms_schedule/#api_6">定时短信删除 API</a></td>
                        <td>DELETE https://api.sms.jpush.cn/v1/schedule/{schedule_id}</td>
                </tr>
				<tr>
        </table>
</div>

### 短信余量查询 API

<div class="table-d" align="center" >
        <table border="1" width = "100%">
                <tr  bgcolor="#D3D3D3" >
                        <th style="width: 185px;">名称</th>
                        <th>资源</th>
                </tr>
				</tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_jsms_api_account/#api_1">账号余量查询 API</a></td>
                        <td>GET https://api.sms.jpush.cn/v1/accounts/dev</td>
                </tr>
                <tr >
                        <td><a href="https://docs.jiguang.cn/jsms/server/rest_jsms_api_account/#api_2">应用余量查询 API</a></td>
                        <td>GET https://api.sms.jpush.cn/v1/accounts/app</td>
                </tr>
        </table>
</div>

</br>
## 返回码
若请求失败，API 会返回如下 JSON 格式的返回码及说明

```json
{
    "error": {
        "code": *****,
        "message": "*****"
    }
}
```

### REST API 返回码汇总

|HTTP CODE| CODE| MESSAGE  | DESC|
|:--- |:--- |:--- |:----
|200|50000|success|请求成功
|400|50001|missing auth|auth 为空
|401|50002|auth failed|auth 鉴权失败
|400|50003|missing body|body 为空
|400|50004|missing mobile|手机号码为空
|400|50005|missing  temp_id|模版ID 为空
|403|50006|invalid mobile|手机号码无效
|403|50007|invalid body|body 无效
|403|50008|no sms code auth|未开通短信业务
|403|50009|out of freq|发送超频
|403|50010|invalid code|验证码无效
|403|50011|expired code|验证码过期
|403|50012|verified code|验证码已验证过
|403|50013|invalid temp_id|模版ID 无效
|403|50014|no money|可发短信余量不足
|400|50015|missing code|验证码为空
|404|50016|api not found|API 不存在
|415|50017|media not supported|媒体类型不支持
|405|50018|request method not support|请求方法不支持
|500|50019|server error|服务端异常|
|403|50020|template auditing|模板审核中
|403|50021|template not pass|模板审核未通过
|403|50022|parameters not all replaced|模板中参数未全部替换|
|403|50023|parameters is empty|参数为空|
|403|50024|unsubscribed mobile|手机号码已退订|
|403|50025|wrong template type|该 API 不支持此模版类型|
|403|50026|wrong msg_id|msg_id 无效|
|403|50027|invalid send_time|send_time 为空或在当前时间之前|
|403|50028|invalid schedule_id|schedule_id 无效|
|403|50029|wrong schedule status|定时短信已发送或已删除，无法再修改|
|403|50030|recipients is empty|recipients 为空|
|403|50031|too much recipients|recipients 短信接收者数量超过1000|
|403|50034|repeat send|重复发送|
|403|50035|illegal IP|非法 IP 请求|
|403|50036|app in black|应用被列为黑名单|
|403|50037|has black word|短信内容存在敏感词汇|
|403|50038|invalid code length|语音验证码长度错误|
|403|50039|invalid code type|语音验证码内容错误，验证码仅支持数字|
|403|50040|invalid voice language type|语音验证码播报语言类型错误|
|403|50041|invalid ttl value|验证码有效期错误|