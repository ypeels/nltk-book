'''
Exercise 4.6

Does the method for creating a sliding window of n-grams behave correctly for the two limiting cases: 
n = 1, and n = len(sent)?


wtf?? what method???

ohhh from Section 4.3.3:
"
>>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
>>> n = 3
>>> [sent[i:i+n] for i in range(len(sent)-n+1)]
[['The', 'dog', 'gave'],
 ['dog', 'gave', 'John'],
 ['gave', 'John', 'the'],
 ['John', 'the', 'newspaper']]

It is quite tricky to get the range of the loop variable right. 
Since this is a common operation in NLP, NLTK supports it with functions bigrams(text) and trigrams(text), 
and a general purpose ngrams(text, n).
"
'''

def ngrams(sent, n):
    '''Simple function that returns all n-grams from list of words 'sent'. 
    
    No error checking.
    '''
    return [sent[i:i+n] for i in range(len(sent)-n+1)]
    
if __name__ == "__main__":
    sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
    print ngrams(sent, 3)
    
    grams = ngrams(sent, 1)
    print "ngrams(sent, 1): ", grams
    print "Does the method behave correctly for n = 1?"    
    print grams == [ [word] for word in sent]                   # True
    print
    
    lengrams = ngrams(sent, len(sent))
    print "ngrams(sent, len(sent)): ", lengrams
    print "Does the method behave correctly for n = len(sent)?"    
    print lengrams == [sent]                                    # True
    print