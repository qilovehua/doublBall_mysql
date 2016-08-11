import re
import urllib2
import cx_Oracle

sql_insert_ball=r'''
   insert into WINNINGNUMBER values(:1,:2,:3,:4,:5,:6,:7,:8)'''
sql_insert_info='''
   insert into WINNINGINFO values(:1,to_date(:2,'YYYY-MM-DD'),:3,:4,:5)'''

#connect(name, passwd, oracle instance)
db=cx_Oracle.connect('test','test', 'localhost:1521/oracle')
cursor=db.cursor()

req=urllib2.urlopen(r'''http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html''')
lin=req.read()

# get all of information
all=re.compile(r'''<tr>.+?(<td align="center".*?)</tr>''', re.DOTALL)
# get date and num
date_num=re.compile(r'''<td align="center">([0-9-]+)</td>.*?<td align="center">([0-9]+)</td>''', re.DOTALL)
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
    Date_Num=date_num.findall(line)
    date,num=Date_Num.pop()
    num=int(num)
    
    RedBall=redball.findall(line)
    red1,red2,red3,red4,red5,red6=[int(x) for x in RedBall]
    
    BlueBall=blueball.findall(line)
    blue=int(BlueBall.pop())
    
    Amount=amount.findall(line)
    saleamount=Amount.pop()
    
    First=first.findall(line)
    firstprise=int(First.pop())
    Second=second.findall(line)
    secondprise=int(Second.pop())
    winningnumber=[num,red1,red2,red3,red4,red5,red6,blue]
    winninginfo=[num,date,saleamount,firstprise,secondprise]
    print winningnumber,"=",winninginfo
    try:
        cursor.execute(sql_insert_ball,winningnumber)
    except cx_Oracle.DatabaseError as err:
        print "ERROR when execute insert winningnumber: %s" % err
    try:
        cursor.execute(sql_insert_info,winninginfo)
    except cx_Oracle.DatabaseError as err:
        print "ERROR when execute insert winninginfo: %s" % err
    except:
        print "UNKNOW ERROR"
    break
#print hua
cursor.execute('commit')
cursor.close()
req.close()
print "done"
print "done"