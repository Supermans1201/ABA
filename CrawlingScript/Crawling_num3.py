#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Crawling import  Crawling

if __name__=="__main__":
    '获取issue存入到mongodb中'
    e=Crawling()
    print e.__doc__
    print e.__dict__
    e.genAllissuestomongodb()
