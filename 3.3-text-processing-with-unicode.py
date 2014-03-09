# -*- coding: utf-8 -*-
# note that this script does NOT run from windows command line
# works fine in IDLE, though
import codecs, nltk, unicodedata

file = codecs.open(
        nltk.data.find('corpora/unicode_samples/polish-lat2.txt'),
        encoding='latin2'
        )

lines = file.readlines()
for line in lines:
    print line.strip().encode('unicode_escape')
    
# ord(char) returns the (ascii-only?!) code of char
print "0x%x" % ord('a'), "\x61"

# Unicode is logical (in-memory), UTF-8 is physical (on-disk)
unicode_str = u"\u0144"
print unicode_str                           # works in IDLE!
print repr(unicode_str)                     # prints escaped unicode
print repr(unicode_str.encode('utf8'))      # prints escaped UTF-8 (series of bytes)

zh_str = u"我恨你"                         # note the leading 'u'! needed by for loop to step over chars correctly
for ch in zh_str:
    print ch, repr(ch), repr(ch.encode('utf8')), unicodedata.name(ch)
# 我 u'\u6211' '\xe6\x88\x91' CJK UNIFIED IDEOGRAPH-6211
# 恨 u'\u6068' '\xe6\x81\xa8' CJK UNIFIED IDEOGRAPH-6068
# 你 u'\u4f60' '\xe4\xbd\xa0' CJK UNIFIED IDEOGRAPH-4F60 <-- names are more informative for non-CJK languages



# and now here's some regex foreshadowing/sloppy editing?
# works with unicode!! just have to be careful about escaping chars.
line = lines[2]
print line.encode('unicode_escape')
import re
search_regex = u'\u015b\w*'
match = re.search(search_regex, line)
print "\nsearch for", repr(search_regex), "found group:", repr(match.group())


