# JSMS API JAVA CLIENT

[Github](https://github.com/jpush/jsms-api-java-client)

### Overview

This is a Java version development package of SMS Rest API. It is officially provided by JPush and generally supports the latest API functions.
Corresponding Rest API documentation: http://docs.jiguang.cn/server/rest_api_jsms/

## Installation

### Way of maven

Place the following dependencies in your project's maven pom.xml.

> Slf4j can work with log frames such as logback, log4j, and commons-logging, and can be configured and used according to your needs.

```xml
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jsms-client</artifactId>
    <version>1.2.8</version>
</dependency>
<dependency>
	<groupId>com.google.code.gson</groupId>
	<artifactId>gson</artifactId>
	<version>2.3</version>
</dependency>
<dependency>
	<groupId>org.slf4j</groupId>
	<artifactId>slf4j-api</artifactId>
	<version>1.7.7</version>
</dependency>
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jiguang-common</artifactId>
    <version>1.0.8</version>
</dependency>
<!-- For log4j -->
<dependency>
	<groupId>org.slf4j</groupId>
	<artifactId>slf4j-log4j12</artifactId>
	<version>1.7.7</version>
</dependency>
<dependency>
	<groupId>log4j</groupId>
	<artifactId>log4j</artifactId>
	<version>1.2.17</version>
</dependency>
```

### Way of Jar Package

* [slf4j](http://www.slf4j.org/) / log4j (Logger)
* [gson](https://code.google.com/p/google-gson/) (Google JSON Utils)
* [jiguang-common-client](https://github.com/jpush/jiguang-java-client-common)
* [jsms-client](https://github.com/jpush/jsms-api-java-client/releases/download/jsms-client-1.2.5/jsms-client-1.2.5.zip)

The slf4j and gson jar packages can be found in the [project libs/ directory](https://github.com/jpush/jsms-api-java-client/tree/master/libs) and can be copied to your project.
