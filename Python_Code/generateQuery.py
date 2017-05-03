import time
import os
import MySQLdb


#Generate query 
def generateQuery(leaf,head):
    db = MySQLdb.connect("localhost","root","Apple@123","testdb" )
    cursor = db.cursor()
    data=None
    print leaf
    print head        
    cursor.execute("SELECT Week, Topics from testdb.CourseSchedule where Topics like ('%s%s');"%("%"+leaf+"%","%"+head+"%"))           
    data = cursor.fetchall()
    data = ''.join(data)
    #data = data.translate(None, '["]')
    print "fetch completed",data,"data"
    if data:      
        print "Output : %s " % data         
    return data



