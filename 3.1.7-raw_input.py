'''The built-in function raw_input(str) prompts the user with 'str' for a line of input.'''
s = raw_input("Enter some text: ")

import nltk
print "You typed", len(nltk.word_tokenize(s)), "words."