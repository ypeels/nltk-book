'''
Section 3.5: Useful Applications of Regular Expressions

Right away, there's a function I haven't tried: re.findall()
I guess the general-purpose tutorials I looked at didn't go TOO far into regexps...
'''

import re, nltk

print '''
3.5.1   Extracting Word Pieces
'''
regexp1 = re.compile(r'[aeiou]')
word1 = 'supercalifragilisticexpialidocious'
print regexp1.pattern, 'findall(', repr(word1), ')'
print regexp1.findall(word1)
print ''


print '''
Your Turn: Convert '2009-12-31' into a list of integers using re.findall()
'''
def date_to_ints(date):
    assert(type(date) == str)
    return [int(n) for n in re.findall(r'[0-9]+', date)]
print date_to_ints('2009-12-31')




            
