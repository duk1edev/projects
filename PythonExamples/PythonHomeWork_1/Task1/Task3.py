import math

print("Квадратное уровнение : a*x`2 + bx + c = 0 ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x1 = ((-b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
x2 = ((-b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

print("X1 = {}, X2 = {}".format(x1,x2))
