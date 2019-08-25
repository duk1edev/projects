from itertools import product

# for i in range(1,9):
#    for j in range(1, 9):
#        print(f'{i} * {j} = {i * j }')
#    print()

for i, j in product(range(1, 5), range(1, 5)):
    print(f'{i} * {j} = {i * j}')
