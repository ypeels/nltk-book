import nltk

wordbank = nltk.corpus.words.words()

# my instinct is to solve it "backwards" - iterate through the wordbank and find all words satisfying the puzzle's constraint
# the alternative is annoying logic, sampling from the letters...
