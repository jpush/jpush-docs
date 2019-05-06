#最近更新

##JVerification iOS SDK v2.1.4

**更新时间**

* 2019-05-06

**Change Log**

* 修改中国电信授权页面文案

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + account_login_sdk_noui_core.framework
        + account_verify_sdk_core.framework
        + EAccountApiSDK.framework
        + jcore-ios-x.x.x.a
        + jverification-ios-2.1.4.a
        + TYRZSDK.framework
    + 项目targets->build phases->link binary with libraries
        + 增加libc++.1.tbd
    + 在极光演示demo中，找到JVerificationResource.bundle，将这个bundle文件加到您的项目中 

##JVerification iOS SDK v2.1.3

**更新时间**

* 2019-04-26

**Change Log**

* 升级中国移动SDK
* 新增授权页面支持横屏模式
* 新增授权页面支持自定义背景
* 修改授权页面隐私条款文案

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + account_login_sdk_noui_core.framework
        + account_verify_sdk_core.framework
        + EAccountApiSDK.framework
        + jcore-ios-x.x.x.a
        + jverification-ios-2.1.3.a
        + TYRZSDK.framework
    + 项目targets->build phases->link binary with libraries
        + 增加libc++.1.tbd
    + 在极光演示demo中，找到JVerificationResource.bundle，将这个bundle文件加到您的项目中 


##JVerification Android SDK v2.1.1

**更新时间**

* 2019-04-26

**Change Log**

* 升级中国移动SDK
* 新增授权页面支持横屏模式
* 新增授权页面支持自定义背景
* 修改授权页面隐私条款文案
* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v2.1.1.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件
    + 用对应CPU文件夹下的 libCtaApiLib.so文件，添加到项目中

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新和JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名和 appKey

+ 拷贝SDK所必须的资源文件
    + 压缩包根目录下有res文件夹，将该文件夹下的所有文件复制到项目res下面对应的文件夹中

##JVerification iOS SDK v2.1.1

**更新时间**

* 2019-04-02

**Change Log**

* 修复一键登录授权页面设置LOGO图片Y偏移不生效的问题
* 一键登录电信、联通协议修改为应用内打开

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + account_login_sdk_noui_core.framework
        + account_verify_sdk_core.framework
        + EAccountApiSDK.framework
        + jcore-ios-x.x.x.a
        + jverification-ios-2.1.1.a
        + TYRZSDK.framework
    + 项目targets->build phases->link binary with libraries
        + 增加libc++.1.tbd
    + 在极光演示demo中，找到JVerificationResource.bundle，将这个bundle文件加到您的项目中 

##JVerification iOS SDK v2.1.0

**更新时间**

* 2019-03-28

**Change Log**

* 新增一键登录功能，并支持自定义授权页

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + account_login_sdk_noui_core.framework
        + account_verify_sdk_core.framework
        + EAccountApiSDK.framework
        + jcore-ios-x.x.x.a
        + jverification-ios-2.1.0.a
        + TYRZSDK.framework
    + 项目targets->build phases->link binary with libraries
        + 增加libc++.1.tbd
    + 在极光演示demo中，找到JVerificationResource.bundle，将这个bundle文件加到您的项目中 

##JVerification Android SDK v2.1.0

**更新时间**

* 2019-03-28

**Change Log**

* 新增一键登录功能，并支持自定义授权页

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v2.1.0.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件
    + 用对应CPU文件夹下的 libCtaApiLib.so文件，添加到项目中

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新和JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名和 appKey

+ 拷贝SDK所必须的资源文件
    + 压缩包根目录下有res文件夹，将该文件夹下的所有文件复制到项目res下面对应的文件夹中

##JVerification iOS SDK v1.1.3

**更新时间**

* 2019-03-21

**Change Log**

* 修复不支持模拟器运行的问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + jcore-ios-x.x.x.a
        + jverification-ios-x.x.x.a
        + account_verify_sdk_core.framework
        + TYRZNoUISDK.framework
        + JVERIFICATIONService.h

##JVerification Android SDK v1.1.3

**更新时间**

* 2019-02-27

**Change Log**

* 新增判断网络环境是否支持认证的接口

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v1.x.x.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新和JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名和 appKey

##JVerification iOS SDK v1.1.2

**更新时间**

* 2019-02-27

**Change Log**

* 新增判断网络环境是否支持认证的接口
* 修复已知问题


**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 替换项目中原有的极光SDK文件
        + jcore-ios-x.x.x.a
        + jverification-ios-x.x.x.a
        + account_verify_sdk_core.framework
        + TYRZNoUISDK.framework
        + JVERIFICATIONService.h

##JVerification iOS SDK v1.1.1

**更新时间**

* 2019-01-17

**Change Log**

* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-ios-v1.x.x.a 替换项目中原有的极光认证sdk的文件

##JVerification Android SDK v1.1.2

**更新时间**

* 2019-01-10

**Change Log**

* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v1.x.x.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新和JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名和 appKey

##JVerification Android SDK v1.1.1

**更新时间**

* 2018-12-17

**Change Log**

* 中国电信协议变更

**升级建议**

* 必须升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v1.x.x.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新和JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名和 appKey

##JVerification iOS SDK v1.1.0

**更新时间**

* 2018-11-13

**Change Log**

* 优化电信SIM卡认证方式，SDK体积更小
* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-ios-v1.x.x.a 替换项目中原有的极光认证sdk的文件

##JVerification Android SDK v1.1.0

**更新时间**

* 2018-11-13

**Change Log**

* 优化电信SIM卡认证方式，SDK体积更小
* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v1.x.x.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新跟JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名 和 appkey

##JVerification iOS SDK v1.0.1

**更新时间**

* 2018-10-31

**Change Log**

* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-ios-v1.x.x.a 替换项目中原有的极光认证sdk的文件

##JVerification Android SDK v1.0.1

**更新时间**

* 2018-10-24

**Change Log**

* 增加运营商优先选择策略，提升通信效率
* 修复已知问题

**升级建议**

* 建议升级

**升级指南**

+ 首先解压您获取到的zip压缩包

+ 更新库文件
    + 打开libs文件夹
    + 用jverification-android-v1.x.x.jar 替换项目中原有的极光认证sdk的jar文件
    + 用jcore-android-v1.x.x.jar 替换项目中原有的极光jcore的jar文件
    + 用对应CPU文件夹下的 libjcore1xy.so文件，替换项目中原有的极光so文件

+ 更新AndroidManifest.xml
    + 压缩包根目录下有示例 AndroidManifest 文件，请对照示例更新跟JVerification相关的组件属性，permission 等配置，并在中文提示的位置替换你的包名 和 appkey

##JVerification Android SDK v1.0.0

**更新时间**

* 2018-09-29

**Change Log**

* 极光认证上线，支持三大运营商

##JVerification iOS SDK v1.0.0

**更新时间**

* 2018-09-29

**Change Log**

* 极光认证上线，支持三大运营商
