def print_matrix(matrix):
    for row in matrix:
        print('_'.join(str(x) for x in row))


#matrix = [[0] * 5] * 5
matrix = [[0] * 5 for x in range (5)]  

print_matrix(matrix)

print()

matrix[1][4] = 55555
print_matrix(matrix)

