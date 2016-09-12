# Windows Phone SDK 集成指南
##使用提示

本文匹配的 SDK 版本 r1.0.0以后。

## 产品功能说明

极光推送  (JPush) 是一个端到端的推送服务，使得服务器的消息能够及时地推送到终端用户手机上，让开发者积极地保持与用户的连接，从而提高用户的活跃度、提高应用的留存率。极光推送客户端支持Android、iOS和Windows Phone三个平台。


本Windows Phone SDK方便开发者基于JPush来快捷的为Windows Phone SDK增加推送功能，减少集成WPNs所需要的工作量，开发的复杂度。

### 主要功能

+ 为JPush Server上报ChannelUri，免除开发者管理ChannelUri的麻烦

### 主要特点

+ 集成简单
+ Windows Phone SDK集成后，服务器向Windows Phone端推送消息更加简单

### 集成压缩包内容

+ JPushSDK-v1.0.0.dll：支持的Windows Phone的版本为8.0及以上
+ pdf文件：WinPhone SDK集成指南
+ example文件夹：开发示例

## SDK集成步骤
### 在JPush Portal上创建应用

+ [在JPush的管理Portal](https://www.jiguang.cn)上创建应用
+ 创建成功后自动生成AppKey用以标识该应用

### 导入API开发包到应用程序项目    

将SDK包解压，在vs2012工程目录中的“Reference”上单击右键，在弹出菜单的右下角选择"Browse",在资源管理器的文件夹中选中SDK目录下的JPushSDK-v1.0.0.dll。

### 配置WMAppManifest.xml

在工程目录下，单击Properties右侧三角块，在展开内容处双击WMAppManifest.xml

选择下图红色矩形内的两项

![](../image/WP.jpg)

### 添加代码

####调用接口

文件App.xaml.cs中监听系统事件，相应地调用 JPush SDK 提供的 API 来实现功能。

以下 ３ 个事件监听与调用 JPush SDK API 都是必须的。请直接复制如下代码块里，注释为 "Required" 的行，到你的应用程序代理类里相应的监听方法里。

请注意：由于微软商店的上架需求，请在第一次调用RegisterNotification函数前，弹出一个提示让用户确认是否推送,具体请参见example中的示例代码

	private void Application_Launching(object sender, LaunchingEventArgs e)
	{
		//Required
		//setup第一个参数替换成您在JPush Portal中的app_key
		//setup第二个参数替换成您定义的渠道名称
		//setup第二个参数是一个获取RegisrtationID的委托，不需要时可以填null
		JPushSDK.JServer.Setup("your app_key", "your channel",null);
		JPushSDK.JServer.RegisterNotification();
	}
	private void Application_Activated(object sender, ActivatedEventArgs e)
	{
		//Required
		JPushSDK.JServer.Activated();
	
	}
	private void Application_Deactivated(object sender, DeactivatedEventArgs e)
	{
		//Required
		JPushSDK.JServer.Deactivated();
	}
####添加统计代码

toast 通知点击提示

添加在您要启动的页面之下，如果在推送通知内没添加该选项，则需要加在MainPage页面内

	protected override void OnNavigatedTo(NavigationEventArgs e)
	{
		JPushSDK.JServer.HandleToastNotification(NavigationContext.QueryString);
		base.OnNavigatedFrom(e);
		
	}
添加统计页面

	protected override void OnNavigatedTo(NavigationEventArgs e)
	{
		JPushSDK.JServer.TrackPageInto("your page name");
		base.OnNavigatedFrom(e);
	}
	protected override void OnNavigatedFrom(NavigationEventArgs e)
	{
		JPushSDK.JServer.TrackPageOut("your page name");
		base.OnNavigatedTo(e);
	}
####打印日志

查看消息是否发送到 JPush服务器，以及集成过程中出错的原因

请注意：发布到商店前，一定关闭要JPush SDK调试模式。

	JPushSDK.JServer.IsDebug = true;
	
##高级功能
请参考：

[winphone API](winphone_api)

##技术支持

邮件联系：<support@jpush.cn>

问答社区：[http://community.jiguang.cn/](http://community.jiguang.cn/)

	