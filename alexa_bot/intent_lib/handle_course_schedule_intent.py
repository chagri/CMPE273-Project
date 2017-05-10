from nlp_lib.entity_extractor import extract_candidate_words

def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]

def get_course_schedule_intent(phrase):

    if "week 1 schedule" in phrase:
        output = "The topic for week 1 is Distributed Systems Overview. Would you like to ask something else?"
        return output

    elif "week 2 schedule" in phrase:
        output = "The topic for week 2 is Integration Protocols. Would you like to ask something else?"
        return output

    elif "week 3 schedule" in phrase:
        output = "The topic for week 3 is Remote Procedural Calls, also there is lab 1 due. Would you like to ask something else?"
        return output

    elif "week 4 schedule" in phrase:
        output = "The topic for week 4 is RESTful Web Services. Would you like to ask something else?"
        return output

    elif "week 5 schedule" in phrase:
        output = "The topic for week 5 is RESTful Web Services. Would you like to ask something else?"
        return output

    elif "week 6 schedule" in phrase:
        output = "The topic for week 6 is Messaging, also there is assignment 1 due. Would you like to ask something else?"
        return output

    elif "week 7 schedule" in phrase:
        output = "The topic for week 7 is Consistency Models. Would you like to ask something else?"
        return output

    elif "week 8 schedule" in phrase:
        output = "The topic for week 8 is Fault Tolerance (Replication), also there is lab 2 due. Would you like to ask something else?"
        return output

    elif "week 9 schedule" in phrase:
        output = "There will not be a lecture in week 9, it is Spring Recess, however there is assignment 2 due. Would you like to ask something else?"
        return output

    elif "week 10 schedule" in phrase:
        output = "The is Mid-term Exam in week 10. Would you like to ask something else?"
        return output

    elif "week 11 schedule" in phrase:
        output = "The topic for week 11 is Fault Tolerance Sharding, also there is lab 3 due. Would you like to ask something else?"
        return output

    elif "week 12 schedule" in phrase:
        output = "The topic for week 12 is Fault Tolerance Consensus. Would you like to ask something else?"
        return output

    elif "week 13 schedule" in phrase:
        output = "The topic for week 13 is Performance, also there is assignment 3 due. Would you like to ask something else?"
        return output

    elif "week 14 schedule" in phrase:
        output = "The topic for week 14 is Decentralized Applications. Would you like to ask something else?"
        return output

    elif "week 15 schedule" in phrase:
        output = "The topic for week 15 is Project Presentations, also there is lab 4 due. Would you like to ask something else?"
        return output

    elif "week 16 schedule" in phrase:
        output = "The topic for week 16 is question and answer session. Would you like to ask something else?"
        return output

    elif "week 17 schedule" in phrase:
        output = "There is final term in week 17. Would you like to ask something else?"
        return output


    else:
        output = "I did not understand what you are saying. Good bye. Have a nice day."
    return statement(output)
