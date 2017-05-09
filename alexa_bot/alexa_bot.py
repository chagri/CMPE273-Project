from flask import Flask
from flask_ask import Ask, statement, question, session
import logging


app = Flask(__name__)
ask = Ask(app, '/summarizer')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@app.route('/')
def homepage():
    return  'hello world!'

@ask.launch
def start_skill():
    #welcome_message = "Hello, I am alexa bot for Enterprise Distributed Systems Course by Professor Sithu Aung. What would you like to know about?"
    welcome_message = "hello"
    return  question(welcome_message)


if __name__ == "__main__":
    app.run(debug=True)


