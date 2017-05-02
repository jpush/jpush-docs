#!/usr/bin/python
# -*- coding: UTF-8 -*-
# syn the info of the release

class info(object):
    release_version = None
    release_time = None
    release_title = None
    release_body = None
    name=None
    languages=None
    project_url = None

    def __init__(self,languages=None,name=None,project_url=None,release_version=None,release_time=None,
                 release_title=None,release_body=None):
        self.release_version = release_version
        self.release_time = release_time
        self.release_title = release_title
        self.release_body = release_body
        self.name=name
        self.project_url=project_url
        self.languages=languages

