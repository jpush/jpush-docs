# Android API

## 停止与恢复推送服务 API
### 支持的版本

开始的版本：v1.3.3

### 功能说明

JPush SDK 提供的推送服务是默认开启的。

开发者App可以通过调用停止推送服务API来停止极光推送服务。当又需要使用极光推送服务时，则必须要调用恢复推送服务 API。

> 本功能是一个完全本地的状态操作。也就是说：停止推送服务的状态不会保存到服务器上。如果停止推送服务后，开发者App被重新安装，或者被清除数据，JPush SDK 会恢复正常的默认行为。（因为保存在本地的状态数据被清除掉了）。
> 
> 本功能其行为类似于网络中断的效果，即：推送服务停止期间推送的消息，恢复推送服务后，如果推送的消息还在保留的时长范围内，则客户端是会收到离线消息。

### API - stopPush

停止推送服务。

调用了本 API 后，JPush 推送服务完全被停止。具体表现为：

+ JPush Service 不在后台运行
+ 收不到推送消息
+ 不能通过 JPushInterface.init 恢复，需要调用resumePush恢复。
+ 极光推送所有的其他 API 调用都无效

#### 接口定义

	public static void stopPush(Context context);
	
#### 参数说明

+ context 应用的 ApplicationContext

### API - resumePush

恢复推送服务。

调用了此 API 后，极光推送完全恢复正常工作。

#### 接口定义

	public static void resumePush(Context context);
	
#### 参数说明

	context 应用的 ApplicationContext

### API - isPushStopped

用来检查 Push Service 是否已经被停止

+ SDK 1.5.2 以上版本支持。

#### 接口定义

	public static boolean isPushStopped(Context context);

####参数说明

+ context 应用的 ApplicationContext

###代码示例
	
以下代码来自于 [JPush Android Example。]()

	public class MainActivity extends InstrumentedActivity implements OnClickListener {
	    private Button mStopPush;
	    private Button mResumePush;
	     
	    @Override
	    public void onCreate(Bundle savedInstanceState) {
	        super.onCreate(savedInstanceState);
	        setContentView(R.layout.main);
	        initView();
	    }
	     
	    // 初始化按钮
	    private void initView() {       
	        mStopPush = (Button)findViewById(R.id.stopPush);
	        mStopPush.setOnClickListener(this);
	         
	        mResumePush = (Button)findViewById(R.id.resumePush);
	        mResumePush.setOnClickListener(this);
	    }
	 
	    @Override
	    public void onClick(View v) {
	        switch (v.getId()) {
	 
	        // 点击停止按钮后，极光推送服务会被停止掉
	        case R.id.stopPush:
	            JPushInterface.stopPush(getApplicationContext());
	            break;
	 
	        // 点击恢复按钮后，极光推送服务会恢复正常工作
	        case R.id.resumePush:
	            JPushInterface.resumePush(getApplicationContext());
	            break;
	        }
	    }
	}
