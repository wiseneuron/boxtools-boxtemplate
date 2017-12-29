--------------------------------------------------------------
version 
0.1

Introduction
boxtemplate is a very light template tool.
   

Dependencies:

1.python 2.4+

Usage
   read _test_.py.
   
if you want to relace a variable with a value, you shoude define represent as ``${varName}`` format in template string
of template file, then put the value into dictionary whose key is varName. then call ``fill_template_*`` functtion. For example,
```python
tpl1 = 'hello, ${user}'
dic = {'user': 'jack'}
s1 = fill_template_str(tpl3, mapDic)
print s1
```
then, you should get, 
```bash
hello, jack
```
if you want to replace some place with an object's property, you should represent it as ``${objectVarName.property1}``, 
if you want to get property object's property, you should only represent it as ``${objectVarName.property1.property2}``, 
'.' represent to get the object's property vaule. For example,
```python
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
     
      
     tpl3 = 'select * from ${sqlbean.table.name} ${sqlbean.where.cond} and ${sqlbean.where.cond} and ${it};'
     sqlbean = SQLBean()
     it = 13
     mapDic = {'sqlbean':sqlbean, 'it':it}
     s3 = fill_template_str(tpl3, mapDic)
     print 'fill_template_with_object:' + s3
```
You can test and learn it by reading and ``run _test_.py`` in the project.      
      
author: neuron
if you want contact the author, please 
visit http://idocbox.com/ or send mail to wiseneuron@gmail.com

thanks!
     
