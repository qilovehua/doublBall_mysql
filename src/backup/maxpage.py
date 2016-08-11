#-*- coding: utf-8 -*-
import re
import urllib2

req=urllib2.urlopen(r'''http://kaijiang.zhcw.com/zhcw/html/ssq/list.html''')
pageContent=req.read()
maxpage_number=re.compile(r'''<p class="pg"> 共<strong>(.*?)</strong>''')

maxpage=maxpage_number.findall(pageContent)
if len(maxpage) == 1:
    print int(maxpage[0])
else:
    print "maxpage is not unique: ", maxpage
    
maxrecord=maxrecord_number.findall(pageContent)
print maxrecord[0][0],maxrecord[0][1]

file='recode_num.txt'
fd=open(file,'w')
fd.write('page:' + str(maxrecord[0][0])+'\n')
fd.close()

fd=open(file,'a+')
fd.write('record:' + str(maxrecord[0][1])+'\n')
fd.close()

fd=open(file,'r')
for line in fd.readlines():
    print line.strip()
print 'Done.'
