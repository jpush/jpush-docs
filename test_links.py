#!/usr/bin/env python
import os
import time
import yaml
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

current = os.path.split(os.path.realpath(__file__))[0]
yaml_file = "{0}/mkdocs.yml".format(current)
mkdocs = yaml.load(open(yaml_file))['pages']
host='http://127.0.0.1:8000'
page_filters = [
    'index.md',
    'resources.md',
    'updates.md',
    'javadoc.md',
    'iOSdoc.md',
    'server/sdk',
]

link_filters = [
    'mailto:',
    'im_android_api_docs',
    'jmessage_ios_appledoc_html',
    'www.mkdocs.org',
    # 'www.jiguang.cn',
    # 'blog.jiguang.cn',
    'sdkfiledl.jiguang.cn',
    # 'developer.apple.com',
    'developer.android.com',
    'google.com',
    'wikipedia.org',
    # 'github.com',

    'api.jpush.cn',
    'report.jpush.cn',
    'device.jpush.cn',
    'admin.jpush.cn',

    'api.im.jpush.cn',
    'report.im.jpush.cn',
    'api.sms.jpush.cn',
]

def extract_value_from_list(mkdocs):
    pages = []
    for product in mkdocs:
        for item in product.values():
            if isinstance(item, str):
                pages.append(item)
            else:
                page = extract_value_from_list(item)
                pages.extend(page)
    return pages


def is_valid_page(item):
    return _is_valid(page_filters, item)

def is_valid_link(item):
    if not item or item.startswith('#'):
        return False
    return _is_valid(link_filters, item)

def _is_valid(filters, item):
    for filter in filters:
        if filter in item:
            return False
    return True

def build_link(base, path):
    if path.startswith('../') or path.startswith('./'):
        return urljoin(base, path)
    return path

def get_links(url):
    links = []
    html = requests.get(url)
    bs = BeautifulSoup(html.content, 'html.parser')
    for link in bs.find('div', { 'id': 'content' }).findAll('a'):
        if 'href' in link.attrs and is_valid_link(link.attrs['href']):
            links.append({'text': link.get_text(), 'href': link.attrs['href']})
    return links


if __name__ == '__main__':
    pages = extract_value_from_list(mkdocs)
    for page in pages:
        msg = "\nworking on " + page + ":\n"
        if is_valid_page(page):
            url = host+'/'+page.replace('.md', '/')
            msg += 'url: ' + url + "\n"

            links = get_links(url)
            if links:
                for link in links:
                    l = build_link(url, link['href'])
                    r = requests.get(l)
                    if r.status_code != 200:
                        print(msg + link['href'] + ' =>  ' + l)
                        print(link)
                        print(r.status_code)
                # time.sleep(1)
            else:
                pass
                # print("This page doesn't have valid links")
        else:
            pass
            # print("skip...")
