import textwrap
saying = "After all is said and done , more is said than done .".split()
format = '%s_(%d),'
pieces = [format % (word, len(word)) for word in saying]
output = ' '.join(pieces)
wrapped = textwrap.fill(output)                             # the (poorly named) function str.fill() wraps a string to a specified width (default 70)
print wrapped.replace('_', ' ')                             # keep words and lengths on the same line - from discussion in text