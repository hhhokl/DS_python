#Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
#Single value needs trailing comma
fruits2 = ('Apple',)
#Tuple cannot be changes
#Delete tuple
del fruits2

#lenght of the tuple
print(len(fruits))


#A set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Grapes', 'Grapes'}

print(fruits_set)

#check if in set
print('Apples' in fruits_set)

#add to set
fruits_set.add('Mango')
print(fruits_set)

people = ('Pidor')
print(people, type(people))
people = ('Pidor suka',)
print(people, type(people))