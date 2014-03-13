# Natural Language Toolkit: code_modal_plot

'''
Example 4.13 from Section 4.8.1: Matplotlib

The Matplotlib package supports sophisticated plotting functions with a MATLAB-style interface

I didn't bother looking up all the API calls...
'''

import pylab


colors = 'rgbcmyk' # red, green, blue, cyan, magenta, yellow, black
def bar_chart(categories, words, counts):
    '''Plot a bar chart showing counts for each word by category'''
    #import pylab                                                           # doesn't this belong outside the function?
    ind = pylab.arange(len(words))
    width = 1.0 / (len(categories) + 1)                                     # made the quotient backwards-compatible (is the ".0" really so burdensome, English majors?)
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind+c*width, counts[categories[c]], width,
                         color=colors[c % len(colors)])                     # module variable 'colors'
        bar_groups.append(bars)
    pylab.xticks(ind+width, words)
    pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    pylab.show()


if __name__ == "__main__":
    import nltk    

    genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfdist = nltk.ConditionalFreqDist(
                 (genre, word)
                 for genre in genres
                 for word in nltk.corpus.brown.words(categories=genre)
                 if word in modals)
    
    counts = {}
    for genre in genres:
        counts[genre] = [cfdist[genre][word] for word in modals]
    bar_chart(genres, modals, counts)