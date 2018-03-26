#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import  ProcessingCorpus
if __name__=="__main__":
    '预处理文本'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    e.gendiffpredealtxt()
    print "java"
    e.gendiffpredealtxt(type ="java")
    print "xml"
    e.gendiffpredealtxt(type= "xml")