#! /usr/bin/env python

import numpy as np


## process images

from load_data import load_data

from ImagePreProcessor.ProcessImage import process_image

docs, imgs, caps = load_data('../data')


deslist = np.empty((0,128))
img_sizes = []

for img in imgs:
	print img
	des = process_image(img)
	img_sizes.append(des.shape[1])

	deslist = np.concatenate((deslist,des))


np.save('img_features.data',deslist)
np.save('img_sizes.data',np.asarray(img_sizes))

