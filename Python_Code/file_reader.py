
tableDict = {}
columnDict = {}

#test paths
path_tables = '/home/Documents/tables.txt'
path_columns = '/home/Documents/columns.txt'


def createDictionary():
    readFromFile(path_tables, "tables")   
    readFromFile(path_columns, "columns")

#reads from text file and create dictionaries
def readFromFile(filePath, category):
    try:
        infile = open(filePath,'r')
        for line in infile:
            line = line.strip()
            parts = [p.strip() for p in line.split(",")]
            if(category == "tables"):
                tableDict[parts[0]] = (parts[1:])
            elif (category == "columns"):
                columnDict[parts[0]] = (parts[1:])
    except IOError:
        print "Could not read file:", filePath

#search dictionary values to find the key
def searchDictionary(dict_name,word_input):
    for k, v in dict_name.iteritems():
       if word_input in v:
           return k
