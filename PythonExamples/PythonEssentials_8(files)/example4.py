with open(__file__) as source:
    for number, line in enumerate(source, 1):
        print(f'{number:3}| {line}', end='')