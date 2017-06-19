# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from yorg.utils import fully_qualified_func_name
from yorg.contrib.court.chinacourt import get_page_num, parse_detail_page, parse_list_page

URL_BASE = "http://jkxfy.chinacourt.org"
COURT = "交口县人民法院"
URL_LIST = "http://jkxfy.chinacourt.org/article/index/id/MzSoNDBINDAwNCACAAA%3D/page/{}.shtml"
MONGO_NAME = 'shanxi'


def do_parse_detail_page(url):
    parse_detail_page(url, MONGO_NAME, COURT,
                      get_start_time_by='content')


def start_job():
    total_page_num = get_page_num(URL_LIST.format(1))
    for index in range(1, total_page_num + 1):
        page_list_url = URL_LIST.format(index)
        parse_list_page.enqueue(page_list_url, URL_BASE,
                                fully_qualified_func_name(do_parse_detail_page))
