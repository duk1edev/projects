import random

numbers = random.sample(range(100), 10)

print(numbers)

numbers_filtered = list(filter(lambda x: x % 2 != 0, numbers))
print('Numbers after filter(x % 2 != 0) : ', numbers_filtered)

numbers_squares = map(lambda x: x ** 2, numbers_filtered)
print('Squares of filter numbers : ', list(numbers_squares))
