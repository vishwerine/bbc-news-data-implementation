#! /usr/bin/env python

### this is the main program for text processing


import codecs

from HTMLParser import HTMLParser

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

from stop_words import get_stop_words




class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.plist = []

	def handle_starttag(self,tag,attrs):
		return

	def handle_endtag(self,tag):
		return

	def handle_data(self,data):
		self.plist.append(data)
		return



def parse(document):
	''' this function takes HTML Document and returns a list of tokens'''

	parser = MyHTMLParser()

	f = codecs.open(document,encoding="ISO-8859-1")

	parser.feed(f.read())

	docstr = ""

	for t in parser.plist:
		docstr = docstr + t

	raw = docstr.lower()

	tokenizer = RegexpTokenizer(r'\w+')

	tokens = tokenizer.tokenize(raw)

	en_stop = get_stop_words('en')

	stopped_tokens = [i for i in tokens if not i in en_stop]

	p_stemmer = PorterStemmer()

	texts = []

	for i in stopped_tokens:
		try:
			i = p_stemmer.stem(i)
		except:
			i = i
		else:
			pass
		texts.append(i)

	return texts


