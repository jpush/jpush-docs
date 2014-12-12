<h1>JPush API Ruby Client</h1>


### 概述

这是 JPush REST API 的 Ruby 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。

gem : ([https://rubygems.org/gems/jpush](https://rubygems.org/gems/jpush))

对应的 REST API 文档：[REST API - Push](../rest_api_v3_push/), [REST API - Report](../rest_api_v3_report/). 

本开发包 Rubydoc：[JPush API Ruby Client Doc](http://www.rdoc.info/github/jpush/jpush-api-ruby-client/master/frames)

版本更新：[Release页面](../../resources/#sdk_1)。下载更新请到这里。

### Installation

Add this line to your application's Gemfile:

```
gem 'JPush'
```
And then execute:

```
$ bundle
```
Or install it yourself as:

local install

```
$ gem build jpush.gemspec
$ gem install jpush -l
```

### 使用样例

####推送样例

以下片断来自项目代码里的文件：example/push_example.rb

```
require 'JPush'

master_secret = '2b38ce69b1de2a7fa95706ea';
app_key = 'dd1066407b044738b6479275';
client = JPush::JPushClient.new(app_key, master_secret);

logger = Logger.new(STDOUT);

payload =JPush::PushPayload.new(platform: JPush::Platform.all,
    audience: JPush::Audience.all,
    notification: JPush::Notification.new(alert: 'alert meassage')
).check

result = client.sendPush(payload);
logger.debug("Got result  " + result)
```

####统计获取样例

以下片断来自项目代码里的文件：example/report_example.rb
```
require 'JPush'

master_secret = '2b38ce69b1de2a7fa95706ea';
app_key = 'dd1066407b044738b6479275';
client = JPush::JPushClient.new(app_key, master_secret);
logger = Logger.new(STDOUT);

#getReceiveds
result = client.getReportReceiveds('1942377665')
logger.debug("Got result - " + result)
```

#### device 样例

以下片断来自项目代码里的文件：example/device_example.rb

```
require 'jpush'

master_secret = '2b38ce69b1de2a7fa95706ea'
app_key = 'dd1066407b044738b6479275'
client = JPush::JPushClient.new(app_key, master_secret)
logger = Logger.new(STDOUT)
# Get user profile
user_profile = client.getDeviceTagAlias('0900e8d85ef')
logger.debug("Got result " + user_profile.toJSON)
# Update Device Tag Alias
add = ['tag1', 'tag2'];
remove = ['tag3', 'tag4'];
tagAlias = JPush::TagAlias.build(:add=> add, :remove=> remove, :alias=> 'alias1')
result = client.updateDeviceTagAlias('0900e8d85ef', tagAlias)
logger.debug("Got result " + result.code.to_s)
```

###单元测试

```
$ rake
```