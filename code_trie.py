'''
Example 4.9 from Section 4.7.1: Recursion

Figure 4.9: Building a Letter Trie
"A letter trie is a data structure that can be used for indexing a lexicon, one letter at a time. 
(The name is based on the word retrieval)."

I guess it's a "pun," cuz it's a tree structure?
'''

# Natural Language Toolkit: code_trie

def insert(trie, key, value):
    '''A recursive function that builds a nested dictionary structure.
    
    each level of nesting contains all words with a given prefix, 
    and a sub-trie containing all possible continuations.'''
    
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:                           # need to initialize empty case
            trie[first] = {}
        insert(trie[first], rest, value)                # RECURSE! builds letter-wise "hash tree" of words
    else:
        trie['value'] = value

if __name__ == "__main__":
    print __doc__

    import pprint
    trie = {}
    insert(trie, 'chat', 'cat')
    insert(trie, 'chien', 'dog')
    insert(trie, 'chair', 'flesh')
    insert(trie, 'chic', 'stylish')
    trie = dict(trie)               # for nicer printing
    trie['c']['h']['a']['t']['value']
    # cat
    
    pprint.pprint(trie)
    # {'c': {'h': {'a': {'t': {'value': 'cat'}},
    #                   {'i': {'r': {'value': 'flesh'}}},
    #              'i': {'e': {'n': {'value': 'dog'}}}
    #                   {'c': {'value': 'stylish'}}}}}    