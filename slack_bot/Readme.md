# CMPE273-Project
In this project, we have created two bots: Slack-bot and Alexa-bot for CMPE green sheets. Slack-bot uses text-based Slack platform for building the chatbot while, Alexa-bot uses voice-based Alexa Skills Kit platform for building the Alexa-bot. Following are the details for corresponding bots:

## 1. Slack-bot:
Slack-bot is designed to answer your questions. We have created the front end using PHP and MySQL. In the front-end we have created a form which takes in values for all the greensheets and enters into our database. Professors can create multiple greensheets for their respective subjects. Users can add specific questions related to these greensheets and we have created algorithms in python to efficiently query the database and fetch results for the same. 

#### Requirements
1. SlackClient
2. nltk
3. spacy
4. parsedatetime
5. PyDictionary
6. PyEnchant
7. Singular and Plural - Pattern
8. Word Suggestion - Pattern

## 2. Alexa-bot:
Alexa-bot requires one of the Alexa enabled devices (Echo, dot, look, show etc.) for running/using the Alexa-bot. Alexa-bot is a Flask based Python application. This bot is built for CMPE 273 green sheet. It provides much more functionalities apart from just being a bot for green sheet. Please refer to the presentation regarding the same.

#### Requirements
1. Flask
2. NLTK
3. SPACY
4. wikipedia
