import requests
import os
import zipfile
import urllib
import time
import dirconfig
import logging
import commands
import sys
import var_dump

from jinja2 import Environment, PackageLoader

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

env = Environment(loader=PackageLoader('syn', 'templates'))
template = env.get_template('index.md')

info_array={}

downloader = GithubDownload()

for project in repositories:
    html_content = downloader.get_html(repositories[project]["url"] + "/releases")
    url=repositories[project]["url"]
    language= repositories[project]["languages"]
    name=repositories[project]["name"]
    try:
        release_title = downloader.get_title(html_content)
        print release_title
        release_body=downloader.get_body(html_content)
        logging.info(release_body)
        logging.info("get title success")
    except:
        logging.info("get title fail")
    zip_url = downloader.get_code(html_content)
    logging.info(zip_url)
    release_time = downloader.get_time(html_content)
    logging.info(release_time)
    release_version = downloader.get_version(html_content)
    info_array[language]=info(language,name,url,release_version,release_time,release_title,release_body)
    #print release_version

download_page=template.render(info_array=info_array)
page_file=open("../zh/JPush/docs/resources.md",'w')
page_file.write(download_page.decode('utf-8'))
page_file.close()


