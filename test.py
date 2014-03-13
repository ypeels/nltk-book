'''
This file contains random snippets of Python code.

Originally created for noodling with Section 4.6
'''



# 4.6.1 Note: remember this? see also python tutorial section 6.1
def _hidden():
    print "Is this function hidden from outside", __file__, "or can you manually call utils._hidden()?"
    

def _hidden_secret_revealed():
    print "Now this function, I'm manually revealing in __all__."
    
def foo():
    print __name__, ".foo()"
    
if __name__ == "__main__":
    print __doc__
    
else:                                           # must be loaded as a module, right?
    
    __all__ = ['_hidden_secret_revealed']
    pass