#! /usr/bin/env python

### python function for loading the raw data

import os

def load_data(folder_address):
	''' loads data from the specified folder and returns list containing filenames '''

	data = os.listdir(folder_address)

	data.sort()

	docs = []
	imgs = []
	caps = []

	for fil in data:
		filn, filex = os.path.splitext(fil)

		if filex == '.jpg':
			imgs.append(folder_address + '/' +fil)

		elif filex == '.txt':
			caps.append(folder_address + '/' +fil)

		elif filex == '.html':
			docs.append(folder_address + '/' +fil)

	return docs, imgs, caps


