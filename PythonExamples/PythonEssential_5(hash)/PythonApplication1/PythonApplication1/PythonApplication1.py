str1 = input("1:")
str2 = input("2:")

common  =set(str1) & set(str2)

print('Found ',len(common),'common char = ',common)
print('\n'.join(common))


