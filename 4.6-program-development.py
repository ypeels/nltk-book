'''
4.6.1 Structure of a Python Module

Recall
- module.'__file__' returns the absolute path where module lives
- module names beginning with underscore will NOT be visible outside the file via "from file import *" - tutorial 6.1
    - like so much in python, this is just a CONVENTION, which you can easily override - even using `from utils import _hidden` like below
    - also don't forget that "from file import *" is considered bad practice, except at the interactive prompt
'''

if __name__ == '__main__':
    print __doc__
    

import test
from test import *
print "test.__all__:", test.__all__
_hidden_secret_revealed()                   # this was revealed in test.__all__


# should raise NameError - see error message for info
try:
    _hidden()
except NameError:
    print "NameError(_hidden) - See, `from xxx import * SKIPS names starting with underscore unless overridden in __all__"
else:
    raise Exception("What? test._hidden() should be hidden...")
print
    
    
print "But you can always access it directly ANYWAY:"
test._hidden()
print
    

# should raise NameError - see error message for info
try:
    foo()
except NameError:
    print "NameError(foo) - Also, notice that the price of futzing with __all__ is BREAKING DEFAULT BEHAVIOR for 'import *'!!"
else:
    print "You can make foo() visible (i.e., get this block to execute) by commenting out the definition of '__all__' in test.py"
    raise Exception("What? test.foo() should be hidden becuase of futzing with test.__all__...")

print '''
Reduced to calling test.foo() manually, despite import *. Like an ANIMAL!
If you're gonna fuck with test.__all__, why don't you just declare a public handle instead??
'''

#print test.__all__

