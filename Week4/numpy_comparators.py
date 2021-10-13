import numpy as np
print("shaden">"Shaden")
print("shaden"<"Aleen")

#less than
print(4<5)
print(40<5)

#less than or equal 
print(5<=5)
#More than
print(100>5)
#More than or equal
print(100>=100)
#equal
print("shaden"=="shaden")
print("shaden"=="Shaden")
#not equal
print("shaden"!="Shaden")
print("shaden"!="shaden")
#Comprators in numpy

age=[50,15,10,20,15,32,45,16,18,17,25]
np_age=np.array(age)

print(np_age>=18)

x=np_age>=18
print(np_age[x])

print(np_age[np_age>=18])

#Boolean operators
print((2<3)and(2>5))

#Boolean operators in NumPy
y=np.logical_and(np_age>=18,np_age<=25)
print(np_age[y])