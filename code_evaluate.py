'''
Example 3.9 from Section 3.8  Word Segmentation
'''



from code_segment import segment

# Natural Language Toolkit: code_evaluate

def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    #print 'sum(seg) =', sum(map(int, list(segs)))
    return text_size + lexicon_size                 # Figure 3.8: the objective function from Brent 1995
                                                    # lexicon_size will be off by 1 relative to the Figure (which added a boundary marker to EVERY word)

if __name__ == "__main__":
    print __doc__
    text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
    seg1 = "0000000000000001000000000010000000000000000100000000000"
    seg2 = "0100100100100001001001000010100100010010000100010010000"
    seg3 = "0000100100000011001000000110000100010000001100010000001"
    print segment(text, seg3)
    print evaluate(text, seg3)                      # 46: 14 segments, lexicon_size = 32
    print evaluate(text, seg2)                      # 47: 15 segments, lexicon_size = 32
    print evaluate(text, seg1)                      # 63: 3 segments, lexicon_size = 60
    
# brief intuition
# - more segments means smaller words
# - smaller words means greater likelihood for repeat usage
# - repeat usage means lower lexicon score (repeated usage of same word is counted only once)