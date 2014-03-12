'''
Section 4.4.2  Parameter Passing

What Python REALLY does is pass mutable objects by POINTER...

If it were pass by value (like the book claims), then the changes below would not propagate back
If it were pass by reference like you might think, then the changes below WOULD propagate back to the caller

It's really more like "pass by pointer", with:
- parameters assignable to other types, like some crazy union in C
- automatic pointer dereferencing on access (with square brackets or function calls, as below)
- pointers passed by VALUE, so that you could in principle destroy the pointer without affecting its reference

If you ask me, this is annoyingly subtle... 
subtle to the point that it could easily introduce insidious bugs if you'd never worked through it, and even if you had...
'''

print __doc__

  	

def set_up(word, properties):
    '''Simple example function that modifies its second argument by "reference"'''
    word = 'lolcat'
    properties.append('noun')           # properties->append('noun') affects caller's copy
    properties = 5                      # "destroy the pointer" - but does NOT affect caller's copy!

w = ''
p = []
set_up(w, p)
print w, p                              # '', ['noun']