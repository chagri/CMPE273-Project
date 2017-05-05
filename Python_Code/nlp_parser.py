import spacy
import re
from nltk import Tree
from nltk.corpus import stopwords
from file_reader import *
from generateQuery import *
FROM_token = ''
cols = list()
CMD = ''
nlp = spacy.load('en')
subjectcode = ''
sectionname = ''
sectionperiod = ''

def nlp_parseInput(command):
    global CMD ,subjectcode ,sectionname, sectionperiod
    print "command ",command     

    GREETLIST = ['hi','hello','hey','hi there','hey there'] 
    if command in GREETLIST:
        response = "hello, try asking something from greesheet. For Example: cmpe273 section2 spring2017, who is the instructor?"
        return response    
              
    if len(command.strip().split()) == 1:
        return None
        
    primaryKey = command.split(' ')
    subjectcode = primaryKey[0]
    sectionname = primaryKey[1]
    sectionperiod = primaryKey[2]

    occur = 3  
    indices = [x.start() for x in re.finditer(" ", command)]    
    command = command[indices[occur-1]+1:]
        
    CMD = command   
    parsedEx = nlp(command.decode('utf-8'))

    tokens = lemmatizeTokens(parsedEx)    
    return removeStopWords(tokens)

def removeStopWords(tokens):
    global FROM_token,CMD
    STOPLIST = set(stopwords.words('english'))
    #customize stopwords to add/remove words    
    QUE_LIST = ['what','when','who','where','how']
    STOPLIST = [q for q in STOPLIST if q not in QUE_LIST]
    STOPLIST.append('?')
    tokens_filtered = [tok for tok in tokens if tok not in STOPLIST]    
    FROM_token = findTableorCol(tokens_filtered,"table")    
    #if no table found, do not search for cols
    if(FROM_token != None):
        cols = findTableorCol(tokens_filtered,"columns")        
        if(len(cols) == 0):
            cols.append("*")
    #new sentence without stop words
    #new_sentence = ' '.join(tokens_filtered)
        print FROM_token,cols
    return dependecyParse(CMD)

def lemmatizeTokens(tokens):
    lemmas = []
    for tok in tokens:
        lemmas.append(tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
    tokens = lemmas
    return tokens

#call file_reader module to find tablename & column name
def findTableorCol(tokens_filtered,key):
    global cols    
    if(key == "table"):
        for t in tokens_filtered:
            table_name = searchDictionary(tableDict,str(t))
            #read columns only when we know the table            
            if(table_name != None):
                FROM_token = table_name.strip("['']")
                readFromFile(FROM_token,"columns")
                return FROM_token
    #add columns to list
    elif (key == "columns"):
        for t in tokens_filtered:
            col_name = searchDictionary(columnDict,str(t))
            if(col_name != None):
                cols.append(col_name.strip("['']"))
                #SELECT_token = col_name.strip("['']")
                #return SELECT_token
        return cols

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

#find dependency between words
def dependecyParse(command):
    parseDep = nlp(command.decode('utf-8'))
    #print command
    print "---dependency tree----"
    [to_nltk_tree(sent.root).pretty_print() for sent in parseDep.sents] 
    for token in parseDep:                 
        #print(token.orth_.encode('utf-8'), token.dep_.encode('utf-8'), token.head.orth_.encode('utf-8'), [t.orth_.encode('utf-8') for t in token.lefts], [t.orth_.encode('utf-8') for t in token.rights])                
        #print token.orth_.encode('utf-8'),token.head.orth_.encode('utf-8')      
        leaf= str(token.orth_.encode('utf-8'))
        head=str(token.head.orth_.encode('utf-8'))
        #call generateQuery module
        searchCondition = "%"+leaf+"%""%"+head+"%"
        if FROM_token:            
            output = generateQuery(FROM_token,cols,searchCondition,subjectcode, sectionname,sectionperiod )
            if output:
                return output                                

    for token in parseDep:                 
        token= "%"+str(token)+"%"
        if FROM_token:
            output = generateQuery(FROM_token,cols,token,subjectcode, sectionname,sectionperiod)
            if output:
                return output 

#method to find nouns, verbs ..
def process_command(command):
    #command = "who is the professor for CMPE273 for spring 2017?"
    tokens = nlp(command.decode('utf-8'))
    verbArr =[]
    nounArr = []
    numArr =[]
    entityArr =[]
    AdverbArr = []
    #filter out nouns
    for np in tokens.noun_chunks:
        nounArr.append(np)
        #filter out entities
        for ent in tokens.ents:
            entityArr.append(ent)
            #filter out verbs, numbers and adverbs
            for token in tokens:
                #print token,token.pos_
                if "VERB" in token.pos_:
                    verbArr.append(token)
                elif "NUM" in token.pos_:
                    numArr.append(token)
                elif "ADV" in token.pos_:
                    AdverbArr.append(token)
    response = "Sure...write some more code then I can do that!"
    #else:
        #response = "I am CMPE bot. How can I help you? Use the *" + EXAMPLE_COMMAND + \
                      #"* command while asking questions."
    return response
