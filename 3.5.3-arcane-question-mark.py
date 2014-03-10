'''
3.5.3   Finding Word Stems
or Moar Ways to use "?" in Regexps

"?" - Standard usage: postfix operator to specify "0 or 1 occurrence"
"?:" - To disable substring capture inside parentheses (use at beginning, like "(?:ing)". "one of many arcane subtleties of regular expressions"
"*?" - Non-greedy star operator

I actually haven't seen the last two on rubular.com OR in either Python tutorial!
'''

import re

print __doc__

# example usage
def run_findall(regexp, word):
    print word
    print regexp
    print re.findall(regexp, word, re.VERBOSE)              # ahh, comments WITHIN regexps...
    print ''
    
run_findall(r'''
            ^.*                              
            
            # parentheses take over findall() as capture operator!
            (ing|ly|ed|ious|ies|ive|es|s|ment)$''' , 
            'processing'
            )               # ['ing']

run_findall(r'''
            ^.*
            
            # leading "?:" disables capture function inside parentheses!!
            (?:ing|ly|ed|ious|ies|ive|es|s|ment)$''',
            'processing'
            )               # ['processing']
            
run_findall(r'''
            ^
            
            # Star operator "*" is by default "greedy"!
            (.*)            
            
            (ing|ly|ed|ious|ies|ive|es|s|ment)$''',
            'processes'
            )               # ['processe', 's']
       

regexp3 = r'''
            ^
            
            # Non-greedy star operator "?*" !! come on...
            (.*?)
            
            # And for good measure, the standard "?" operator usage of "0 or 1"
            (ing|ly|ed|ious|ies|ive|es|s|ment)?$
            '''       
run_findall(regexp3, 'processes')
run_findall(regexp3, 'language')

