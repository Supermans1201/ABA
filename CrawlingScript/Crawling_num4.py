#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.Crawling import  Crawling

if __name__=="__main__":
    '获取所有的commit编号存入到txt'
    e=Crawling()
    print e.__doc__
    print e.__dict__
    e.genAllcommitsshatxt()
