#Max Low
#11-13-17
#middleWord.py -- finds middle if even print both

words = input('Enter some words').split()

if len(words)%2 == 0:
    print(words[len(words)//2:len(words)+1])
else:
    print(words[len(words)//2])

