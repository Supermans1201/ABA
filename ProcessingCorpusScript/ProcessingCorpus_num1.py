#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.ProcessingCorpus import  ProcessingCorpus
import time
if __name__=="__main__":
    '清洗文本'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__

    e.gendiffsanitizationtxt(type="all")
    e.gendiffsanitizationtxt(type="java")
    e.gendiffsanitizationtxt(type="xml")

