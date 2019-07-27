number = int(input("Number = "))
factorial = 1

for i in range(number,0,-1):
    factorial *= i
print("F({0}) = {1}".format(number,factorial))

print()