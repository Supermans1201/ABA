#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.Analysis import  Analysis

if __name__=="__main__":
    '统计不同的文件名称'
    e=Analysis()
    print e.__doc__
    print e.__dict__
    e.statisticsdifferentfilename()





