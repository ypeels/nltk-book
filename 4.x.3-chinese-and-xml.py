# -*- coding: utf-8 -*-

import codecs, nltk 

path = nltk.data.find('corpora/unicode_samples/sinorama-gb.xml')        # book incorrectly had 'samples/sinorama-gb.xml'
f = codecs.open(path, encoding='gb2312')
lines = f.readlines()
for L in lines:
    L = L[:-1]
    utf_enc = L.encode('utf8')
    print repr(utf_enc)
    print utf_enc
    
# '<?xml version="1.0" encoding="gb2312" ?>'
# ''
# '<sent>'
# '\xe7\x94\x9a\xe8\x87\xb3\xe7\x8c\xab\xe4\xbb\xa5\xe4\xba\xba\xe8\xb4\xb5'
# ''
# 'In some cases, cats were valued above humans.'
# '</sent>'

# "With appropriate support on your terminal, the escaped text string inside the <SENT> element above will be rendered 
# as the following string of ideographs: 甚至猫以人贵."
# - didn't work in IDLE. meh.


print '"We can also read in the contents of an XML file using the etree package (at least, if the file is encoded as UTF-8 — '
print 'as of writing, there seems to be a problem reading GB2312-encoded files in etree).'
path_utf8 = nltk.data.find('corpora/unicode_samples/sinorama-utf8.xml') # book incorrectly had 'samples/sinorama-utf8.xml'
#from nltk.etree import ElementTree as ET
from xml.etree import ElementTree as ET
tree = ET.parse(path_utf8)
text = tree.findtext('sent')
uni_text = text.encode('utf8')
print repr(uni_text.splitlines()[1])
print uni_text.splitlines()
# '\xe7\x94\x9a\xe8\x87\xb3\xe7\x8c\xab\xe4\xbb\xa5\xe4\xba\xba\xe8\xb4\xb5'
