# HTTP 状态码
</br>
</br>
本文档定义 JPush REST API 的 HTTP 返回码规范。  
JPush Push API v3 新版本 API 满足此规范。JPush Report API 也满足此规范。

## 状态码定义

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >Code</th>
			<th >描述</th>
			<th >详细解释</th>
		</tr>
		<tr >
			<td>200</td>
			<td>OK</td>
			<td>Success!</td>
		</tr>
		<tr >
			<td>400</td>
			<td>错误的请求</td>
			<td>该请求是无效的。相应的描述信息会说明原因。</td>
		</tr>
		<tr >
			<td>401</td>
			<td>未验证</td>
			<td>没有验证信息或者验证失败</td>
		</tr>
		<tr >
			<td>403</td>
			<td>被拒绝</td>
			<td>理解该请求，但不被接受。相应的描述信息会说明原因。</td>
		</tr>
		<tr >
			<td>404</td>
			<td>无法找到</td>
			<td>资源不存在，请求的用户的不存在，请求的格式不被支持。</td>
		</tr>
		<tr >
			<td>405</td>
			<td>请求方法不合适</td>
			<td>该接口不支持该方法的请求。</td>
		</tr>
		<tr >
			<td>410</td>
			<td>已下线</td>
			<td>请求的资源已下线。请参考相关公告。</td>
		</tr>
		<tr >
			<td>429</td>
			<td>过多的请求</td>
			<td>请求超出了频率限制。相应的描述信息会解释具体的原因。</td>
		</tr>
		<tr >
			<td>500</td>
			<td>内部服务错误</td>
			<td>服务器内部出错了。请联系我们尽快解决问题。</td>
		</tr>
		<tr >
			<td>502</td>
			<td>无效代理</td>
			<td>业务服务器下线了或者正在升级。请稍后重试。</td>
		</tr>
		<tr >
			<td>503</td>
			<td>服务暂时失效</td>
			<td>服务器无法响应请求。请稍后重试。</td>
		</tr>
		<tr >
			<td>504</td>
			<td>代理超时</td>
			<td>服务器在运行，但是无法响应请求。请稍后重试。</td>
		</tr>
	</table>
</div>


## 遵守的规范

+ 200 一定是正确。所有异常都不使用 200 返回码
+ 业务逻辑上的错误，有特别的错误码尽量使用 4xx，否则使用 400。
+ 服务器端内部错误，无特别错误码使用 500。
+ 业务异常时，返回内容使用 JSON 格式定义 error 信息。

## 文档参考

+ [Twitter Status Codes](http://docs.jpush.cn/display/dev/HTTP-Status-Code)
+ [Wikipedia HTTP Status Codes](http://wiki.jpushoa.com/display/KKPush/2013/04/16/Wikipedia+HTTP+Status+Codes)



