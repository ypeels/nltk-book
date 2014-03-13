# Natural Language Toolkit: code_modal_plot

'''
Example 4.13 from Section 4.8.1: Matplotlib

The Matplotlib package supports sophisticated plotting functions with a MATLAB-style interface

I didn't bother looking up all the API calls...
'''

#import pylab                                                               # CANNOT IMPORT HERE, not if you want to be able to change backend and save to png... crotchety pylab api...


colors = 'rgbcmyk' # red, green, blue, cyan, magenta, yellow, black
def bar_chart(categories, words, counts):
    '''Plot a bar chart showing counts for each word by category'''
    import pylab                                                            # doesn't this belong outside the function? NO (see above)
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

print 'asdfasdf'
if __name__ == "__main__":
    import nltk

    genres = ['news', 'religion', 'hobbies', 'government', 'adventure']     # all this just sets up data for bar_chart
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    cfdist = nltk.ConditionalFreqDist(
                 (genre, word)
                 for genre in genres
                 for word in nltk.corpus.brown.words(categories=genre)
                 if word in modals)
    
    counts = {}
    for genre in genres:
        counts[genre] = [cfdist[genre][word] for word in modals]
        
    import sys
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] != 'save'):
        bar_chart(genres, modals, counts)                                   # <==== THE MAIN EVENT
    else:    
        import matplotlib                                                   # extra code snippet from book: save figure to disk
        matplotlib.use('Agg')                                               # "must be called *before* pylab, matplotlib.pyplot, or matplotlib.backends is imported for the first time"        
        filename = 'modals.png'
        
        import pylab                                                        # yes, this still has to be below matplotlib.use(). something tells me the 'pylab' api is deprecated...
        bar_chart(genres, modals, counts)                                   # still have to call the main function (eat the show() call?). text was NOT clear about that
        pylab.savefig(filename)
        print "Saved figure to", filename
        

