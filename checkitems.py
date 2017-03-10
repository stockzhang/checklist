#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/9 16:50
# @Author  : Stock Zhang
# @Site    : 
# @File    : checkitems.py
# @Software: PyCharm

from tools import *
import sys
import os
import stat
import pwd

def checkIsDirectory(path):
#    print(path)
    if not os.path.isdir(path):
        echo(path,"isnt directory!",False,space=1)
        sys.exit(1)
    else:
        echo(path,"have been checked!",True,space=1)
        return True

def checkPermission(obj,uid=33):
    if (os.stat(obj).st_uid != 33) or (os.stat(obj).st_gid !=33):
        echo(obj,"owner or group isnot 'www-data(uid=33 or gid=33)'",False,1)

def checkDirectoryIsWrite(path,user=33):
    if not isinstance(user,int):
        user_info=pwd.getpwnam(user)
        uid=user_info.pw_uid
    else:
        uid=user
    st=os.stat(path)
    mode=st.st_mode
    return( (st.st_uid == uid) and ((mode & stat.S_IWUSR) > 0))

def traversal(root):
    for dirpath,dirnames,filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirpath,filename)
        for dirname in dirnames:
            yield os.path.join(dirpath,dirname)


def check(appname,appdir):
    d="%s/%s" % (appdir,appname)
    if not os.path.islink(d):
        echo(appname,"link isnt exits!",False,space=1)
        sys.exit(1)
    else:
        echo(appname,"link is ok!",True,space=1)
        realpath = os.path.realpath(d)
    if checkIsDirectory(realpath):
        for root in traversal(realpath):
            checkPermission(root)
