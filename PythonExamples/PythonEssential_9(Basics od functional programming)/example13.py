from functools import partial


def add(x, y):
    return x + y


add_to_five = partial(add, 5)
print(add_to_five(3))
print(add_to_five(13))

print_with_comma = partial(print, sep=', ')

print_with_comma(1, 23, 1, 23, 42, 3, 234, 234)
