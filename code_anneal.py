'''
Example 3.10 from Section 3.8  Word Segmentation

Uses simulated annealing (!) to optimize the objective function from Example 3.9
(iirc, simulated annealing applies a [Metropolis!?] Monte Carlo walk to optimize a multidimensional function)


ahhhh that's why they are using such a weird segment data structure
- so they can walk through the 2^(len-1) states easily
'''

from code_segment import segment
from code_evaluate import evaluate

# Natural Language Toolkit: code_anneal

from random import randint

def flip(segs, pos):                                            # proposed MC move (one cell)
    return (
        segs[:pos] +                                            # cells before pos, unmodified
        str(1-int(segs[pos])) +                                 # flip cell 'pos'
        segs[pos+1:]                                            # cells after pos, unmodified
        )
        

def flip_n(segs, n):                                            # proposed MC move (n cells)
    for i in range(n):
        segs = flip(segs, randint(0,len(segs)-1))               # flip n random cells
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))                              # initialize T to something big
    best_segs, best = segs, evaluate(text, segs)                # initialization really belongs WAY out here
    while temperature > 0.5:                                    
        #best_segs, best = segs, evaluate(text, segs)           # <-- book has initialization here, unnecessarily
        for i in range(iterations):                             # instead of the Metropolis criterion: 
            guess = flip_n(segs, int(round(temperature)))       # - make "iterations" random moves
            score = evaluate(text, guess)                       
            if score < best:
                best, best_segs = score, guess                  # - keep your best score from all those moves 
        
        #score, segs = best, best_segs                          # only segs needs to be updated for next T
        segs = best_segs
        
        temperature = temperature / cooling_rate                # temperature, and thus move "length", gradually decreases
        
        #print evaluate(text, segs), segment(text, segs)        # my version shows intent more cleanly - running high score
        print evaluate(text, best_segs), segment(text, best_segs)
        
    print
    return segs


if __name__ == "__main__":
    print __doc__
    text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
    seg1 = "0000000000000001000000000010000000000000000100000000000"
    seg2 = "0100100100100001001001000010100100010010000100010010000"    # for kicks: scores 47, with lower score 44 with "doyou" 
    anneal(text, seg1, 5000, 1.2)
    
    # my best (lowest) score from book's seg1: 42
    # 42:  ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy']