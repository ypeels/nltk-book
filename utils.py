# convenient list of all texts; first concocted in 1.1.4
from nltk.book import *
all_texts = [ locals()['text' + str(index+1)] for index in range(9) ]