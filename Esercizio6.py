#Iteration 

#---Loops---

for i in range(3): #range() creates a sequence of values [0,...,n-1]
    print(i)

#Looping over a string 
word= "Earth"
def function3(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True 
    return False

print(function3(word))

#for line in open("word.txt"):
#    print(line)

f = open("word.txt")
print(f.readline())

total = 0
for line in open("word.txt"):
    total += 1

print(total)
