#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.Crawling import  Crawling

if __name__=="__main__":
    '获得所有的issue 编号存入到txt中'
    e=Crawling()
    print e.__doc__
    print e.__dict__
    e.genAllissuesnumtxt()

