from nltk.book import *
from utils import all_texts

print '''
1.3.2: Fine-grained Selection of Words

So a basic frequency analysis did not really address "the question of what makes a text distinct."

The next idea is to look at long words; "perhaps these will be more characteristic and informative."

Actually, the only reason I have a script for this section is that
you should be able to use a SET comprehension directly...
No need to use a list comprehension in "translating" set builder to Python...
Did they just not want to introduce the concept of set comprehension or sets?
But they already used the set() function!! 
Maybe the book predates set comprehensions?
'''

def print_very_long_words(text):
    print "Very long words in", text
    print sorted({ w for w in set(text1) if len(w) > 15 })

# should really normalize fdist threshold by total # words
def print_long_frequent_words(text):
    fdist = FreqDist(text)
    print "Reasonably long AND reasonably frequent words in", text
    print sorted([w for w in set(text) if len(w) > 7 and fdist[w] > 7])
    

if __name__ is '__main__':
    for text in all_texts:
        print_very_long_words(text)
        
    for text in all_texts:
        print_long_frequent_words(text)  
