#!/usr/bin/python
# -*- coding: UTF-8 -*-
# syn the info of the release


content=open("../zh/JMessage/docs/resources.html", "rb+")

print (content.readline(1))

class info(object):
    version = None
    time = None
    changelog = None
    info = None
    def __init__(self):
        version=None
        time=None
        changelog=None
        info=None

    def get_version(self,version):
        self.version="<li>版本号：{{version}}</li>".replace("{{version}}",version)

    def get_time(self,time):
        self.time="<li>更新时间：{{time}}</li>".replace("{{time}}",time)

    def get_changelog(self,changelog):
        self.changelog="<li>更新内容：{{changelog}}</li>".replace("{{changelog}}",changelog)

    def get_info(self):
        info=self.version+self.time+self.changelog
        self.info='''<ul class="download-info-ul"><div style=" clear:both; visibility:hidden;">{{info}}</ul>'''.replace("{{info}}",info)



class language_info(object):
    language_info=None
    info=None

    def __init__(self):
        language_info=None
        info=None

    def get_language_info(self):
        pass
    def replace_language_info(self):
        pass
