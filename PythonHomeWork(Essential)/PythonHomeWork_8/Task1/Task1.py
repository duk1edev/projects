with open('../data/random_numbers.txt', 'r') as data:
    numbers = [int(line) for line in data]

print(f'Сумма всех чисел из списка = {sum(numbers)}')
