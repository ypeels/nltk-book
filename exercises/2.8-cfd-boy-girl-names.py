import nltk

names = nltk.corpus.names
#boy_names = names.words('male.txt')
#girl_names = names.words('female.txt')

# uh, just a TINY change to code above Figure 2.10...
cfd = nltk.ConditionalFreqDist(
            (fileid, name[0])
            for fileid in names.fileids()
            for name in names.words(fileid)
            )
            
# but how do you normalize for total # counts??
# i can't figure out the ConditionalProbDist constructor
# NLTK documentation SUCKS too