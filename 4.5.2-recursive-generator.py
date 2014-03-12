'''
An unmarked code snippet from Section 4.5.2

But it seems nontrivial enough to note...
'''



  	

def permutations(seq):
    '''This function is a RECURSIVE GENERATOR.
    
    Such a construction is nontrivial to the point that I haven't seen ANYTHING like it...
    Not in the Python Tutorial, not in Dive into Python...
    
    Is it even worth thinking about?  Or is it just too confusing???
    '''
    if len(seq) <= 1:
        yield seq
    else:
    
        # in all recursively-obtained permutations of seq[1:]   # can't a brother get a comment!?
        for perm in permutations(seq[1:]):                      # for loop ensures that the "generator will run to completion", but only if it is ever triggered???
        
            # insert seq[0] at every possible point in perm     # like my boson/fermion IMC approach
            for i in range(len(perm)+1):
                yield perm[:i] + seq[0] + perm[i:]              # previously seq[0:1], which just made things even more confusing       
                
# permutations([0]) is trivial
# permutations([0, 1])
    # for perm in [1]                                           # permutations([1]) "==" [1] from previous ("by recursion")
        # for i in range(2)
            # i=0: [] + [0] + [1] == [0, 1]
            # i=1: [1] + [0] + [] == [1, 0]
# permutations([0, 1, 2])
    # for perm in ([1, 2], [2, 1])                              # permutations([1, 2]) "==" ([1, 2], [2, 1]) ("by recursion")
    
        # perm = [1, 2]
        # for i in range(3)                                     # lookee, all the perm's have the same length
            # i=0: [] + [0] + [1, 2]    = [0, 1, 2]
            # i=1: [1] + [0] + [2]      = [1, 0, 2]
            # i=2: [1, 2] + [0] + []    = [1, 2, 0]
            
        # perm = [2, 1]
        # same as perm = [1,2] case; swap 1 and 2 in result, haha
# etc.
            



if __name__ == "__main__":
    print __doc__
    print list(permutations(['police', 'fish', 'buffalo']))     # to force the permutations() function to generate all its output, we wrap it with a call to list()
    # [['police', 'fish', 'buffalo'], ['fish', 'police', 'buffalo'],
    # ['fish', 'buffalo', 'police'], ['police', 'buffalo', 'fish'],
    # ['buffalo', 'police', 'fish'], ['buffalo', 'fish', 'police']]
    
    print permutations(['police', 'fish', 'buffalo'])           # <generator object permutations at ...>