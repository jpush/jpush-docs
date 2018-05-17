# JMessage API PHP Client
[Github](https://github.com/jpush/jmessage-api-php-client)

This is a development package in PHP version for the JMessage REST API. It is provided by the JPush officially and generally supports the latest API functionality.

Corresponding REST API documentation: https://docs.jiguang.cn/jmessage/server/rest_api_im/

> Supported PHP versions: 5.4 ～ 5.6.x, 7

## Installation

#### Install by Composer

- Add the jmessage dependency in the project's  `composer.json` file

```json
"require": {
    "jiguang/jmessage": "~1.1"
}
```

- Perform a  `$ php composer.phar install` or `$ composer install` to install

#### Download source code directly to install

> Directly download source code is also a method to install SDK. However, because of maintenance problems of version updates, this type of installation is not recommended. Composer cannot be used sometimes due to various reasons. Therefore, we also provide backups for this situation.

- Download the source code package and unzip it into the project
- Introduce autoload in the project (in the root directory of source code)

```php
require 'path_to_sdk/autoload.php';
```

## Usage

* [JMessage Client](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#jmessage-client)
* [Certificate issues](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#证书问题)
* [User](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#user-用户)
* [Admin](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#admin-管理员)
* [Blacklist](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#blacklist-黑名单)
* [Group](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#group-群组)
* [Friend](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#friend-好友)
* [Resource](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#resource-媒体资源)
* [Message](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#消息相关)
* [SensitiveWord](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#sensitiveword-敏感词)
* [ChatRoom](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/GUIDE.md#chatroom-聊天室)
* [Cross App](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/CROSS.md#cross-跨应用)
* [Report](https://github.com/jpush/jmessage-api-php-client/blob/master/docs/REPORT.md)

## Examples

**Note: This is just a sample and should not be used directly in the actual environment!!**

There is a simple sample code in the project's [examples folder](https://github.com/jpush/jmessage-api-php-client/tree/master/examples). Developers can refer to the examples for a quick understanding of how to use the library.

Note: The downloaded sample code cannot be used immediately. You need to fill in the `examples/config.php` with the necessary parameters, or set the relevant environment variables. If you do not do this, the sample operation will fail. In addition to protecting developer privacy, examples/config.php file is not in version control and needs to be manually copied by using the following command:

```sh
$ cp examples/config.php.example examples/config.php
```

**Simple of example usage**

To run the sample code in friend_examples.php

```sh
# 假定当前目录为 JMessage 源码所在的根目录
$ php examples/friend_examples.php
```

> Of course, you can also edit the relevant sample file and change the parameters to see the implementation effect.

## ErrorCode

Error code reported by the JMessage server. It may appear in the return value, which can be queried here: https://docs.jiguang.cn/jmessage/client/im_errorcode_server/

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jmessage-api-php-client.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
