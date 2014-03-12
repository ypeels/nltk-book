'''
Section 4.2.2  Operating on Sequence Types
'''

print '''
I've wanted to do reverse lists before but not known how!
Should've known it'd be analogous to 'sorted'...
'''

L = range(10)
Lr = reversed(L)
Ls = sorted(L)

print '''
But BEWARE: reversed() and sorted() return DIFFERENT TYPES!!!"
- sorted() returns a brand-spanking-new object
- reversed() returns an ITERATOR, 

- list.sort() and list.reverse(), of course, modify the list in place
'''

print "Lr:",
for item in Lr: print item,
print
try:
    print "direct access? Lr[0] =", Lr[0]
except TypeError:
    print "TypeError!  see, you can't access items in a return value of reverse()"
print

print "Ls:",
for item in Ls: print item,
print

print
print "and after all that, the original list is still unmodified"
print L             # unmodified!  L.reverse() would modify it in place, like L.sort()
                    # however, L.reversed() and L.sorted() do not exist, probably to avoid typo errors?
                    
                    
print "And here's an idiomatic way of performing swap() using tuple packing/unpacking:"
L[0], L[1] = L[1], L[0]
print L