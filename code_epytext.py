'''
Example 4.5 from Section 4.4: Documenting Functions

As downloaded, file was corrupt and had "izip" instead of "zip" inthe for loop.
https://github.com/nltk/nltk_book/issues/49

Largely noteworthy as an example of how 'NLTK uses the "epytext" markup language to document parameters.'
'''


# Natural Language Toolkit: code_epytext

def accuracy(reference, test):
    '''
    Calculate the fraction of test items that equal the corresponding reference items.

    Given a list of reference values and a corresponding list of test values,
    return the fraction of corresponding values that are equal.
    In particular, return the fraction of indexes
    {0<i<=len(test)} such that C{test[i] == reference[i]}.

    @param reference: An ordered list of reference values.
    @type reference: C{list}
    @param test: A list of values to compare against the corresponding
        reference values.
    @type test: C{list}
    @rtype: C{float}
    @raise ValueError: If C{reference} and C{length} do not have the
        same length.
    '''                                                             # NLTK uses "epytext" markup language to document parameters

    if len(reference) != len(test):
        raise ValueError("Lists must have the same length.")        # ooh, silently introducing exceptions, are we?    
    num_correct = 0
    for x, y in zip(reference, test):                               # this was originally "izip(reference, test)"
        if x == y:
            num_correct += 1
    return float(num_correct) / len(reference)
    
    
if __name__ == "__main__":
    print __doc__
    print accuracy(['ADJ', 'N', 'V', 'N'], ['N', 'N', 'V', 'ADJ'])  # 0.5