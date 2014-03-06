import nltk

wordbank = nltk.corpus.words.words()

# my instinct is to solve it "backwards" - iterate through the wordbank and find all words satisfying the puzzle's constraint
# the alternative is annoying logic, sampling from the letters...

# COULD move these constants into is_a_solution(), but then there'd be redundant assignments??


# v2: Pythonic iteration, refactored about as clean as I can think of
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
    
    
required_letters = ['r']
optional_letters = ['e', 'v', 'o', 'l', 'v', 'i', 'n', 'g']
solutions = []
for word in wordbank:
    if is_a_solution(word, required_letters, optional_letters):
        solutions.append(word)
        
print len(solutions), "solutions found:", solutions
