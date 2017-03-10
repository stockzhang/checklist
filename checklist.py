#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/9 16:50
# @Author  : Stock Zhang
# @Site    : 
# @File    : checklist.py
# @Software: PyCharm

from tools import *
from checkitems import * 

APP_LIST = ['summer-hill','official-web','user-center']
LOG_LIST = ['/usr/local/php7/var/log/php_errors.log']
APP_DIR = "/web/neo"

if  __name__  == '__main__':
    if len(sys.argv) < 2:
        Usage()
    appListName = sys.argv[1].split(",")
    for appname in appListName:
        if appname in APP_LIST:
            echo(appname,"is checking......",True)
            check(appname,APP_DIR)
        else:
            echo(appname,"not available!",False)
        echo(appname,"had been checked!",True)
    print('*'*80)
    for log in LOG_LIST:
        echo(log,"is checking......",True)
        if checkDirectoryIsWrite(log):
            echo(log,"can be writen",True,1)
        else:
            echo(log,"cannt be writen!",False,1)
