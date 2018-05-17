# JMessage API Java Library

[Github Source Code ](https://github.com/jpush/jmessage-api-java-client)

## Overview

This is a development package in Java version for the JMessage REST API, which is provided by the JPush officially and generally supports the latest API features.

Corresponding REST API documentation：<https://docs.jiguang.cn/jmessage/server/rest_api_im/>

This Development Kit Javadoc: [API Docs](http://jpush.github.io/jmessage-api-java-client/apidocs/)

Version update: [Releases](https://github.com/jpush/jmessage-api-java-client/releases). Please download updates here.

> Developers are very welcome to submit code and contribute a piece of power. Valid code reviewed will be incorporated into this project.

## Installation

### Maven way

Place the following dependencies in maven pom.xml file of your project.

> Among them, slf4j can work with logging frameworks such as logback, log4j, and commons-logging, and can be configured and used according to your needs.

```Java
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jmessage-client</artifactId>
    <version>1.1.7</version>
</dependency>
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jiguang-common</artifactId>
    <version>1.1.0</version>
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

### Jar package method

Please go to the [Releases](https://github.com/jpush/jmessage-api-java-client/releases) to download the corresponding release package.

### Dependent package
* [slf4j](http://www.slf4j.org/) / log4j (Logger)
* [gson](https://code.google.com/p/google-gson/) (Google JSON Utils)
* [jiguang-common](https://github.com/jpush/jiguang-java-client-common)

> Among them, slf4j can work with logging frameworks such as logback, log4j, and commons-logging, and can be configured and used according to your needs.

> [Click](https://github.com/jpush/jmessage-api-java-client/releases) to download jar package of jiguang-common.

## Compile Source Code

> If the developer wants to do some extended development based on this project, or want to understand the source code of the project, he can refer to this chapter, otherwise skip this chapter.

### Import this item

* You can use `git clone https://github.com/jpush/jmessage-api-java-client.git jmessage-api-src` to download the source code
* If you don't use git, go to the [Releases](https://github.com/jpush/jmessage-api-java-client/releases) to download the source code package and unzip it
* Use eclipse to import the downloaded source code project. Maven is recommended for easy management of dependent packages.
* If you use the method of importing an ordinary project, the project may report an error. Please check the Build Path and Libraries then,
* Dependent jar packages can be found in the libs directory. Please add the ones not in there yet to Build Path and Libraries
* Jpush-client jar package can [click to download](https://github.com/jpush/jpush-api-java-client/releases)
* Log4j is used as the logging framework by default. Developers can replace logback, commons-logging, and other logging frameworks according to their needs.
* In rare cases, if the test directory reports an error, please manually add the dependency jar package of test：mockwebserver-2.0.0.jar, okhttp-2.0.0.jar, okio-1.0.0.jar
* Developers need to be careful to set the encoding format of this project to UTF-8

### Build this project

You can use the Eclipse class IDE to export jar packages. It is recommended to use maven directly to execute the command

```
maven package
```

### Automated testing

Execute the command in the project directory:

```
mvn test
```

## Samples

> The following fragment comes from the file in the project code: example/cn.jmessage.api.examples.UserExample

```java
public static void testGetUserInfo() {
    JMessageClient client = new JMessageClient(appkey, masterSecret);
    try {
        String res = client.getUserInfo("test_user");
        LOG.info(res);
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Message: " + e.getMessage());
    }
}
```

> The following fragment comes from the file in the project code: example/cn.jmessage.api.examples.GroupExample

```java
public static void testCreateGroup() {
    JMessageClient client = new JMessageClient(appkey, masterSecret);
    try {
        String res = client.createGroup("test_user", "test_gname1", "description", "test_user");
        LOG.info(res);
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Message: " + e.getMessage());
    }
}
```

## Contributor List

* [@tangyikai](https://github.com/tangyikai)
