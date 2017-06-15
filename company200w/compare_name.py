# -*- coding: utf-8 -*-

import pymongo
import thread

mongo = pymongo.MongoClient()

old_db = mongo['com200']['com200']
new_db = mongo['com200']['company2']

def compare_name():
    new_companys = new_db.find({'is_checked': None})
    counter = new_companys.count()
    for new_company in new_companys:
        print "thread has {} left".format(counter)
        counter -= 1
        old_company = old_db.find_one({'code': new_company['code']})
        if new_company['company'] == old_company['company']:
            pass
        else:
            old_company['company_new'] = new_company['company']
            old_company['is_wrong'] = True
            old_db.save(old_company)
        new_company['is_checked'] = True
        new_db.save(new_company)


if __name__ == '__main__':
    compare_name()
