#! /usr/bin/env python

from gensim import corpora, models
import numpy as np

### main script for text processing

from load_data import load_data

from TextPreProcessor.Parser import parse
from ImagePreProcessor.GetRepresentations import get_images , get_visual_terms


docs, imgs, caps = load_data('../data')

texts = []
for doc in docs:
	text = parse(doc)
	texts.append(text)


tese = get_images()

### convert images to required representation

dictionary = corpora.Dictionary(texts + tese)

dictionary.save('dictionary')

mixed_doc = []

for i in range(len(tese)):
	temp = texts[i] + tese[i]
	mixed_doc.append(temp)

corpus = [dictionary.doc2bow(i) for i in mixed_doc]

ldamodel = models.ldamodel.LdaModel(corpus, num_topics = 750, id2word = dictionary , passes = 5)

ldamodel.save('ldamodel')


