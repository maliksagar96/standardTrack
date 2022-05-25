import numpy as np 

data = np.load('/home/sagar/Documents/codes/python/myISF/fiveframes.npy')

np.savetxt('sample.txt', data)
