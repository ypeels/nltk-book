print '''

In order of appearance.
To display docstring of 'obj', just perform
>>> help(obj)

1.1  Computing with Language: Text and Words
===========================================

>>> from nltk.book import *

nltk.text.Text instance methods  # help(Text) for more info
-----------------
concordance(word): prints all occurrences of 'word', with surrounding context
similar(word): prints words that appear in a similar context as 'word'?
common_contexts([word_list]): contexts shared by two or more words...[what's with the underscores??]
dispersion_plot([word_list]): plots word occurrences vs word offset.  Cool!
generate(): generates random text in the style of the object instance.  Cool!!  Note punctuation separation


1.3  Computing with Language: Simple Statistics
===============================================

nltk.probability.FreqDist  # help(FreqDist) for more info
-------------------------
- quacks like a dictionary of { "word": count } - but that's not all!
- FreqDist(Text): constructor (more generally, argument can be any iterable!? e.g. [len(w) for w in text])
- keys(): returns samples sorted in **decreasing order of frequency**
- items(): returns [(key1, count1), (key2, count2), ...], still in decreasing order of frequency
- max(): returns the KEY with the highest count
- freq(key): returns (count of 'key') / (total count)
- plot(N, cumulative=True) for a (cumulative) frequency plot of N most common words
- hapaxes(): returns a list of words that occur once only, the so-called hapaxes
- for more, see Table 1.2. e.g., N() = total count

nltk.util.bigrams([word0, word1, ..., wordN]): returns [(word0, word1), (word1, word2), ..., (wordN-1, wordN)]

nltk.text.Text.collocations(): returns all UNUSUALLY frequent two-word phrases ("ignoring stopwords")
'''