import pandas as pd
import numpy as np

np_array=np.array([[1,2,3,4],
                   [5,6,7,8],
                   ["9","10","11","12"]])
print(type(np_array))

np_2Darray=np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
print(np_2Darray[:,3])

np_2Darray1=np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
print(np_2Darray1[[0,2],:2])

height=[1.90,1.54,1.56,1.70,2.00,1.68]
np_array_height=np.array(height)
print(np.mean(np_array_height))
#import data from excel file 
world_population=pd.read_excel("countries.xlsx",index_col=0)

#Dimentions of the dataframe
print(world_population.shape)

#print the first 10 elements of the data 
print(world_population.head(10))

#Selecting data using Square Brackets
print(world_population[["Country Name"]])

print(world_population[["Country Name","population"]])
print(world_population[1:50])


#Selecting data using loc method
print(world_population.loc["SXM"])
print(world_population.loc[:,["population"]])
print(world_population.loc[["ABW","AND","AFG"],["Country Name"]])

#Selecting data using iloc method
print(world_population.iloc[0])
print(world_population.iloc[:,[1]])
print(world_population.iloc[[0,1,2],[0,1]])