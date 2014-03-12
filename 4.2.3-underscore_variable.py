'''
Section 4.2.3  Combining Different Sequence Types
'''


words = "I turned off the spectroroute".split()
wordlens = [(len(w), w) for w in words]
wordlens.sort()
print ' '.join(w for (_, w) in wordlens)            # "we can use underscore by convention to indicate that we will not use its value"
print '''
BEWARE!!! '_' will come out of this process as having its final value in the for loop
AND the special magic interactive-mode variable '_' for the last PRINTED value will be destroyed!!!
'''

print '''
side note: there are no TUPLE COMPREHENSIONS
- they come out as generator expressions instead
- they probably don't exist because tuples are immutable...
'''

# http://stackoverflow.com/questions/626759/whats-the-difference-between-list-and-tuples-in-python
# http://stackoverflow.com/questions/5150958/lists-in-python
# python tutorial section 5.3 (it was mentioned PRETTY briefly...but it's in my notes there too)
print '''
another side note about Python convention 
- lists are homogeneous by CONVENTION
- tuples are the natural data structure for heterogeneous sequnces
'''

print '''
A note on generation expressions from Section 4.2.4:
Using a generator expression instead of a list comprehension allows data to be "streamed to the calling function"
- instead of allocating storage for the entire list object before processing
'''