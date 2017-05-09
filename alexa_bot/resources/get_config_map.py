

def get_config_map():
    config_map = {}
    key_to_intent_map ={}
    key_to_intent_map["title"] = "title"
    key_to_intent_map["course name"] = "title"
    key_to_intent_map["name of the course"] = "title"

    key_to_intent_map["office location"] = "office location"

    key_to_intent_map["office hours"] = "office hours"

    key_to_intent_map["email"] = "email"
    key_to_intent_map["e mail"] = "email"
    key_to_intent_map["email id"] = "email"
    key_to_intent_map["mail"] = "email"

    key_to_intent_map["teaching"] = "instructor"
    key_to_intent_map["instructor"] = "instructor"
    key_to_intent_map["professor"] = "instructor"
    key_to_intent_map["name"] = "instructor"

    key_to_intent_map["classroom location"] = "classroom"
    key_to_intent_map["where is classroom"] = "classroom"
    key_to_intent_map["where is classroom located"] = "classroom"

    key_to_intent_map["classroom timing"] = "timing"
    key_to_intent_map["what time is class"] = "timing"
    key_to_intent_map["when is class"] = "timing"

    key_to_intent_map["course website"] = "website"
    key_to_intent_map["what is course website"] = "website"
    key_to_intent_map["where can I find course website"] = "website"

    config_map["title"] = "The title of the course is Enterprise Distributed Systems. Would you like to ask something else?"
    config_map["office location"] = "Engineering Building 281. Would you like to ask something else?"
    config_map["office hours"] = "Wednesday 5pm to 6pm by Appointment Only. Would you like to ask something else?"
    config_map["email"] = "The email of Professor Sithu Aung is sithu.aung at s j s u dot e d u. Would you like to ask something else?"
    config_map["instructor"] = "Professor Sithu Aung is teaching Enterprise Distributed Systems. Would you like to ask something else?"
    config_map["classroom"] = "The classroom is located at Sweeney Hall 100. Would you like to ask something else?"
    config_map["timing"] = "Wednesday 6 pm to 845 pm . Would you like to ask something else?"
    config_map["website"] = "s j s u dot instructure dot com. Would you like to ask something else?"

    return (key_to_intent_map, config_map)