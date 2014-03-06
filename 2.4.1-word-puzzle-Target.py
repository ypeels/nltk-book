import nltk

# Problem specification from Figure 2.9
# my instinct is to solve it "backwards" - iterate through the wordbank and find all words satisfying the puzzle's constraint
# the alternative is annoying logic, sampling from the letters...
# well apparently this is how the book does it too! so i guess it's forward-thinking, haha
# book's solution uses ntlk.probability.FreqDist instead. meh.  (ohhhh fdist1 < fdist2 if samples in fdist1 occur fewer times than in fdist2 - see Table 1.2)
# weren't they trying to teach functions? i guess that was SO section 2.3


def can_spell(bank, word):
    '''Returns True iff "word" can be spelled by the letters in "bank"'''
    for letter in word:
        if bank.count(letter) < word.count(letter):
            return False
    return True


def is_a_solution(word, required, optional):
    '''Returns True iff 'word' can be spelled by letters in "required" + "optional", and is 4 letters or longer'''    
    
    # 1: word contains all required letters
    # 2: letter bank contains all letters in word
    # 3: word is 3 letters or longer
    return \
        can_spell(word, required) and \
        can_spell(optional+required, word) and \
        len(word) >= 4                          
    
    
# COULD move these constants into is_a_solution(), but then there'd be redundant assignments??
# too lazy to write a class
required = ['r']
optional = ['e', 'v', 'o', 'l', 'v', 'i', 'n', 'g']

# v3: list comprehension, like book's solution
wordbank = nltk.corpus.words.words()
solutions = [word for word in wordbank if is_a_solution(word, required, optional)]
        
print len(solutions), "solutions found:", solutions
full_solutions = [s for s in solutions if len(s) == len(required + optional)]
if len(full_solutions) > 0:
    print "Full solutions using all letters:", full_solutions
else:
    print "No solutions use all letters! You fail it!"

