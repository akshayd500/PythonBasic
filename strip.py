import numpy as np
from PIL import Image
h= np.zeros(800*800*3,dtype=np.uint8).reshape(800,800,3) 
for i in range(h.shape[0]):
	for j in range(h.shape[1]):
		if ((i//90) + (j//90)) %2 ==0:
			box = ((i//20) + (j//20)) % 8
			r , g , b = box // 4 , ( box % 4 ) // 2 , box % 2
			h[i,j,:] = np.array([r,g,b]) * 255
h=Image.fromarray(h)
h.save("chess.jpg")
