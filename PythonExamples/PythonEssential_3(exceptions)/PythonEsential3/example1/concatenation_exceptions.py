a = 5
b = 0

try:
    result = a/b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from None
else:
    print('Esle block in try catch')