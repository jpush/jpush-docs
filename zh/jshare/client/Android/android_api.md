# Android JShare API
### API - init
初始化接口，建议在项目的Appliction的OnCreate中使用。  
#### 接口定义
```
public static void init(Context context)
```
#### 参数说明
* context 应用的 ApplicationContext

### API - setDebugModel
设置调试模式。  
注：该接口需在init接口之前调用，避免出现部分日志没打印的情况。多进程情况下建议在自定义的Application中onCreate中调用。
#### 接口定义
```
public static void setDebugModel(boolean enable)
```
#### 参数说明
* enable enable 为true则会打印debug级别的日志，false则只会打印warning级别以上的日志

### API - getPlatformList
获取SDK所有能用的平台名称，如要使用某个平台，必须在JGShareSDK.xml中配置。  
#### 接口定义
```
public static List<String> getPlatformList()
```

### API - isClientValid
判断该平台的分享是否有效。
#### 接口定义
```
public static boolean isClientValid(String name)
```
#### 参数说明
* name 平台名称，值可选Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、QQ.Name、QZone.Name。  

### API - share
分享接口
#### 接口定义
```
public static void share(String name, ShareParams shareParams, PlatActionListener shareActionListener))
```
#### 参数说明
* name 平台名称，值可选Wechat.Name、WechatMoments.Name、WechatFavorite.Name、SinaWeibo.Name、QQ.Name、QZone.Name。  
* shareParams 分享的配置参数，具体设置请参考各个平台的分享参数说明。
* shareActionListener 回调接口，可为null，为null时则没有回调

# 各个平台的分享参数说明
## 微信(包括微信朋友圈、微信收藏)
### 1）分享文本

参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_TEXT
Text | 是 | String|分享标题|不超过10K

```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_TEXT);
shareParams.setText("Text");//必须
```
### 2）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片路径|长度不能超过10K,大小不能超过10M，ImagePath与ImageData必须二选一
ImageData| 否 | Bitmap|图片Bitmap|大小不能超过10M，ImagePath与ImageData必须二选一
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
Title| 否 | String|音乐标题|长度不能超过512字符
Text| 否 | String|音乐描述|长度不能超过1K
MusicUrl| 是 | String|音乐资源Url|点击播放按钮可直接播放url,长度不能超过10K
Url| 否 | String|跳转Url|点击跳转页面url,长度不能超过10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过10K,大小不能超过32K,与ImageData二选一
ImageData| 否 | Bitmap|缩略图，图片Bitmap|大小不能超过32K,与ImagePath二选一
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
Title| 否 | String|视频标题|长度不能超过512字符
Text| 否 | String|视频描述|长度不能超过1K，朋友圈不显示该字段内容
Url| 是 | String|视频Url|长度不能超过10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过10K,大小不能超过32K,与ImageData二选一
ImageData| 否 | Bitmap|缩略图，图片Bitmap|大小不能超过32K,与ImagePath二选一
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
Title| 否 | String|网页标题|长度不能超过512字符
Text| 否 | String|网页描述|长度不能超过1K，朋友圈不显示该字段内容
Url| 是 | String|网页Url|长度不能超过10K
ImagePath| 否 | String|缩略图，本地图片路径|长度不能超过10K,大小不能超过32K,与ImageData二选一
ImageData| 否 | Bitmap|缩略图，图片Bitmap|大小不能超过32K,与ImagePath二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setUrl(share_url);//必须
shareParams.setImagePath(file.getAbsolutePath());
```
### 6）分享Emoji表情（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_EMOJI
ImagePath| 否 | String|本地图片路径|长度不能超过10K,大小不能超过10M，ImagePath与ImageData必须二选一
ImageData| 否 | Bitmap|图片Bitmap|大小不能超过10M，ImagePath与ImageData必须二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_EMOJI);
shareParams.setImagePath(file.getAbsolutePath());
```
### 7）分享文件（朋友圈、微信收藏不支持）
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_FILE
FilePath| 是 | String|本地文件路径|长度不能超过10K,大小不能超过10M
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_FILE);
shareParams.setFilePath(file.getAbsolutePath());
```
## QQ
### 1）分享图片
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_IMAGE
ImagePath| 否 | String|本地图片路径|ImagePath与ImageUrl必须二选一
ImageUrl| 否 | String|网络图片地址|必须以http或https开头,ImagePath与ImageUrl必须二选一
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_IMAGE);
shareParams.setImagePath(file.getAbsolutePath());
```
### 2）分享链接
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_WEBPAGE
Title| 否 | String|标题|不超过30字符
Text| 否 | String|描述|不超过40字符
ImagePath| 否 | String|缩略图，本地图片路径|与ImageUrl二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以http或https开头,与ImagePath二选一
Url| 是 | String|跳转链接|必须以http或https开头
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setTitle(share_title);
shareParams.setText(share_text);
shareParams.setUrl(share_url);
shareParams.setImagePath(file.getAbsolutePath());
```
### 3）分享音乐
参数 |是否必须|参数类型|参数说明|备注
---- |-----|----|----|----
ShareType | 是| int| 分享类型| Platform.SHARE_MUSIC
Title| 否 | String|标题|不超过30字符
Text| 否 | String|描述|不超过40字符
MusicUrl| 是 | String|音乐链接|音乐文件的远程链接 ,点击播放按钮可直接播放， 以 URL 的形式传入 , 不支持本地音乐，必须以http或https开头
Url| 是 | String|跳转链接|跳转页面url,必须以http或https开头
ImagePath| 否 | String|缩略图，本地图片路径|与ImageUrl二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以http或https开头,与ImagePath二选一
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
Text| 否 | String|描述|不超过10000字符
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
Url| 是 | String|跳转链接|必须以http或https开头
ImagePath| 否 | String|缩略图，本地图片路径|与ImageUrl二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以http或https开头,与ImagePath二选一
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
MusicUrl| 否 | String|音乐链接|音乐文件的远程链接 ,点击播放按钮可直接播放， 以 URL 的形式传入 , 不支持本地音乐,必须以http或https开头
Url| 是 | String|跳转链接|跳转页面url,必须以http或https开头
ImagePath| 否 | String|缩略图，本地图片路径|与ImageUrl二选一
ImageUrl| 否 | String|缩略图，网络图片地址|必须以http或https开头,与ImagePath二选一
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
Text| 是 | String|文本|不超过1999字符
ImagePath| 否 | String|本地图片地址|不支持网络图片,文件不超过10M，与ImageData二选一
ImageData| 否 | Bitmap|本地图片bitmap|不支持网络图片,不超过2M，与ImagePath二选一
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
Text| 否 | String|文本|不超过1999字符
ImagePath| 是 | String|本地图片地址|不支持网络图片,文件不超过10M，与ImageData二选一
ImageData| 是 | Bitmap|本地图片bitmap|不支持网络图片,不超过2M，与ImagePath二选一
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
Text| 否 | String|文本|不超过1999字符
ImagePath| 否 | String|本地图片地址|不支持网络图片,文件不超过10M，与ImageData二选一
ImageData| 否 | Bitmap|本地图片bitmap|不支持网络图片,不超过2M，与ImagePath二选一
Url| 是 | String|跳转链接|长度不超过512字符
```
ShareParams shareParams = new ShareParams();
shareParams.setShareType(Platform.SHARE_WEBPAGE);
shareParams.setText(share_text);
shareParams.setImagePath(file.getAbsolutePath());
shareParams.setUrl(share_url);
```