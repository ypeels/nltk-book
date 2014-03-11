'''
Exercise 3.25
Pig Latin, in 3 stages
'''

import nltk     # for word_tokenize(), because I'm lazy (i.e. part of NLTK's target audience)
import re

english_pattern = (

        # leading consonants (including y, which must [?] be consonant if leading). oops, 'y' was part of phase 3...
        #r'^(y|[bcdfghjklmnpqrstvwxz]*)'        # phase 1
        r'^(y|[bcdfghjklmnprstvwxz(?:qu)]*)'    # phase 3: (?:qu) to detect leading "qu"
        
        # the rest of the word, starting with its first vowel. (assumes internal 'y' is vowel-like)
        r'([aeiouy]\w*)'      

        )
        


piglatin_replacement_pattern = r'\2\1ay'

    
english_re = re.compile(english_pattern)
#piglatin_re = re.compile(piglatin_replacement_pattern) # no, you don't compile the replacement pattern

def pig_latinize_word(input_word):    
    output_word = english_re.sub(piglatin_replacement_pattern, input_word.lower())
    if input_word.istitle():                            # phase 3: maintain capitalization    
        output_word = output_word.title()
    return output_word

    #return english_re.sub(piglatin_replacement_pattern, word)
    
def pig_latinize_text(text):
    words = [ word for word in nltk.word_tokenize(text) if word.isalpha() ]
    
    # instead of worrying about punctuation, i'll just MODIFY WORDS in the original string
    for w in set(words):
        text = text.replace(w, pig_latinize_word(w))            # remember, str is immutable!
    return text
    
    
if __name__ == "__main__":
    sentence = "The quick brown fox jumps over the Lazy Dog School squeak"
    for word in sentence.split():
        print word, "->", pig_latinize_word(word)
    
    print pig_latinize_text(sentence)