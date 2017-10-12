#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProcessingCorpus import  ProcessingCorpus

if __name__=="__main__":
    'Processing Corpus 属性'
    e=ProcessingCorpus()
    print e.__doc__
    print e.__dict__
    print e.__module__



    for k,v in e.__dict__.items():
        print k,":",v

    for k,v in ProcessingCorpus.__dict__.items():
        print "-"+k,":"