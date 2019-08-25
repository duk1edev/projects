#def add(x, y):
#    return x + y


#def sub(x, y):
#    return x - y


#def mul(x, y):
#    x * y


#def div(x, y):
#    return x / y
from operator import add, sub, mul, truediv


operations = {
    '+': add,     #lambda x, y: x + y,
    '-': sub,     #lambda x, y: x - y,
    '*': mul,     #lambda x, y: x * y,
    '/': truediv, #lambda x, y: x / y,
    '^': pow
}

try:
    first = float(input('1st num: '))
    operation = input('Operation: ')
    second = float(input('2nd num: '))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result: ', result)
