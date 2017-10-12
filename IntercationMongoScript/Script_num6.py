#!/usr/bin/python
# -*- coding: UTF-8 -*-
from InteractionMongo import  InteractionMongo
if __name__=="__main__":
    '读取处理后的issue和commit'
    e=InteractionMongo()
    print e.__doc__
    print e.__dict__
    e.readdealissuesandcommits()