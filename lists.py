numbers = [1,2,3,4,5]

numbers2 = list((1,2,3,4,5))

print(numbers2)

fruits = ['Apples', 'Oranges', 'Avokados', 'Grapes']

print(fruits)

fruits.append('Mangos')

print(fruits)
print(fruits[1])
print(len(fruits))

fruits.remove('Grapes')
fruits.insert(1, 'Strawberries')
#Remove with pop
fruits.pop(2)
print(fruits)