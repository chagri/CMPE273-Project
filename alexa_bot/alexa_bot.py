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


# when user wants to listen
@ask.intent('YesIntent')
def share_headlines():
    yes_msg = get_yes_response()
    return statement(yes_msg)


# when user doesn't like and wants, we have a no intent:
@ask.intent('NoIntent')
def no_intent():
    exit_text  = get_no_response()
    return statement(exit_text)

@ask.intent('CMPEIntroIntent')
def intro_intent(IntroDetails):
    print ('CMPEIntroIntent instructor_intent')
    phrase = IntroDetails
    output = get_intro_response(IntroDetails)
    return question(output)

if __name__ == "__main__":
    app.run(debug=True)


