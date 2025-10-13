#Lists


#Sequences of value, which can be of any type 
n = [34, 56, 87543]
c = ['Hello', 'Hola', 'Ciao']

s = ['NiHao', 2.453, 7, [12, 45]]

#list indices work the same way as str indices, but they are mutable 

numbers = [89, 54]

numbers[1] = 12

print(numbers)
print(c[:])

#List operations 

# + joins two lists
# * makes multiple copies and concatenates 

#sum -->Add up the elements
#min --> Find the smallest element
#max --> Find the largest element
#sorted --> Sort the elements of a list

#List methods

#append(x) --> Add x to the end of the list
#extend(l)--> Append all the elements of l to the end of the list
#pop(i) -->Remove the i th element, and return it. If no index is specified, remove and
#       return the last element
#remove(x) -->Remove the first element from the list whose value is equal to x
