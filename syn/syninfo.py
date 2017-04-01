#!/usr/bin/python
# -*- coding: UTF-8 -*-
# syn the info of the release

class info(object):
    release_version = None
    release_time = None
    release_title = None
    release_body = None

    def __init__(self,release_version,release_time,release_title,release_body):
        self.release_version = release_version
        self.release_time = release_time
        self.release_title = release_title
        self.release_body = release_body

