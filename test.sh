#!/bin/zsh

MONGONAME='shaanxi'
START_JOB="from yorg.contrib.court.shaanxi.xian_yanliang import start_job; start_job()"

YORG_DIR='~/program/yorg/'
TEST_YORG_PATH=~/program/test-yorg/
cd $YORG_DIR
echo you are now in `pwd`

echo -n dropping datebase $MONGONAME ...
python $TEST_YORG_PATH/drop_mongo.py $MONGONAME
echo 'OK'

PROCESS=`ps -ef|grep beanstalkd|grep -v grep|grep -v PPID|awk '{ print $2}'`
for i in $PROCESS
do
        echo "Kill the $1 process [ $i ]"
        sudo kill -9 $i
done

echo -n run beanstalkd ...
beanstalkd &
echo OK

echo start_job ...
/home/laixintao/.virtualenvs/yorg/bin/python -c $START_JOB
echo start_job finished

echo start_yorg
/home/laixintao/.virtualenvs/yorg/bin/yorg
