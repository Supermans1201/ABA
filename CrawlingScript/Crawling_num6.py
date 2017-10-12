#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Crawling import  Crawling
if __name__=="__main__":
    '获得所有不同的commit分支'
    e=Crawling()
    print e.__doc__
    print e.__dict__
    e.genAllcommitsdiffpatch()
