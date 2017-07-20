
# REST API 概述
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<ul style="margin-bottom: 0;">
<li>使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；</li>
<li>API 请求的内容和响应完全使用 JSON 格式；</li>
<li>短信所有 API 返回码汇总；</li>
</ul>
</div>
</br>

## HTTP 验证
> 使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；

HTTP Header（头）里加一个字段（Key/Value对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64(appKey:masterSecret)，即:对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。appKey、masterSecret 可以在控制台应用设置中查看。

## JSON格式
> API 请求的内容和响应完全使用 JSON 格式；

HTTP Header（头）里加一个字段（Key/Value对）：

```
Content-Type: application/json
```


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

###短信 API 返回码汇总

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
