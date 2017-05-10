from flask import Flask
from flask_ask import Ask, statement, question, session
import logging

from intent_lib.handle_yes_intent import get_yes_response
from intent_lib.handle_no_intent import get_no_response
from intent_lib.handle_cmpe_intro_intent import get_intro_response
from intent_lib.handle_grading_intent import get_grading_intent_response
from intent_lib.handle_book_intent import get_book_intent
from intent_lib.handle_course_schedule_intent import get_course_schedule_intent
from intent_lib.handle_help_intent import get_help_response
from summarizer.get_summary import get_summary





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

@ask.intent('HelpIntent')
def share_headlines():
    help_msg = get_help_response()
    return question(help_msg)


@ask.intent('CMPEIntroIntent')
def intro_intent(IntroDetails):
    print ('CMPEIntroIntent instructor_intent')
    phrase = IntroDetails
    output = get_intro_response(IntroDetails)
    return question(output)

@ask.intent('GradingIntent')
def grading_intent(WeightageDetails):
    print ('GradingIntent')
    phrase = WeightageDetails
    output = get_grading_intent_response(phrase)
    return question(output)    

@ask.intent('BookIntent')
def grading_intent(SuggestedBooks):
    print ('BookIntent')
    phrase = SuggestedBooks
    output = get_book_intent(phrase)
    return question(output)

@ask.intent('CourseScheduleIntent')
def course_intent(CourseSchedule):
    print ("CourseScheduleIntent")
    phrase = CourseSchedule
    output = get_course_schedule_intent(phrase)
    return question(output)


@ask.intent('KnowledgeIntent')
def instructor_intent(CourseTopic):
    out_sum = get_summary(CourseTopic)
    return question('Here is the summary for {}'.format(CourseTopic) + out_sum)


@ask.intent('SummaryIntent')
def input_intent(Subject):
    out_sum = get_summary(Subject)
    return question('Here is the summary for {}'.format(Subject) + out_sum)



if __name__ == "__main__":
    app.run(debug=True)


