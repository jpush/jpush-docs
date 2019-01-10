# Windows Phone API

### API Overview
APIs are mainly concentrated in the class JServer of the namespace JPushSDK
Property-IsDebug
Turn on debugging mode to help understand the integration and print the relevant log. `Close the debug mode when publishing to the store, otherwise it will not be approved by the Microsoft App Store`.

#### Support Version
Starting to support v1.0.0

  public static  bool  IsDebug{get;set;}
#### Parameter Description
- IsDebug=true Turn on debug mode
- IsDebug=false Turn off debug mode

#### Method - Setup

Call this API to escalate APP_KEY to JPush backend

##### Supported Versions
Starting to support v1.0.0

##### Interface Definition
  public  static void  Setup(string APP_KEY, string CHANNEL,Action<string> action)
  
##### Parameter Description
- APP_KEY
    - appkey generated after registering the application on JPush Portal
-  CHANNEL
    - As a release of the application, you can define it yourself
- action
    - Call this callback function after successfully obtaining the RegistrationID 
    void registationIDCallback(string registrationID) 
    {
          Debug.WriteLine(registrationID); 
    }
#### Method -Activated
The application enters the call of the Activated state to correctly handle the Tomstoning state.

##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public  static void Activated()

#### Method-Deactiveted
The application enters the call of Deactivated state and is used to properly save the application's exit status
##### Supported Version
Starting to support v1.0.0

#### Interface Definition
public  static void Deactivated()


### JPush SDK Status and MPNs Notification
Register events in the JPush SDK to monitor the operation of the JPush SDK and receive messages sent by the MPNs
#### Supported Version
Starting to support v1.0.0
#### Interface Definition
    public static void AddNotification(string name, Action<Dictionary<string, string>> selector)
#### Parameter Description
- name
    - The type of messages monitored, the JPush SDK provides the following 5 types
    - NotificationCenter.kNetworkDidSetupNotification - Establish connection
    - NotificationCenter.kNetworkDidRegisterNotification - Login success
    - NotificationCenter.kNetworkDidLoginNotification - Register success
    - NotificationCenter.kNetworkDidCloseNotification - Close connection
    - NotificationCenter.kNetworkDidMPNsMessageNotification- Receive MPNs messages
- selector
    - Trigger the callback function when an event occurs
    - Dictionary with a RegistrationID when kNetworkDidSetupNotification
    - Dictionary with a MPNs message when kNetworkDidSetupNotification

#### Sample Code
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


### Enable, Query and Stop MPNs Push Function
API descriptions related to Windows Phone push
#### Method - RegisterNotification
Interface for registering MPNs service. Use this interface when customizing the pop-up window that the user could push. `After the user closes the MPNs notification, call this function if the notification is turned on again. Cannot call RegisterNotificationWithMessagebox`
##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public static void RegisterNotification()

#### Method - RegisterNotificationWithMessagebox
Register MPNs interface to help manage pop-up messagebox for the initial registration, and save the user selection status
##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public  static void RegisterNotificationWithMessagebox(string content, string title, Action<bool> callBack)
##### Parameter Description
- content
    - The content of the popup
- title
    - The title of the popup
- callBack + callback function informs the user of the result
#### Method-CloseNotification

Turn off MPNs push

##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public  static void CloseNotification()
#### Method-IsOpneNotification
Check if MPNs are turned on

##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public static bool IsOpneNotification()


### API Tags and Alias ​​APIs
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
 <p>Tips, please pay attention to deal with the call back results when setting the label alias.
 <p>Only if the value returned by call back is 0, the setting is successful and the target can be pushed. Otherwise the server API will return a 1011 error.
</div>

Provide related APIs for setting aliases and tags.

The API can be called anywhere in the app.

#### Alias
For the user who installed the application, identify them by aliases. Then they can be specified with this alias when the Push message is given to this user later,.

Each user can only specify one alias.

Within the same application, different aliases are recommended for different users. In this way, users are uniquely identified based on their aliases.

The system does not restrict one alias to only one user. If an alias is assigned to more than one user, the server-side API will send messages to multiple users when specifying the alias.

Example: In a game where the user wants to log in, it is possible to set the alias userid. If you found that the user has not played the game for 3 days, Then, call the server API to notify the client of the user's notification based on the userid.

#### Tag
Label the user who installed the application. Its purpose is mainly to facilitate developers to deliver Push messages in batches according to labels.
Multiple tags can be played for each user.
Example: game, old_page, women

#### Method - SetTagsWithAlias(with Callback)
Call this API to set up aliases and tags at the same time, and support the callback function.
It needs to be understood that this interface is overlay logic, not incremental logic. That is, the new call will overwrite the previous setting.
After the previous call, if you need to rechange the alias and label, you only need to call this API again.

##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public static void  SetTagsWithAlias(HashSet<string> tags, string alias, Action<int, HashSet<string>, string> callback)
##### Parameter Description
- tags
    - null -This value is not set for this call
    - An empty set represents to cancel the previous setting
    - Set at least one tag per call, overwriting previous settings, but not adding new settings.
    - Valid label components: letters (case-sensitive), numbers, underscores, and Chinese characters.
    - Restrictions: Each tag is limited to a 40-byte named length and supports up to 100 tags, but the total length must not exceed 1K bytes. (UTF-8 encoded is required to determine the length)
    - A single device supports up to 100 tags. There is no limit to the number of App global tags.
- alias
    - null - This call does not set this value.
    - An empty string ("") indicates the previous setting was canceled.
    - Each call sets a valid alias, overwriting previous settings.
    - Valid aliases are composed of letters (case-sensitive), numbers, underscores, and Chinese characters.
    - Limitation: The alias name length is limited to 40 bytes. (UTF-8 encoded is required to determine the length)
- callbackSelector
    - null - Callback is not required for this call.
    - Used to return the corresponding parameters alias, tags, and  return the corresponding status code: 0 is successful, for other return code, please refer to the definition of error code.
    
        private void TagsAliasCallBack(int resultCode, HashSet<string> tags, string alias);
    

#### Method - FilterValidTags
Used to filter out the correct and available tags

If the total number exceeds the maximum limit, the maximum number of top and available tags is returned.
<div style="font-size:13px;background: #E0EFFE;border: 1px solid #ACBFD7;border-radius: 3px;padding: 8px 16px; padding-bottom: 0;margin-bottom: 0;">
 <p>Recommendations: 
 	<br>
<p>When tags are set, if one of the tags is invalid, the entire setup process fails.
<br>
<p>If the app tags are set dynamically during the run and there are invalid characters specified in the JPush SDK tag, it is possible that an invalid tag results in the failure of all tag updates in this call.
 <br>
 <p>At this point, you can call this method FilterValidTags to filter out invalid tags, get valid tags, and then call the JPush SDK's set tags / alias method.
</div>




##### Supported Version
Starting to support v1.0.0

##### Interface Definition
public static HashSet<string> FilterValidTags(HashSet<string> tags)

##### Parameter Description
- tags
    - Original tag collection
##### Interface Return
A valid tag collection

##### Definition of Error Code

<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >Description</th>
      <th >详细解释</th>
    </tr>
    <tr >
      <td>6001</td>
      <td>Invalid setting, tag/alias should not be null</td>
      <td></td>
    </tr>
    <tr >
      <td>6002</td>
      <td>Set timeout</td>
      <td>Recommend to try again</td>
    </tr>
    <tr >
      <td>6003</td>
      <td>Alias string is illegal </td>
      <td>Valid aliases and labels are composed of letters (case-sensitive), numbers, underscores, and Chinese characters.</td>
    </tr>
    <tr >
      <td>6004</td>
      <td>Alias is too long. Up to 40 bytes</td>
      <td>Chinese UTF-8 is 3 bytes</td>
    </tr>
    <tr >
      <td>6005</td>
      <td>One of the tag strings is illegal</td>
      <td>Valid aliases and labels are composed of letters (case sensitive), numbers, underscores, and Chinese characters. </td>
    </tr>
    <tr >
      <td>6006</td>
      <td>One tag is extremely long. One tag up to 40 bytes</td>
      <td>Chinese UTF-8 is 3 bytes</td>
    </tr>
    <tr >
      <td>6007</td>
      <td>The number of tags exceeds the limit. Up to 100</td>
      <td>This is the limitation of a device. There is no limit to the number of tags that can be applied globally.</td>
    </tr>
    <tr >
      <td>6008</td>
      <td>tag 超出总长度限制</td>
      <td>总长度最多 1K 字节</td>
    </tr>
    <tr >
      <td>6011</td>
      <td>Tag exceeds total length limit</td>
      <td>Total length up to 1K bytes</td>
    </tr>
  </table>
</div>

### Statistics Function
Used to counting of Toast clicks, page switching and other events

#### Method-HandleToastNotification
Used to count the events that click on the Toast notification to enter the application. It needs to be put into the page corresponding to the Toast notification and the default page, such as the MainPage.xaml page.
##### Supported Version
Starting to support v1.0.0

##### Interface Definition
    public static void HandleToastNotification(IDictionary<string, string> remotoInfo)

##### Parameter Description
- remoteInfo
    - When the page is switched, obtained by the interface of wp 8 sdk: NavigationContext.QueryString

#### Method-TrackPageInto

Used to count the events that the user enters into the page. This function is added to OnNavigatedTo which needs the statistics page.

##### Supported Version
Starting to support v1.0.0

##### Interface Definition
    public static void TrackPageInto(string pageName)
##### Parameter Description
- pageName
    - page name

#### Method-TrackPageOut
Used to count the events of the user leaving the page. This function is added to OnNavigatedFrom of the page that needs statistics.

##### Supported Version
Starting to support V1.0.0

##### Interface Definition
    public static void TrackPageOut(string pageName)
##### Parameter Description
- pageName
    - page name


### Obtain RegistrationID
This API is in the class JServer of the namespace JPushSDK

#### Method-GetRegisrtationID
Get RegistrationID. Return empty string before successful login, and return RegistrationID after successful registration. 

##### Supported Version
Starting to support V1.0.0

##### Interface Definition
public static string   GetRegisrtationID()


### Definition of Client Error Code
<div class="table-d" align="center" >
  <table border="1" width = "100%">
    <tr  bgcolor="#D3D3D3" >
      <th >Code</th>
      <th >Description</th>
    </tr>
    <tr >
      <td>1008</td>
      <td>AppKey is illegal</td>
    </tr>
    <tr >
      <td>1009</td>
      <td>There is no WinPhone application created under the current appkey. Please go to the official website to check the application details of this application.</td>
    </tr>
  </table>
</div>