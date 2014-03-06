# Natural Language Toolkit: code_random_text
import nltk

# tsk tsk, no docstring in the original
def generate_model(cfdist, word, num=15):
    ''' Plays a "word association game"  starting with "word" for "num" iterations.
        
        Precondition: cfdist = ConditionalFreqDist( conditions=words, samples=associated_words )
    '''
    for i in range(num):                    # num = iterations 
        print word,
        word = cfdist[word].max()           # next word is whatever word is MOST associated with the previous word

        
if __name__ == '__main__':
    text = nltk.corpus.genesis.words('english-kjv.txt')
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams) # [_bigram-condition] - in this example, word2 is associated with word1 if it FOLLOWS it (completes a bigram with it) in "text"
    
    print cfd['living']
    generate_model(cfd, 'living')           # I would call this PSEUDO-random text at best...

# TODO
# - move into a class? seems like you should be able to call cfd.generate_model('living')
# - rule out punctuation, which gives silly results (try 'son')

# note "funnel"
# ',' -> 'and' -> 'the' -> 'land' -> of' -> 'the' -> ...
                                
