# Example 2.6
# Natural Language Toolkit: code_plural

def plural(word):
    '''"This function tries to work out the plural form of any English noun.
        
        From Example 2.6.
        As the text mentions, this is a work in progress! 
        >>> plural('fan')  # fen
        >>> plural('span')  # spen    
    '''
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

