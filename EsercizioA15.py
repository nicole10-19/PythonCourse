#Classes

#A class is a programmer-defined type 

import copy   #the copy module provides the copy function that can duplcate any object 


class Time:
	pass




lunch =Time()
dinner = copy.copy(lunch)


#deepcopy = copy the object, the objects it refers to, the objects they refer to, and so on 
print(lunch)
