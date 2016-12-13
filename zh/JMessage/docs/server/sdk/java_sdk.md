[![Build Status](https://travis-ci.org/jpush/jmessage-api-java-client.svg?branch=master)](https://travis-ci.org/jpush/jmessage-api-java-client)
[![Dependency Status](https://www.versioneye.com/user/projects/53eff13a13bb06f0bb000518/badge.svg?style=flat)](https://www.versioneye.com/user/projects/53eff13a13bb06f0bb000518)
[![GitHub version](https://badge.fury.io/gh/jpush%2Fjmessage-api-java-client.svg)](https://badge.fury.io/gh/jpush%2Fjmessage-api-java-client) 

# JMessage API Java Library

## 概述

这是 JMessage REST API 的 Java 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。

对应的 REST API 文档：<http://docs.jpush.io/server/rest_api_im/>

本开发包 Javadoc：[API Docs](http://jpush.github.io/jmessage-api-java-client/apidocs/)

版本更新：[Release页面](https://github.com/jpush/jmessage-api-java-client/releases)。下载更新请到这里。

> 非常欢迎各位开发者提交代码，贡献一份力量，review过有效的代码将会合入本项目。


## 安装

### maven 方式
将下边的依赖条件放到你项目的 maven pom.xml 文件里。
> 其中 slf4j 可以与 logback, log4j, commons-logging 等日志框架一起工作，可根据你的需要配置使用。

```Java
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jmessage-client</artifactId>
    <version>1.0.0</version>
</dependency>
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jiguang-common</artifactId>
    <version>0.1.6</version>
    <exclusions>
    	<exclusion>
	    <groupId>org.slf4j</groupId>
	    <artifactId>slf4j-jdk14</artifactId>
	</exclusion>
	<exclusion>
	    <groupId>org.slf4j</groupId>
	    <artifactId>slf4j-nop</artifactId>
	</exclusion>
    </exclusions>
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
### jar 包方式

请到 [Release页面](https://github.com/jpush/jmessage-api-java-client/releases)下载相应版本的发布包。

### 依赖包
* [slf4j](http://www.slf4j.org/) / log4j (Logger)
* [gson](https://code.google.com/p/google-gson/) (Google JSON Utils)
* [jiguang-common](https://github.com/jpush/jiguang-java-client-common)

> 其中 slf4j 可以与 logback, log4j, commons-logging 等日志框架一起工作，可根据你的需要配置使用。

> jiguang-common 的 jar 包下载。[请点击](https://github.com/jpush/jmessage-api-java-client/releases)

## 编译源码

> 如果开发者想基于本项目做一些扩展的开发，或者想了解本项目源码，可以参考此章，否则可略过此章。

### 导入本项目

* 可以采用 `git clone https://github.com/jpush/jmessage-api-java-client.git jmessage-api-src` 命令下载源码
* 如果不使用git，请到[Release页面](https://github.com/jpush/jmessage-api-java-client/releases)下载源码包并解压
* 采用eclipse导入下载的源码工程，推荐采用maven的方式，方便依赖包的管理
* 假如采用导入普通项目的方式，项目报错，检查Build Path，Libraries
 * 依赖jar包都在libs目录下可以找到，没有加入的请添加到Build Path，Libraries
 * jpush-client jar包可以[点击下载](https://github.com/jpush/jpush-api-java-client/releases)
 * 默认采用了log4j做日志框架，开发者可根据自己需求替换logback、commons-logging等日志框架
 * 极个别情况下，如果test目录报错，请手动添加test的依赖jar包mockwebserver-2.0.0.jar、okhttp-2.0.0.jar、okio-1.0.0.jar
* 开发者需要注意，将本项目的编码格式设置为UTF-8

### 构建本项目

可以用 Eclipse 类 IDE 导出 jar 包。建议直接使用 maven，执行命令：

	maven package

### 自动化测试

在项目目录下执行命令：

	mvn test

## 使用样例

> 以下片断来自项目代码里的文件：example / cn.jmessage.api.examples.UserExample

```Java
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

> 以下片断来自项目代码里的文件：example / cn.jmessage.api.examples.GroupExample
```Java
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

## 贡献者列表

* [@tangyikai](https://github.com/tangyikai)
