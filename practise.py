#STRINGs


name = 'Brand'
age = 37

#Concatenate
print('Hello, my name is ' + name + ' and I\'m ' + str(age) + ' old')

print('Hello, my name is {name} and I\'m {age} years old'.format(name=name, age=age))

print(f'Hello, my name is {name} and I\'m {age}')

#String methods

s = 'Pipa,Meh,Fasol'
print(s, len(s))

print(s.split(','))

