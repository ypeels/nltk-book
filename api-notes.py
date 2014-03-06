print '''

In order of appearance.
To display docstring of 'obj', just perform
>>> help(obj)
'''

print '''
1. Language Processing and Python
#################################

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


1.5  Automatic Natural Language Understanding
=============================================
nltk.misc.babelfish.babelize_shell(): interactive shell that attempts machine translation (12 iterations)
- I'm getting "BabelfishChangedError: Can't recognize translated string", even for book's examples...meh.

nltk.chat.chatbots(): "an example of a primitive dialogue system"
'''



print '''
2. Accessing Text Corpora and Lexical Resources
###############################################

2.1   Accessing Text Corpora
============================

nltk.corpus.gutenberg
---------------------
- subclass of PlaintextCorpusReader
- fileids(): lists names of all .txt files in gutenberg/
- words(filename): return file as "list" of words and punctuation symbols 
    - (pass to Text() constructor)
    - actual class is nltk.corpus.reader.util.StreamBackedCorpusView, hence truncated output
- raw(filename): returns file as raw string. includes whitespace!
- sents(filename): returns file as "list" of sentences, each sentence as a RAW LIST OF WORDS + punctuation

see also PlaintextCorpusReader(self, path, fileids): where fileids can be wildcards, or regexes?


Other corpora (query with fileids()) subpackages of nltk.corpus
----------------------------------
webtext: forum posts, conversations, movie script, want ads, wine reviews, IM chats
brown: the first million-word electronic corpus of English, est. 1961 -  http://icame.uib.no/brown/bcm-los.html
- subclass of CategorizedTaggedCorpusReader
- brown.categories(self): returns categories as list of strings
- brown.words(self, fileids=None, categories=None): returns one big "list" of words in all specified files, categories
- brown.sents(self, fileids=None, categories=None): returns one big "list" of sentences (each sentence a RAW list of words)
reuters: also a subclass of CategorizedTaggedCorpusReader
inaugural: a subclass of PlaintextCorpusReader, like gutenberg
cess_esp: Spanish-language?
floresta: um, Italian?
udhr: Universal Declaration of Human Rights, in over 300 languages!
Table 2.3: for more info about the corpus API.

Other
-----
nltk.probability.ConditionalFreqDist( [(condition, sample) tuples] ): binned frequencies. or is it a GENERATOR argument??
- tabulate(conditions=[subset of conditions], samples=[subset of samples]): see figure above "Reuters Corpus" heading
- plot()


2.2   Conditional Frequency Distributions
=========================================

nltk.probability.ConditionalFreqDist (cont.)
- conditions(): returns list of category bins
- [bin]: returns the (unconditional!) FreqDist for bin
- Table 2.4 for more info


2.4   Lexical Resources
=======================

nltk.corpus.stopwords: high-frequency words like the, to and also
- subclass of WordListCorpusReader
- words(fileids): filenames 'english', 'french', etc.

'''