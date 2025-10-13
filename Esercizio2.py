#Types, Values and expressions

# +, -, *, // integers, the result is an ineger 
#/ integers, the result is a floating-point number 

#NB: Parentheses influence the order 

a = 12 +5 *6
print(a)

b = (12+5) * 6
print(b)

#Strings 
#We an use only two operators with strings +(join two strings), *(makes multiple copies and concatenates)

c = "Well, " + "this is " + "the world"
print(c)

d= "Hello, " * 5
print(d)

#type --> returns the type of any value 
print(type(c))

#int , float and str can be used as functions to convert values 

print(int(34.89))

print(float(b))


print(str(a))