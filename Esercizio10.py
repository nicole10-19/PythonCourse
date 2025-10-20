#Tuples 


#A tuple is a sequence of values and idexed by integers 

t = ('a', 'b', 'c', 'd')

print(type(t))


s = ('a')
print(type(s))

r = ('a', )
print(type(r))

#Most list operators also work with tuple 

t1= ('h','e', 'l')
t2= ('l', 'o')

print(t1+t2)
print(t2*4)

print(sorted(t1+t2))
#NB : tuples are immutable, there are no methods like append or remove , but they are hashable 

d = dict()

d[1,2] = 'a'
d[3,4] = 'b'

print(d)

#NB : Values are assigned to variables from left to right 
#If the left side is a tuple, the right side can be any kind of sequence 

# Functions can oly retrun a single value, but if that value is a tuple...
#quotient, reminder = divmod(x,y)
#(w,z)

#Collectiong multple arguments into a tuple 

def mean(*args):
    return sum(args) /len(args)

print(mean(1,2))
print(mean(1,2,3,4,5,6))
