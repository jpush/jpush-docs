#Verify API

##功能说明

+ 提交手机号码和token，验证是否一致

##调用地址

+ POST https://api.verification.jpush.cn/v1/web/verify

##请求示例

~~~
   curl --insecure -X POST -v https://api.verification.jpush.cn/v1/web/verify -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"token":"STsid0000001542695429579Ob28vB7b0cYTI9w0GGZrv8ujUu05qZvw","phone":15813554612,"carrier":"CM","platform":"a","exID":"1234566"}'
~~~

+ 请求参数

|KEY|REQUIRE|DESCRIPTION| 
|:---:|:---:|:---:|
|token|True|运营商下发的token|
|phone|True|待认证的手机号码|
|exID|False|开发者自定义的id，非必填|

##响应示例

**请求成功**

~~~
   {"id":117270465679982592,"code":9000,"content":"verify consistent","exID":"1234566"}
~~~

**请求失败**

~~~
   {"code":9011,"content":"auth failed"}
~~~

+ 响应参数

|KEY|DESCRIPTION| 
|:---:|:---:|
|id|流水号，请求出错时可能为空|
|exID|开发者自定义的id，若请求时为空返回为空|
|code|返回码|
|content|返回码说明|
