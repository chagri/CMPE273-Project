import time
import os
from slackclient import SlackClient
from file_reader import *
from nlp_parser import *
from SpellCheck import SpellCheckResponse
import MySQLdb
import enchant

d = enchant.Dict("en_US")

def DB_Response(command):
    doc1 = nlp(command.decode("utf-8"))
    db = MySQLdb.connect(host="127.0.0.1",  # your host, usually localhost
                         user="root",  # your username
                         passwd="root1234",  # your password
                         db="test")  # name of the data base

    cur = db.cursor()
    i = 0
    flag = 0
    mainAttributes = []
    responseAttributes = []


    attr = "hello"
    if attr in command:
        response = 'hey there, Try asking me something from your greesheet For Example: cmpe273 section2 spring,2017, who is the instructor?'
        return response


    for word in doc1:
            if word.pos_ == "NOUN":
                if i <2:
                    mainAttributes.append(word)
                    flag = 1
                elif i > 2:
                    responseAttributes.append(word)
                i = i + 1;
    for word in responseAttributes:
           if SpellCheckResponse(word) == False:
            return "Hey I see There Is someting wrong with the Spelling you provided. Do you mean" +  str(d.suggest(word)) + "  instead of "+ str(word)


    if flag == 1:

        # Use all the SQL you like

        query = "SELECT instructor FROM greensheet1  where subject_code=" + "'" + str(mainAttributes[
                                                                                          0]) + "' and section_name =" + "'" + str(
            mainAttributes[1]) + "' and section_period=" + "'" + str(mainAttributes[2]) + "';"


        cur.execute(query)
        response = cur.fetchall()
        return response


