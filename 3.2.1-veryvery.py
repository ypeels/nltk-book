'''"Your Turn" in subsection "Basic Operations with Strings"'''
a = range(1, 8) + range(6, 0, -1)
b = [' '*2*(7-i) + 'very'*i for i in a]

# prediction: this will print a diamond of "very"
for line in b:
    print line
    # nailed it!