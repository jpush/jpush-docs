# HTTP Status Code

This document defines the specification of HTTP return code for the JPush REST API.
The new version of the JPush Push API v3 API meets this specification. The JPush Report API also satisfies this specification.

## Definition of Status Code 

<div class="table-d" align="center" >
    <table border="1" width = "100%">
        <tr  bgcolor="#D3D3D3" >
            <th >Code</th>
            <th >Description</th>
            <th >Detailed Explanation</th>
        </tr>
        <tr >
            <td>200</td>
            <td>OK</td>
            <td>Success!</td>
        </tr>
        <tr >
            <td>400</td>
            <td>Wrong Request</td>
            <td>This request is invalid. The corresponding description information will explain the reason.</td>
        </tr>
        <tr >
            <td>401</td>
            <td>Unverified</td>
            <td>No verification information or verification failed</td>
        </tr>
        <tr >
            <td>403</td>
            <td>Rejected</td>
            <td>Understand the request but it is not accepted. The corresponding description information will explain the reason.</td>
        </tr>
        <tr >
            <td>404</td>
            <td>Not Found</td>
            <td>The resource does not exist, the requested user does not exist, and the format of the request is not supported.</td>
        </tr>
        <tr >
            <td>405</td>
            <td>Unsuitable request method</td>
            <td>The interface does not support requests for this method.</td>
        </tr>
        <tr >
            <td>410</td>
            <td>Has been offline</td>
            <td>The requested resource has gone offline. Please refer to the relevant announcement.</td>
        </tr>
        <tr >
            <td>429</td>
            <td>Excessive requests</td>
            <td>The request exceeded the frequency limit. The corresponding description information will explain the specific reason.</td>
        </tr>
        <tr >
            <td>500</td>
            <td>Internal service error</td>
            <td>There was an error inside the server. Please contact us to solve the problem as soon as possible.</td>
        </tr>
        <tr >
            <td>502</td>
            <td>Invalid proxy</td>
            <td>The business server is offline or upgrading. Please try again later.</td>
        </tr>
        <tr >
            <td>503</td>
            <td>Temporary service failure</td>
            <td>The server could not respond to the request. Please try again later.</td>
        </tr>
        <tr >
            <td>504</td>
            <td>Agent timeout</td>
            <td>The server is running, but it cannot respond to the request. Please try again later.</td>
        </tr>
    </table>
</div>

## Compliance with the specifications

+ 200 must be correct. Do not use 200 return codes for all exceptions
+ Errors in business logic. Use 4xx as much as possible if there are special error codes, otherwise use 400.
+ Internal server error. Use 500 if there is no special error code.
+ When the business is abnormal, the returned content defines the error information by using the JSON format.

## Documentation Reference
+ [Twitter Status Codes](https://dev.twitter.com/overview/api/response-codes)
+ [Wikipedia HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)