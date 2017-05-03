import spacy
from nltk import Tree
from file_reader import *

#this import to be changed after adding db module
from event_handler import generateQuery
nlp = spacy.load('en')


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_
    
#find dependency between words
def dependecyParse(command):
    parsedEx = nlp(command.decode('utf-8'))
    print "---dependency tree----"
    [to_nltk_tree(sent.root).pretty_print() for sent in parsedEx.sents]   
    for token in parsedEx:            
        print(token.orth_.encode('utf-8'), token.dep_.encode('utf-8'), token.head.orth_.encode('utf-8'), [t.orth_.encode('utf-8') for t in token.lefts], [t.orth_.encode('utf-8') for t in token.rights])                
        print token.orth_.encode('utf-8'),token.head.orth_.encode('utf-8')
      
        leaf= str(token.orth_.encode('utf-8'))
        head=str(token.head.orth_.encode('utf-8'))
        #response = generateQuery(leaf,head)
    #call to file_reader module -find tablename and column name
    #table_name = searchDictionary(tableDict,'assignment')
    #select_col = searchDictionary(columnDict,'lab')
    #print table_name,select_col
     

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
    print "---nouns----"
    print nounArr
    print "---verbs----"
    print verbArr
    print "--Adverbs---"
    print AdverbArr
    response = "Sure...write some more code then I can do that!"
    #else:
        #response = "I am CMPE bot. How can I help you? Use the *" + EXAMPLE_COMMAND + \
                      #"* command while asking questions."
    return response

