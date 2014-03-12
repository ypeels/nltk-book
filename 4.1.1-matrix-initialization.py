'''
Section 4.1.1 Initialization

"Your Turn"

Brief exploration of "matrix initialization" (multi-dimensional 'arrays')

Haven't I gone over this elsewhere??
Can't find it in tutorials or my notes...


'''

print __doc__


# a combined assignment sets L1 and L2 to the SAME OBJECT, which is problematic because that object is MUTABLE
L1 = L2 = []
L1.append(1)
L2.append(2)
print "combined assignment:", L1, L2, L1 == L2
# combined assignment: [1, 2] [1, 2] True


# Individual assignment to '[]' (the empty list VALUE), however, behaves more as expected
L1 = []
L2 = []
L1.append(1)
L2.append(2)
print "separate assignment:", L1, L2, L1 == L2
# separate assignment: [1] [2] False


# This has great implications for matrix initialization
mcombined = [0,0,0]
mcombined[0] = mcombined[1] = mcombined[2] = []
mcombined[0] += [1]
print "matrix with 'combined' assignment (which is awkward)", mcombined


print '''
Your Turn!
'''
nested = ([],) * 3
nested[0].append(1)
print "matrix with multiplication initialization (even if outer layer is a tuple):", nested
print '''
This is the annoying case, because what you WANT is 3 distinct empty lists...
but what you GET is 3 COPIES of the SAME empty list
Upon reflection, that's what the multiplication operator DOES:
`L = [x] * n` sets L to a list of n COPIES of x
- the confusion only sets in because immutable x are copied in by value, mutable by reference.
'''




rows = 3
cols = 5


print "How about multiplication initialization of TUPLES?"
mtuple = [(0,)*cols] * rows
mtuple[0] = mtuple[0] + (5,)
print mtuple
print "This is fine because TUPLES ARE IMMUTABLE! But for the same reason, the syntax is much more annoying"




mlistcomp = [ [0 for c in range(cols)] for r in range(rows) ]
mlistcomp[rows/2][cols/2] = 1
print "A list comprehension (or equivalent double loop) is fine too, and probably most Pythonic for initializing matrix dimensions"
for row in mlistcomp:
    print row