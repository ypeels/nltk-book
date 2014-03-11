'''
Exercise 3.23

Stumped me for a bit
'''
print __doc__

import nltk, re
pattern = r"(\w+)(n't)|(\w+)?"
sentence = "I don't think so, that wouldn't be right"
nltk.re_show(pattern, sentence)
print re.findall(pattern, sentence)


print '''
I think the problem with the original regex was that the '\w+' was greedy?
Didn't really know how to fix it like with the "*?" operator
My fix SEEMS to work...
The output format is probably wrong...
'''
