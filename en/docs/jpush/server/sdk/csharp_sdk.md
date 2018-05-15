# JPush Library for .NET

[Github Source Code](https://github.com/jpush/jpush-api-csharp-client)

JPush .NET API Client officially supported by Jiguang.

> Note: Jiguang.JPush is the refactored version based on .NET Standard. API usage has changed greatly, and it is not compatible with the old version (cn.jpush.api). Please pay attention before upgrading.

Example in the project is the .NET Core Console application.

Development Tools: Visual Studio 2017.

##Install

- [NuGet](https://preview.nuget.org/packages/Jiguang.JPush/)

## Documents

[REST API documents](https://docs.jiguang.cn/jpush/server/push/server_overview/).

## Support

[Jiguang Community](https://community.jiguang.cn/)

## FAQ

1. If there is a deadlock when the asynchronous method is invoked, ie [HttpResponse](https://github.com/jpush/jsms-api-csharp-client/blob/v2-dev/Jiguang.JSMS/Model/HttpResponse.cs), refer to this [article](https://blogs.msdn.microsoft.com/jpsanders/2017/08/28/asp-net-do-not-use-task-result-in-main-context/)。
2. If you are using the .NET Framework 4.0, you need to use the v1 version

## Contribute

Please contribute! [Look at the issues](https://github.com/jpush/jpush-api-csharp-client/issues).

## License
MIT © [JiGuang](/license)
