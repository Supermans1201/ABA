#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import ProcessingCorpus
if __name__=="__main__":
    '获得单词的相似度'
    e=ProcessingCorpus()
    e.gendiffpicture("Intent", type="java", size=2)

    # word=e.getsmailarword("intent",type="all",number=10)
    # print word
    # e.gendiffpicture("intent",type="xml")