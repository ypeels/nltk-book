'''Exercise 2.23: Zipf's Law'''
import nltk, pylab

def zipf_plot(text):
    '''Creates a log-log plot of word frequency vs word rank.
    
    "a function to process a large text and plot word frequency against word rank using pylab.plot"
    
    Precondition: 'text' contains a list of words.
    '''
    
    fdist = nltk.FreqDist(text)
    
    # figured out pylab.plot syntax, sadly, from random googling
    pylab.plot(
            range(1, fdist.B() + 1),      # x-axis: word rank
            fdist.values()                # y-axis: word count
            )
            
    # http://stackoverflow.com/questions/773814/plot-logarithmic-axes-with-matplotlib-in-python
    # just do a visual inspection and be done with it
    # not exactly doing a linear regression analysis here      
    pylab.xscale('log')
    pylab.yscale('log')
    pylab.show()
    

    
if __name__ == "__main__":
    #text = nltk.corpus.gutenberg.words('austen-sense.txt')
    
    
    #import utils  # 
    #for text in utils.all_texts:   # this works fine, but is too slow for testing Part 2
    
    #text = utils.all_texts[ random.choice(range(9)) ]
    #print "Part 1: Now plotting Zipf's Law plot for:", text.name
    #zipf_plot(text)
    
    print '''
    # analysis
    # The "Zipf plots" ARE quite linear in the middle portion!! Zipf's law is empirically corroborated.
    # For large x (rank), lots of words have the same count, so there are lots of flat portions
        # there's also probably a flatline at log(count) = 0 (singleton words) that's buried under the x-axis
    # For small x (rank), there are often nonlinear transients, probably because punctuation/smileys behave abnormally.
    '''
    
    import numpy, random
    target_length = 456477#numpy.mean( [len(" ".join(text)) for text in utils.all_texts] )   


    
    # Use the string concatenation operator to accumulate characters into a (very) long string.
    random_string = ""
    while len(random_string) < target_length:
        random_string += random.choice('abcdefg ')
        
    # Then tokenize this string, and generate the Zipf plot as before,
    random_text = random_string.split()
    print "Part 2: Plotting Zipf's Law plot for random text"
    zipf_plot(random_text)
    
    print '''
    Analysis:
    Zipf plot of randomly generated strings (with 1/8 probability of whitespace) is NOT linear.
    Weirdly, though, there are "steps" in the log-log plot, which I don't really want to think too hard about...
    
    Zipf's law appears to be, at the very least, a property of written English.
    '''