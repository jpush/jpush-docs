# HTTP 状态码

本文档定义 JPush REST API 的 HTTP 返回码规范。

JPush Push API v3 新版本 API 满足此规范。JPush Report API 也满足此规范。

### 状态码定义

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th style="padding: 0 5px;text-align:center;" >Code</th>
			<th style="padding: 0 5px;text-align:center;" >描述</th>
			<th style="padding: 0 5px;" >详细解释</th>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">200</td>
			<td style="padding: 0 5px;text-align:center;">OK</td>
			<td style="padding: 0 5px;">Success!</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">400</td>
			<td style="padding: 0 5px;text-align:center;">错误的请求</td>
			<td style="padding: 0 5px;">该请求是无效的。相应的描述信息会说明原因。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">401</td>
			<td style="padding: 0 5px;text-align:center;">未验证</td>
			<td style="padding: 0 5px;">没有验证信息或者验证失败</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">403</td>
			<td style="padding: 0 5px;text-align:center;">被拒绝</td>
			<td style="padding: 0 5px;">理解该请求，但不被接受。相应的描述信息会说明原因。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">404</td>
			<td style="padding: 0 5px;text-align:center;">无法找到</td>
			<td style="padding: 0 5px;">资源不存在，请求的用户的不存在，请求的格式不被支持。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">405</td>
			<td style="padding: 0 5px;text-align:center;">请求方法不合适</td>
			<td style="padding: 0 5px;">该接口不支持该方法的请求。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">410</td>
			<td style="padding: 0 5px;text-align:center;">已下线</td>
			<td style="padding: 0 5px;">请求的资源已下线。请参考相关公告。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">429</td>
			<td style="padding: 0 5px;text-align:center;">过多的请求</td>
			<td style="padding: 0 5px;">请求超出了频率限制。相应的描述信息会解释具体的原因。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">500</td>
			<td style="padding: 0 5px;text-align:center;">内部服务错误</td>
			<td style="padding: 0 5px;">服务器内部出错了。请联系我们尽快解决问题。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">502</td>
			<td style="padding: 0 5px;text-align:center;">无效代理</td>
			<td style="padding: 0 5px;">业务服务器下线了或者正在升级。请稍后重试。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">503</td>
			<td style="padding: 0 5px;text-align:center;">服务暂时失效</td>
			<td style="padding: 0 5px;">服务器无法响应请求。请稍后重试。</td>
		</tr>
		<tr >
			<td style="padding: 0 5px;text-align:center;">504</td>
			<td style="padding: 0 5px;text-align:center;">代理超时</td>
			<td style="padding: 0 5px;">服务器在运行，但是无法响应请求。请稍后重试。</td>
		</tr>
	</table>
</div>


### 遵守的规范

+ 200 一定是正确。所有异常都不使用 200 返回码
+ 业务逻辑上的错误，有特别的错误码尽量使用 4xx，否则使用 400。
+ 服务器端内部错误，无特别错误码使用 500。
+ 业务异常时，返回内容使用 JSON 格式定义 error 信息。

### 文档参考

+ [Twitter Status Codes](http://docs.jpush.cn/display/dev/HTTP-Status-Code)
+ [Wikipedia HTTP Status Codes](http://wiki.jpushoa.com/display/KKPush/2013/04/16/Wikipedia+HTTP+Status+Codes)



