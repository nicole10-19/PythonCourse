#Dictionaries 

numbers = {}
numbers['zero'] = 0
numbers['one'] = 1
numbers['two'] = 2

print(numbers)

#Dictionaries are implemented usin hash tables 
#NB: Mutable types can be used as values but cannot be used as keys 

#This part of code make an error 
#d = {'a':1, 'b' :[1,2]}
#l = [3,4]
#d[l] = 5


#Looping 

r = {'a':1, 'b':2, 'c':3}

for i in r:
    print(i,r[i])