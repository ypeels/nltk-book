# I'm just not happy with the way the book uses a ConditionalFreqDist when they only need a 2-d data structure
# - I mean, congratulations, you have a distribution of Kronecker deltas. Something's gone physically wrong...

# how about a dictionary of lists?

import nltk

all_entries = nltk.corpus.cmudict.entries()
p3_entries = [(word, pron) for (word, pron) in all_entries if pron[0] == 'P' and len(pron) == 3]    # 3-syllable P-words
p3 = [(pron[0] + '-' + pron[2], word) for (word, pron) in p3_entries]                               # book's data format

        
# iterative version
iterative_dict = { }    
for (pron_str, word) in p3:
    if not iterative_dict.has_key(pron_str):
        iterative_dict[pron_str] = [word]
    else:
        iterative_dict[pron_str].append(word)
        
# # listcomp version?? ugh, could not figure this out easily
# p3_list = [ (pron, [ w for  ]) for (pron, word) in p3]
# 
# p3 = { pron[0] + '-' + pron[2] : [word for (word, pron) in p3_entries]          # this feels wrong... and it 
#         for (word, pron) in p3_entries }

def output_dict(d):        
    for pron_str in sorted(d.keys()):
        word_list = d[pron_str]
        if len(word_list) > 10:
            print pron_str, " ".join(sorted(word_list))
     
     
output_dict(iterative_dict)      
    
# there's gotta be a more pythonic way to write this...
# oh, apparently there are dict comprehensions starting in Python 2.7!? http://stackoverflow.com/questions/1747817/
# didn't help (still iterative): http://stackoverflow.com/questions/5378231/python-list-to-dictionary-multiple-values-per-key
# i just can't figure out how to write a "comprehension" statement that merges multiple values into a list, for a given key
    # meh, i thnk the iterative version is PRETTY clear...
