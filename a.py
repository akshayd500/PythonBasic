import numpy as np
from PIL import Image as im
'''
#for delay
from time import sleep
'''
img = im.open("b.jpeg")
print (type(img))
img = np.array(img)
print (type(img))
x, y, ch = img.shape

"""
#Re-color
for i in range(x):
	for j in  range(y):
		for k in  range(ch):
			if (i < x//4) or (i > y*3//4):
				img[i,j,k] = 0
"""




#crop in circle
for i in range(x):
	for j in  range(y):
		for k in  range(ch):
			if ((i-x//2)**2 + (j+y//2)**2) == (x//2)**2:
				img[i,j,k] = 50
		#	else:
		#		img[i,j,k] = 0
'''
#to crop image in square shape
img[:500,:120,:]=50
img[380:,:500,:]=50
img[:120,:500,:]=50
img[:500,380:,:]=50
'''
'''
print (img)
img = img * 9500
'''
img = im.fromarray(img)
img.save("abc.jpeg")
