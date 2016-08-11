from py_ora_lib import getMaxNumFromDB,getMaxNumFromFile,getMaxNumFromUrl
from py_doubleball_lib import getRecordFromURL
from py_random_lib import get_redblueball
   
def main():
    maxNumFromUrl=getMaxNumFromUrl()
    maxNumFromDB=getMaxNumFromDB()
#     maxNumFromFile=getMaxNumFromFile()
    maxNumFromFile=maxNumFromDB
    print "getMaxNumFromUrl: ", maxNumFromUrl
    print "getMaxNumFromDB: ", maxNumFromDB
    print "getMaxNumFromFile: ", maxNumFromFile
    if maxNumFromDB != maxNumFromFile and maxNumFromDB != maxNumFromUrl and maxNumFromFile != maxNumFromUrl:
        print "ERROR: the number is inconformity"
        return 1
    elif maxNumFromDB != maxNumFromUrl:
        print "New record: updating from URL..."
        getRecordFromURL()
        print 'Done.'
    elif maxNumFromDB != maxNumFromFile:
        print "The amount of NUM between DB and recode_num.txt is different."
        print "Please check"
    else:
        print "No New recode need to be updated."
        print 'Done.'
    get_redblueball(5)
        
if __name__ == '__main__':
    main()

        
