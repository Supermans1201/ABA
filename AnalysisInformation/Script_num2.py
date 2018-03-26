#!/usr/bin/python
# -*- coding: UTF-8 -*-
from AnalysisInformation.Analysis import  Analysis

if __name__=="__main__":
    '统计不同的文件类型'
    e=Analysis()
    print e.__doc__
    print e.__dict__
    e.statisticsdifferentfiletype()

