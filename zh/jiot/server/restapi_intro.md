# 服务端 REST API 概述

##REST API 基本约束
+ API 被设计为符合 HTTP, REST规范。例如：查询请求使用 Get 方法，提交请求使用 POST 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
+ 如无特殊说明，调用参数值应转码为：UTF-8, [URL编码](https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

##鉴权方式
极光 REST API 采用 [HTTP 基本认证](http://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81) 的验证方式。

基本作法为，HTTP Header（头）里加 Authorization：

    Authorization: Basic ${base64_auth_string}


Header 名称是 "Authorization", 值是 base64转换过的 "ProductKey:ProductSecret"（中间有个冒号）。这两者可以在极光 IoT 服务的Web控制台[产品设置]中查看。


## API 频率控制
### 属性设置频率
每个 ProductKey 在 1 分钟内最多可调用 1000 次属性设置操作。 若超出返回 Too Many Requests 错误。    

### 消息下发频率
每个 ProductKey 在 1 分钟内最多可调用 1000 次消息下发操作。 若超出返回 Too Many Requests 错误。

## 文档参考

+ [Wikipedia HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
