'''
Python's standard libraries include csv support!

Boy, when they say 'batteries included'...

Here is some sample usage

>>> import csv
>>> input_file = open("lexicon.csv", "rb")
>>> for row in csv.reader(input_file):
...     print row

note that these will all be raw STRINGS.
'''

print __doc__
