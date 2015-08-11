<h1>JPush API client library for PHP</h1>

###概述

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px;">
<p>温馨提示：</p>
<p>详细API介绍文档地址   <a href="https://github.com/jpush/jpush-api-php-client/blob/master/doc/api.md">JPush Api PHP client doc</a></p>
</div>

<br>

这是 JPush REST API 的 PHP 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。



对应的 REST API 文档：

+ [REST API - Push](../rest_api_v3_push/)

+ [REST API - Report](../rest_api_v3_report/)

版本更新:[Release](../../resources/#sdk_1)页面有详细的版本发布记录与下载。

###依赖

PHP >= 5.3

#### 快速安装

JPush PHP Library 使用 Composer管理项目依赖, 鉴于某些原因, 国内的用户使用Composer下载依赖库比较困难,所以我们将Composer依赖打包. 用户可以通过以下方式在您的项目中加入JPush PHP Library.


* 下载依赖包 [vendor.tar.gz](http://7qn8xa.com1.z0.glb.clouddn.com/vendor.zip)

* 解压vendor.tar.gz到您的项目目录下，在需要使用JPush的源文件头部 引入 vendor/autoload.php 既可使用.

```
# 引入代码
php require_once 'vendor/autoload.php';
```

#### 使用Composer 

如果你的项目使用composer管理依赖, 可以通过以下方式使用JPush PHP Library.

* 在 composer.json 中添加 jpush依赖, 如目前最新版本为 v3.2.1

```
{
    "require":{
        "jpush/jpush": "v3.2.1"
    }
}
```

* 执行 php composer.phar install 或 php composer.phar update


### 快速使用

####Example


下载的[JPush PHP Library](http://docs.jpush.cn/download/attachments/2228302/jpush-api-php-client-3.2.2.zip?version=1&modificationDate=1422968810000) example文件夹有简单示例代码, 开发者可参考以快速使用该库


├── examples

│   ├── composer.json　项目依赖

│   ├── DeviceExample.php 对Tag, Alias, Registeration_id的操作示例

│   ├── PushExample.php　推送示例

│   ├── README.md　说明

│   ├── ReportExample.php　获取统计信息示例

│   └── ValidateExample.php　使用validate接口示例




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


### FAQ
Q: 运行示例提示　require_once(vendor/autoload.php): failed to open stream 怎么解决?

A: 下载下载依赖包 [vendor.tar.gz](http://7qn8xa.com1.z0.glb.clouddn.com/vendor.zip) 并解压到examples目录即可, 也可以使用composer管理依赖, 在composer.json中加入 "jpush/jpush": "v3.2.1" 并执行 php composer.phar install 即可.


Q: 运行示例提示

```
Fatal error: Uncaught exception 'UnexpectedValueException' with message 'The stream or file "jpush.log" could not be opened: failed to open stream: Permission denied
```
该如何解决?

A: 此问题是因为工程没有写入权限导致不能生成日志文件. 只需对赋予该项目对本目录的写入权限即可,如 sudo chmod 777 example

Q: 使用示例每次推送都会打印推送的JSON, 如何禁止其打印?

A: 在调用示例推送的时候, 注释掉 ->printJSON() 即可, 该函数可以打印当前构建的推送对象.