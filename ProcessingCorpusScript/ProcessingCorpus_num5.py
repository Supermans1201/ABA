#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import  ProcessingCorpus
if __name__=="__":
    '生成diff的图片'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    e.gendiffpicture("intent",type="java")
    e.gendiffpicture("SNAPSHOT",type="all")
    e.gendiffpicture("intent",type="xml")