# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pymongo
import re
from xml.sax import handler, parseString
import random

mongo_client = pymongo.MongoClient()
db_coll = mongo_client['com200']['test']


class CompanyHandler(handler.ContentHandler):
    def __init__(self):
        self.number = ""
        self.name = ""
        self.counter = 0
        self.parse_content = False
        self.has_number = False

    def startElement(self, name, attr):
        if name == 'ss:Row':
            self.number = ""
            self.name = ""
            self.parse_content = True

            
    def characters(self, content):
        print content
        content = content.strip()
        if content:
            print content
            if not self.has_number:
                self.number = content
                self.has_number = True
            else:
                self.name = content

    def endElement(self, name):
        if name == 'ss:Row':
            self.parse_content = False
            db_coll.update_one({'code': self.number},
                    {'$set': {'code':self.number, 'company': self.name, 'random': random.randint(0,20)}},
                               upsert=True)
            self.number = ""
            self.name = ""
            self.counter += 1
            self.has_number = False
            if self.counter % 100 == 0 :
                print self.counter


if __name__ == '__main__':
    with open('test.xml', 'r') as com_file:
        parseString(com_file.read(), CompanyHandler())
