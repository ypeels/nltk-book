'''
Exercise 3.10
Just more list comprehension practice
'''

print __doc__

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']

iterative_result = []
for word in sent:
    word_len = (word, len(word))
    iterative_result.append(word_len)

listcomp_result = [(word, len(word)) for word in sent]
print listcomp_result
print "Equivalent to iterative version?", listcomp_result == iterative_result
