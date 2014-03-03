print '''
Getting Started with Python
- using my installation of Portable Python 2.7.3

Getting Started with NLTK
- http://www.nltk.org/install.html > https://pypi.python.org/pypi/nltk
- python setup.py build
- python setup.py install
- >>> import nltk
- >>> nltk.download()
- Collections > book
- pycmd.bat: setenv NLTK_DATA to store corpora locally. sheesh...can't i just modify PYTHONPATH?
- >>> from nltk.book import * [slow!! reads the corpora INTO MEMORY]

didn't need to
- install PyYAML
- install numpy (it's included in the standard python libraries as of 2.7.3)
'''