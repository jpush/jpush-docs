<h1> API Deubg Guide</h1>

```
请选用 v2 版本 API。 v1 版本已经停止使用。
```

###Library 选择

+ 如果 API 调用使用 Java，则建议使用 JPush 提供的 JPush API Library。
+ 避免自己写代码组装 JSON 字符串，而使用一些成熟的第三方 library 来生成。

###具体问题

####拼接verification_code的最后一个参数master_secret如何获取

请登陆portal，在你所创建应用的应用详情界面可以获取到。

####1002：app_key doesn't exist 

可能有两个原因：

+ 没有传appkey或key填写无效（如多了空格）
+ 没有按照要求post：HTTP Post 的Content-Type 需采用 application/x-www-form-urlencoded
+ 只有msg_content的内容是json，其它的参数都是post的键值
 

####1003 msg_content should be JSON format

大多数时候是由于自己写代码拼装 JSON，而 JSON 的特殊字符没有做转义引起的。建议使用第三方 JSON 库来生成 JSON 字符串。

另外一个常见的原因是，字符串不是 utf-8 编码。


####1004 verification_code is incorrect

+ 拼接verification_code的参数不对：由 sendno, receiver_type, receiver_value, master_secret 4个值拼接起来（直接拼接字符串）
+ md5有问题，需要32位大写
+ 你的编码不是utf-8

具体看[Push API v2](../push_api_v2)中的verification_code参数

####不用登录Jpush的portal界面，在APP的面板中直接发送通知可以吗？

可以。直接封装Jpush的V2 API就可以了，具体可参考 [Push API v2](../push_api_v2)


###官方帮助

当出现问题时，建议仔细阅读官方文档，看看有没有什么遗漏信息。如果还是无法解决，建议在[QA问答网站](https://www.jpush.cn/qa/)搜索，有没有碰到类似信息

如果还是无法解决，可以通过以下途径寻求帮助

1. 官方的QA问答网站  [https://www.jpush.cn/qa/ ](https://www.jpush.cn/qa/ )
2. 给我们的support发邮件 (如果有敏感信息，建议使用support邮箱)   <support@jpush.cn>

为了更高效，快速的解决问题，在寻求帮助时，请提供下列信息：

1. API的接口， 比如  [http://api.jpush.cn:8800/v2/push](http://api.jpush.cn:8800/v2/push)
2. 提供appkey，massageid信息
3. 提供调用API出现问题时的时间

