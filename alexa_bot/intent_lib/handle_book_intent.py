from nlp_lib.entity_extractor import extract_candidate_words

def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]

def get_book_intent(phrase):
    if "recommended book" in phrase or 'recommended book for the course' in phrase or 'which book should I refer' in phrase:
        output = "First, Web Services, by Gustavo Alonso, Fabio Casati, Harumi Kuno and Vijay Machiraju. Second, Enterprise Integration Patterns, by Gregor Hohpe and Bobby Woolf. Third, Restful Web Services, by Leonard Richardson, Sam Ruby and David Hansson. Would you like to ask something else?"
        return output
    else:
        output = "I did not understand what you are saying. Good bye. Have a nice day."
        return output
