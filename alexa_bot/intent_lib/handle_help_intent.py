from nlp_lib.entity_extractor import extract_candidate_words

def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]

def get_help_response():

    return_msg = 'I can help you with anything about Enterprise Distributed Course Details. Currently, I support instructor details, \
    course topics,  exam details, weightage details etc.. Additionaly, I can also summarize any given topic for you. Just say explain \
    distributed systems ?'
    return return_msg
