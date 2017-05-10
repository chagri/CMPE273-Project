
from nlp_lib.entity_extractor import extract_candidate_words

def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]