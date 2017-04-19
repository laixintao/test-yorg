#!/bin/zsh

MONGONAME='shandong'
START_JOB='from yorg.contrib.court.shandong import start_job;start_job()'

YORG_DIR='~/program/yorg/'
cd $YORG_DIR
echo you are now in ${YORG_DIR}

echo -n dropping datebase $MONGONAME ...
python drop_mongo.py $MONGONAME
echo 'OK'

PROCESS=`ps -ef|grep beanstalkd|grep -v grep|grep -v PPID|awk '{ print $2}'`
for i in $PROCESS
do
        echo "Kill the $1 process [ $i ]"
        kill -9 $i
done

echo -n run beanstalkd ...
beanstalkd &
echo OK

echo start_job ...
python -c $START_JOB
echo start_job finished

echo start_yorg
yorg

