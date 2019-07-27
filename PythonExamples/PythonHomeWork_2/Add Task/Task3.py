import math

print("ax2 + bx + x = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = (pow(b,2) - (4 * a * c))

if d < 0 :
    print("Уровнение не иммет действительных корней")
elif d == 0:
    x = (-b / (2 * a))
    print("x = {}".format(x))
elif d > 0 :
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)

    print("x1 = {}, x2 = {}".format(x1,x2))