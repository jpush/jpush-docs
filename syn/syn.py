import requests
import os
import zipfile
import urllib
import time
import dirconfig
import logging
import commands
import os
from jinja2 import Environment, PackageLoader

from githubdownload import GithubDownload
from repositories import repositories
from ziptool import ZipTool
from syninfo import info
env = Environment(loader=PackageLoader('syn', 'templates'))
template = env.get_template('index.md')
#print template.render(the='variables', go='here')

infos={}

downloader = GithubDownload()
for project in repositories:
    html_content = downloader.get_html(repositories[project]["url"] + "/releases")
    print repositories[project]["url"]
    try:
        release_title = downloader.get_title(html_content)
        logging.info("get title success")
    except:
        logging.info("get title fail")
    zip_url = downloader.get_code(html_content)
    print zip_url
    release_time = downloader.get_time(html_content)
    print release_time
    release_version = downloader.get_version(html_content)
    print release_version

