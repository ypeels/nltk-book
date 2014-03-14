'''
Exercise 4.16

Gematria assigns numerical values to words and maps words with the same value to discover hidden meanings...
http://en.wikipedia.org/wiki/Gematria
http://essenes.net/gemcal.htm  - this link was dead

'''

import nltk     # for Index and corpus.words, used in decode()
import random   # for choice() in Decoder.decode()
 	

letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
                'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
                'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
                

                


def gematria(word):                                 # wtf, can't Decoder access free functions? didn't feel like troubleshooting further
    return Decoder().gematria(word)
    
    
class Decoder:
    '''    
    
    Annoyingly, class variables are only initialized on the first call to __init__!?
    So you can't manipulate data in the class object itself without instantiating...
    
    Singleton was too annoying to implement, so I didn't bother...
    
    
    TODO: scan document and update index before scrambling
    - there might be words in the doc but not in the index...
    - current implementation adds words on the fly to the index - so the first instance of a # can't be scrambled
    
    '''
    
    __index = None                                  # lazy initialization (Decoder may go unused)    
    __instance = None
    
    def __initialize_index(self):                   # let's do better than scrambling words in a doc!
        if not Decoder.__index:
            print "Creating Decoder index...",
            Decoder.__index = nltk.Index( (gematria(word), word) 
                        #for word in nltk.corpus.words.words('en') # hmm that's a bit too many weird words
                        #for word in nltk.corpus.stopwords.words('english') # too few words
                        for word in nltk.corpus.words.words('en-basic')
                        )
            print "done."
            
    
    def decode(self, words):                        # class method (singleton, to share table and avoid reinitialization)
        #index = Decoder.__index                    # aliasing does NOT work. STUPID nltk.Index...
        if not Decoder.__index:
            Decoder.__initialize_index(self)        # could move __index behind an accessor function... but for such a short class, this is clearer
        
                                                    # one-liner will crash on punctuation? (__index() returns None)
        #return [random.choice( Decoder.__index[g] ) 
        #        for w in words 
        #        for g in [self.gematria(w)]         # hack to get "local variable"...
        #        ]
        decoded_words = []
        for w in words:
            g = gematria(w)
            if g > 0 and Decoder.__index.has_key(g):
                decoded_words.append(random.choice( Decoder.__index[g] ))
            else:
                decoded_words.append(w)             # don't modify punctuation, OR words not in the index...
                if not Decoder.__index.has_key(g):
                    Decoder.__index[g] = [w]
        return decoded_words
        
        
        
    # ehh, can't call free functions easily from within class!?!?
    def gematria(self, word):
        assert(type(word) == str)
        return sum(self.__value(letter) for letter in word)
        
    def __value(self, letter):
        '''Returns a numerical value for any letter from a-z, or 0 otherwise.'''
        assert(type(letter) == str and len(letter) == 1)
        letter = letter.lower()
        if letter in letter_vals:                       # value table defined above. hey, THAT'S not in the class...
            return letter_vals[letter]
        else:
            return 0                                    # for digits, punctuation, etc.
            
    
        
        
    #def __new__(cls, *args, **kwargs):              # http://stackoverflow.com/questions/42558/python-and-the-singleton-pattern
    #    if not cls.__instance:                      
    #        cls.__instance = super(Decoder, cls).__new__(cls, *args, **kwargs)
    #    return cls.__instance
    def __init__(self):
        if not Decoder.__index:
            Decoder.__index = nltk.Index([])
            Decoder.__index
        
        
            
    

    
    


    
if __name__ == "__main__":
    from nltk.corpus import state_union
    print "Occurrences of the sign of the Devil in SotU addresses past:"
    for file in state_union.fileids():
        print file[:4], sum(1 for word in state_union.words(file) if gematria(word) == 666)

    
    decoded = Decoder().decode(state_union.words())
    print decoded[:200]
    

    