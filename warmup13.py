#Max Low
#11-16-17
#warmup13.py --  make a list of 20 #'s print min, max, and sum

from random import randint

number = []
for n in range(1,21):
    number.append(randint(-100,100))
print(number)

print(max(number))
print(min(number))
print(sum(number))
