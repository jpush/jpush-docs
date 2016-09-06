#!/usr/bin/env python

import commands
import os
import time

def git_pull():
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/"))
    print (commands.getstatusoutput("git pull origin renew"))
    print ("git pull origin renew")

def set_venv():
    print (os.chdir("/opt/push/jpush-docs/"))
    print (commands.getstatusoutput(". venv/bin/activate"))
    print (". venv/bin/activate")

def build():
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JPush/"))
    print ("JPush/")
    print (commands.getstatusoutput("mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JMessage/"))
    print ("JMessage/")
    print (commands.getstatusoutput("mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JSMS/"))
    print ("JSMS/")
    print (commands.getstatusoutput("mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/Index/"))
    print (commands.getstatusoutput("mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))

set_venv()
git_pull()
build()
print time.asctime(time.localtime(time.time()))








