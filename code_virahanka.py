# Natural Language Toolkit: code_virahanka

'''
Figure 4.12: Four Ways to Compute Sanskrit Meter: 
(i) iterative; [actually, recursive]
(ii) bottom-up dynamic programming; 
(iii) top-down dynamic programming; and 
(iv) built-in memoization.

This is a "brief introduction to dynamic programming. We will encounter it again in 8.4."
'''

def virahanka1(n):
    '''Naively computes all permutations of S(1) and L(2) that sum to n.
    
    Recomputes virahanka(n-1) wastefully for each occurrence in the tree.
    Wasteful! You waste!!'''
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahanka1(n-1)]          # (S)hort syllables take up 1 unit of length
        l = ["L" + prosody for prosody in virahanka1(n-2)]          # (L)ong syllables take up 2 units of length
        return s + l

def virahanka2(n):
    '''"Bottom-up dynamic programming" to iteratively build the Virahanka table up from length 1, stopping as soon as we reach n.
    So called because we "solve smaller problems on the way to solving larger problems."
    "Crucially, each sub-problem is only ever solved once."
    
    [If you ask me, this just means virahanka1() was VERY poorly designed...]
    '''
    lookup = [[""], ["S"]]
    for i in range(n-1):
        s = ["S" + prosody for prosody in lookup[i+1]]
        l = ["L" + prosody for prosody in lookup[i]]
        lookup.append(s + l)
    return lookup[n]

def virahanka3(n, lookup={0:[""], 1:["S"]}):
    '''"Top-down dynamic programming" to RECURSIVELY build the Virahanka table.
    
    NOTE: this function will breaks if the user calls this function with a second argument that is anything except a valid "Virahanka dictionary"!!
    
    Is this REALLY top-down? Just because it STARTS larger sub-problems before starting the smaller ones??  
    The "static variable 'lookup'" is still built up from smaller to larger strings...
    
    The book claims that this is less wasteful than virahanka2() because it is top-down,
    but the real reason is that virahanka2() doesn't bank results between calls...
    That has NOTHING to do with top-down vs bottom-up...    
    
    And for a SINGLE call like in their test code, there is NO recomputation!
    If anything, the recursive version in that case would have extra overhead from the extra function calls...
    '''
    if n not in lookup:                                             # check cached "static variable" if results have been computed before
        s = ["S" + prosody for prosody in virahanka3(n-1)]
        l = ["L" + prosody for prosody in virahanka3(n-2)]
        lookup[n] = s + l                                           # "bank" new results in the "static variable"    
    return lookup[n]

    
from nltk import memoize
@memoize
def virahanka4(n):
    '''Same as virahanka3(), but with the "memoize" decorator to auto-implement result caching instead of hacky default variable
    
    ''use a Python "decorator" called memoize, which takes care of the housekeeping work done by virahanka3() without cluttering up the program.
    This "memoization" process stores the result of each previous call to the function along with the parameters that were used.''
    
    I actually haven't gone over Python decorators yet, have I??
    '''
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]                                                # seed data for memoize
    else:
        s = ["S" + prosody for prosody in virahanka4(n-1)]
        l = ["L" + prosody for prosody in virahanka4(n-2)]
        return s + l


if __name__ == "__main__":
    print __doc__

    #print virahanka1(4)
    for i in range(21):                                             
        print "Checking Virahanka for length", i
        try:
            all_v = virahanka1(i), virahanka2(i), virahanka3(i), virahanka4(i)
            assert(all_v[0] == all_v[1] == all_v[2] == all_v[3])
        except AssertionError:
            print "Uh oh, one of the virahanka methods didn't match..."
            #print all_v
            
            print "and here are all the PAIRWISE differences:"
            for ia in range(len(all_v)-1):
                for ib in range(ia+1, len(all_v)):
                    if all_v[ia] != all_v[ib]:
                        print ia+1, "^", ib+1, set(all_v[ia]) ^ set(all_v[ib])
               
            raise Exception("Virahanka version mismatch at n = " + str(i))
        else:
            if i < 7:                                               # gets SLOW for large i, even 20
                print all_v[0]
            else:
                print "Output suppressed to keep runtime reasonable"
            print "All versions match!!"
            print
    