#Extras 


#Sets--> collections of unique elements 

s = set()
print(type(s))
s = set('hello')
print(s)

#Counter--> keep track of how many times elements appear

import collections

c = collections.Counter('hello')
print(c)
print(c['l'])

#Defaultdict --> automatically generates keys that do not exist

d = collections.defaultdict(list)
print(d)

print(d['zero'])
print(d)

#Conditional expressions --> expressions that use conditionals to select one or two values 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


#or factorial implemented with a conditional expression 
#def factorial(n):
#   return 1 if n== o else n* factorial(n-1)


#List comprehensions --> concise ways to loop through a sequence and create a list 
# **Traditional loop**
# def capitalize_title(title):
#   t = []
#   for word in title.split():
#       t.append(cord.capitalize())
#   return ' '.join(t)


# **With a list comprehension**

def capitalize_title(title):
    t = [word.capitalize() for word in title.split()]
    return ' '.join(t)


