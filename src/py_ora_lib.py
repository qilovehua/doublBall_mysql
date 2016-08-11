#-*- coding: utf-8 -*-
import re
import urllib2
#import cx_Oracle
import MySQLdb

def getMaxNumFromFile():
    file='recode_num.txt'
    max_num=re.compile(r'''maxnum:(.+)''')
    maxnum=0
    fd=open(file, 'r')
    for line in fd.readlines():
        line=line.strip()
        group_max=max_num.match(line)
        if group_max == None:
            #print "Match None."
            continue
        else:
            maxnum=int(group_max.group(1))
    
    return maxnum

def getMaxNumFromDB():    
    #db=cx_Oracle.connect('test','test', 'localhost:1521/oracle')
    db=MySQLdb.connect('localhost','test','test','test')
    cursor=db.cursor()
    sql_max=r'''select max(num) from winninginfo'''
    cursor.execute(sql_max)
    # (2015016,)
    max_num=cursor.fetchone()
    cursor.close()
    db.close()
    return max_num[0]

def getMaxNumFromUrl():
    latest_record=re.compile(r'''<tr>.+?<td align="center">.+?</td>.+?<td align="center">(.+?)</td>''', re.DOTALL)
    req=urllib2.urlopen(r'''http://kaijiang.zhcw.com/zhcw/html/ssq/list.html''')
    latest=req.read()
    latestRecord=latest_record.findall(latest)
    return int(latestRecord[0])

def updateLatestRecord(maxNumFromUrl,maxNumFromDB):
    if maxNumFromUrl < maxNumFromDB:
        print "ERROR: the num from DB is newer than URL, exit"
        return 
    if maxNumFromDB == maxNumFromUrl:
        print "No newer num is available, exit."
        return
    yearUrl=maxNumFromUrl/1000
    yearDB=maxNumFromDB/1000
    if yearUrl == yearDB:
        diff=yearUrl-yearDB
    else:
        #db=cx_Oracle.connect('test','test', 'localhost:1521/oracle')
        db=MySQLdb.connect('localhost','test','test','test')
        cursor=db.cursor()
        sql_max_num_year=r'''select max(num) from winninginfo where num like '%d''' % yearDB
        cursor.execute(sql_max_num_year)
        max_num_year=cursor.fetchone()
        maxNumYear=max_num_year[0]
        diff=max_num_year - maxNumFromDB + maxNumFromUrl%1000
        
def getRecordUniq():
    from py_random_lib import get_redblueball
    from py_doubleball_lib import connectDB, closeDB
    uniq=0
    db, cursor = connectDB()
    while 1:
        redblue=get_redblueball()
        sql_uniq=r'''select red1,red2,red3,red4,red5,red6 from winningnumber where blue != %d''' % redblue[6]
        cursor.execute(sql_uniq)
        while cursor.fetchone() != None:
             break
        
        
def getBlueballCount(year='0'):
    from py_doubleball_lib import connectDB, closeDB
    if year == '0':
        sql_blue_count=r'''select blue, count(blue) from winningnumber a inner join winninginfo b on a.num=b.num group by blue order by blue'''
    else:
        sql_blue_count=r'''select blue, count(blue) as count from winningnumber where num > %s000 group by blue order by count''' % year
        
    db, cursor=connectDB()
    cursor.execute(sql_blue_count)
    bluedic={}
    print " BLUE - COUNT"
    for line in cursor.fetchall():
        print '  %2d  -  %d' % line
        bluedic[line[0]]=line[1]
    closeDB(db, cursor)
#     print bluedic.keys()
#     print bluedic.values()
    
def getRedballCount(year='0'):
    from py_doubleball_lib import connectDB, closeDB
    if year == '0':
        sql_red_count=r'''select red1,red2,red3,red4,red5,red6 from winningnumber a inner join winninginfo b on a.num=b.num'''
    else:
#         sql_red_count=r'''select red1,red2,red3,red4,red5,red6 from winningnumber a inner join winninginfo b on a.num=b.num where to_char(opendate,'yyyy')=%s''' % year
#         sql_red_count=r'''select red1,red2,red3,red4,red5,red6 from winningnumber a inner join winninginfo b on a.num=b.num where year(opendate,'yyyy')=%s''' % year
        sql_red_count=r'''select red1,red2,red3,red4,red5,red6 from winningnumber where num > %s000 ''' % year
        
    db, cursor=connectDB()
    cursor.execute(sql_red_count)
    dict_red={}
    while 1:
        line=cursor.fetchone()
        if line == None:
            break
        for red in line:
            if dict_red.has_key(red):
                dict_red[red]=dict_red[red]+1
            else:
                dict_red[red]=1
    closeDB(db, cursor) 
        
#     dict_red.keys().sort()       
#     print " RED - COUNT"
#     for key in dict_red.keys():
#         print '  %2d  -  %d' % (key, dict_red[key])
        
    # get 15 redball number which amount is at least
    value_key=[[value[1],value[0]] for value in dict_red.items()]
    value_key.sort()
    print "============================"
    print "15 minimun red ball number:"
    print "RED -- Num "
    minimun_amount=[]
    for i in range(0,32):
        if i == 15:
            print "====15===="
        print " %2d -> %d" % (value_key[i][1],value_key[i][0])
        minimun_amount.append(value_key[i][1])
    minimun_amount.sort()
    return minimun_amount

    
    
    
    
    
    
    
    
        
        
        
        