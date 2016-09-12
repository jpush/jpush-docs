# Android SDK 调试指南

## SDK启动过程

+ 检查AndroidManifest.xml中是否有配置AppKey，如果没有，则启动失败
+ 检查 Androidmanifest.xml文件配置的正确性，必须要保证“Android SDK 集成指南”中所有标注“
+ Required”的部分都正确配置，否则启动失败
+ 检查 JPush SDK库文件的有效性，如果库文件无效，则启动失败
+ 检查网络是否可用，如果网络可用则连接服务器登录，否则启动失败
+ 登陆成功后可以从log中看到如下log

![](../image/jpush.jpg)

## 测试确认

+ 确认 Androidmanifest.xml 中所需的所有 “Required” 项都已经添加。如果有 "Required" 项未添加，日志会提示错误。
+ 确认 AppKey (在Portal上生成的) 已经正确的写入 Androidmanifest.xml 中,没写会有日志提示错误。
+ 确认在程序启动时候调用了init(context) 接口
+ 确认测试手机（或者模拟器）的网络可用，如果网络正常可用，客户端调用 init 后不久，应有登录成功（Login succeed）的日志信息，如 SDK 启动过程所示
+ 启动应用程序，登陆 Portal 系统，并向应用程序发送自定义消息或者通知栏提示。在几秒内，客户端应可收到下发的通知或者正定义消息.



## 别名与标签设置异常处理

由于网络连接不稳定的原因，有一定的概率 JPush SDK 设置别名与标签会失败。
App 开发者合理地处理设置失败，则偶尔失败对应用的正常使用 JPush 影响是有限的。

以下以 Android SDK 作为示例。

基本思路：

+ 设置成功时，往 SharePreference 里写状态，以后不必再设置
+ 遇到 6002 超时，则稍延迟重试。


		// 这是来自 JPush Example 的设置别名的 Activity 里的代码。一般 App 的设置的调用入口，在任何方便的地方调用都可以。
		private void setAlias() {
		    EditText aliasEdit = (EditText) findViewById(R.id.et_alias);
		    String alias = aliasEdit.getText().toString().trim();
		    if (TextUtils.isEmpty(alias)) {
		        Toast.makeText(PushSetActivity.this,R.string.error_alias_empty, Toast.LENGTH_SHORT).show();
		        return;
		    }
		    if (!ExampleUtil.isValidTagAndAlias(alias)) {
		        Toast.makeText(PushSetActivity.this,R.string.error_tag_gs_empty, Toast.LENGTH_SHORT).show();
		        return;
		    }

		    // 调用 Handler 来异步设置别名
		    mHandler.sendMessage(mHandler.obtainMessage(MSG_SET_ALIAS, alias));
		}

		private final TagAliasCallback mAliasCallback = new TagAliasCallback() {
		    @Override
		    public void gotResult(int code, String alias, Set<String> tags) {
		        String logs ;
		        switch (code) {
		        case 0:
		            logs = "Set tag and alias success";
		            Log.i(TAG, logs);
		            // 建议这里往 SharePreference 里写一个成功设置的状态。成功设置一次后，以后不必再次设置了。
		            break;
		        case 6002:
		            logs = "Failed to set alias and tags due to timeout. Try again after 60s.";
		            Log.i(TAG, logs);
		            // 延迟 60 秒来调用 Handler 设置别名
		            mHandler.sendMessageDelayed(mHandler.obtainMessage(MSG_SET_ALIAS, alias), 1000 * 60);
		            break;
		        default:
		            logs = "Failed with errorCode = " + code;
		            Log.e(TAG, logs);
		        }
		        ExampleUtil.showToast(logs, getApplicationContext());
		    }
		};
		private static final int MSG_SET_ALIAS = 1001;
		private final Handler mHandler = new Handler() {
		@Override
		    public void handleMessage(android.os.Message msg) {
		        super.handleMessage(msg);
		        switch (msg.what) {
		        	case MSG_SET_ALIAS:
		        		Log.d(TAG, "Set alias in handler.");
		                // 调用 JPush 接口来设置别名。
		            	JPushInterface.setAliasAndTags(getApplicationContext(),
		            							        (String) msg.obj,
		            							         null,
		            							         mAliasCallback);
		            break;
		        default:
		            Log.i(TAG, "Unhandled msg - " + msg.what);
		        }
		    }		        				        
		};


## Android SDK 网络问题解析

Android 客户端网络不稳定，会导致App 有时候无法及时收到 Push 消息。
很多开发者认为这是因为 JPush 推送不稳定、延迟，甚至有时候认为 JPush 后台推送系统出问题了。
本文目的是从各个方面来分析 Android 网络导致的 JPush 不能正常工作的问题。

## JPush 正常工作的必要条件

首先，我们需要知道，JPush SDK  并不是集成到App 后就必然一直工作的。

其正常工作的必要条件是：JPush SDK 与 JPush Server 的网络保持着连接。请参考这篇文章来做进一步的理解：[极光推送技术原理：移动无线网络长连接。](http://blog.jiguang.cn/jpush_wireless_push_principle/)

而 Android 设备的网络的复杂性、不稳定性，是 Android 设备开发最复杂的地方之一。

另外，每款手机的网络能力也是千差万别的。国内很多杂牌手机在网络方面甚至会有严重的问题。大品牌厂商的手机则要好很多。

只要 JPush 的网络连接是正常的，则：

+ JPush 收到消息一定是及时的。其延迟是秒级的，一般在 1 秒之内。如果超过 10 秒，则一定是客  户端网络出了问题。
+ 手机休眠时，也能够及时地收到推送消息。

## 部分系统的特殊处理导致问题

### MIUI V5 系统

+ 自启动管理：默认情况下，手机开机后，只有系统默认的服务可以启动起来。除非在自启动管理界面，设置允许第三方程序自启动。
+ 网络助手：可以手动禁止已安装的第三方程序访问2G/3G和WIFI的网络和设置以后新安装程序是否允许访问2G/3G和WIFI的网络。


### 4.0以上的android系统

+ 在设置－>应用，强行停止 应用程序后该程序无法再自启动，就算重新开机也一样，一定要手动开启才能运行起来。

### 让我们从目前得到的反馈来整理调试的思路

**手机休眠时收不到 JPush 消息，解锁或屏幕灯亮则可以成功接收**

这个现象表明，手机休眠时，JPush SDK “被迫”与服务器端的网络失去了连接。

JPush SDK 的工作原理是要确保在手机休眠时也能正常的工作，即休眠时也可以及时地收到Push消息。实际上JPush在大部分上手机上都能达到此效果。

这个“被迫”，是由 Android 设备的环境所导致的。涉及的原因有如下几个方面：

+ 手机本身的网络设置。标准版本的 Android ROM 是没有这个设置的，但某些特殊的 ROM 可能会有这方面的设置。
+ 手机上的安全、省电工具软件额外做的事情

上述的特殊机制会关闭网络。网络一旦连接上，JPush也会连接上服务器，从而Push消息就会收到。

**有时候收到 JPush 消息很及时，有时候则要等几分钟**

JPush 会监听网络切换广播。当网络关闭时，把原来JPush连接关闭。当有新的网络时，创建JPush连接。

另外，RTC会定时发送心跳。如果之前的网络已经断了，则会重新连接。

应该说，当前的网络连接策略还是相对简单的，这样做的目的是：省电、省流量。

不 好之处就是：网络没有切换时，因为当时网络过差，JPush连接会被中断。这种情况下，就只能等 RTC 心跳去触发连接。这也是有时候JPush 无法及时接收Push消息的原因。根据网络条件的不同，出现这个情况的概率也会不同。但据我们自己的测试，90% 的时候是可以及时地收到Push消息的。

JPush 目前在网络策略方面没有像微信这种聊天工具做得积极。如果这样做到，电量和流量的消耗必然会成倍地增加。

**完全收不到 JPush 消息**

如果集成之后就完全收不到Push消息，则很有可能是某个地方配置错误。请根据文档仔细检查：Android SDK 集成指南，iOS SDK 集成指南，或者根据参考教程：Android SDK 调试指南，iOS SDK 调试指南。

