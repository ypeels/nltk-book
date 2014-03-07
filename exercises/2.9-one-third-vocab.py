import nltk
from nltk.probability import FreqDist
from utils import all_texts

#for text in all_texts:
#    cfd

# the ConditionalFreqDist API is TOO CROTCHETY... 
# i guess i don't care about plotting or tabulating them together
#cfd = nltk.ConditionalFreqDist(
#        (text.name, word)
#        for text in all_texts
#        for word in text   # eat the stopwords and punctuation...
#        )
#cfd.plot(100, cumulative=True)


fdists = [ (text.name, FreqDist(text)) for text in all_texts ]



print "How many words constitute 1/3 of all words in the following works?"
fraction = 0.5 #2.0 / 3
for (name, fd) in fdists:
    threshold = fd.N() * fraction
    running_word_count = running_unique_word_count = 0    
    #current_word = None  #ehh? why did i want this?
    for (word, count) in fd.items():                                    # in the end, it was easier to fish around the API
        #current_word = word
        running_word_count += count
        running_unique_word_count += 1
        if running_word_count >= threshold:
            break
    print running_unique_word_count, "word types, out of", fd.B(), name
        

# Results    
# 17 word types, out of 19317 Moby Dick by Herman Melville 1851
# 18 word types, out of 6833 Sense and Sensibility by Jane Austen 1811
# 10 word types, out of 2789 The Book of Genesis
# 13 word types, out of 9754 Inaugural Address Corpus
# 32 word types, out of 6066 Chat Corpus
# 12 word types, out of 2166 Monty Python and the Holy Grail
# 23 word types, out of 12408 Wall Street Journal
# 14 word types, out of 1108 Personals Corpus
# 17 word types, out of 6807 The Man Who Was Thursday by G . K . Chesterton 1908


# Analysis
# Chat Corpus has tons of smileys and weirdness, so it's an outlier
# All other works have 10-23 word types constituting 1/3 of all words, i.e., stopwords?
# even for Chat Corpus, the ABSOLUTE NUMBER of "stopwords" is surprisingly similar, and INDEPENDENT of the text's vocabulary
# even if you crank the fraction up to 1/2, it's still on the order of 50 words for MOST works! (WSJ and Chat Corpus ~100)