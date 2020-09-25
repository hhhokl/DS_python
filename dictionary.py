#A Dictionary is a collection which is unordered, changable and indexed. No duplicate members

#Create dict

person = {
    'first_name':'Denis',
    'last_name':'Lunev',
    'age':32
}

#use constructor
#person2 = dict(first_name='Denis', last_name='Lunev')

print(person, type(person))
print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555-555-55-55'
print(person)

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Kharkiv'
print(person2)

# Remove an item

del(person['age'])
person.pop('phone')


# Clear 
person.clear()
# Lenght

print(len(person2))
print(person2)

# List of dict

peoples = [
    {'name': 'Martha', 'age': 30 },
    {'name': 'John', 'age': 25}
]

print(peoples)
print(peoples[1]['name'])