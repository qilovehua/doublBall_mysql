import re
import urllib2

req=urllib2.urlopen(r'''http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html''')
lin=req.read()

print type(lin)

# get all of information
all=re.compile(r'''<tr>.+?(<td align="center".*?)</tr>''', re.DOTALL)
# get date
date=re.compile(r'''<td align="center">([0-9-]+)</td>.*?<td align="center">([0-9]+)</td>''', re.DOTALL)
# get six red ball number
redball=re.compile(r'''<em class="rr">(\d+)</em>''')
# get blue ball number
blueball=re.compile(r'''<em>(\d+)</em>''')
# sale amount
amount=re.compile(r'''<td><strong>(.*?)</strong></td>''')
# first prise
first=re.compile(r'''<td align="left" style="color:#999;"><strong>(.*?)</strong>''')
# second prise
second=re.compile(r'''<td align="center"><strong class="rc">(.*?)</strong></td>''')

hua=all.findall(lin)
for line in hua:
    print date.findall(line)
    print redball.findall(line)
    print blueball.findall(line)
    print amount.findall(line)
    print first.findall(line)
    print second.findall(line)
    print "=================================="
    break
#print hua
print "done"
print "done"