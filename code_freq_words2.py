'''
Example 4.4 from Section 4.4.5: Functional Decomposition

Revision to Example 4.3 (code_freq_words1.py)
'''

import nltk

# Natural Language Toolkit: code_freq_words2

def freq_words(url):
    '''Figure 4.4: Well-Designed Function to Compute Frequent Words'''
    freqdist = nltk.FreqDist()                  # no more side effect of modifying an input parameter
    text = nltk.clean_url(url)
    for word in nltk.word_tokenize(text):
        freqdist.inc(word.lower())
    return freqdist


if __name__ == "__main__":
    constitution = "http://www.archives.gov/national-archives-experience" \
                   "/charters/constitution_transcript.html"
    fd = freq_words(constitution)
    result1 = fd.keys()[:20]                        
    print result1                               # no more printing inside freq_words(): more reusable
    
    print "we have now simplified the work of freq_words to the point that we can do its work with three lines of code"
    print "[Is this really appropriate? I thought you're trying to teach English majors that 'functions are good'...]"
    words = nltk.word_tokenize(nltk.clean_url(constitution))
    fd = nltk.FreqDist(word.lower() for word in words)
    result2 = fd.keys()[:20]
    print result2
    print "Answers are equivalent?", result1 == result2