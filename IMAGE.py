import numpy as np
from PIL import Image

im = Image.open("b.jpeg")
im = np.array(im)
row , col , color = im.shape
'''
#to find red color
for i in range(row):
	for j in range(col):
		if im[i,j,0]<100:
			im[i][j]=[0,0,0]
		elif im[i,j,1]>50 or im [i,j,2]>50:
			im[i][j]=[0,0,0]

'''
for i in range(row):
	for j in range(col):
		if im[i,j,0]<80:
			im[i][j]=(im[i,j,0]//3 +  im[i,j,1]//3 + im[i,j,2]//3)
		elif im[i,j,1] > 100: 
			im[i][j]=(im[i,j,0]//3 +  im[i,j,1]//3 + im[i,j,2]//3)
		elif im[i,j,2] > 100:
			im[i][j]=(im[i,j,0]//3 +  im[i,j,1]//3 + im[i,j,2]//3)

im = Image.fromarray(im)
im.save("new.jpg")
'''im.save("red.jpg")
'''
