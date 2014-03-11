'''
Exercise 3.25
Pig Latin, in 3 stages
'''

import re

english_pattern = (

        # leading consonants (including y, which must [?] be consonant if leading)
        r'^(y|[bcdfghjklmnpqrstvwxz]*)'          
        
        # the rest of the word, starting with its first vowel. (assumes internal 'y' is vowel-like)
        r'([aeiouy]\w*)'      

        )
        


piglatin_replacement_pattern = r'\2\1ay'

    
english_re = re.compile(english_pattern)
#piglatin_re = re.compile(piglatin_replacement_pattern) # no, you don't compile the replacement pattern

def pig_latinize_word(word):
    return english_re.sub(piglatin_replacement_pattern, word)
    
    
if __name__ == "__main__":
    for word in "the quick brown fox jumps over the lazy dog school squeak".split():
        print word, "->", pig_latinize_word(word)
    
    