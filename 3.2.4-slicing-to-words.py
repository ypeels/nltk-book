'''"Your Turn" in subsection "Accessing Substrings"'''

import string   # for whitespace + punctuation

def tokenize(str):
    '''My attempt at pulling out words from a sentence, using slice notation "only"...
    str.split() would be cheating!
    but let's allow str.strip(), to avoid dealing with STUPID boundary cases

    This is indeed much more laborious than str.split()
    
    Limitation: treats punctuation as delimiters instead of tokens
    '''
    
    str = str.strip()
    assert(not str[0].isspace() and not str[-1].isspace())
    
    space_indices = [ index for index in range(len(str)) 
                            if str[index] in (string.whitespace + string.punctuation)
                            ]
    
    if len(space_indices) == 0:
        print "Input string is already a single word!"
        return [str]        
    elif len(space_indices) == 1:
        return [ str[0:the_only_space], str[the_only_space+1, len(str)] ]
    assert(len(space_indices) >= 2)
    
    result = []
    left_index = 0
    for right_index in space_indices:
        result.append( str[left_index:right_index] )
        
        # prepare for next iteration
        left_index = right_index+1
        
    # we stripped the string of leading/trailing whitespace, remember??
    assert(not str[-1].isspace())
    result.append(str[left_index:])
        
    
    return [word for word in result if not word.isspace() and len(word) > 0]
    
if __name__ == "__main__":
    print tokenize('   the quick brown fox jumps   over the lazy    ')
    
    