def add(x, y):
    return x + y


def add_2(x):
    def do_add_2(y):
        return x + y

    return do_add_2


add_3 = lambda x, y: x + y

print(add(4, add(4, 1)))
print()
print(add_2(45)(4))
print(add_3(15, 25))
print()
print(add(5, add_3(3, 3)))
