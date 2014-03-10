'''Code for the "Your Turn" Notes in Section 3.4
    Various queries for nltk.corpus.words    
'''

print __doc__
    
# i COULD just eat the extra imports, but i wanted to see if i could figure out how to do this
# see dive into python "regression.py"... uh, why doesn't this work??
# oh maybe i'm supposed to declare the module global? meh
# 
# def smart_import_single_module(module):
#     print module
#     import importlib
#     if module not in globals():
#         # NEITHER this nor __import__(module) works!?
#         __import__(module)
#         #map(__import__, [module]) 
#         #importlib.import_module(module)
#         print "here's how things look INSIDE the function:", globals(), locals(), "\n\n"
#         
#     if module == 'nltk':
#         print dir(nltk)
# def smart_import(input):
#     if type(input) == list:
#         for module in input:
#             smart_import_single_module(module)
#     elif type(input) == str:
#         if module not in globals():
#             smart_import_single_module(module)
#     else:
#         print 'Unsupported type in smart_import:', type(input)

num_to_display = 100
wordlist = []
def create_wordlist():
    global wordlist
    if len(wordlist) == 0:
        import nltk
        wordlist = [w for w in nltk.corpus.words.words('en')]


        
        
print '3.4.1 Using Basic Meta-Characters - Your Turn'
print 'trivial, but included to satisfy curiosity regarding the answer'
print "Regex search for /..j..t../"
#smart_import(['re', 'nltk'])
import re, nltk, timeit
create_wordlist()
regex1_str = '..j..t..'
regex1 = re.compile(regex1_str)
print [w for w in wordlist if regex1.search(w)][:num_to_display]                                            # re.search() returns True iff ANY match for the regexp was found
    # the result is, of course, much longer than /^..j..t..$/, whose result it contains as a subset

# performance measurement!
#regex1_env = 'from __main__ import re, wordlist, regex1, regex1_str'
#print "Compiled:", timeit.timeit('L = [w for w in wordlist if regex1.search(w)]', regex1_env, number=10)
#print "Uncompiled:", timeit.timeit('L = [w for w in wordlist if re.search(regex1_str, w)]', regex1_env, number=10)
#    # Compiled: 1.15
#    # Uncompiled: 3.20


print '''
3.4.2 Ranges and Closures - Your Turn
"finger-twisters' - telephone numbers that only use PART of the number pad
'''
import re, nltk
create_wordlist()
regex2_strings = [ r'^[g-o]+$', r'^[a-fj-o]+$' ]
def run_search(regex_str, wordbank):
    regex = re.compile(regex_str)
    print regex_str
    result = [w for w in wordbank if regex.search(w)]
    print result[:num_to_display]
    print ''
    return result
    
for r in regex2_strings:
    run_search(r, wordlist)
    
print "Trivium: the '+' and '*' regex symbols are known as (Kleene) closures. No relation to lambda closures..."


print '''
And finally the tiny 'instructive' case they mention in passing
'''
import re, nltk
wsj = sorted(set(nltk.corpus.treebank.words()))
print "Note that parentheses are used in the following example to specify operator scope, NOT to capture substrings"
parenthesized = run_search('(ed|ing)$', wsj)
unparenthesized = run_search('ed|ing$', wsj)                        # apparently '|' has low priority (or $ has high priority?)
equivalent_to_unparenthesized = run_search('(ed)|(ing$)', wsj)      # will search for all strings ending in 'ing' or CONTAINING 'ed' (not necessarily at the end!)
print 'The last 2 are equivalent?', unparenthesized == equivalent_to_unparenthesized
print "parenthesized - unparenthesized\n", [w for w in unparenthesized if w not in parenthesized]

print "See Table 3.3 for a summary of the regex 'meta-characters' explored in section 3.4"