def add(x):
    def do_add(y):
        return x + y
    return do_add

print(add(5)(3))
add_to_fife = add(5)
print(add_to_fife(25))
print(add_to_fife(40))
