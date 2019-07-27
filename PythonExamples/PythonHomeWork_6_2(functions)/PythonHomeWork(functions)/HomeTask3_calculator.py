#Calculator
import math


def add_numbers(x,y):
    return x + y

def sub_numbers(x,y):
    return x - y

def mul_numbers(x,y):
    return x * y

def div_numbers(x,y):
    if y == 0:
        print("Error.Divine by Zero")
    else:
        return x / y

def main():
    while True:
        print()
        print(
"""Calculator.Choose the action
1. +
2. -
3. *
4. /
5.Exit
 """)
        action = input("Action: ")
        if action == "1" or action == "+":
            x = float(input("x = "))
            y = float(input("y = "))
            result = add_numbers(x,y)
            print("{} + {} = {}".format(x,y,result))

        elif action == "2" or action == "-":
            x = float(input("x = "))
            y = float(input("y = "))
            result = sub_numbers(x,y)
            print("{} - {} = {}".format(x,y,result))

        elif action == "3" or action == "*":
            x = float(input("x = "))
            y = float(input("y = "))
            result = mul_numbers(x,y)
            print("{} * {} = {}".format(x,y,result))

        elif action == "4" or action == "/":
            x = float(input("x = "))
            y = float(input("y = "))
            result = div_numbers(x,y)
            print("{} / {} = {}".format(x,y,result))

        elif action == "5" or action == "exit" or action == "Exit" or action == "Q" or action == "q":
            print("Closing app...")
            break
        else:
            print("The wrong entered!Repeat again....")
    print()
main()