print "writing this up ONLY because the cmudict API turned out to be also VERY STUPID to use"

#import nltk.corpus.cmudict  # this does not work!?!?
from nltk.corpus import cmudict
import string

phoneme_dict = dict(cmudict.entries())

def syllables_in_word(word):
    print word
    if phoneme_dict.has_key(word):        
        return len( [ph for ph in phoneme_dict[word] if ph.strip(string.letters)] )   # no. syllables == no. (0,1,2) digits, right??        
    else:
        return 0                           
    

def syllables_in_text(text):
    delims = string.punctuation + string.whitespace
    for word in text.split(): print word
    
    return sum([syllables_in_word(word) for word in text.strip(delims).split(delims)])  # TODO: strip strings of punctuation. wtf, i thought this is supposed to be EASY in python
    
if __name__ == "__main__":
    test_text = "'the cow jumped over the moon'"
    print test_text, "syllables:", syllables_in_text(test_text)
    #syllables_in_text(test_text)
