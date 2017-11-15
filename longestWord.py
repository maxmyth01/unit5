#Max Low
#11-13-17
#middleWord.py -- finds middle if even print both

words = input('Enter some words').split()

for w in words:
    lettercount=0
    maxletters = 0
    word=0
    for ch in word:
        lettercount += 1
    if lettercount >= maxletters:
        lettercount = maxletters
        word = w
    lettercount = 0
        
print("The longest word is", words[word])
            
        
        
