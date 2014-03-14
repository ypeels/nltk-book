'''
Exercise 4.11

Plays with (nested) list copying, and introduces Python's copy.deepcopy()
'''

print __doc__


print "Part 0: Simple shallow copy means sent1 and sent2 refer to the same object."
sent1 = "The quick brown fox jumps over the lazy dog .".split()
sent2 = sent1                                                       # shallow copy
sent1[0] = "A"
print sent1
print sent2
print
assert(sent1 == sent2)


print "Part 1: Range copy is 'deep' and copies CONTENTS to a new list, even for [:]"
sent2_1 = sent1[:]
sent1[0] = "B"
print sent1
print sent2_1
print
assert(sent1 != sent2_1)


print '''Part 2: Range copy only goes as deep as copying contents of CURRENT list, even if they are references!
I.e.,
`
text2 = text1[:]
`

is equivalent to (writing it C-style for greater transparency)
`
text2 = [None] * len(text1)
for i in range(len(text1)):
    text2[i] = text1[i]             # each of these is the same as sent2 = sent1!
`
'''
text1 = []
for i in range(3):
    text1.append(sent1[:])
#print text1 
text2 = text1[:]
text1[1][1] = 'Monty'
print text1
print text2
assert(text1 == text2)


print "Part 3: Python's copy.deepcopy() takes care of such issues for arbitrarily deeply nested lists."
import copy
text3 = copy.deepcopy(text1)
text1[1][1] = 'Python'
print text1
print text3
assert(text1 != text3)
   
