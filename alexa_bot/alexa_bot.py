from flask import Flask
from flask_ask import Ask, statement, question, session
import logging


app = Flask(__name__)
ask = Ask(app, '/summarizer')

if __name__ == "__main__":
    app.run(debug=True)


