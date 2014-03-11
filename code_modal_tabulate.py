'''
Example 3.11 from Section 3.9  Formatting: From Lists to Strings

A "manual" implementation of ConditionalFreqDist.tabulate()
'''

# Natural Language Toolkit: code_modal_tabulate

def tabulate(cfdist, words, categories):
    category_width = 16
    column_width = colw = max(len(w) for w in words)                           # as suggested in the text. note `print,` lets you get away with len instead of len+1

    print '%-*s' % (category_width, 'Category'),        # left-justify         # note tuple needed for variable width
    for word in words:                                  # column headings
        print '%*s' % (column_width, word),                                    # presupposes that column data and headers will be 5 chars or narrower
    print                                                                      # less ugly than  ` print "" `
    for category in categories:
        print '%-*s' % (category_width, category),      # row heading
        for word in words:                              # for each word
            print '%*d' % (colw,cfdist[category][word]),# print table cell
        print                                           # end the row


         
if __name__ == "__main__":
    print __doc__
  	
    import nltk
    cfd = nltk.ConditionalFreqDist(
              (genre, word)
              for genre in nltk.corpus.brown.categories()
              for word in nltk.corpus.brown.words(categories=genre))
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    tabulate(cfd, modals, genres)