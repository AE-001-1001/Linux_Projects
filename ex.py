import numpy as np
import pandas as pd
from PIL import Image,ImageEnhance



a = np.array([[0,0,1],
	      [1,0,1],
	      [1,1,1],
	      [0,1,1]], dtype = int)
print('Dataset before training: ','\n',a)

def _Pillow_(_file_):
	
	with Image.open(_file_) as im:
		im.convert("L")
		out = im.point(lambda i: i * 1.5)
		ehh = ImageEnhance.Contrast(im)
		enhancer = ImageEnhance.Sharpness(im)
		ehh.enhance(1.3).show("30% More Contrast")
	for i in range(5):
		factor = i / 0.6
		enhancer.enhance(factor).show(f"Sharpeness {factor:f}")
		print(out)	
		return im.show()

def activation(a):
	print('***','\n')
	print('DataSet After Training:')
	for i in a:
		if a.shape == (4,3):
			i ** 2
		if a.any() == 1:
			i+=1
		if a.all() <= 3:
			i-=1
		sigmoid = 1 / (1 * np.exp(-i))
	return print("Sigmoid: ",sigmoid,'\n'),print(np.multiply(18,a))

def backwardprop(arr):
	#Decompiling
	a = np.exp(arr)
	arr = np.array([[15],[30],[45]])
	for x in arr:
		x += 20
	if arr.all() <=50 :
		print('\n',arr,arr.mean())
	return activation(a+np.random.random(3))
for i in range(1,2):
	backwardprop(a)
	_Pillow_("Juice.jpg")
