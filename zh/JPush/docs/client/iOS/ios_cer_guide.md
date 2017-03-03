# iOS 证书设置指南

## 创建应用程序ID

+ 登陆 [苹果开发者网站](https://developer.apple.com/) 进入开发者账户。

![go_to_account_page](../image/1_goToAccountPage.png)

+ 从开发者账户页面左侧入口进入“Certificates, IDs & Profiles” 页面。

![go_to_cert_page](../image/2_goToCertPage.png)

+ 创建 App ID，填写 App ID 的 NAME 和 Bundle ID（如果 ID 已经存在可以直接跳过此步骤）。

![appid_add](../image/6.5_appid_add.png)
![appid_name](../image/7_appid_name.png)

	注: 此处需要指定具体的 Bundle ID 不要使用通配符。
![appid_suffix](../image/8_appid_suffix.png)

+ 为 App 开启 Push Notification 功能。如果是已经创建的 App ID 也可以通过设置开启 Push Notification 功能。

![appid_service](../image/9_appid_service.png)

+ 填写好以上属性后，点击 “Continue”，确认 AppId 属性的正确性，点击 “Register”，注册 AppId 成功。

## 两种鉴权方式的配置

### 方式一：通过 .p12 证书鉴权

+ 如果你之前没有创建过 Push 证书或者是要重新创建一个新的，请在证书列表下面新建。

![go_to_add_cert](../image/10_toAddCert.png)

+ 新建证书需要注意选择 APNs 证书种类。如图 APNs 证书有开发（Development）和生产（Production）两种。

	注：开发证书用于开发调试使用；生产证书既能用于开发调试，也可用于产品发布。此处我们选择生产证书为例。
	
![cert_type](../image/11_certType.png)

+ 点击 "Continue", 之后选择该证书准备绑定的 AppID。

![cert_to_app](../image/12_certToApp.png)

+ 点击 “Continue”，会进入 CSR 说明界面。

![require_CSR](../image/13_needCSR.png)

+ 再点 “Continue” 会让你上传 CSR 文件。

![update_CSR](../image/14_uploadCSR.png)

+ 打开系统自带的 KeychainAccess 创建 Certificate Signing Request。如下图操作：

![](../image/Screenshot_13-4-1_5_22.png)

+ 填写“User Email Address”和“Common Name” 后选择 Saved to disk 进行保存 。

![](../image/Snip20140122_7.png)

+ 回到浏览器中 CSR 上传页面，上传刚刚生成的后缀为 .certSigningRequest 的文件。
+ 生成证书成功后，点击 “Download” 按钮把证书下载下来，是后缀为 .cer 的文件。

![cert_ready](../image/15_CertReady.png)

+ 双击证书后，会在“KeychainAccess”中打开，选择左侧“钥匙串”列表中“登录”，以及“种类”列表中“我的证书”，找到刚才下载的证书，并导出为 .p12 文件。如下图：

![output_p12](../image/16_toP12.png)
![save_p12](../image/17_saveP12.png)

+ 在极光控制台上，进入你应用的应用设置中 iOS 的鉴权方式选择 “证书”，上传刚才导出的 .p12 证书。极光会在后台为你的应用进行鉴权。

### 通过 APNs Auth Key 鉴权

+ 首先回到 “Certificates, IDs & Profiles” 页面。点击 “APNs Auth Key” 看账户中是否已有 auth key，没有则点击 “+” 新建。

![go_to_add_auth_key](../image/3_goToAddAuthKey.png)

+ 证书类型选择为 Authentication Key。 （注：在开发和生产环境均可使用，且不会过期。）

![create_auth_key](../image/4_createAuthKey.png)

+ 点击 “Continue” 进入 Auth Key 详情页将证书下载下来，并获取 Key ID（注意：只可以下载一次，下载后妥善保存）

![auth_key_ready](../image/5_authKeyReady.png)

+ 在账户的 “Membership” 页面获取 Team ID

![team_id](../image/6_getTeamId.png)

+ 在极光控制台上，进入你应用的应用设置中 iOS 的鉴权方式选择 “Authentication Key”，上传 auth key 文件，并填写你的 KEY ID，TeamID，和指定应用的 BundleID。极光会在后台为你的应用进行鉴权。

## Provisioning Profile的创建

+ 创建Provisioning Profile的前提，已在Apple Developer网站创建待发布应用所使用的Bundle ID的App ID，且为该App ID创建了APNs证书，如下图:

![jpush_ios](../image/appidcer.png)


+ 创建App ID、APN证书和p12证书的导出的具体步骤请看 :[iOS 证书 设置指南](#id)

+ 在[苹果开发者账号的Provisioning Profile](https://developer.apple.com/account/ios/profile/profileList.action)页面点击下图按钮，创建Provisioning Profile

![jpush_ios](../image/provision_profile.png)

+ 选择此Provisioning Profile的环境后点击[Continue]：

![jpush_ios](../image/create_pp_type.png)

+ 选择要创建Provisioning Profile的App ID后点击[Continue]：

![jpush_ios](../image/pp_appid_new.png)

+ 选择所属的开发者证书，（这里创建了多个开发者证书，建议只创建一个，方便管理）为了方便，选择了[Select All]，再点击[Continue]进入下一步：

![jpush_ios](../image/select_cer.png)

+ 为该Provisioning Profile选择将要安装的设备（一般选择[Select All]），点击[Continue]:

![jpush_ios](../image/select_devices.png)

+ 给该Provisioning Profile填写Profile Name，点击[generate]完成创建。

![jpush_ios](../image/pp_name.png)

+ 填写完Profile Name后点击[generate]完成创建，之后点击[DownLoad]下载Provisioning Profile

![jpush_ios](../image/download_pp.png)

+ 双击下载下来的Provisioning Profile，添加到xcode。

## XCode的证书配置教程

参照[iOS SDK 集成指南](ios_guide_new/)集成JPush SDK 和上传了推送用到的p12证书后在编译运行前需要先配置一下证书，步骤如下：

+ 打开xxx-info.plist的Bundle identifier项把上传到JPush 控制台的bundle id填写进去：

![jpush_ios](../image/xcode_bundle.png)

+ 点击项目，选择目标TARGETS后进入Build Setting 界面，搜索“Code signing”，按照下图配置

![jpush_ios](../image/xcode_buildsettings_cs.png)


