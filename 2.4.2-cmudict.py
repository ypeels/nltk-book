# I'm just not happy with the way the book uses a ConditionalFreqDist when they only need a 2-d data structure
# - I mean, congratulations, you have a distribution of Kronecker deltas. Something's gone physically wrong...

# how about a dictionary of lists?

import nltk

cmudict_entries = nltk.corpus.cmudict.entries()
p3 = [(pron[0] + '-' + pron[2], word)
        for (word, pron) in cmudict_entries
        if pron[0] == 'P' and len(pron) == 3
        ]
    
target_dict = {}    
for (pron_str, word) in p3:
    if not target_dict.has_key(pron_str):
        target_dict[pron_str] = [word]
    else:
        target_dict[pron_str].append(word)
        
for pron_str in sorted(target_dict.keys()):
    word_list = target_dict[pron_str]
    if len(word_list) > 10:
        print pron_str, " ".join(sorted(word_list))
    
# there's gotta be a more pythonic way to write this...