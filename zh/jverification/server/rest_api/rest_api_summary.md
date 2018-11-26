#REST API
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; ">
<p>特别提示：建议不要在客户端直接调用 Rest API。JVerification 私密信息容易因此暴露给他人，得到 Appkey 和 MasterSecret 信息的人可能进行恶意的调用。
<br>
<p>建议的使用方式是：调用 JVerification Rest API 的代码放在开发者应用服务器上。开发者应用服务器对自己的客户端提供接口，开发者服务器收到来自客户端的请求后再调极光的 API 。
</div>

JVerification 为开发者提供遵从 REST 规范的 HTTP API，以供开发者远程调用 JVerification 提供的服务。

##REST API 基本约束

+ API 被设计为符合 HTTP, REST规范。例如：查询请求使用 Get 方法，提交请求使用 POST 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
+ 如无特殊说明，调用参数值应转码为：UTF-8, [URL编码](https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

##鉴权方式

极光 REST API采用 HTTP 基本认证的验证方式。基本做法为，HTTP Header 中加 Authorization：

~~~
   Authorization: Basic ${base64_auth_string} 
~~~

Header 名称是 "Authorization", 值是 base64转换过的 "appKey:masterSecret"（中间有个冒号）。这两者可以在极光开发者服务的Web控制台[应用设置]-[应用信息]中查看。

###鉴权举例

你的 appKey 是 "7d431e42dfa6a6d693ac2d04", masterSecret 是 "5e987ac6d2e04d95a9d8f0d1"，则调用 Verification API v1 时，使用 curl 命令的话，是这样写：

~~~
   curl --insecure -X POST -v https://api.verification.jpush.cn/v1/web/verify 
   -H "Content-Type: application/json"
   -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
   ...
~~~

HTTP 请求是：

~~~
   > POST /v1/web/verify HTTP/1.1
   > Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
~~~

##API 资源列表

|名称|资源|
|---|---|
|[发起认证API](../verify_api/)|POST https://api.verification.jpush.cn/v1/web/verify|




