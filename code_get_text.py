'''Example 4.2 from Section 4.4

The only new thing this example introduces is docstrings.
It's just a random subroutine example used to discuss subroutines in general.
'''

# Natural Language Toolkit: code_get_text

import re
def get_text(file):                                 # introducing: docstrings
    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)
    return text


if __name__ == "__main__":
    print __doc__
    print "get_text(file):", get_text.__doc__
