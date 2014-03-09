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


Moar corpora
------------
stopwords: high-frequency words like the, to and also
- subclass of WordListCorpusReader
- words(fileids): filenames 'english', 'french', etc.

names: another subclass of WordListCorpusReader; male.txt and female.txt

cmudict: a pronouncing dictionary. `from nltk.corpus import cmudict` - because `import nltk.corpus.cmudict` FAILS. STUPID NON-OBVIOUS NLTK API
- customized class CMUDictCorpusReader
- "list" of: (word, [syllables])
- quacks like a Python dictionary, but cmudict[word] returns ALL CATALOGUED PRONUNCIATIONS [[syllables1], [syllables2]]
- can use as a rhyming dictionary
- 1: primary stress,   2: secondary stress,   0: no stress - can use as a "rhythm dictionary"
- in 2.4.2 "A Pronouncing Dictionary", they use ConditionalFreqDist on this corpus where they really mean to use a simpler 2-d data structure
  - a dictionary of words will do

swadesh: lists of about 200 common words in several languages (all in the same order)
- words(fileids): will APPEND the languages given by fileids, rather uselessly (or at least inconveniently)
- entries(fileids): convenience function for zip( *[swadesh.words(id) for id in fileids] ). try passing to dict constructor!
  
toolbox: 
- class ToolboxCorpusReader, and see http://www.sil.org/computing/toolbox/
- rather irregular data, can't be spreadsheeted...
- "The loose structure of Toolbox files makes it hard for us to do much more with them at this stage."
- see Chapter 11


2.5   WordNet
=============

nltk.corpus.wordnet - are we done going over corpora yet??
- synsets(word): returns raw list of Synset objects (w/ codes) to which 'word' belongs; "thesaurus search for 'word'"
    - this is essential to "translate" from English words into Synset's "codes"
- synset(code): returns an nltk.corpus.reader.wordnet.Synset object, where code is like 'car.n.01'
- lemmas(word): returns raw list of all Lemma objects belonging to all synsets of 'word'
- antonyms(): returns list of all Lemma objects which are antonyms of self

nltk.corpus.reader.wordnet.Synset instance attributes/methods - e.g., Synset('car.n.01')
- note that to instantiate a Synset object, you can't just use Synset('car.n.01'); have to use wordnet.synset('car.n.01')
- see Figure 2.7 for technical terms: "lemma", "gloss", etc.
- ss.lemma_names: raw list of the real words corresponding to each synonym ("lemma")
- ss.definition: a prose definition (raw string)
- ss.examples: raw list of example sentences
- ss.lemmas: raw list of all the Lemma objects for the current synset
- lemma(code): returns/constructs a Lemma object, where code is like 'car.n.01.automobile' (synonyms come in PAIRS!)
- hyponyms(): returns list of Synset objects for all hyponyms ("subclasses", e.g. 'ambulance' is a hyponym of 'motorcar')
- hypernyms(): returns list of Synset objects for all hypernyms ("superclasses")
- hypernym_paths(): returns list of paths (each a list of Synset objects from ROOT hypernym[s??] to current Synset)
- root_hypernyms(): returns list of most general hypernyms of a Synset (each hypernym is itself a Synset object)
- <background information>: an item's meronyms are its components; the item is its meronyms' holonym.
- part_meronyms(): returns list of Synset objects which are "component parts" of self (for tree: trunk, limb, ...)
- substance_meronyms(): returns list of Synset objects which are "substance parts" of self (for tree: heartwood, sapwood)
- member_holonyms(): returns list of Synset objects which are formed by a COLLECTION of self (for tree: forest)
    - similarly part_holonyms(), substance_holonyms(), and member_meronyms()
    - hilarious example from text: mint.n.04 (mint leaf) has part_holonym mint'02 (mint plan) and substance_holonym mint.n.05 (mint candy)
- entailments(): returns list of Synset objects which are implied by the (verb) self    
- lowest_common_hypernyms(synset): returns list of lowest common hypernyms (as Synsets) - "If two synsets share a very specific hypernym (one that is low down in the hypernym hierarchy) they must be closely related."
- min_depth(): returns minimum "depth" from one of self's root hypernyms; use with result of lowest_common_hypernyms() to quantify degree of specificity
- path_similarity(synset): returns score on [0, 1] "based on the shortest path that connects the concepts in the hypernym hierarchy"
- basically, crazy class hierarchies/taxonomies for LOTS of words. who DID all this data entry???

nltk.corpus.reader.wordnet.Lemma instance attributes/methods - e.g., Lemma('car.n.01.automobile')
- synset: raw string code of corresponding synset to which this lemma belongs, like 'car.n.01'
- name: the actual "word", like "automobile"

nltk.app.wordnet(): you can, for instance, explore the WordNet hierarchy by following hypernym/hyponym links
- i didn't let it through Windows Firewall on my first try and was too lazy to change the setting

nltk.corpus.verbnet: "a hierarchical verb lexicon linked to WordNet"


2.8   Exercises
===============
4. nltk.corpus.state_union: reader for multiple plaintext documents
13. wordnet.all_synsets('n'): returns all noun synsets. WARNING: THIS IS A GENERATOR, NOT A LIST; use it ONCE in a for loop
'''
