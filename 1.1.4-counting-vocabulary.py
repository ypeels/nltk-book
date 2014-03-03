from __future__ import division # Python 3 automatic float division of ints
from nltk.book import * # slow! reading in 9-text corpora


print '''
This section is more Python-based than NLTK-based, so I'm not gonna take much notes on it
'''

# [ text1, ..., text9 ]
texts = [ locals()['text' + str(index+1)] for index in range(9) ]

print "Word counts"
print "-----------"
total_wordcount_width = 7
distinct_wordcount_width = 8
ratio_width = 7

print \
    "Total".rjust(total_wordcount_width), \
    "Distinct".rjust(distinct_wordcount_width), \
    "Ratio".rjust(ratio_width)
    
for text in texts:
    total = len(text)
    distinct = len(set(text))
    print \
        str(total).rjust(total_wordcount_width), \
        str(distinct).rjust(distinct_wordcount_width), \
        str(total / distinct).rjust(ratio_width), \
        text.name
        # meh, gave up on formatting. this doesn't quite work correctly
    #print "{:7d}{:9d}".format(len(text), len(set(text))), text.name
    #print "%7d words" % len(text), text.name # printf-like syntax (older; deprecated?)
    

