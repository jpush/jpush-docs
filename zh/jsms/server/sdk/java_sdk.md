# jsms-api-java-client

### 概述
这是短信 Rest API 的 Java 版本封装开发包，是有极光推送官方提供的，一般支持最新的 API功能。

对应的 Rest API 文档：http://docs.jiguang.cn/server/rest_api_jsms/

## 安装

### maven 方式
将下边的依赖条件放到你项目的 maven pom.xml 文件里。
> 其中 slf4j 可以与 logback, log4j, commons-logging 等日志框架一起工作，可根据你的需要配置使用。

```Java
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jsms-client</artifactId>
    <version>1.2.1</version>
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
    <version>1.0.6</version>
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
* [slf4j](http://www.slf4j.org/) / log4j (Logger)
* [gson](https://code.google.com/p/google-gson/) (Google JSON Utils)
* [jiguang-common-client](https://github.com/jpush/jiguang-java-client-common)
* [jsms-client](https://github.com/jpush/jsms-api-java-client/releases/download/jsms-client-1.1.1/jsms-client-1.1.1.jar)

[项目 libs/ 目录](https://github.com/jpush/jsms-api-java-client/tree/master/libs)下可以找到 slf4j 及 gson jar 包 可复制到你的项目里去。
