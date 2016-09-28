#!/usr/bin/python
# -*- coding: UTF-8 -*-
# low couple
# syn module only synchronize the docs.################
# if it went wrong, the auto build module will run all the same.
import requests
import os
import zipfile
import urllib
import time
import dirconfig
import logging
import commands
import os

from githubdownload import GithubDownload
from repositories import repositories
from ziptool import ZipTool

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/opt/push/jpush-docs/syndocs/autosyn.log',
                    filemode='a+')

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

downloader=GithubDownload()
for file_dic in repositories:
     html_content = downloader.get_html(repositories[file_dic]["url"]+"/releases")
     try:
          title = downloader.get_title(html_content)
          logging.info("get title success")
     except:
          logging.info("get title fail")
     zip_url = downloader.get_code(html_content)
     release_time = downloader.get_time(html_content)
     release_version = downloader.get_version(html_content)
     if(not os.path.exists(dirconfig.conf["zip"])):
          os.mkdir(dirconfig.conf["zip"])
     zip_folder=os.path.join(dirconfig.conf["zip"],repositories[file_dic]["name"])
     if(not os.path.exists(zip_folder)):
          os.mkdir(zip_folder)
     zip_dir=downloader.get_dir(name=repositories[file_dic]["name"],version=release_version)
     zip_tool=ZipTool()
     if zip_tool.is_zip_exist(zip_dir):
         logging.info("the file exist,pass")
         logging.info("nothing to push")
     else:
         logging.info("the file do not exist,replace")
         logging.info("git pull,update the local file")
         git_pull()
         zip_tool.zip_download(zip_dir,release_version,repositories[file_dic]["url"])
         zip_tool.unzip_file(repositories[file_dic]["name"],release_version)
         zip_tool.replace_readme(repositories[file_dic]["name"],release_version)
         git_push()
         logging.info("git push,update the remote file")




