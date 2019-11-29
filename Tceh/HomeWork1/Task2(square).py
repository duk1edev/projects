# Square
import string

a = float(input('Enter height: '))
b = float(input('Enter width: '))

print('Square = ', a * b)
# ------------------------------------------------------------------------------

# Choose the operation

x = int(input('x =  '))
y = int(input('y = '))
sing = input('Enter the sing "+" or "-" : ')

if sing == '+':
    print('{} + {} = {}'.format(x, y, x + y))
elif sing == '-':
    print('{} - {} = {}'.format(x, y, x - y))
else:
    print('Something going wrong...')
# -------------------------------------------------------------------------------

# Simple number

n = int(input("Enter the limit number: "))

lst = []

for x in range(2, n + 1):
    for y in lst:
        if x % y == 0:
            break
    else:
        lst.append(x)
print(lst)
# -------------------------------------------------------------------------------

# numbers % 5 == 0
start = int(input('Start number: '))
end = int(input('End number: '))

for x in range(start, end + 1):
    if x % 5 == 0:
        print(x)
# -------------------------------------------------------------------------------


# ______________________________________________
keys = list(string.ascii_lowercase)

for char in keys:
    print(keys)