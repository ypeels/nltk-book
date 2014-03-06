import nltk

wordbank = nltk.corpus.words.words()

# my instinct is to solve it "backwards" - iterate through the wordbank and find all words satisfying the puzzle's constraint
# the alternative is annoying logic, sampling from the letters...

# COULD move these constants into is_a_solution(), but then there'd be redundant assignments??


# v1: Pythonic iteration
def is_a_solution(word, required, optional):
    '''Returns True iff 'word' can be spelled by letters in "required" + "optional"'''    
    
    # requirement 1: word must contain ALL letters in "required"; abort if not
    for letter in set(required):
        if word.count(letter) < required.count(letter):     # word doesn't contain enough required letters
            return False

    # requirement 2: letter bank must contain ALL letters in "word; abort if not.
    # I smell refactoring...
    letter_bank = optional + required
    for letter in set(word):
        if letter_bank.count(letter) < word.count(letter):  # bank doesn't contain enough letters to spell word!
            return False

    assert(len(word) <= len(letter_bank))
    
    # requirement 3: word is 4 letters or longer
    return len(word) >= 4
    
    
required_letters = ['r']
optional_letters = ['e', 'v', 'o', 'l', 'v', 'i', 'n', 'g']
solutions = []
for word in wordbank:
    if is_a_solution(word, required_letters, optional_letters):
        solutions.append(word)
        
print len(solutions), "solutions found:", solutions
