# -*- coding: utf-8 -*-

##########################
# AUTHOR : AMAN SINGHAL
##########################

# Importing third-party modules
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('wordnet')

# Splitting the sentence into words.
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# reducing inflection in words to their root forms such as mapping a group of words to the same stem even if the stem itself is not a valid word in the Language 
def stem(word):
    return lemmatizer.lemmatize(word.lower())

# It is a method of feature extraction with text data. A bag of words is a representation of text that describes the occurrence of words within a document
def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence] 
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag
 