# -*- coding: utf-8 -*-
'''
Exercise 3.26
Create vowel bigram table from a document in, say, Hungarian.

Maybe this will be good Unicode practice too?
'''


import nltk, re, unicodedata

text = nltk.corpus.udhr.words('Hungarian_Magyar-UTF8')



n = 50



# 2 vowels in a row
vowel_pattern = r'[^bcdfghjklmnpqrstvwxyz]{2,2}'            # forget y...
vowel_re = re.compile(vowel_pattern, flags=re.IGNORECASE)


# basic algorithm from 3.5.2
bigrams = [bigram
            for word in text if word.isalpha()
            for bigram in vowel_re.findall(word)
            ]



# oh come ON, this thing requires ascii??
# http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
# forget this, i'm not importing a third-party library just for this stupid exercise
# and i'm NOT creating a unicode-compatible CFD, if NLTK didn't even bother

print "Investigating non-ascii vowels:"
S = set([ c
            for b in bigrams
            for c in b if not 0 <= ord(c) <= 127
            ])
for c in S:
    print c, repr(c)
# á u'\xe1'
# é u'\xe9'
# ó u'\xf3'
# ő u'\u0151'
# ű u'\u0171'

vowel_to_ascii = [
    (u'á', 'a'),
    (u'é', 'e'),
    (u'\xf3', 'o'),
    (u'\u0151', 'o'),
    (u'\u0171', 'u')
    ]


# this listcomp doesn't work, and i don't feel like figuring out why
#ascii_bigrams = [ b.replace(unicode_vowel, ascii_vowel)
#                  for unicode_vowel, ascii_vowel in vowel_to_ascii
#                  for b in bigrams ]
# and watch out for modifying lists that you're looping over!!! less confusing to use C-style...
ascii_bigrams = bigrams  # for correct size AND initial values
for i in range(len(ascii_bigrams)):  #range(len(ascii_bigrams)):
    ascii_bigram = ascii_bigrams[i]
    for unicode_vowel, ascii_vowel in vowel_to_ascii:
        ascii_bigram = ascii_bigram.replace(unicode_vowel, ascii_vowel)
    ascii_bigrams[i] = ascii_bigram

        

for i in range(len(bigrams)):
    if bigrams[i] != ascii_bigrams[i]:
        print bigrams[i], ascii_bigrams[i]
    

print nltk.ConditionalFreqDist(ascii_bigrams).items()
nltk.ConditionalFreqDist(ascii_bigrams).tabulate()

# results
#      a    e    i    u
# a    0    1   12    1
# e    3    3    9    0
# i    8    4    3    0
# o    1    0    1    0
# u    0    1    0    0