import spacy
from SpellCheck import SpellCheckResponse
import MySQLdb
import enchant


d = enchant.Dict("en_US")
nlp = spacy.load('en')
def DB_Response(command):
    doc1 = nlp(command.decode("utf-8"))
    db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                         user="greensheet",  # your username
                         passwd="root1234",  # your password
                         db="slackbot")  # name of the data base

    cur = db.cursor()
    i = 0
    flag = 0
    mainAttributes = []
    responseAttributes = []


    for word in doc1:
            if word.pos_ == "NOUN":
                if i <3:
                    print "input mainAtrr"
                    mainAttributes.append(word)


                elif i > 2:
                    print "Input response Att"
                    responseAttributes.append(word)
                i = i + 1
            if i > 2:
                flag =1
            else:
                flag = 0


    for word in responseAttributes:
           print  "Checking spell check response"
           if SpellCheckResponse(word) == False:
            print "found an spelling error"
            return "Hey I see There Is someting wrong with the Spelling you provided. Do you mean" +  str(d.suggest(word)) + "  instead of "+ str(word)


    if flag == 1:
        print "Finally got every thing All right"
        query = "SELECT instructor FROM greensheet1  where subject_code=" + "'" + str(mainAttributes[0]) + "' and section_name =" + "'" + str(mainAttributes[1]) + "' and section_period=" + "'" + str(mainAttributes[2]) + "';"

        cur.execute(query)
        response = cur.fetchall()
        return response
    else:
        print "Test from Hello"
        response = 'hey there, Try asking me something from your greesheet For Example: cmpe273 section2 spring,2017, who is the instructor?'
        return response

