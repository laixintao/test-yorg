#!/env/python
# -*- coding: utf-8 -*-

import csv


csv_file = open('company200w_0615b.csv', 'w')
writer = csv.writer(csv_file)

writer.writerow(['公司名', '原文件中的序号', '统一社会信用代码', '注册号'])

import pymongo
mongo_client = pymongo.MongoClient()
db_coll = mongo_client['com200']['com200']

companys = db_coll.find()
counter = companys.count()
for com in companys:
    name = com['company']
    code = com['code']
    uscc = com.get('uscc') or ''
    reg_no = com.get('reg_no') or ''
    writer.writerow(
            [name.encode('utf-8'),
            code.encode('utf-8'),
            uscc.encode('utf-8'),
            reg_no.encode('utf-8')])
    if counter % 1000 == 0:
        print counter
    counter -= 1

csv_file.close()
