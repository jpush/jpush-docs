# Android JShare API

## SDK Initializes API

### API - init

The initialization interface is recommended to use in the OnCreate of the project's Application.

#### Interface Definition
```
public static void init(Context context)
```

#### Parameter Description

* ApplicationContext of the context

### API - init
The initialization interface is recommended to use in the OnCreate of the project's Application, and this initialization API supports the setting of third-party platform information in the code.

* Supported by SDK 1.5.0 or later versions

#### Interface Definition
```
public static void init(Context context, PlatformConfig platformConfig)
```

#### Parameter Description
* ApplicationContext of the context
* platformConfig: Information configuration of third-party platform, please see information settings API of third-party platforms

## Information Settings API of Third-party Platforms
JShare provides the PlatformConfig class. After the instantiation, you can choose to set the corresponding third-party platform information.
### API - setWechat
Set up information on WeChat platform
#### Interface Definition
```
public PlatformConfig setWechat(String appId, String appSecret)
```
#### Parameter Description
* appId：appId of WeChat
* appSecret：appSecret of WeChat


### API - setQQ
Set up information on QQ platform
#### Interface Definition
```
public PlatformConfig setQQ(String appId, String appKey)
```

#### Parameter Description
* appId: appId of QQ
* appKey: appKey of QQ

### API - setSinaWeibo
Set up information on Sina Weibo platform
#### Interface Definition
```
public PlatformConfig setSinaWeibo(String appKey, String appSecret, String redirectUrl)
```
#### Parameter Description
* appKey: appKey of Sina Weibo
* appSecret: appSecret of Sina Weibo
* redirectUrl: callback url of Sina Weibo

### API - setFacebook
Set up information on Facebook platform
#### Interface Definition
```
public PlatformConfig setFacebook(String appId, String appName)
```
#### Parameter Description
* appId: appId of Facebook
* appName; appName of Facebook

### API - setTwitter
Set up information on Twitter platform
#### Interface Definition
```
public PlatformConfig setTwitter(String consumerKey, String consumerSecret)
```

#### Parameter Description
* consumerKey; consumerKey of Twitter
* consumerSecret: consumerSecret of Twitter

## Get Platform APIs That Are Already Configured Correctly
### API - getPlatformList
Get all available platform names for the SDK. If you want to use a platform, you must configure the appropriate jar and third-party platform information.
#### Interface Definition
```
public static List<String> getPlatformList()
```

## Set Debug Mode API
### API - setDebugMode
Set debug mode.
Note: This interface needs to be called before the init interface to avoid the situation where some logs are not printed. In the case of multi-process, it is recommended to call in onCreate in the custom Application.
#### Interface Definition
```
public static void setDebugMode(boolean enable)
```
#### Parameter Description
* Print debug level logs when enable is true, and only print logs above warning level when enable is false

## Get Platform APIs That Are Already Configured Correctly
### API - getPlatformList
Get all available platform names for the SDK. If you want to use a platform, you must configure the appropriate jar and third-party platform information.

#### Interface Definition
```
public static List<String> getPlatformList()
```

##Determine whether sharing of the platform is a valid API
###API - isClientValid
Determine whether sharing of the platform is valid.
#### Interface Definition
```
public static boolean isClientValid(String name)
```
####Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name

## Sharing API
### API - share
Sharing interface
#### Interface Definition
```
public static void share(String name, ShareParams shareParams, PlatActionListener shareActionListener))
```
#### Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name
* shareParams: Please refer to the share parameter instructions on each platform for its specific settings
* shareActionListener: callback interface, which could be null. No callback when it is null.

## Determine whether a platform supports the authorization API
### API - isSupportAuthorize
Determine whether a platform supports authorization

* Supported by SDK 1.2.0 or later versions

#### Interface Definition
```
public static boolean isSupportAuthorize(String name)
```
#### Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name

## Authorization API

### API - authorize
Authorization interface

* Supported by SDK 1.2.0 or later versions

#### Interface Definition
```
public static void authorize(String name, AuthListener authListener)
```
#### Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name.
* authListener: callback interface, which could be null. No callback when it is null.
#### Code Example
```
JShareInterface.authorize(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int i, BaseResponseInfo data) {
        Logger.dd(TAG, "onComplete:" + platform + ",action:" + action + ",data:" + data);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_AUTHORIZING:
                if (data instanceof AccessTokenInfo) {        //授权信息
                    String token = ((AccessTokenInfo) data).getToken();// token
                    long expiration = ((AccessTokenInfo) data).getExpiresIn();// token有效时间，时间戳
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
    public void onError(Platform platform, int i, int i1, Throwable throwable) {
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_AUTHORIZING:
                toastMsg = "授权失败";
                break;
        }
    }

    @Override
    public void onCancel(Platform platform, int i) {
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

## Determine whether the API has been authorized

### API - isAuthorize
Determine whether the interface has been authorized

* Supported by SDK 1.2.0 or later versions

#### Interface Definition
```
public static boolean isAuthorize(String name)
```
#### Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name

## Remove Authorization API
### API - removeAuthorize
Remove authorization interface

* Supported by SDK 1.2.0 or later versions

#### Interface Definition
```
public static void removeAuthorize(String name, AuthListener actionListener)
```

#### Parameter Description
* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name
* authListener: callback interface, which could be null. No callback when it is null.

#### Code Example
```
JShareInterface.removeAuthorize(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int i, BaseResponseInfo data) {
       Logger.dd(TAG, "onComplete:" + platform + ",action:" + action + ",data:" + data);
       String toastMsg = null;
       switch (action) {
           case Platform.ACTION_REMOVE_AUTHORIZING:
               toastMsg = "删除授权成功";
               break;
       } 
    }

    @Override
    public void onError(Platform platform, int i, int i1, Throwable throwable) {
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

## Get User Information API
### API - getUserInfo
Get user information interface

* Supported by SDK 1.2.0 or later versions

#### Interface Definition
```
public static void getUserInfo(String platName, AuthListener authListener)
```
#### Parameter Description

* Name: platform name, values could be Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、SinaWeiboMessage.Name、QQ.Name、QZone.Name、Facebook.Name、FbMessenger.Name、Twitter.Name
* authListener: callback interface, which could be null. No callback when it is null.

#### Code Example
```
JShareInterface.getUserInfo(platform, new AuthListener() {
    @Override
    public void onComplete(Platform platform, int i, BaseResponseInfo data) {
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
    public void onError(Platform platform, int i, int i1, Throwable throwable) {
        Logger.dd(TAG, "onError:" + platform + ",action:" + action + ",error:" + error);
        String toastMsg = null;
        switch (action) {
            case Platform.ACTION_USER_INFO:
                toastMsg = "获取个人信息失败";
                break;
        }
    }

    @Override
    public void onCancel(Platform platform, int i) {
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

# Instructions of Share Parameters on Each Platform
## Wechat (including WeChat moments, Wechat collection)
### 1）Share Texts

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share type| Platform.SHARE_TEXT
Text | Yes | String|Share title|No more than 10KB

```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText("Text");//必须
```

### 2）Share Pictures
Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share Type| Platform.SHARE_IMAGE
ImagePath|NoNo | String|Thumbnail, local image path|Length can't exceed 10KB, size can't exceed 32K, choose it or ImageData
ImageData| No | Bitmap|Thumbnail, picture Bitmap|Size can't exceed 32K, choose it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageData(bitmap);
```


### 3）Share Musics

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_MUSIC
Title| No | String|Music title|Length cannot exceed 512
Text| No | String|Music description|Length cannot exceed 1k
MusicUrl| Yes | String|Music resources Url|Click play button to play url directly. The length cannot exceed 10K
Url| No | String|Jump Url|Click on the jump page url. The length cannot exceed 10K
ImagePath| No | String|Thumbnail, local image path|Length can't exceed 10KB, size can't exceed 32K, choose it or ImageData
ImageData| No | Bitmap|Thumbnail, picture Bitmap|Size can't exceed 32K, choose it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_MUSIC);
shareParams.setUrl(url);
shareParams.setMusicUrl(music_url);
shareParams.setImagePath(file.getAbsolutePath());
```

### 4）Share Videos

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_VIDEO
Title| No | String|Video title|Length cannot exceed 512
Text| No | String|Video description|Length cannot exceed 1K, and Wechat moments does not display the contents of this field
Url| Yes | String|Video Url|Length cannot exceed 10K
ImagePath| No | String|Thumbnail, local image path|Length can't exceed 10KB, size can't exceed 32K, choose it or ImageData
ImageData| No | Bitmap|Thumbnail, picture Bitmap|Size can't exceed 32K, choose it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setUrl(share_videourl);
shareParams.setImagePath(file.getAbsolutePath());
```

### 5）Share Websites

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_WEBPAGE
Title| No | String|Webpage title|Length cannot exceed 512
Text| No | String|Webpage description|Length cannot exceed 1K, and Wechat moments does not display the contents of this field
Url| Yes | String|Webpage Url|Length cannot exceed 10K
ImagePath| No | String|Thumbnail, local image path|Length can't exceed 10KB, size can't exceed 32K, choose it or ImageData
ImageData| No | Bitmap|Thumbnail, picture Bitmap|Size can't exceed 32K, choose it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);//必须
shareParams.setImagePath(file.getAbsolutePath());
```

### 6）Share Emoji Expressions (Not support in Wechat moments and Wechat collection)

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_EMOJI
ImagePath| No | String|Local image path|Length can't exceed 10KB, size can't exceed 32K, choose it or ImageData
ImageData| No | Bitmap|Picture Bitmap|Size can't exceed 32K, choose it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_EMOJI);
shareParams.setImagePath(file.getAbsolutePath());
```

### 7）Share Files (Not support in Wechat moments and Wechat collection)

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType |Yes| int| Share type| Platform.SHARE_FILE
FilePath| Yes | String|Local file path|Length can't exceed 10KB, and size can't exceed 32K
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_FILE);
shareParams.setFilePath(file.getAbsolutePath());
```

## QQ
### 1）Share Pictures

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share Type| Platform.SHARE_IMAGE
ImagePath| no | String|Local image path|Choose either ImagePath or ImageUrl 
ImageUrl| no | String|Network image address|Must start with http or https. Choose either ImagePath or ImageUrl
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```


### 2）Share Links

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| 分享类型| Platform.SHARE_WEBPAGE
Title| No | String|Title|No more than 30 characters
Text| No | String|Description|No more than 40 characters
ImagePath| No | String|Thumbnail, local image path|Choose either ImagePath or ImageUrl
ImageUrl| No | String|Thumbnail, web image address|Must start with http or https. Choose either ImagePath or ImageUrl
Url| Yes | String|Jump link|Must start with http or https
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setImagePath(file.getAbsolutePath());
```

### 3）Share Musics

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share Type| Platform.SHARE_MUSIC
Title| No | String|Title|No more than 30 characters
Text| No | String|Description|No more than 40 characters
MusicUrl| Yes | String|Music link|Remote link for music files. Click play button to play directly. It is passed as URL, does not support local music, and must start with http or https
Url| Yes | String|Jump link|Jump page url. Must start with http or https
ImagePath| No | String|Thumbnail, local image path|Choose either ImagePath or ImageUrl
ImageUrl| No | String|Thumbnail, web image address|Must start with http or https. Choose either ImagePath or ImageUrl
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


## QQ Space
### 1)Share Texts

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share type| Platform.SHARE_TEXT
Text| No | String|Description|No more than 10000 characters
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText(share_text);
```

### 2)Share Pictures

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share Type| Platform.SHARE_IMAGE
ImagePath| No | String|Local image path|Choose one from ImagePath, ImageUrl、and ImageArray 
ImageUrl| No | String|Must start with http or https. Choose one from ImagePath, ImageUrl、and ImageArray
ImageArray| No | Array|Image address array|Support multiple pictures. After more than 9 pictures, it will become an uploaded album. Uploaded album only supports local pictures. Choose one from ImagePath, ImageUrl、and ImageArray.
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(MyApplication.ImagePath);
//shareParams.setImageUrl(share_imageurl);
//String[] array = new String[]{ share_imageurl, share_imageurl_1};
//shareParams.setImageArray(array);
```

### 3)Share Links

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share type| Platform.SHARE_WEBPAGE
Title| Yes | String|Title|Up to 200 characters
Text| No | String|Description|Up to 600 characters
Url| Yes | String|Jump link|Must start with http or https.
ImagePath| No | String|Thumbnail, local image path|Choose either ImagePath or ImageUrl
ImageUrl| No | String|Thumbnail, web image address|Must start with http or https. Choose either ImagePath or ImageUrl
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setTitle(share_title);
shareParams.setUrl(share_url);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
```


### 4)Share Musics

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| Share Type| Platform.SHARE_MUSIC
Title| Yes | String|Title|Up to 200 characters
Text| No | String|Description|Up to 600 characters
MusicUrl| No | String|Music links|Remote link for music files. Click play button to play directly. It is passed as URL, does not support local music, and must start with http or https
Url| Yes | String|Jump link|Jump page url. Must start with http or https
ImagePath| No | String|Thumbnail, local image path|Choose either ImagePath or ImageUrl
ImageUrl| No | String|Thumbnail, web image address|Must start with http or https. Choose either ImagePath or ImageUrl
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_MUSIC);
shareParams.setTitle(share_title);
shareParams.setMusicUrl(share_musicurl);
shareParams.setUrl(music_shareUrl);
shareParams.setImagePath(file.getAbsolutePath());
//shareParams.setImageUrl("http://inews.gtimg.com/newsapp_bt/0/876781763/1000");
```


### 5)Share Local Videos

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_VIDEO
VideoPath| Yes | String|Local video address|Not support online videos
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(MyApplication.VideoPath);
```

## Sina Weibo
### 1)Share Texts
Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_TEXT
Text| Yes | String|Text|No more than 1999
ImagePath| No | String|Local image address |Not support network images, and files cannot exceed 2M. Choose either it or ImageData
ImageData| No | Bitmap|Local picture bitmap|Not support network images, and files cannot exceed 2M. Choose either it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
```


### 2)Share Pictures

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_IMAGE
Text| No | String|Text|No more than 1999
ImagePath| Yes | String|Local image address |Not support network images, and files cannot exceed 2M. Choose either it or ImageData
ImageData| Yes | Bitmap|Local picture bitmap|Not support network images, and files cannot exceed 2M. Choose either it or ImagePath
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
```

### 3)Share Links
Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_WEBPAGE
Text| No | String|Text|No more than 1999
ImagePath| No | String|Local image address |Not support network images, and files cannot exceed 2M. Choose either it or ImageData
ImageData| No | Bitmap|Local picture bitmap|Not support network images, and files cannot exceed 2M. Choose either it or ImagePath
Url| Yes | String|Jump link|Length cannot exceed 512
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setUrl(share_url);
```

## Direct Message on Sina Weibo
### 1)Share Links

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_WEBPAGE
Text| No | String|Text|No more than 1024
Title| No | String|Title|No more than 512
ImagePath| No | String|Local image address |Not support network images, and files cannot exceed 32K. Choose either it or ImageData
ImageData| No | Bitmap|Local picture bitmap|Not support network images, and files cannot exceed 32K. Choose either it or ImagePath
Url| Yes | String|Jump links|The length does not exceed 512
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setUrl(share_url);
```

## Facebook、FbMessenger
### 1)Share Links

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_WEBPAGE
Url| Yes | String|Share links|
Quote| No | String|Share references|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);
shareParams.setQuote(quote);
```

### 2)Share Pictures
Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_IMAGE
ImagePath| No | String|Local image address |
ImageData| No | String|Local picture bitmap|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```

### 3)Share Videos

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | 是| int| ShareType| Platform.SHARE_VIDEO
VideoPath| No | String|Local video address|
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(file.getAbsolutePath());
```

## Twitter
### 1)Share Texts

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | 是| int| ShareType| Platform.SHARE_TEXT
Text| 是 | String|Text|Cannot be empty, and text length cannot exceed 140
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setUrl(text);
```

### 2)Share Links

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | 是| int| Share Type| Platform.SHARE_WEBPAGE
Url| 是 | String|Share Links|Only supports http and https. Sharing can have pictures or videos, but cannot have pictures and videos at the same time
Text| No | String|Text|The sum of text length and link length cannot exceed 140
ImagePath| No | String|Local image address |In the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray 
ImageData| No | String|Local picture bitmap|JIn the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray 
ImageArray| No | Array|Array of local image address|Support multiple pictures, up to 4. In the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray
VideoPath| No | String|Local video address|Not support online videos
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);
```

### 3)Share Pictures

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | 是| int| ShareType| Platform.SHARE_IMAGE
Text| No | String|Text|Text length cannot exceed 140
ImagePath| No | String|Local image address |In the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray 
ImageData| No | String|Local picture bitmap|In the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray 
ImageArray| No | Array|Array of local image address |Support multiple pictures, up to 4. In the format of JPG, PNG, GIF, WEBP and cannot exceed 5M. Choose one from ImagePath, ImageUrl and ImageArray
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```

### 4)Share Videos

Parameter |Whether Required|Parameter Type|Parameter Description|Remarks
---- |-----|----|----|----
ShareType | Yes| int| ShareType| Platform.SHARE_VIDEO
Text| No | String|Text|Text length cannot exceed 140
VideoPath| Yes | String|Local video address|Not support online videos. There are many requirements on formats of the video, please refer to the twitter document: https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_VIDEO);
shareParams.setVideoPath(videoPath);
```

