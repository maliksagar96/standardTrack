import numpy as np 

for fr in range(0, 1000):

	data = np.load("linkedData"+str(fr)+".npy")

	particles = int(np.shape(np.where(data[:, 2] == data[:,2][0]))[1])
	sorted_array = np.zeros([len(data[:, 0]), 4], dtype = float)

	frames = int(data[:,2][len(data[:,2])-1] - data[:,2][0] + 1)
	firstFrame = int(data[:, 2][0])

	currentFrame = 0

	for i in range(firstFrame, frames+firstFrame):
		
		foo = data[np.where(data[:, 2] == i)]
		sorted_arr = foo[np.argsort(foo[:, 3])]

		for j in range(0, particles):
			sorted_array[j+particles*currentFrame, 0] = sorted_arr[j, 0] 
			sorted_array[j+particles*currentFrame, 1] = sorted_arr[j, 1] 
			sorted_array[j+particles*currentFrame, 2] = sorted_arr[j, 2] 	
			sorted_array[j+particles*currentFrame, 3] = sorted_arr[j, 3] 

		currentFrame += 1

	print("Sorted ",fr, "th frame")
	print("---------------------------------------")

	np.save("Link"+str(fr), sorted_array)
