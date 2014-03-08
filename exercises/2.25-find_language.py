'''
Exercise 2.25

This exercise DOES look trivial...

But fine, I'll do it, just to see how compact and Pythonic I can make it...
Also to review the uhdr api briefly
'''

from nltk.corpus import udhr

latin_languages = [ lang for lang in udhr.fileids() if lang.endswith('-Latin1') ]


def find_language(word):
    '''Returns list of languages for which word is found in 
    
    Limitations:
    - currently only checks nltk.corpus.udhr (universal declaration of human rights, i.e., whether word is "universal", haha)
    - currently only checks Latin-1 languages in udhr
    '''
    
    # trivial, like i said. right??
    import string  # to strip off punctuation - my little finishing touch
    return [ lang for lang in latin_languages 
                if word.strip(string.punctuation) in set(udhr.words(lang)) ]
    

    
if __name__ == "__main__":
    words = 'The quick brown fox jumps over the lazy dog.'.split()
    for w in words:
        print w, find_language(w)
        