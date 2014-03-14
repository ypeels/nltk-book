'''
Chapter 4 Extras 4.5.1 [NLTK's] Sorting Algorithms
'''

import random
a = range(1000)
random.shuffle(a)                               # good to know


print "oh, we're off into NLTK's sorts, are we?"
from nltk.misc import sort                      # couldn't get nltk.misc.sort to work
print sort.bubble(a[:])                         # ~250k modifications to a
print sort.merge(a[:])                          # ~9k modifications
print sort.quick(a[:])                          # ~2k

