'''
Exercise 2.26
wait, isn't this basically another trivial one-liner??
'''
from nltk.corpus import wordnet


number_of_hyponyms = number_of_nouns_with_hyponyms = 0
for noun in wordnet.all_synsets('n'):
    n = len(noun.hyponyms())
    if n > 0:
        number_of_hyponyms += n                 # if we're going to do the test anyway (for the right divisor)
        number_of_nouns_with_hyponyms += 1

print 'In the current copy of WordNet:'
print 'nouns with hyponyms:', number_of_nouns_with_hyponyms
print 'total hyponyms:', number_of_hyponyms
print 'branching factor:', float(number_of_hyponyms) / number_of_nouns_with_hyponyms

# i COULD do a one-line with 2 listcomps, but that just feels WAY too inefficient
#print sum([ len(noun.hyponyms()) for 
    
    
    # Answer
    # In the current copy of WordNet:
    # nouns with hyponyms: 16693
    # total hyponyms: 75850 
    # branching factor: 4.54382076319
