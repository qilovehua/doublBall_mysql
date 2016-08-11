#import cx_Oracle
import MySQLdb

#connect(name, passwd, oracle instance)
#db=cx_Oracle.connect('test','test', 'localhost:1521/oracle')
db=MySQLdb.connect('localhost','test','test','test')
cursor=db.cursor()

sql_create_1=r'''
    create table if not exists WINNINGNUMBER(
    num  smallint(6) primary key,
    red1 tinyint(2) not null,
    red2 tinyint(2) not null,
    red3 tinyint(2) not null,
    red4 tinyint(2) not null,
    red5 tinyint(2) not null,
    red6 tinyint(2) not null,
    blue tinyint(2) not null)'''

sql_create_2=r'''
    create table if not exists WINNINGINFO(
    num smallint(6) primary key,
    opendate date not null,
    saleamount varchar(13) not null,
    firstprise tinyint(3) not null,
    secondprise smallint(3) not null)'''
# try:    
cursor.execute(sql_create_1)
# except cx_Oracle.DatabaseError as err:
#     print "ERROR1: %s" % err
    
# try:
cursor.execute(sql_create_2)
# except cx_Oracle.DatabaseError as err:
#     print "ERROR2: %s" % err
    
db.commit()
cursor.close()
db.close()   
print "done"