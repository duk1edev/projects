vowels = {'a','e','u','i','o','y'}

words = input("Str : ").split(', ')

for word in words:
    vowels.intersection_update(word.lower())

print('\n'.join(vowels))

