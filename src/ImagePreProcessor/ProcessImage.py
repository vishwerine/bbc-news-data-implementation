#! /usr/env/bin python 

## processes images and converts them to required format


import cv2

def process_image(img_path):
	''' input an image path and this will return an np array of SIFT Features '''

	img = cv2.imread(img_path)

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	sift = cv2.SIFT()

	kp , des = sift.detectAndCompute(gray, None)

	return des


