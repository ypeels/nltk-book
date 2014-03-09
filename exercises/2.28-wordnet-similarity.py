'''Exercise 2.28, or, "finishing Section 2.5: WordNet busywork'''

import nltk
from nltk.corpus import wordnet

# from problem statement, with some Find-Replace laziness
words = [("car", "automobile"), ( "gem", "jewel"), ( "journey", "voyage"), ( "boy", "lad"), ( "coast", "shore"), ( "asylum", "madhouse"), ( "magician", "wizard"), ( "midday", "noon"), ( "furnace", "stove"), ( "food", "fruit"), ( "bird", "cock"), ( "bird", "crane"), ( "tool", "implement"), ( "brother", "monk"), ( "lad", "brother"), ( "crane", "implement"), ( "journey", "car"), ( "monk", "oracle"), ( "cemetery", "woodland"), ( "food", "rooster"), ( "coast", "hill"), ( "forest", "graveyard"), ( "shore", "woodland"), ( "monk", "slave"), ( "coast", "forest"), ( "lad", "wizard"), ( "chord", "smile"), ( "glass", "magician"), ( "rooster", "voyage"), ( "noon", "string")]





# Measure 1: larger min_depth means greater similarity. 
# to RANK these pairs, i have to decide how to assign a SINGLE simplicity metric to the pair
# only checking the first common hypernym for simplicity...
depths = {}

# Measure 2: synset1.path_similarity(synset2)
paths = {}
for w1, w2 in words:
    hypernyms = []
    for s1, s2 in zip(wordnet.synsets(w1), wordnet.synsets(w2)):
        hypernyms += s1.lowest_common_hypernyms(s2)
    depths[(w1, w2)] = max([ h.min_depth() for h in hypernyms])
    
    # Measure 2 is much simpler, since the function only generates a score, not ANOTHER stupid list
    paths[w1, w2] = max([ s1.path_similarity(s2) for s1, s2 in zip(wordnet.synsets(w1), wordnet.synsets(w2)) ])
    
print "\nSimilarity by min_depth (higher means more similar)"
for item in nltk.FreqDist(depths).items():
    print item    
    
print "\nSimilarity by path_similarity"
for item in nltk.FreqDist(paths).items():
    print item

# BOTH of these analyses miss meronym/holonym similarity: 
# e.g., "food" and "fruit" are considered dissimilar, because one is much more specific than the other,
#       even though in normal speech you would not REALLY consider them dissimilar...
    
        

# larger min_depth means greater similarity
# ugh, forget stupid pythonisms for now... bleh! once again, the hard part is grappling with the stupid nltk api
#depths = [  max(h.min_depth())
#            for (w1, w2) in words      
#            for s1, s2 in zip(wordnet.synsets(w1), wordnet.synsets(w2))
#            for h in s1.lowest_common_hypernyms(s2)       # ohhh is THAT how you "declare" a dummy variable in a listcomp?
#            ]



# Measure 2: larger path_similarity means greater similarity


# Results
# -------
# Similarity by min_depth (higher means more similar)
# (('car', 'automobile'), 10)
# (('midday', 'noon'), 9)
# (('journey', 'voyage'), 8)
# (('tool', 'implement'), 6)
# (('asylum', 'madhouse'), 5)
# (('bird', 'crane'), 5)
# (('boy', 'lad'), 5)
# (('brother', 'monk'), 5)
# (('lad', 'brother'), 5)
# (('lad', 'wizard'), 5)
# (('magician', 'wizard'), 5)
# (('monk', 'oracle'), 5)
# (('monk', 'slave'), 5)
# (('coast', 'shore'), 4)
# (('furnace', 'stove'), 4)
# (('gem', 'jewel'), 4)
# (('bird', 'cock'), 3)
# (('coast', 'hill'), 3)
# (('crane', 'implement'), 3)
# (('glass', 'magician'), 3)
# (('cemetery', 'woodland'), 2)
# (('coast', 'forest'), 2)
# (('food', 'fruit'), 2)
# (('shore', 'woodland'), 2)
# (('chord', 'smile'), 1)
# (('food', 'rooster'), 1)
# 
# Similarity by path_similarity
# (('car', 'automobile'), 1.0)
# (('magician', 'wizard'), 1.0)
# (('midday', 'noon'), 1.0)
# (('coast', 'shore'), 0.5)
# (('tool', 'implement'), 0.5)
# (('boy', 'lad'), 0.3333333333333333)
# (('journey', 'voyage'), 0.25)
# (('coast', 'hill'), 0.2)
# (('lad', 'wizard'), 0.2)
# (('monk', 'slave'), 0.2)
# (('shore', 'woodland'), 0.2)
# (('coast', 'forest'), 0.16666666666666666)
# (('bird', 'cock'), 0.14285714285714285)
# (('lad', 'brother'), 0.14285714285714285)
# (('asylum', 'madhouse'), 0.125)
# (('brother', 'monk'), 0.125)
# (('gem', 'jewel'), 0.125)
# (('monk', 'oracle'), 0.125)
# (('bird', 'crane'), 0.1111111111111111)
# (('cemetery', 'woodland'), 0.1111111111111111)
# (('glass', 'magician'), 0.1111111111111111)
# (('crane', 'implement'), 0.1)
# (('food', 'fruit'), 0.1)
# (('chord', 'smile'), 0.09090909090909091)
# (('furnace', 'stove'), 0.07692307692307693)
# (('journey', 'car'), 0.07692307692307693)
# (('forest', 'graveyard'), 0.07142857142857142)
# (('food', 'rooster'), 0.0625)
# (('noon', 'string'), 0.058823529411764705)
# (('rooster', 'voyage'), 0.041666666666666664)

