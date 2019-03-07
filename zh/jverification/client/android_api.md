#Android SDK API

##SDK接口说明

* JVerificationInterface，包含SDK所有接口

##SDK初始化

+ ***JVerificationInterface.init(Context context)***
	+ 接口说明：
		+ 初始化接口。建议在Application的onCreate中调用
	+ 参数说明：
		+ context：android的上下文
	+ 调用示例：

~~~
	JVerificationInterface.init(this);
~~~

##SDK设置debug模式

+ ***JVerificationInterface.setDebugMode(boolean enable)***
	+ 接口说明：
		+ 设置是否开启debug模式。true则会打印更多的日志信息。建议在init接口之前调用。
	+ 参数说明：
		+ enable：debug开关
	+ 调用示例：

~~~
	JVerificationInterface.setDebugMode(true);
~~~

##SDK判断网络环境是否支持

+ ***JVerificationInterface.checkVerifyEnable(Context context)***
	+ 接口说明：
		+ 判断当前的手机网络环境是否可以使用认证。
	+ 参数说明：
		+ context：android的上下文
	+ 返回说明：
       + 返回true代表可以使用；返回false建议使用其他验证方式。
	+ 调用示例：

~~~
	boolean verifyEnable = JVerificationInterface.checkVerifyEnable(this);
        if(!verifyEnable){
            Log.d(TAG,"当前网络环境不支持认证");
            return;
        }
~~~

##SDK获取token

+ ***JVerificationInterface.getToken(Context context, VerifyListener listener)***
	+ 接口说明：
		+ 获取当前在线的sim卡所在运营商及token。如果获取成功代表可以用来验证手机号。获取失败则建议做短信验证
	+ 参数说明：
		+ context：android的上下文
		+ listener：接口回调
	+ 回调说明：
    ***onResult(int code, String  content, String operator)***
  		+ code: 返回码，2000代表获取成功，其他为失败，详见错误码描述
    	+ content：成功时为token，可用于调用验证手机号接口。token有效期为1分钟，超过时效需要重新获取才能使用。失败时为失败信息
    	+ operator：成功时为对应运营商，CM代表中国移动，CU代表中国联通，CT代表中国电信。失败时可能为null
  	+ 调用示例：

~~~
	JVerificationInterface.getToken(this, new VerifyListner{
	    @Override
        public void onResult(int code, String content, String operator) {
	        if (code == 2000){
	            Log.d(TAG, "token=" + content + ", operator=" + operator);
            } else {
            	Log.d(TAG, "code=" + code + ", message=" + content);
            }
	    });
~~~
***说明***：开发者可以通过SDK获取token接口的回调信息来选择验证方式，若成功获取到token则可以继续使用极光认证进行号码验证；若获取token失败，需要换用短信验证码等方式继续完成验证。

##SDK发起认证

+ ***JVerificationInterface.verifyNumber(Context context, String token, String phone, VerifyListener listener)***
	+ 接口说明：
    	+ 验证手机号是否是当前在线的sim卡的手机号
  	+ 参数说明：
    	+ context：android的上下文
		+ token：选填，getToken接口返回的token。如果传空，将自动调用getToken方法再执行手机号验证
		+ phone：必填，需要验证的手机号。如果传空会报4001参数错误
		+ listener：接口回调
  	+ 回调说明：
  	***onResult(int code, String  content, String operator)***
		+ code: 返回码，1000代表验证一致，1001代表验证不一致，其他为失败，详见错误码描述
		+ content：返回码的解释信息
		+ operator：成功时为对应运营商，CM代表中国移动，CU代表中国联通，CT代表中国电信。失败时可能为null
  	+ 调用示例：

~~~
	JVerificationInterface.verifyNumber(this, null, "13512341234", new VerifyListner{
	    @Override
        public void onResult(int code, String content, String operator) {
	        if (code == 1000){
	            Log.d(TAG, "verify consistent, operator=" + operator);
            } else if (code == 1001) {
            	Log.d(TAG, "verify not consistent");
            } else {
                Log.d(TAG, "code=" + code + ", message=" + content);
            }
	    });
~~~

***说明***：开发者调用该接口，需要在管理控制台找到该应用，并在［认证设置］-［其他设置］中开启［SDK发起认证］。

##错误码

|code|message|备注|
|:-----:|:----:|:-----:|
|1000|verify consistent|手机号验证一致|
|1001|verify not consistent|手机号验证不一致|
|1002|unknown result|未知结果|
|1003|token expired|token失效|
|1004|sdk verify has been closed|SDK发起认证未开启|
|1005|包名和 AppKey 不匹配|请检查客户端配置的包名与官网对应 Appkey 应用下配置的包名是否一致|
|1006|frequency of verifying single number is beyond the maximum limit|同一号码自然日内认证消耗超过限制|
|1007|beyond daily frequency limit|appKey自然日认证消耗超过限制|
|1008|AppKey 非法|请到官网检查此应用信息中的 appkey，确认无误|
|1009||请到官网检查此应用的应用详情；更新应用中集成的极光SDK至最新|
|1010|verify interval is less than the minimum limit|同一号码连续两次提交认证间隔过短|
|1011|appSign invalid|应用签名错误，检查签名与Portal设置的是否一致|
|2000|内容为token|获取token成功|
|2001|fetch token failed|获取token失败|
|2002|init failed|SDK初始化失败|
|2003|network not reachable|网络连接不通|
|2004|get uid failed|极光服务注册失败|
|2005|request timeout|请求超时|
|2006|fetch config failed|获取应用配置失败|
|2007|内容为异常信息|验证遇到代码异常|
|2008|Token requesting, please try again later|正在获取token中，稍后再试|
|2009|verifying, please try again later|正在认证中，稍后再试 |
|2010|don't have READ_PHONE_STATE permission|未开启读取手机状态权限|
|2011|内容为异常信息|获取配置时代码异常|
|2012|内容为异常信息|获取token时代码异常|
|2013|内容为具体错误原因|网络发生异常|
|2014|internal error while requesting token|请求token时发生内部错误|
|2016|network type not supported|当前网络环境不支持认证|
|4001|parameter invalid|参数错误。请检查参数，比如是否手机号格式不对|
|4018||没有足够的余额|
|4031||不是认证SDK用户|
|4032||获取不到用户配置|
|5000|bad server|服务器未知错误|
|-994|网络连接超时|   |
|-996|网络连接断开|   |
|-997|注册失败/登录失败|（一般是由于没有网络造成的）如果确保设备网络正常，还是一直遇到此问题，则还有另外一个原因：JPush 服务器端拒绝注册。而这个的原因一般是：你当前 App 的 Android 包名以及 AppKey，与你在 Portal 上注册的应用的 Android 包名与 AppKey 不相同。|
