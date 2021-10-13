import numpy as np 

Height=[1.73,1.80,1.76,1.89,1.65]
Weight=[65.5,57.2,65.7,88.6,70.3]

np_array_height=np.array(Height)
np_array_weight=np.array(Weight)


height_cm=Height*10

np_array_height_cm=np_array_height*100
np_array_weight_pound=np_array_weight*2.2

print(np_array_height_cm)
print(np_array_weight_pound)

#Selecting and indexing (Numby Array)
print(np_array_height[0])
print(np_array_height[0:5])

#2D Numpy Array
np_2D=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(np_2D.shape)

#Selecting and indexing (2D Numby Array)
print(np_2D[0])
print(np_2D[1,3])
print(np_2D[1,4])
print(np_2D[:,3])
print(np_2D[0,:])
print(np_2D[:,[1,2,3]])


print("Mean of heights "+str(np.mean(np_array_height)))
print("Mean of weights "+str(np.mean(np_array_weight)))

print("Median of heights "+str(np.median(np_array_height)))
print("Median of weights "+str(np.median(np_array_weight)))

print("Standard Deviation of heights "+str(np.std(np_array_height)))
print("Standard Deviation of weights "+str(np.std(np_array_weight)))
