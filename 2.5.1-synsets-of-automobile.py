from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Lemma, Synset

print '''
So The book claims that 'automobile' has one synset. 
I almost submitted a bug report on GitHub, but it looks like this might be true...from a certain point of view...

Submit it anyway!?
https://github.com/nltk/nltk_book/issues/48

"Unlike the words automobile and motorcar, which are unambiguous and have one synset"
BUT! wordnet.synsets('automobile') returns:
'''
print wordnet.synsets('automobile'), "<-- see, there's two items here"  # [Synset('car.n.01'), Synset('automobile.v.01')]


print '''
However, only ONE of these two Synset objects STARTS with 'automobile'". Maybe that's what text means?

Nevertheless, the immediately following code example contradicts that hypothesis, stating
"the word car is ambiguous, having five synsets"

and wordnet.synsets('car') returns, as shown in the code example:
'''
print wordnet.synsets('car'), "<-- there's 5 items here"  # [Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'), Synset('cable_car.n.01')]

print '''
Most likely, the authors didn't run `wordnet.synsets('automobile')` and just ASSUMED there was only 1 def?
'''


print 'Finally, some code for the "Your Turn" Note:'
for lemma in wordnet.lemmas('dish'):
	print lemma.synset, lemma.synset.definition
