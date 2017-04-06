{% extends "base.md" %}
{% block serversdk %}
<li>
    <div class="auto-download-left">
        <div class="auto-download-image">
            <img src="../image/resource_sdk_{{info_array[info].name}}.png">
        </div>
    </div>
    <div class="auto-download-right">
        <div class="auto-download-title">
            <p>{{info_array[info].languages}} - SDK下载</p>
        </div>
        <div class="auto-download-info">
            <ul class="auto-download-info-ul">
                <li>版本号：{{info_array[info].release_version}}</li>
                <li>更新时间：{{info_array[info].release_time}}</li>
                <li>GitHub：<a href="{{info_array[info].project_url}}">源码获取</a></li>
            </ul>
        </div>
        <div class="auto-download-changelog">
            <ul>
                <li class="auto-changelog-title">
                    <h3>更新内容:{{info_array[info].release_title}}</h3></li>
                    <li><div>{{info_array[info].release_body}}</div></li>
            </ul>
        </div>
      <div class="auto-download-icon">
       <a href="https://www.jiguang.cn/downloads/resource/1459130284033">下载</a>
      </div>
    </div>
    <div class="hr">
       <hr />
    </div>
</li>
{% endblock %}