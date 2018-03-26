#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import  ProcessingCorpus

if __name__=="__main__":
    '生成字典'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    e.gendirectory(type="xml")
    e.gendirectory(type="java")
    e.gendirectory(type="xml")

