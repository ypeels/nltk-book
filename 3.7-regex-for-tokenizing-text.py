'''
Section 3.7   Regular Expressions for Tokenizing Text

Here are some example usages of regexps that I hadn't learned before now.
'''

import re

print __doc__

raw = (
''''When I'M a Duchess,' she said to herself,  (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people} {hot-tempered,'...'''
)

results = []
results.append(re.split(r' ', raw))             # 0. misses '\n': "tone\nthough"; although it DOES catch consecutive spaces
results.append(re.split(r'[ \t\n]+', raw))      # 1. misses punctuation: "though)"  
results.append(re.split(r'\s+', raw))           # 2. split on any whitespace char
results.append(re.split(r'\W+', raw))           # 3. leaves leading/trailing blank-chars, due to leading/trailing punct. \W == any NON-word character! (word characters are letter, number, underscore)
results.append(re.findall(r'\w+', raw))         # 4. why didn't you just START with this? you already introduced re.findall()...
results.append(re.findall(r'\w+|\S\w*', raw))   # 5. words, OR words with any leading punctuation (or single punctuation chars). but why bother?

results.append(re.findall(  r'\w+'              # 6. words
                            r"(?:[-']\w+)*"     # with any INTERNAL single "-" or "'" to catch hyphenated, possessives, or contract'ns
                            r"|'"               # OR any leading or trailing "'", which are apparently used for quotations in this sample
                            r"|[-.(]+"          # OR any (selected) punctuation, possibly repeated (not including "'", so "'..." is split. but to what end??
                            r"|\S\w*"           # or any words with leading, unconsidered punctuation?  like 5., WEIRDLY treats trailing punctuation differently
                            ,
                            raw))
                            
results.append(re.findall(  r'\w+'              
                            r"(?:[-']\w+)*"     
                            #r"|'"               
                            r"|[-.(']+"         # 7. this DOES make a minor difference    
                            r"|\S\w*"           
                            ,
                            raw))
                         

for i, r in enumerate(results):
    print i+1
    print r
    print ""

for ia, ib in [(1,2), (6, 7)]:
    print "Results", ia+1, ib+1, "are identical for this text sample?", results[ia] == results[ib]
    if results[ia] != results[ib]:
        print "Here are the differences:", set(results[ia]) ^ set(results[ib])       # inspired by Note

    
print '''
Example usage for nltk.regexp_tokenize():
'''
import nltk
text = 'That U.S.A. poster-print costs $12.40...' * 1000

nltk_prefix = '''(?x)              # set flag to allow verbose regexps'''       # verbose regexp will be set for re using re.VERBOSE
pattern = r'''
            ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
          | \w+(-\w+)*        # words with optional internal hyphens
          | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
          | \.\.\.            # ellipsis
          | [\]\[.,;"'?:-_`]  # these are separate tokens - book also included parentheses, removed here to allow direct comparison with re.findall(), re.split()
          '''
         

re_pattern = pattern.replace('(', '(?:')                                        # undo the "convenience convention" 
regexp = re.compile(re_pattern, flags=re.VERBOSE)
          
          


nltk_vs_re = []

# come ON, they even switched the argument order. such an "academic" library...
def n1(): return nltk.regexp_tokenize(text, nltk_prefix + pattern )
def n2(): return nltk.regexp_tokenize(text, nltk_prefix + pattern, gaps=True)
def r1(): return regexp.findall(text)
def r2(): return regexp.split(text)
def r1slow(): return re.findall(re_pattern, text, flags=re.VERBOSE)
def r2slow(): return re.split(re_pattern, text, flags=re.VERBOSE)
nltk_vs_re.append( (n1(), r1()) )     
assert r1() == r1slow()      
nltk_vs_re.append( (n2(), r2()) )
assert r2() == r2slow()

if len(text) < 100:                         # suppress output for large tests
    for i,(n,r) in enumerate(nltk_vs_re):
        print i
        print n
        print r
        print "Identical?", n == r
        if n != r:
            print "Differences:", set(n) ^ set(r)
        print ""

        # Analysis
        # Once you account for the (stupid and confusing) API differences that:
        # - parentheses are used ONLY for operator scope in regexp_tokenize() (i.e., no substring capture?)
        # - verbose regexps are set using a weird prefix flag in the PATTERN instead of a flag in the function call
        # then regexp_tokenize() and re.findall() return the SAME RESULTS.
        # also, regexp_tokenize(gaps=True) and re.split() return ALMOST the same results - 
    
# text claims that regexp_tokenize() "is more efficient for this task". IS IT??
import timeit
iterations = 10000
print "nltk findall:", timeit.timeit('n1()', 'from __main__ import n1', number=iterations)
print "re findall:", timeit.timeit('r1()', 'from __main__ import r1', number=iterations)
print "re findall uncompiled:", timeit.timeit('r1slow()', 'from __main__ import r1slow', number=iterations)
print ''
print "nltk split:", timeit.timeit('n2()', 'from __main__ import n2', number=iterations)
print "re split:", timeit.timeit('r2()', 'from __main__ import r2', number=iterations)
print "re split uncompiled:", timeit.timeit('r2slow()', 'from __main__ import r2slow', number=iterations)
    
# results for 10000 iterations, original string * 1000
# nltk findall: 39.8061135463
# re findall: 35.4433712171
# re findall uncompiled: 35.4049968066
# 
# nltk split: 41.3144439487
# re split: 34.1490649798
# re split uncompiled: 33.9462257102

# no friggin WAY is regexp_tokenize() faster than a vanilla regexp!!
# strangely, though, re.compile doesn't speed things up?? 



