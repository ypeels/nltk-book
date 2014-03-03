print '''

In order of appearance.
To display docstring of 'obj', just perform
>>> help(obj)

1.1 Computing with Language: Text and Words
===========================================

>>> from nltk.book import *

nltk.text.Text instance methods
-----------------
concordance(word): prints all occurrences of 'word', with surrounding context
similar(word): prints words that appear in a similar context as 'word'?
common_contexts([word_list]): contexts shared by two or more words...[what's with the underscores??]
dispersion_plot([word_list]): plots word occurrences vs word offset.  Cool!
generate(): generates random text in the style of the object instance.  Cool!!  Note punctuation separation
'''