#Max Low
#11-16-17
#stringListDemo.py -- print out words that start with a vowel

words = input("Enter Some Words: ").split(" ")

for word in words:
    if word[0] in "aeiouAEIOU":
        print(word)
        

        
