#Max Low
#11-15-17
#dictionaryDemo.py -- list practice

dictionary = ['alphbet','sweatshirt','sweatpants','shorts','computer','waterbottle']

dictionary.sort()

number = int(input('What number word do you want to look up?'))
print('Word number',number,'is', dictionary[number - 1])
