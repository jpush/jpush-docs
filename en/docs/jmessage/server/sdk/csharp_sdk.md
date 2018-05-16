# JMessage Library for .NET
[Github 源码](https://github.com/jpush/jmessage-api-csharp-client)

JMessage's officially supported .NET library for accessing JMessage APIs.

极光官方支持的 IM .NET 服务器端 SDK。

## Install

[Nuget](https://www.nuget.org/packages/Jiguang.JMessage)

## Example

可参考项目 *./Test* 目录中的测试代码。

## Document

[REST API document](http://docs.jiguang.cn/jmessage/server/rest_api_im/).

## Support

- [Issues](https://github.com/jpush/jmessage-api-csharp-client/issues)
- [极光社区](https://community.jiguang.cn/)

## FAQ

1. 如果调用异步方法时出现死锁，即一直没有返回 HttpResponse，可参考这篇[文章](https://blogs.msdn.microsoft.com/jpsanders/2017/08/28/asp-net-do-not-use-task-result-in-main-context/)。

1. 因为使用了 HttpClient，所以当前 library 不支持 .NET Framework 4.0 及以下版本。因此如果是这些版本的话，建议使用 [v1](https://github.com/jpush/jmessage-api-csharp-client/tree/v1) 版本的 library。

## Contribute

Please contribute! [Look at the issues](https://github.com/jpush/jmessage-api-csharp-client/issues).

## License

MIT © [JiGuang](https://github.com/jpush/jmessage-api-csharp-client/blob/master/license)