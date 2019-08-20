


if __name__ == '__main__':

    some_string = []
    index = len(some_string)
    while index < 10:

        some_string.append(int(input('Enter the number:')))
        index += 1
    some_string.sort()
    
    for i in some_string:
        print(i)


