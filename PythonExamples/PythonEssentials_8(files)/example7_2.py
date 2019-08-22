
with open('data/example7.txt', 'r') as text_file:
    numbers = [int(line) for line in text_file]
print(numbers)