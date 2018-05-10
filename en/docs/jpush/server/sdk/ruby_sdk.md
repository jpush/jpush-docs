JPush API Ruby Client
Github Source Code
 
This is the Ruby version package development package for the JPush REST API. It is provided by the JPush officially and generally supports the latest API features.
Corresponding REST API documentation: https://docs.jiguang.cn/jpush/server/push/server_overview/
Supported Ruby Versions: >= 2.2

Installation
Add this line to your application's Gemfile:
gem 'jpush'
# OR
gem 'jpush', git: 'https://github.com/jpush/jpush-api-ruby-client.git'

Usage
    • Getting Started
    • Push API
    • Report API
    • Schedule API
    • Device API
    • Http2 Support

Development
After checking out the repo, run bin/setup to install dependencies. Then, run rake test to run the tests. You can also run bin/console for an interactive prompt that will allow you to experiment.
To install this gem onto your local machine, run bundle exec rake install. To release a new version, update the version number in version.rb, and then run bundle exec rake release, which will create a git tag for the version, push git commits and tags, and push the .gem file to rubygems.org.

Testing
# Copy the test configuration file
$ cp test/config.yml.example test/config.yml

# Edit the test/config.yml file and fill in the required variable values
# OR setting the appropriate environment variable

# Run all test cases
$ bundle exec rake

# Run a specific test case
$ bundle exec rake test TEST=test/jpush/xx_test.rb

Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/jpush/jpush-api-ruby-client.

License
The gem is available as open source under the terms of the MIT License.