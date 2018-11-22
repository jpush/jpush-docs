<h1>Android IM SDK 基础功能</h1>


## 概述
JMessage Android IM SDK的基础功能。了解极光 IM 的详细信息，请参考文档：[JMessage 产品简介](../../guideline/jmessage_guide)


### 字符串规范
此处定义JMessage产品里字段属性与规范，用于校验与规范化。  

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >参数</th>
			<th >字符说明</th>
			<th >长度限制</th>
		</tr>
		<tr >
			<td>app_key</td>
			<td>由 JPush Web Portal 生成的 24位字符串。字母或者数字，不区分大小写</td>
			<td></td>
		</tr>
		<tr >
			<td>username</td>
			<td>以字母或者数字开头。支持字母、数字、下划线、英文点、减号、 @。</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>password</td>
			<td>不限</td>
			<td>Byte(4~128)</td>
		</tr>
		<tr >
			<td>group_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>nickname</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>note_name</td>
			<td>不支持的字符：“\n” “\r”</td>
			<td>Byte(0~64)</td>
		</tr>
		<tr >
			<td>other</td>
			<td>其他未明确指定的 String 类型字段，都按照这个处理。  
支持字符：全部</td>
			<td>Byte(0~250)</td>
		</tr>
	</table>
</div>



### SDK 初始化

在调用IM其他接口前必须先调此接口初始化SDK，推荐在application类中调用。默认关闭消息漫游。
```
JMessageClient.init(Context context)
```

参数说明

+ Context context 应用程序上下文对象。

### SDK初始化(设置消息记录漫游)
***Since 2.1.0***  
SDK初始化,同时指定是否启用消息记录漫游。  
打开消息漫游之后，用户多个设备之间登录时，sdk会自动将当前登录用户的历史消息同步到本地，同步完成之后sdk会发送一个`ConversationRefreshEvent`事件通知上层刷新，具体事件处理方法见[事件处理](./event)一节。</br>

```
JMessageClient.init(Context context, boolean msgRoaming)
```
参数说明

+ Context context 应用程序上下文对象。
+ boolean msgRoaming 是否启用消息漫游，true - 启用，false - 关闭。 


### 注册
```
JMessageClient.register(String username, String password, BasicCallback callback);

/**
 * 注册同时指定用户信息中的其他字段
 * @since 2.3.0
 */
JMessageClient.register(String userName, String password, RegisterOptionalUserInfo optionalUserInfo, BasicCallback callback);
```

参数说明

+ String username 用户名
+ String password 用户密码
+ RegisterOptionalUserInfo optionalUserInfo 注册时的用户其他信息
+ BasicCallback callback 结果回调


### 登录
```
JMessageClient.login(String username, String password, BasicCallback callback);
```

参数说明

+ String username 用户名
+ String password 用户密码
+ BasicCallback callback 结果回调

### 退出登录
```
JMessageClient.logout();
```

### 登陆设备记录
***Since 2.5.0***  
登陆时获取设备登陆记录
```
    /**
     * 用户登陆，并且在回调中获取用户账号所登陆过的设备信息{@link cn.jpush.im.android.api.model.DeviceInfo}<br/>
     * 每个端：移动端（Android 、iOS），PC端，Web端（JS、微信小程序）只保存最近一次设备登陆记录。
     *
     * @param userName 开发者注册的用户名，应该唯一。
     * @param password 用户登录密码，推荐将字符串加密。
     * @param callback 回调接口
     * @since 2.5.0
     */
    public static void login(String userName, String password, RequestCallback<List<DeviceInfo>> callback) {
        login(userName, password, (BasicCallback) callback);
    }
```
DeviceInfo
<div class="table-d" align="left" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th width="10px">方法</th>
      <th width="20px">类型</th>
      <th width="370px">说明</th>
    </tr>
    <tr >
      <td >getDeviceID()</td>
      <td >`long`</td>
      <td >获取设备ID</td>
    </tr>
	<tr >
      <td >getPlatformType()</td>
      <td >`PlatformType`</td>
      <td >获取设备所属平台类型</td>
    </tr>
    <tr >
      <td >getOnlineStatus()</td>
      <td >`int`</td>
      <td >获取设备在线状态，0不在线，1在线</td>
    </tr>
	<tr >
      <td >isLogin()</td>
      <td >`boolean`</td>
      <td >判断设备当前是否处于登陆状态, true:登陆，false:登出</td>
    </tr>
	<tr >
      <td >getLastLoginTime()</td>
      <td >`int`</td>
      <td > 获取设备最近一次登陆时间，单位-秒</td>
    </tr>
	<tr >
      <td >getFlag()</td>
      <td >`int`</td>
      <td > 默认为0，1表示该设备被当前登录设备踢出</td>
    </tr>
    </table>
</div>

### 多端同时在线
SDK从2.3.0版本开始支持多端同时在线，具体规则见[多端在线说明](../../guideline/faq/#multi-platfrom)

