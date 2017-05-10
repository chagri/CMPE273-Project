from PyDictionary import PyDictionary
import MySQLdb


def getAllColumns(table):
    table = "greensheet"
    allColumns = set()
    # global allColumns
    db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                         user="greensheet",  # your username
                         passwd="root1234",  # your password
                         db="slackbot")  # name of the data base
    cursor = db.cursor()
    sql = """ SHOW COLUMNS FROM %s """ % table
    cursor.execute(sql)
    fields = cursor.fetchall()
    counter = 0
    for field in fields:
        allColumns.add(field[0])
    cursor.close()
    db.close()

    return allColumns


def getSetOfAllColumns():
    listOfColumnNames = getAllColumns("greensheet")
    listOfColumnNames.update(getAllColumns("course_sch"))
    listOfColumnNames.update(getAllColumns("grading_policy"))
    return listOfColumnNames


def getCorrectAttribute(attributeToCheck, columnSynonymDict):
    attributeToCheck = attributeToCheck.replace(" ", "_").lower()
    queryValue = None;
    listOfColumnNames = getSetOfAllColumns()

    if (attributeToCheck in listOfColumnNames):
        return attributeToCheck

    for key, value in columnSynonymDict.iteritems():

        if attributeToCheck is not None and value is not None and attributeToCheck in value:
            queryValue = key
            break;

    return queryValue


def getAttributeFromJoinedList(attributeList):
    joinedAttribute = None
    concatAttribute = []
    listOfColumnNames = getSetOfAllColumns()
    columnNamesStr = ''.join(listOfColumnNames)
    counter = 0

    for attribute in attributeList:
        if attribute is not None and attribute.lower() in columnNamesStr:
            counter += 1
            concatAttribute.append(attribute)
            if counter == 2:
                joinedAttribute = '_'.join(concatAttribute)
                break

    if joinedAttribute is not None and joinedAttribute.lower() in columnNamesStr:
        return joinedAttribute
    else:
        if joinedAttribute is not None:
            joinedAttribute = joinedAttribute.split("_")
            joinedAttribute.reverse()
            joinedAttribute = "_".join(joinedAttribute)
            if joinedAttribute is not None and joinedAttribute.lower() in columnNamesStr:
                return joinedAttribute
            joinedAttribute = None

    return joinedAttribute


def getColumnName(attributeList):
    attributeList = [str(i) for i in attributeList]
    columnToReturn = None;
    listOfColumnNames = getSetOfAllColumns()
    dictionary = PyDictionary()

    columnSynonymDict = {}
    for column in listOfColumnNames:
        if "_" not in column:
            columnSynonymDict[column] = dictionary.synonym(column)

    for attributeToCheck in attributeList:
        columnToReturn = getCorrectAttribute(attributeToCheck, columnSynonymDict)
        if (columnToReturn == None):
            continue
        else:
            return columnToReturn
    if (columnToReturn == None):
        columnToReturn = getAttributeFromJoinedList(attributeList)
    return columnToReturn


def getColumnAndTableName(attributeList):
    column_name = None
    table_name = None
    column_name = getColumnName(attributeList)
    if column_name == None:
        return None, None
    greensheetColumns = getAllColumns("greensheet")
    courseScheduleColumns = getAllColumns("course_sch")
    gradingPolicyColumns = getAllColumns("grading_policy")
    if (column_name in greensheetColumns):
        table_name = "greensheet"
    elif (column_name in courseScheduleColumns):
        table_name = "course_schedule"
    elif (column_name in gradingPolicyColumns):
        table_name = "grading_policy"
    else:
        table_name = "greensheet"
    return column_name, table_name
