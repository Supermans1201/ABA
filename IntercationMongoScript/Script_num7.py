#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pygitthub.InteractionMongo import  InteractionMongo

if __name__=="__main__":
    '处理 diffinfo'
    e=InteractionMongo()
    print e.__doc__
    print e.__dict__

    e.dealdiffinfo()