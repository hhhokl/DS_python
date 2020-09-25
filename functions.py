# Create a function
def sayHello(name='hhhokl'):
    print(f'Hello {name}')


sayHello('Denis Lunev')
sayHello()

# Return values

def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(1,2))
num = getSum(5, 300)
print(num)

getSum1 = lambda num1,num2 : num1 + num2

print(getSum1(10,3))