# Example 2.8 from Section 2.4
# Natural Language Toolkit: code_unusual
import nltk

def unusual_words(text):
    '''This function returns all words in 'text' not found in /usr/share/dict/words.
    '''
    text_vocab = set(w.lower() for w in text if w.isalpha())           # compute vocabulary of 'text' (set of all its words)
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())  # /usr/share/dict/words (with extra set() to be sure members are unique)
    #unusual = text_vocab.difference(english_vocab)                     
    #return sorted(unusual)
    return sorted(text_vocab - english_vocab)                          # set operations are even clearer!


if __name__ == '__main__':
    print "100 unusual words in Sense and Sensibility:", unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))[:100]
    print "100 unusual words in the Chat Corpus:", unusual_words(nltk.corpus.nps_chat.words())[:100]
