JPush API PHP Client
Github Source Code
This is a PHP version development package for the JPush REST API. It is provided by the JPush officially and generally supports the latest API features.
Corresponding REST API documentation: https://docs.jiguang.cn/jpush/server/push/server_overview/ 
Supported PHP versions:5.3.3 ～ 5.6.x, 7.0.x
If PHP 5.3.3 and lower versions need to be compatible, you can use the v3 branch code. Since running Composer requires PHP 5.3.2+ or later, it does not provide Composer support. You can also click the link to download the source code of v3.4.x version.

Installation
Use Composer to install
    • Add the jpush dependency to the composer.json  file in the project
"require": {
    "jpush/jpush": "^3.5"
}
    • Perform a $ php composer.phar install  or  $ composer install for installation.
Directly Download Source Code to Install
Directly downloading the source code is also a method of installing the SDK. However, because of maintenance problems of version updates, this type of installation is not recommended. We provide backups for this situation where Composer cannot be used due to various reasons.
    • Download the source code package and unzip it into the project
    • Introduce autoload in the project
require 'path_to_sdk/autoload.php';

Usage
    • Init API
    • Push API
    • Report API
    • Device API
    • Schedule API
    • Exception Handle
    • HTTP/2 Support
    • Group Push
Initialization
use JPush\Client as JPush;
...
...

    $client = new JPush($app_key, $master_secret);

...
OR
$client = new \JPush\Client($app_key, $master_secret);
Simple Push
$client->push()
    ->setPlatform('all')
    ->addAllAudience()
    ->setNotificationAlert('Hello, JPush')
    ->send();
Exception Handling
$pusher = $client->push();
$pusher->setPlatform('all');
$pusher->addAllAudience();
$pusher->setNotificationAlert('Hello, JPush');
try {
    $pusher->send();
} catch (\JPush\Exceptions\JPushException $e) {
    // try something else here
    print $e;
}

Examples
Note: This is just a sample and should not be used directly in the actual environment!!
There is a simple example code in the download examples folder, and developers can refer to the sample to quickly understand how to use the library.
Note: The downloaded sample code cannot be used immediately. You need to fill in the examples/config.php file with necessary parameters, or set the relevant environment variables. Otherwise the sample operation will fail. In order to protect developer privacy, the examples/config.php file is not in version control and needs to be manually copied by using the following command:
$ cp examples/config.php.example examples/config.php
Simple Use
To run the sample code in push_example.php:：
# Assume that the current directory is the root directory of the JPush source
$ php examples/push_example.php
At the same time can also edit the relevant sample files, and change the parameters to view the effect of the execution

Testing
# Edit the tests/bootstrap.php file and fill in the required variable values
# OR setting the corresponding environment variable

# Run all test cases
$ composer tests

#Run a specific test case
$ composer tests/JPush/xxTest.php

Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jpush-api-php-client.

License
The library is available as open source under the terms of the MIT License.