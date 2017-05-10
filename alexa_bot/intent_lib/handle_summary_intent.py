
import wikipedia
import unidecode

def get_summary(input_str):
    wiki_summary = wikipedia.summary(input_str)
    wiki_summary = wiki_summary.split('\n')[0]
    wiki_summary = unidecode.unidecode(wiki_summary)
    return wiki_summary