import nltk.corpus



# this exercise is trivial, but i wanted practice writing pythonic code
# i find i write things out on multiple lines, then copy/paste into a glorious-sized listcomp
# - probably  not the clearest way to do things
# - plus, it's harder to modify such expressions, although they MIGHT read a little more easily...

# all_words = nltk.corpus.brown.words() # "too many values to unpack"
all_words = nltk.corpus.brown.words(categories='news')
fdist = nltk.FreqDist(nltk.corpus.brown.words())
filtered_words = sorted([word for (word, count) in fdist.items() if count >= 3])

# here's a taste
print filtered_words[:100]

# one-liner. works now, but i had to figure out i forgot the items()
#filtered_words = sorted([word for (word, count) in nltk.FreqDist(nltk.corpus.brown.words()).items() if count >= 3]) # "too many values to unpack"