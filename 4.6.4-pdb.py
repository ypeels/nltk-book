'''
Section 4.6.4: Debugging Techniques

Apparently you can run 'pdb' interactively.
I'd expect this to be similar to 'gdb'?
Type "help" at the pdb prompt to find out...

List of commands mentioned in the book:
- 's' or 'step' (Step Into)
- 'n' or 'next' (Step Over)
- 'b' or 'break'
- 'c' or 'continue'
- 'h' or 'help' (or '?' ??)
- type the name of any variable to inspect
- 'args' to show value of any arguments in current function

>>> import pdb
>>> pdb.run("foo('asdf')")
'''

print __doc__

