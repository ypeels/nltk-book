# Natural Language Toolkit: code_search_documents

'''
Example 4.10 from Section 4.7: Space-Time Tradeoffs

a simple text retrieval system for the Movie Reviews Corpus
By indexing the document collection it provides much faster lookup.
[Although we're never given a non-indexed version for comparison...]

Touched up so that snippet() is no longer buggy?
'''

import re

tag_re = re.compile(r'<.*?>')                                       # speed that shit up? or are these too short to make a difference?
ws_re = re.compile(r'\s+')


def raw(file):
    '''Opens 'file' and returns it as a string scrubbed of html/xml tags, and with whitespace normalized to " ".'''
    contents = open(file).read()
    contents = tag_re.sub(' ', contents)                            # strip html/xml tags
    contents = ws_re.sub(' ', contents)                             # normalize whitespace. isn't THIS bugged?? (wasn't a raw string in the original)    
    return contents

def snippet(doc, term): # buggy (fixed now?)                        # doesn't seem buggy to me...?? maybe if there are multiple instances of term in doc??
    '''Returns a string in 'doc' that contains 'term'.
    Depends on calling code to keep track of how many times to call it.
    '''
    PAD = 30
    
    text = ' '*PAD + raw(doc) + ' '*PAD

    if snippet.doc != doc:                                          # new document! reset counters
        snippet.doc = doc
        snippet.start_index = 0
    
    pos = text.index(term, snippet.start_index)
    snippet.start_index = pos+1                                     # prepare counter for next snippet
    return text[pos-PAD:pos+PAD]
    
    
# http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
# initialize function's static variables (functions are objects too!)
snippet.doc = None
snippet.start_index = 0
snippet.PAD_WIDTH = 30


if __name__ == "__main__":
    import nltk
    
    print "Building Index..."
    files = nltk.corpus.movie_reviews.abspaths()
    idx = nltk.Index((w, f) for f in files for w in raw(f).split())

    query = ''
    while query != "quit":
        query = raw_input("query> ")                                # i COULD suppress output for "quit" (just combine this line with above), but then how would you ever query that word??
        if query in idx:
            for doc in idx[query]:
                print snippet(doc, query)
        else:
            print "Not found"
        
        

