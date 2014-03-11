'''
Exercise 3.41

should be trivial, right?  still, couldn't resist...
'''

print __doc__

  	

words = ['attribution', 'confabulation', 'elocution',
         'sequoia', 'tenacious', 'unidirectional']
         
def iterative_answer():
    vsequences = set()
    for word in words:
        vowels = []
        for char in word:
            if char in 'aeiou':
                vowels.append(char)
        vsequences.add(''.join(vowels))
    return sorted(vsequences)
    # ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa'] 
    
    
    

#vowels = 'aeiou'                       # yes, it really is a one-liner again
listcomp_answer = sorted([ ''.join([ch for ch in word if ch in 'aeiou']) for word in words ])
print listcomp_answer
print "equivalent to iterative answer?", listcomp_answer == iterative_answer()