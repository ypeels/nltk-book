# Natural Language Toolkit: code_strings_to_ints

'''
Example 4.11 from Section 4.7: Space-Time Tradeoffs

Figure 4.11: Preprocess tagged corpus data, converting all words and tags to integers

"A more subtle example of a space-time tradeoff"
- uh..... storage space is reduced, but to work with words directly, you'd have to spend time back-converting?
'''

def preprocess(tagged_corpus):
    '''Preprocess tagged corpus data, converting all words and tags to integers'''
    words = set()                                       # can't use single-line initialization, since that would be assignment by reference! ("no copy constructor" or "shallow copy")
    tags = set()
    for sent in tagged_corpus:                          # "create a vocabulary for the corpus"
        for word, tag in sent:                          # assumes 'sent' is of the form [(word, tag)...]
            words.add(word)                             # set.add(word) does nothing if `word in set`
            tags.add(tag)
    wm = dict((w,i) for (i,w) in enumerate(words))      # "invert this [vocabulary] so that we can look up any word to find its identifier."
    tm = dict((t,i) for (i,t) in enumerate(tags))
    return [[(wm[w], tm[t]) for (w,t) in sent] for sent in tagged_corpus]   # hey, the dictionaries were just a throwaway means to create this list

