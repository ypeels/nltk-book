'''
Exercise 4.16

Gematria assigns numerical values to words and maps words with the same value to discover hidden meanings...
http://en.wikipedia.org/wiki/Gematria
http://essenes.net/gemcal.htm  - this link was dead

'''

 	

letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
                'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
                'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
                
def value(letter):
    '''Returns a numerical value for any letter from a-z, or 0 otherwise.
    '''
    assert(type(letter) == str and len(letter) == 1)
    letter = letter.lower()
    if letter in letter_vals:                       # value table defined above
        return letter_vals[letter]
    else:
        return 0                                    # for digits, punctuation, etc.
    
def gematria(word):
    assert(type(word) == str)
    return sum(value(letter) for letter in word)
    

    
if __name__ == "__main__":
    from nltk.corpus import state_union
    print "Occurrences of the sign of the Devil in SotU addresses past:"
    for file in state_union.fileids():
        print file[:4], sum(1 for word in state_union.words(file) if gematria(word) == 666)
    