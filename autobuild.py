#!/usr/bin/env python
import logging
import commands
import os
import time

def kill_git():
    logging.info(commands.getstatusoutput("kill -s 9 `pgrep git-remote-http`"))
    #logging.info(commands.getstatusoutput("sudo ps -ef |grep downloader.py  |awk '{print $2}'|xargs sudo  kill -9"))

def git_pull():
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/"))
    logging.info(commands.getstatusoutput("git pull origin renew"))
    print ("git pull origin renew")


def build():
    logging.info(os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JPush/"))
    print ("JPush/")
    logging.info (commands.getstatusoutput("/opt/push/jpush-docs/venv/bin/mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))

    logging.info (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JAnalytics/"))
    print ("JAnalytics/")
    logging.info(commands.getstatusoutput("/opt/push/jpush-docs/venv/bin/mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))

    logging.info(os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JMessage/"))
    print ("JMessage/")
    logging.info (commands.getstatusoutput("/opt/push/jpush-docs/venv/bin/mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))

    logging.info (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JSMS/"))
    print ("JSMS/")
    logging.info (commands.getstatusoutput("/opt/push/jpush-docs/venv/bin/mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))

    logging.info (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/Index/"))
    print ("Index/")
    logging.info (commands.getstatusoutput("/opt/push/jpush-docs/venv/bin/mkdocs build"))
    time.sleep(1)
    print time.asctime(time.localtime(time.time()))


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/opt/push/jpush-docs/autobuild.log',
                    filemode='a+')

kill_git()
build()
git_pull()
exit()








