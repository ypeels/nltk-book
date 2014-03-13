'''Notes on the NLTK API

In order of appearance (some liberties taken within each section for readability)
To display docstring of 'obj', just perform
>>> help(obj)
'''
print __doc__

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
- accessible as nltk.FreqDist
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


print '''
3.  Processing Raw Text
#######################

3.1   Accessing Text from the Web and from Disk
===============================================

nltk.word_tokenize(str): returns list of all tokens (words and punctuation)
nltk.clean_html(str): returns string of all RAW TEXT (scrubs 'str' of all html tags, headers)
nltk.wordpunct_tokenize(str): returns list of all tokens, with punctuation tokenized a LITTLE more aggressively/in a less sophisticated manner?

nltk.text.Text(self, tokens, name=None): needs list of TOKENS to instantiate, not raw string
nltk.data.find(<relative path in nltk_data>): returns absolute path of file name for any corpus item

Third party libraries mentioned in the book
-----------------------
- the "more sophisticated... Beautiful Soup package" for HTML scrubbing
- Universal Feed Parser to process RSS feeds
- pypdf to access text in PDF binary files
- pywin32 to access text in MSWord binary files

Python notes that my 2 previous tutorials somehow missed? (Or I didn't note)
- type(var) displays the type of 'var'


3.4   Regular Expressions for Detecting Word Patterns
=====================================================
nltk.corpus.treebank: "raw, tagged, parsed and combined data from Wall Street Journal for 1650 sentences (99 treebank files wsj_0001 .. wsj_0099)


3.5   Useful Applications of Regular Expressions
================================================
nltk.corpus.toolbox: uh, a rotokas dictionary? get all words using words('rotokas.dic')

nltk.tokenwrap(tokens): pretty print list of text tokens, breaking lines on whitespace

nltk.probability.ConditionalFreqDist: can be initialized with a list of 2-char strings, since "each of these is a pair")
- accessible as nltk.ConditionalFreqDist

nltk.util.Index: the "multi-valued dictionary" convenience class i wanted! 
- accessible as nltk.Index
- construct with a list of pairs: index = nltk.Index( [(key, value)] ), where there MAY BE DUPLICATE KEYS
- access with index[key]: [ value1, ..., valueN ]

nltk.text.Text
- accessible as nltk.Text
- findall() takes NLTK-CUSTOM regexps with angle brackets used to mark token boundaries
    - ALL whitespace is ignored? (big whoop)
    - verbose regexps are not supported (nooooooo! well, you could piece the string together...)? maybe with "(?x)" flag?? see 3.7
    - cannot compile?? oh boy...
    - PRINTS RESULTS ONLY - doesn't save the data... doesn't seem very useful...
        - and DOESN'T do what you expect, i.e., return value is DIFFERENT from re.findall()
    
nltk.re_show(regexp, s)
- prints s, with {matches to regexp} delimited
- like Text.findall() this only seems useful in interactive mode...
    
nltk.app.nemo(): graphical interface for exploring regular expressions. "Finding (and Replacing) Nemo"
- Nemo box: the regexp
- maki box: replacement text, with \# marking the #th captured substring
- kinda silly, since the book hasn't talked about substitutions yet...


3.6   Normalizing Text
======================
nltk.stem.porter.PorterStemmer
nltk.stem.lancaster.LancasterStemmer
- stem(str) is an instance method of each: returns a guess at the stem of str (e.g., "lie" for "lying")
- "The Porter Stemmer is a good choice if you are indexing some texts and want to support search using alternative forms of words"

nltk.stem.wordnet.WordNetLemmatizer
- lemmatize(str) removes affixes of 'str' if it is in its dictionary
- "The WordNet lemmatizer is a good choice if you want to compile the vocabulary of some texts and want a list of valid lemmas (or lexicon headwords)."

So they never DEFINED normalization explicitly  , but examples include
- converting all words to lower case
- stemming all words ('lying' becomes 'lie', etc.)
- lemmatization (see chapter summary in text)


3.7   Regular Expressions for Tokenizing Text
=============================================
nltk.regexp_tokenize(text, pattern, gaps=False): the REAL equivalent of re.findall() and re.split()...
- gaps: when False, the function behaves EXACTLY like re.findall(); when True, the function behaves EXACTLY like re.split()
- differences with 're' that i just find confusing
    - start pattern with "(?x)" to enable verbose regexps!? come ON, you're going to make this even MORE OPAQUE!?
    - avoids the need for special treatment of parentheses (don't need to start parenthesized expression with "?:")
- "nltk.regexp_tokenize() is more efficient [than re.findall()]"
    - but i find that timeit numbers confirm the OPPOSITE - that this stupid function is friggin SLOWER than vanilla re.findall() and re.split()

    
3.8   Segmentation
==================
nltk.tokenize.punkt.PunktSentenceTokenizer
- nltk.data.load('tokenizers/punkt/english.pickle'): unserializes Punkt sentence segmenter
    - from README, these things are mostly data, generated from nltk.tokenize.punkt, and trained on lots of corpora
- tokenize(raw text): segments raw text into sentences, which it returns 


3.9   Formatting: From Lists to Strings
=======================================
nltk.corpus.genesis.words('english-kjv.txt')


3.12  Exercises
===============
nltk.metrics.spearman.spearman_correlation
- available as nltk.spearman_correlation(ranks1, ranks2)
- returns a correlation coefficient for 2 rankings, each dicts or sequences of (key, rank)
    - "only calculated for keys in both rankings (for meaningful results, remove keys present in only one list before ranking)."
   
   
4.3   Questions of Style 
========================
nltk.probability.FreqDist: cumulative is for plot only! for tables, must do by hand??


4.4   Functions: The Foundation of Structured Programming
=========================================================
nltk.util.clean_url(url)
- accessible as nltk.clean_url
- convenience function that combines wget + clean_html()


4.6   Program Development
=========================
- "Most NLTK modules also include a demo() function which can be used to see examples of the module in use"


4.8   A Sample of Python Libraries
==================================
"NLTK's clustering package nltk.cluster makes extensive use of NumPy arrays, 
and includes support for k-means clustering, Gaussian EM clustering, 
group average agglomerative clustering, and dendrogram plots. 
For details, type help(nltk.cluster)."

[First you have to explicitly `import nltk.cluster`]

'''
