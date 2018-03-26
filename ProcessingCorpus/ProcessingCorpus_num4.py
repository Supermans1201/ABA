#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import  ProcessingCorpus
if __name__=="__main__":
    '生成词向量模型'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    e.genmodel(type="all")
    e.genmodel(type="java")
    e.genmodel(type="xml")