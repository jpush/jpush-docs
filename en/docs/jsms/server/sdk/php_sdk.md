# JSMS API PHP CLIENT

[Github](https://github.com/jpush/jsms-api-php-client)

This is a PHP version development package for SMS API. It is provided officially by Jiguang and generally supports the latest API features.

Corresponding API documentation: https://docs.jiguang.cn/jsms/server/rest_api_summary/

> Supported PHP versions: 5.3.3 to 5.6.x, 7.0.x
> must have cURL extension enabled

## Installation

- Add JSMS dependencies in the `composer.json` file in your project

```json
"require": {
    "jiguang/jsms": "*"
}
```

- Perform `$ php composer.phar install` or `$ composer install` to install

## Usage

#### Initialization

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

#### Certificate Issue

```php
// 禁用 SSL 证书的验证，
$client = new JSMS($app_key, $master_secret, [ 'disable_ssl' => true ]);
```

**We hope that developers will handle SSL certificate issues as they understand the risks involved.**

#### Send Verification Code of Voice SMS

```php
$client->sendCode($phone, $temp_id);
```

**Parameter Description::**

> $phone: Phone number to receive verification code

> $temp_id: Template id

#### Send Verification Code of Voice SMS

```php
$client->sendVoiceCode($phone, $options = []);
```

**Parameter Description::**

> $phone: Phone number to receive verification code

> $options: An array of optional options, accepting one or more of the three keys `ttl`，`code`，`voice_lang`

+ ttl: Timeout. Default is 60 seconds
+ code: The value of voice verification code. The verification code only supports 4-8 digits
+ voice_lang: Broadcast language selection, 0: Chinese, 1: English, 2: Chinese and English

#### Verification

```php
$client->checkCode($msg_id, $code);
```

**Parameter Description::**

> $msg_id: Corresponding value of msg_id key in the array returned by the sendCode function after sending a verification code
> $code: Verification code received by the phone

#### Send Template SMS

```php
$client->sendMessage($mobile, $temp_id, array $temp_para = [], $time = null);
```

**Parameter Description::**

> $phone: Phone number to receive verification code

> $temp_id: Template id

> $temp_para: Template parameter. Parameter name and the corresponding value of pair need to be replaced, and only accepts values in array type

> $time: Sending time of scheduled SMS is in the format of yyyy-MM-dd HH:mm:ss. Defaults `null` to send immediately.

#### Send Template SMS in Batch

```php
$client->sendBatchMessage($temp_id, array $recipients， $time = null);
```

**Parameter Description::**

> $temp_id: Template id

> $recipients: List of receivers, accepting an associative array with a mobile key corresponding to its temp_para value

> $time: Sending time of scheduled SMS is in the format of yyyy-MM-dd HH:mm:ss. Defaults `null` to send immediately.

#### Query Scheduled Template SMS

```php
$client->showSchedule($scheduleId);
```

#### Delete Scheduled Template SMS

```php
$client->deleteSchedule($scheduleId);
```

#### Query Application Margin

```php
$client->getAppBalance();
```

#### Description of Call Return Code

http://docs.jiguang.cn/en/server/rest_api_jsms/#_12

## Examples

There is a simple example code in the downloaded [example folder](https://github.com/jpush/jsms-api-php-client/tree/master/examples). Developers can refer to the sample to quickly understand how to use the library.

> Note: The downloaded sample code can't be used immediately, so you need to fill in the relevant file with the necessary parameters. Otherwise, the sample operation will fail.

#### Simple Use

> Assuming the current directory is the root directory of the JSMS source

+ Edit send_example.php and fill in the information

```php
$appKey = 'xxxx';
$masterSecret = 'xxxx';
$phone = 'xxxxxxxxxxx';
```

- Run the example `$ php examples/send_example.php`

- Get `msg_id` and `code`

- Edit `check_example.php` and fill in the information

```php
$appKey = 'xxxx';
$masterSecret = 'xxxx';
$msg_id = 'xxxx';
$code = 'xxxxxx';
```
- Run the example `$ php examples/check_example.php`

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jsms-api-php-client.

## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
