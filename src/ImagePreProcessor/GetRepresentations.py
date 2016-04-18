#! /usr/bin/env python

### cluster image features to form Visual Terms

from sklearn.cluster import KMeans
import numpy as np

def get_visual_terms(deslist):
	''' this function uses kmeans clustering algorithm to learn visual terms '''

	kmeans_model = KMeans(n_clusters = 2000, random_state = 1).fit(deslist)

	labels = kmeans_model.labels_

	centers = kmeans_model.cluster_centers_

	np.save('visual_terms_centers',centers)

	np.save('labels',labels)
	return

	

def get_images():
	''' this function loads the data and convert images to required format '''

	img_sizes = np.ndarray.tolist(np.load('img_sizes.data.npy'))


	labels = np.ndarray.tolist(np.load('labels.npy'))

	img_rep = []
	img_p = [0]
	sumt = 0
	for img_s in img_sizes:
		sumt = sumt + img_s
		img_p.append(sumt)

	for i in range(len(img_p)-1):
		img_rep.append(labels[img_p[i]:img_p[i+1]])

	tese = []
	for img_rep_array in img_rep:
		tes = []
		for img_rep_cell in img_rep_array:
			tes.append(str(img_rep_cell))
		tese.append(tes)

	
	return tese


