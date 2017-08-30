# -*- coding: utf-8 -*-

import beanstalkc

bt = beanstalkc.Connection()

tubes = bt.tubes()

for tube in tubes:
    print "{}\t{}".format(bt.stats_tube(tube)['total-jobs'], tube)
