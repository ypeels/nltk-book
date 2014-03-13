'''
Some examples of the linear algebra capabilities of numpy.

Not gonna install it on Linux right now:
- sudo pip install numpy
    - need python.h from python-dev
- sudo apt-get install python-dev
    - forget it; this is like 40 MB
    

"There are many other Python libraries, and you can search for them with the help of the 
Python Package Index http://pypi.python.org/. 

Many libraries provide an interface to external software, such as relational databases (e.g. mysql-python) 
and large document collections (e.g. PyLucene). 

Many other libraries give access to file formats such as PDF, MSWord, and XML (pypdf, pywin32, xml.etree), 
RSS feeds (e.g. feedparser), and electronic mail (e.g. imaplib, email)."
'''

print __doc__

from numpy import array

cube = array([ [[0,0,0], [1,1,1], [2,2,2]],
               [[3,3,3], [4,4,4], [5,5,5]],
               [[6,6,6], [7,7,7], [8,8,8]] ])
               
print cube[1,1,1]                       # 4   - note "fortran-like" indexing

print cube[2].transpose()
# array([[6, 7, 8],
#        [6, 7, 8],
#        [6, 7, 8]])

print cube[2,1:]
# array([[7, 7, 7],
#        [8, 8, 8]])



from numpy import linalg
a=array([[4,0], [3,-5]])
u, s, vt = linalg.svd(a)                # "used in latent semantic analysis to help identify implicit concepts in a document collection"

print u
# array([[-0.4472136 , -0.89442719],
#        [-0.89442719,  0.4472136 ]])

print s
# array([ 6.32455532,  3.16227766])

print vt
# array([[-0.70710678,  0.70710678],
#        [-0.70710678, -0.70710678]])
