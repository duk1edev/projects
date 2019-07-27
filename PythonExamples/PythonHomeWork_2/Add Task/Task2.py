import math

x = float(input("x = "))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
elif x < math.pi or x > math.pi:
    y = x
else:
    y = 0;

print("y = {}".format(y))