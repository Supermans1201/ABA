#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.ProcessingCorpus import  ProcessingCorpus

if __name__=="__main__":
    '获得单词的相似度'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    # e.gendiffpicture("intent",type="all")
    word=e.getsmailarword("SNAPSHOT",type="all",number=10)
    print word
    # e.gendiffpicture("intent",type="xml")