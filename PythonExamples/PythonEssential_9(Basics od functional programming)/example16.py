from itertools import takewhile, dropwhile

values = [1, 2, 3, 123, 4, 1, 23, 4]
predicate = lambda x: x < 5

for elem in takewhile(predicate, values):
    print(elem)
print()
for elem in dropwhile(predicate, values):
    print(elem)