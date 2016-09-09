# JPush API Ruby Client

[![Build Status](https://travis-ci.org/jpush/jpush-api-ruby-client.svg?branch=master)](https://travis-ci.org/jpush/jpush-api-ruby-client)
[![Gem Version](https://badge.fury.io/rb/jpush.svg)](https://badge.fury.io/rb/jpush)

这是 JPush REST API 的 Ruby 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。
对应的 REST API 文档: [Push Rest API](../push/rest_api_v3_push),
支持 Ruby 版本 >= 2.2.0

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'jpush'
# OR
gem 'jpush', git: 'https://github.com/jpush/jpush-api-ruby-client.git'
```

## Usage

- [Getting Started](https://github.com/jpush/jpush-api-ruby-client/blob/master/docs/Guides.md#getting-started)
- [Push API](https://github.com/jpush/jpush-api-ruby-client/blob/master/docs/Guides.md#push-api)
- [Report API](https://github.com/jpush/jpush-api-ruby-client/blob/master/docs/Guides.md#report-api)
- [Schedule API](https://github.com/jpush/jpush-api-ruby-client/blob/master/docs/Guides.md#schedule-api)
- [Device API](https://github.com/jpush/jpush-api-ruby-client/blob/master/docs/Guides.md#device-api)

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake test` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Testing

```bash
# 复制测试的配置文件
$ cp test/config.yml.example test/config.yml

# 编辑 test/config.yml 文件，填入必须的变量值
# OR 设置相应的环境变量

# 运行全部测试用例
$ bundle exec rake

# 运行某一具体测试用例
$ bundle exec rake test TEST=test/jpush/xx_test.rb
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jpush-api-ruby-client.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).