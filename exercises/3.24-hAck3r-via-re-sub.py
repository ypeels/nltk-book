'''
Exercise 3.24

Using re.sub, which WAS NOT COVERED in the text...
'''

patterns = [
        (r'[aA4][tT][eE]', r'8'),       # uh, added the 4 so that this thing is in PRINCIPLE order-invariant
        (r'[aA]', r'4'),
        (r'[eE]', r'3'),
        (r'[iI]', r'1'),
        (r'[oO]', r'0'),
        (r'[lL]', r'|'),
        (r'([\b\s])[sS]', r'\1$'),      # s at word beginning. back-reference is how you preserve matched text (see also nltk.app.nemo)
        
        # any internal 's' with "5".
        # r'\15' will NOT work for the replacement regex, since Python thinks that's backref #15!
        # (?P  indicates a Python regex extension
        # (?P<name>  allows a named group, accessed as shown below
        # sheesh, had to dig pretty deep to figure this out: http://www.regular-expressions.info/replacebackref.html
        (r'(?P<pre>\w+)[sS]', r'\g<pre>5'),
        
        
        (r'\.', r' 5w33t!')             # I think it'd be better with an extra space
        ]


def hacker(str):
    import re
    for pattern, replacement in patterns:
        str = re.sub(pattern, replacement, str)
    return str

if __name__ == "__main__":
    example = "If it is sustenance you crave, then it is sustenance you shall receive."
    print example
    print hacker(example)
    print hacker(raw_input(hacker("Me hungry! Give me m04r text to h4ck3rize: ")))
        
