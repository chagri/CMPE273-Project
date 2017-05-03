import time
import os
import MySQLdb


#Generate query 
def generateQuery(fromTable,selectColumns,whereColumns,leaf,head):
    db = MySQLdb.connect("localhost","root","****","testdb" )
    cursor = db.cursor()
    data=None   
    print selectColumns
    selectString=None
    print(len(selectColumns))
    if len(selectColumns)>1:
        selectString = ', '.join(str(e) for e in selectColumns) 
        
    else:
        selectString= ','.join(str(s) for s in selectColumns)    
        
    print selectString
    for column in set(whereColumns):
        print column
        cursor.execute("SELECT %s from %s where %s like ('%s%s');"%(selectString,fromTable,column,"%"+leaf+"%","%"+head+"%"))                   
        data = cursor.fetchall()
        print data
        data='\n'.join(','.join(elems) for elems in data)                
        print "fetch completed",data,"data"
        if data:      
            print "Output : %s " % data 
            return data    
    

#sample input
selectColumns=set()
selectColumns.add("Week")  
selectColumns.add("Dues")  
fromTable="CourseSchedule"
leaf="final"
head="exam"  
whereColumns=set()
whereColumns.add("topics")    
generateQuery(fromTable,selectColumns,whereColumns,leaf,head)




