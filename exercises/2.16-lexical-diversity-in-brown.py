import nltk.corpus

print "Genre", "Lexical diversity"
for cat in nltk.corpus.brown.categories():
    words_in_cat = nltk.corpus.brown.words(categories=cat)
    print cat, "{:3g}".format( float(len(words_in_cat)) / len(set(words_in_cat)) )

    
print '''
CAUTION: confusingly, a higher lexical diversity value means a "LESS DIVERSE" (less recycled) vocabulary
From Table 1.1, diversity := tokens / types
- diversity = 1 means text contains ALL WORDS (tokens) are unique
- diversity = N means text contains 1 word, N times

What is it about academics and not wanting to be understood?
Does it make them feel smarter?
'''

# results
# Genre Lexical diversity
# adventure 7.81406
# belles_lettres 9.39667     <----------
# editorial 6.22892
# fiction 7.36272
# government 8.57071
# hobbies 6.89946
# humor 4.3243
# learned 10.7888            <---------
# lore 7.60525
# mystery 8.18805
# news 6.98583
# religion 6.18217
# reviews 4.71876
# romance 8.28467
# science_fiction 4.47572

# analysis
# hahaha, very funny; "learned" has the least diverse vocabulary
# oh, those are SCIENTIFIC/TECHNICAL PAPERS, so this is hardly surprising
# - those have rather specialized, small vocabularies which are recycled
# - technical writers generally have shitty English
# 
# runner up: belles_lettres (wtf is this?? whatever)