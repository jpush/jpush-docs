#Android API
##JShareInterface类
####public static void init(Context context)
接口说明：初始化接口，建议在项目的Appliction的OnCreate中使用。  
参数说明：Context 应用的 ApplicationContext
####public static List<Platform> getPlatformList()
接口说明：获取SDK所有能用的平台，如要使用某个平台，必须在JGShareSDK.xml中配置并把该平台的Enable设置为true。  
返回说明：以List形式返回所有能用的平台。
#### public static Platform getPlatform(String name)
接口说明：获取SDK特定平台，如该平台不能用，会返回null。  
参数说明：name 平台名称，值可选SinaWeibo、QQ、QZone、Wechat、WechatMoments。  
返回说明：平台的实例。
##Platform类
####public boolean isEnable()
接口说明：判断该平台是否能够使用，在JGShareSDK.xml中配置该参数。  
####public boolean isClientValid()
接口说明：判断该平台的客户端是否有效，通常用来判断平台客户端是否已经正常安装。
####public void setPlatActionListener(PlatActionListener shareActionListener)
接口说明：设置分享、授权、获取用户信息的回调接口。  
参数说明：shareActionListener 回调接口。
####public String getName()
接口说明：获取该平台的名称。  
返回说明：该平台的名称，如SinaWeibo、QQ、QZone、Wechat、WechatMoments。 
####public void share(ShareParams params)
接口说明：该平台的分享接口。  
参数说明：params 分享的配置参数，具体设置请参考各个平台的分享参数说明。
####public void authorize()
接口说明：获取授权接口
####public void showUser(String account)
接口说明：获取该平台下用户的个人信息。  
参数说明：account 授权后获得的open_id，可通过platform.getDb().getUserId()接口获取。
#各个平台的分享参数说明
##微信(微信朋友圈)
###1）分享文本
![](http://i.imgur.com/umELNk3.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_TEXT);
	shareParams.setTitle("Title");
	shareParams.setText("Text");
###2）分享图片
![](http://i.imgur.com/N1FapXf.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_IMAGE);
	shareParams.setImagePath(file.getAbsolutePath());
	//shareParams.setImageUrl(share_imageurl);
	//shareParams.setImageData(bitmap);
###3）分享音乐
![](http://i.imgur.com/0qnaef7.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setShareType(Platform.SHARE_MUSIC);
	shareParams.setUrl(url);
	shareParams.setMusicUrl(music_url);
	shareParams.setImagePath(file.getAbsolutePath());
###4）分享视频
![](http://i.imgur.com/f8NND1b.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setTitleUrl(share_videourl);
	shareParams.setShareType(Platform.SHARE_VIDEO);
	shareParams.setUrl(share_videourl);
	shareParams.setImagePath(file.getAbsolutePath());
###5）分享网页
![](http://i.imgur.com/SwTVnHX.png)   

	ShareParams shareParams = new ShareParams();
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setShareType(Platform.SHARE_WEBPAGE);
	shareParams.setUrl(share_url);
	shareParams.setImagePath(file.getAbsolutePath());
###6）分享Emoji表情（朋友圈不支持）
![](http://i.imgur.com/xReBnP3.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_EMOJI);
	shareParams.setImagePath(file.getAbsolutePath());
###7）分享文件（朋友圈不支持）
![](http://i.imgur.com/i20eA9u.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_FILE);
	shareParams.setFilePath(file.getAbsolutePath());
##QQ
###1）分享图文
![](http://i.imgur.com/N72wBwX.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_WEBPAGE);
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setTitleUrl(share_url);
	shareParams.setImagePath(file.getAbsolutePath());
###2）分享音乐
![](http://i.imgur.com/9F13B46.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_MUSIC);
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setTitleUrl(share_url);
	shareParams.setMusicUrl(music_url);
	shareParams.setImagePath(file.getAbsolutePath());
	//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
###3）分享图片
![](http://i.imgur.com/SBv3zCB.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_IMAGE);
	shareParams.setImagePath(file.getAbsolutePath());
##QQ空间
###1)分享图文
![](http://i.imgur.com/6ivwAbV.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_TEXT);
	shareParams.setTitleUrl(share_url);
	shareParams.setTitle(share_title);
	shareParams.setText(share_text);
	shareParams.setImagePath(file.getAbsolutePath());
	// shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
###2)发布说说
![](http://i.imgur.com/wy3pKBM.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_TEXT);
	shareParams.setText(share_text);
	shareParams.setImagePath(file.getAbsolutePath());
	//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
##新浪微博
###1)分享文本
![](http://i.imgur.com/dRFXekI.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_TEXT);
	shareParams.setText(share_text);
###2)分享图文
![](http://i.imgur.com/PCK8sci.png)  

	ShareParams shareParams = new ShareParams();
	shareParams.setShareType(Platform.SHARE_TEXT);
	shareParams.setText(share_text);
	shareParams.setImagePath(file.getAbsolutePath());
	//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
> 注意：
如果新浪微博需要跳转链接的，请在Text中拼接url，如：  
shareParams.setText(share_text + share_url); //share_text 为分享内容，share_url为链接