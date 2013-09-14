#!/usr/bin/env python
#author Chunhui Li wiseneuron@gmail.com

#find firs tag in template.
# The length of start tag is 2, and the end is 1.
def find_tag(template, tag={'start':'${', 'end':'}'}):
    l = len(template)
    start = - 1;
    end = -1;
    argPos = {'start':start, 'end':end}
    if l > 0:
       start = template.find(tag['start'])
       end = template.find(tag['end'])
       if start > 0 and end > start:
         tagContent = template[start + 2: end]
         argPos = {'start':start, 'end':end, 'tagContent': tagContent}
    return argPos
#find all tag.
def find_all_tag(template):
      args = []
      hasArg = True
      tpl = template[0:]
      while hasArg:
         argPos = find_tag(tpl)
         if argPos['end'] > 0 :
            tagContent = argPos['tagContent']
            try:
               idx = args.index(tagContent)
            except ValueError:
               args.append(tagContent)
            hasArg = True
            if argPos['end'] + 1 < len(tpl) :
                 tpl = tpl[argPos['end'] + 1:]
            else :
                 tpl = ''
         else :
            hasArg = False
      return args
#fill template with value in given dictionary.
def _fill_template_with_dic(template, argDic):
      #replace arguments in template with "$".
      args = argDic
      w = ''
      idx = 0;
      ret = []
      hasArg = True
      tpl = template[0:]
      while hasArg:
         arglen = len(args)
         argPos = find_tag(tpl)
         if argPos['end'] > 0 :
            ret.append(tpl[0: argPos['start']])
            if arglen > 0 :
                 w = args.get(argPos['tagContent'])
                 idx = idx + 1
                 ret.append(w)
            hasArg = True
            if argPos['end'] + 1 < len(tpl) :
                 tpl = tpl[argPos['end'] + 1:]
            else :
                 tpl = ''
         else :
            w = tpl[argPos['end'] + 1:]
            ret.append(w)
            hasArg = False
     
      #join string in newUnitList with space.
      result = ''.join([str(ele) for ele in ret])
      return result
#generate new file by template file .
#fill value in argDic into template.
def _fill_template_file_with_dic(teplateFileName, generatedFileName, argDic):
     tf = open(teplateFileName, 'r')
     gf = open(generatedFileName, 'w')
     args = argDic
     line = tf.readline()
     newline = ''
     while line:
        #generate string by template.
        ret = _fill_template_with_dic(line,args)
        #write generated string.
        gf.writelines(ret)
        #read next line.
        line = tf.readline()
     gf.close()
     tf.close()
# fill template with object's peoperties.
# mapDic = {namspacename1:object1, namespace2:object2[,...]}
# object1's name is equals to namespacename1, object2 also is the
# same to namespace2.
def fill_template_str(template, mapDic):
     args = find_all_tag(template)
     argDic = {}
     mapDicKeys = mapDic.keys()
     for arg in args:
           parsedArg = _parse_argument(arg)
           namesp = parsedArg['namespace']
           if len(namesp) > 0:
                 #generate python code to get value.
                 chain = parsedArg['chain']
                 #get value by visite chain.
                 value = _execute_viste_chain(mapDic, namesp, chain)
           if value is not None:
                 argDic[arg] = value
     # fill value into template.
     ret = _fill_template_with_dic(template, argDic)
     return ret
#generate new file by template file .
#fill value in mapDic into template file.
def fill_template_file(teplateFileName, generatedFileName, mapDic):
     tf = open(teplateFileName, 'r')
     gf = open(generatedFileName, 'w')
     args = mapDic
     line = tf.readline()
     newline = ''
     while line:
        #generate string by template.
        ret = fill_template_str(line,args)
        #write generated string.
        gf.writelines(ret)
        #read next line.
        line = tf.readline()
     gf.close()
     tf.close()
def _execute_viste_chain(mapDic, objectname, chain):
      """ get property value  by given chain  from 
       in named object.
      """
      #get object from map.
      value = mapDic.get(objectname)
      if value is None:
                print  'the property %s is not found!'  %(objectname);
      vchain = [objectname]
      for p in chain:
                value = getattr(value, p,  None);
                vchain.append(p)
                if value is None:
                        print  'the property %s is not found!'  %('.'.join(vchain));
                        break
      return value
# parse argument into namespace and visite chain.
# argument format is namespace.member, for examplse, a.c's namespace is a, visite
# chain is [c]
# variable d's namespace is  d, visite chain is [].
def _parse_argument(arg):
      namesp = ''
      chain = []
      parsed = {'namespace':'', 'chain': []}
      arglen = len(arg)
      if arglen > 0:
            lst = arg.split('.')
            namesp = lst[0]
            if len(lst) > 1:
                  chain = lst[1:]
      parsed = {'namespace': namesp, 'chain': chain}
      return parsed
