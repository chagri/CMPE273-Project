#!/usr/bin/python
# encoding=utf8

import nltk
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


def split_to_sents(text):
    sents = sent_detector.tokenize(text)
    return sents

def clean_text(text):
    sents = split_to_sents(text)
    cleaned_sent = [re.sub('\W+', ' ', sent.lower()) for sent in sents]
    return " . ".join(cleaned_sent)
