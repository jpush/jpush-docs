#!/usr/bin/python
# -*- coding: UTF-8 -*-
# low couple
# syn module only synchronize the docs.################
# if it went wrong, the auto build module will run all the same.
import sys
import os
import zipfile
import urllib
import time
import dirconfig
import logging
import commands
import os

from jinja2 import Environment, PackageLoader

from githubtool import *
from githubdownload import GithubDownload
from repository import repositories
from ziptool import ZipTool
from syninfo import info
reload(sys)
sys.setdefaultencoding( "utf-8" )

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/opt/push/jpush-docs/syn.log',
                    filemode='a+')


env = Environment(loader=PackageLoader('synpage', 'templates'))
template = env.get_template('index.md')
downloader=GithubDownload()
info_array={}
for file_dic in repositories:
     html_content = downloader.get_html(repositories[file_dic]["url"]+"/releases")
     url = repositories[file_dic]["url"]
     language = repositories[file_dic]["languages"]
     name = repositories[file_dic]["name"]
     try:
         release_title = downloader.get_title(html_content)
         print release_title
         release_body = downloader.get_body(html_content)
         logging.info(release_body)
         logging.info("get title success")
     except:
         logging.info("get title fail")
     zip_url = downloader.get_code(html_content)
     release_time = downloader.get_time(html_content)
     release_version = downloader.get_version(html_content)
     info_array[language] = info(language, name, url, release_version, release_time, release_title, release_body)

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
         #git_push()
         logging.info("git push,update the remote file")


download_page=template.render(info_array=info_array)
page_file=open("../zh/JPush/docs/resources.md",'w')
page_file.write(download_page.decode('utf-8'))
page_file.close()
git_pull()
#git_push()
