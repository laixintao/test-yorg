
from __future__ import unicode_literals

import re

with open('data/200_company_name.xml', 'rw') as f:
    for line in f:
        s = re.search(r'>.{2,}[\u4e00-\u9fa5]+', line)
        if s:
            print s.groups()
