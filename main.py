import random
from difficulty import Difficulty

def load_words(difficulty_level):
    """Loads random words from a dictionary with length equal to difficulty"""
    dictionary = open("popular.txt").readlines()
    words = []
    while len(words) < 10:
        word = random.choice(dictionary)
        word = word.rstrip('\r\n')
        if len(word) == difficulty_level:
            if word not in words:
                words.append(word)
    return words
