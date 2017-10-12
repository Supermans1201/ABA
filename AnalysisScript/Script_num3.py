#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.Analysis import  Analysis

if __name__=="__main__":
    '生成diff信息存入到数据库中'
    e=Analysis()
    print e.__doc__
    print e.__dict__
    e.gendiff()
    for k,v in e.__dict__.items():
        print k,":",v

    for k,v in Analysis.__dict__.items():
        print "-"+k,":"