import nltk

# doing battle with the idiosyncratic nltk api...
# "Read in the texts of the State of the Union addresses, using the state_union corpus reader."
su = nltk.corpus.state_union
address_dict = { file[:4]: su.words(file) for file in su.fileids()} # dictcomp!
address_list = [(int(file[:4]), su.words(file)) for file in su.fileids()]

# "Count occurrences of men, women, and people in each document. 
# What has happened to the usage of these words over time?"

# ugh, my attempt at a listcomp got SLOPPY
#word_counts = [(year, addr.count('men'), addr.count('women'), addr.count('people')) 
#                #for word in ['men', 'women', 'people'] # couldn't figure out how to use this without iteration
#                for year in addresses.keys()
#                for addr

# a = addresses['1945']
# [('1945',) + tuple([ a.count(word) for word in ['men', 'women', 'people']   ])]


# ahh, this is much more transparent once you figure out how to express it with listcomps
# seems like the point of these listcomps is to FOCUS your attention on the data
search_words = ['men', 'women', 'people']
word_count = [ 
    (year,) + 
    tuple([addr.count(word) for word in search_words]) +        # WOW that's transparent, ESPECIALLY compared with the iterative/imperative version. beat that, ruby!
    tuple([addr.count(word) / float(len(addr)) for word in search_words])
    for year, addr in address_list
    ]
from pprint import pprint
pprint(word_count)     

# seems like another ratio you could compute would be men/women or men/people
# it would also be more informative to PLOT these data, but i'm too tired
# my main objective here is to learn python well enough for the coursera course
# but i'll learn nltk more thoroughly if/when the time comes...



def iterative_version():
    '''ugly, unpythonic, iterative first solution to Exercise 2.4'''
    
    addresses = address_dict  # I used my dictcomp on my first try
    
    word_counts = []
    word_ratios = []
    search_words = ['men', 'women', 'people']
    for year in sorted(addresses.keys()):
        addr = addresses[year]
        count = [year]
        ratio = []
        for word in search_words:
            count.append(addr.count(word))
            ratio.append(addr.count(word) / float(len(addr)))
        word_counts.append(tuple(count))
        word_ratios.append(tuple(ratio))
        
    print "Year", " ".join(search_words), "ratios"
    for count, ratio in zip(word_counts, word_ratios):
        print count, ratio
        
    
    
#iterative_version()    
