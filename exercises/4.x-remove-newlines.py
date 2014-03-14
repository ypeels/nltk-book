'''
Chapter 4 Extras, Exercise 1

A "continuation" of Exercise 3.38 (I knew this looked familiar)

The functions 
'''

import re

def strip1(tokens):
    '''Strips all newlines from all strings in 'tokens'
    
    Use doubly-nested for loops.
    
    Purty clunky...'''
    
    result = []
    for t in tokens:
        tnew = ''
        for ch in t:
            if ch != '\n':
                tnew += ch
        result.append(tnew)
    return result
        


def strip2(tokens):
    '''Strips all newlines from all strings in 'tokens'
    
    Replace the inner loop with a call to re.sub().
    
    MUCH cleaner!
    
    But str.replace() would probably be even better'''    
    result = []
    for t in tokens:
        result.append( strip2.newline_re.sub(r'', t) )
    return result
        
strip2.newline_re = re.compile(r'\n')


def strip3(tokens):
    '''Strips all newlines from all strings in 'tokens'
    Finally, replace the outer loop with call to the map() function, to apply this substitution to each token.
    
    Yes, it's a one-liner, but one that includes map() and a lambda, neither of which is very readble...
    '''
    
    return map( lambda t: strip2.newline_re.sub(r'', t), tokens )
    
    
def strip4(tokens):
    '''Strips all newlines from all strings in 'tokens'
    
    How about a good old listcomp?  That's cleaner than ANYTHING the book proposed...
    '''
    
    return [ t.replace('\n', '') for t in tokens ]

if __name__ == "__main__":
    sent = "The quick brown fox jumps over the lazy dog".replace(' ', '\n ').split(' ')
    #sent = filter(None, sent)               # http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings

    print sent

    print "strip1:", strip1(sent)
    print "strip2:", strip2(sent)
    print "strip3:", strip3(sent)
    print "strip4:", strip3(sent)
    
    assert(strip1(sent) == strip2(sent) == strip3(sent) == strip4(sent))
    