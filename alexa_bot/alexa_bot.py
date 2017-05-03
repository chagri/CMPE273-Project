from flask import Flask
from flask_ask import Ask, statement, question, session
from config import get_pwd
import wikipedia



import json
import requests
import time
import unidecode
import wikipedia
import logging


app = Flask(__name__)
ask = Ask(app, '/summarizer')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@app.route('/')
def homepage():
    return  'hello world!'

@ask.launch
def start_skill():
    welcome_message = "Hello, what would you like to know about?"
    return  question(welcome_message)

# when user wants to listen
@ask.intent('YesIntent')
def share_headlines():
    #headlines = get_wiki_head('sjsu')
    headlines = "This skill works!"
    headlines = unidecode.unidecode(headlines)
    headlines_msg = 'Today\'s headlines are: {}'.format(headlines)
    return statement(headlines_msg)


@ask.launch
def start_skill():
    welcome_message = "Hello, what would you like to know about?"
    return  question(welcome_message)


if __name__ == "__main__":
    app.run(debug=True)
