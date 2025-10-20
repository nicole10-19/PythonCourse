#Files 

import os 
print(os.getcwd())

#os --> provides functions for working with files and directories 
# getcwd() returns the current working directory 

#Others functions 
# listdir --> list the content of a directory 
# path.exists --> check whether a file or directory exists 
# path.isdir --> check whether a path refers to a directory 
# path.isfile --> check whether a path refers to a file 
# path.join --> join directories and filename into a path 


#F-Strings 

d = {'one':1}
l = [1, 2, 3]

writer = open("word.txt", "w")

writer.write(f'dict: {d}, list: {l}\n')
writer.write(f'sum list : {sum(l)}\n')
writer.close()

print(open('word.txt').read())

writer = open('word.txt', 'w')
writer.write("dict: " +str(d) + " , list: "+ str(l) +"\n")
