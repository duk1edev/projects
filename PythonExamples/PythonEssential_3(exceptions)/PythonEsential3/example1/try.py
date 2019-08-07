print('Calculator')

#some calculaеtions



try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a/b)


except (ZeroDivisionError,ValueError) as error:
    print((error))
print('Programm working after error')