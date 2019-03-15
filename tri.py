from PIL import Image as I
import numpy as np 
#im = np.arange( 300*255*3, dtype = np.uint8 ).reshape( 300,255,3 )
#im[:,:,:]=0
#for i in range(300):
#	for j in range(255):
#		im[:,i,i//100] = j
#
img = np.arange( 800*800, dtype = np.uint8 ).reshape( 800,800 )
img[:,:]= 255
for i in range (800):
	for j in range(800):
		"""
		if(i//100)%2 == 0:
			img[i,:]=0
		elif(j//100%2)==1:
			img[:,j]=255
		"""

		if ( ( i // 100 ) + ( j // 100) ) % 2 == 0 :
			img[i,j] = 30
		else:
			img[i,j] = 255
img = I.fromarray(img)
img.save("z.jpg")
#im = I.fromarray(im)
#im.save("tri.jpg")
