print '''
Getting Started with Python
- using my installation of Portable Python 2.7.3

Getting Started with NLTK: Windows install
- http://www.nltk.org/install.html > https://pypi.python.org/pypi/nltk
- python setup.py build
- python setup.py install  # don't mind irreversible install on my Portable Python


didn't need to
- install PyYAML (did it auto-download via nltk's setup.py? didn't pay attention...)
- install numpy (it's included in the standard python libraries as of 2.7.3)


Getting Started with NLTK: Linux install (Ubuntu 12.04)
- http://www.nltk.org/install.html > http://pypi.python.org/pypi/setuptools
- wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
- sudo easy_install pip
- sudo pip install -U nltk  # autofetches PyYAML; -U flag is to Upgrade any existing packages
- sudo pip install -U numpy # NOT auto-installed on Linux! leaner/meaner?
  - SystemError: Cannot compile 'Python.h'. Perhaps you need to install python-dev|python-devel.
  - ugh, hold off on python-dev (and therefore numpy) for now, since it's 30+ MB


Installing NLTK-Data
- >>> import nltk
- >>> nltk.download()
- Collections > book
- pycmd.bat: setenv NLTK_DATA to store corpora locally. sheesh...can't i just modify PYTHONPATH?
- >>> from nltk.book import * [slow!! reads the corpora INTO MEMORY]
'''
