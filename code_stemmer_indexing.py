'''
Example 3.6 from Section 3.6

"uses object oriented programming techniques that are outside the scope of this book, 
string formatting techniques to be covered in 3.9, 
and the enumerate() function to be explained in 4.2"

uh....ok....
'''

import nltk

# Natural Language Toolkit: code_stemmer_indexing

class IndexedText(object):                                          # object oriented programming techniques that are outside the scope of this book

    def __init__(self, stemmer, text, on_the_fly=False):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)              # pre-computes index for EVERY WORD. wouldn't it be better to do this on the fly? especially since this class is used INTERACTIVELY??
                                 for (i, word) in enumerate(text))  # enumerate() from 4.2 (ahhhh)
        self.__on_the_fly = on_the_fly
    
    def __make_index(self, word):
        if self.__on_the_fly:
            _index = { self._stem(word): [i for (i, w) in enumerate(self._text) if w == word] }  
        else:
            pass

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = width/4                # words of context
        self.__make_index(word)
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '%*s'  % (width, lcontext[-width:])          # string formatting from 3.9
            rdisplay = '%-*s' % (width, rcontext[:width])           # recall that the "*" allows width to be specified at runtime
            print ldisplay, rdisplay

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


if True: #__name__ == "__main__":
    grail = nltk.corpus.webtext.words('grail.txt')
    
    text = IndexedText(
            nltk.PorterStemmer(),                                   # PorterStemmer is one of NLTK's "off-the-shelf stemmers"
            grail
            )
    text.concordance('lie')
    
    text2 = IndexedText(
            nltk.PorterStemmer(),                                   
            grail,
            on_the_fly=True                                         # faster one-time construction, slower per-call concordance()
        )                                                           # for the one-call interactive example, strictly faster (overall)
    text2.concordance('lie')
            
            
    #text3 = IndexedText(nltk.WordNetLemmatizer(), grail)           # WordNetLemmatizer is NOT a stemmer, although it part of module nltk.stem
    #text3.concordance('lie')


