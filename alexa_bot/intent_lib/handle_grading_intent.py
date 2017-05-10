from nlp_lib.entity_extractor import extract_candidate_words

def extract_intent(text):
    entities = extract_candidate_words(text)
    return entities[0]

def get_grading_intent_response(phrase):
    if "quiz" in phrase or 'pop quiz' in phrase:
        output = "The weightage of pop quizzes is 5 percent. Would you like to ask something else?"
        return output

    elif 'lab weightage' in phrase:
        output = "The weightage of labs is 5 percent. Would you like to ask something else?"
        return output

    elif "assignment weightage" in phrase or "what is the weightage of assignments" in phrase:
        output = "The weightage of assignments is 30 percent. Would you like to ask something else?"
        return output

    elif "class project weightage" in phrase or "weightage of class project" in phrase:
        output = "The weightage of class project is 20 percent. Would you like to ask something else?"
        return output

    elif "mid term weightage" in phrase or 'mid term exam weightage' in phrase or "weightage of midterm" in phrase:
        output = "The weightage of mid term exam is 20 percent. Would you like to ask something else?"
        return output

    elif "final term weightage" in phrase or 'final term exam weightage' in phrase or "weightage of final term" in phrase:
        output = "The weightage of final exam is 20 percent. Would you like to ask something else?"
        return output

    elif "final grade" in phrase or 'final grading' in phrase or 'final grading criteria' in phrase:
        output = "Your final grade will be based on labs, assignments, project, exams, and class participation. Would you like to ask something else?"
        return output

    elif "grading pattern" in phrase or 'straight grading or curved' in phrase:
        output = "The grading will be curved. Would you like to ask something else?"
        return output

    else:
        output = "I did not understand what you are saying. Would you like to ask something else?"
        return output
