#Assignment 1


def check_word(word, avaible, required):
    if required not in word :
        return False
    
    if len(word) < 4:
        print('The word must have at least four letters')
        return False

    for i in word:
        if i not in avaible:
            return False

    return True

def score_word(parola, disponibile):
    t = 1 
    add = len(parola) - 4
    t += add

    parola = parola.lower()
    disponibile = disponibile.lower()

    pangram = True
    for l in parola:
        if l not in disponibile:
            pangram = False
            break
    if pangram == True:
        t += 7

    return t 



test = 'color'
test2 = 'ACDLORT'
test3= 'R'

test = test.lower()
test2 = test2.lower()
test3= test3.lower()

r1 = check_word(test, test2, test3)
print(r1)

score = score_word(test, test2)
print(score)

