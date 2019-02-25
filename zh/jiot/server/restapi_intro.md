# 服务端 REST API 概述

##REST API 基本约束
+ API 被设计为符合 HTTP, REST规范。例如：查询请求使用 Get 方法，提交请求使用 POST 方法。如果一个请求不是相应的 HTTP 方法，将返回错误。
+ 如无特殊说明，调用参数值应转码为：UTF-8, [URL编码](https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81)

##鉴权方式
极光 REST API 采用 [HTTP 基本认证](http://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81) 的验证方式。

基本作法为，HTTP Header（头）里加 Authorization：

    Authorization: Basic ${base64_auth_string}


Header 名称是 "Authorization", 值是 base64转换过的 "ProductKey:ProductSecret"（中间有个冒号）。这两者可以在极光 IoT 服务的Web控制台[产品设置]中查看。



### 鉴权举例

你的 appKey 是 "7d431e42dfa6a6d693ac2d04", masterSecret 是 "5e987ac6d2e04d95a9d8f0d1"，则调用 Push API v3 时，使用 curl 命令的话，是这样写：

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json"
-u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1"
-d  '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush!"}}'
```

HTTP 请求发出的请求是：

```
> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```
## API 频率控制
### 属性设置频率
每个 ProductKey 在 30 秒内最多可调用 100 次属性设置操作。 若超出返回 Too Many Requests 错误。    

### 消息下发频率
每个 ProductKey 在 30 秒内最多可调用 100 次消息下发操作。 若超出返回 Too Many Requests 错误。

## 文档参考

+ [Wikipedia HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
