def sub_generator():
    yield '[sub_generator] hello'
    yield 'f-ck all i need is U'

def generator():
    yield 'generator'
    yield from sub_generator()
    yield from (x**2 for x in range(10))
    yield 'end'

for value in generator():
    print(value)