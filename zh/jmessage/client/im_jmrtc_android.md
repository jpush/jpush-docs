<h1>Android JMRTC SDK 实时音视频</h1>


## 概述

极光 IM 为开发者提供稳定可靠的实时音视频开发框架（简称 JMRTC），开发者可集成 JMRTC SDK，快速实现实时音视频通讯功能，支持1对1语音/视频私聊，多人语音视频聊天。


### 集成指南
#### 使用提示
+ JMRTC是基于JMessage功能上使用的，如果要集成JMRTC需要先集成JMessage，并且JMessage从2.6.0才开始支持JMRTC。
+ 如果您看到本文档，但还未下载Android With JMRTC SDK，请访问[SDK下载页面](../resources)下载。

+ 音视频服务需[付费开通](../guideline/faq/#open)或[申请试用](../guideline/faq/#_15)后才能使用，详细价格方案见：[计费说明](../guideline/faq/#_5)

#### JMessage with JMRTC SDK压缩包内容简介
+ demo/
	+ 一个用来展示JMessage SDK接口和JMRTC接口基本用法的demo应用。
+ doc/jmessage
	+ JMessage sdk中所包含所有对外接口的java doc。
+ doc/jmrtc
    + JMRTC sdk中所包含所有对外接口的java doc。
+ libs/jcore-android_v1.X.Y.jar
	+ 极光开发者服务的核心包。
+ libs/jmessage-android-2.X.Y.jar
	+ JMessage SDK开发包
+ libs/jmrtc-android-1.X.Y.jar
    + JMRTC SDK开发包
+ libs/agora-rtc-sdk.jar
    + agora SDK开发包
+ libs/(cpu-type)/libjcore1xy.so 
    + 各种CPU类型的native开发包。

#### jcenter 自动集成步骤
+ 如果您没有集成过JMessage或JMessage版本低于2.6.0需要先集成JMessage，请见[JMessage集成指南](./jmessage_android_guide)。
```
compile 'cn.jiguang.sdk:jmrtc:1.0.2'  // 此处以jmrtc 1.0.2 版本为例
```
#### 手动集成步骤:
+ 解压缩 jmessage-sdk-android-with-JMRTC-v2.X.Y.zip 集成压缩包
+ 如果您没有集成过JMessage或JMessage版本低于2.6.0需要先集成JMessage，请见[JMessage集成指南](./jmessage_android_guide)。
	+ 注意下载的JMessage with JMRTC SDK包含JMessage SDK包，集成JMessage时无需再下载
+ 复制 libs/jmrtc-android-1.X.Y.jar.jar 到工程 libs/ 目录下。
+ 复制 libs/agora-rtc-sdk.jar 到工程 libs/ 目录下
+ 配置AndroidManifest.xml，查看AndroidManifest.xml是否包含以下内容，不包含则添加
```
    <!-- Required for jmrtc -->
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.CAMERA" />
	<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```
+ 混淆文件中添加JMRTC配置
```
#========================JMRTC================================
-dontwarn cn.jiguang.jmrtc.**
-keep class cn.jiguang.jmrtc.api.** {*;}

#========================Agora================================
-dontwarn io.agora.rtc.**
-keep class io.agora.rtc.** {*;}
```

### 开发指南
#### 业务流程

![JMRTC][0]

#### 音视频引擎初始化
在使用其他接口之前，必须先调用此接口初始化引擎。
```
/**
 * @param listener 音视频相关事件回调监听类
 */
JMRtcClient.getInstance().initEngine(JMRtcListener listener);
```
调用此接口，sdk背后会检查初始化所需要的权限。如果必要权限没有获取到，则会触发`JMRtcListener#onPermissionNotGranted(String[])`回调通知上层,获取权限成功以后调用下面接口重新初始化引擎。
```
JMRtcClient.getInstance().reinitEngine();
```

#### 释放音视频引擎
释放之后如果需要再次使用音视频服务，需要重新调用`JMRtcClient.initEngine(JMRtcListener)`来重新初始化音视频引擎。
```
JMRtcClient.getInstance.releaseEngine();
```

#### 主要通话行为
##### 发起通话邀请
```
/**
 * 发起通话邀请。
 * 任何通话的发起都应该以此接口开始。
 * <p>
 * 邀请发出之后，触发{@link JMRtcListener#onCallOutgoing(JMRtcSession)}回调，通知上层正在发起通话。之后进入outgoing状态。
 * <p>
 * 被邀请方收到邀请时，触发{@link JMRtcListener#onCallInviteReceived(JMRtcSession)}回调，通知上层收到邀请。
 *
 * @param invitedUsers 被邀请的用户的UserInfo集合
 * @param mediaType    通话类型
 * @param callback     结果回调
 */
JMRtcClient.getInstance().call(List<UserInfo> invitedUsers, JMSignalingMessage.MediaType mediaType, final BasicCallback callback);
```

##### 邀请其他用户加入通话
与发起通话邀请的区别是此时用户已经处在通话频道中，邀请其他用户加入该频道
```
/**
 * 向其他用户发起邀请，加入通话。
 * 此接口只能在通话建立、sdk回调了{@link JMRtcListener#onCallConnected(JMRtcSession, SurfaceView)}接口之后，才能发起调用。
 * <p>
 * 邀请发出之后，当前通话中的其他用户会触发{@link JMRtcListener#onCallOtherUserInvited(UserInfo, List, JMRtcSession)}回调，通知上层有其他人被邀请加入通话
 * <p>
 * 被邀请方收到邀请时，触发{@link JMRtcListener#onCallInviteReceived(JMRtcSession)}回调，通知上层收到邀请。
 *
 * @param invitedUsers 被邀请的用户的UserInfo集合
 * @param callback     结果回调
 */
JMRtcClient.getInstance().invite(List<UserInfo> invitedUsers, final BasicCallback callback);
```

##### 接受通话邀请
```
/**
 * 接受通话邀请。
 * 此接口只能在收到通话邀请、sdk回调了{@link JMRtcListener#onCallInviteReceived(JMRtcSession)}之后，才能发起调用。
 * <p>
 * 成功调用后，双方都会触发{@link JMRtcListener#onCallConnected(JMRtcSession, SurfaceView)}通知上层通话连接已建立。
 * 并且sdk会通过{@link JMRtcListener#onCallMemberJoin(UserInfo, SurfaceView)}上报当前已经在通话频道内的用户。
 *
 * @param callback 结果回调
 */
JMRtcClient.getInstance().accept(final BasicCallback callback);
```

##### 拒绝通话邀请
```
/**
 * 拒绝通话邀请。
 * 此接口只能在收到通话邀请、sdk回调了{@link JMRtcListener#onCallInviteReceived(JMRtcSession)}之后，才能发起调用。
 * <p>
 * 成功调用后，被邀请方会触发{@link JMRtcListener#onCallDisconnected(DisconnectReason)}通知上层连接断开，通话已结束。
 * <p>
 * 邀请方触发{@link JMRtcListener#onCallMemberOffline(UserInfo, DisconnectReason)}通知上层有用户离线，离线原因{@link DisconnectReason#refuse}
 *
 * @param callback 结果回调
 */
JMRtcClient.getInstance().refuse(final BasicCallback callback);
```

##### 通话挂断
```
/**
 * 通话挂断。
 * 此接口可以在邀请阶段以及通话阶段由任意通话中用户发起
 * <p>
 * 成功调用后，调用者会触发{@link JMRtcListener#onCallDisconnected(DisconnectReason)}通知上层连接断开，通话已结束。
 * <p>
 * 其他用户触发{@link JMRtcListener#onCallMemberOffline(UserInfo, DisconnectReason)}通知上层有用户离线，离线原因{@link DisconnectReason#hangup}
 *
 * @param callback 结果回调
 */
JMRtcClient.getInstance().hangup(final BasicCallback callback);
```

#### 通话属性设置
##### 设置本地音频输出开关
```
/**
 * 设置本地音频输出开关。只在视频或语音通话连接建立之后调用有效。
 * <p>
 * 默认打开。
 *
 * @param isEnable true - 开启音频输出, false - 关闭音频输出
 * @return 操作结果。 true - 操作成功，false - 操作失败
 */
JMRtcClient.getInstance().enableAudio(boolean isEnable);
```

##### 设置本地视频输出开关
```
/**
 * 设置本地视频输出开关。只在视频通话连接建立之后调用有效。
 * <p>
 * 视频通话中默认打开。音频通话中此接口无效。
 *
 * @param isEnable true - 开启视频输出, false - 关闭视频输出
 * @return 操作结果。 true - 操作成功，false - 操作失败
 */
JMRtcClient.getInstance().enableVideo(boolean isEnable) {
	if (null == stateMachine) {
		Logger.ee(TAG, "[enableVideo] failed. should init engine first.");
		return false;
	}
	return stateMachine.enableVideo(isEnable);
}
```

##### 设置使用本地外置扬声器开关
```
/**
 * 设置使用本地外置扬声器开关。只在视频或语音通话连接建立之后调用有效。
 * <p>
 * 默认打开
 *
 * @param isEnable true - 使用外置扬声器, false - 不使用外置扬声器
 * @return 操作结果。 true - 操作成功，false - 操作失败
 */
JMRtcClient.getInstance().enableSpeakerphone(boolean isEnable);
```

##### 切换前置/后置摄像头
```
/**
 * 切换前置/后置摄像头。只在视频或语音通话连接建立之后调用有效。
 * <p>
 * 默认使用前置摄像头
 *
 * @return 操作结果。 true - 操作成功，false - 操作失败
 */
JMRtcClient.getInstance.switchCamera()
```

##### 设置视频输出的编码属性
```
/**
 * 设置视频输出的编码属性
 * <p>
 * 视频通话期间调用此接口设置的属性将在下次视频通话中生效
 *
 * @param videoProfile 视频编码属性
 */
JMRtcClient.getInstance.setVideoProfile(VideoProfile videoProfile);
```

##### 获取当前设置的视频编码属性
```
/**
 * 获取当前设置的视频编码属性
 * <p>
 * 默认为{@link VideoProfile#Profile_360P}
 *
 * @return
 */
JMRtcClient.getInstance.getVideoProfile();
```

#### 通话元信息Session
##### 获取当前通话Session(通话元信息)对象
```
/**
 * 获取当前通话session对象。
 *
 * @return {@link JMRtcSession}对象,如果当前不在任何会话中，则返回null。
 */
JMRtcClient.getInstance.getSession();
```

##### 获取通话类型
```
/**
 * 获取通话类型
 *
 * @return 通话类型
 */
session.getMediaType();
```

##### 获取用户在通信中的角色
```
/**
 * 获取用户在通信中的角色，{@link SessionRole#inviter}邀请发起者，或者{@link SessionRole#invited}被邀请者。
 *
 * @return 通信中的角色
 */
session.getSessionRole();
```

##### 获取邀请者用户信息
```
/**
 * 获取邀请者用户信息
 *
 * @param callback 结果回调
 */
session.getInviterUserInfo(final RequestCallback<UserInfo> callback);
```

##### 获取当前被邀请的用户的用户信息集合
```
/**
 * 获取当前被邀请的用户的用户信息集合
 *
 * @param callback 结果回调
 */
session.getInvitingUserInfos(final RequestCallback<List<UserInfo>> callback);
```

##### 获取当前已加入通信的用户的用户信息集合
```
/**
 * 获取当前已加入通信的用户的用户信息集合
 *
 * @param callback 结果回调
 */
session.getJoiendMembers(final RequestCallback<List<UserInfo>> callback);
```

#### 相关事件回调
##### JMRtc引擎初始化结果
```
/**
 * jmrtc引擎初始化结果回调。
 *
 * @param errCode 错误码。 0 - 成功，其他错误码参见错误码定义表
 * @param errDesc 错误描述。
 */
public void onEngineInitComplete(int errCode, String errDesc) {
}
```
#####  通话已播出(onCallOutgoing)
```
/**
 * 邀请方成功调用{@link JMRtcClient#call(List, JMSignalingMessage.MediaType, BasicCallback)}后，会触发此回调通知上层通话已播出。
 *
 * @param callSession 保存通信元信息的实体对象
 */
public void onCallOutgoing(JMRtcSession callSession) {
}
```

##### 收到通话邀请(onCallInviteReceived)
只有状态机处于Idle状态时，才会触发此回调
```
/**
 * 被邀请方收到邀请时，会触发此回调通知上层收到通话邀请。
 *
 * @param callSession 保存通信元信息的实体对象
 */
public void onCallInviteReceived(JMRtcSession callSession) {
}
```

##### 通话过程中，有其他用户被邀请(onCallOtherUserInvited)
```
/**
 * 通话过程中，有其他用户被邀请。
 *
 * @param fromUserInfo     邀请发起方用户信息
 * @param invitedUserInfos 被邀请方用户信息集合
 * @param callSession      保存通信元信息的实体对象
 */
public void onCallOtherUserInvited(UserInfo fromUserInfo, List<UserInfo> invitedUserInfos, JMRtcSession callSession) {
}
```

##### 音视频通信连接已建立(onCallConnected)
```
/**
 * 音视频通信连接已建立。
 * 当被邀请方有任意一方成功调用{@link JMRtcClient#accept(BasicCallback)}接受邀请后，邀请方和接受方都会触发此回调通知上层通信连接已建立。
 *
 * @param callSession      保存通信元信息的实体对象
 * @param localSurfaceView 本地视频预览SurfaceView对象，对于视频聊天，上层可以直接用此对象在界面上进行渲染展示。
 */
public void onCallConnected(JMRtcSession callSession, SurfaceView localSurfaceView) {
}
```

##### 有用户加入通信(onCallMemberJoin)
对于刚加入通信的用户，此接口会上报当前所有已在通信中的用户的信息,对于已加入通信的用户，此接口上报通信过程中加入的用户的信息。
```
/**
 *
 * @param joinedUserInfo    加入的用户的用户信息
 * @param remoteSurfaceView 加入用户的视频预览SurfaceView对象。对于视频聊天，上层可以直接用此对象在界面上进行渲染展示。
 */
public void onCallMemberJoin(UserInfo joinedUserInfo, SurfaceView remoteSurfaceView) {
}
```

##### 通话过程中，有用户退出通话
```
/**
 * 通话过程中，有用户退出通话。
 *
 * @param leavedUserInfo 退出通话的用户的用户信息
 * @param reason         退出原因
 */
public void onCallMemberOffline(UserInfo leavedUserInfo, JMRtcClient.DisconnectReason reason) {
}
```

##### 通话连接断开
```
/**
 * 通话连接断开。
 *
 * @param reason 断开原因
 */
public void onCallDisconnected(JMRtcClient.DisconnectReason reason) {
}
```

##### 通话过程中发生错误
```
/**
 * 通话过程中发生错误
 *
 * @param errorCode 错误码
 * @param desc      错误描述
 */
public void onCallError(int errorCode, String desc) {
}
```

##### 音视频初始化失败
音视频引擎初始化过程中，有些必要的权限没有获取到导致初始化失败时回调。
```
/**
 * 上层收到此回调后，建议根据系统具体版本决定是否需要向用户动态申请权限（android 6.0之后）。
 * 权限申请成功之后，需要调用{@link JMRtcClient#reinitEngine()}重新初始化引擎。
 *
 * @param requiredPermissions 缺少的权限
 */
public void onPermissionNotGranted(String[] requiredPermissions) {
}
```

##### 对方用户禁用/启用视频流
```
/**
 * 对方用户禁用/启用视频流时的回调。
 *
 * @param remoteUser 用户信息
 * @param isMuted    是否禁用。 true - 禁用，false - 启用
 */
public void onRemoteVideoMuted(UserInfo remoteUser, boolean isMuted) {
}
```

### 错误码定义

参考文档：[JMRTC Android SDK 错误码列表](./im_errorcode_android/#jmrtc-android)


[0]: image/jmrtcFlow.png