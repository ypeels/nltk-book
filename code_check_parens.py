# Natural Language Toolkit: code_check_parens

'''
Example 4.2 from Chapter 4 Extras, Section 4.2.1: Stacks and Queues
'''


def check_parens(tokens):
    '''Figure 4.2: Check whether parentheses are balanced
    
    "overkill because we could have done a direct count: phrase.count('(') == phrase.count(')')"
    
    Limitation: will crash if there are more closing than opening parens'''
    stack = []
    for token in tokens:
        if token == '(':     # push
            stack.append(token)
        elif token == ')':   # pop
            stack.pop()
    return stack                                    # evaluates to False 

if __name__ == "__main__":
     phrase = "( the cat ) ( sat ( on ( the mat )"
     print check_parens(phrase.split())             # ['(', '(']
     
     try:
        print check_parens(")")
     except IndexError as e:
        print "See? the stack.pop() call can't handle it when empty...", e.message
        #raise IndexError(e)                        # if you really wanted to get the user's attention...meh