#!/usr/bin/python
# -*- coding: UTF-8 -*-
# github tool to auto git push git pull
import requests
import os
import zipfile
import urllib
import time
import dirconfig
import logging
import commands
import os

def git_push():
    print (os.chdir("/opt/push/jpush-docs/syndocs/jpush-docs/"))
    add_result= (commands.getstatusoutput("git add ."))
    commit_result=(commands.getstatusoutput('git commit -m "new jpush doc from the github"'))
    push_result= (commands.getstatusoutput("git push origin renew"))
    logging.info(add_result)
    logging.info(commit_result)
    logging.info(push_result)
    if(push_result[0]):
        print ("fail")
        reset_result=commands.getstatusoutput("git reset --hard HEAD^")
        logging.info(reset_result)
    else:
        print ("success")
        logging.info("git push origin renew")

def git_pull():
    print time.asctime(time.localtime(time.time()))
    print (os.chdir("/opt/push/jpush-docs/syndocs/jpush-docs/"))
    logging.info(commands.getstatusoutput("git pull origin renew"))
    print ("git pull origin renew")