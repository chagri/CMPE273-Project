import spacy
from nltk import Tree
from nltk.corpus import stopwords
from file_reader import *
FROM_token = ''
SELECT_token = ''

nlp = spacy.load('en')

def nlp_parseInput(command):
    parsedEx = nlp(command.decode('utf-8'))
    tokens = lemmatizeTokens(parsedEx)
    removeStopWords(tokens)

def removeStopWords(tokens):
    global FROM_token,SELECT_token
    STOPLIST = set(stopwords.words('english'))
    #customize stopwords to add/remove words
    QUE_LIST = ['what','when','who','where']
    STOPLIST = [q for q in STOPLIST if q not in QUE_LIST]
    STOPLIST.append('?')
    tokens_filtered = [tok for tok in tokens if tok not in STOPLIST]
    print "----after stop word filter---"
    print tokens_filtered
    FROM_token = findTableorCol(tokens_filtered,"table")
    #if no table found, do not search for cols
    if(FROM_token != None):
        SELECT_token = findTableorCol(tokens_filtered,"columns")
        if(SELECT_token == None):
            SELECT_token ='*'
    print FROM_token,SELECT_token
    
    #new sentence without stop words
    new_sentence = ' '.join(tokens_filtered)
    #dependecyParse(new_sentence)

def lemmatizeTokens(tokens):
    lemmas = []
    for tok in tokens:
        lemmas.append(tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
    tokens = lemmas
    return tokens

#call file_reader module to find tablename & column name
def findTableorCol(tokens_filtered,key):
    if(key == "table"):
        for t in tokens_filtered:
            table_name = searchDictionary(tableDict,str(t))
            if(table_name != None):
                FROM_token = table_name                
                return FROM_token
    #assuming one column for noe
    elif (key == "columns"):
        for t in tokens_filtered:
            col_name = searchDictionary(columnDict,str(t))
            if(col_name == None):
                SELECT_token = col_name
                return SELECT_token


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

#find dependency between words
def dependecyParse(tokens_new):
    #tokenizeText(parsedEx)
    parseDep = nlp(tokens_new.decode('utf-8'))
    print "---dependency tree----"
    [to_nltk_tree(sent.root).pretty_print() for sent in parseDep.sents] 
    for token in parseDep:            
        #print(token.orth_.encode('utf-8'), token.dep_.encode('utf-8'), token.head.orth_.encode('utf-8'), [t.orth_.encode('utf-8') for t in token.lefts], [t.orth_.encode('utf-8') for t in token.rights])                
        print token.orth_.encode('utf-8'),token.head.orth_.encode('utf-8')      
        leaf= str(token.orth_.encode('utf-8'))
        head=str(token.head.orth_.encode('utf-8')) 
   
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
    # print "---nouns----"
    # print nounArr
    # print "---verbs----"
    # print verbArr
    # print "--Adverbs---"
    # print AdverbArr
    response = "Sure...write some more code then I can do that!"
    #else:
        #response = "I am CMPE bot. How can I help you? Use the *" + EXAMPLE_COMMAND + \
                      #"* command while asking questions."
    return response

