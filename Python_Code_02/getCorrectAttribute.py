from PyDictionary import PyDictionary

def getCorrectAttribute(attributeToCheck):
 queryValue = None;
 dictionary=PyDictionary()
 #listOfColumnNames = getAllColumns(“greensheet1”)
 listOfColumnNames = ["instructor","exam","section name","section period"]

 if(attributeToCheck in listOfColumnNames):
    return attributeToCheck

 columnSynonymDict = {}
 for column in listOfColumnNames:
   columnSynonymDict[column] = dictionary.synonym(column)

 for key, value in columnSynonymDict.iteritems():

   if attributeToCheck in value:
       queryValue = key
       break;

 return queryValue

