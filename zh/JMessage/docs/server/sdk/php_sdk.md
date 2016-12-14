# JMessage API PHP Client

这是 JMessage REST API 的 PHP 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。

对应的 REST API 文档: https://docs.jiguang.cn/jmessage/server/rest_api_im/

> 支持的 PHP 版本: 5.3.3 ～ 5.6.x, 7

## Installation

#### 使用 Composer 安装

- 在项目中的 `composer.json` 文件中添加 jmessage 依赖：

```json
"require": {
    "jiguang/jmessage": "1.0.*"
}
```

- 执行 `$ php composer.phar install` 或 `$ composer install` 进行安装。

#### 直接下载源码安装

> 直接下载源代码也是一种安装 SDK 的方法，不过因为有版本更新的维护问题，所以这种安装方式**十分不推荐**，但由于种种原因导致无法使用 Composer，所以我们也提供了这种情况下的备选方案。

- 下载源代码包，解压到项目中
- 在项目中引入 autoload（在源码根目录下）：

```php
require 'path_to_sdk/autoload.php';
```

## Usage

* [JMessage Client](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#jmessage-client)
* [User 用户](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#user-用户)
* [Admin 管理员](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#admin-管理员)
* [Blacklist 黑名单](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#blacklist-黑名单)
* [Group 群组](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#group-群组)
* [Friend 好友](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#friend-好友)
* [Resource 媒体资源](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#resource-媒体资源)
* [发送消息](https://github.com/jpush/jmessage-api-php-client/blob/master/GUIDE.md#发送消息)

## Examples

**注意: 这只是使用样例, 不应该直接用于实际环境中!!**

在项目的 [examples](https://github.com/jpush/jmessage-api-php-client/tree/master/examples) 文件夹中有简单的使用示例代码, 开发者可以参考其中的样例快速了解该库的使用方法。

**注：所下载的样例代码不可马上使用，需要在 `examples/config.php` 文件中填入相关的必要参数，或者设置相关环境变量，不进行这个操作则示例运行会失败。**另外为保护开发者隐私 `examples/config.php` 文件不在版本控制中，需要使用如下命令手动复制：

```php
$ cp examples/config.php.example examples/config.php
```

**示例简单使用方法**

若要运行 friend_examples.php 中的示例代码：

```bash
# 假定当前目录为 JMessage 源码所在的根目录
$ php examples/friend_examples.php
```
> 当然也可编辑相关的示例文件，更改参数查看执行效果

## ErrorCode

JMessage 服务器端报的错误码。有可能出现在返回值中，可在这里查询含义： https://docs.jiguang.cn/jmessage/client/im_errorcode_server/

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jmessage-api-php-client.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
