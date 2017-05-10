
from nlp_lib.entity_extractor import extract_candidate_words
from resources.get_config_map import get_config_map


def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]


def get_intro_response(phrase):

    extracted_intent = extract_intent(phrase)
    print "extracted intent: ", extracted_intent

    key_to_intent_map, config_map = get_config_map()

    if extracted_intent in key_to_intent_map:
        return config_map[key_to_intent_map[extracted_intent]]

    elif "title" in phrase or "course name" in phrase or "name of the course" in phrase:
        output = "The title of the course is Enterprise Distributed Systems. Would you like to ask something else?"
        return output

    elif "office location" in phrase:
        output = "Engineering Building 281. Would you like to ask something else?"
        return output

    elif "office hours" in phrase:
        output = "Wednesday 5pm to 6pm by Appointment Only. Would you like to ask something else?"
        return output

    elif "email" in phrase or 'e mail' in phrase or 'mail' in phrase or 'email id' in phrase:
        output = "The email of Professor Sithu Aung is sithu.aung at s j s u dot e d u. Would you like to ask something else?"
        return output

    elif "teaching" in phrase or "instructor" in phrase or "professor" in phrase or "name" in phrase:
        output = "Professor Sithu Aung is teaching Enterprise Distributed Systems. Would you like to ask something else?"
        return output

    elif "classroom location" in phrase or "where is classroom" in phrase or "where is classroom located" in phrase:
        output = "The classroom is located at Sweeney Hall 100. Would you like to ask something else?"
        return output

    elif "classroom timing" in phrase or "what time is class" in phrase or "when is class" in phrase:
        output = "Wednesday 6 pm to 845 pm . Would you like to ask something else?"
        return output

    elif "course website" in phrase or 'what is course website' in phrase or 'where can I find course website' in phrase:
        output = "s j s u dot instructure dot com. Would you like to ask something else?"
        return output

    else:
        output = "I did not understand what you are saying. Good bye. Have a nice day."
        return  output

