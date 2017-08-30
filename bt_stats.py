# -*- coding: utf-8 -*-

from collections import defaultdict

import beanstalkc
import msgpack

bt = beanstalkc.Connection()

tubes = bt.tubes()

def get_jobs_from_tube(tube):
    bt.watch(tube)
    job = bt.reserve(timeout=0.01)
    while job is not None:
        yield job
        job.bury()
        job = bt.reserve(timeout=0.01)
        

print "total\tready\ttube"
for tube in tubes:
    tube_status = bt.stats_tube(tube)
    print "{}\t{}\t{}".format(tube_status['total-jobs'], tube_status['current-jobs-ready'], tube)

    jobs = defaultdict(lambda :0)
    for job in get_jobs_from_tube(tube):
        task_data = msgpack.loads(job.body)
        jobs[task_data['taskname']] += 1
    for name, numbers in jobs.items():
        print "\t{}\t  |-{}".format(numbers, name)
