#Max Low
#12-1-17
#stat.py  -- takes several inputs then gives min, max, mean, median, mode

numbers = []

while True:
    num = input("Type a list of numbers, enter q to stop")
    if num == "q":
        break 
    numbers.append(num)
numbers.sort()
print("Max:",numbers[len(numbers)-1])
print("Min:",numbers[0])

mean = 0
for i in numbers:
    i = float(i)
    mean += i
mean = mean/len(numbers)

print("Mean:",mean)

total = 0 
for j in numbers:
   