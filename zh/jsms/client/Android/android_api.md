## SDK API 描述
+ SMSSDK 类：对外的类，该类为单例，调用该类的方法都需要获取该类的唯一实例，获得方法为 SMSSDK.getInstance()。

+ SmscodeListener：获取验证码的回调接口，在调用 SMSSDK 的 getSmsCode 时需要传入接口实例。

+ SmscheckListener：检查验证码的回调接口，在调用 SMSSDK 的 checkSmsCode 时需要传入接口实例。

### SMSSDK.initSdk(Context context)
#### 接口说明

该接口为初始化接口，主要是检测一些配置信息，如果配置错误将会初始化失败，将会打印错误日志。调用其它接口前必须先调用该接口，仅且仅需调用一次，建议在 Application 或初始 Activity 中调用。

#### 调用示例

	SMSSDK.getInstance().initSdk(this);

### SMSSDK.getSmsCode(String phone, String tempId, SmscodeListener listener)
#### 接口说明
获取验证码。

>该接口是在非 UI 线程回调，需要在 UI 线程回调可调用 SMSSDK.getSmsCodeAsyn()。

#### 参数说明
+ phone：手机号码
+ tempId：短信模板
+ listener：回调接口

#### 调用示例

	SMSSDK.getInstance().getSmsCodeAsyn("159xxxxxxxx", "1", new SmscodeListener() {
		@Override
		public void getCodeSuccess(final String uuid) {
			// 获取验证码成功，uuid 为此次获取的唯一标识码。
		}

		@Override
		public void getCodeFail(int errCode, final String errMsg) {
			// 获取验证码失败 errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
		}
	});

### SMSSDK.checkSmsCode(String phone, String code, SmscheckListener listener)
#### 接口说明
验证码验证接口。
>该接口是在非 UI 线程回调，需要在 UI 线程回调可调用 SMSSDK.checkSmsCodeAsyn()。

#### 参数说明
+ phone：手机号码
+ code：短信验证码
+ listener：回调接口

#### 调用示例

	SMSSDK.getInstance().checkSmsCodeAsyn("159xxxxxxxx", "123456", new SmscheckListener() {
		@Override
		public void checkCodeSuccess(final String code) {
			// 验证码验证成功，code 为验证码信息。
		}

		@Override
		public void checkCodeFail(int errCode, final String errMsg) {
			// 验证码验证失败, errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
		}
	});

### SMSSDK.getVoiceCode(String phone, SmscodeListener listener)
#### 接口说明
获取语音验证码。语音语言为中文。

>该接口是在非 UI 线程回调，需要在 UI 线程回调可调用 SMSSDK.getVoiceCodeAsyn()。

#### 参数说明
+ phone：手机号码
+ listener：回调接口

#### 调用示例

	SMSSDK.getInstance().getVoiceCodeAsyn("159xxxxxxxx", new SmscodeListener() {
		@Override
        public void getCodeSuccess(final String uuid) {
            //获取验证码成功，uuid 为此次获取的唯一标识码。
        }
        @Override
        public void getCodeFail(int errCode, final String errMsg) {
            //获取验证码失败，errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
        }
	});

### SMSSDK.getVoiceCode(String phone,int language,SmscodeListener listener)
#### 接口说明
获取语音验证码。该接口可指定语言。

>该接口是在非 UI 线程回调，需要在 UI 线程回调可调用 SMSSDK.getVoiceCodeAsyn()。

#### 参数说明
+ phone：手机号码
+ language：0为中文，1为英文，2为中英文，传入不支持的语言会报50040错误
+ listener：回调接口

#### 调用示例

	SMSSDK.getInstance().getVoiceCodeAsyn("159xxxxxxxx",2,new SmscodeListener() {
		@Override
        public void getCodeSuccess(final String uuid) {
            //获取验证码成功，uuid 为此次获取的唯一标识码。
        }
        @Override
        public void getCodeFail(int errCode, final String errMsg) {
            //获取验证码失败，errCode 为错误码，详情请见文档后面的错误码表；errMsg 为错误描述。
        }
	});

### SMSSDK.setIntervalTime(long intervalTime)
#### 接口说明
设置前后两次获取验证码的时间间隔，默认 30 秒。

#### 参数说明
+ intervalTime：时间间隔，单位是毫秒(ms)。

#### 调用示例

    SMSSDK.getInstance().setIntervalTime(60000);    // 设置间隔时间为 60 秒

### SMSSDK.getIntervalTime()
#### 接口说明
获取当前设置的时间间隔。
#### 返回值
+ long：单位为毫秒(ms)。

#### 调用示例

    SMSSDK.getInstance().getIntervalTime();

### SMSSDK.setDebugMode(boolean debugMode)
#### 接口说明
设置 debug 模式，设置 true 会输出 SDK 打印的日志。

#### 参数说明
+ debugMode：true 为 debug 模式，false 为非 debug 模式。

#### 调用示例

    SMSSDK.getInstance().setDebugMode(true);


## 错误码描述
| 错误码 | 错误码描述 | 备注 |
|--------|---------------------|--------------------------|
| 3001 | 请求超时 |  |
| 3002 | 无效的手机号码 |  |
| 4001 | body 为空 |  |
| 4002 | 无效的 AppKey |  |
| 4003 | 无效的来源 |  |
| 4004 | body 解密失败 |  |
| 4005 | aes key 解密失败 |  |
| 4006 | 时间戳转化失败 |  |
| 4007 | body 格式不正确 |  |
| 4008 | 无效时间戳 |  |
| 4009 | 没有短信验证权限 |  |
| 4011 | 发送超频 | 同一手机号每天获取验证码无限制，通知类相同内容10分钟3条，不同内容无限制，营销类10分钟3条。|
| 4013 | 模板不存在 |  |
| 4014 | extra 为空 |  |
| 4015 | 验证码不正确 |  |
| 4016 | 没有余额 |  |
| 4017 | 验证码超时 |  |
| 4018 | 重复验证 |  |
| 2993 | 验证码校验失败 | 短信已下发但获取 uuid 异常 |
| 2994 | 本地数据有误 |  |
| 2995 | 数据解析错误 |  |
| 2996 | 两次请求不超过 1 分钟 | 本地校验 |
| 2997 | 未获取验证码 |  |
| 2998 | 网络错误 | 没有网络等 |
| 2999 | 其它错误 |  |
| 50040 | 传入不支持的语言 | 0为中文，1为英文，2为中英文 |
