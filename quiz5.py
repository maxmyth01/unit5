#Max Low
#12-4-17
#quiz 5.py -- 5 rand num in a list, last element of a list, number of charactures in each word, andlarges w/o using min/max

from random import randint

def rand5():
    x=0
    rand = []
    while x < 5:
        rand.append(randint(1,100))
        x+=1
    return rand

def lastElement(animals):
    return animals[len(animals)-1]
    
def wordLengths(sentance):
    new = []
    for word in sentance:
        new.append(len(word))
    return new
    
def biggest(z):
    z.sort()
    return z[len(z)-1]

print(rand5())
print(lastElement(['cat','dog','rat']))
print(wordLengths(['the','cat','is','hungry']))
print(biggest([3,-1,5,-2,7,2,1]))

