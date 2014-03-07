import nltk

english_stopwords = nltk.corpus.stopwords.words('english')
def is_ok(word):
    return word.lower() not in english_stopwords and word.isalpha()

def top_50_bigrams(text):
    all_filtered_bigrams = [ (w1, w2) for (w1, w2) in nltk.util.bigrams(text)       # maybe change to lower(w1), lower(w2)?
                            # for w in b  # ugh could not get this to work, stupid pythonism - it would still pick up punctuation
                            if is_ok(w1) and is_ok(w2) 
                            ]
    fdist = nltk.FreqDist(all_filtered_bigrams)
    return fdist.keys()[:50]
                



if __name__ == "__main__":
    print "here are the english stopwords:", english_stopwords
    from utils import all_texts
    for text in all_texts:
        print text.name, top_50_bigrams(text)
    
    # now THAT's how you write test code... instead of waiting stupidly for texts to import, only to have to debug syntax errors
    #print top_50_bigrams("the cat jumped over the moon".split())