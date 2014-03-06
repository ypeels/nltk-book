import nltk
from nltk.corpus import brown


print '''
working through the "Your Turn" in subsection "Plotting and Tabulating Distributions"
# "condition" vs "sample" is hella confusing... so much so that there's a typo in the book!
'''


# meh, datetime.date requires working with date INSTANCES. figuring it out would take longer...
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# genres limited to the ones we want to query for THIS problem.
# could further limit word to 'days'...but this seems fast enough
# uh, not sure this answers "which days of the week are most newsworth"
# it just answers "how frequently day-of-week strings occur in genres", and poorly (no abbreviations, lowercase variations, etc.)
print "Generating conditional frequency distribution (may be slow...)"
cfd_brown = nltk.ConditionalFreqDist(
                (genre, word)                       # actually a generator expression!
                for genre in ['news', 'romance']    # instead of full brown.categories()  
                for word in brown.words(categories=genre)
                )   

cfd_brown.tabulate(samples=days)

# As of this writing (2014-03-06), the Note in the chapter incorrectly says "conditions="
days.reverse()  # reverses list IN PLACE - how annoying...
cfd_brown.plot(samples=days)
days.reverse()

                
if __name__ == "__main__":
    import os, sys
    print os.path.basename(sys.argv[0]), "all done."
