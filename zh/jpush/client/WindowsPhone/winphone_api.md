#Windows Phone API
### API概述

APIs 主要都集中在名空间JPushSDK的类JServer中

#### Property-IsDebug
开启调试模式，帮助了解集成的情况，打印相关log，发布商店时，`请关闭调试模式，否则会导致无法通过微软应用商店的审核`

#### 支持版本
开始支持v1.0.0

	public static  bool  IsDebug{get;set;}
##### 参数说明
+ IsDebug=true  开启调试模式
+ IsDebug=false 关闭调试模式

#### Method - Setup

调用此API将APP_KEY上报给JPush后台

##### 支持的版本
开始支持v1.0.0

##### 接口定义
	public  static void  Setup(string APP_KEY, string CHANNEL,Action<string> action)
	
##### 参数说明
+ APP_KEY
	+ JPush Portal上注册应用后生成的 appkey
+ CHANNEL
	+ 作为应用程序的发布去发，可自行定义
+ action
	+ 成功获取RegistrationID后调用该回调函数                 
	void registationIDCallback(string registrationID)
	{
	  Debug.WriteLine(registrationID);
	} 

#### Method -Activated

应用程序进入Activated状态的调用，以正确的处理Tomstoning状态

##### 支持版本
开始支持v1.0.0

##### 接口定义
	public  static void Activated()
#### Method-Deactiveted

应用程序进入Deactivated状态调用，用来正确的保存应用程序的退出状态

##### 支持版本
开始支持v1.0.0

##### 接口定义

	public  static void Deactivated()
	
### JPush SDK的状态和MPNs的通知

注册JPush SDK中的事件，用来监听JPush SDK的运行情况和接收MPNs发送的信息

#### 支持版本
开始支持v1.0.0
#### 接口定义
	
	public static void AddNotification(string name, Action<Dictionary<string, string>> selector)

#### 参数说明
+ name
	+ 监听的消息类型，JPush SDK提供以下5种类型
	+ NotificationCenter.kNetworkDidSetupNotification                  建立连接
	+ NotificationCenter.kNetworkDidRegisterNotification              登陆成功
	+ NotificationCenter.kNetworkDidLoginNotification                  注册成功
	+ NotificationCenter.kNetworkDidCloseNotification                  关闭连接
	+ NotificationCenter.kNetworkDidMPNsMessageNotification    收到MPNs消息
+ selector
	+ 当有事件发生时触发该回调函数
	+ Dictionary在kNetworkDidSetupNotification时会带一个RegistrationID
	+ Dictionary在kNetworkDidSetupNotification时会带一个MPNs的消息
	
	
####示例代码
	void callBack(Dictionary<string, string> dict)
	{
	   Debug.WriteLine(dict.ToString());
	} 
	或者使用lamda表达式
	JPushSDK.NotificationCenter.AddNotification(JPushSDK.NotificationCenter.kNetworkDidCloseNotification, (K) =>
	{
	      Deployment.Current.Dispatcher.BeginInvoke(() =>
	      {
	         //TextConnectionState.Text = "关闭连接";
	      });
	}); 

### 开启、查询和停止MPNs推送功能

与Windows Phone推送相关的API说明

#### Method - RegisterNotification
注册MPNs服务的接口。当自行定制弹出用户允许推送的窗口，`请使用这个接口。用户关闭了MPNs通知后，如果再次开启通知请调用此函数。不能调用RegisterNotificationWithMessagebox`

##### 支持的版本

开始支持v1.0.0

##### 接口定义

public  static void RegisterNotification()

#### Method - RegisterNotificationWithMessagebox

 注册MPNs的接口，帮助管理首次注册弹出messagebox，并保存用户选择状态

##### 支持的版本
开始支持v1.0.0

##### 接口定义

	public  static void RegisterNotificationWithMessagebox(string content, string title, Action<bool> callBack)
	 
##### 参数说明
+ content
	+ 弹出框的内容
+ title
	+ 弹出框的标题
+ callBack
	+回调函数通知用户选择结果
#### Method-CloseNotification

关闭MPNs推送

##### 支持的版本
开始支持的版本v1.0.0

##### 接口定义
	public  static void CloseNotification()
	
#### Method-IsOpneNotification

检查MPNs是否开启


##### 支持版本
开始支持版本v1.0.0

##### 接口定义
	public  static bool IsOpneNotification()

### 标签与别名 API 

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
 <p>温馨提示，设置标签别名请注意处理call back结果。
 <p>只有call back 返回值为 0 才设置成功，才可以向目标推送。否则服务器 API 会返回1011错误。
</div>

提供相关 API 用来设置别名（alias）与标签（tags）。

API 可以在 App 里任何地方调用。

#### 别名 alias
为安装了应用程序的用户，取个别名来标识。以后给该用户 Push 消息时，就可以用此别名来指定。

每个用户只能指定一个别名。

同一个应用程序内，对不同的用户，建议取不同的别名。这样，尽可能根据别名来唯一确定用户。

系统不限定一个别名只能指定一个用户。如果一个别名被指定到了多个用户，当给指定这个别名发消息时，服务器端API会同时给这多个用户发送消息。

举例：在一个用户要登录的游戏中，可能设置别名为 userid。游戏运营时，发现该用户 3 天没有玩游戏了，则根据 userid 调用服务器端API发通知到客户端提醒用户。

#### 标签 tag
为安装了应用程序的用户，打上标签。其目的主要是方便开发者根据标签，来批量下发 Push 消息。

可为每个用户打多个标签。

举例： game, old_page,  women

#### Method - SetTagsWithAlias(with Callback)

调用此 API 来同时设置别名与标签，支持回掉函数。

需要理解的是，这个接口是覆盖逻辑，而不是增量逻辑。即新的调用会覆盖之前的设置。

在之前调用过后，如果需要再次改变别名与标签，只需要重新调用此 API 即可。

##### 支持的版本
开始支持的版本：1.0.0

##### 接口定义
	public static void  SetTagsWithAlias(HashSet<string> tags, string alias, Action<int, HashSet<string>, string> callback)
	
##### 参数说明
+ tags
	+ null 此次调用不设置此值。
	+ 空集合表示取消之前的设置。
	+ 每次调用至少设置一个 tag，覆盖之前的设置，不是新增。
	+ 有效的标签组成：字母（区分大小写）、数字、下划线、汉字。
	+ 限制：每个 tag 命名长度限制为 40 字节，最多支持设置 100 个 tag，但总长度不得超过1K字节。（判断长度需采用UTF-8编码）
	+ 单个设备最多支持设置 100 个 tag。App 全局 tag 数量无限制。
+ alias
	+ null此次调用不设置此值。
	+ 空字符串 （""）表示取消之前的设置。
	+ 每次调用设置有效的别名，覆盖之前的设置。
	+ 有效的别名组成：字母（区分大小写）、数字、下划线、汉字。
	+ 限制：alias 命名长度限制为 40 字节。（判断长度需采用UTF-8编码）
+ callbackSelector
	+ NULL 此次调用不需要 Callback。
	+ 用于回掉返回对应的参数 alias, tags。并返回对应的状态码：0为成功，其他返回码请参考错误码定义。
	
			private void TagsAliasCallBack(int resultCode, HashSet<string> tags, string alias);	


#### Method - FilterValidTags

用于过滤出正确可用的 tags。

如果总数量超出最大限制则返回最大数量的靠前的可用tags。

<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
 <p>使用建议:
 	<br>
<p>设置 tags 时，如果其中一个 tag 无效，则整个设置过程失败。
<br>
<p>如果 App 的 tags 会在运行过程中动态设置，并且存在对 JPush SDK tag 规定的无效字符，则有可能一个 tag 无效导致这次调用里所有的 tags 更新失败。
 <br>
 <p>这时你可以调用本方法 FilterValidTags 来过滤掉无效的 tags，得到有效的 tags，再调用 JPush SDK 的 set tags / alias 方法。
</div>

##### 支持的版本
开始支持的版本：1.0.0

##### 接口定义

	public static HashSet<string> FilterValidTags(HashSet<string> tags)

##### 参数说明
+ tags
	+ 原 tag 集合。
	
##### 接口返回

有效的 tag 集合。

#### 错误码定义

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >描述</th>
      <th >详细解释</th>
    </tr>
    <tr >
      <td>6001</td>
      <td>无效的设置，tag/alias 不应参数都为 null</td>
      <td></td>
    </tr>
    <tr >
      <td>6002</td>
      <td>设置超时</td>
      <td>建议重试</td>
    </tr>
    <tr >
      <td>6003</td>
      <td>alias 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字。</td>
    </tr>
    <tr >
      <td>6004</td>
      <td>alias超长。最多 40个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6005</td>
      <td>某一个 tag 字符串不合法</td>
      <td>有效的别名、标签组成：字母（区分大小写）、数字、下划线、汉字。</td>
    </tr>
    <tr >
      <td>6006</td>
      <td>某一个 tag 超长。一个 tag 最多 40个字节</td>
      <td>中文 UTF-8 是 3 个字节</td>
    </tr>
    <tr >
      <td>6007</td>
      <td>tags 数量超出限制。最多 100个</td>
      <td>这是一台设备的限制。一个应用全局的标签数量无限制。</td>
    </tr>
    <tr >
      <td>6008</td>
      <td>tag 超出总长度限制</td>
      <td>总长度最多 1K 字节</td>
    </tr>
    <tr >
      <td>6011</td>
      <td>10s内设置tag或alias大于10次</td>
      <td>短时间内操作过于频繁</td>
    </tr>
  </table>
</div>

### 统计功能

用于统计Toast点击，页面切换等事件

#### Method-HandleToastNotification

用于统计点击Toast通知进入应用程序的事件，需要放入到与Toast通知对应的页面和默认的页面，比如MainPage.xaml页面

##### 支持版本
开始支持v1.0.0

##### 接口定义
	public static void HandleToastNotification(IDictionary<string, string> remotoInfo)
##### 参数说明
+ remoteInfo
	+ 页面切换时，由wp 8 sdk的接口：NavigationContext.QueryString获取
#### Method-TrackPageInto

用于统计用户进入页面的事件，在需要统计页面的OnNavigatedTo中加入这个函数

##### 支持版本
开始支持版本v1.0.0

##### 接口定义
	public static void TrackPageInto(string pageName)

##### 参数说明
+ pageName
	+ 页面名称

#### Method-TrackPageOut

用于统计用户离开页面的事件，在需要统计的页面的OnNavigatedFrom中加入这个函数

##### 支持版本
开始支持版本v1.0.0

##### 接口定义
```
public static void TrackPageOut(string pageName)
```

#####参数说明

+ pageName
	+ 页面名称
	
		
### 获取RegistrationID
这个API中在名空间JPushSDK的类JServer中

####  Method-GetRegisrtationID
获取RegistrationID,没有登录成功之前返回空的字符串，登录成功后返回 RegistrationID

##### 支持版本
开始支持V1.0.0

#####  接口定义
	public static string   GetRegisrtationID()

### 客户端错误码定义

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >描述</th>
    </tr>
    <tr >
      <td>1008</td>
      <td>AppKey非法</td>
    </tr>
    <tr >
      <td>1009</td>
      <td>当前的appkey下没有创建WinPhone应用。请到官网检查此应用的应用详情</td>
    </tr>
  </table>
</div>


