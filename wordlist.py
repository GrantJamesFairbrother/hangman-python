import requests
from random_word import RandomWords
from time import sleep

def generate_word_list():
    # return ['Stjoepits', 'Kefloepits']
    # return ['Kefloepitst', 'Kefloepitst']
    # return ['the', 'and']
    r = RandomWords()
    
    words = r.get_random_words(
        hasDictionaryDef="true", minCorpusCount=3, minLength=3, maxLength=10, limit=30)
    
    return words
