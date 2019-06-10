# Android JShare API
## SDK 初始化 API
### API - init
初始化接口，建议在项目的 Application 的 OnCreate 中使用。  
* SDK 1.5.0 之前的版本支持
#### 接口定义
```
public static void init(Context context)
```
#### 参数说明
* context 应用的 ApplicationContext

### API - init
初始化接口，建议在项目的 Application 的 OnCreate 中使用，这个初始化API支持代码中设置第三方平台信息。  
* SDK 1.5.0 及以后版本支持
#### 接口定义
```
public static void init(Context context, PlatformConfig platformConfig)
```
#### 参数说明
* context 应用的 ApplicationContext
* platformConfig 第三方平台信息配置，详情见第三方平台信息设置API

## 第三方平台信息设置 API
JShare 提供PlatformConfig类，实例化后可选择设置相应的第三方平台信息。
### API - setWechat
设置微信平台信息。  
#### 接口定义
```
public PlatformConfig setWechat(String appId, String appSecret)
```
#### 参数说明
* appId 微信平台appId
* appSecret 微信平台appSecret

### API - setQQ
设置QQ平台信息。  
#### 接口定义
```
public PlatformConfig setQQ(String appId, String appKey)
```
#### 参数说明
* appId QQ平台appId
* appKey QQ平台appKey

### API - setSinaWeibo
设置新浪微博平台信息。  
#### 接口定义
```
public PlatformConfig setSinaWeibo(String appKey, String appSecret, String redirectUrl)
```
#### 参数说明
* appKey 新浪微博平台appKey
* appSecret 新浪微博平台appSecret
* redirectUrl 新浪微博平台的回调url

### API - setFacebook
设置Facebook平台信息。  
#### 接口定义
```
public PlatformConfig setFacebook(String appId, String appName)
```
#### 参数说明
* appId Facebook平台appId
* appName Facebook平台appName

### API - setTwitter
设置Twitter平台信息。  
#### 接口定义
```
public PlatformConfig setTwitter(String consumerKey, String consumerSecret)
```
#### 参数说明
* consumerKey Twitter平台consumerKey
* consumerSecret Twitter平台consumerSecret

### API - setJchatPro
设置 JChatpro 平台信息。  
#### 接口定义
```
public PlatformConfig setJchatPro(String auth)
```
#### 参数说明
* auth JchatPro平台auth


## 获取已经正确配置的平台 API
### API - getPlatformList
获取 SDK 所有能用的平台名称，如要使用某个平台，必须正确配置相应的jar以及第三方平台信息。  
#### 接口定义
```
public static List<String> getPlatformList()
```

## 设置调试模式 API
### API - setDebugMode
设置调试模式。  
注：该接口需在 init 接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的 Application 中 onCreate 中调用。
#### 接口定义
```
public static void setDebugMode(boolean enable)
```
#### 参数说明
* enable 为 true 则会打印 debug 级别的日志，false 则只会打印 warning 级别以上的日志



## 判断某平台分享是否有效 API
### API - isClientValid
判断该平台的分享是否有效。
#### 接口定义
```
public static boolean isClientValid(String name)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name、JChatPro.Name。  

## 分享 API
### API - share
分享接口
#### 接口定义
```
public static void share(String name, ShareParams shareParams, PlatActionListener shareActionListener))
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name、JChatPro.Name。  
* shareParams 分享的配置参数，具体设置请参考各个平台的分享参数说明。
* shareActionListener 回调接口，可为 null，为 null 时则没有回调

## 判断某平台是否支持授权 API
### API - isSupportAuthorize 
判断某平台是否支持授权
* SDK 1.2.0 以上版本支持
#### 接口定义
```
public static boolean isSupportAuthorize(String name)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name。  

## 授权 API
### API - authorize
授权接口
* SDK 1.2.0 以上版本支持
#### 接口定义
```
public static void authorize(String name, AuthListener authListener)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、SinaWeibo.Name、QQ.Name、Facebook.Name、Twitter.Name、JChatPro.Name。  
* authListener 回调接口，可为 null，为 null 时则没有回调。
#### 代码示例
```
JShareInterface.authorize(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int action, BaseResponseInfo data) {
        Logger.dd(TAG, "onComplete:" + platform + ",action:" + action + ",data:" + data);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_AUTHORIZING:
                if (data instanceof AccessTokenInfo) {        //授权信息
                    String token = ((AccessTokenInfo) data).getToken();//token
                    long expiration = ((AccessTokenInfo) data).getExpiresIn();//token有效时间，时间戳
                    String refresh_token = ((AccessTokenInfo) data).getRefeshToken();//refresh_token
                    String openid = ((AccessTokenInfo) data).getOpenid();//openid
                    //授权原始数据，开发者可自行处理
                    String originData = data.getOriginData();
                    toastMsg = "授权成功:" + data.toString();
                    Logger.dd(TAG, "openid:" + openid + ",token:" + token + ",expiration:" + expiration + ",refresh_token:" + refresh_token);
                    Logger.dd(TAG, "originData:" + originData);
                }
                break;
        }
    }

    @Override
    public void onError(Platform platform, int action, int errorCode, Throwable error) {
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_AUTHORIZING:
                toastMsg = "授权失败";
                break;
        }
    }

    @Override
    public void onCancel(Platform platform, int action) {
        Logger.dd(TAG, "onCancel:" + platform + ",action:" + action);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_AUTHORIZING:
                toastMsg = "取消授权";
                break;
        }
    }
});
```

## 判断是否已经授权 API
### API - isAuthorize
判断是否已经授权接口
* SDK 1.2.0以上版本支持
#### 接口定义
```
public static boolean isAuthorize(String name)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name。

## 删除授权 API
### API - removeAuthorize
删除授权接口
* SDK 1.2.0 以上版本支持
#### 接口定义
```
public static void removeAuthorize(String name, AuthListener actionListener)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name。
* authListener 回调接口，可为 null，为 null 时则没有回调
#### 代码示例
```
JShareInterface.removeAuthorize(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int action, BaseResponseInfo data) {
       Logger.dd(TAG, "onComplete:" + platform + ",action:" + action + ",data:" + data);
       String toastMsg = null;
       switch (action) {
           case Platform.ACTION_REMOVE_AUTHORIZING:
               toastMsg = "删除授权成功";
               break;
       } 
    }

    @Override
    public void onError(Platform platform, int action, int errorCode, Throwable error) {
        Logger.dd(TAG, "onError:" + platform + ",action:" + action + ",error:" + error);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_REMOVE_AUTHORIZING:
                toastMsg = "删除授权失败";
                break;
        }
    }

    @Override
    public void onCancel(Platform platform, int i) {
    
    }
});
```

## 获取个人信息 API
### API - getUserInfo
获取个人信息接口
* SDK 1.2.0 以上版本支持
#### 接口定义
```
public static void getUserInfo(String platName, AuthListener authListener)
```
#### 参数说明
* name 平台名称，值可选 Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name。
* authListener 回调接口，可为 null，为 null 时则没有回调
#### 代码示例
```
JShareInterface.getUserInfo(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int action, BaseResponseInfo data) {
        Logger.dd(TAG, "onComplete:" + platform + ",action:" + action + ",data:" + data);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_USER_INFO:
                if (data instanceof UserInfo) {      //第三方个人信息
                    String openid = ((UserInfo) data).getOpenid();  //openid
                    String name = ((UserInfo) data).getName();  //昵称
                    String imageUrl = ((UserInfo) data).getImageUrl();  //头像url
                    int gender = ((UserInfo) data).getGender();//性别, 1表示男性；2表示女性
                    //个人信息原始数据，开发者可自行处理
                    String originData = data.getOriginData();
                    toastMsg = "获取个人信息成功:" + data.toString();
                    Logger.dd(TAG, "openid:" + openid + ",name:" + name + ",gender:" + gender + ",imageUrl:" + imageUrl);
                    Logger.dd(TAG, "originData:" + originData);
                }
                break;
        }
    }

    @Override
    public void onError(Platform platform, int action, int errorCode, Throwable error) {
        Logger.dd(TAG, "onError:" + platform + ",action:" + action + ",error:" + error);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_USER_INFO:
                toastMsg = "获取个人信息失败";
                break;
        }
    }

    @Override
    public void onCancel(Platform platform, int action) {
        Logger.dd(TAG, "onCancel:" + platform + ",action:" + action);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_USER_INFO:
                toastMsg = "取消获取个人信息";
                break;
        }
    }
});
```

# 各个平台的分享参数说明
## 微信(包括微信朋友圈、微信收藏)
### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
Text | 是 | String|分享标题|不超过 10KB

```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText("Text");//必须
```
### 2）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片路径|长度不能超过 10KB,大小不能超过 10M，ImagePath 与 ImageData 必须二选一
ImageData| 否 | Bitmap|图片 Bitmap|大小不能超过1 0M，ImagePath 与 ImageData 必须二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageData(bitmap);
```
### 3）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_MUSIC
Title| 否 | String|音乐标题|长度不能超过 512
Text| 否 | String|音乐描述|长度不能超过 1K
MusicUrl| 是 | String|音乐资源 Url|点击播放按钮可直接播放 url,长度不能超过 10K
Url| 否 | String|跳转 Url|点击跳转页面 url,长度不能超过 10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过 10KB,大小不能超过 32K,与 ImageData 二选一
ImageData| 否 | Bitmap|缩略图，图片 Bitmap|大小不能超过 32K,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_MUSIC);
shareParams.setUrl(url);
shareParams.setMusicUrl(music_url);
shareParams.setImagePath(file.getAbsolutePath());
```
### 4）分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_VIDEO
Title| 否 | String|视频标题|长度不能超过 512
Text| 否 | String|视频描述|长度不能超过 1K，朋友圈不显示该字段内容
Url| 是 | String|视频Url|长度不能超过 10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过 10KB,大小不能超过 32K,与 ImageData 二选一
ImageData| 否 | Bitmap|缩略图，图片 Bitmap|大小不能超过 32K,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setUrl(share_videourl);
shareParams.setImagePath(file.getAbsolutePath());
```
### 5）分享网页
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Title| 否 | String|网页标题|长度不能超过 512，注：Title和Text字段微信和微信收藏必须要有其一
Text| 否 | String|网页描述|长度不能超过 1K，朋友圈不显示该字段内容，注：Title和Text字段微信和微信收藏必须要有其一
Url| 是 | String|网页 Url|长度不能超过 10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过 10KB,大小不能超过 32K,与 ImageData 二选一
ImageData| 否 | Bitmap|缩略图，图片 Bitmap|大小不能超过 32K,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);//必须
shareParams.setImagePath(file.getAbsolutePath());
```
### 6）分享 Emoji 表情（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_EMOJI
ImagePath| 否 | String|本地图片路径|长度不能超过 10KB,大小不能超过 10M，ImagePath 与 ImageData 必须二选一
ImageData| 否 | Bitmap|图片 Bitmap|大小不能超过 10M，ImagePath 与 ImageData 必须二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_EMOJI);
shareParams.setImagePath(file.getAbsolutePath());
```
### 7）分享文件（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_FILE
FilePath| 是 | String|本地文件路径|长度不能超过 10KB,大小不能超过 10M
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_FILE);
shareParams.setFilePath(file.getAbsolutePath());
```

### 8）分享小程序（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_MINI_PROGRAM
Title| 否 | String|网页标题/小程序标题|长度不能超过 512，注：Title和Text字段微信必须要有其一(微信低于6.5.6版本，小程序分享变网页分享)
Text| 否 | String|网页描述/小程序描述|长度不能超过 1K，注：Title和Text字段微信必须要有其一(微信低于6.5.6版本，小程序分享变网页分享)
Url| 是 | String|网页 Url|长度不能超过 10K，用于微信低版本兼容，当微信客户端低于6.5.6时，小程序分享变网页分享
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过 10KB,大小不能超过 32K,与 ImageData 二选一，如果都没有填，默认使用MiniProgramImage的数据，用于微信低版本兼容，当微信客户端低于6.5.6时，小程序分享变网页分享
ImageData| 否 | Bitmap|缩略图，图片 Bitmap|大小不能超过 32K,与 ImagePath 二选一，如果都没有填，默认使用MiniProgramImage的数据，用于微信低版本兼容，当微信客户端低于6.5.6时，小程序分享变网页分享
MiniProgramPath| 否 | String|小程序页面路径|发起分享的App与小程序属于同一微信开放平台帐号
MiniProgramUserName| 是 | String|小程序原始id|发起分享的App与小程序属于同一微信开放平台帐号
MiniProgramImagePath| 否 | String|小程序缩略图，本地图片路径|长度不能超过 10KB,大小不能超过 128K,与 MiniProgramImageData 二必选一
MiniProgramImageData| 否 | Bitmap|小程序缩略图，图片 Bitmap|大小不能超过 128K,与 MiniProgramImagePath 二必选一
MiniProgramWithShareTicket| 是 | boolean|是否使用带shareTicket的分享|通常开发者希望分享出去的小程序被二次打开时可以获取到更多信息，例如群的标识。可以设置withShareTicket为true，当分享卡片在群聊中被其他用户打开时，可以获取到shareTicket，用于获取更多分享信息。最低客户端版本要求：6.5.13
MiniprogramType| 是 | int|小程序的类型|正式版:0，开发版（测试版）:1，体验版（预览版）:2
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_MINI_PROGRAM);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);//用于微信低版本兼容，当微信客户端为低版本时，小程序分享变网页分享
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setMiniProgramWithShareTicket(false);//
shareParams.setMiniProgramType(0);// 正式版:0，开发版（测试版）:1，体验版（预览版）:2
shareParams.setMiniProgramImagePath(file.getAbsolutePath());//小程序图片地址
shareParams.setMiniProgramPath("pages/index/index");//小程序页面路径
shareParams.setMiniProgramUserName("gh_cd370c00d3d4");//小程序原始id
```

## QQ
### 1）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片路径|ImagePath 与 ImageUrl 必须二选一
ImageUrl| 否 | String|网络图片地址|由于QQ的原因，从1.5.0版本起不再支持
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```
### 2）分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Title| 否 | String|标题|不超过 30 字符
Text| 否 | String|描述|不超过 40 字符
ImagePath| 否 | String|缩略图，本地图片路径|与 ImageUrl 二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以 http 或 https 开头,与 ImagePath 二选一
Url| 是 | String|跳转链接|必须以 http 或 https 开头
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setImagePath(file.getAbsolutePath());
```

### 3）分享app
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_APPS
Title| 否 | String|标题|不超过 30 字符
Text| 否 | String|描述|不超过 40 字符
ImagePath| 否 | String|缩略图，本地图片路径|与 ImageUrl 二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以 http 或 https 开头,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_APPS);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
```

### 4）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_MUSIC
Title| 否 | String|标题|不超过 30 字符
Text| 否 | String|描述|不超过 40 字符
MusicUrl| 是 | String|音乐链接|音乐文件的远程链接 ,点击播放按钮可直接播放， 以 URL 的形式传入 , 不支持本地音乐，必须以 http 或 https 开头
Url| 是 | String|跳转链接|跳转页面 url,必须以 http 或 https 开头
ImagePath| 否 | String|缩略图，本地图片路径|与 ImageUrl 二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以 http 或 https 开头,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_MUSIC);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setMusicUrl(music_url);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
```
## QQ空间
### 1)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
Text| 否 | String|描述|不超过 10000 字符
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText(share_text);
```
### 2)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片路径|ImagePath与ImageUrl、ImageArray必须三选一
ImageUrl| 否 | String|网络图片地址|必须以http或https开头,ImagePath与ImageUrl、ImageArray必须三选一
ImageArray| 否 | Array|图片地址数组|支持多个图片，超出9张后，会变成上传相册，上传相册时只支持本地图片,ImagePath与ImageUrl、ImageArray必须三选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(MyApplication.ImagePath);
//shareParams.setImageUrl(share_imageurl);
//String[] array = new String[]{ share_imageurl, share_imageurl_1};
//shareParams.setImageArray(array);
```
### 3)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Title| 是 | String|标题|最长 200 个字符
Text| 否 | String|描述|最长 600 个字符
Url| 是 | String|跳转链接|必须以 http 或 https 开头
ImagePath| 否 | String|缩略图，本地图片路径|与 ImageUrl 二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以 http 或 https 开头,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setTitle(share_title);
shareParams.setUrl(share_url);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
```
### 4)分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_MUSIC
Title| 是 | String|标题|最长 200 个字符
Text| 否 | String|描述|最长 600 个字符
MusicUrl| 否 | String|音乐链接|音乐文件的远程链接 ,点击播放按钮可直接播放， 以 URL 的形式传入 , 不支持本地音乐,必须以 http 或 https 开头
Url| 是 | String|跳转链接|跳转页面 url,必须以 http 或 https 开头
ImagePath| 否 | String|缩略图，本地图片路径|与 ImageUrl 二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以 http 或 https 开头,与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_MUSIC);
shareParams.setTitle(share_title);
shareParams.setMusicUrl(share_musicurl);
shareParams.setUrl(music_shareUrl);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
```
### 5)分享本地视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_VIDEO
VideoPath| 是 | String|本地视频地址|不支持网络视频
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(MyApplication.VideoPath);
```
## 新浪微博
### 1)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
Text| 是 | String|文本|不超过 1999 字符
ImagePath| 否 | String|本地图片地址|不支持网络图片,文件不超过 10M，与 ImageData 二选一
ImageData| 否 | Bitmap|本地图片 bitmap|不支持网络图片,不超过 2M，与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
```
### 2)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
Text| 否 | String|文本|不超过 1999 字符
ImagePath| 是 | String|本地图片地址|不支持网络图片,文件不超过 10M，与 ImageData 二选一
ImageData| 是 | Bitmap|本地图片 bitmap|不支持网络图片,不超过 2M，与 ImagePath 二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
```
### 3)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Text| 否 | String|文本|不超过1999 字符
ImagePath| 否 | String|本地图片地址|不支持网络图片,文件不超过 10M，与 ImageData 二选一
ImageData| 否 | Bitmap|本地图片 bitmap|不支持网络图片,不超过 2M，与 ImagePath 二选一
Url| 是 | String|跳转链接|长度不超过 512 字节
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setUrl(share_url);
```
## 新浪微博私信
### 1)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Text| 否 | String|文本|不超过1024 字符
Title| 否 | String|标题|不超过512 字符
ImagePath| 否 | String|本地图片地址|不支持网络图片,文件不超过 32K，与 ImageData 二选一
ImageData| 否 | Bitmap|本地图片 bitmap|不支持网络图片,不超过 32K，与 ImagePath 二选一
Url| 是 | String|跳转链接|长度不超过512 字节
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setUrl(share_url);
```

## Facebook、FbMessenger
### 1)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Url| 是 | String|分享链接|
Quote| 否 | String|分享引用|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);
shareParams.setQuote(quote);
```

### 2)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片地址|
ImageData| 否 | String|本地图片bitmap|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```

### 2)分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_VIDEO
VideoPath| 否 | String|本地视频地址|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(file.getAbsolutePath());
```

## Twitter
### 1)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
Text| 是 | String|文本|不可为空，文本长度不超过 140 字符
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText(text);
```
### 2)分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Url| 是 | String|分享链接|仅支持http、https
Text| 否 | String|文本|文本长度与链接长度之和不能超过140 字符
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);
```

### 3)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
Text| 否 | String|文本|与url总长度不能超过 140 字符
Url| 是 | String|分享链接|仅支持http、https，与文本总长度不超过 140 字符
ImagePath| 否 | String|本地图片地址|JPG, PNG, GIF, WEBP格式，不能超过5M，ImagePath与ImageUrl、ImageArray必须三选一
ImageData| 否 | String|本地图片bitmap|JPG, PNG, GIF, WEBP格式，不能超过5M，ImagePath与ImageUrl、ImageArray必须三选一
ImageArray| 否 | Array|本地图片地址数组|支持多个图片，最多4张，JPG, PNG, GIF, WEBP格式，单张不能超过5M，ImagePath与ImageUrl、ImageArray必须三选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```
### 4)分享视频
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_VIDEO
Text| 否 | String|文本|与url总长度不能超过 140 字符
Url| 是 | String|分享链接|仅支持http、https，与文本总长度不超过 140 字符
VideoPath| 是 | String|本地视频地址|不支持网络视频，视频的格式要求较多，具体参考twitter文档：https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(videoPath);
```



## JChatPro
### 1)分享图文
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGETEXT
AppName| 否 | String|应用名称|
title| 否 | String|消息标题|
text| 否 | String|消息内容|
ImageUrl| 否 | String|缩略图网络图片地址|
TargetPkg| 否 | String|点击消息时跳转应用的包名|
TargetClass| 否 | String|点击消息时跳转应用的类名|
Extra| 否 | String|点击消息跳转到第三方应用时带的extra信息|
Url| 否 | String|点击消息时跳转应用的url|
CallBackUrl| 否 | String|点击消息跳转第三方应用失败时，回调的url|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGETEXT);
shareParams.setAppName("JShareDemo");
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setTargetPkg("com.tencent.mm");
shareParams.setTargetClass("com.tencent.mm.ui.LauncherUI");
shareParams.setExtra("this message from jshare.");
```

### 2)分享文本
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
AppName| 否 | String|应用名称|
text| 否 | String|消息内容，建议不超过3Kb|
TargetPkg| 否 | String|点击消息时跳转应用的包名|
TargetClass| 否 | String|点击消息时跳转应用的类名|
Extra| 否 | String|点击消息跳转到第三方应用时带的extra信息|
Url| 否 | String|点击消息时跳转应用的url(iOS用)|
CallBackUrl| 否 | String|点击消息跳转第三方应用失败时，回调的url|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setAppName("JShareDemo");
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setTargetPkg("com.tencent.mm");
shareParams.setTargetClass("com.tencent.mm.ui.LauncherUI");
shareParams.setExtra("this message from jshare.");
```

### 3)分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
AppName| 否 | String|应用名称|
ImageUrl| 否 | String|图片网络地址，与img_path、img_array三选一|
ImagePath| 否 | String|图片本地地址，与img_url、img_array三选一|
ImageArray| 否 | String|图片地址数组，与img_url、img_path三选一，最多9张|
TargetPkg| 否 | String|点击消息时跳转应用的包名|
TargetClass| 否 | String|点击消息时跳转应用的类名|
Extra| 否 | String|点击消息跳转到第三方应用时带的extra信息|
Url| 否 | String|点击消息时跳转应用的url(iOS用)|
CallBackUrl| 否 | String|点击消息跳转第三方应用失败时，回调的url|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setAppName("JShareDemo");
//shareParams.setImageUrl(image_url);
//shareParams.setImagePath(image_path);
//shareParams.setImageArray(image_array);
shareParams.setUrl(share_url);
shareParams.setTargetPkg("com.tencent.mm");
shareParams.setTargetClass("com.tencent.mm.ui.LauncherUI");
shareParams.setExtra("this message from jshare.");
```