import nltk

# doing battle with the idiosyncratic nltk api...
# "Read in the texts of the State of the Union addresses, using the state_union corpus reader."
su = nltk.corpus.state_union
addresses = { file[:4]: su.words(file) for file in su.fileids()} # dictcomp!

# "Count occurrences of men, women, and people in each document. 
# What has happened to the usage of these words over time?"

# ugh, my attempt at a listcomp got SLOPPY
#word_counts = [(year, addr.count('men'), addr.count('women'), addr.count('people')) 
#                #for word in ['men', 'women', 'people'] # couldn't figure out how to use this without iteration
#                for year in addresses.keys()
#                for addr


# ugly, unpythonic, iterative implementation
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
    
    
    
    
