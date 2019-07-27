import math

print("Calculator")

sing = input("""Choose the operation
1. +
2. -
3. *
4. /
5. **
6. sin
7. cos
8. tan
""")

if sing == "+":
    number1 = float(input("Enter the 1 number: "))
    number2 = float(input("Enter the 2 number: "))
    print("{} + {} = {}".format(number1,number2,number1 + number2))

elif sing == "-":
    number1 = float(input("Enter the 1 number: "))
    number2 = float(input("Enter the 2 number: "))
    print("{} - {} = {}".format(number1,number2,number1 - number2))

elif sing == "*":
    number1 = float(input("Enter the 1 number: "))
    number2 = float(input("Enter the 2 number: "))
    print("{} * {} = {}".format(number1,number2,number1 * number2))

elif sing == "/":
    number1 = float(input("Enter the 1 number: "))
    number2 = float(input("Enter the 2 number: "))
    if number2 > 0:
        print("{} / {} = {}".format(number1,number2,number1 / number2))
    else:
        print("Error!Try to divine by Zero")

elif sing == "**":
    number1 = float(input("Enter the number: "))
    pow = float(input("Enter the pow of number: "))
    print("{}**{} = {}".format(number1,pow,number1 ** pow))

elif sing == "sin":
    number1 = float(input("Enter the value: "))
    print("sin({})  = {}".format(number1,math.sin(number1)))

elif sing == "cos":
    number1 = float(input("Enter the value: "))
    print("cos({})  = {}".format(number1,math.cos(number1)))

elif sing == "tan":
    number1 = float(input("Enter the value: "))
    print("tan({})  = {}".format(number1,math.tan(number1)))

else:
    print("Incorrect choise!")
