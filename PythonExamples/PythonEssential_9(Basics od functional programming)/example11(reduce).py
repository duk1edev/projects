from functools import reduce

values = [4, 2, -2, 3, 3, -3]

product = reduce(lambda x, y: x * y, values)

print(product)
