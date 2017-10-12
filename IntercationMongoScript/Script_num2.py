#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pygitthub.InteractionMongo import InteractionMongo

if __name__=="__main__":
    '读取处理后的commit'
    a= InteractionMongo()
    a.readdealcomments()