import numpy as np
a=np.arange(5*5*3).reshape(5,5,3)
'''
for i in range(5):
	for j in range(5):
		for k in range(3):
			if a[i,j,k] % 3 == 1:
				a[i,j,k]=0
'''

print(a)
