# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
import pymongo

mongo_client = pymongo.MongoClient()
db_coll = mongo_client['com200']['com200']


def matching(name, hits):
    index = 0
    for hit in hits:
        h_name = hit['_source']['name']
        if name == h_name:
            return 'name_match', index
        index += 1
    index = 0
    for hit in hits:
        for fname in hit['_source'].get('former_name', []):
            if fname == name:
                return 'former_name_match', index
        index += 1

    index = 0
    print name, '->',
    name = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",name)
    print name
    for hit in hits:
        h_name = hit['_source']['name']
        h_name = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",h_name)
        if name == h_name:
            return 'name_match_nc', index
        index += 1
    index = 0
    for hit in hits:
        for fname in hit['_source'].get('former_name', []):
            h_name = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",fname)
            if h_name == name:
                return 'former_name_match_nc', index
        index += 1
    return 'not_match', -1

    


one_company = db_coll.find({'total_result': {'$gte': 50}})
counter = one_company.count()
for com in one_company:
    print counter
    counter -= 1
    hits = com['query_result'].get('hits')
    if not hits:
        print "no hits"
        continue
    com['total_result'] = hits['total']
    com['is_matched'] = True
    if hits['total'] == 0:
        com['match_type'] = 'not_match'
        com['match_result'] = -1
        db_coll.save(com)
        continue
    else:
        mtype, index = matching(com['company'], hits['hits'])
    com['match_type'] = mtype
    com['match_result'] = index
    print com['company'], mtype, index
    if mtype != 'not_match':
        com['is_match_success'] = True
        com['reg_no'] = hits['hits'][index]['_source'].get('reg_no')
        com['uscc'] = hits['hits'][index]['_source'].get('uscc')
    db_coll.save(com)
