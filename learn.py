# coding=utf-8
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

from src.tnpy import RegexCore
core = RegexCore('../rules/learn')

print core
import src.tngraph as graph
graph.buildGraph(core,'int_0_99');
import codecs
RegexCore.LogFile = codecs.open("learn.log", 'w',"utf-8")
RegexCore.LogFile.truncate()
matchs=core.Match(u'领导你好！老婆你好');
for m in matchs:
   print 'match',m.mstr, 'pos:',m.pos
#
# print(core.Rewrite(u'领导你好！老婆您好'));

print(core.Rewrite(u'十三与十四和十五和 68 '));

# for r in ["十","三十七","一十三","68"]:
#     print r
#     core.Rewrite(r)
print({r:core.Rewrite(r) for r in [u'十',u'三十七',u'一十三',u'68']});

RegexCore.LogFile.flush()
RegexCore.LogFile.close()
