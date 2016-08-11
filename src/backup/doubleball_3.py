import re
import urllib2
import cx_Oracle
from doubleball_2 import firstprise, secondprise

sql_insert_ball=r'''
   insert into WINNINGNUMBER values(:1,:2,:3,:4,:5,:6,:7,:8)'''
sql_insert_info='''
   insert into WINNINGINFO values(:1,to_date(:2,'YYYY-MM-DD'),:3,:4,:5)'''

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

def connectDB(username='test', passwd='test', instance='oracle'):
    #connect(name, passwd, oracle instance)
    #db=cx_Oracle.connect('test','test', 'localhost:1521/oracle')
    db=cx_Oracle.connect(username,passwd, 'localhost:1521/'+instance)
    cursor=db.cursor()
    return cursor

def closeDB(cursor):
    cursor.execute('commit')
    cursor.close()
    
def getData(maxPage,cursor):
    for page in range(1,maxPage+1):
        print "=========================="
        print "Page Number is: %d" % page
        try:
            getUrl(page,cursor)
        except:
            raise Exception("UNKNOW ERROR")

def getUrl(pagenum,cursor):
    req=urllib2.urlopen(r'''http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html''' % str(pagenum))
    pageContent=req.read()
    usefull=all.findall(pageContent)
    for line in usefull:
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
        tmp=First.pop()
        if len(tmp) == 0:
            firstprise=0
        else:
            firstprise=int(tmp)
            
        Second=second.findall(line)
        tmp=Second.pop()
        if len(tmp) == 0:
            secondprise=0
        else:
            secondprise=int(tmp)
            
        winningnumber=[num,red1,red2,red3,red4,red5,red6,blue]
        winninginfo=[num,date,saleamount,firstprise,secondprise]
        print date,"=",num
        try:
            cursor.execute(sql_insert_ball,winningnumber)
        except cx_Oracle.DatabaseError as err:
            print "ERROR when execute insert winningnumber: %s" % err
        except:
            print "UNKNOW ERROR"
            print date, "=", num
            raise Exception("UNKNOW ERROR")           
        
        try:
            cursor.execute(sql_insert_info,winninginfo)
        except cx_Oracle.DatabaseError as err:
            print "ERROR when execute insert winninginfo: %s" % err
        except:
            print "UNKNOW ERROR"
            print date, "=", num
            req.close()
            raise Exception("UNKNOW ERROR")
     
    req.close()   

def main():
    maxPage=88
    cursor=connectDB('test', 'test', 'oracle')
    getData(maxPage, cursor)
    closeDB(cursor)
    
if __name__=='__main__':
    main()
