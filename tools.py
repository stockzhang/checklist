#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/9 16:50
# @Author  : Stock Zhang
# @Site    : 
# @File    : tools.py
# @Software: PyCharm

import sys

def Usage():
    print """Usage:
             python checklist.py appname
             - appname: application name，eg:summer-hill
          """
    sys.exit(1)

def echo(cls,contents,flag,space=0):
    space="\t"*space
    if flag:
        print("%s\033[1;32;40m[+OK]: '%s' %s\033[0m" % (space,cls,contents))
    else:
        print("%s\033[5;31;40m[-ERR]: '%s' %s\033[0m" % (space,cls,contents))
