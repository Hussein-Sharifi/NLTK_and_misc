# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:11:03 2024

@author: husse
"""
import nltk
from nltk.corpus import words

def unusual_vocab(text):
    Dict = set(w.lower() for w in nltk.corpus.words.words() if w.isalpha)
    text_Dict = set(w.lower() for w in text if w.isalpha())
    return text_Dict - Dict
    