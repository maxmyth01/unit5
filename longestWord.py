#Max Low
#11-13-17
#middleWord.py -- finds middle if even print both

words = input('Enter some words: ').split()

for w in words:
    lettercount=0
    maxletters = 0
    maxword=0
    
    for ch in w:
        lettercount += 1
        
    if lettercount >= maxletters:
        lettercount = maxletters
        maxword = w
    lettercount = 0
print("The longest word is",maxword)
            
        
        
