


def wget(url):
    from urllib import urlopen
    print "Fetching", url, "..."
    return urlopen(url).read()                              # see text for manual proxy configuration
    

if __name__ == "__main__":
    
    num_to_display = 150
    url = "http://www.gutenberg.org/files/2554/2554.txt"    # still valid, as of this writing (2014-03-09)

    raw = wget(url)
    print "raw string: ", raw [:num_to_display]
    
    import nltk
    tokens = nltk.word_tokenize(raw)
    print "token list:", tokens[:num_to_display]
    print "pass a TOKEN list to nltk.text.Text() to instantiate, enabling use of Chapter 2 API"

# http://www.gutenberg.org/ebooks/2554.txt.utf-8 as of this writing 
# http://www.gutenberg.org/files/2554/2554.txt