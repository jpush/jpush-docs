# JSMS API PHP Client

这是短信 API 的 PHP 版本封装开发包，是由极光官方提供的，一般支持最新的 API 功能。

对应的 API 文档：<http://docs.jiguang.cn/server/rest_api_jsms/>

> 支持的 PHP 版本: 5.3.3 ～ 5.6.x, 7.0.x
> 须启用 cURL 扩展

## Installation

- 在项目中的 `composer.json` 文件中添加 JSMS 依赖：

```json
"require": {
    "jiguang/jsms": "v1.0.*"
}
```

- 执行 `$ php composer.phar install` 或 `$ composer install` 进行安装。

## Usage

#### 初始化

```php
use JiGuang\JSMS as JSMS;
...
...

    $client = new JSMS($app_key, $master_secret);

...
```

OR

```php
$client = new \JiGuang\JSMS($app_key, $master_secret);
```

#### 证书问题

```php
// 禁用 SSL 证书的验证，
$client = new JSMS($app_key, $master_secret, [ 'ssl_verify' => false ]);
```

**希望开发者在了解相关风险的前提下如此处理 SSL 证书问题。**

#### 发送验证码

```php
$client->sendCode($phone, $temp_id);
```

> 参数说明:

> $phone: 接收验证码的手机号码
> $temp_id: 模板ID

#### 发送语音短信验证码

```php
$client->sendVoiceCode($phone);
# OR
$client->sendVoiceCode($phone, $ttl);
```

> 参数说明:

> $phone: 接收验证码的手机号码
> $ttl: 超时时间，默认为 60 秒

#### 验证

```php
$client->checkCode($msg_id, $code)
```

> 参数说明:

> $msg_id: 发送验证码 sendCode 函数返回的数组中的 msg_id 键对应的值
> $code: 手机接收到的验证码

#### 发送模板短信

```php
$client->sendMessage($mobile, $temp_id, $temp_para)
```

> 参数说明:

> $phone: 接收验证码的手机号码
> $temp_id: 模板 ID
> $temp_para: 模板参数,需要替换的参数名和 value 的键值对,仅接受数组类型的值

#### 调用返回码说明

http://docs.jiguang.cn/server/rest_api_jsms/#_12

## Examples

在下载的中的 [examples](https://github.com/jpush/jsms-api-php-client/tree/master/examples) 文件夹有简单示例代码, 开发者可以参考其中的样例快速了解该库的使用方法。

> **注：所下载的样例代码不可马上使用，需要在相应文件中填入相关的必要参数，不然示例运行会失败**

#### 简单使用方法

> 假定当前目录为 JSMS 源码所在的根目录

- 编辑 send_example.php 文件，填写信息

```php
$appKey = 'xxxx';
$masterSecret = 'xxxx';
$phone = 'xxxxxxxxxxx';
```

- 运行示例 `$ php examples/send_example.php`

- 获取 `msg_id` 和 `code`

- 编辑 check_example.php 文件，填写信息

```php
$appKey = 'xxxx';
$masterSecret = 'xxxx';
$msg_id = 'xxxx';
$code = 'xxxxxx';
```
- 运行示例 `$ php examples/check_example.php`

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jsms-api-php-client.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
