#def generator_function():
#    for x in range(5):
#        for y in range(3):
#            if (x + y) % 2 == 0:
#                yield x * y
#
generator = (x * y  for x in range(5) for y in range(3) if (x + y) % 2 == 0)
for g in generator:
    print(g)

print('Sum = ', sum( x**2 for x in range(10)))