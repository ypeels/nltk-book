'''
3.5.4   Searching Tokenized Text

nltk.text.Text.findall(regexp) allows direct application of regexps to its token LIST
with the following custom NLTK modifications:
- without compiliation?
- without verbose regexp support :(  maybe with "(?x)" prefix? see 3.7
- regexp for each TOKEN inside angle brackets
- ALL (?) whitespace is ignored
'''

print __doc__



import nltk
#moby = nltk.Text(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
#result = moby.findall(
#        r"<a>"             # here's my workaround to "emulate" re.VERBOSE
#        r"(< . * >)      " # whitespace OUTSIDE angle brackets is ignored
#        r"<ma  n>"         # whitespace INSIDE the angle brackets is ignored too (since it's iterating over a huge token list)
#        )
#        # monied; nervous; ...   "a monied man", "a nervous man", etc.
#        
#chat = nltk.Text(nltk.corpus.nps_chat.words())
#chat.findall(
#        r"<l.*>"            # all tokens starting with "l"
#        r"{3,}"             # 3 or more occurrences in a row
#        )

        
print '''
Your Turn (1).

nltk.app.nemo() opens a GUI for experimenting with regexps.

But first, try out nltk.re_show(regexp, string) - shows matches for 'regexp' in 'string'
'''

sentence = "A man, a plan, a canal, panama."
nltk.re_show(
                r"[Aa] "    
                r"([\w]+)"                      # substring captures are IGNORED by re_show()
                r","
                ,
                sentence
                )                               # {A man,} {a plan,} {a canal,} panama.
    
print ""
print "To try 'Finding (and Replacing) Nemo, run `nltk.app.nemo()`"
#nltk.app.nemo()


print '''
Your Turn (2)

Looking for "as x as y" - analogous to the "x and other ys" example
'''

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
hobbies_learned.findall(r"<as> <\w*> <as> <\w*>")