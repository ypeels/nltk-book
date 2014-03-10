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

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)              # pre-computes index for EVERY WORD. wouldn't it be better to do this on the fly? especially since this class is used INTERACTIVELY??
                                 for (i, word) in enumerate(text))  # enumerate() from 4.2 (ahhhh)

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = width/4                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '%*s'  % (width, lcontext[-width:])          # string formatting from 3.9
            rdisplay = '%-*s' % (width, rcontext[:width])
            print ldisplay, rdisplay

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


if __name__ == "__main__":
    text = IndexedText(
            nltk.PorterStemmer(),                                   # one of NLTK's "off-the-shelf stemmers"
            nltk.corpus.webtext.words('grail.txt')
            )
    text.concordance('lie')




