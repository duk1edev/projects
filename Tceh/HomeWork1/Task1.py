# Game puzzles

# Dictionary
# Puzzel 1: What numeric data types with floating-point  has python?
# Puzzel 2: What logic data types has python?(bool)
# Puzzel 3: Which type of data you need to use if needed put nothing to variable?(none)
# Puzzel 4: Which type of data you need to use if needed use text?(string)
# Puzzel 5: Which symbols uses  for comments?(#)
# Puzzel 6: Which function  can print text on screen?(print)
# Puzzel 7: Which function can call for user input to the program?(input)
# Puzzel 8: Which condition statement has python?(if-else)
# Puzzel 9: Which loops you can use when you write program on Python?(for)
# Puzzel 10: Can you compare string and bool types?(no )

my_dict = {
    'What numeric data types with floating-point  has python?': 'float',
    'What logic data types has python?': 'bool',
    'Which type of data you need to use if needed put nothing to variable?': 'none',
    'Which type of data you need to use if needed use text?': 'string',
    'Which symbols uses  for comments?': '#',
    'Which function  can print text on screen?': 'print',
    'Which function can call for user input to the program?': 'input',
    'Which condition statement has python?': 'if',
    'Which loops with counter you can use when you write program on Python?': 'for',
    'Can you compare string and bool types?': 'no'
}


right_answers = 0
wrong_answers = 0

print("Welcome to the game - Puzzles")

for key, value in my_dict.items():
    print(key)
    answer = input(">: ")
    if answer.lower() == value:
        right_answers = right_answers + 1
    else:
        wrong_answers = wrong_answers + 1

print('You answered for {} right and {} wrong answers!'.format(right_answers, wrong_answers))

