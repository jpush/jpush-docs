#SMS JSMS Android SDK集成指南
##SDK 说明
### 主要功能
### 主要特点
### 支持版本
+ 目前SDK只支持Android 2.3或以上版本的手机系统。

### SDK 压缩包内包括

+ AndroidManifest.xml
	+ 客户端嵌入SDK参考的配置文件
+ libs/jpush-sdk-sms-v1.x.x.jar
	+ SDK Java 开发包
+ example
  + 是一个完整的 Android 项目，通过这个演示了 SMS SDK 的基本用法，可以用来做参考。

## 集成步骤

### 创建应用
注册成为JPush开发者。在极光的web portal 上创建应用得到APPkey，如果您已经是是极光其他产品的用户并且创建过应用，那么无需重复创建。
  
### 导入 SDK 开发包到你自己的应用程序项目
解压压缩包，将libs/jpush-sdk-sms-v1.x.x.jar复制到工程的libs下面

### 集成 JPush Android SDK 的混淆

```
-keep class cn.jpush.sms.SMSSDK {*;}
-keep class cn.jpush.sms.listener.** {*;}
-keep class cn.jpush.sms.utils.DeviceInfo {*;}

#========================gson & protobuf================================
-dontwarn com.google.**
-keep class com.google.gson.jpush.annotations.Until {*;}

#Gson specific classes
-keep class sun.misc.Unsafe { *; }
-keep public abstract class com.google.gson.jpush.internal.UnsafeAllocator { *; }

```

### 配置 AndroidManifest.xml
+ 配置权限：

`
<uses-permission android:name="android.permission.INTERNET" />
`

+ 配置appkey：

`
<meta-data android:name="JPUSH_APPKEY" android:value="Your AppKey"/>
`
### 添加代码
参考 Demo 和 SDK API 说明进行添加集成


## SDK API 描述
+ SMSSDK类:对外的类，该类为单例，调用该类的方法都需要获取该类的唯一实例，获得方法为SMSSDK.getInstance()。

+ SmscodeListener:获取验证码的回调接口，在调用SMSSDK的getSmsCode时需要传入接口实例。

+ SmscheckListener:检查验证码的回调接口，在调用SMSSDK的checkSmsCode时需要传入接口实例。

#### SMSSDK.init(Context context)
**接口说明**

该接口为初始化接口，主要是检测一些配置信息，如果配置错误将会初始化失败，将会打印错误日志。调用其它接口前必须先调用该接口。仅且仅需调用一次。建议在application或初始activity中调用。

**调用示例：**

```
SMSSDK.getInstance().init(this);

```
#### SMSSDK.getSmsCode(String phone,String temp_id,SmscodeListener listener)

**接口说明：获取验证码**

注：该接口是在非ui线程回调。需要在ui线程回调可调用SMSSDK.getSmsCodeAsyn()接口

**参数说明：**

+ phone：手机号码
+ temp_id:短信模板
+ listener:回调接口

**调用示例：**

```
SMSSDK.getInstance().getSmsCodeAsyn("159xxxxxxxx","1",new SmscodeListener(){
@verride
public void getCodeSuccess(final String uuid){
//获取验证码成功，uuid为此次获取的唯一标识码
}
@verride
public void getCodeFail(int errCode,final String errmsg){
//获取验证码失败 errCode为错误码，详情请见文档后面的错误码表，errmsg为错误描述
}
});
```

#### SMSSDK.checkSmsCode(String phone,String code,SmscheckListener listener)
**接口说明：验证码验证接口。**

注：该接口是在非ui线程回调。需要在ui线程回调可调用SMSSDK.checkSmsCodeAsyn()接口

**参数说明：**

+ phone：手机号码
+ code:短信验证码
+ listener:回调接口

**调用示例：**

```
SMSSDK.getInstance().checkSmsCodeAsyn("159xxxxxxxx","123456",new SmscheckListener(){
@verride
public void checkCodeSuccess(final String code){
//验证码验证成功，code为验证码信息
}
@verride
public void checkCodeFail(int errCode,final String errmsg){
//验证码验证失败 errCode为错误码，详情请见文档后面的错误码表，errmsg为错误描述
}
});
```


## 错误码描述
| 错误码 | 错误码描述 | 备注 |
|--------|---------------------|--------------------------|
| 3001 | 请求超时 |  |
| 3002 | 无效的手机号码 |  |
| 4001 | body为空 |  |
| 4002 | 无效的appkey |  |
| 4003 | 无效的来源 |  |
| 4004 | body解密失败 |  |
| 4005 | aes key解密失败 |  |
| 4006 | 时间戳转化失败 |  |
| 4007 | body格式不正确 |  |
| 4008 | 无效时间戳 |  |
| 4009 | 没有短信验证权限 |  |
| 4010 | 重复发送 |  |
| 4011 | 发送超频 |  |
| 4013 | 模板不存在 |  |
| 4014 | extra为空 |  |
| 4015 | 验证码不正确 |  |
| 4016 | 没有余额 |  |
| 4017 | 验证码超时 |  |
| 2993 | 验证码校验失败 | 短信已下发但获取uuid异常 |
| 2994 | 本地数据有误 |  |
| 2995 | 数据解析错误 |  |
| 2996 | 两次请求不超过1分钟 | 本地校验 |
| 2997 | 未获取验证码 |  |
| 2998 | 网络错误 | 没有网络等 |
| 2999 | 其它错误 |  |
