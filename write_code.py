# -*- coding: utf-8 -*-

"""
代码生成器：
自动生成针对chinacourt域名下爬虫的测试代码。

从template中根据模板生成代码，下载需要的测试文件，
生成完成之后打印一条执行本测试的命令.
我他妈简直是偷懒的天才.
"""

import os
import click
import requests


@click.group()
def main():
    pass


@main.command()
@click.option('--name', '-n', multiple=True)
@click.option('--url', '-u')
@click.option('--db-number', '-d', default=1)
def test_chinacourt(name, url, db_number):
    page_body = requests.get(url).text
    if len(name) == 2:
        package = "{}.{}".format(*name)
        testname = "{}{}".format(*[n.capitalize() for n in name])
        html_file_path = '/Users/laixintao/Program/yorg/tests/data/court/test_court_{}_{}_detail_page.html'.format(*name)
        html_path = '"data/court/test_court_{}_{}_detail_page.html"'.format(*name)
        test_path = '/Users/laixintao/Program/yorg/tests/court/test_{}_{}.py'.format(*name)
    else:
        package = name[0]
        testname = name[0].capitalize()
        html_path = '"data/court/test_court_{}_detail_page.html"'.format(*name)
        html_file_path = '/Users/laixintao/Program/yorg/tests/data/court/test_court_{}_detail_page.html'.format(*name)
        test_path = '/Users/laixintao/Program/yorg/tests/court/test_{}.py'.format(*name)
    data_num = db_number
    # remove _
    testname = testname.replace('_', '')
    with open(html_file_path, 'wb') as html:
        html.write(page_body.encode('utf-8'))
    click.echo("Download html file success!")
    with open('/Users/laixintao/Program/test-yorg/templates/test_chinacourt.py', 'r') as chinacourt:
        content = chinacourt.read()
        content = content.format(package=package, testname=testname, html_path=html_path, data_num=db_number, url=url)
        with open(test_path, 'w') as test_file:
            test_file.write(content)
    click.echo("write code success!")
    click.echo("pytest {}".format(test_path))


@main.command()
@click.option('--path', '-p')
def chinacourt(path):
    dir_path = '/Users/laixintao/Program/yorg/yorg/contrib/court/{}/'.format(path)
    if not os.path.isdir(dir_path):
        os.system('mkdir -p {}'.format(dir_path))
    with open('/Users/laixintao/Program/test-yorg/templates/chinacourt.py', 'r') as chinacourt:
        with open(dir_path+'__init__.py', 'w') as code:
            code.write(chinacourt.read())


if __name__ == '__main__':
    main()
