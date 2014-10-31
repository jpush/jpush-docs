<h1>JPush API client library for PHP</h1>

###概述

这是 JPush REST API 的 PHP 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。


对应的 REST API 文档：
+ [REST API - Push](../rest_api_v3_push/)
+ [REST API - Report](../rest_api_v3_report/)
+ [JPush Api PHP client doc](https://github.com/jpush/jpush-api-php-client/blob/master/doc/api.md)

版本更新:[Release](https://github.com/jpush/jpush-api-php-client/releases/)页面有详细的版本发布记录与下载。

###依赖

PHP >= 5.3

#### 快速安装

解压 examples/vendor.tar.gz 到项目目录，在需要使用JPush的源文件头部 引入 vendor/autoload.php 既可使用。

```
require_once 'vendor/autoload.php';
```

#### Composer install


Use composer to fetch the library and dependencies defined in composer.json, and install them:

```
#download the composer.phar
$ curl -sS https://getcomposer.org/installer | php
#install by composer.json
$ php composer.phar install
```

### 快速使用

####Easy Push

```
require_once 'vendor/autoload.php';

use JPush\Model as M;
use JPush\JPushClient;
use JPush\Exception\APIConnectionException;
use JPush\Exception\APIRequestException;

$br = '<br/>';
$client = new JPushClient($app_key, $master_secret);

$result = $client->push()
    ->setPlatform(M\all)
    ->setAudience(M\all)
    ->setNotification(M\notification('Hi, JPush'))
    ->send();
echo 'Push Success.' . $br;
echo 'sendno : ' . $result->sendno . $br;
echo 'msg_id : ' .$result->msg_id . $br;
echo 'Response JSON : ' . $result->json . $br;
```

#### Easy Report

```
require_once 'vendor/autoload.php';

use JPush\Model as M;
use JPush\JPushClient;
use JPush\Exception\APIConnectionException;
use JPush\Exception\APIRequestException;

$br = '<br/>';

$client = new JPushClient($app_key, $master_secret);

$msg_ids = '1931816610,1466786990,1931499836';
$result = $client->report($msg_ids);
foreach($result->received_list as  $received) {
    echo '---------' . $br;
    echo 'msg_id : ' . $received->msg_id . $br;
    echo 'android_received : ' .  $received->android_received . $br;
    echo 'ios_apns_sent : ' .  $received->ios_apns_sent . $br;
}
```


