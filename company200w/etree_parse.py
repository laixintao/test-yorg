# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from lxml import etree

xml = 'data/200_company_name.xml'

doc = etree.parse(xml)

for d in doc.xpath('//ss//'):
    print d.text_content()

