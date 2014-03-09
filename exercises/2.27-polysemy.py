'''
Exercise 2.27

These final "starred" exercises aren't harder or anything...
they just cover on the WordNet API, which was just the last section...
'''

from nltk.corpus import wordnet     # import nltk.corpus.wordnet does NOT work!



# Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.
# "The polysemy of a word is the number of senses it has."
# However, are we supposed to average over words, or synsets?  I am going to assume the former.

# from help(wordnet): 
# Data and other attributes defined here:
# ADJ = 'a'
# ADJ_SAT = 's'
# ADV = 'r'
# NOUN = 'n'
# VERB = 'v'

word_type_names = { 'n':'noun', 'v':'verb', 'a':'adjective', 'r':'adverb' }
word_types = word_type_names.keys()

for type in word_types:         
    print "average polysemy for", word_type_names[type], ":",
    words = { ss.name.split('.')[0] for ss in wordnet.all_synsets(type) }       # ss.name == 'car.n.01', say 
    print sum([len(wordnet.synsets(w)) for w in words]) / float(len(words))     # api "algorithm" from problem statement

# answer    
# average polysemy for adjective : 2.52227934876
# average polysemy for adverb : 1.91114754098
# average polysemy for verb : 4.23924731183
# average polysemy for noun : 1.69155650828

# yes, listcomps make these programs LOOK SHORT
# but they also make the CONTENT PER LINE a bit too high for my taste...
    # and you really lose the ability to write meaningful variable names for intermediate results...