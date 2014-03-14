# Natural Language Toolkit: code_hill_climb

'''
Example 4.4 from Chapter 4 Extras 4.7: Search
Figure 4.4: Hill-Climbing Search
'''

from code_evaluate import evaluate  # hmmm.... old Chapter 3 snippets...
from code_segment import segment


def flip(segs, pos):
    '''Single-segment MC move, same as in code_anneal'''
    #return segs[:pos] + `1-int(segs[pos])` + segs[pos+1:]          # backquotes (`) are an alternative to repr()? http://stackoverflow.com/questions/7490261/python-repr-vs-backquote
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]        # changed to code_anneal's version
    
def hill_climb(text, segs, iterations):
    '''Greedy optimization using single-flip moves only
    
    Note that without flip_n, which modified segs in-place, we need not worry about juggling segs and best!
    '''
    best = evaluate(text, segs)                                     # 
    for i in range(iterations):
        print i,
        pos = -1                                                    
        #pos, best = 0, evaluate(text, segs)                        # pos should really be out of range - what if the first word is a single letter??
        for i in range(len(segs)):
            score = evaluate(text, flip(segs, i))
            if score < best:
                pos, best = i, score                                # is it just the C programmer in me, or is this LESS legible?
        if pos >= 0:                                                # found a greed-satisfying move (changed from !=)
            segs = flip(segs, pos)
            print evaluate(text, segs), segment(text, segs),
        print
    return segs

if __name__ == "__main__":

    # data from code_anneal.py??
    text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
    seg1 = "0000000000000001000000000010000000000000000100000000000"
    
    print evaluate(text, seg1), segment(text, seg1)
    # 63 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
    
    hill_climb(text, seg1, 20)
    # 61 ['doyouseethekittyseethedoggy', 'doyoulikethekitty', 'likethedoggy']
    # 59 ['doyouseethekittyseethedoggydoyoulikethekitty', 'likethedoggy']
    # 57 ['doyouseethekittyseethedoggydoyoulikethekittylikethedoggy'] 
    # hahahahahaha greed is a sin