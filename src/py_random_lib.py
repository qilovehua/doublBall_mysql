import random
from py_doubleball_lib import blueball

def get_redball():
    list_redball=[]
    num=6
    i=0
    while i < num:
        red=random.randint(1,33)
        if red not in list_redball:
            list_redball.append(red)
            i=i+1
    list_redball.sort()
    return list_redball

def get_blueball(list_redball):
    # get blueball num according redball, redball is sort ascending
    begin=list_redball[0]
    if list_redball[4] < 16:
        end=list_redball[3]
    else:
        end=list_redball[2]
        
    if begin > 16:
        begin=1
        end=16
    elif end > 16:
        end=16
    
    return random.randint(list_redball[0],list_redball[2])

def get_redblueball(num=1):
    # get records including red and blue ball, one record by default.
    for n in range(0,num):
        list_redblueball=[]
        list_redball=get_redball()
        blueball=get_blueball(list_redball)
        list_redblueball.extend(list_redball)
        list_redblueball.append([blueball])
        print n+1, " -> ", list_redblueball
        
    return list_redball

def get_blue_count():
    # same as py_ora_lib.getBlueballCount(2015)
    from py_doubleball_lib import connectDB
    db,cursor=connectDB()
    blue_count_sql=r"""
         select blue, count(blue) as count from winningnumber where num>2015000 group by blue order by count;
     """
    cursor.execute(blue_count_sql)
    while 1:
        line=cursor.fetchone()
        if line is None:
            break
        print line 
    cursor.close()
    db.close()
        