# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import re
import pymongo
import requests
import traceback
import random

import logging
logger = logging.getLogger('requests_worder')
hdlr = logging.FileHandler('worker.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

mongo_client = pymongo.MongoClient()
db_coll = mongo_client['com200']['com200']
headers = {
    'Origin': 'http://aws-9000.bosondata.net:9000',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2,de;q=0.2,ko;q=0.2,mt;q=0.2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://aws-9000.bosondata.net:9000/_plugin/head/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}


one_companys = db_coll.find({'total_result': {'$gte': 50}})
counter = one_companys.count()
for one_company in one_companys:
    print counter
    counter -= 1
    print one_company['company']
    # if re.match("[^\u4e00-\u9fa5]+$", one_company['company_new']):
    #     one_company['company'] = one_company['company_new']
    # else:
    #     one_company['company'] = re.sub(r'^[0-9A-Z]+', '', one_company['company_new'], count=1)
    # print one_company['company'], counter, '\n', one_company['company_new'], '\n\n'
    # db_coll.save(one_company)
    # continue
    data = '''{
               "query": {
                        "term": {
                                   "name.raw": "''' +one_company['company']+'''"
                                        }
                                           }
                                            }'''
    resp = requests.post('http://aws-9000.bosondata.net:9000/_search', headers=headers,
                         data=data.encode('utf-8'))
    one_company['is_queried'] = True
    one_company['is_term'] = True
    one_company['query_result'] = resp.json()
    db_coll.save(one_company)
