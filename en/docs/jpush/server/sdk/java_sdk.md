# JPush API Java Library

[Github Source Code](https://github.com/jpush/jpush-api-java-client)

## Overview

This is a Java version development package for the JPush REST API. It is provided by the JPush officially and generally supports the latest API features.

Corresponding REST API documentation: [REST API - Push](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/), [REST API - Report](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_report/).

This Development Kit Javadoc: [API Docs](http://jpush.github.io/jpush-api-java-client/apidocs/)

Version update: [Release Page](https://github.com/jpush/jpush-api-java-client/releases). Download updates here.

> Developers are very welcome to submit code and contribute a piece of power. Valid code reviewed will be incorporated into this project.

## Installation

### Maven Way

Place the following dependencies in your project's maven pom.xml file.

```xml
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jpush-client</artifactId>
    <version>3.3.4</version>
</dependency>
```

### Jar Package Mode

Please go to the [Release Page](https://github.com/jpush/jpush-api-java-client/releases) to download the corresponding release package

### Dependent Package

* [slf4j](http://www.slf4j.org/) / log4j (Logger)
* [gson](https://code.google.com/p/google-gson/) (Google JSON Utils)

> Among them, slf4j can work with log frames such as logback, log4j, and commons-logging, and can be configured and used according to your needs.

If you use Maven to build your project, you need to add it to your project pom.xml:

```xml
<dependency>
    <groupId>cn.jpush.api</groupId>
    <artifactId>jiguang-common</artifactId>
    <version>1.1.1</version>
</dependency>
<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.6.Final</version>
    <scope>compile</scope>
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

If you are not using Maven to build the project, the dependencies jar in the project libs/ directory can be copied to your project.

## Compile Source Code

> If the developer wants to do some extended development based on this project, or want to understand the source code of the project, this chapter can be a reference, otherwise please skip this chapter.

### Import this Item

* You can use git clone https://github.com/jpush/jpush-api-java-client.git jpush-api-src to download the source code
* If you don't use git, go to the Release Page to download the source package and unzip it
* Use eclipse to import and download the source code project. Maven is recommended to facilitate management of dependent packages
* If you use the method of importing an ordinary project, the project will report and error. Then please check the Build Path, Libraries
* Dependent jar packages can be found in the libs directory. Please add them to Build Path, Libraries if it is not added
* Log4j is used as the logging framework by default. Developers can replace logback, commons-logging, and other logging frameworks according to their needs.
* In rare cases, if the test directory reports an error, please manually add the test dependency jar package mockwebserver-2.0.0.jar, okhttp-2.0.0.jar, okio-1.0.0.jar
* Developers need to be careful to set the encoding format of this project to UTF-8

### Build this Project

You can use the Eclipse class IDE to export jar packages. It is recommended to use maven directly to execute the command:

```
mvn package
```

### Automated Test

Execute the command in the project directory:

```
mvn test
```

### Use Samples

If you use NettyHttpClient (new in version 3.2.15), you need to manually call the close method in NettyHttpClient after the response is returned. Otherwise, the process will not exit. Code example:

```java
...
try {
    PushResult result = jpushClient.sendPush(payload);
    LOG.info("Got result - " + result);
    Thread.sleep(5000);
    // 请求结束后，调用 NettyHttpClient 中的 close 方法，否则进程不会退出。
    jpushClient.close();
} catch(InterruptedException e) {
    e.printStackTrace();
}
```

After the 3.2.17 release, the user can freely switch between ApacheHttpClient, NettyHttpClient, or NativeHttpClient, if the setHttpClient(IHttpClient client) method was added to the PushClient.

### Push Sample

> The following fragment comes from the file in the project code: example / cn.jpush.api.examples.PushExample

```java
JPushClient jpushClient = new JPushClient(MASTER_SECRET, APP_KEY, null, ClientConfig.getInstance());

// For push, all you need do is to build PushPayload object.
PushPayload payload = buildPushObject_all_all_alert();

try {
    PushResult result = jpushClient.sendPush(payload);
    LOG.info("Got result - " + result);

} catch (APIConnectionException e) {
    // Connection error, should retry later
    LOG.error("Connection error, should retry later", e);

} catch (APIRequestException e) {
    // Should review the error, and fix the request
    LOG.error("Should review the error, and fix the request", e);
    LOG.info("HTTP Status: " + e.getStatus());
    LOG.info("Error Code: " + e.getErrorCode());
    LOG.info("Error Message: " + e.getErrorMessage());
}
```

The key to pushing is to build a PushPayload object. The following example shows the generic usage for building object.

* Build push objects quickly: In all platforms and all devices, Notifications with ALERT as its content

```java
public static PushPayload buildPushObject_all_all_alert() {
    return PushPayload.alertAll(ALERT);
}
```

* Build push objects: In all platforms, the push target with "alias1" as alias and ALERT as notification content.

```java
public static PushPayload buildPushObject_all_alias_alert() {
    return PushPayload.newBuilder()
            .setPlatform(Platform.all())
            .setAudience(Audience.alias("alias1"))
            .setNotification(Notification.alert(ALERT))
            .build();
}
```

* Build push objects: The platform is Android, the target is a device with "tag1" as tag, Android notification ALERT as content, and TITLE as title

```java
public static PushPayload buildPushObject_android_tag_alertWithTitle() {
    return PushPayload.newBuilder()
            .setPlatform(Platform.android())
            .setAudience(Audience.tag("tag1"))
            .setNotification(Notification.android(ALERT, TITLE, null))
            .build();
}
```

* Build push objects: the platform is iOS, the push target is the intersection of "tag1", "tag_all", and the push content includes both notifications and messages – ALERT as  notification information, 5 as the number of corner signs, "happy" as the notification sound,  from = "JPush" as additional Field; the message content is MSG_CONTENT. The notification is in the APNs push channel, and the message is in the JPush application message channel. APNs push environment is "production" (Library defaults to development if not explicitly set)

```java
public static PushPayload buildPushObject_ios_tagAnd_alertWithExtrasAndMessage() {
    return PushPayload.newBuilder()
        .setPlatform(Platform.ios())
        .setAudience(Audience.tag_and("tag1", "tag_all"))
        .setNotification(Notification.newBuilder()
            .addPlatformNotification(IosNotification.newBuilder()
                .setAlert(ALERT)
                .setBadge(5)
                .setSound("happy")
                .addExtra("from", "JPush")
                .build())
            .build())
        .setMessage(Message.content(MSG_CONTENT))
        .setOptions(Options.newBuilder()
             .setApnsProduction(true)
             .build())
         .build();
}
```

* Build push objects: The platform is Andorid and iOS, the push target is intersection of (the union of "tag1" and "tag2") (the union of "alias1" and "alias2"), and the push content is - the message with MSG_CONTENT as content and from = JPush as additional fields.

```java
public static PushPayload buildPushObject_ios_audienceMore_messageWithExtras() {
    return PushPayload.newBuilder()
        .setPlatform(Platform.android_ios())
        .setAudience(Audience.newBuilder()
            .addAudienceTarget(AudienceTarget.tag("tag1", "tag2"))
            .addAudienceTarget(AudienceTarget.alias("alias1", "alias2"))
            .build())
        .setMessage(Message.newBuilder()
            .setMsgContent(MSG_CONTENT)
            .addExtra("from", "JPush")
            .build())
        .build();
}
```

* Build push objects: Push content contains SMS information

```java
public static void testSendWithSMS() {
    JPushClient jpushClient = new JPushClient(masterSecret, appKey);
    try {
        SMS sms = SMS.content("Test SMS", 10);
        PushResult result = jpushClient.sendAndroidMessageWithAlias("Test SMS", "test sms", sms, "alias1");
        LOG.info("Got result - " + result);
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Code: " + e.getErrorCode());
        LOG.info("Error Message: " + e.getErrorMessage());
    }
}
```

### Statistics Acquisition Sample

> The following fragment comes from the file in the project code: example / cn.jpush.api.examples.ReportsExample

```java
JPushClient jpushClient = new JPushClient(masterSecret, appKey);
try {
    ReceivedsResult result = jpushClient.getReportReceiveds("1942377665");
    LOG.debug("Got result - " + result);

} catch (APIConnectionException e) {
    // Connection error, should retry later
    LOG.error("Connection error, should retry later", e);

} catch (APIRequestException e) {
    // Should review the error, and fix the request
    LOG.error("Should review the error, and fix the request", e);
    LOG.info("HTTP Status: " + e.getStatus());
    LOG.info("Error Code: " + e.getErrorCode());
    LOG.info("Error Message: " + e.getErrorMessage());
}
```

### Tag/Alias Sample

> The following fragment comes from the file in the project code: example /cn.jpush.api.examples.DeviceExample

* Get Tag Alias

```java
    try {
        TagAliasResult result = jpushClient.getDeviceTagAlias(REGISTRATION_ID1);

        LOG.info(result.alias);
        LOG.info(result.tags.toString());
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Code: " + e.getErrorCode());
        LOG.info("Error Message: " + e.getErrorMessage());
    }
```

* Bind Phone Number

```java
    try {
        DefaultResult result =  jpushClient.bindMobile(REGISTRATION_ID1, "13000000000");
        LOG.info("Got result " + result);
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Code: " + e.getErrorCode());
        LOG.info("Error Message: " + e.getErrorMessage());
    }
```

### Schedule Sample

> The following fragment comes from the file in the project code: example / cn.jpush.api.examples.ScheduleExample

```java
    JPushClient jpushClient = new JPushClient(masterSecret, appKey);
    String name = "test_schedule_example";
    String time = "2016-07-30 12:30:25";
    PushPayload push = PushPayload.alertAll("test schedule example.");
    try {
        ScheduleResult result = jpushClient.createSingleSchedule(name, time, push);
        LOG.info("schedule result is " + result);
    } catch (APIConnectionException e) {
        LOG.error("Connection error. Should retry later. ", e);
    } catch (APIRequestException e) {
        LOG.error("Error response from JPush server. Should review and fix it. ", e);
        LOG.info("HTTP Status: " + e.getStatus());
        LOG.info("Error Code: " + e.getErrorCode());
        LOG.info("Error Message: " + e.getErrorMessage());
    }
```

### Sample of Custom Client

> The fragment comes from the file in the project code: example /cn.jpush.api.examples.ClientExample

* The configured SSLVersion indicates that at least the supported protocol version is specified, and other multiple protocol versions may also be supported. The list of supported protocol versions depends on the JRE and the operating environment.

```java
    public static void testCustomClient() {
        ClientConfig config = ClientConfig.getInstance();
        config.setMaxRetryTimes(5);
        config.setConnectionTimeout(10 * 1000); // 10 seconds
        config.setSSLVersion("TLSv1.1");        // JPush server supports SSLv3, TLSv1, TLSv1.1, TLSv1.2

        JPushClient jPushClient = new JPushClient(masterSecret, appKey, null, config);
    }

    public static void testCustomPushClient() {
        ClientConfig config = ClientConfig.getInstance();
        config.setApnsProduction(false);    // development env
        config.setTimeToLive(60 * 60 * 24); // one day

    //  config.setGlobalPushSetting(false, 60 * 60 * 24); // development env, one day

        JPushClient jPushClient = new JPushClient(masterSecret, appKey, null, config);  // JPush client

    //  PushClient pushClient = new PushClient(masterSecret, appKey, null, config);     // push client only

    }
```

### Weblogic Uses the Java SDK

Some things that needs to pay attention to when using jpush-api-java-client by Weblogic.

#### Precautions

This document is based on weblogic 10.3.6 version. For version 12, please configure the path accordingly.

In rare cases, the certificate will have a version upgrade, so be sure to verify that the fingerprints of current and the official certificate are the same.

**Settings of Weblogic console**

* [HostName Authentication] Set to None, otherwise, weblogic.security.SSL.HostnameVerifier is used for host name verification, and hostname authentication will fail.
    * Configuration path Weblogic Console> Server Settings> SSL> Advanced> Host Name Verification
* Select [Use JSSE SSL], because Weblogic's default encryption algorithm is different from the encryption algorithm in Java standard
    * Configuration path Weblogic Console> Server Settings> SSL> Advanced> Using JSSE SSL

**Certificate Configuration**

* Check the location of the Trust Key Store used by Weblogic
    * The default file used is the jre\lib\security\cacerts file in the JRE directory
    * Some developers may change to a custom Trust Key Store
* Check if the corresponding truststore contains the root certificate of Geo Trust or secondary certificate of Geo Trust SSL
    * Example: keytool -list -keystore cacerts
    * This process requires the password of the truststore (default changeit)
    * If any of these two certificates is contained, calling the JPush interface can be invoked through
* If the truststore does not contain the above certificate, you need to import the public key to the corresponding truststore
    * Open jpush.cn and export the public key (can be either Geo Trust root certificate, Geo Trust SSL or *.jpush.cn, please search in Baidu for specific exporting method)
    * Import the exported public key certificate to the corresponding trust store in step 1
    * Example: keytool -import -alias geotrustssl -keystore cacerts -file GeoTrustSSL.cer
    * This process requires the password of the truststore (default changeit)

**Comparison of Certificates**

* Execute the keytool -list -keystore mykey.jks command to list all the public keys in the truststore and observe the fingerprint of the corresponding certificate.
* Check the official website certificate and observe the fingerprint of the corresponding certificate
*  Compare whether two fingerprints are the same, as shown in the figure below
