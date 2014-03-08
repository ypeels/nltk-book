print "writing this up ONLY because the cmudict API turned out to be also VERY STUPID to use"

#import nltk.corpus.cmudict  # this does not work!?!?
from nltk.corpus import cmudict
import string

phoneme_dict = dict(cmudict.entries())

def syllables_in_word(word):
    '''Attempts to count the number of syllables in the string argument 'word'.
    
    Limitation: word must be in the CMU dictionary (but that was a premise of the Exercise)
    "Algorithm": no. syllables == no. (0,1,2) digits in the dictionary entry, right??        
    '''
    
    # although listcomps may be readable, you can't insert print statements to instrument them!!
    if phoneme_dict.has_key(word):   
        #return sum([ phoneme.count(str(num)) for phoneme in phoneme_dict[word] for num in range(3) ])
        return len( [ph for ph in phoneme_dict[word] if ph.strip(string.letters)] )   # more destructive; less efficient? NO! see timeit results in my comments below
    else:        
        return 0                           
    

def syllables_in_text(text):
    '''Attempts to count the number of syllables in the string argument 'text'.
    
    Limitation: any "internal punctuation" must be part of the word. (it wouldn't get "this,and" correctly)
    Lets syllables_in_word do the heavy lifting.
    '''

    # ok, so apparently str.split(delim) only works for A SINGLE CHAR delim...
    # anything fancier, and you might want a regex (and its associated performance penalty)
    return sum([syllables_in_word(word.strip(string.punctuation))       # but str.strip(delims) will strip all leading and trailing chars in "delims"!
                for word in text.split()])                              # - alternatives at http://stackoverflow.com/questions/265960/    
    
    
    
if __name__ == "__main__":
    test_text = "'the cow jumped, over the moon'"
    print test_text, "syllables:", syllables_in_text(test_text)
    #syllables_in_text(test_text)
    
    import timeit
    print "time trial:", timeit.Timer('f(test_text)', 'from __main__ import test_text, syllables_in_text as f').timeit(100000)

    # time trial results
    # - sum(): 3.33ish
    # - len(): 1.12ish.  the double-for listcomp LOOKS nicer, but single-for + strip is actually faster!
    
# final thoughts
# the ACTUAL amount of code I wrote was not that much!  only like 6 lines!
# but the correctness of those 6 lines depended heavily on learning various idiosyncracies about Python's string functions... batteries might be included, but what KIND of batteries??
# also, i noticed i'm REALLY bad at tinkering with listcomps... maybe with practice i'll get less inefficient, but...
    # agile mindset: write correct code as quickly as possible (semi-pythonic iterative, for me?), and refactor later...