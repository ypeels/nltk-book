'''
Section 4.1.3  Conditionals

Apparently, Python offers built-in functions any(arg) and all(arg), where 
arg is a sequence (or generator?) of conditionals
'''

  	

sent = ['No', 'good', 'fish', 'goes', 'anywhere', 'without', 'a', 'porpoise', '.']
print all(len(w) > 4 for w in sent)  # False
print any(len(w) > 4 for w in sent)  # True

