import wikipedia
import unidecode

from common.clean_text import split_to_sents


def get_summary(input_str):
    wiki_summary = wikipedia.summary(input_str)
    wiki_summary = wiki_summary.split('\n')[0]
    wiki_summary = split_to_sents(wiki_summary)[:2]
    wiki_summary  = " ".join(wiki_summary)
    wiki_summary = unidecode.unidecode(wiki_summary)
    return wiki_summary

