'''
Example 4.6 in Section 4.5.2: Accumulative Functions (a.k.a. Generators)

Figure 4.6: Accumulating Output into a List
'''

# Natural Language Toolkit: code_search_examples

def search1(substring, words):
    '''iterative, "standard way to" accumulate search hits into a list
    
    returns aggregated results as a list'''
    result = []
    for word in words:
        if substring in word:
            result.append(word)
    return result

def search2(substring, words):
    '''generator that will output the same results as search1(), if both are called in a for loop
    
    note that unlike search1(), it's up to the caller to store all aggregate results here'''
    for word in words:
        if substring in word:
            yield word

            
if __name__ == "__main__":
    import nltk

    print search1.__doc__
    print "search1 results (will display in one big shot - cuz it's allocating huge storage):"
    for item in search1('zz', nltk.corpus.brown.words()):
        print item
        
    print search2.__doc__
    print "search2 results (will stream out piecewise):"
    for item in search2('zz', nltk.corpus.brown.words()):
        print item

