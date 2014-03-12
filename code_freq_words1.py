'''
Example 4.3 from Section 4.4.5: Functional Decomposition

Revised in Example 4.4 (code_freq_words2.py)
'''

import nltk

# Natural Language Toolkit: code_freq_words1

def freq_words(url, freqdist, n):
    '''Figure 4.3: Poorly Designed Function to Compute Frequent Words'''
    text = nltk.clean_url(url)
    for word in nltk.word_tokenize(text):
        freqdist.inc(word.lower())          # problem 1: modifies freqdist argument as a side-effect
    print freqdist.keys()[:n]               # problem 2: prints result (makes this less reusable)


    
if __name__ == "__main__":
    print __doc__
    
    constitution = "http://www.archives.gov/national-archives-experience" \
                   "/charters/constitution_transcript.html"
    fd = nltk.FreqDist()
    freq_words(constitution, fd, 20)
    # ['the', 'of', 'charters', ',', 'bill', 'constitution', 'declaration', 'rights', '-', '.', 'freedom', 'impact', 'independence', 'making']