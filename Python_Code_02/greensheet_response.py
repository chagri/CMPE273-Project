import time
import os
from slackclient import SlackClient
from file_reader import *
from nlp_parser import *
import MySQLdb

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
    sideAttributes = []
    attr = "hello"

    for word in doc1:

        if (i < 3):

            # check for side Attributes
            if word.pos_ == "NOUN":
                mainAttributes.append(word)
                flag = 1
            i = i + 1

    if flag == 1:

        # Use all the SQL you like

        query = "SELECT instructor FROM greensheet1  where subject_code=" + "'" + str(mainAttributes[
                                                                                          0]) + "' and section_name =" + "'" + str(
            mainAttributes[1]) + "' and section_period=" + "'" + str(mainAttributes[2]) + "';"

        cur.execute(query)
        response = cur.fetchall()
        return response

    elif attr in command:
        response = 'hey there, Try asking me something from your greesheet For Example: cmpe273 section2 spring,2017, who is the instructor?'
        return response
