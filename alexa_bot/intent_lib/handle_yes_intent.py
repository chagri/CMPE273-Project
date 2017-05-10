import unidecode
from summarizer.get_summary import get_summary

def get_yes_response():
    headlines = get_summary("distributed computing")
    headlines = unidecode.unidecode(headlines)
    headlines_msg = 'Today\'s headlines are: {}'.format(headlines)
    return headlines_msg

