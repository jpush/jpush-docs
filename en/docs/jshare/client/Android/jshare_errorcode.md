# Definition of JShare SDK ErrorCode 

The ErrorCode in the following list may appear during the calling of SDK. Below is for your reference to understand its meaning.


<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th>Error Message</th>
			<th>Remarks</th>
		</tr>

    <tr>
      <td>40001</td>
      <td>appid missing</td>
      <td>Missing appid parameter</td>
    </tr>
    <tr>
      <td>40002</td>
      <td>appkey missing</td>
      <td>Missing appkey parameter</td>
    </tr>
    <tr>
      <td>40003</td>
      <td>secret missing</td>
      <td>Missing secret parameter</td>
    </tr>
    <tr>
      <td>40004</td>
      <td>mediaType missing</td>
      <td>Missing mediaType parameter</td>
    </tr>
    
    <tr>
      <td>40005</td>
      <td>invalid mediaType</td>
      <td>Invalid mediaType</td>
    </tr>
    <tr>
      <td>40006</td>
      <td>platform missing</td>
      <td>Missing platform parameter</td>
    </tr>
    <tr>
      <td>40007</td>
      <td>invalid platform</td>
      <td>Invalid platform</td>
    </tr>
    <tr>
      <td>40009</td>
      <td>not install app</td>
      <td>Not install the application</td>
    </tr>
    <tr>
      <td>40010</td>
      <td>unfinished initialization</td>
      <td>Not initialize</td>
    </tr>
    <tr>
      <td>40011</td>
      <td>shareParams missing</td>
      <td>Missing shareParams</td>
    </tr>
        <tr>
      <td>40012</td>
      <td>platform haven't  configuration</td>
      <td>Platform is not configured</td>
    </tr>
    <tr>
      <td>41001</td>
      <td>text size out of limit</td>
      <td>Length of text parameter exceeds the limit</td>
    </tr>
    <tr>
      <td>41002</td>
      <td>image url size out of limit</td>
      <td>Length of image link field exceeds the limit</td>
    </tr>
    <tr>
      <td>41003</td>
      <td>image size out of limit</td>
      <td>Image size exceeds the limit</td>
    </tr>
    <tr>
      <td>41004</td>
      <td>url size out of limit	</td>
      <td>Url length exceeds the limit</td>
    </tr>
    <tr>
      <td>41005</td>
      <td>audio url size out of limit</td>
      <td>Length of audio url exceeds the limit</td>
    </tr>
    <tr>
      <td>41006</td>
      <td>video url size out of limit</td>
      <td>Length of video url exceeds the limit</td>
    </tr>
    <tr>
      <td>41009</td>
      <td>file size out of limit</td>
      <td>File size exceeds the limit</td>
    </tr>
    <tr>
      <td>41010</td>
      <td>emotion size out of limit</td>
      <td>Emotion size exceeds the limit</td>
    </tr>
    <tr>
      <td>41011</td>
      <td>title size out of limit</td>
      <td>Title parameter exceeds the limit</td>
    </tr>
    <tr>
      <td>41012</td>
      <td>description size out of limit</td>
      <td>Description parameter exceeds the limit</td>
    </tr>
    <tr>
      <td>41013</td>
      <td>thumb size out of limit</td>
      <td>Thumbnail parameter exceeds the limit</td>
    </tr>
    <tr>
      <td>41014</td>
      <td>image is empty</td>
      <td>Picture parameter is empty</td>
    </tr>
    <tr>
      <td>41015</td>
      <td>audio url is empty</td>
      <td>Audio url parameter is empty</td>
    </tr>
    <tr>
      <td>41016</td>
      <td>video url is empty</td>
      <td>Video url parameter is empty</td>
    </tr>
    <tr>
      <td>41018</td>
      <td>emotion is empty</td>
      <td>Emotion parameter is empty</td>
    </tr>
    <tr>
      <td>41019</td>
      <td>file is empty</td>
      <td>File parameter is empty</td>
    </tr>
    <tr>
      <td>41021</td>
      <td>url is empty</td>
      <td>Url parameter is empty</td>
    </tr>
        <tr>
      <td>41022</td>
      <td>text is empty	</td>
      <td>Text parameter is empty</td>
    </tr>
        <tr>
      <td>41025</td>
      <td>title is empty</td>
      <td>Title parameter is empty</td>
    </tr>
        <tr>
      <td>41026</td>
      <td>invalid url</td>
      <td>Invalid url</td>
    </tr>
        <tr>
      <td>41027</td>
      <td>file not exist</td>
      <td>File does not exist</td>
    </tr>
    <tr>
      <td>41028</td>
      <td>text and url size out of limit</td>
      <td>Length of text and url exceeds limit</td>
    </tr>
    <tr>
      <td>41029</td>
      <td>can't share image and video together</td>
      <td>Can't share pictures and videos at the same time</td>
    </tr>
    <tr>
      <td>42001</td>
      <td>invalid credential</td>
      <td>Invalid credentials </td>
    </tr>
        </tr>
        <tr>
      <td>50001</td>
      <td>get access token error</td>
      <td>Get access token error</td>
    </tr>
        </tr>
        <tr>
      <td>50002</td>
      <td>share failed</td>
      <td>Failed to share</td>
    </tr>
        </tr>
        <tr>
      <td>50003</td>
      <td>get userinfo failed</td>
      <td>Failed to get user information</td>
    </tr>
        </tr>
        <tr>
      <td>50004</td>
      <td>auth failed</td>
      <td>Authorization failed</td>
    </tr>
        </tr>
        <tr>
      <td>50005</td>
      <td>this platform unsupported authorize</td>
      <td>Platform does not support authorization</td>
    </tr>
    
    <tr>
      <td>50006</td>
      <td>Invalid or expired token</td>
      <td>Invalid or expired token</td>
    </tr>
    
    <tr>
      <td>50007</td>
      <td>Unable to verify your credentials</td>
      <td>Unable to verify your credentials</td>
    </tr>
    
    <tr>
      <td>50008</td>
      <td>Internal error</td>
      <td>Unknown internal error occurred</td>
    </tr>
    
    <tr>
      <td>50009</td>
      <td>Status is a duplicate</td>
      <td>Content of this status has been released by verified account</td>
    </tr>
    
</table>
</div>



