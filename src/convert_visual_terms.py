#! /usr/bin/env python

## learn k means and get visual terms on all images

from ImagePreProcessor.GetRepresentations import get_visual_terms
import numpy as np


deslist = np.load('img_features.data.npy')
img_sizes = np.ndarray.tolist(np.load('img_sizes.data.npy'))

get_visual_terms(deslist)


