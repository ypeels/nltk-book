'''
Section 4.5.1: Functions as Arguments

Whoa, they introduced function objects AND lambda expressions on basically a SINGLE PAGE.

I didn't know you could change the comparison operation of sorted() so easily...
'''

  	

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',
        'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
        
print sorted(sent, lambda x, y: cmp(len(y), len(x)))
# ['themselves', 'sounds', 'sense', 'Take', 'care', 'will', 'take', 'care', 'the', 'and', 'the', 'of', 'of', ',', '.']

# cmp(x, y) returns 1 if x>y, -1 if x<y, and 0 if x == y
print sorted(sent, lambda x, y: -cmp(len(y), len(x)))
# [',', '.', 'of', 'of', 'the', 'and', 'the', 'Take', 'care', 'will', 'take', 'care', 'sense', 'sounds', 'themselves']