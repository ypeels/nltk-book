import nltk.corpus

english_stopwords = nltk.corpus.stopwords.words('english')      # ahhhh a regular list; no stupid API stupidity

def words_minus_stopwords(words):
    return [w for w in words if w.lower() not in english_stopwords 
        and w.isalpha()]                                        # also rule out stupid puncutation
    
def top_50_non_stopwords(words):
    non_stopwords = words_minus_stopwords(words)
    fdist = nltk.FreqDist(non_stopwords)
    return fdist.keys()[:50]                                    # MAYBE i'll want to reuse this??
    


if __name__ == "__main__":
    from utils import all_texts
    for text in all_texts:
        print text.name, top_50_non_stopwords(text)