print '''
Chapter 4 Extras
4.8   Object-Oriented Programming in Python (DRAFT)

Pretty standard stuff...

Of note:
- override __getitem__(self, index) to implement [] accessor
- isinstance(item, T) is a shortcut for `type(item) == T`, with some extra features
- override __repr__ to output the string of your choice when an instance is wrapped with repr()
- override __str__  to output the string of your choice when an instance is wrapped with str()?