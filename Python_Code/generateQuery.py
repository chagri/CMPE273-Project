import time
import os
import MySQLdb
from getColumnNames import *
from dateutil import parser
from datetime import datetime
import datetime

#Generate query 
def generateQuery(fromTable,selectColumns,searchCondition,subjectcode, sectionname,sectionperiod):
    subjectcode = int(filter(str.isdigit, str(subjectcode)))
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
            
    for column in set(whereColumns):                        
        rows_affected = cursor.execute("SELECT %s from %s where %s like ('%s') and subject_code=trim('%s') and section_name=trim('%s') and section_period=trim('%s');"%(selectString,fromTable,column,searchCondition,subjectcode, sectionname,sectionperiod))                   
        data = cursor.fetchall()        
        if rows_affected >1:                                  
            cursor.execute("SELECT %s,%s from %s where %s like ('%s') and subject_code=trim('%s') and section_name=trim('%s') and section_period=trim('%s');"%(column,selectString,fromTable,column,searchCondition,subjectcode,sectionname,sectionperiod))                           
            data = cursor.fetchall()
                  
        data='\n'.join(''.join(str(elems)) for elems in data)    
        data = data.replace("'","").replace('(', '').replace(')', '').replace('datetime.date', '')
        if data:      
            print "Output : %s " % data 
            return data
    return None

