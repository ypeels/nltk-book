# Natural Language Toolkit: code_convert_parens

'''
Example 4.3 from Chapter 4 Extras, 4.2.1: Stacks and Queues
'''

def convert_parens(tokens, debug=False):
    '''Convert a nested phrase into a nested list using a stack
    
    Limitation: same return value regardless of whether parentheses are matched...
    '''
    stack = [[]]
    for token in tokens:
        if token == '(':     # push
            sublist = []
            stack[-1].append(sublist)                       # push NESTED []
            stack.append(sublist)                           # push reference to SAME []
        elif token == ')':   # pop
            stack.pop()                                     # pop running [stuff that was pushed]. 
        else:                # update top of stack
            stack[-1].append(token)
            
        if debug:
            print token, '\t', stack                        # my added instrumentation

    if debug:
        print 
        if len(stack) > 1:                                  # i think the point of pushing 2 copies is so that you can see at a glance where the imbalance begins?
            print "Unmatched parentheses somewhere!?"
            print stack
            print
            
    return stack[0]


if __name__ == "__main__":
    phrase = "( the cat ) ( sat ( on ( the mat ) ) )"
    convert_parens(phrase.split()[:-1], debug=True)         # unmatched!
    
    print "aa", convert_parens(phrase.split())              # [['the', 'cat'], ['sat', ['on', ['the', 'mat']]]]