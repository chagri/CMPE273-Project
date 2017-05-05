import time
import os
import MySQLdb
from getColumnNames import *

#Generate query 
def generateQuery(fromTable,selectColumns,searchCondition):

    allColumns = getAllColumns(fromTable)
    selectColumns = set(selectColumns)       
    whereColumns = eliminateSelectColumns(selectColumns,allColumns)       
    db = MySQLdb.connect("localhost","root","Apple@123","testdb" )
    cursor = db.cursor()
    data=None       
    selectString=None    
    if len(selectColumns)>1:
        selectString = ', '.join(str(e) for e in selectColumns) 
        
    else:
        selectString= ','.join(str(s) for s in selectColumns)    
        
    print "selectString",selectString
    for column in set(whereColumns):
        print column
        print "searchCondition", searchCondition
        cursor.execute("SELECT %s from %s where %s like ('%s');"%(selectString,fromTable,column,searchCondition))                   
        data = cursor.fetchall()
        print data
        data='\n'.join(','.join(elems) for elems in data)                
        print "fetch completed",data,"data"
        if data:      
            print "Output : %s " % data 
            return data    
    return None

#sample input
#selectColumns=set()
#selectColumns.add("Week")  
##selectColumns.add("Dues")  
#fromTable="CourseSchedule"
#leaf="final"
#head="exam"  
#whereColumns=set()
#whereColumns.add("topics")    
#generateQuery(fromTable,selectColumns,whereColumns,leaf,head)




