# JMessage Library for .NET

[Github Source Code](https://docs.jiguang.cn/jmessage/server/sdk/csharp_sdk/)

JMessage's officially supported .NET library for accessing JMessage APIs.

IM .NET server-side SDK officially supported by Jiguang.

## Install

[Nuget](https://www.nuget.org/packages/Jiguang.JMessage)

## Example

Refer to the test code in the ./Test directory.

## Document

[REST API document](http://docs.jiguang.cn/jmessage/server/rest_api_im/).

## Support

- [Issues](https://github.com/jpush/jmessage-api-csharp-client/issues)
- [Jiguang Community](https://community.jiguang.cn/)

## FAQ

1. If there is a deadlock when calling the asynchronous method, ie HttpResponse has not been returned, please refer to [this article](https://blogs.msdn.microsoft.com/jpsanders/2017/08/28/asp-net-do-not-use-task-result-in-main-context/).

2. Because HttpClient is used, the current library does not support .NET Framework 4.0 or below. Therefore, if they are these versions, it is recommended to use the [v1 version](https://github.com/jpush/jmessage-api-csharp-client/tree/v1) of the library.

## Contribute

Please contribute! [Look at the issues](https://github.com/jpush/jmessage-api-csharp-client/issues).

## License

MIT © [JiGuang](https://github.com/jpush/jmessage-api-csharp-client/blob/master/license)