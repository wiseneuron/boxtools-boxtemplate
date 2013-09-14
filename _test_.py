#!/usr/bin/env python
#author Chunhui Li wiseneuron@gmail.com
import sys
from path import *
from boxtemplate import *
class SQLBean:
      def __init__(self):
            self.table = Table('User')
            self.where = Where('id=123')
class Table:
      def __init__(self, tableName):
            self.name = tableName
class Where:
      def __init__(self, cond):
            self.cond = cond

if __name__ == "__main__":
     root = path(sys)
     #find all tag
     print '-----------------------find all tag----------------------------'
     tpl = 'select * from ${tbl} ${where} and ${tbl};'
     args = find_all_tag(tpl)
     print 'template %s:' %(tpl) 
     print 'tags:' + str(args)
     print '--------------------------------------------------------------------'
     
     #fill template string.
     print '------------------------fill template string.-------------------'
     tpl3 = 'select * from ${sqlbean.table.name} ${sqlbean.where.cond} and ${sqlbean.where.cond} and ${it};'
     sqlbean = SQLBean()
     it = 13
     mapDic = {'sqlbean':sqlbean, 'it':it}
     s3 = fill_template_str(tpl3, mapDic)
     print 'fill_template_with_object:' + s3
     print '--------------------------------------------------------------------'
     
     #generate file by template file. fill with object.
     print '------------generate file by template file.-------'
     tpl1 = root + "/templates/" + "1.tpl"
     genObject = root + "/generated/" + "gen-by-object.txt"
     you = 'Merry'
     me = 'neuron'
     it = 'Meal'
     mpDic = {'you': you, 'me': me,'it':it}
     fill_template_file(tpl1,genObject,mpDic)
     print 'generated file at ' + genObject
     print '--------------------------------------------------------------------'