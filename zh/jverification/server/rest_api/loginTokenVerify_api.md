#loginTokenVerify API

##功能说明

+ 提交loginToken，验证后返回手机号码

##调用地址

+ POST https://api.verification.jpush.cn/v1/web/loginTokenVerify

##请求示例

~~~
   curl --insecure -X POST -v https://api.verification.jpush.cn/v1/web/loginTokenVerify -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"loginToken":"STsid0000001542695429579Ob28vB7b0cYTI9w0GGZrv8ujUu05qZvw","exID":"1234566"}'
~~~

+ 请求参数

|KEY|REQUIRE|DESCRIPTION| 
|:---:|:---:|:---:|
|loginToken|True|认证SDK获取到的loginToken|
|exID|False|开发者自定义的id，非必填|

##响应示例

**请求成功**

~~~
   {"id":117270465679982592,"code":8000,"content":"get phone success","exID":"1234566","phone":"HpBLIQ/6SkFl0pAq0LMdw1aZ8RHoofgWmaY//LE+0ahkSdHC5oTCnjrR8Tj8y5naKVI03torFU+EzAQnwtVqAoQyYckT0S3Q02TKuAal3VRGiR5Lmp4g2A5Mh4/W5A4o6QFviHuBVJZE/WV0AzU5w4NGhpyQntOeF0UyovYATy4="}
~~~

**请求失败**

~~~
   {"code":8001,"content":"get phone fail"}
~~~

+ 响应参数

|KEY|DESCRIPTION| 
|:---:|:---:|
|id|流水号，请求出错时可能为空|
|exID|开发者自定义的id，若请求时为空返回为空|
|code|返回码|
|content|返回码说明|
|phone|加密后的手机号码，需用配置在极光的公钥对应的私钥解密|
