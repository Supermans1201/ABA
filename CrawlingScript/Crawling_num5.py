#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Crawling import Crawling

if __name__=="__main__":
    '将所有的commot存入到数据库中'
    e=Crawling()
    print e.__doc__
    print e.__dict__
    e.genAllcommitstomongodb()
