import random
import pickle
numbers = []


def create_numbers():
    for i in range(10000):
        numbers.append(random.randint(-100, 100))


create_numbers()

with open('../data/random_numbers.txt', 'w') as num:
    for number in numbers:
        num.write(f'{number}\n')
with open('../data/random_numbers.pkl', 'wb') as bin_file:
    for i in numbers:
        pickle.dump(i, bin_file)