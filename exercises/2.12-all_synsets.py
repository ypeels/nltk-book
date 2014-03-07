from nltk.corpus import wordnet

# MOAR CROTCHETINESS - all_synsets() returns a GENERATOR, NOT a list!
# i.e. you can't set a variable equal to it and recycle it
print \
    len([s for s in wordnet.all_synsets('n') if not s.hyponyms()]), "of", \
    len([s for s in wordnet.all_synsets('n')]), "nouns in WordNet have no hyponyms"
